# 2026-10-29 PM handover

Anton's handover to Leu Dorakhau, the Business Analyst, written by Anton's agent
(claude-code/claude-opus-5-5) on 29 October 2026. Working material, not evidence (`ba/AGENTS.md`): it
points at the notes and sources that hold the facts. From here on `ba/` is yours; change or drop this
note as you see fit.

Most typed notes are `draft` or `proposed`: our current picture, not settled facts. Where a source
and a note disagree, the source wins, and the note gets fixed through ingest.

## Start here

Day one:

1. `README.md`: set up the KB once (Git, Obsidian, Claude Code), with the BA line in step 4. Start
   Claude sessions on the KB folder itself, not in a worktree.
2. `AGENTS.md`, the rules your agent follows, and `schema/types.md`, the nine note types. You own
   three: Requirements, Questions and Terms.
3. `index.md`: every note, with "Needs a decision" at the top.
4. This note, then your files below.

Then the knowledge, in this order:

- The system: the twelve Capabilities, [[CAP-001 Identity, roles and access]] to
  [[CAP-012 Security and compliance]].
- The words: [[TRM-001 Report]] to [[TRM-009 ECD]].
- What is needed: [[REQ-001 Record and calculate a shift without internet]] to
  [[REQ-020 Create and manage well jobs and assign engineers]]. What we still have to ask:
  [[QUE-001 Why a desktop at the rig, and tablets later]] to
  [[QUE-012 Are engineers assigned to rigs or to wells]].
- The decisions that shape discovery: [[DEC-005 Desktop at the rig, web app at HQ]],
  [[DEC-006 Calculations run in the desktop app, formulas fixed in the code]],
  [[DEC-010 Confirm the product with the client through prototypes in code]],
  [[DEC-011 Move scope between milestones and start building in the first month]],
  [[DEC-015 Discovery - our own picture of the system, questions as if from scratch]].
- What we owe and are owed: [[COM-020 Milestone plan and deliverables]],
  [[COM-002 Written acceptance of each deliverable]], [[COM-005 Change requests]],
  [[COM-007 Client answers clarifications within three business days]].
- The risks closest to your work: [[K-5 Scope grows through the prototypes]],
  [[K-10 Fixed price with vague acceptance criteria]],
  [[K-4 No client contact with authority, or a slow one]].

## Where things stand, 29 October

- The Agreement is the client's contract ([[2026-09-07 Final contract - overview]]). The SOW is its
  Annex 1. The latest SOW we store is v10.4 of 15 June 2026 ([[2026-06-15 SOW v10.4 - rendering]]).
  Aliaksandr Kavalchuk sent a newer SOW, reworked to the Agreement, on 20 October. It is not stored
  here and not signed yet. Discovery runs in parallel with the signing (his e-mail of 27 October).
- When the six months start is open: [[QUE-007 What is the Effective Date]],
  [[K-3 The six months run from the client's signature, before discovery starts]].
- 20 October: the introductory call. What was agreed, and who owes what:
  [[2026-10-20 Introductory call follow-up]].
- The kick-off: Thursday 29 October was proposed and got no reply. The next proposal is Monday
  2 or Tuesday 3 November, 2 PM Saudi time, with the deck as a PDF
  ([[2026-10-28 Kick-off on Monday or Tuesday]]; the deck: [[2026-10-18 Kick-off deck]]).
- Asked of the client on 20 October and not received by 28 October: filled field reports, the formula
  set with its manual, anything that shows how data is entered and flows today, and the logos.
- Our team: you, confirmed on 27 October. The Tech Lead is not named yet ("joins during Discovery").
  A UI/UX designer on demand. Developers and QA when development starts.

## Who is who

Ours, from [[2026-10-16 RACI v.2]] (final):

| Person | Seat |
|---|---|
| Anton Oparienko, PM | Runs delivery; the client's day-to-day contact and routing |
| Mikhail Andrushkevich, Lead PM | Delivery strategy, scope boundary, commitments to the client; escalations |
| Arseniy Klimenko, DM | Technical direction; covers the TL's column until a TL is staffed |
| Aliaksandr Kavalchuk (AM), Anton Snotov (SM) | Contract and commercial terms |

Your rows in the RACI: R on 6 (scope boundary: what we absorb, what becomes a CR), 8 (requirements
and acceptance; Anton is A), 9 (delivery cycle), 11 (delivery process), 17 (client communication) and
19 (risk register); C on 5 (baseline and re-forecast), 10 (release and UAT) and 14 (AI-assisted
delivery).

Theirs, as agreed on 20 October:

- Mr. Ishaq Lawal, General Manager: project sponsor and decision maker. He accepts the prototypes and
  the requirements, and joins the working sessions when available.
- Ms. Ayaa Khalid: contractual, financial and business matters.
- Ms. Zahra Ahmed and Ms. Jood: day-to-day contacts for technical and IT questions, and for the data
  we ask for.
- Dr. Jaber, the CEO, signs the contract (question sheets, "Context for every session").

## What we already know

The client's top three, in their words (Q&A A.1, [[2025-10-29 Client answers to the Q&A register - rendering]]):
"Must generate complete and accurate reports."; "99.9% data integrity and efficient synchrony between
job sites and HQ server."; "User friendly interface with low latency and minimal bugs." Their pain,
from the first call: Excel calculators that each engineer has his own set of, not standardized, data
hard to centralize.

The shape: an offline-first Windows desktop app for mud engineers at the rig, a web app for managers
at HQ, a central database with sync ([[CAP-002 Offline data and sync between rigs and HQ]],
[[CON-001 Offline operation and sync between rigs and HQ]]). Calculations run in the desktop app
(DEC-006).

Points to keep in mind in every session:

- Three roles or four: [[REQ-004 Roles and what each role can do]], disputed.
- What a "report" is: [[TRM-001 Report]], disputed.
- Hosting: [[DEC-012 Host the central system on Google Cloud in the Kingdom]] is a draft; on-premises
  has come up too.
- The rheological model: the client's procedures use the power law, their program screen shows
  Herschel-Bulkley ([[QUE-008 Which rheological model the hydraulics must use]]).
- Formulas: the SOW makes deriving and validating them the client's job. On 20 October Mr. Lawal
  still expected "a level of double-checking from your side", and alignment with API standards. How
  far we check is Mikhail's and Aliaksandr's call, before the calculations session.
- The tool they used before: most likely MUDPRO (our conclusion; Mr. Lawal said "Mod4"). He does not
  want a copy of it.
- Daily.xlsx, the client's sample daily report, is a water-based report. The client called the
  formula samples "examples", not the required set.
- The client wants a mobile app, the onboarding wizard and an API. All are out of scope or
  change-request candidates, and are never drawn as working screens.

Limits that exist only in the WBS, to be put in writing in the V&S and the acceptance criteria: up to
50 parameters per mud check, up to 30 logged actions in the audit trail, three unit sets, simple
charts, English only; from the SOW, a single desktop resolution and no dark mode. The largest gap:
sync has no WBS line at all ([[2026-10-01 SOW v10.4 to v1 WBS scope mapping]]).

## How discovery runs

The plan: [[2026-10-13 Discovery plan - draft]], Anton's, for the leads. It was written before you
joined, so its week 0 and the BA search are past. In short:

- Milestone 1 is one month. Its deliverables are in [[COM-020 Milestone plan and deliverables]]: the
  V&S with the backlog, the Solution Architecture Design, the UI Kit, the mockups (our prototypes, if
  the client agrees), the communication plan, the revised WBS and the project plan.
- Twelve prototype areas (D1 to D6 desktop, W1 to W6 web) in seven session topics, plus one technical
  session.
- Each topic gets one session. You revise the prototype, and the client confirms it by clicking
  through and answering by e-mail. Development on a topic starts after its written OK; nobody waits
  for all twelve.
- About ten sessions in the month, two or three a week, Monday to Thursday.

What the kick-off deck tells the client: two or three sessions a week, a vision session, three UI
style options to choose from, one topic per session, a technical session, the deliverables at the
end.

Two prototypes exist, and they overlap:

- Anton's v0, topics 1 and 2 (D1, W1, D2, W3, and W2's ranges and units). The master is the canvas,
  https://claude.ai/artifact/R5mrsrgEuYm1ZznV7mqLnE, which Anton shares with you. An offline copy:
  [[2026-10-18 Discovery prototypes v0 - README]].
- Mikhail's OE prototype, both apps, with live calculations from the client's formula sheets, not yet
  verified: [[OE prototype - read me]].

Which one goes to the client, or how they merge, is not decided.

## Open calls you are part of

1. Where the master copy of your deliverables lives (user stories, V&S): the KB's Requirements, with
   the client-facing space generated from them, or the client-facing space, with each approved
   version ingested. Decide it before the client gets a shared space. Decision 5 in
   [[2026-10-14 Generated documents as sources - options]].
2. Which prototype goes to the client, and the three UI styles.
3. Whether the prototypes stand in for the SOW's mockups, with the UI Kit taken from them (the plan's
   open item 1).
4. An e-mail round for confirmations, or four sessions a week (the plan's open item 2).

## Your files

Moved here from `pm/` on 29 October:

- [[2026-10-13 Discovery question sheets - draft]]: your working tool for each area. The rules for
  the BA, the 12 areas with their WBS rows, what the scope mapping changes, the limits, the context
  for every session, and a sheet of questions per area.
- [[2026-10-21 MUDPRO research]]: the tool OES used before, how it works and looks.
- [[2026-10-22 API standards research]]: the API 13 series, the test formulas, RP 13D hydraulics, and
  what it means for the app.
- [[2026-10-22 Prototypes against MUDPRO and API]]: both prototypes checked against the two notes,
  what to change now and what to hold, and new questions.

Still in `pm/`, the PMs' to edit: the Discovery plan, Mikhail's
[[2026-10-01 SOW v10.4 to v1 WBS scope mapping]] (to be re-run once the SOW as sent is stored), the
RACI, `pm/exports/` (what we sent the client) and `pm/prototypes/`.

## Not in the KB yet

Nothing after mid-October is ingested:

- the meetings: the introductory call of 20 October (Bluedot 6ad73c7c657f708925b041c5), the call of
  27 October that confirmed you (6ae0774306b1fd276aeae4bc), the sync of 28 October
  (6ae1cbcb337bec6da8a207a0)
- the client e-mail after 14 October
- the chats after mid-October

For what we said to the client, read the exports in `pm/exports/`. Ask Anton for the Bluedot
recordings.

## Links outside the KB

Each needs view access; ask Anton.

- Kick-off deck: https://docs.google.com/presentation/d/1_NXDUbQH-0odi-fPFF3U1H3ZPGwe0rLxqssGFAFAnE0/edit
- Introductory meeting deck, 20 October: https://docs.google.com/presentation/d/1S7TBajpwuE-EZ4eh3OYZSPhw46nyLWW2pmkdQ538CUo/edit
- SOW v10.4, with the fee schedule (the KB rendering has no money): https://docs.google.com/document/d/1bzY2oTz7nEbwalBQXC3dAPhmzVPRzZL2pf7iEAVG6-g
- v1 WBS, tab "Development Flutter", MVP lines: https://docs.google.com/spreadsheets/d/10H7vDQCbev_-jC6y0J5zeCw1Os2n-6MfJiAVb0k2hbg
- Daily.xlsx, the client's sample daily report: https://docs.google.com/spreadsheets/d/1K118jJZabVe8zwgxSLwmizwYQGrSPp5k
- The client's formula and chart samples: https://drive.google.com/drive/folders/1pC29fiMRRpXLm4ikHdjY4qJbZyH8TFKx
- The client's answers to the Q&A register: https://docs.google.com/document/d/1ZbIYC6VGfa2TB9EPVC03cvgCh_iCXmKDEa1KIzGHGbo
- OES company research from presale: https://docs.google.com/document/d/14yvl0zOD_vuEQnVkUbUYlguNroIgxvYpPUGvJSEU6NE
- The company site: https://www.oes.com.sa/

## How we work in the KB

- Say "sync" to your agent when you start and when you stop.
- After a session, "process this meeting" with the transcript. Your agent proposes changes;
  nothing becomes knowledge until you approve them (`procedures/ingest.md`).
- Agents write `draft` or `proposed`. Only a person makes a note `stable`; for your notes, you.
- Requirements say what and why, never how. A Question note only when it blocks a WBS line or needs
  the client.
- A demo, a nod or a positive comment is not acceptance. Each area closes with a written OK by e-mail
  from the client.
- No money amounts anywhere, no personal data beyond names and roles. Fictional data in the
  prototypes ([[CON-006 Confidentiality of the client's customers' data]]).
- Nothing goes to the client except through `procedures/export.md`, and a person sends it.
- Build discovery questions from the client's own material. The banks in `reference/` are too
  general.
