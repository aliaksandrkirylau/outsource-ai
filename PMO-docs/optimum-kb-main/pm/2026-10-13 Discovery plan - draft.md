# 2026-10-13 Discovery plan - draft

Anton's draft for Mikhail, Arseniy and Aliaksandr Kavalchuk. Working material, not evidence
(`pm/AGENTS.md`). Restructured on 15 October. The BA's preparation is in
[[2026-10-13 Discovery question sheets - draft]], the text for the client in
[[2026-10-13 Discovery plan, client version - draft]]. Why discovery runs this way:
[[DEC-015 Discovery - our own picture of the system, questions as if from scratch]],
[[DEC-010 Confirm the product with the client through prototypes in code]].

## What discovery delivers

Milestone 1 as the SOW lists it ([[COM-020 Milestone plan and deliverables]]), accepted in writing
([[COM-002 Written acceptance of each deliverable]]):

- Clickable prototypes, each with the client's written OK. They stand in for the SOW's "Main UI/UX
  mockups", and the UI Kit is taken from them, if the client agrees (open item 1).
- Vision and Scope, with the backlog behind each approved prototype: user stories and acceptance
  criteria.
- Solution Architecture Design, including sync and how updates reach the rigs.
- Revised WBS: per topic, the WBS line against our minimal solution and the client's ask, plus
  estimates for what the WBS lacks, sync first
  ([[2026-10-01 SOW v10.4 to v1 WBS scope mapping]]).
- Project plan for Milestones 2 to 6, and the communication plan.

Minimum: the written OK on the Milestone 1 documents and on the topics Milestone 2 builds. Maximum: an
OK on every topic. Only the minimum can be committed to; the feedback loops are the client's (Mikhail).

## What prototypes we build

Clickable prototypes in Claude Design, no Figma. One per area of the WBS tab "Development Flutter", MVP
lines only - twelve:

| Desktop app at the rig         | Web app at HQ                                                   |
| ------------------------------ | --------------------------------------------------------------- |
| D1 Sign-in and app frame       | W1 Sign-in and app frame                                        |
| D2 Job and measurements        | W2 Admin panel: users, thresholds, edit approvals, audit, units |
| D3 Calculations and hydraulics | W3 Job management and QC                                        |
| D4 Inventory                   | W4 Inventory                                                    |
| D5 Reports                     | W5 Reports and approval                                         |
| D6 Dashboard                   | W6 Dashboard                                                    |

- First, before the client: a clickable skeleton of both apps - sign-in, navigation by role, the
  modules as empty frames - then v0 of topics 1 and 2, so the first sessions have something to click.
- Done ahead of the BA, 16-17 October: v0 of topics 1 and 2 on one canvas,
  [Optimum prototypes v0](https://claude.ai/artifact/R5mrsrgEuYm1ZznV7mqLnE) - D1, W1, D2, W3, and W2
  ranges and units. Built from the question sheets and the client's daily report; every guess is a
  question on the canvas's sticky notes. Opens in a browser signed in to claude.ai, once Anton shares
  it; each frame plays with its Play button. A copy that opens from the KB folder, without an account
  or a link: [[2026-10-18 Discovery prototypes v0 - README]]. Not shown to the client yet.
- Minimal: the smallest version that meets its WBS line. Anything bigger is logged as a delta, not
  drawn ([[K-5 Scope grows through the prototypes]]).
- Out of scope and change-request candidates are not drawn as working screens: mobile, the onboarding
  wizard, the API, historical import, documents from HQ, lab equipment, the engineering-calculation
  report ([[COM-005 Change requests]]).
- Fictional data only ([[CON-006 Confidentiality of the client's customers' data]]).
- Each prototype is accepted on its own; development on it starts after its written OK, nobody waits
  for all twelve.
- Not prototyped: sync, the rig PCs and updates, hosting and compliance. The technical session and the
  Solution Architecture Design cover them.

## How we split it into topics

Seven, each covering the desktop and the web side of a module together, plus one technical session.
Built from the WBS section names; the questions inside each are in the question sheets.

1. Sign-in, app frames and roles (D1, W1)
2. Well job, mud checks and QC, with thresholds and units (D2, W3, W2 thresholds)
3. Administration: users, edit approvals, audit (W2)
4. Inventory (D4, W4)
5. Calculations and hydraulics (D3)
6. Reports and report approval (D5, W5)
7. Dashboards (D6, W6)

Technical session: offline work and sync, the rig PCs and updates, hosting and compliance (X1 to X3).

## Schedule - likely tight

Weeks count from the first session with the client's contact, not from a date: when the six months
start is open ([[QUE-007 What is the Effective Date]]).

- Week 0, until the client names a contact (now): this plan, the client version, the materials list,
  the BA search. Once the BA is on board: the skeleton of both apps, then v0 of topics 1 and 2.
- Week 1: kickoff - who approves, the subject experts, cadence, how the written OK works, the materials
  list (the formulas first). Vision - a day of a mud engineer and of a supervisor today, users and roles,
  a walk through the skeleton. Topic 1.
- Week 2: topics 2 and 3.
- Week 3: topics 4 and 5; the technical session.
- Week 4: topics 6 and 7; the Milestone 1 documents assembled.
- Week 5, a buffer. Topics without an OK by then carry on alongside the building of approved ones
  ([[DEC-011 Move scope between milestones and start building in the first month]]).

Each topic gets one session. The BA then revises the prototype and the client confirms it by clicking
through a link and answering by email; a second session only where that does not work. That makes
about ten sessions in the month: kickoff, vision, seven topics, the technical session - two or three a
week, 60 to 90 minutes, online, Monday to Thursday (the client works Sunday to Thursday). From us, the
BA and the PM in every session, Arseniy or the architect in the technical one.

Why it is likely tight: it holds only if the client names a contact and the experts in week 1, sends
the materials in week 1, and answers each email round within about a week. The contract gives the
client no deadline for a written OK (the 14 business days are for formal deliverables), and the
client's contact may be slow ([[K-4 No client contact with authority, or a slow one]]). Planning on
about a week per OK, development on topic 1 starts around week 3, not week 2. Without the email round,
it is four sessions a week, or six weeks.

## What we need from the client

People: the contact who can approve; one or two mud engineers and a field supervisor for the sessions;
their IT for the technical session.

Materials, in week 1: the full formula set with the source manual (asked for on 18 November 2025, never
received); the mud-check parameter list per mud system, with units and ranges; two or three filled
daily reports and an end-of-section and end-of-well report, anonymised; the product catalogue; the rig
PC spec and connectivity; the KPIs for the dashboards.

Answers: written questions are due an answer in three business days
([[COM-007 Client answers clarifications within three business days]]), but a late answer gives us no
extra time ([[COM-008 Client cooperation and dependencies]]). Open questions go out in writing the day
of the session.

## Open

1. Do we propose the prototypes as the SOW's mockups, with the UI Kit taken from them, at the kickoff?
2. The email round for confirmations, or four sessions a week?
3. An interpreter for demos to the decision-maker? (hearsay that he speaks only Arabic, COM-008)
4. When the six months start ([[QUE-007 What is the Effective Date]]); the schedule above does not wait
   for it.
5. Hours and control - the BA's hours against the discovery line, the per-topic numbers, the weekly
   check and the call after discovery - left out of this version for now.
