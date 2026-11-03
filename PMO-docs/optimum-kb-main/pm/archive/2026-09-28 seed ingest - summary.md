# 2026-09-28 seed ingest - summary

For Anton (claude-code/claude-opus-5-5). The seed ingest of the Optimum KB: batches 1 to 7 and the two
meetings of 2026-09-28, commits b4cb7da to da0315f. What went wrong in the rules and tools along the way,
and what to change: [[2026-09-28 seed ingest - procedure findings]].

## What the KB holds

76 typed notes. None is stable: every one is draft, proposed or disputed, and promotion is the owners'
(the BA for Requirements and Terms, the TL for Concerns, the PMs for Commitments, the named deciders for
Decisions).

| Type | Notes | Draft | Proposed | Disputed |
|---|---|---|---|---|
| Requirement | 20 | 19 | - | 1 |
| Concern | 7 | 7 | - | - |
| Decision | 11 | 8 | 3 | - |
| Question | 9 | 2 | 7 | - |
| Term | 9 | 8 | - | 1 |
| Commitment | 20 | 16 | - | 4 |
| Total | 76 | 60 | 10 | 6 |

29 sources: client 3, contract 2, internal 5, meetings 4, presale 15. Seven are link-only, and the client's
ten formula and chart images are stored as images.

## Needs a decision

Disputed, both versions kept, for the owner to settle:

- [[COM-001 Delivery within six months]]: the contract and the SOW v10.4 set the term differently.
- [[COM-012 Payment schedule]]: three schedules on file disagree.
- [[COM-015 Saudi cybersecurity and regulatory compliance]]: the contract and the SOW place the burden
  differently.
- [[COM-016 Termination and settlement]]: the contract and the SOW give different termination rights.
- [[REQ-004 Roles and what each role can do]]: three roles or four.
- [[TRM-001 Report]]: a report wraps a shift (our reading) or is a daily report built from four mud
  checks (the client's).

Four of the Commitments turn on the contract's own clause that the Agreement prevails over the SOW
(1.3). Whether that settles them is yours to say (findings 29, change 8).

Decisions waiting on people:

- Proposed, for the decider to verify: [[DEC-003 Handling small change requests]] (Alexey Gamanovich,
  Anton Snotov), [[DEC-004 Backend stack]] and [[DEC-007 Flutter for the desktop app]] (Arseniy).
- Draft with deciders named, ready to propose: [[DEC-001 Delivery quality over margin]] (Alexey,
  Mikhail), [[DEC-002 Senior engineers first]] (Alexey; `valid_from` 2026-09-25, though the 7 September
  call agreed the same).
- Draft, no deciders named in any source: [[DEC-005 Desktop at the rig, web app at HQ]] and
  [[DEC-006 Calculations run in the desktop app, formulas fixed in the code]] (the client's and presale's
  choices); [[DEC-008 Fixed price with milestones, on the client's contract]] and
  [[DEC-009 Sign the client's final contract as it stands]] (a PM names them);
  [[DEC-010 Confirm the product with the client through prototypes in code]] and
  [[DEC-011 Move scope between milestones and start building in the first month]] (the 28 September
  proposals). Both of those run against the 7 September line "Разработку не начинаем, пока не закроем
  основные вопросы", and DEC-010's designer part against the UI Kit and UI/UX mockups due in Milestone 1.

Open Questions, seven:

- For the client: [[QUE-001 Why a desktop at the rig, and tablets later]],
  [[QUE-003 Do calculations and modelling need 3D or complex visuals]],
  [[QUE-005 Is the client an NCA Category A or B entity]] (our reading is B, not confirmed),
  [[QUE-008 Which rheological model the hydraulics must use]],
  [[QUE-009 Where may our team members be located]] (Sales first).
- For the team: [[QUE-006 Which SOW and which plan are Annex 1 and Annex 2]] (Annex 1 is the SOW v10.4
  only "по идее"; Annex 2 open), [[QUE-007 What is the Effective Date]] (the client's signature is still
  ahead).

Answered, with a part left open: [[QUE-002 Do managers send anything back to the rigs]] (data goes both
ways; whether managers send instructions back is not answered).

Change request candidates, three: [[REQ-012 Documents uploaded at HQ available at the rig]],
[[REQ-016 Inventory of lab equipment and reagents]],
[[REQ-017 Report on a single calculation or simulation]].

## What was held back, and why

Money, as facts without figures (rule 7):

- Removed in place: every amount and price percentage of the contract (Article 7) and the SOW v10.4; the
  rates and USD columns of both WBS versions; the proposal's discount, advance and support budget; the
  financial plan's figures; the late-payment rate, a credits figure and a cost share in the answers to
  the client; money in 23 messages of the contract chat and 2 of the presale chat; two margin figures in
  the 25 September sync; a figure read as the BA's rate in the 28 September call; a price comparison in
  the 1:1.
- Link-only because of money: the economy chat and the AWS infrastructure breakdown. The P&L itself was
  never ingested.
- The contract chat's redaction map is not in the repo. A copy is in your My Drive, private, since
  2026-09-28, without the two entries that carry Zoom passwords (see the handoff).

People:

- Contact data out: phone numbers and e-mail addresses (contract, SOW, WBS headers, proposal, company
  research), Zoom passwords and IDs, user IDs in Drive links.
- Remarks out, marked in place: a heated remark in the presale chat (you kept it out); a personal detail
  in the 25 September sync; in the 28 September call a remark about the colleague who interpreted and
  a leaving colleague's details; in the 1:1 everything not about Optimum, and Mikhail's remark on starting
  before the formal approvals.

Not rendered, and why:

- The Arabic text of the contract and the SOW; only the English is rendered. The contract says the
  Arabic prevails (15.3).
- Superseded or working versions, link-only: the working estimate, the DevOps estimate, the resource
  plan, the April hours plan (its copy carries money).
- The NCNICC-1 translation: a third party's regulation in an unchecked translation, link-only.
- The MAUI tabs and the infrastructure costs tab of the v1 WBS; the diagram images of the presale
  architecture and the proposal; the proposal's budget and timeline slides; the thumbnails of the client
  images; Gemini's notes of the 28 September call (unusable, finding 62).
- Not sought: the chat with the Flutter estimate (your call).

Rejected at approval: rows 1, 2, 4 and 5 of the 1:1 (the staffing details, location, the Flutter doubt,
the order of work). They stay in its minutes.

## Rules changed during the seed

- b4cb7da, before batch 1: the money gate in kb-sync and the pre-commit hook, one shared pattern file,
  what counts as money, link-only sources, versions, long chats in parts, sync from the main checkout.
- 56ca5db, batch 4: rule 6 lets a note quote a WBS line's initial estimate as history.
- d6eb286, batch 7: a small image may come in with its rendering, internal only; exports strip them.

## Next

- People: the lists under "Needs a decision".
- The KB: the fourteen changes at the top of the findings note; Jira keys once there is a board; links
  to the PMO risk register once it is filed (the contract risks and Anton's acceptance reading of
  28 September wait for it); the PMO Drive folder; the NotebookLM notebook, fed from the repo.
- Ingest: the contract chat's part 4, from after 2026-09-28 12:48 UTC; the [Core] chat as it grows.
