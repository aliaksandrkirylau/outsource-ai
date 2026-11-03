// Link a newly stored source in notes that named it in plain text.
// usage: node link-source.mjs <knowledge dir> <placeholder regex> <link name> <mention regex>
// Replaces the placeholder with "([[link name]])" and adds the link to `sources:` in every note that
// mentions the source. Prints what it changed and any placeholder left.
import fs from "node:fs";
import path from "node:path";
const [dir, placeholder, name, mention] = process.argv.slice(2);
const ph = new RegExp(placeholder, "g"), men = new RegExp(mention);
const link = `"[[${name}]]"`;
for (const sub of fs.readdirSync(dir)) {
  const d = path.join(dir, sub);
  if (!fs.statSync(d).isDirectory()) continue;
  for (const f of fs.readdirSync(d).filter((x) => x.endsWith(".md"))) {
    const p = path.join(d, f);
    let t = fs.readFileSync(p, "utf8"), n = 0;
    t = t.replace(ph, () => { n++; return `([[${name}]])`; });
    let added = false;
    if (men.test(t) && !t.split("\n---")[0].includes(link)) {
      const lines = t.split("\n");
      const s = lines.indexOf("sources:");
      const end = lines.indexOf("---", 1);
      if (s > 0 && s < end) {
        let i = s + 1;
        while (/^\s+- /.test(lines[i])) i++;
        lines.splice(i, 0, `  - ${link}`);
        t = lines.join("\n");
        added = true;
      }
    }
    if (n || added) { fs.writeFileSync(p, t); console.log(`${sub}/${f}: ${n} placeholder(s), source ${added ? "added" : "already there"}`); }
    if (ph.test(t)) console.log(`LEFT ${sub}/${f}`);
  }
}
