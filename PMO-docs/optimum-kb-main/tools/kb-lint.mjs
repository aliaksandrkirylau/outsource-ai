#!/usr/bin/env node
// kb-lint - deterministic checks for the team KB. No dependencies.
// Usage: node tools/kb-lint.mjs [repo-dir] [--naive]
//   --naive  also run the Zeppla-style check (frontmatter must match /^---\n/) to show the CRLF trap
// Exit code 1 when any ERROR is found. The rules follow schema/types.md and the rules in AGENTS.md.

import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const args = process.argv.slice(2);
const naive = args.includes("--naive");
const root = path.resolve(args.find((a) => !a.startsWith("--")) || ".");
const SKIP = new Set([".git", ".obsidian", "node_modules", ".claude", ".codex", "templates"]);
const PREFIX = { requirement: "REQ", concern: "CON", decision: "DEC", question: "QUE", term: "TRM", commitment: "COM",
  capability: "CAP", increment: "INC", risk: "K" };
const TYPED = new Set(Object.keys(PREFIX));
// risks are K-n as the PMO register numbers them; every other type is PFX-001
const idPattern = (type) => (type === "risk" ? /^K-[1-9]\d*$/ : new RegExp(`^${PREFIX[type]}-\\d{3}$`));
const idExample = (type) => (type === "risk" ? "K-1" : `${PREFIX[type]}-001`);
const STATUS = new Set(["draft", "proposed", "stable", "disputed", "deprecated"]);
const ORIGIN = new Set(["extracted", "evaluated", "envisioned"]);
const SCOPE = new Set(["contracted", "clarified", "derived", "proposed-change", "out-of-scope"]);
const JUSTIFIED = new Set(["contracted", "clarified", "derived"]);
const DECISION_SECTIONS = ["Context", "Options considered", "Decision", "Rationale", "Consequences"];
// baseline entries: WBS:<tab>!<row>[-<row>], SOW:M<n> <item>, a Commitment link, CR:<id>
const BASELINE = /^(WBS:[^!]+!\d+(-\d+)?|SOW:M\d+(\s.*)?|\[\[COM-\d{3}[^\]]*\]\]|CR:\S+)$/;
// state lives in Jira and the P&L, never in a note (AGENTS.md rule 6)
const STATE_KEYS = ["sprint", "iteration", "assignee", "progress", "estimate", "hours", "state", "jira_status"];
const RISK_ENUMS = {
  register: ["client", "internal"],
  severity: ["high", "med", "low"],
  response: ["accept", "mitigate", "clarify", "escalate", "transfer", "defer", "monitor", "re-estimate", "re-align"],
  critical: ["yes", "no"],
};
// Folder instruction files share names on purpose and are never wikilinked.
const INSTRUCTION_NAMES = new Set(["agents", "readme", "claude"]);
// Content areas get the money and credential screens; tools and reference do not.
const CONTENT = /^(knowledge|sources|pm|ba|tl|qa|inbox)\/|^log\.md$/;
// where the money: client-domain flag counts (kb-money.pl has the same pattern)
const CLIENT_DOMAIN = /^sources\/client\/[^/]+\/[^/]+ - rendering( \d+)?\.md$/i;
// Money rules live in tools/money-patterns.txt, shared with tools/kb-money.pl (the commit gate).
const MONEY_RULES = fs.readFileSync(path.join(path.dirname(fileURLToPath(import.meta.url)), "money-patterns.txt"), "utf8")
  .split(/\r?\n/).filter((l) => l.trim() && !l.startsWith("#"))
  .map((l) => { const [level, name, src] = l.split("\t"); return { level, name, re: new RegExp(src, "iu") }; });
const MONEY_ERR = MONEY_RULES.filter((r) => r.level === "ERROR"), MONEY_WARN = MONEY_RULES.filter((r) => r.level === "WARN");
// link targets, bare URLs, wikilinks and inline code without spaces (Drive and chat IDs) are not text
const moneyText = (l) => l.replace(/\]\([^)]*\)/g, "]()").replace(/https?:\/\/\S+/g, " ").replace(/\[\[[^\]]*\]\]/g, " ").replace(/`[^`\s]*`/g, " ");
const firstRule = (s, rules) => rules.find((r) => r.re.test(s));
// a line, and the line joined to the next (PDFs and chats split "USD" from the figure)
function moneyHit(l, next) {
  const e = firstRule(l, MONEY_ERR) || (next !== undefined && !firstRule(next, MONEY_ERR) ? firstRule(`${l} ${next}`, MONEY_ERR) : undefined);
  return e || firstRule(l, MONEY_WARN);
}
const SECRET = /-----BEGIN [A-Z ]*PRIVATE KEY-----|\b(?:password|passwd|pwd|api[_-]?key|secret|token)\s*[:=]\s*\S{4,}|\bAKIA[0-9A-Z]{16}\b|\bghp_[A-Za-z0-9]{30,}|\bsk-[A-Za-z0-9]{20,}/i;
const INTERNAL_ID = /\b(?:REQ|CON|DEC|QUE|TRM|COM|CAP|INC)-\d{3}\b/;
const today = new Date().toISOString().slice(0, 10);

const anyName = new Set(); // every file name, any extension, for [[file.png]] links
function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (SKIP.has(e.name)) continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, out);
    else {
      anyName.add(e.name.toLowerCase());
      if (e.name.endsWith(".md")) out.push(p);
    }
  }
  return out;
}

const files = walk(root);
const rel = (f) => path.relative(root, f).split(path.sep).join("/");
// The names git records (tracked, plus new files not ignored), to catch case-only differences.
let gitPaths = null, gitLower = new Map();
try {
  const out = execFileSync("git", ["-C", root, "-c", "core.quotepath=off", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], { encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] });
  gitPaths = new Set(out.split("\0").filter(Boolean));
  gitLower = new Map([...gitPaths].map((p) => [p.toLowerCase(), p]));
} catch { /* not a git repo: skip the case check */ }
const byBase = new Map(files.map((f) => [path.basename(f, ".md").toLowerCase(), f]));
const problems = [];
const add = (level, file, line, msg) => problems.push({ level, file: rel(file), line, msg });

// Wikilinks resolve by note name, so two notes with the same name make links ambiguous.
{
  const seen = new Map();
  for (const f of files) {
    const b = path.basename(f, ".md").toLowerCase();
    if (INSTRUCTION_NAMES.has(b)) continue;
    if (seen.has(b)) add("ERROR", f, 1, `note name also used by ${rel(seen.get(b))} - wikilinks become ambiguous`);
    else seen.set(b, f);
  }
}

const linkTarget = (v) => { const m = /\[\[([^\]|#]+)/.exec(v || ""); return m ? m[1].trim() : ""; };
const ids = new Map(); // id -> first file that used it
const notes = new Map(); // lower-case note name -> { file, supersedes, superseded_by }

for (const file of files) {
  const raw = fs.readFileSync(file, "utf8");
  const lines = raw.split(/\r?\n/);
  const relPath = rel(file);

  // Windows stops at 260 characters for the full path; leave room for the clone folder
  if (relPath.length > 150) add("WARN", file, 1, `path is ${relPath.length} characters - long paths fail on Windows clones in deep folders`);

  if (naive && raw.startsWith("---") && !/^---\n/.test(raw))
    add("NAIVE", file, 1, "no frontmatter by /^---\\n/ (file starts with ---\\r\\n)");

  // conflict markers left in the file
  lines.forEach((l, i) => {
    if (/^(<{7}|>{7})( |$)/.test(l) || /^={7}$/.test(l)) add("ERROR", file, i + 1, `conflict marker: ${l.slice(0, 30)}`);
  });

  // frontmatter: flat keys, with block lists ("key:" then "  - item") and inline lists ("[a, b]")
  let fm = null, lists = new Map(), bodyStart = 0;
  if (lines[0] === "---") {
    const end = lines.indexOf("---", 1);
    if (end > 0) {
      bodyStart = end + 1;
      fm = new Map();
      let lastKey = null;
      for (let i = 1; i < end; i++) {
        const item = /^\s+-\s*(.*)$/.exec(lines[i]);
        if (item && lastKey) { lists.get(lastKey).push(item[1].replace(/^["']|["']$/g, "").trim()); continue; }
        const m = /^([A-Za-z_][\w-]*):(.*)$/.exec(lines[i]);
        if (!m) continue;
        if (fm.has(m[1])) add("ERROR", file, i + 1, `duplicate frontmatter key "${m[1]}"`);
        const v = m[2].replace(/\s+#.*$/, "").trim();
        fm.set(m[1], v.replace(/^["']|["']$/g, ""));
        lastKey = m[1];
        lists.set(m[1], /^\[.*\]$/.test(v) ? v.slice(1, -1).split(",").map((s) => s.trim().replace(/^["']|["']$/g, "")).filter(Boolean) : []);
        if (v) lastKey = null;
      }
      // frontmatter lines further down: a union merge of two new files leaves the second note's
      // metadata in the body (git keeps the shared first lines once, so there is no second fence)
      for (let i = end + 1; i < lines.length; i++)
        if (/^(type|id|status|origin|author|verified_by|sources|supersedes|superseded_by):\s/.test(lines[i]))
          add("ERROR", file, i + 1, `frontmatter key in the body: ${lines[i].slice(0, 30)}`);
      const h1 = lines.filter((l) => /^# /.test(l)).length;
      if (h1 > 1) add("WARN", file, 1, `${h1} top-level headings - two notes merged into one?`);
    } else add("ERROR", file, 1, "frontmatter not closed");
  }
  const list = (k) => lists.get(k) || [];

  const type = fm?.get("type");
  if (TYPED.has(type)) {
    const st = fm.get("status"), org = fm.get("origin"), id = fm.get("id") || "", vb = fm.get("verified_by");
    for (const k of ["id", "status", "author"]) if (!fm.get(k)) add("ERROR", file, 1, `typed note without ${k}`);
    if (st && !STATUS.has(st)) add("ERROR", file, 1, `status "${st}" - use draft, proposed, stable, disputed or deprecated`);
    if (!ORIGIN.has(org)) add("ERROR", file, 1, "origin missing - extracted, evaluated or envisioned");
    if (st === "stable" && !vb) add("ERROR", file, 1, "stable with no human verifier");
    if (vb && !/^human:\S+$/.test(vb)) add("ERROR", file, 1, `verified_by "${vb}" - only a person verifies: human:<id>`);
    if (st === "disputed") add("WARN", file, 1, "disputed - two versions kept, needs a decision");
    if (id && !idPattern(type).test(id)) add("ERROR", file, 1, `id ${id} - a ${type} id looks like ${idExample(type)}`);
    for (const k of STATE_KEYS) if (fm.has(k)) add("ERROR", file, 1, `"${k}" is state - it lives in Jira, not in a note (AGENTS.md rule 6)`);
    // an entry-by-entry check of the baseline, for the types that carry one
    const checkBaseline = () => {
      for (const b of list("baseline")) if (!BASELINE.test(b)) add("WARN", file, 1, `baseline entry "${b}" - use WBS:<tab>!<row>, SOW:M<n> <item>, a Commitment link or CR:<id>`);
    };
    const base = path.basename(file, ".md");
    if (id && base !== id && !base.startsWith(id + " ")) add("ERROR", file, 1, `file name must start with the id ${id}`);
    if (id && ids.has(id)) add("ERROR", file, 1, `id ${id} already used by ${rel(ids.get(id))}`);
    else if (id) ids.set(id, file);

    const srcs = list("sources");
    if (!srcs.length && org === "extracted") add("ERROR", file, 1, "origin extracted but no sources - cite what said it");
    else if (!srcs.length && (st === "proposed" || st === "stable")) add("ERROR", file, 1, `${st} with no sources`);
    else if (!srcs.length && st !== "deprecated") add("WARN", file, 1, "no sources yet");

    const early = st === "draft" || st === "disputed"; // not yet claimed complete
    if (type === "requirement") {
      const sc = fm.get("scope_status");
      if (!SCOPE.has(sc)) add("ERROR", file, 1, "scope_status missing - contracted, clarified, derived, proposed-change or out-of-scope");
      if (!fm.get("acceptance_measure")) add(early ? "WARN" : "ERROR", file, 1, "no acceptance_measure");
      if (fm.has("wbs")) add("ERROR", file, 1, "wbs is now baseline, a list: WBS:<tab>!<row> one per line");
      if (JUSTIFIED.has(sc) && !list("baseline").length && st !== "deprecated")
        add(st === "draft" ? "WARN" : "ERROR", file, 1, `${sc} but no baseline entry - name what justifies it`);
      checkBaseline();
    }
    if (type === "decision") {
      const ds = list("deciders");
      if (!ds.length && st !== "draft") add("ERROR", file, 1, "decision without deciders - name them, or tbd until a PM does");
      for (const d of ds) if (d !== "tbd" && !/^(human|client):\S+$/.test(d)) add("ERROR", file, 1, `decider "${d}" - use human:<id>, client:<name or role>, or tbd`);
      if (ds.includes("tbd")) add(st === "stable" ? "ERROR" : "WARN", file, 1, "deciders still to be named (tbd) - a PM names them");
      // a choice the client made is verified by a PM against the source, not by the client
      const clientOnly = ds.length > 0 && ds.every((d) => d.startsWith("client:"));
      if (st === "stable" && vb && ds.length && !clientOnly && !ds.includes(vb)) add("ERROR", file, 1, `verified_by ${vb} is not one of the deciders`);
      for (const sec of DECISION_SECTIONS)
        if (!lines.some((l) => l.toLowerCase().startsWith(`## ${sec.toLowerCase()}`))) add("WARN", file, 1, `decision without a "## ${sec}" section`);
    }
    if (type === "commitment") {
      const p = fm.get("party");
      if (p && !["us", "client", "both"].includes(p)) add("ERROR", file, 1, `party "${p}" - us, client or both`);
    }
    if (type === "capability") {
      if (!["business", "enabler", "hybrid"].includes(fm.get("kind"))) add("ERROR", file, 1, "kind missing - business, enabler or hybrid");
      if (!list("baseline").length && st !== "deprecated") add(st === "draft" ? "WARN" : "ERROR", file, 1, "capability with no baseline - a change request candidate until it has one");
      checkBaseline();
    }
    if (type === "increment") {
      if (!list("capabilities").length && st !== "deprecated") add(st === "draft" ? "WARN" : "ERROR", file, 1, "increment without capabilities - name what it implements");
    }
    if (type === "risk") {
      for (const [k, allowed] of Object.entries(RISK_ENUMS)) {
        const v = fm.get(k);
        if (!v) add(early ? "WARN" : "ERROR", file, 1, `risk without ${k} - ${allowed.join(", ")}`);
        else if (!allowed.includes(v)) add("ERROR", file, 1, `${k} "${v}" - ${allowed.join(", ")}`);
      }
      const ow = fm.get("owner");
      if (!ow) add(early ? "WARN" : "ERROR", file, 1, "risk without an owner - not finished until someone owns it");
      else if (!/^human:\S+$/.test(ow)) add("ERROR", file, 1, `owner "${ow}" - human:<id>`);
    }
    const vt = fm.get("valid_to");
    if (vt && vt < today && st !== "deprecated") add("WARN", file, 1, `valid_to ${vt} has passed - supersede or deprecate`);
    if (fm.get("superseded_by") && st !== "deprecated") add("WARN", file, 1, "superseded but not deprecated");
    notes.set(base.toLowerCase(), { file, supersedes: linkTarget(fm.get("supersedes")), superseded_by: linkTarget(fm.get("superseded_by")) });
  }

  // money and credentials, in the content areas only. A client sample rendering the curator flagged
  // money: client-domain keeps the client's own figures (AGENTS.md rule 7); credentials still count.
  const clientDomain = fm?.get("money") === "client-domain" && CLIENT_DOMAIN.test(relPath);
  if (fm?.has("money") && !clientDomain) add("ERROR", file, 1, `money: ${fm.get("money")} - only "client-domain", only on a rendering under sources/client/`);
  if (CONTENT.test(relPath)) {
    const plain = lines.map(moneyText);
    lines.forEach((l, i) => {
      const m = clientDomain ? undefined : moneyHit(plain[i], plain[i + 1]);
      if (m) add(m.level, file, i + 1, m.level === "ERROR"
        ? `looks like a money amount (${m.name}) - record the fact, not the figure`
        : `may be a money amount (${m.name}) - check it is not a figure`);
      if (SECRET.test(l)) add("ERROR", file, i + 1, "looks like a credential - remove it and rotate it");
    });
  }

  // published forms carry no internal IDs or links
  if (relPath.startsWith("pm/exports/")) lines.slice(bodyStart).forEach((l, i) => {
    if (INTERNAL_ID.test(l)) add("ERROR", file, bodyStart + i + 1, "internal ID in a published form");
    if (l.includes("[[")) add("ERROR", file, bodyStart + i + 1, "wikilink in a published form");
  });

  // links: markdown relative links to .md, and wikilinks by name - skipping code blocks and inline code
  let fence = false;
  lines.forEach((l, i) => {
    if (/^\s*```/.test(l)) { fence = !fence; return; }
    if (fence) return;
    const text = l.replace(/`[^`]*`/g, "");
    for (const m of text.matchAll(/\]\(([^)#\s]+\.md)(#[^)]*)?\)/g)) {
      if (/^[a-z]+:/i.test(m[1])) continue;
      const target = path.resolve(path.dirname(file), decodeURI(m[1]));
      if (!fs.existsSync(target)) add("ERROR", file, i + 1, `broken link ${m[1]}`);
      else if (gitPaths) {
        // Windows and macOS find the file whatever the case; Linux and the Git host do not
        const r = rel(target), known = gitLower.get(r.toLowerCase());
        if (known && known !== r) add("ERROR", file, i + 1, `link says ${path.basename(r)} but git records ${path.basename(known)} - breaks on Linux and on the Git host`);
      }
    }
    for (const m of text.matchAll(/\[\[([^\]|#]+)[^\]]*\]\]/g)) {
      const name = path.basename(m[1].trim());
      const ok = /\.[a-z0-9]{2,5}$/i.test(name) && !name.endsWith(".md")
        ? anyName.has(name.toLowerCase())
        : byBase.has(path.basename(name, ".md").toLowerCase());
      if (!ok) add("ERROR", file, i + 1, `broken wikilink [[${m[1]}]]`);
    }
  });
}

// supersession must point both ways, or the chain lies from one side
for (const [name, n] of notes) {
  if (n.supersedes) {
    const old = notes.get(n.supersedes.toLowerCase());
    if (old && old.superseded_by.toLowerCase() !== name) add("ERROR", n.file, 1, `supersedes [[${n.supersedes}]], which does not point back with superseded_by`);
  }
  if (n.superseded_by) {
    const nw = notes.get(n.superseded_by.toLowerCase());
    if (nw && nw.supersedes.toLowerCase() !== name) add("ERROR", n.file, 1, `superseded_by [[${n.superseded_by}]], which does not point back with supersedes`);
  }
}

for (const p of problems) console.log(`${p.level.padEnd(5)} ${p.file}:${p.line}  ${p.msg}`);
const errors = problems.filter((p) => p.level === "ERROR").length;
console.log(`kb-lint: ${files.length} files, ${errors} errors, ${problems.length - errors} other`);
process.exit(errors ? 1 : 0);
