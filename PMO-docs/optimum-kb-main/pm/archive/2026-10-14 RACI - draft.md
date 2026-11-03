# 2026-10-14 RACI - draft

Anton's first cut of the Optimum RACI. This is working material, not evidence (`pm/AGENTS.md`), and it
is internal only. It is our draft built on the PMO reference matrix: the Google Sheet
`1cd95PYsEZDfhtSImD7RXNeEp_kkI7uj-XvXGOu-TdX8` behind Confluence 5057675462. The Confluence page itself
was not read, because the Atlassian connector here does not reach the Innowise site. No money.

From 15 October the working copy is the Google Sheet "Optimum RACI - draft for comments"
(https://docs.google.com/spreadsheets/d/15T_vhxT0rICpuRr8zYXzpHzkR5A8e60RllyVMoTroEU/edit, Anton's
My Drive, not shared yet), where Mikhail and Arseniy leave comments or edit (the 15 Oct call, below). This file
is the version exported to it on 15 October and is not kept in step. The agreed version comes back
from the Sheet.

What it rests on:

- The 14 October call between Anton, Mikhail and Arseniy on the PM/DM split. It is in Bluedot
  (https://app.bluedothq.com/preview/6acf56bc155ee5010f183cd2) and not stored in `sources/` yet.
  Arseniy calls himself "технический PM" (0:00). Mikhail's split is that the tech lead works as the
  architect, "валидация его работы как архитектора, это будет на Арсении", and that planning and
  delivery stay with the PM (1:35). Anton supplies the hours and Arseniy judges what they produced
  (3:23). Mikhail warned this "размазывание" must not move delivery accountability to Arseniy (4:25).
  The model Mikhail described is that the PM plans the two-week sprint, tracks it and flags slippage
  early, while Arseniy guards the architecture, stops "вайб-кодинг" and raises technical stories ahead
  of time (5:56). All three agreed to try it and adjust (7:59, 8:11).
- The 15 October call, the same three, over this draft on screen. It is in Bluedot
  (https://app.bluedothq.com/preview/6ad09c4ee0af1d44ee9d2d9b, 3:29, starts mid-sentence) and not
  stored in `sources/`. Its corrections are under "Changed on 15 October". It ended with Mikhail's
  proposal to "экспортим эту табличку в Google Docs", share it and trade comments there (2:31);
  Anton agreed to send it, and Mikhail and Arseniy to comment (2:42 to 3:17).
- 28 Sep: "Mikhail and Anton one PM role in the first RACI"; "The RACI is drawn once the tech lead
  is settled" (`sources/meetings/2026-09-28 Optimum discuss next steps`, Internal agreements).
- 13 Oct: "Антон Опариенко будет ПМ, а я лид ПМом" (Mikhail); Kavalchuk is the project's AM
  (`sources/meetings/2026-10-13 Optimum Three Caballeros call`, minutes row 21).

## Who is in it

| Column  | Person                | Seat on this project                                                                       |
| ------- | --------------------- | ------------------------------------------------------------------------------------------ |
| PM      | Anton Oparienko       | Plans, tracks and delivers: what is done and by when. Owns the economy and the commitments |
| Lead PM | Mikhail Andrushkevich | The PM's supervisor. His column is open call 1                                             |
| DM      | Arseniy Klimenko      | Technical validator and AI-in-delivery lead: how it is done                                |
| AM      | Aliaksandr Kavalchuk  | Account and Sales: contract, commercial terms, the client's top level                      |
| TL      | not staffed           | Architect who also codes; works day to day with the developers                             |
| BA      | not staffed (K-6)     | Discovery, prototypes, requirements                                                        |

The Head of PMO (Alexey Gamanovich) is not a column. He is where escalations go (row 30).

## The matrix

A = accountable (one per row; it accepts the result and cannot be delegated). R = does the work.
C = must be consulted, and may stop the work if it is going wrong. I = must be informed. Per the PMO
legend, C and I are obligations, not courtesies.

| #   | Activity                                                                 | PM                         | Lead PM | DM                      | AM/Sales               | TL                        | BA               |
| --- | ------------------------------------------------------------------------ | -------------------------- | ------- | ----------------------- | ---------------------- | ------------------------- | ---------------- |
|     | **Contract and commercial**                                              |                            |         |                         |                        |                           |                  |
| 1   | SOW signature, and keeping the work covered by signed documents          | C                          | I       | I                       | A, R                   | -                         | -                |
| 2   | Commercial changes: scope changes, CR terms, negotiation                 | R (scope and hours impact) | C       | C                       | A, R                   | C                         | -                |
| 3   | Milestone invoicing                                                      | R (acceptance evidence)    | I       | I                       | A, R                   | -                         | -                |
| 4   | Top-level client relationship (GM/CEO), business satisfaction            | C                          | C       | I                       | A, R                   | -                         | -                |
|     | **Scope and requirements**                                               |                            |         |                         |                        |                           |                  |
| 5   | Discovery plan and its run (Milestone 1)                                 | A, R                       | C       | C                       | C (first session only) | C                         | R                |
| 6   | Prototypes and the client's written OK on each (DEC-010, COM-002)        | A                          | I       | C                       | I                      | C                         | R                |
| 7   | Scope boundary against the WBS and SOW; what becomes a CR (K-5, DEC-003) | A, R                       | C       | C                       | C                      | C                         | R                |
| 8   | Scope prioritisation while the client has no product owner               | A, R                       | C       | C                       | I                      | C                         | C                |
|     | **Planning and tracking**                                                |                            |         |                         |                        |                           |                  |
| 9   | Roadmap and milestone plan, Milestones 2 to 6, against the commitments   | A, R                       | C       | C                       | I                      | R                         | C                |
| 10  | Effort estimates and their validation, Claude-assisted included (K-7)    | A                          | I       | C                       | -                      | R                         | R                |
| 11  | Sprint planning: estimates collected, priorities set, realism checked    | A, R                       | I       | C                       | -                      | R                         | C                |
| 12  | Sprint and milestone tracking; slippage flagged early                    | A, R                       | I       | I                       | I                      | R                         | R                |
| 13  | Release planning: test plan, UAT, rollout to the rigs                    | A, R                       | I       | C                       | I                      | R                         | C                |
|     | **Technical**                                                            |                            |         |                         |                        |                           |                  |
| 14  | Architecture and solution design: sync, offline, hosting                 | C                          | I       | A                       | I                      | R                         | C                |
| 15  | Technical decisions: stack, infrastructure                               | C                          | I       | A, R                    | -                      | R                         | -                |
| 16  | Architecture integrity: no dead ends, no uncontrolled vibe coding        | I                          | -       | A, R                    | -                      | R                         | -                |
| 17  | Code review and code style                                               | I                          | -       | C                       | -                      | A, R                      | -                |
| 18  | Technical stories raised ahead of the sprints that need them             | C                          | -       | A, R                    | -                      | R                         | -                |
| 19  | Tech debt control                                                        | C                          | -       | A                       | -                      | R                         | -                |
| 20  | AI tooling for the team: agents, context engineering                     | I                          | I       | A, R                    | -                      | R                         | C                |
| 21  | Team effectiveness with AI: metrics, measurement, findings               | R (hours and plan data)    | I       | A, R                    | -                      | R                         | -                |
| 22  | Technical explanation to the client                                      | A                          | -       | R                       | I                      | R                         | -                |
|     | **Resources and economy**                                                |                            |         |                         |                        |                           |                  |
| 23  | Resource plan: roles and hours by month                                  | A, R                       | C       | C                       | I                      | C                         | -                |
| 24  | Staffing run: candidates found, assessed, accepted                       | R (BA)                     | R (BA)  | A, R (TL's hard skills) | I                      | C (developers)            | -                |
| 25  | Hours, economy and P&L tracking                                          | A, R                       | C       | I                       | I                      | -                         | -                |
|     | **Communication and reporting**                                          |                            |         |                         |                        |                           |                  |
| 26  | Day-to-day contact with the client's team (open call 3)                  | A, R                       | I       | C                       | C                      | R (technical)             | R (requirements) |
| 27  | Weekly status: PROREP and the accounting chat                            | A, R                       | C       | C                       | I                      | -                         | -                |
| 28  | Risks, timeline shifts and scope commitments to the client               | A, R                       | C       | C                       | C                      | C                         | -                |
| 29  | Communication plan                                                       | A, R                       | C       | C                       | C                      | I                         | I                |
|     | **Risks and escalation**                                                 |                            |         |                         |                        |                           |                  |
| 30  | Escalation beyond the team: Head of PMO, management                      | R                          | A       | C                       | I                      | -                         | -                |
| 31  | Risk register: identify, assess, respond                                 | A, R                       | C       | R (technical risks)     | C                      | R                         | R                |
|     | **Process**                                                              |                            |         |                         |                        |                           |                  |
| 32  | Delivery process set-up: scope, change, release, quality                 | A, R                       | C       | C                       | I                      | R (git flow, code review) | R (requirements) |

Until a TL is staffed, the DM covers the TL's column. That makes him A, R on rows 14 and 17.

## Changed on 15 October

From the 15 Oct call. Row numbers above are the new ones; the Sheet uses them.

- Row 2 no longer says "team changes". Mikhail: "...командой это ставить на нас" (0:01, the
  recording starts mid-sentence); Anton does not expect "Саша" (Kavalchuk, the AM) to step into team
  management (0:13), and "Давай я Тима отсюда уберу" (0:21), which we read as "team". Team changes
  have no row of their own; the staffing run is row 24.
- The old row 5, "Client contact with authority named, authorised representatives (K-4)", is
  dropped. Mikhail asked what it meant (0:51); Anton: "Это сделано уже", the row was drawn before the
  contact was confirmed (0:55 to 1:11). Ishaq Lawal, General Manager, was named on 14 October (K-4,
  COM-008). Rows 6 to 33 became 5 to 32.
- Row 5, discovery: the AM moves from "C (client scheduling)" to "C (first session only)". Anton:
  "это тоже только относительно типа первого по-хорошему, так я уже сам с клиентом договорюсь, но по
  discovery, workshop и так далее больше ко мне" and "discovery на BA плюс на мне" (1:23 to 1:48).
  What "первого" refers to is our reading; the comment round confirms it.
- Mikhail asked for A, and for a bigger part than C and I: open call 1.

## Where this departs from the PMO template

- The template has two layouts. Type 1 is PM, TL and Sale. Type 2 adds a DM who is accountable for
  value delivery, the roadmap, the budget and risk communication. Ours has a DM column, but the DM's
  content is the opposite of Type 2: per the 14 Oct call, the PM is accountable for planning,
  delivery, the economy and the client's commitments. The DM is accountable for the technical "how".
- The template gives the TL accountability for the whole technical block. Here the DM is accountable
  for architecture, technical decisions, integrity and tech debt (rows 14 to 16, 19), and the TL is
  accountable for code review and code style (row 17). That follows Mikhail's line at 1:35.
- New rows that are not in the template: AI tooling (20), team effectiveness with AI (21), technical
  stories ahead of sprints (18), prototypes with written OK (6), and the scope boundary against the
  WBS (7). The first three come from the 14 Oct call. The other two come from the fixed-price
  contract and K-5.
- A Lead PM column is added. The template has none.
- Rows dropped as not ours, or as people management that belongs to the A12 team version: goal
  setting, 1-on-1s, mentoring, skills gaps, ERD, code documentation, and KPI definition (folded into
  21).

## Open calls

1. **Mikhail's column.** The draft makes him a supervisor: consulted on commitments, the economy, the
   roadmap and risks, and accountable only for escalation beyond the team (row 30). The alternative
   is the 28 Sep idea of one shared PM column. That breaks the one-A rule unless one name holds every
   A. Another alternative is giving him the client relationship, which the 25 Sep sync gave him, but
   that collides with the AM on row 4. On 15 Oct Mikhail asked for more: "Давай, наверное, Эйн [A] на
   меня", since otherwise his part is only to be informed and consulted, and "Я планирую несколько
   более активно участвовать" (1:56 to 2:11). Asked where, he said discovery "и по остальным
   активностям тоже", and which ones he has to look at first (2:15 to 2:25). If he takes A on
   discovery (row 5), the PM's A there goes. He will say which rows in his comments in the Sheet.
2. **DM against TL on architecture.** The draft puts A on the DM and R on the TL (row 14). The other
   option is A on the TL, with the DM as C. Because a C may stop the work, that still gives him a veto
   while leaving the TL owning the design. This decision affects what we promise when we staff the TL.
3. **Who talks to the client day to day.** Until the contract was signed, Sales was the only channel
   (Snotov). Since 13 Oct, Kavalchuk writes to the client. The draft gives the working contact to the
   PM and keeps the AM consulted. On 15 Oct Anton said he would arrange things with the client
   himself after the first session (1:23); nobody objected, which is not agreement. We also need to
   confirm whether Snotov is still on the project.
4. **Client-side columns.** Ishaq Lawal, General Manager, was named as the contact on 14 October;
   whether he can answer and approve is still open (K-4). The columns go in at A12.

## Next

- A02, now: the internal RACI (Sales / DM / Competency Center), meaning the PM, Lead PM, DM and AM
  columns. It is internal only and shared in the accounting chat.
- 15 Oct: in the Sheet for Mikhail's and Arseniy's comments. Then a short call on what is left, and
  the agreed version back here.
- A12, once the TL and BA are staffed: add the TL, BA, QA, developers and the client's people. Every
  person listed confirms their role, with a target of 100% before the readiness review.
- The version we file should be a copy of the PMO sheet, so its legend travels with it. That waits
  until the shape is agreed.
