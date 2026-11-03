# Optimum KB - instructions for AI agents

Read by Claude Code (CLAUDE.md imports this file) and by Codex (natively). Every teammate's agent
loads it, so it stays short: the project's facts live in the notes, not here.

## What this is

The delivery knowledge base for Optimum Engineering Standards (OES): an offline-first Windows
desktop app for mud engineers on rigs, a web app for managers, a central database with sync. Fixed
price, six months. Internal to the Innowise team. Documents for the client are made from it
(`procedures/export.md`), never sent from it.

It is an LLM wiki: sources that are never edited, a compiled layer of typed notes, and this file as
the schema. Three operations: ingest, query, lint. People edit in Obsidian; their agents edit for
them.

## Layout

| Folder | What | Agents read it by default |
|---|---|---|
| `sources/` | What came in: meetings, client material, presale, contract renderings, internal docs. Never edited, only added to | yes |
| `knowledge/` | The typed notes | yes |
| `index.md` | Generated: every typed note, open questions, disputed notes, change request candidates | yes |
| `log.md` | Append-only record of ingests, applied changes, reviews, schema changes | when asked |
| `pm/` `ba/` `tl/` `qa/` | Each role's working area: prep, drafts, analysis, variants. Not evidence | only when asked |
| `inbox/` | Anything dropped in for ingest | during ingest |
| `reference/` | Question banks for discovery sessions | during workshop prep |
| `schema/types.md` | The nine types and the note header | before writing a typed note |
| `procedures/` | How to ingest, answer, review, prepare a workshop, export | when the task matches |
| `templates/` | Obsidian templates, one per type | - |
| `tools/` | Sync, lint, index, setup check. Curator-owned | - |

Every folder has an `AGENTS.md` saying what it holds and how far to trust it. Read it before using
the folder.

## The nine types

| Type | ID | Folder under `knowledge/` | Owner | In one line |
|---|---|---|---|---|
| Capability | CAP | capabilities | PM and TL | A lasting thing the system must do; the rest hangs on it |
| Requirement | REQ | requirements | BA | A testable need: what and why, never how |
| Concern | CON | concerns | TL | A quality or constraint the architecture must treat |
| Decision | DEC | decisions | the named deciders | A choice with its options, rationale and consequences |
| Question | QUE | questions | BA, or TL for technical | Something that blocks a WBS line or needs the client |
| Term | TRM | terms | BA | A word with one meaning in this project |
| Commitment | COM | commitments | PMs | What we owe the client, or they owe us |
| Increment | INC | increments | TL, with the PM | One demonstrable result for an iteration, across Capabilities |
| Risk | K | risks | PMs | An uncertain event; the PMO register is generated from these |

Fields, statuses, body sections and the distinctions between the types: `schema/types.md`.

## What to do when the person asks

| The person says | Follow |
|---|---|
| "process this meeting", "ingest", "add this", or hands over a transcript, document, chat, file | `procedures/ingest.md` |
| a question about the project | `procedures/query.md` |
| "prepare for the workshop / the call / the session" | `procedures/workshop-prep.md` |
| "weekly review", "check the KB", "what is stale" | `procedures/weekly-review.md` |
| "make a client version", "summary for the client", "draft the email" | `procedures/export.md` |
| "sync", "save", "share", "push", "pull", "update" | Syncing, below |

For anything else, help normally, and keep to the rules below.

## Rules that do not bend

1. `sources/` is never edited: originals, renderings and transcripts stay as stored. New material is
   a new file; a correction is a new file saying what it corrects (`- minutes 2`). Ours to update,
   and only this: overviews and minutes (a row's result, added links and pointers), and swapping our
   own placeholder for the link once that source is stored, in any file. The folders' `AGENTS.md`
   trust notes are schema: the curator changes them, and the change is logged.
2. Only a person promotes. Agents write `draft` or `proposed`. `stable` needs `verified_by:
   human:<id>` set by that person; for a Decision, one of its `deciders`. The id is the person's
   Innowise email name, `human:anton.oparienko`.
3. Never pick a winner. When sources or people disagree, keep both versions in the note and set
   `status: disputed`. The owner or the deciders settle it.
4. Supersede, do not rewrite. When the core of a stable note changes, write a new note with
   `supersedes`, and give the old one `superseded_by` and `status: deprecated`. When only a part
   changes, link the new note and add a line to the old one saying what no longer holds. A meeting
   that overturns a decision gets its superseding Decision proposed in the same ingest.
5. Late changes: describe the concrete change, not a rewrite of the note.
6. No state in notes. Status, assignee, sprint, current estimates and hours spent live in Jira and the
   P&L, and reach the KB only as a generated snapshot, never written by hand. A note may quote the
   initial estimate of a WBS line as history, citing the WBS version. A note carries the Jira key.
7. No money amounts of ours, anywhere: the contract, rates, salaries, payments, budgets, the P&L.
   Anything that affects decisions or delivery is recorded as a fact without the figure: "the
   warranty is unpriced", not the price. One exception: the client's own figures in client material
   the app will handle (the prices, costs and cost shares in a sample report) stay as printed in that
   rendering under `sources/client/`, which the curator flags `money: client-domain`; no note or
   export repeats them. No CVs, no personal data beyond names and roles, no credentials.
8. Numbers and dates are copied exactly as the cited source has them.
9. `origin` says who said it: extracted (a source says it, cite it), evaluated (we concluded it),
   envisioned (we propose it). Never present an assumption as a fact.
10. A demo, a nod or a positive comment is not acceptance unless acceptance is explicit.
11. Requirements say what and why, never how. Architecture goes into Concerns and Decisions.
12. Ask only what blocks. A Question note only when it blocks a named WBS line or needs the client.
    Otherwise propose a Decision with the options, and move on.
13. Before creating a note, look for an existing one: the ID, words from the title, Term aliases.
    Prefer updating. A thin source gets no note of its own.
14. Nothing leaves for the client except through `procedures/export.md`, and the person sends it.

## IDs, names and links

- A typed note's file name is its ID and a short title: `REQ-012 Offline draft report.md`. Names
  are unique across the repo, because wikilinks find a note by its name.
- Next ID: the highest number with that prefix under `knowledge/`, plus one. Two people can still
  collide between syncs; lint flags it and the curator renumbers the later note. Risks are `K-n`
  without leading zeros, as the PMO register numbers them, and are never renumbered.
- Link with wikilinks: `[[REQ-012 Offline draft report]]`.
- The baseline (WBS lines, SOW milestone items, Commitments) is referenced in one format:
  `WBS:Development Flutter!42`, `SOW:M3 <item>`, a Commitment link. `schema/types.md` has it.

## Who writes where

- `pm/`, `ba/`, `tl/`, `qa/`: each is written only by its owner and that owner's agent.
- `knowledge/`: by type owner, in the table above. The curator (Anton) keeps the folder tidy:
  renames, moves and deprecations are his. Nothing is deleted; it is superseded.
- kb-sync warns when a change falls outside the person's area. Before editing a file outside it,
  ask the person.
- `index.md` is generated by `sh tools/gen-index.sh`. Never edit it by hand.
- `log.md` is append-only: one line at the end, never change old lines.

## Syncing - when the person says sync, save, share, push, pull or update

Run exactly this, from the root of the main checkout - the KB folder on branch main, never a git
worktree an agent app made (kb-sync refuses any other branch, and work there reaches nobody):

    bash tools/kb-sync.sh -m "<one line: what changed and why>"

A person without an agent, or in PowerShell where `bash` may be missing or WSL: double-click
`sync-kb.cmd`, or run it from the KB folder.

Do not run git commands that change anything yourself: no add, commit, pull, fetch, merge,
rebase, reset, push, stash, checkout, switch, restore, rm, mv, branch, tag, config. Read-only git
(status, log, diff, show) is fine for explaining what happened. Run it from the repo root, without
`-C`, which is refused. For the branch, use `git status --short --branch`; `git branch` is refused
in every form. Use absolute paths rather than `cd` inside a command, which can move the session.

Then tell the person, in plain words, what the script said:

- `SYNCED` or `NOTHING`: done. Say what was shared and what came in from others
  (`git log --oneline -5`).
- `DISPUTED <file> <person>`: that person changed the same passage at the same time. The
  script kept both versions in a box in the note and marked it `status: disputed`. Show the
  person both versions and who wrote the other one, and ask what they want. Do not choose for
  them, and do not remove the box until they tell you which wording stands. Then edit the
  note, set `status` back to what it was before (the box says), and sync again.
- `WARN ...`: repeat it to the person.
- `STOPPED <reason>`: do not try to fix it with git. Tell the person what it says; their work is
  saved on their computer. The curator (Anton) fixes these.

Never force push, rewrite shared history, or delete branches, even if the person asks or says it is
urgent. Explain that it would erase a teammate's work, and offer to ask the curator.

## Changing the schema

A new type or field needs the curator's yes. Add it to `schema/types.md` with its distinctions,
update `tools/kb-lint.mjs` and `tools/gen-index.sh`, and log it in `log.md` with who approved it. A
type is deprecated, never deleted.

## Where the rest lives

- Jira: not created yet. When it is, status, assignee and sprint live there, and a generated
  snapshot brings them in read-only. The generator is built when there is a board.
- PMO risk register: generated from `knowledge/risks/` and filed as a Confluence page, never edited
  there. Not filed yet; the generator is built at A06. Blockers (`B-n`) stay in the PMO issue log.
- PMO Drive folder: created 2026-11-02 by the RM, `PMO Private > Projects 2026 > Optimum Engineering
  Standards`. The General side, for the team, is
  https://drive.google.com/drive/folders/1lHNFUdFfaegjDN-GWRd9_kiYNBZTCipg: presale copies in
  `01_Presale`, the client's sample reports in `02_Documentation/Requirements`. The Sensitive side (P&L,
  contracts, internal; PMs only) is not linked here, because this repo feeds the project notebook.
  Large originals and anything with our money amounts stay in Drive.
- WBS: the Google Sheet `10H7vDQCbev_-jC6y0J5zeCw1Os2n-6MfJiAVb0k2hbg`; the current estimate is the
  Flutter roll-up.
- Project NotebookLM notebook: "Optimum Engineering Standards - Project Brain",
  https://notebook.google.com/notebook/aa0f69db-c963-4e49-8c23-2a9d988f44d8. Team only, never the
  client. It is fed from this repo through generated Google Docs (the build is in the PM's copilot
  workspace), and money is never in it, not even as a link.

If anything is unclear or unusual, stop and ask the person.
