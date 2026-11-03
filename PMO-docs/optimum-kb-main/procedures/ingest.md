# Ingest - turning something that came in into knowledge

For a meeting (internal or with the client), a document, client material, a chat thread, or
anything in `inbox/`. The output is a stored source plus a list of proposed changes that a person
approves before anything becomes knowledge. Nothing is applied without that approval.

Built from Zeppla's meeting pipeline and the Spec Framework's meeting processor and scope audit.

## 1. Know what it is and why

- What kind: meeting, document, client material, chat.
- Why we are collecting it, in one line. If the person has not said and it is not obvious, ask. No
  purpose, no ingest.
- For a meeting: date, title, who was there, internal or with the client, and where the transcript
  comes from (Bluedot for recorded meetings; someone's notes when there is no recording).
- A recorded meeting: take the transcript from Bluedot first. Before using any summary (Gemini's
  notes, Bluedot's own), check the transcript is in the language the meeting was held in. Gemini
  turned a call in Russian into English fragments and built its summary on them.
- Who is speaking: speaker labels are often wrong. Check them against the transcript (an
  introduction, a reply by name) before quoting anyone. Name a person only as a source names them;
  an identification from another source says "most likely" and cites it; one nobody can make stays
  unidentified.
- A handoff from an earlier session carries Drive file IDs, not only names, since Drive search does
  not find files shared by link. Its counts (messages, files) are a snapshot: recount at ingest.

## 2. Screen before storing

Remove, and say what you removed:

- money amounts (keep the fact, drop the figure): currency amounts, rates, salaries, and any
  percentage of price, margin, discount, rent or a payment split. Hours, headcount, durations and
  dates stay. "The warranty is unpriced" and "a large discount was given" are facts and stay.
  The exception is the client's own figures in client material the app will handle: the prices,
  costs and cost shares in a sample report stay as printed, since they are what the app computes.
  The rendering goes under `sources/client/` with `money: client-domain` in its frontmatter, which
  the curator sets; kb-money and kb-lint then skip it. Anything of ours in it is still removed. The
  figures are the client's confidential data: notes cite the rendering, never copy them.
- personal data beyond names and roles: e-mail addresses, phone numbers, home addresses, passport
  and other ID numbers, signatures, CVs
- bank details: account numbers, IBAN, SWIFT
- credentials of any kind
- a remark about a person that carries no project content: redacted and marked in place, and the
  overview says so. A remark that could embarrass a colleague and adds little: kept out by default
  and put to the person running the ingest.
- from a 1:1, or any meeting that also covers other work: only the parts about this project, kept
  verbatim. The other turns are marked in place as removed, with no content.

How to remove:

- Normalise whitespace first (non-breaking and other unusual spaces), then match. A removal that
  matches nothing is an error to fix, not a pass: a letter with non-breaking spaces inside its
  figures slipped three amounts past a text match.
- When a column header says money but its cells hold hours, or the other way round, read the
  formulas and the chats that explain them, and say in the rendering which it is. Never drop or keep
  a column by its header alone.
- A chat that is mostly money (the Economy chat, pricing threads) is stored link-only (step 3), with
  its non-money facts dated in the overview's summary.

Build the rendering outside the repo (or in `inbox/`) and screen it before it comes in:
`perl tools/kb-money.pl --files <rendering>`. Fix every `MONEY` line; look at every `MONEY?` line and
keep it only if it is not a figure. kb-sync refuses a commit with a money amount anyway, but by then
the figure is on disk in the shared folder.

If the original carries money, the original stays in Drive and only the cleaned rendering comes in.
Large files (spreadsheets, recordings, images of 1 MB or more, PDFs over 5 MB) also stay in Drive;
the rendering links them.

A client-material PDF of 5 MB or less (a report sample, a form, a program's output) may come in next
to its rendering as the original, once whoever ingests it has read every page: kb-money cannot read a
PDF. Our money, personal data or credentials in it keep it in Drive; the client's own figures do not
(the exception above). Name it after its source and the original file,
`<name> - <original file name>.pdf`, link it from the overview, and let notes link to a page as
`[[<file>.pdf#page=3|p3]]`. A file's metadata can hold what its pages do not (an author's account
ID): check it, and if it must go, rebuild the file from its pages and check they render the same.
kb-sync refuses a PDF anywhere else, or over 5 MB. Like stored images, internal reference only.

A small image (under 1 MB: a formula page, a chart, a screenshot) may come in with its rendering, as a
reference copy. kb-money cannot read an image, so a person, or the agent working for them, looks at
each one for money, personal data and credentials before it comes in, and the overview says who did.
Name it after its source, `<name> - image 01.png`, in plain ASCII, and embed it at the top of its
section of the rendering (`![[<name> - image 01.png]]`). The text transcription stays: search and
agents read text. Stored images are for internal reference only, since their copyright is often a
third party's (a manual, a program's screens): they never go into an export (`procedures/export.md`).

## 3. Store the source

Never edit a stored source afterwards, except what AGENTS.md rule 1 names as ours. Names must be
unique across the repo.

Order, when several sources come in together: first the scope references the scope check needs (the
SOW, the WBS, the contract), and the chats that explain a document before or with that document.
A note that names a source not stored yet writes `(not yet stored: <source name>)`; when the source
comes in, the link replaces it (a link swap, rule 1).

Meeting: `sources/meetings/<YYYY-MM-DD> <title>/`

- `<YYYY-MM-DD> <title> - transcript.md`: verbatim, with timestamps, as exported. Later parts get
  `- transcript 2`.
- `<YYYY-MM-DD> <title> - minutes.md`: written in step 5 from `templates/Template - Meeting minutes.md`.

Document, client material, chat: `sources/<meetings|client|presale|contract|internal>/<name>/`

- `<name> - rendering.md`: a faithful markdown rendering, cleaned per step 2. For a chat, see below.
- `<name> - overview.md`: from `templates/Template - Source overview.md`. What it is, the Drive
  link to the original, how far to trust it, what it is not for, the purpose from step 1.
- The original itself only if it is small text, a small image, or a client-material PDF under step 2.

Pick the folder by what the source is; its `AGENTS.md` says how far it is trusted. Move anything
you took from `inbox/` into its new place.

A chat: every message with its date and time (UTC), author, text, and the names and links of its
attachments. Leave out bot and system messages and reaction-only messages, and count them under
"Removed at ingest". A bot message that relays a person's words (a feedback form, a forwarded
answer) is the exception: quote it in the overview, attributed to the person it relays. An author the
chat shows as "Deleted User" or a bare ID is rendered as shown, never guessed; when it matters who
said it, ask a PM. Take every count (messages, removed, parts) from the rendering script's output,
not by hand. A chat longer than about 300 messages is rendered in parts by period:
`<name> - rendering 1.md`, `<name> - rendering 2.md`. A chat still in use gets a new part at each
ingest, starting after the last message of the previous part; the overview of each part records its
first and last message.

A source that cannot be rendered (a recording with no transcript, a video, a file that is all money)
still gets an overview, with `kind: link-only` and no rendering: what it is, the Drive link, why it is
not rendered, and what would make it renderable.

A document with versions: render the versions someone relied on - sent to the client, signed, or used
as the estimate. Each such version is its own source; its overview names the version it replaces in
`supersedes`. The versions in between are listed, with their links, in the overview of the latest
one, and get no folder of their own.

A living document (a spreadsheet that keeps changing) takes the date someone relied on it, such as
the day it was named the current estimate; the overview records the day it was read.

Formulas: one line of plain text each, in a code block, with a key (`_` subscript, `^` power,
`sqrt()`). Mark a reading that could go two ways. No dollar signs: the money screen reads them as
amounts.

A scaled copy of an image (a thumbnail) is listed in the overview, not rendered.

Once the source is stored, delete any copy a tool downloaded outside the repo. The Google tools save
files to `~/.workspace-mcp/attachments`, where contract PDFs with amounts and personal data were
found after an ingest.

## 4. Read what the KB already knows

Before extracting anything: `index.md`, the open Questions, the Decisions and Requirements that
touch the topics, and the Terms and their aliases for the words the source uses. Use the KB's
existing names for things.

## 5. Extract, into the minutes or the overview

- Summary: neutral, outcome-focused, a few lines.
- Decisions: each with a timestamp or section and a short quote. Mark proposals as proposals. A
  demo, a nod or "sounds good" is not acceptance unless acceptance is explicit.
- Agreements with the client, kept apart from internal agreements.
- Actions: one line each - what, who (only if stated), when (only if stated). No checkboxes; the
  action goes to Jira and the line gets the key.
- Questions raised, and new scope mentioned.
- Proposed changes: the table in step 6.

Invent nothing. No owner, date or agreement that the source does not state.

## 6. Propose changes

One row per change, in the minutes or the overview:

| # | Change | Note | What | Origin | Scope | Source |
|---|---|---|---|---|---|---|
| 1 | new | REQ-013 Draft report survives power loss | ... | extracted | clarifies WBS:Development Flutter!42 | 00:14:32 |

Change is one of: new, update, supersede, disputed, answer (closes a Question), no material.

For every item, before writing its row:

- Duplicate check. Decide reuse (update an existing note), create, or unresolved (ask the person).
  Search by ID, title words and Term aliases. Never take an ID from a label in the source.
- Page-creation gate. Create a note only if the item holds something no existing note holds, and
  someone joining the team in six months would need it. Otherwise update, or "no material".
- Scope check, for every Requirement row: in the baseline (give the `baseline` entries: WBS lines,
  SOW milestone items, Commitments), clarifies a baseline item, or change request candidate. A
  candidate is a new Requirement with `scope_status: proposed-change` naming the nearest items it
  falls outside. It never edits a stable Requirement. Once Capabilities exist, name the Capability
  it refines and check that Capability's baseline too.
- Contradiction check. If the item contradicts a stable note: supersede when the client or the team
  changed position over time (that is history), disputed when two sources disagree now. Never a
  silent edit. For a new Decision, also check it against what the Commitments and the SOW say is
  delivered, whatever their status: a Milestone 1 deliverable does not become optional because its
  Commitment is still draft.
- A decision overturned in this meeting gets a supersede row for the old Decision, or, when only a
  part is overturned, an update row on the old one saying what no longer holds.
- A decision taken while refining an Increment gets its own Decision row, linked to the Capability.
- Questions only when they block a named WBS line or need the client. Otherwise propose a Decision
  with the options.
- Numbers and dates exactly as the source has them.

## 7. Stop and ask

Show the table. The person approves rows: "apply 1-4 and 6", "change 5 to...", "drop 3". Do not
apply anything before that.

For every new or changed Decision, ask the person who decided it. Record what they say in
`deciders`: `human:<id>` for our people, `client:<name or role>` for the client's choice. If nobody
can say yet, write `tbd`; the Decision may still be proposed, and a PM names the deciders later.

## 8. Apply the approved rows

- Create or update notes from `templates/` and `schema/types.md`. Status `draft` or `proposed`,
  never `stable`. Set `origin`. Link the sources with timestamps.
- Supersede: the new note gets `supersedes`, the old one `superseded_by` and `status: deprecated`.
- Disputed: both versions in the note, each with its source, `status: disputed`.
- Mark each row in the table with its result: `applied <date>`, `recorded <date>, no note`, or
  `rejected <date>`.

## 9. Record and check

- Add one line to `log.md`: `<date> ingest <source name> - <n> applied, <m> rejected - <person>`.
- In the minutes or overview frontmatter, set `procedure_version` to the short hash from
  `git log -1 --format=%h -- procedures/ingest.md`, so the result can be reproduced.
- Run `sh tools/gen-index.sh`, then `node tools/kb-lint.mjs` if Node is installed. Fix what it
  reports in the notes you wrote.
- Tell the person, in plain words, what changed, and offer to sync.
