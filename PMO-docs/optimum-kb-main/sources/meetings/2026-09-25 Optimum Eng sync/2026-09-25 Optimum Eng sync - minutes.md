---
type: source
kind: meeting-minutes
date: 2026-09-25
setting: internal
participants:
  - Alexey Gamanovich
  - Mikhail Andrushkevich
  - Arseniy Klimenko
  - Anton Oparienko
transcript: "[[2026-09-25 Optimum Eng sync - transcript]]"
recording: https://app.bluedothq.com/preview/6ab63874170a43238bcf81a7
purpose: internal kick-off of the delivery team - roles, approach, how we treat scope and quality, what happens before staffing
procedure_version: 7ce7904
---
# 2026-09-25 Optimum Eng sync - minutes

Internal, no client present. 32 minutes, in Russian. Transcript: [[2026-09-25 Optimum Eng sync - transcript]].

Speech-recognition slips that matter: at 00:00:04 "Витя Андрушкевич" is Mikhail Andrushkevich;
"ГМ" is DM; "BM" is BA; "SuperBase" is Supabase; "Купайлот" is Copilot.

## Summary

Alexey set out the start: the contract is being finalised on site by Snotov, the project starts in
about a week, staffing launches Monday-Tuesday next week. Roles were assigned. Arseniy described the
product: an offline desktop app for about 70 rigs, where engineers record shifts and calculations
run locally, syncing to a central database when a connection returns, plus a web admin panel. The
team questioned why it is a desktop and not a tablet, and agreed to ask the client. Two backend
options are open. The team agreed that delivery quality comes before margin; how small change
requests are handled is still open.

## Decisions

- Delivery quality comes before margin: no minimal or crutch implementations to save hours.
  Anton framed the choice (00:27:41, "за 20 часов мы типа пилим жесткий костыль ... если мы
  потратим 40 часов, мы можем сделать получше"); Mikhail: "Первый не пройдет" (00:28:16); Alexey:
  "Гуд" (00:28:34).
- Staffing starts with the right senior people; a cheaper mix is looked at later (Alexey, 00:00:04,
  "на первом этапе обязательно, чтобы были такие правильные, подходящие бойцы").
- Roles (Alexey, 00:00:04): Mikhail - client relationship and major strategic questions; Anton -
  regular project administration and a transparent picture; Arseniy - DM, prepares and runs the
  delivery approach; Alexey - the technical side of the delivery strategy and cross-department
  blockers.
- Proposal, not yet a decision: delivery in three waves - the system backbone, then isolating
  context at the API and component level, then the functionality (Alexey, 00:00:04). Arseniy to
  prepare it.

## Agreements with the client

None - internal meeting.

## Internal agreements

- Arseniy sends all materials from the rework period; Anton and Mikhail take them in through the
  copilot into a project knowledge container (00:05:03).
- A clarifying question list goes to the client (00:14:38), through Snotov while he is on site
  (00:13:29).
- Staffing launches Monday-Tuesday next week; Arseniy prepares the position cards, for both stack
  options (00:30:07, 00:30:57).

## Actions

- Arseniy: send all documents, estimates and the current SOW; he does not have the latest contract
  (00:31:20).
- Arseniy: prepare the staffing positions and cards in Maksim Lebedev's new process, for both stack
  options (00:30:07).
- Alexey and Arseniy: a live whiteboard session on the solution design - offline/online sync
  patterns, one-way or two-way - and a review of Arseniy's formula analysis (00:05:03).
- Alexey, with the BA practice: pick a BA suited to working out the formulas; Gestico people are a
  candidate, decided next week (00:07:05).
- Alexey: work out the client strategy, including the change request stance, with Snotov (00:27:33;
  the transcript reads "со снопами", most likely a recognition slip for Snotov).
- Mikhail and Arseniy: the clarifying question list for the client (00:14:38).
- All: a follow-up call around the middle of next week (00:05:03).

No Jira keys yet; there is no board.

## Questions raised

- Why a desktop at the rig and not a tablet; would they later want tablets (00:11:29-00:15:00).
- Do managers send anything back to the rigs (00:15:00).
- Who holds the solution architect role, Arseniy or someone else (00:15:00, 00:15:42) - a staffing
  question.
- Were the estimates made with AI-assisted coding in mind (00:21:50). Answer: no.

## New scope mentioned

None.

## Also said, kept here rather than as notes

- Estimates were made over a year ago for MAUI (.NET desktop), in about 40 minutes, not adjusted
  for AI-assisted coding; Arseniy reviewed them since and says the numbers still hold; the stack
  moved to Flutter because of available expertise (00:21:33-00:23:13). Belongs in the WBS source
  overview when the WBS is ingested.
- Why we take the project: a reference and entry to the MENA oil and gas market rather than
  commercial success (Alexey relaying Snotov, 00:24:34). Folded into DEC-001's context.
- Arseniy judges the formulas simple (fractions and brackets, 2D dependency graphs, 00:08:12);
  Alexey calls them the core of the system (00:00:04). Not a contradiction - both go into CON-003.

## Proposed changes

Status of every new note: draft, except the two open decisions, which are proposed. Approved by
Anton on 2026-09-28: all rows.

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | new | DEC-001 Delivery quality over margin | No crutch implementations to save hours. Options: build to the estimate even if it is a crutch, keeps the economy / spend more and build it properly - chosen. Context: the goal is a reference and entry to the MENA market. Deciders: Gamanovich, Andrushkevich | evaluated | - | 00:23:13-00:28:34 | applied 2026-09-28 |
| 2 | new | DEC-002 Senior engineers first | Seniors for the first part, a cheaper mix looked at later. Decider: Gamanovich | extracted | - | 00:00:04 | applied 2026-09-28 |
| 3 | new | DEC-003 Handling small change requests (proposed) | Open: absorb small changes within reason / absorb only trivial ones (a label, an hour), anything from about a day becomes a CR citing the discount. Gamanovich to settle with Snotov | evaluated | - | 00:26:11-00:27:33 | applied 2026-09-28 |
| 4 | new | DEC-004 Backend stack (proposed) | Open: Flutter + a Node or Python backend, 4 part-time devs (the original estimate) / Flutter + self-hosted Supabase, 2 full-stack devs full-time, same timeline, Flutter lead commits. Supabase's cloud may not be available in the region (Oparienko, unverified). Owner: Klimenko | extracted | staffing lines, to check once the WBS is in | 00:15:42-00:19:46, 00:30:57 | applied 2026-09-28 |
| 5 | new | CON-001 Offline operation and sync between rigs and HQ | The desktop works without internet, calculations run locally, it syncs to the central database when a connection returns. One-way or two-way to be fixed | extracted | - | 00:05:03, 00:08:12 | applied 2026-09-28 |
| 6 | new | CON-002 Deployment outside public cloud | An on-prem or self-hosted server and updates to about 70 offline desktops; the Flutter team mostly deploys to public clouds | evaluated | - | 00:17:49-00:19:46 | applied 2026-09-28 |
| 7 | new | CON-003 Correct calculations | The formulas are the core of the system (Gamanovich); judged simple (Klimenko); the BA works them out | extracted | - | 00:00:04, 00:08:12 | applied 2026-09-28 |
| 8 | new | QUE-001 Why a desktop at the rig, and tablets later | Paper then a PC looks like double entry; rugged tablets exist; moving to tablets later needs a different UI. Asks: client, via Snotov | evaluated | blocks the UI/UX lines, named once the WBS is in | 00:11:29-00:15:00 | applied 2026-09-28 |
| 9 | new | QUE-002 Do managers send anything back to the rigs | Decides one-way or two-way sync (CON-001). Asks: client | evaluated | - | 00:15:00 | applied 2026-09-28 |
| 10 | new | TRM-001 Report | The entity wrapping a shift's recorded work, which admins view. Name provisional ("назовем это отчетом") | extracted | - | 00:08:12 | applied 2026-09-28 |
| 11 | new | TRM-002 Shift | A work shift opened, filled with readings and closed on the desktop | extracted | - | 00:08:12 | applied 2026-09-28 |
| 12 | new | REQ-001 Record and calculate a shift without internet | An engineer opens a shift, enters readings, runs calculations and closes it offline; it syncs later | extracted | believed contracted (SOW v10.4, per the A01 harvest), WBS line once the WBS is in | 00:08:12 | applied 2026-09-28 |
| 13 | new | REQ-002 Managers see engineers' reports in the web app | Admin staff view the reports from the rigs in a web panel | extracted | as row 12 | 00:08:12 | applied 2026-09-28 |
| 14 | no material | Delivery roles | Goes to the A02 stakeholder register; not a KB type | - | - | 00:00:04 | recorded 2026-09-28, no note |
| 15 | no material yet | Three-wave delivery approach | A Decision once Klimenko's plan sets out the options | - | - | 00:00:04 | recorded 2026-09-28, no note |
| 16 | no material | Estimate provenance | Into the WBS source overview when the WBS is ingested | - | - | 00:21:33-00:23:13 | recorded 2026-09-28, no note |
