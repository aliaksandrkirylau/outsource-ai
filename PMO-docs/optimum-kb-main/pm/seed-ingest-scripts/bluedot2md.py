# Turn a Bluedot PDF transcript export (text already extracted) into speaker turns:
# "[h:mm:ss] Name: text", lines of a turn joined, text verbatim.
# usage: python bluedot2md.py <in.txt> <out-body.md> "Name One" "Name Two" ...
import re, sys
src, out, names = sys.argv[1], sys.argv[2], sys.argv[3:]
lines = open(src, encoding="utf-8").read().splitlines()
start = next(i for i, l in enumerate(lines) if l.strip() == "Transcription") + 1
speaker = re.compile(r"^(" + "|".join(re.escape(n) for n in names) + r") (\d+:\d{2}(?::\d{2})?)\s*$")
turns, cur = [], None
for l in lines[start:]:
    m = speaker.match(l.strip())
    if m:
        if cur: turns.append(cur)
        t = m.group(2)
        if t.count(":") == 1: t = "0:" + t.zfill(5)
        cur = [t, m.group(1), []]
    elif cur is not None and l.strip():
        cur[2].append(l.strip())
if cur: turns.append(cur)
with open(out, "w", encoding="utf-8") as f:
    for t, n, body in turns:
        f.write(f"[{t}] {n}: {' '.join(body)}\n\n")
print("turns", len(turns))
