#!/usr/bin/env bash
# kb-doctor - is this computer set up for the team KB? Says what is fine and what to fix.
#
#   bash tools/kb-doctor.sh         check only, changes nothing
#   bash tools/kb-doctor.sh --fix   also apply the safe local git settings (same as kb-sync.sh setup)
#
# Output: OK, FIX (something to do, and how), WARN (works, worth knowing), INFO.
# Exit 0 when nothing needs fixing, 1 otherwise.
# It reads local files and asks the server for its branch list. It never prints, stores or asks
# for a password or token; signing in is always the person's own step.

set -u
mode=${1:-}
export GIT_TERMINAL_PROMPT=0 GCM_INTERACTIVE=never LC_ALL=C
export GIT_SSH_COMMAND="${GIT_SSH_COMMAND:-ssh -o BatchMode=yes -o ConnectTimeout=10}"
git() { command git -c core.quotepath=off "$@"; }   # real file names, not escapes
nfix=0
ok()   { echo "OK    $1"; }
fix()  { echo "FIX   $1"; [ -n "${2:-}" ] && echo "        -> $2"; nfix=$((nfix + 1)); }
warn() { echo "WARN  $1"; [ -n "${2:-}" ] && echo "        -> $2"; }
info() { echo "INFO  $1"; }
trim() { printf '%s' "$1" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'; }
json() { perl -MJSON::PP -e "$1" "${@:2}" 2>/dev/null; }   # perl ships with Git for Windows and macOS

echo "== git"
command -v git >/dev/null || { fix "git is not installed" "install Git for Windows (default options are fine) or git on Mac"; exit 1; }
ver=$(git --version | sed 's/^[^0-9]*\([0-9]*\)\.\([0-9]*\).*/\1 \2/')
set -- $ver
if [ "$1" -gt 2 ] || { [ "$1" -eq 2 ] && [ "$2" -ge 30 ]; }; then ok "git $1.$2"; else fix "git $1.$2 is too old" "update git to 2.30 or newer"; fi
top=$(git rev-parse --show-toplevel 2>/dev/null) || { fix "not inside the KB folder" "open a terminal in the KB folder and run this again"; exit 1; }
cd "$top" || exit 1
gitdir=$(git rev-parse --git-dir)
[ -f tools/kb-sync.sh ] || { fix "this folder has no tools/kb-sync.sh - is it the team KB?" "ask the curator for the right folder"; exit 1; }
ok "KB folder: $top"

name=$(git config user.name || true); email=$(git config user.email || true)
if [ -n "$name" ] && [ -n "$email" ]; then ok "commits are signed as $name <$email>"
else fix "no name or email for your commits" 'git config --global user.name "Your Name"  and  git config --global user.email "you@innowise.com"'; fi

setup_ok=yes
[ "$(git config pull.rebase || true)" = false ] || setup_ok=no
[ "$(git config merge.conflictStyle || true)" = diff3 ] || setup_ok=no
[ -d tools/hooks ] && { [ "$(git config core.hooksPath || true)" = tools/hooks ] || setup_ok=no; }
if [ $setup_ok = yes ]; then ok "sync settings applied (merge, diff3, conflict-marker hook)"
elif [ "$mode" = --fix ]; then bash tools/kb-sync.sh setup | sed 's/^/        /'; ok "sync settings applied now"
else fix "sync settings not applied yet" "bash tools/kb-sync.sh setup   (or run this check with --fix)"; fi

echo "== files"
if [ -f .gitattributes ] && [ "$(git check-attr eol -- log.md | sed 's/.*: //')" = lf ]; then ok "line-ending rules in effect (LF)"
else fix "no line-ending rules (.gitattributes) in effect" "ask the curator - this must be in the repo's first commit"; fi
ncrlf=$(git ls-files --eol 2>/dev/null | awk '$2 == "w/crlf" && /eol=lf/' | wc -l | tr -d ' ')
if [ "$ncrlf" = 0 ]; then ok "no Windows line endings on disk"
else fix "$ncrlf file(s) on disk still have Windows line endings (lint and diffs will be noisy)" "sync your work first, then ask the curator to refresh your copy"; fi
info "core.autocrlf = $(git config core.autocrlf || echo unset) (does not matter while the LF rule is in effect)"

if [ -f "$gitdir/MERGE_HEAD" ] || [ -d "$gitdir/rebase-merge" ] || [ -d "$gitdir/rebase-apply" ]; then
  fix "a merge or rebase was left half-done in this folder" "ask the curator; do not sync until it is cleared"
elif [ -n "$(git ls-files -u)" ]; then fix "files are still marked as conflicted" "ask the curator"
else ok "no half-finished merge or rebase"; fi
marked=$(git grep -lE '^(<{7}|>{7}) ' -- '*.md' 2>/dev/null | head -5 | tr '\n' ' ')
if [ -z "$marked" ]; then ok "no conflict markers in notes"; else fix "conflict markers in: $marked" "open the note, keep the right text, delete the <<<<<<< ======= >>>>>>> lines; or ask the curator"; fi

# Windows: a full path over 260 characters fails with "Filename too long" unless core.longpaths is on
# (runs/29-*). Folder of the clone + the longest note path in the repo.
case "$(uname -s 2>/dev/null)" in MINGW*|MSYS*|CYGWIN*)
  longest=$(git ls-files | awk '{ if (length($0) > m) m = length($0) } END { print m + 0 }')
  total=$(( ${#top} + 1 + longest ))
  if [ "$(git config core.longpaths || true)" = true ]; then ok "long paths allowed (core.longpaths); longest here is $total characters"
  elif [ "$total" -gt 240 ]; then fix "paths reach $total characters here; Windows stops at 260" "git config --global core.longpaths true   (or clone into a short folder such as C:\\kb)"
  else ok "paths up to $total characters here (Windows limit 260)"; fi ;;
esac

echo "== shared repo"
url=$(git remote get-url origin 2>/dev/null || true)
if [ -z "$url" ]; then fix "no shared repo (origin) configured" "ask the curator for the clone link"
else
  shown=$(echo "$url" | sed -E 's#^(https?://)[^@/]*@#\1#')   # never echo credentials embedded in a URL
  case "$url" in
    http*) info "server: $shown (HTTPS, credential helper: $(git config credential.helper || echo none))" ;;
    *@*:*|ssh://*) info "server: $shown (SSH)" ;;
    *) info "server: $shown" ;;
  esac
  branch=$(git symbolic-ref --short -q HEAD || echo main)
  if git ls-remote --heads origin "$branch" >/dev/null 2>&1; then ok "server reachable and you are signed in"
  else fix "cannot reach the server, or not signed in yet" "sign in once yourself: run bash tools/kb-sync.sh and complete the Git Credential Manager window (HTTPS) or add your SSH key; nobody else types your password"; fi
  nlocal=$(git status --porcelain | wc -l | tr -d ' ')
  nahead=$(git rev-list --count "origin/$branch..HEAD" 2>/dev/null || echo 0)
  if [ "$nlocal" = 0 ] && [ "$nahead" = 0 ]; then ok "nothing waiting to be shared"
  else info "$nlocal changed file(s) not saved yet, $nahead commit(s) not shared yet - say sync, or run kb-sync"; fi
fi

echo "== Obsidian"
if [ ! -d .obsidian ]; then info "no .obsidian folder - fine if you read the KB in an IDE"
else
  if [ -f .obsidian/app.json ]; then
    links=$(json 'local $/; open F, "<", $ARGV[0]; my $j = decode_json(<F>); print join(",", map { my $v = $j->{$_}; ref $v ? ($v ? "true" : "false") : (defined $v ? $v : "unset") } qw(useMarkdownLinks newLinkFormat alwaysUpdateLinks))' .obsidian/app.json)
    case "$links" in
      false,shortest,true|unset,shortest,true) ok "link settings: wikilinks, shortest names, update on rename" ;;
      *) fix "link settings are not the team's ($links)" "Obsidian: Settings > Files and links: Use [[Wikilinks]] ON, New link format = Shortest path when possible, Automatically update internal links ON" ;;
    esac
    git diff --quiet -- .obsidian/app.json 2>/dev/null || warn "you changed the shared .obsidian/app.json" "kb-sync would share that change with everyone; ask the curator first"
  fi
  git check-ignore -q .obsidian/workspace.json || fix "Obsidian workspace files are not ignored (they cause conflicts nobody wrote)" "ask the curator to update .gitignore"
  if [ ! -f .obsidian/workspace.json ]; then info "Obsidian has not opened this folder yet - open it: vault switcher > Open folder as vault"
  elif [ -f tools/obsidian-plugins.txt ]; then
    enabled=$(json 'local $/; open F, "<", $ARGV[0]; print join("\n", @{ decode_json(<F>) })' .obsidian/community-plugins.json)
    listed=" "
    while IFS='|' read -r id pname level why; do
      id=$(trim "$id"); [ -z "$id" ] && continue; case "$id" in \#*) continue ;; esac
      pname=$(trim "$pname"); level=$(trim "$level"); why=$(trim "$why"); listed="$listed$id "
      m=".obsidian/plugins/$id/manifest.json"
      if [ -f "$m" ] && echo "$enabled" | grep -qx "$id"; then ok "plugin $pname $(json 'local $/; open F, "<", $ARGV[0]; print decode_json(<F>)->{version}' "$m") installed and on"
      elif [ -f "$m" ]; then fix "plugin $pname is installed but switched off" "Obsidian: Settings > Community plugins > turn on $pname"
      elif [ "$level" = recommended ]; then fix "plugin $pname is missing - $why" "Obsidian: Settings > Community plugins > Browse > \"$pname\" > Install > Enable  (https://community.obsidian.md/plugins/$id)"
      else info "optional plugin $pname not installed - $why (https://community.obsidian.md/plugins/$id)"; fi
    done < tools/obsidian-plugins.txt
    # A loop, not $( ... ): bash 3.2 (macOS) cannot parse a case pattern's ")" inside $( ... ).
    others=
    for d in .obsidian/plugins/*/; do
      [ -d "$d" ] || continue; b=$(basename "$d")
      case "$listed" in *" $b "*) ;; *) others="$others$b " ;; esac
    done
    [ -n "$others" ] && info "your own plugins, not shared with the team: $others"
  fi
fi

echo "== AI agent"
found=no
if command -v claude >/dev/null 2>&1 || [ -n "${KB_DOCTOR_CLAUDE_JSON:-}" ]; then
  found=yes
  [ -f .claude/settings.json ] || warn "the repo has no .claude/settings.json" "ask the curator"
  # Claude Code keeps workspace trust in ~/.claude.json, keyed by folder path. Only that one flag is
  # read, for this folder and its parents (inference: trusting a parent covers the children).
  cj="${KB_DOCTOR_CLAUDE_JSON:-$HOME/.claude.json}"
  t=$(json 'local $/; open F, "<", $ARGV[0]; my $p = decode_json(<F>)->{projects} || {}; my $d = $ARGV[1];
            while (length $d) { if (($p->{$d} || {})->{hasTrustDialogAccepted}) { print $d; exit } last unless $d =~ s{/[^/]*$}{} }' "$cj" "$top")
  if [ -n "$t" ]; then ok "Claude Code trusts this folder${t:+ (via $t)}, so the team's permission settings apply"
  else fix "Claude Code has not been trusted in this folder yet - until then it ignores the team's permission settings" "open Claude Code in this folder once (terminal: claude, or the desktop app) and accept the trust prompt"; fi
fi
if command -v codex >/dev/null 2>&1; then
  found=yes; info "Codex found: mark this project as trusted when it asks; each sync may need your approval (not tested here)"
fi
[ $found = no ] && info "no AI agent found - sync with sync-kb.cmd (Windows) or bash tools/kb-sync.sh"

echo
if [ $nfix = 0 ]; then echo "kb-doctor: all set"; exit 0; fi
echo "kb-doctor: $nfix thing(s) to fix above"; exit 1
