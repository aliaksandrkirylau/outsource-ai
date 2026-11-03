# Turn a Bluedot get_meeting result (JSON, word-level "transcription") into speaker turns:
# "[hh:mm:ss] Name: text", consecutive words of one speaker joined, text verbatim.
# Also writes Bluedot's own summary, as markdown, next to the output (for reading, not for storing).
# usage: python bluedot-json2md.py <get_meeting result file> <out-body.md>
import json, sys

src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src, encoding="utf-8"))
if isinstance(d, list):
    d = d[0]
if "transcription" not in d and "text" in d:
    d = json.loads(d["text"])

def stamp(sec):
    s = int(sec)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"

turns, cur = [], None
for w in d["transcription"]:
    who, text = w.get("speakerTag") or "Unknown", w["text"].strip()
    if not text:
        continue
    if cur is None or cur[1] != who:
        cur = [w["start"], who, []]
        turns.append(cur)
    cur[2].append(text)

with open(out, "w", encoding="utf-8", newline="\n") as f:
    for start, who, words in turns:
        f.write(f"[{stamp(start)}] {who}: {' '.join(words)}\n\n")

summary = out.rsplit(".", 1)[0] + " - bluedot summary.md"
with open(summary, "w", encoding="utf-8", newline="\n") as f:
    for e in d.get("summary", {}).get("entries", []):
        f.write(f"# {e.get('name', '')}\n\n")
        for b in e.get("blocks", []):
            f.write((b.get("text") or "") + "\n\n")

speakers = {}
for _, who, words in turns:
    speakers[who] = speakers.get(who, 0) + len(words)
print("turns:", len(turns), "words:", sum(speakers.values()), "by speaker:", speakers)
print("last word at", stamp(d["transcription"][-1]["end"]), "- duration", d.get("duration"))
