# Split a two-column bilingual PDF (English left, Arabic right) into the English text, page by page.
# usage: python pdf-columns.py <in.pdf> <out.txt>
import sys, pymupdf
doc = pymupdf.open(sys.argv[1])
out = []
for n, page in enumerate(doc, 1):
    mid = page.rect.width / 2
    blocks = [b for b in page.get_text("blocks") if b[6] == 0]
    left = [b for b in blocks if b[0] < mid - 5]
    left.sort(key=lambda b: (round(b[1], 1), b[0]))
    out.append(f"=== page {n}")
    for b in left:
        t = b[4].strip()
        if t:
            out.append(t)
open(sys.argv[2], "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print("pages", len(doc))
