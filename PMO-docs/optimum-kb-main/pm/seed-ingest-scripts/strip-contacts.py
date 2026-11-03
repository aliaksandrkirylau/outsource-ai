# Remove phone numbers and e-mail addresses from a rendering, in place; print how many were removed.
# usage: python strip-contacts.py <file>
import re, sys
p = sys.argv[1]
t = open(p, encoding="utf-8").read()
n = 0
for pat, rep in [
    (r",?\s*(?:Tel|Telephone|Mobile|Phone)\s*:?\s*\(?\+?[0-9][0-9 ()-]{6,}[0-9]\)?", " [contact removed]"),
    (r",?\s*Email\s*:?\s*[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}", " [contact removed]"),
    (r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}", "[e-mail removed]"),
    (r"\+[0-9][0-9 ()-]{8,}[0-9]", "[phone removed]"),
]:
    t, k = re.subn(pat, rep, t)
    n += k
t = t.replace(" [contact removed] [contact removed]", " [contacts removed]")
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("removed", n)
