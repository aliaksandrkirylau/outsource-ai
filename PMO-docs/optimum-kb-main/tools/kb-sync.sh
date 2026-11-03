#!/usr/bin/env bash
# kb-sync - the one command a person (or their agent) runs to share their work in the team KB.
#
#   bash tools/kb-sync.sh              save everything, get everyone else's work, share yours
#   bash tools/kb-sync.sh -m "text"    same, with your own commit message
#   bash tools/kb-sync.sh setup        one-time settings for this clone
#   bash tools/kb-sync.sh status       what would be synced, without doing it
#
# What it never does: force push, rebase, reset, delete branches, rewrite history, pick a winner
# when two people changed the same passage.
# When two people changed the same passage of a note, it keeps BOTH versions in a visible box,
# marks the note `status: disputed`, and still syncs, so nobody's work is lost or hidden.
# Anything else it cannot handle safely (a note deleted on one side and edited on the other, two
# renames, a merge left half-done by hand) stops before anything is shared, and says who to ask.
#
# Output lines an agent can rely on: SYNCED, NOTHING, DISPUTED <file> <other person>,
# AUTO <file> <how>, WARN <text>, STOPPED <reason>. Exit 0 = synced or nothing to do,
# 3 = stopped, needs a person; 4 = unsafe state found before starting; 5 = nothing saved, the files
# carry conflict markers or a money amount (tools/kb-money.pl).

set -u
export GIT_MERGE_AUTOEDIT=no GIT_TERMINAL_PROMPT=0 LC_ALL=C
# Real file names in git output (Cyrillic, accents), not "З..." escapes (runs/28-cross-os-before-fix.txt).
git() { command git -c core.quotepath=off "$@"; }
REMOTE=origin
top=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "STOPPED not inside the KB folder"; exit 4; }
cd "$top" || exit 4
gitdir=$(git rev-parse --git-dir)
me=$(git config user.name || true)

stop() { echo "STOPPED $1"; [ -n "${2:-}" ] && echo "  $2"; exit "${3:-3}"; }

# keep_both <file> <base> <upstream>: turn every conflict hunk (diff3 style) into a visible box
# with both versions and the text before either change. A hunk inside the frontmatter keeps the
# frontmatter as it was before either change (so it still parses) and lists both versions in a box
# right below it. The note is marked `status: disputed`.
keep_both() {
  local f=$1 base=$2 up=$3 mine other oname st_mine st_other tmp
  mine="$me: $(git log -1 --format='%ad, "%s"' --date=short "$base..HEAD" -- "$f")"
  oname=$(git log -1 --format='%an' "$base..$up" -- "$f")
  other="$oname: $(git log -1 --format='%ad, "%s"' --date=short "$base..$up" -- "$f")"
  st_mine=$(git show "HEAD:$f" | sed -n 's/^status: *//p' | head -1)
  st_other=$(git show "$up:$f" | sed -n 's/^status: *//p' | head -1)
  tmp="$gitdir/kb-sync.tmp"
  awk -v mine="$mine" -v other="$other" -v sm="$st_mine" -v so="$st_other" '
    function box(kind,   i) {
      if (kind == "fm") out[++np] = "> [!warning] kb-sync: two versions of these properties were saved at the same time. The properties above are as they were before either change. Decide, then delete this box."
      else print "> [!warning] kb-sync: two versions of this passage were saved at the same time. Decide, keep one, then delete this box."
      add(kind, ">"); add(kind, "> **" mine "**")
      for (i = 1; i <= no; i++) add(kind, "> " (kind == "fm" ? "`" o[i] "`" : o[i])); if (!no) add(kind, "> (removed)")
      add(kind, ">"); add(kind, "> **" other "**")
      for (i = 1; i <= nt; i++) add(kind, "> " (kind == "fm" ? "`" t[i] "`" : t[i])); if (!nt) add(kind, "> (removed)")
      add(kind, ">"); add(kind, "> Before either change:")
      for (i = 1; i <= nb; i++) add(kind, "> " (kind == "fm" ? "`" b[i] "`" : b[i])); if (!nb) add(kind, "> (nothing)")
      add(kind, ">"); add(kind, "> Status before: " (sm == "" ? "-" : sm) " and " (so == "" ? "-" : so))
      if (kind != "fm") print ""
    }
    function add(kind, s) { if (kind == "fm") out[++np] = s; else print s }
    st == 0 && /^<<<<<<< / { st = 1; no = nt = nb = 0; next }
    st == 1 && /^\|\|\|\|\|\|\| / { st = 2; next }
    (st == 1 || st == 2) && /^=======$/ { st = 3; next }
    st == 3 && /^>>>>>>> / {
      st = 0
      if (fm == 1) { for (i = 1; i <= nb; i++) print b[i]; box("fm") } else box("body")
      next
    }
    st == 1 { o[++no] = $0; next }
    st == 2 { b[++nb] = $0; next }
    st == 3 { t[++nt] = $0; next }
    NR == 1 && $0 == "---" { fm = 1; print; next }
    fm == 1 && $0 == "---" { fm = 2; print; if (np) { print ""; for (i = 1; i <= np; i++) print out[i] }; next }
    { print }' "$f" > "$tmp" && mv "$tmp" "$f"
  # mark the note disputed (first status: line inside the frontmatter)
  perl -0pi -e 's/\A(---\n(?:(?!---\n).*\n)*?)status:[^\n]*\n/${1}status: disputed\n/' "$f"
  git add -- "$f"
  echo "DISPUTED $f $oname"
}

# resolve_all <base> <upstream>: called with a merge stopped on conflicts. Resolves what is safe,
# or aborts the merge and stops if anything is not.
resolve_all() {
  local base=$1 up=$2 f stages bad= disputed= regen=no list
  list=$(git diff --name-only --diff-filter=U)
  # pass 1: can every conflicted file be handled?
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    stages=$(git ls-files -u -- "$f" | awk '{print $3}' | sort -u | tr -d '\n')
    case "$f:$stages" in
      index.md:*|log.md:123|log.md:23) ;;
      *.md:123|*.md:23) ;;
      *) bad="$bad $f" ;;
    esac
  done <<EOF
$list
EOF
  if [ -n "$bad" ]; then
    git merge --abort
    echo "STOPPED someone else changed the same files in a way kb-sync will not merge on its own:$bad"
    echo "  (a note deleted on one side and edited on the other, a double rename, or a non-note file)"
    echo "  Your work is saved locally and NOT shared yet. Nothing of anyone's was changed. Ask the curator."
    return 1
  fi
  # pass 2: resolve
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    stages=$(git ls-files -u -- "$f" | awk '{print $3}' | sort -u | tr -d '\n')
    case "$f:$stages" in
      index.md:*) regen=yes ;;
      log.md:*)
        git show ":2:$f" > "$gitdir/kb-o"; git show ":3:$f" > "$gitdir/kb-t"
        { git show ":1:$f" 2>/dev/null || true; } > "$gitdir/kb-b"
        git merge-file --union "$gitdir/kb-o" "$gitdir/kb-b" "$gitdir/kb-t"
        cp "$gitdir/kb-o" "$f"; rm -f "$gitdir"/kb-[obt]; git add -- "$f"; echo "AUTO $f kept both sides' lines" ;;
      *:23)
        # two people created the same note: theirs keeps the name (already shared), yours is renamed
        alt="${f%.md}.$(echo "$me" | tr -c 'A-Za-z0-9\n' '-').md"
        git show ":2:$f" > "$alt"; git show ":3:$f" > "$f"; git add -- "$f" "$alt"
        echo "DISPUTED $f $(git log -1 --format=%an "$up" -- "$f") (you both created it; yours is now $alt)"
        disputed=yes ;;
      *) keep_both "$f" "$base" "$up"; disputed=yes ;;
    esac
  done <<EOF
$list
EOF
  if [ -f tools/gen-index.sh ] && { [ $regen = yes ] || [ -n "$disputed" ]; }; then
    sh tools/gen-index.sh && git add index.md && echo "AUTO index.md regenerated"
  fi
  if git diff --cached -U0 | grep -qE '^\+(<{7}|>{7}|={7}$)'; then
    git merge --abort; echo "STOPPED conflict markers survived the merge - nothing shared. Ask the curator."; return 1
  fi
  git commit -q --no-edit -m "kb-sync: merged $up${disputed:+; both versions kept where edits overlapped}" || { git merge --abort; echo "STOPPED could not save the merge"; return 1; }
  [ -n "$disputed" ] && echo "  Both versions are kept (see DISPUTED above). Decide with the other person which one stands."
  return 0
}

cmd=sync; msg=
case "${1:-}" in
  setup|status) cmd=$1 ;;
  -m) msg=${2:-} ;;
  "") ;;
  *) echo "usage: kb-sync.sh [setup | status | -m message]"; exit 2 ;;
esac

if [ "$cmd" = setup ]; then
  [ -n "$me" ] || stop "no name set for your commits" 'run once: git config user.name "Your Name"' 4
  git config pull.rebase false
  git config merge.conflictStyle diff3
  [ -d tools/hooks ] && git config core.hooksPath tools/hooks
  [ -f .gitattributes ] || echo "WARN no .gitattributes in the repo - ask the curator (line endings)"
  echo "SETUP done for $me: merge (never rebase), diff3 conflict style, hooks from tools/hooks"
  exit 0
fi

# 1. Refuse to start from a half-finished state somebody left by hand.
[ -f "$gitdir/MERGE_HEAD" ] && stop "a merge was left unfinished in this folder" "ask the curator; 'git merge --abort' returns to your last saved state" 4
{ [ -d "$gitdir/rebase-merge" ] || [ -d "$gitdir/rebase-apply" ]; } && stop "a rebase was left unfinished in this folder" "ask the curator; 'git rebase --abort' returns to your last saved state" 4
branch=$(git symbolic-ref --short -q HEAD) || stop "not on a branch (detached HEAD)" "ask the curator" 4
# The KB lives on one branch. A side branch (a git worktree an agent app made, a stray checkout)
# would be pushed as a new branch and nobody would see the work.
[ "$branch" = "${KB_BRANCH:-main}" ] || stop "this folder is on branch '$branch'; the KB shares only ${KB_BRANCH:-main}" "your work is saved on this branch - ask the curator to bring it over" 4
[ -n "$(git ls-files -u)" ] && stop "files are still marked as conflicted" "ask the curator" 4
[ -n "$me" ] || stop "no name set for your commits" 'run once: git config user.name "Your Name"' 4

# Case-only renames (ecd.md -> ECD.md): Windows and macOS ignore case, so git does not see them and
# would keep the old name for everyone else (runs/28-cross-os.txt). Record them. Only on disks that
# ignore case, where two names differing only by case cannot both exist. File names, not folders.
if [ "$(git config core.ignorecase || true)" = true ]; then
  git ls-files -z | perl -0ne 'chomp; my ($d, $b) = m{^(.*/)?([^/]+)$}; $d = "" unless defined $d;
    my $dir = $d eq "" ? "." : $d;
    unless (exists $ls{$dir}) { $ls{$dir} = {}; if (opendir(my $h, $dir)) { $ls{$dir}{lc $_} = $_ for readdir $h; closedir $h } }
    my $disk = $ls{$dir}{lc $b}; print "$_\0$d$disk\0" if defined $disk && $disk ne $b' |
  while IFS= read -r -d '' old && IFS= read -r -d '' new; do
    git mv -f -- "$old" "$new" && echo "AUTO recorded rename $old -> $new (case only)"
  done
fi

# 2. What changed locally, and is any of it outside this person's area (warn only).
changes=$(git status --porcelain --untracked-files=all)
territory=$(git config kb.territory || true)
if [ -n "$changes" ] && [ -n "$territory" ]; then
  echo "$changes" | cut -c4- | sed 's/.* -> //' | while read -r f; do
    case "$f" in log.md|index.md) continue ;; esac
    ok=no; for t in $territory; do case "$f" in "$t"*) ok=yes ;; esac; done
    [ $ok = no ] && echo "WARN $f is outside your area ($territory) - make sure its owner knows"
  done
fi
# A stored source changed or deleted (warn only): sources are never edited (AGENTS.md rule 1).
# New files (an ingest) are not listed; overviews, minutes and the folder notes are ours to update.
# Obsidian rewrites a whole table when a cell is typed in, so this catches accidents too.
git diff -z --name-only --diff-filter=MDT HEAD -- sources/ | while IFS= read -r -d '' f; do
  case "$f" in
    *" - overview.md"|*" - minutes.md"|*" - minutes "*.md|*/AGENTS.md) ;;
    *) echo "WARN $f is a stored source and was changed - sources are never edited (AGENTS.md rule 1); unless you swapped a placeholder for a link, tell the curator" ;;
  esac
done
if [ "$cmd" = status ]; then
  [ -n "$changes" ] && { echo "Would save:"; echo "$changes"; } || echo "Nothing to save locally."
  git fetch -q "$REMOTE" 2>/dev/null && echo "Others' new commits: $(git rev-list --count "HEAD..$REMOTE/$branch" 2>/dev/null || echo ?)"
  exit 0
fi

# 3. Save local work as one commit, refusing to save conflict markers.
if [ -n "$changes" ]; then
  git add -A
  if git diff --cached -U0 | grep -qE '^\+(<{7}|>{7}|={7}$)'; then
    git reset -q
    stop "your files contain conflict markers (<<<<<<< / >>>>>>>) - nothing was saved" "$(git grep -lE '^(<{7}|>{7}) ' -- '*.md' | head -5 | tr '\n' ' ')" 5
  fi
  # A PDF comes in only as a client-material original under sources/client/, 5 MB at most
  # (procedures/ingest.md step 2): kb-money cannot read it, and once pushed it stays in the history.
  pdfs=$(git diff --cached --name-only --diff-filter=AM -z | while IFS= read -r -d '' f; do
    case "$f" in *.[pP][dD][fF]) ;; *) continue ;; esac
    s=$(git cat-file -s ":$f" 2>/dev/null || echo 0)
    case "$f" in sources/client/*/*) [ "$s" -le 5242880 ] && continue ;; esac
    printf '%s (%s KB) ' "$f" $((s / 1024))
  done)
  if [ -n "$pdfs" ]; then
    git reset -q
    stop "a PDF outside sources/client/ or over 5 MB - nothing was saved. Large originals stay in Drive" "$pdfs" 5
  fi
  # No money amount leaves this computer: once pushed it stays in the shared history.
  if [ -f tools/kb-money.pl ]; then
    money=$(perl tools/kb-money.pl --staged); mrc=$?
    echo "$money" | sed -n 's/^MONEY? \(.*\)/WARN may be a money amount, check it is not a figure: \1/p'
    if [ $mrc = 1 ]; then
      git reset -q
      stop "a money amount in your files - nothing was saved. Record the fact, not the figure" "$(echo "$money" | sed -n 's/^MONEY //p' | head -5 | tr '\n' ' ')" 5
    fi
    [ $mrc = 2 ] && echo "WARN the money check could not run (perl or tools/money-patterns.txt missing) - ask the curator"
    export KB_MONEY_CHECKED=1   # the pre-commit hook need not repeat it
  fi
  files=$(git diff --cached --name-only | head -3 | tr '\n' ',' | sed 's/,$//; s/,/, /g')
  n=$(git diff --cached --name-only | wc -l | tr -d ' ')
  git commit -q -m "${msg:-$me: $n file(s) - $files}" || stop "could not save (commit failed)" "see the message above" 3
fi

# 4. Get everyone else's work, share ours; retry if someone pushed in between.
for attempt in 1 2 3; do
  git fetch -q "$REMOTE" || stop "cannot reach the shared repo" "check the network or sign-in; nothing was lost, run sync again later" 3
  up="$REMOTE/$branch"
  git rev-parse -q --verify "$up" >/dev/null || { git push -q -u "$REMOTE" "$branch" && echo "SYNCED (new branch $branch)"; exit 0; }
  if git merge-base --is-ancestor "$up" HEAD; then
    [ "$(git rev-parse HEAD)" = "$(git rev-parse "$up")" ] && { echo "NOTHING to sync - you are up to date"; exit 0; }
  elif git merge-base --is-ancestor HEAD "$up"; then
    git merge -q --ff-only "$up" || stop "could not update your files" "a local file is in the way; ask the curator" 3
    echo "SYNCED - got $(git rev-list --count "ORIG_HEAD..HEAD") new commit(s) from others, nothing of yours to share"; exit 0
  else
    base=$(git merge-base HEAD "$up")
    if ! out=$(git -c merge.conflictStyle=diff3 merge -q --no-ff --no-edit "$up" 2>&1); then
      [ -f "$gitdir/MERGE_HEAD" ] || stop "could not merge others' work - nothing shared" "$(echo "$out" | head -3)" 3
      resolve_all "$base" "$up" || exit 3
    fi
  fi
  if git push -q "$REMOTE" "HEAD:$branch" 2>/dev/null; then
    echo "SYNCED"; exit 0
  fi
  echo "  someone shared at the same moment - trying again ($attempt)"
done
stop "could not share after 3 tries" "your work is saved locally; run sync again in a minute" 3
