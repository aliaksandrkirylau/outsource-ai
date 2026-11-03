# 2026-09-28 seed ingest - handoff

For the next session that continues the seed ingest (claude-code/claude-opus-5-5, for Anton). Read
this, AGENTS.md, schema/types.md, procedures/ingest.md and the trust notes first. Guided mode: stop at
each batch's table and wait for Anton's rows. No em dashes; " - ". Every terminal command starts with a
`# AIM:` comment. The findings so far: [[2026-09-28 seed ingest - procedure findings]] - keep adding to
it and finish it at the end.

## Where things stand

| Batch | What | Commit |
|---|---|---|
| rules | money gate, ingest rules, contract trust note, sync from main | b4cb7da |
| 1 | presale requirements: client Q&A answers, sample daily report, first call notes, company research, project description, BA draft WBS | 99c62ae |
| 2 | first-call transcript (+ minutes 2), presale architecture, solution proposal, proposal slides, comm plan draft, answers to the client, cybersecurity framework | 413e4b5 |
| 3 | SOW v10.4 (presale), final contract (contract), client financial plan shape | 0977fae |
| 4 | v1 WBS (internal), the WBS sent to the client on 5 Nov 2025 (presale); REQ-020; v1 WBS linked in 30 notes | 56ca5db |
| 5 | presale chat, 461 messages in two parts (presale); link-only working estimate, DevOps estimate, AWS breakdown; 13 notes updated; DEC-007 Flutter for the desktop app (draft, no deciders named) | 942b6ed |
| 6 | contract chat, 665 messages in three parts (contract); link-only economy chat, resource plan, April hours plan, NCNICC-1 translation (internal); 27 notes updated (14 COM, 3 QUE, 3 CON, 2 REQ, 5 DEC); DEC-008 and DEC-009 new (draft); DEC-007 proposed, decider Arseniy Klimenko | e5ce69d |
| 7 | client images: 10 formula pages and program screens transcribed and stored as images (client), thumbnails not rendered; 7 notes updated (4 REQ, 1 CON, 1 DEC, 1 QUE) and 2 presale chat files linked; QUE-008 (rheological model, for the client) and TRM-009 ECD new; the "batch 7" placeholders linked; ingest.md and export.md: small images may come in, internal only | the "Ingest batch 7" commit |
| 28 Sep meetings | the 11:00 call "Optimum: discuss next steps" (Bluedot transcript, three removals; Gemini notes link-only) and the Anton / Mikhail 1:1 (Optimum parts only), in `sources/meetings/`; DEC-010 and DEC-011 new (draft, deciders not named), QUE-009 new; COM-020, DEC-002, COM-008, DEC-009 updated; from the 1:1 only the DEC-010 row | the commit after "Ingest batch 7" |

Next free IDs: REQ-021, CON-008, DEC-012, QUE-010, TRM-010, COM-021. Every table up to batch 7 was
approved in full ("apply all"); the 11:00 call's too; the 1:1's for one row only (DEC-010).

From batch 7: the images themselves came into the KB with Anton's yes (finding 55), under a new rule in
ingest.md step 2 (under 1 MB, looked at first, `<name> - image 01.png`, embedded, internal only). The
downloaded copies in `~/.workspace-mcp/attachments` were deleted after. Batches 4 to 6 were run on the main checkout with no worktree: file tools write
directly, no scratch copy needed.

Waiting on people, from batch 6:

- DEC-008 (fixed price with milestones) and DEC-009 (sign the client's final contract as it stands):
  draft, no deciders named. Anton: "pretty much a go for project, but we will try to follow the
  procedure anyway". A PM names the deciders; then they can be proposed. Whether DEC-009 supersedes
  DEC-008 in part is theirs (finding 53).
- DEC-007: proposed; Arseniy sets `verified_by` to make it stable.
- DEC-002: `valid_from` 2026-09-25, though the 7 September call agreed the same (finding 54).
- The disputed Commitments stay disputed; batch 6 added history, not settlements.

Waiting on people, from the 28 Sep meetings:

- DEC-010 (prototypes in code, no designer at the start) and DEC-011 (move scope between milestones,
  build from month 1): draft, deciders not named. Both run against the 7 September line "Разработку не
  начинаем, пока не закроем основные вопросы" (quoted in DEC-009); the deciders settle it. DEC-010's
  designer part is still to decide: the UI Kit and the UI/UX mockups are Milestone 1 deliverables (Anton;
  finding 66).
- QUE-009 (where our people may sit): to Sales (Snotov) first, then the client.

The two 2026-09-28 meetings are done: `sources/meetings/2026-09-28 Optimum discuss next steps/` and
`sources/meetings/2026-09-28 Anton and Mikhail 1-1/`, each table in its minutes. The 1:1 keeps only the
Optimum turns; Mikhail's remark on starting before the formal approvals is kept out (Anton did not ask
for it back).

## Remaining batches

4. **WBS.** Done. `sources/internal/2026-09-25 v1 WBS/` and
   `sources/presale/2025-11-05 WBS sent to the client/`; the table is in the v1 overview.
5. **Presale chat.** Done: `sources/presale/2025-10-20 Presale chat/`, the table in its overview. The
   old estimate and the DevOps estimate are stored link-only in `sources/presale/` (superseded presale
   drafts; finding 44). The resource plan and the April hours plan are not in the presale chat: look in
   the contract and economy chats (batch 6). The Flutter-estimate chat ("чат с флатером") is not
   sought for now (Anton). Anton, 2026-09-28: "we go with flutter for the build".
6. **Contract and economy chats.** Done: `sources/contract/2025-11-25 Contract chat/` (three parts, the
   table in its overview), `sources/internal/2025-11-25 Economy chat/` (link-only, facts without
   figures), and link-only `2025-11-25 Resource plan`, `2026-03-03 April hours plan` and
   `2026-07-14 NCNICC-1 translation` in `sources/internal/`. The "(stored in batch 6)" placeholders in
   the WBS sources are now links (finding 51). The contract chat is still in use: the next ingest of it
   is a part 4 from after 2026-09-28 12:48 UTC. The redaction map for parts 1 to 3 (it holds figures)
   is not in the repo (finding 47). Since 2026-09-28 a copy is in Anton's My Drive, private: "Optimum KB -
   contract chat redaction map, parts 1-3 (2026-09-28).json" (file ID 1TfNVV_yjTHqhvuEGad_8X_66VLg2DWdD).
   The two entries that carry Zoom passwords were left out of that copy; its `note` names the two
   messages, to re-add from the chat before re-rendering. A part 4 needs only its own map.
7. **Client images.** Done: `sources/client/2025-11-20 Client formula and chart samples/`, the table
   in its overview. Formulas as one line of plain text in code blocks, no dollar signs (finding 56).
   The ten images are stored next to the rendering and embedded; copyright unchecked, so internal
   reference only (findings 55, 59).

Then, done 2026-09-28: the findings note is final, with the fourteen changes it proposes at the top
([[2026-09-28 seed ingest - procedure findings]]), and the summary for Anton is written
([[2026-09-28 seed ingest - summary]]). The seed ingest is closed; what comes next is ordinary ingest
(the contract chat's part 4, the [Core] chat, new meetings) and the curator's changes.

## How to write into the KB

- The main checkout is `C:\Users\USER\AI Projects\optimum-kb` on main. If the session runs in a
  worktree, its file tools cannot write there: build files in a scratch copy and `cp` them in, with
  Anton's OK (he gave it for the seed). Check `git status --short` in main before copying.
- `tools/**` is deny for agents: Anton copies tools himself, in PowerShell (`Copy-Item`, no `&&`).
- Screen every rendering: `perl tools/kb-money.pl --files <file>` from the main checkout.
- Sync: `bash tools/kb-sync.sh -m "..."` from the main checkout, after gen-index, lint and a log line.
- procedure_version for overviews: ingest.md changed in the batch 7 sync (the image rule), so take it
  from `git log -1 --format=%h -- procedures/ingest.md`; batch 7's own overview keeps b4cb7da, the
  version it was ingested under.

## Conventions used

- Source folders `<YYYY-MM-DD> <title>/`; renderings keep the source's words; `removed:` in the header.
- One table per batch, in the main source's overview or minutes; the others point to row numbers.
  Source keys defined above each table.
- Sources not stored yet are named in plain text ("SOW v10.4 (stored in batch 3)") and linked later.
- Disputed where two sources disagree now, even if one says it prevails; Anton settles.
- Commitments: no figures; "party" us or client, "both" in the body when mutual.
- Hours: a note may quote a WBS line's initial estimate as history, citing the WBS version (rule 6,
  changed 2026-09-28); only where the number makes the point, not in every note with a `wbs` line.
- A person is `human:<email name>`; client people are named in text only.

## Scripts

In `pm/seed-ingest-scripts/`: `bluedot2md.py` (Bluedot PDF transcript to turns), `pdf-columns.py`
(English column of a bilingual PDF), `strip-contacts.py` (phones and e-mails out), `mark-results.mjs`
(fill the Result column), `link-source.mjs` (link a newly stored source in notes, by placeholder),
`link-mention.mjs` (link the first plain mention of a source, when there is no placeholder; `--dry`
lists first), `chat2md.mjs` (render a Google Chat into parts by period; its header lists the config
fields). Write new scripts as files, never inline: the shell tool drops backslashes.

How to render a chat with `chat2md.mjs` (finding 46): read the space with the Chat tool at a page size
of 1000 and a `createTime` filter for the period; the result is too large for the conversation, so the
app saves it as a JSON file under the session's `tool-results/`. Unpack its `result` text to a file in
the scratchpad, write a config there (dump, outDir, parts, redactions; never in the repo), run
`node pm/seed-ingest-scripts/chat2md.mjs <config.json>`, fix every "NOT FOUND", then screen each part
with `perl tools/kb-money.pl --files <file>` before copying it in.
