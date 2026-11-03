// Link a newly stored source in notes that name it in plain text, with no placeholder to replace.
// usage: node link-mention.mjs <knowledge dir> "<mention words>" "<link name>" [--dry]
// In every note whose body names the source: the first mention that is not inside a wikilink and not
// already followed by " ([[" becomes "<mention> ([[link name]])", and the link is added to `sources:`.
// Words of the mention may be split by any whitespace, a line break included. Prints what it changed.
import fs from "node:fs";
import path from "node:path";
const [dir, words, name, flag] = process.argv.slice(2);
const dry = flag === "--dry";
const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const mention = words.split(" ").map(esc).join("\\s+");
const link = `"[[${name}]]"`;
const insideLink = (s, i) => s.lastIndexOf("[[", i) > s.lastIndexOf("]]", i);
for (const sub of fs.readdirSync(dir)) {
  const d = path.join(dir, sub);
  if (!fs.statSync(d).isDirectory()) continue;
  for (const f of fs.readdirSync(d).filter((x) => x.endsWith(".md"))) {
    const p = path.join(d, f);
    const t = fs.readFileSync(p, "utf8");
    const end = t.indexOf("\n---", 3);
    let head = t.slice(0, end), body = t.slice(end);
    if (!new RegExp(mention).test(body)) continue;
    let linked = false;
    const re = new RegExp(mention, "g");
    for (let m; (m = re.exec(body)); ) {
      const at = m.index + m[0].length;
      if (insideLink(body, m.index) || body.startsWith(" ([[", at)) continue;
      body = body.slice(0, at) + ` ([[${name}]])` + body.slice(at);
      linked = true;
      break;
    }
    let added = false;
    if (!head.includes(link)) {
      const lines = head.split("\n");
      const s = lines.indexOf("sources:");
      if (s > 0) {
        let i = s + 1;
        while (i < lines.length && /^\s+- /.test(lines[i])) i++;
        lines.splice(i, 0, `  - ${link}`);
        head = lines.join("\n");
        added = true;
      }
    }
    if (!linked && !added) continue;
    if (!dry) fs.writeFileSync(p, head + body);
    console.log(`${sub}/${f}: ${linked ? "first mention linked" : "no plain mention left"}, source ${added ? "added" : "already there"}`);
  }
}
