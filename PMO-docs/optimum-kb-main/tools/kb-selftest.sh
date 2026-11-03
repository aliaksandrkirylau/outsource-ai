#!/usr/bin/env bash
# kb-selftest - does kb-sync work on THIS computer (its OS, git, bash, awk, perl)?
# Builds a throwaway server and two clones at a temp folder, runs the cases that matter, prints
# PASS/FAIL, deletes the temp folder. Touches nothing else, needs no network.
#   bash tools/kb-selftest.sh
set -u
here=$(cd "$(dirname "$0")" && pwd)
[ -f "$here/kb-sync.sh" ] || { echo "no kb-sync.sh next to this script"; exit 2; }
T=$(mktemp -d 2>/dev/null || mktemp -d -t kbselftest) || exit 2
trap 'rm -rf "$T"' EXIT
export GIT_MERGE_AUTOEDIT=no GIT_TERMINAL_PROMPT=0
git() { command git -c core.quotepath=off "$@"; }
pass=0; fail=0
check() { if eval "$2"; then echo "PASS  $1"; pass=$((pass + 1)); else echo "FAIL  $1"; fail=$((fail + 1)); fi; }
at() { local d=$1; shift; ( cd "$T/$d" && "$@" ); }
sync() { local d=$1; shift; ( cd "$T/$d" && bash tools/kb-sync.sh "$@" ) > "$T/out" 2>&1; echo $? > "$T/rc"; }
out() { grep -q "$1" "$T/out"; }
rc() { [ "$(cat "$T/rc")" = "$1" ]; }
server_head() { git -C "$T/server.git" rev-parse main; }
D=knowledge/decisions/DEC-001.md
U="ba/Заметка воркшопа.md"
SR="sources/meetings/x/2026-01-01 Call - rendering.md"; SO="sources/meetings/x/2026-01-01 Call - overview.md"

echo "== environment"
echo "os:   $(uname -s 2>/dev/null) $(uname -r 2>/dev/null)"
echo "bash: $BASH_VERSION"
echo "git:  $(command git --version)"
echo "awk:  $( (awk --version 2>/dev/null || awk -W version 2>/dev/null) | head -1)"
echo "perl: $(perl -e 'print $^V' 2>/dev/null || echo MISSING)"
echo "case: $(t=$(mktemp -d 2>/dev/null || mktemp -d -t kbcase); touch "$t/a"; [ -e "$t/A" ] && echo insensitive || echo sensitive; rm -rf "$t")"
echo "== cases"

# the throwaway team repo
git init -q --bare "$T/server.git"; git -C "$T/server.git" symbolic-ref HEAD refs/heads/main
git -C "$T/server.git" config receive.denyNonFastForwards true
git clone -q "$T/server.git" "$T/a" 2>/dev/null
at a git checkout -q -b main
mkdir -p "$T/a/tools/hooks" "$T/a/knowledge/decisions" "$T/a/ba" "$T/a/sources/meetings/x"
cp "$here/kb-sync.sh" "$T/a/tools/"; [ -d "$here/hooks" ] && cp "$here"/hooks/* "$T/a/tools/hooks/"
for f in kb-money.pl money-patterns.txt money-samples.txt; do [ -f "$here/$f" ] && cp "$here/$f" "$T/a/tools/"; done
printf '* text=auto eol=lf\nlog.md merge=union\n' > "$T/a/.gitattributes"
printf -- '---\ntype: decision\nid: DEC-001\nstatus: proposed\n---\n\n# DEC-001\n\n## Decision\n\nUse SSO with a 12-hour session.\n\n## Notes\n\n- none\n' > "$T/a/$D"
printf -- '---\ntype: meeting\nstatus: draft\n---\n\n# Workshop\n\n- window: 12 hours\n' > "$T/a/$U"
printf '# Log\n\n- seed\n' > "$T/a/log.md"
printf -- '- a\n' > "$T/a/ba/notes.md"
printf '| who | said |\n|---|---|\n| A | yes |\n' > "$T/a/$SR"; printf -- '- result: open\n' > "$T/a/$SO"
at a git add -A; at a git -c user.name=seed -c user.email=seed@test commit -q -m seed; at a git push -q -u origin main 2>/dev/null
git clone -q "$T/server.git" "$T/b" 2>/dev/null
for c in a b; do at $c git config user.name "$c"; at $c git config user.email "$c@test"; at $c bash tools/kb-sync.sh setup >/dev/null; done

t0=$(date +%s)
echo "- a line" >> "$T/a/ba/notes.md"; sync a
check "plain sync shares work" 'rc 0 && out SYNCED'
sync b
check "the other clone receives it" 'rc 0 && grep -q "a line" "$T/b/ba/notes.md"'
t1=$(date +%s)
check "LF on disk in a fresh clone" '! at b git ls-files --eol | grep -q "w/crlf"'

perl -pi -e 's/12-hour/8-hour/' "$T/a/$D"; sync a
perl -pi -e 's/12-hour/24-hour/' "$T/b/$D"; sync b
check "same line -> DISPUTED, both kept, still synced" 'rc 0 && out DISPUTED && out SYNCED && grep -q "8-hour" "$T/b/$D" && grep -q "24-hour" "$T/b/$D" && grep -q "^status: disputed" "$T/b/$D"'
check "no conflict markers left" '! grep -qE "^(<<<<<<<|>>>>>>>) " "$T/b/$D"'

sync a
perl -pi -e 's/^status: disputed/status: accepted/' "$T/a/$D"; sync a
perl -pi -e 's/^status: disputed/status: superseded/' "$T/b/$D"; sync b
check "frontmatter clash -> one status line, YAML kept valid" 'rc 0 && [ "$(sed -n "2,/^---\$/p" "$T/b/$D" | grep -c "^status:")" = 1 ] && grep -q "^status: disputed" "$T/b/$D"'

sync a; echo "- from a" >> "$T/a/log.md"; sync a
echo "- from b" >> "$T/b/log.md"; sync b
check "both append to log.md -> both lines" 'rc 0 && grep -q "from a" "$T/b/log.md" && grep -q "from b" "$T/b/log.md"'

sync a
perl -pi -e 's/12 hours/10 hours/' "$T/a/$U"; sync a
perl -pi -e 's/12 hours/24 hours/' "$T/b/$U"; sync b
check "non-ASCII file name with spaces -> DISPUTED, not a false stop" 'rc 0 && out DISPUTED'

sync a; at a git rm -q ba/notes.md; sync a -m "remove notes"
echo "- b edit" >> "$T/b/ba/notes.md"; before=$(server_head); sync b
check "delete vs edit -> STOPPED, nothing shared" 'rc 3 && out STOPPED && [ "$(server_head)" = "$before" ]'
at b git reset -q --hard origin/main 2>/dev/null; at b git fetch -q

printf '<<<<<<< HEAD\nx\n=======\ny\n>>>>>>> z\n' >> "$T/b/log.md"; sync b
check "conflict markers in a file -> refused" 'rc 5'
at b git checkout -q -- log.md

if [ -f "$here/kb-money.pl" ]; then
  check "money rules land on their samples" 'perl "$here/kb-money.pl" --samples >/dev/null'
  M="ba/Money check.md"
  sync b; before=$(server_head)
  printf -- '- agreed price USD 12,000\n' > "$T/b/$M"; sync b
  check "money amount -> refused, nothing saved or shared" 'rc 5 && out STOPPED && [ "$(server_head)" = "$before" ] && [ -n "$(at b git status --porcelain)" ]'
  rm -f "$T/b/$M"
  printf -- '- the warranty is unpriced; budget 150 тыс\n' > "$T/b/$M"; sync b
  check "possible amount -> WARN, still synced" 'rc 0 && out "WARN may be a money amount" && out SYNCED'
  printf -- '- price USD 9,000\n' >> "$T/b/$M"; at b git add -A; before=$(at b git rev-parse HEAD)
  at b git commit -qm "outside kb-sync" 2>/dev/null
  check "commit outside kb-sync with an amount -> hook refuses" '[ "$(at b git rev-parse HEAD)" = "$before" ]'
  at b git reset -q; at b git checkout -q -- "$M"
  P=pm/prototypes/x; mkdir -p "$T/b/$P"
  printf 's=s.replace(re,"$1")\n' > "$T/b/$P/support.js"; sync b
  check "prototype runtime .js under pm/prototypes/ -> not screened, synced" 'rc 0 && out SYNCED'
  printf '<p>price $500</p>\n' > "$T/b/$P/Main.dc.html"; sync b
  check "amount in a prototype page -> still refused" 'rc 5 && out STOPPED'
  rm -f "$T/b/$P/Main.dc.html"
  CD="sources/client/x/2026-01-01 Sample - rendering.md"; mkdir -p "$T/b/sources/client/x"
  printf -- '---\ntype: source\nkind: rendering\nmoney: client-domain\n---\n\n| BARITE | unit price USD 12,500.00 |\n' > "$T/b/$CD"; sync b
  check "client figures in a flagged sources/client/ rendering -> not screened, synced" 'rc 0 && out SYNCED'
  F2="sources/meetings/x/2026-01-02 Call - rendering.md"
  printf -- '---\ntype: source\nkind: rendering\nmoney: client-domain\n---\n\n- agreed price USD 12,000\n' > "$T/b/$F2"; sync b
  check "the same flag outside sources/client/ -> still refused" 'rc 5 && out STOPPED'
  rm -f "$T/b/$F2"
fi

mkdir -p "$T/b/sources/client/x"
head -c 4096 /dev/urandom > "$T/b/sources/client/x/2026-01-01 Sample - original.pdf"; sync b
check "client-material PDF under sources/client/ -> synced, bytes kept" 'rc 0 && out SYNCED && [ "$(at b git cat-file -s "HEAD:sources/client/x/2026-01-01 Sample - original.pdf")" = 4096 ]'
head -c 4096 /dev/urandom > "$T/b/ba/notes.pdf"; sync b
check "PDF outside sources/client/ -> refused" 'rc 5 && out STOPPED'
rm -f "$T/b/ba/notes.pdf"
head -c 5300000 /dev/urandom > "$T/b/sources/client/x/big.pdf"; sync b
check "PDF over 5 MB -> refused" 'rc 5 && out STOPPED'
rm -f "$T/b/sources/client/x/big.pdf"

sync b
echo "- result: done" >> "$T/b/$SO"; printf -- '- new\n' > "$T/b/sources/meetings/x/2026-02-02 New - rendering.md"; sync b
check "overview updated, new source added -> no source warning" 'rc 0 && out SYNCED && ! out "stored source"'
perl -pi -e 's/\|---\|---\|/| --- | ---- |/' "$T/b/$SR"; sync b
check "stored source changed -> WARN, still synced" 'rc 0 && out "WARN $SR is a stored source" && out SYNCED'

sync b; echo "- a2" >> "$T/a/log.md"; sync a                     # the server moves on
echo "- b" >> "$T/b/log.md"; at b git commit -qam "local"; before=$(server_head)
at b git push -q --force origin main 2>/dev/null                  # would overwrite a's commit
check "force push refused (hook, then server)" '[ "$(server_head)" = "$before" ]'
at b git fetch -q; at b git reset -q --hard origin/main

sync a
if [ "$(at a git config core.ignorecase)" = true ]; then
  at a mv "$D" knowledge/decisions/tmp.md; at a mv knowledge/decisions/tmp.md knowledge/decisions/Dec-001.md; sync a
  check "case-only rename recorded (case-insensitive disk)" 'rc 0 && at a git ls-files knowledge/decisions | grep -q "Dec-001.md"'
else
  at a git mv "$D" knowledge/decisions/Dec-001.md; sync a
  check "case-only rename shared (case-sensitive disk)" 'rc 0 && at a git ls-files knowledge/decisions | grep -q "Dec-001.md"'
fi

echo "== result: $pass passed, $fail failed (one sync with nothing to merge took about $((t1 - t0)) s for two runs)"
[ $fail = 0 ]
