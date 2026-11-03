// Render a Google Chat dump (the text the Chat read tool returns, unpacked from its saved JSON) into KB
// chat renderings, one file per period.
// usage: node chat2md.mjs <config.json>
// The config names the dump, the output parts and the redactions. Keep it outside the repo: its
// redaction list holds the very figures it removes.
//   dump        path of the unpacked text dump
//   outDir      where the parts are written
//   base        rendering name without " - rendering N", e.g. "2025-11-25 Contract chat"
//   space, spaceName, original, readOn
//   parts       [{ from: "YYYY-MM-DD", to: "YYYY-MM-DD", n }] (inclusive, UTC dates), in order; n is the
//               part's number when a later part is rendered on its own (default: its position)
//   total       the chat's number of parts when it differs from parts.length (a later part)
//   removedNote lines for the `removed:` header, the same for every part
//   botAuthors  authors whose messages are left out
//   system      regexes (strings) for task-system bodies that are left out
//   authorMap   { shown author: rendered author }
//   redact      { message id after "/messages/": [[find, replace], ...] } - every find must occur
//   stored      { needle in a link or attachment name: "[[rendering]] or a note" }
// Prints counts per part and every redaction that did not match.
import fs from "node:fs";
import path from "node:path";

const cfg = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const text = fs.readFileSync(cfg.dump, "utf8").replace(/\r\n/g, "\n");
const chunks = text.split(/\n\n(?=\[\d{4}-\d{2}-\d{2}T[\d:.]+Z\] )/).slice(1);
const system = (cfg.system || []).map((s) => new RegExp(s));
const used = new Set();

const msgs = chunks.map((c) => {
  const m = /^\[(\S+)\] (.*?):\n([\s\S]*)$/.exec(c.replace(/\n+$/, ""));
  if (!m) throw new Error("cannot parse: " + c.slice(0, 80));
  const [, ts, author, rest] = m;
  const out = { ts, author, body: [], links: [], atts: [], thread: null, id: null };
  for (const line of rest.split("\n")) {
    let x;
    if ((x = /^  \[thread: (\S+)\]$/.exec(line))) out.thread = x[1];
    else if (/^  \[reactions: /.test(line) || /^  Use download_chat_attachment\(/.test(line)) continue;
    else if ((x = /^  \[attachment \d+: (.*) \(([^()]+)\)\]$/.exec(line))) out.atts.push({ name: x[1], mime: x[2] });
    else if ((x = /^  \[linked: (\S+)\]$/.exec(line))) out.links.push(x[1]);
    else if ((x = /^  \(Message ID: (\S+)\)$/.exec(line))) out.id = x[1];
    else out.body.push(line);
  }
  if (out.body.length) out.body[0] = out.body[0].replace(/^  /, "");
  // Non-breaking spaces become plain spaces, so redactions match what the eye sees.
  let body = out.body.join("\n").replace(/ /g, " ").replace(/\s+$/, "");
  if (body === "No text content") body = "";
  out.text = body;
  out.key = out.id.split("/messages/")[1];
  return out;
});

const byId = new Map(msgs.map((m) => [m.id, m]));
const left = (m) =>
  (cfg.botAuthors || []).includes(m.author) ? "bot" :
  system.some((r) => r.test(m.text)) ? "system" :
  !m.text && !m.atts.length && !m.links.length ? "empty" : null;

const mask = (s) => s
  .replace(/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g, "[e-mail removed]")
  // Drop the ouid parameter from links. Until 2026-10-13 a trailing [?&] was then trimmed from the
  // whole text, which also cut the "?" off every message that ended with a question.
  .replace(/([?&])ouid=\d+(&?)/g, (_, sep, amp) => (amp ? sep : ""));
const esc = (s) => s.replace(/\\/g, "\\\\").replace(/\*/g, "\\*").replace(/^#/gm, "\\#");
const storedFor = (s) => {
  for (const [needle, note] of Object.entries(cfg.stored || {})) if (s.includes(needle)) return " - " + note;
  return "";
};
const kind = (mime) => ({
  "application/vnd.google-apps.document": "Google Doc",
  "application/vnd.google-apps.spreadsheet": "Google Sheet",
  "application/vnd.google-apps.presentation": "Google Slides",
  "application/vnd.google-apps.folder": "Drive folder",
}[mime] || "in the chat");

function render(m) {
  let t = m.text;
  for (const [find, repl] of (cfg.redact || {})[m.key] || []) {
    if (!t.includes(find)) { console.log(`NOT FOUND in ${m.key}: ${find.slice(0, 60)}`); continue; }
    t = t.split(find).join(repl);
    used.add(m.key + find);
  }
  t = mask(t);
  const author = (cfg.authorMap || {})[m.author] || m.author;
  let reply = "";
  if (m.thread) {
    const tid = m.thread.split("/threads/")[1];
    const startId = m.thread.replace("/threads/", "/messages/") + "." + tid;
    if (startId !== m.id) {
      const s = byId.get(startId);
      reply = s ? ` (↳ ${s.ts.slice(0, 10)} ${s.ts.slice(11, 16)}${left(s) ? `, a ${left(s)} message, left out` : ""})`
                : " (↳ a thread whose first message is not in the chat)";
    }
  }
  const lines = esc(t || "(no text)").split("\n").filter((l) => l.trim() !== "");
  let out = `- ${m.ts.slice(11, 16)} **${author}**${reply}: ${lines[0]}\n`;
  for (const l of lines.slice(1)) out += `  ${l}\n`;
  const links = m.links.map(mask);
  if (links.length === 1) out += `  - Link: ${links[0]}${storedFor(links[0])}\n`;
  else if (links.length) out += `  - Links: ${links.map((l) => l + storedFor(l)).join(" · ")}\n`;
  for (const a of m.atts) out += `  - Attachment: ${esc(a.name)} (${kind(a.mime)})${storedFor(a.name)}\n`;
  return out;
}

const counts = [];
cfg.parts.forEach((p, i) => {
  const inPart = msgs.filter((m) => m.ts.slice(0, 10) >= p.from && m.ts.slice(0, 10) <= p.to);
  const kept = inPart.filter((m) => !left(m));
  const gone = { bot: 0, system: 0, empty: 0 };
  inPart.forEach((m) => left(m) && gone[left(m)]++);
  const n = p.n || i + 1, total = cfg.total || cfg.parts.length;
  const first = kept[0].ts, last = kept[kept.length - 1].ts;
  let md = `---\ntype: source\nkind: rendering\ndate: ${first.slice(0, 10)}\noriginal: ${cfg.original}\nremoved:\n`;
  md += `  - ${gone.bot} bot messages, ${gone.system} task-system messages, ${gone.empty} empty messages\n`;
  for (const r of cfg.removedNote || []) md += `  - ${r}\n`;
  md += `---\n\n# ${cfg.base} - rendering ${n}\n\n`;
  md += `Google Chat space "${cfg.spaceName}" (${cfg.space}), part ${n} of ${total}: from ${first.slice(0, 10)} ` +
        `${first.slice(11, 16)} UTC to ${last.slice(0, 10)} ${last.slice(11, 16)} UTC. Read on ${cfg.readOn}; rendered ` +
        `by \`pm/seed-ingest-scripts/chat2md.mjs\` from the Chat tool's output. Every message in order: time in ` +
        `UTC, author, text verbatim (typos kept; blank lines inside a message dropped), links and attachments. ` +
        `"↳ YYYY-MM-DD HH:MM" marks a reply in the thread started by the message of that time, which may be in ` +
        `another part. Money amounts, credentials and e-mail addresses are replaced in square brackets. ` +
        `Where an attachment is stored in the KB, its rendering is named. Never edited after storing.\n`;
  let day = "";
  for (const m of kept) {
    if (m.ts.slice(0, 10) !== day) { day = m.ts.slice(0, 10); md += `\n## ${day}\n\n`; }
    md += render(m);
  }
  const file = path.join(cfg.outDir, `${cfg.base} - rendering ${n}.md`);
  fs.writeFileSync(file, md);
  counts.push({ part: n, first, last, rendered: kept.length, ...gone });
});
console.table(counts);
console.log("messages in dump:", msgs.length);
for (const [key, list] of Object.entries(cfg.redact || {}))
  for (const [find] of list) if (!used.has(key + find) && byId.size && !msgs.some((m) => m.key === key)) console.log(`NO MESSAGE ${key}`);
