---
type: source
kind: meeting-minutes
date: 2025-10-22
setting: client
participants:
  - Anton Snotov
  - Marina Zaretskaya
  - Polina Yanovskaya
  - Lawal (client, introduces himself as the general manager)
  - Zahra Ahmed (client)
transcript: "[[2025-10-22 First call with OES - transcript]]"
recording: https://app.bluedothq.com/preview/68f88f2f11127db221fa5eee
purpose: the first discovery call with the client, now from its transcript
procedure_version: b4cb7da
---
# 2025-10-22 First call with OES - minutes 2

**This file corrects [[2025-10-22 First call with OES - minutes]]**, which says no transcript exists.
One does: a Bluedot export posted in the presale chat on 2025-10-22, stored as
[[2025-10-22 First call with OES - transcript]]. Everything else in the first minutes stands; these
minutes add what the transcript says. The first minutes are not edited (AGENTS.md rule 1).

The participants: Polina Yanovskaya hosted the recording but does not speak in it. Bluedot labels
nearly all client speech "Zahra Ahmed", but that speaker introduces himself as Lawal, "the general
manager of the of the organization" (0:00:57), and speaks of Zara in the third person. Zahra is on the
call; which turns are hers cannot be told. Below, "the client" means the client's speaker. "Anton" in
the transcript is Anton Snotau (Sales).

## Summary

The client's main speaker explained the business: OES provides drilling-fluid engineering on rigs
owned by its customers, Saudi Aramco the biggest; engineers on each rig measure the fluid with lab
equipment, keep inventory of chemicals, materials and lab tools, and report daily and at the end of
each well, at up to 70 rigs at once. Current tools (Excel, off-the-shelf software) do not scale and are
not standard across engineers. No sensors, no IoT: data is typed in from lab results, four "mud
checks" a day make one daily report. The client wants alerts that stop nonsense and flag
out-of-spec values, calculators every engineer uses the same way, hydraulics scenario simulation
"not overly complicated", PDF reports plus CSV and Excel, a one-page dashboard, and local data at the
rig moved regularly to a server in the office, not fully in a cloud. "It needs to be a desktop
application. That is first and foremost", with a mobile app later for supervisors. Timeline wished for:
"plus or minus three to four months". Direct proposal and contract; the speaker decides, with the
CEO's final approval; a proposal was promised in one to two weeks.

## Decisions

None. The client stated requirements and preferences; nothing was agreed.

## Agreements with the client

- Innowise sends a proposal within one to two weeks: "Okay, I can give you one to two weeks" (1:15:02).
  A presale step, done in November 2025.
- Questions during estimation go through Polina or "Johan" (1:21:51).

## Internal agreements

- Marina Zaretskaya takes desktop versus web to the solution architects (1:04:02).

## Actions

- Innowise: the proposal, within one to two weeks (1:14:45). Done (the presale proposal of 2025-11-03
  and the slides of 2025-11-05).

## Questions raised

- How to define a "user" when one rig computer serves many engineers over time (0:57:56 to 1:01:47).
  Unanswered on the call.
- Cloud, local or hybrid storage: "something that we need to deliberate on" (0:43:55, 0:44:41).
- Whether the client's own customers get access to the software: the client is "ambivalent" (0:29:42).

## New scope mentioned

- Inventory of lab tools, reagents and equipment (0:12:27, 0:37:48), not in the v1 WBS: REQ-016 in the
  table.
- A report of a single calculation or simulation (0:37:48): REQ-017.
- Suggestions after a calculation ("these are the suggested things you should do about it", 0:47:25):
  recorded in REQ-007 as an expectation beyond the calculator.

## Also said, kept here rather than as notes

- Why the client builds its own software: Excel is unstable at scale, depends on each user's skill, is
  hard to centralise; off-the-shelf tools confine them; "this is a core aspect of our business" (0:19:02).
- The client's customers are big (Aramco, and competitors Schlumberger, Baker Hughes with their own
  tools); OES is "a small, medium sized enterprise" and wants something "very cost effective"; they
  invited alternative proposals without costly nice-to-haves (1:17:13 to 1:21:02). For the A02 and A04
  drafts.
- Innowise's pitch (0:01:49 to 0:08:25): company facts, not project knowledge.

## Proposed changes

The whole batch 2 table is here; the batch 2 overviews point to their rows. Source keys:

- T = [[2025-10-22 First call with OES - transcript]] (timestamp)
- ARCH = [[2025-10-24 Presale architecture - rendering]]
- PROP = [[2025-11-03 Solution proposal - rendering]]
- SLIDES = [[2025-11-05 Proposal slides - rendering]] (slide n)
- ANS = [[2025-12-30 Answers to the client's questions - rendering]]
- COMM = [[2025-12-30 Communication plan draft - rendering]]
- SEC = [[2026-07-14 Cybersecurity framework - rendering]]
- QA = [[2025-10-29 Client answers to the Q&A register - rendering]]

The v1 WBS and the SOW v10.4 are named in plain text, as in batch 1, until batches 3 and 4 store them.

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | disputed | TRM-001 Report | Version A (Klimenko, 25 Sep): a report wraps what an engineer records in a shift. Version B (the client): four mud checks a day make one daily mud report, "Each mod check is not a report in and of itself", and the day's second engineer generates it and shares it with the customer and the office. Both kept, status disputed | extracted | - | T 0:42:22, 1:06:48; 25 Sep transcript 00:08:12 | applied 2026-09-28 |
| 2 | new | TRM-008 Mud check | One complete set of fluid measurements from a sample: each engineer does two per 12-hour shift, one every six hours, four a day; "the industry standards is usually three to four times"; lab equipment, rheology, chemical titrations; aliases full mud check, mod check | extracted | - | T 0:22:25, 0:42:22 | applied 2026-09-28 |
| 3 | update | TRM-002 Shift | Add: 24-hour operation, two engineers share it in 12-hour shifts, each enters the details of their own shift | extracted | - | T 0:42:22, 1:06:48 | applied 2026-09-28 |
| 4 | update | TRM-005 Project (well job) | Add: "Each of those walls on in themselves is like a project"; one rig computer may see five to ten wells in six months; a well "can take between 30 to 45, sometimes 60 or more days" | extracted | - | T 0:12:27, 1:06:48 | applied 2026-09-28 |
| 5 | update | TRM-003 Mud engineer | Add aliases drilling fluid engineer, job sites engineer; engineers rotate while the computer stays | extracted | - | T 0:25:39, 0:47:56, 1:06:48 | applied 2026-09-28 |
| 6 | update | QUE-001 Why a desktop at the rig, and tablets later | Add: "it needs to be a desktop application. That is first and foremost", mobile "what the, the supervisors mostly will find more useful", Windows; the client asked for our recommendation and Marina leaned to web "For scalability". The tablet half stays open | extracted | - | T 1:02:23, 1:03:23, 1:03:41, 1:04:02 | applied 2026-09-28 |
| 7 | update | DEC-005 Desktop at the rig, web app at HQ | Context: the desktop is the client's requirement, stated on the first call; the presale architecture says a desktop "is required". Option 1 (web) was Marina's first lean. Still no named deciders | extracted | - | T 1:02:23, 1:04:02; ARCH | applied 2026-09-28 |
| 8 | update | REQ-005 Parameter thresholds and entry alerts | Correct and add: the client wants out-of-range values still captured, flagged and counted, with the reason justified, and entry of data "that do not make sense" prevented; the range is the one "required by the customer". So the mandatory comment matches the client's words, and the slides showed it to the client | extracted | contracted, Development Flutter!52 | T 0:35:31; SLIDES 13 | applied 2026-09-28 |
| 9 | update | REQ-011 Dashboards and KPIs | Add: "forget about the term real time" - saved data is visible to authorised users, a supervisor sees a finished report; the dashboard's form is "too early to define", "a single one page snapshot", current status against the target; web reports show the last synced data. Replaces the real-time edge case | extracted | contracted, Development Flutter!31 | T 0:33:11, 0:34:40, 0:39:42, 0:40:30; ANS | applied 2026-09-28 |
| 10 | update | REQ-007 Derived values and standard calculations | Add: automatic standard calculations versus a calculator mode; calculators so every engineer uses the same, company-issued tool instead of personal Excel; the weight-up example (from 10 ppg or SG 1.4 to 1.6, barite, calcium carbonate or both, bags or metric tons); the client expects the tool to warn of knock-on changes and suggest actions - beyond a calculator, a scope risk; AI "might be involved, but not heavily" (out for the MVP, QA P1 5); formulas hard-coded (DEC-006) | extracted | contracted, Development Flutter!58 | T 0:47:25, 0:52:09; ANS | applied 2026-09-28 |
| 11 | update | REQ-008 Fluid hydraulics simulation | Add: the flow-rate window ("an ideal flow rate", too low and the well is not cleaned, too high and it fractures); "it's not overly complicated", once done on "a big HP programmable calculator or Excel" | extracted | contracted, Development Flutter!60 | T 0:52:09, 1:10:43 | applied 2026-09-28 |
| 12 | update | QUE-003 Do calculations and modelling need 3D or complex visuals | Add evidence: the client calls the simulation "not overly complicated"; dashboards "too early to define"; presale read the "No" as "a potential desire for complex visualizations". Stays open | extracted | - | T 0:39:42, 1:10:43; PROP Challenges | applied 2026-09-28 |
| 13 | answer | QUE-004 Is a separate engineering calculation report expected | Yes, in the client's words: "The engineer just want to be able to do an engineering calculation or simulation and generate report just for that". The presale proposal still had "Engineering Calculation reports"; the slides dropped them. answered_by REQ-017 | extracted | - | T 0:37:48; PROP Objectives; SLIDES 12, 13 | applied 2026-09-28 |
| 14 | new | REQ-017 Report on a single calculation or simulation | The engineer generates a report of one calculation or simulation. Not in the v1 WBS or the SOW v10.4: a change request candidate | extracted | proposed-change, nearest Development Flutter!67 | T 0:37:48; QA P1 3 | applied 2026-09-28 |
| 15 | new | REQ-016 Inventory of lab equipment and reagents | "The inventory of their own tools and reagents and equipment that they use in the lab"; a list of lab equipment and consumables at the start, now and used; in the presale architecture and proposal. The v1 WBS and the SOW cover chemicals and materials only: a change request candidate | extracted | proposed-change, nearest Development Flutter!39 | T 0:12:27, 0:37:48; ARCH; PROP | applied 2026-09-28 |
| 16 | update | REQ-009 Inventory tracking | Add: the drilling fluid itself and "the long list of chemicals and materials"; stock at the start, now and used "with a click of a button"; lab equipment moves to REQ-016 | extracted | contracted, Development Flutter!61 | T 0:12:27, 0:37:48 | applied 2026-09-28 |
| 17 | update | REQ-010 Reports | Add: PDF is the industry standard, then sent by e-mail; CSV and Excel wanted to share only parts; reports generated selectively; the day's second engineer generates the report; whether the client's customers get access to the software is open ("ambivalent", un-QCed data is the risk) | extracted | contracted, Development Flutter!67 | T 0:29:42, 0:37:48, 1:06:48 | applied 2026-09-28 |
| 18 | update | REQ-004 Roles and what each role can do | Add to the record (stays disputed): the client names three groups - engineers with the same rights, project supervisors over "10, 15" rigs who QC the data, and management; the presale architecture has the same three, no admin; the proposal and slides have four | extracted | contracted, Development Flutter!12 | T 0:25:39; ARCH; PROP; SLIDES 14 | applied 2026-09-28 |
| 19 | update | REQ-003 Sign in on a shared rig computer | Add the client's question: one rig computer, "10 engineers at various point in time, maximum two at the same time" over a year - is each engineer a user, or the computer? Unanswered on the call | extracted | contracted, Development Flutter!47 | T 0:59:46 | applied 2026-09-28 |
| 20 | update | CON-004 Scale and data volume | Add: up to 70 locations at the same time; a well 30 to 45, sometimes 60 or more days (the notes said about 2 months); 24-hour operation; a supervisor over 10 to 15 rigs | extracted | - | T 0:12:27, 0:25:39, 0:42:22 | applied 2026-09-28 |
| 21 | update | CON-002 Deployment outside public cloud | Add: storage undecided on the call; local data on the rig computers moved "into a physical server in the office"; not "100% on cloud" for confidentiality and outages "like we're having recently with AWS". Presale history: on-premises hybrid, client provides hardware, deployment and maintenance outside the budget (PROP); then "cloud provider instead of hybrid or on-premise" (SLIDES 24); slide 14 says "AWS PostgreSQL Database ... Deployed at OES HQ". The framework: personal data inside Saudi Arabia, cloud in the Saudi region (SEC) | extracted | - | T 0:43:55, 0:44:41; PROP; SLIDES 14, 24; SEC | applied 2026-09-28 |
| 22 | update | CON-001 Offline operation and sync between rigs and HQ | Add: "we want the 50 rigs data to be regularly centrally stored"; presale design: an aggregation service; "bi-directional synchronization and conflict-resolution engine ... the primary technical challenge"; web reports use the last synced data; on "99.9%": "how we define / promise this" (internal comment) | extracted | - | T 0:28:04; ARCH; PROP; ANS | applied 2026-09-28 |
| 23 | update | CON-006 Confidentiality of the client's customers' data | Add: "Confidential customer data and we have confidentiality to protect"; giving the client's customers access is a risk with un-QCed data. Treatment points to CON-007 | extracted | - | T 0:29:42, 0:44:41 | applied 2026-09-28 |
| 24 | new | CON-007 Saudi cybersecurity and data protection rules | The framework's four sets of controls (NCNICC-1:2025, DCC-1:2022, PDPL, CCC-2:2024): secure SDLC, secure coding and SAST, vulnerability scans, penetration tests for Category A, MFA for admin and remote access, least privilege, SBOM, data classification, TLS 1.2 or higher, encryption at rest, key management, immutable audit logs, secure disposal, privacy by design, consent, data subject rights, personal data inside Saudi Arabia, records of processing, cloud controls. Which of them the project must meet comes with the contract (batch 3) and the contract chat (batch 6) | extracted | - | SEC | applied 2026-09-28 |
| 25 | new | QUE-005 Is the client an NCA Category A or B entity | Penetration testing is required for Category A, recommended for Category B (SEC). Asks: client. Blocks the v1 WBS DevOps and QA lines, which carry no penetration testing | evaluated | blocks the v1 WBS DevOps tab | SEC | applied 2026-09-28 |
| 26 | new | DEC-006 Calculations run in the desktop app, formulas fixed in the code | Options: formulas in the desktop code, chosen; formulas configurable in the web admin, lost because "the calculations would no longer work offline"; calculations on the central server, lost for the same reason. Told to the client on 2025-12-30; no deciders named. Consequences: a formula change needs a new desktop release on every rig; hard to reverse. Treats CON-001 and CON-003 | extracted | - | ANS; T 0:47:25 | applied 2026-09-28 |
| 27 | update | REQ-013 Mobile app | Add: the web app is designed for desktop screens only ("The default desktop frame is 1440x1024 pixels", no tablet or phone layouts); iteration 2 dropped mobile; the proposal made it "a future phase"; the architect noted MAUI could run on Android and iOS | extracted | out-of-scope, Development Flutter!75 | ANS; SLIDES 24; PROP; ARCH comment | applied 2026-09-28 |
| 28 | update | REQ-014 Onboarding wizard for new users | Add: the proposal named "guided wizards" as an objective and hints as a "Bonus", while internal comments called hints "out of scope" | extracted | out-of-scope, Development Flutter!48 | PROP | applied 2026-09-28 |
| 29 | update | REQ-015 Import of historical data | Add: the proposal: migration "will be scoped separately"; yet the AWS-credits answer defines go-live as the moment "all data is migrated" - a presale statement that assumes migration | extracted | out-of-scope, none | PROP; ANS comment | applied 2026-09-28 |
| 30 | new | REQ-018 Units of measure and conversion | "unit management system was added to the scope" (iteration 3); v1 WBS rows 22 and 54: "Choosing metric units used for measurements and the conversion of one unit of measurement into another, including validation rules. Assumption - 3 data sets."; the client's units (ppg, SG, lb/bbl, bags, metric tons) | extracted | contracted, Development Flutter!54 | SLIDES 28; T 0:47:25; QA E24 | applied 2026-09-28 |
| 31 | new | REQ-019 API for other systems | Out of scope, recorded so nobody re-asks: the client "Unsure about API design", on the call "I don't think this is required"; Marina suggested an API for data exchange; our answer: discuss in discovery, estimate separately; v1 WBS assumption 15 and the SOW v10.4 exclude it | extracted | out-of-scope, none | QA P1 5; T 0:27:12, 0:32:10; ANS | applied 2026-09-28 |
| 32 | no material | Communication plan draft and working rules | The meeting cadence (COMM) and the rules in the answers (e-mail as the main channel, "Requirements are approved in writing", the client sends calculations, charts and reports by e-mail) are for the PM's communication plan; the ones the contract keeps become Commitments in batch 3 | - | - | COMM; ANS 3 | recorded 2026-09-28, no note |
| 33 | no material | Warranty and payment history | Warranty offered as 3 weeks (SLIDES 32), then 6 weeks (ANS); payment term 14 working days, advance within 10 calendar days, governing law KSA, annual renewal removed; the client asked for three milestone installments every two months (ANS). Kept for batch 3, where the contract's terms become Commitments | - | - | SLIDES 32; ANS 1, 4, 5 | recorded 2026-09-28, no note |
| 34 | no material | Special pricing conditions | Start in the first week of January 2026, success-story rights after go-live, an advance before start (SLIDES 28). Batch 3 checks what the contract kept | - | - | SLIDES 28 | recorded 2026-09-28, no note |
| 35 | no material | AWS credits and the first client timeline | The AWS-credits promise (ANS comment) goes to the hosting history in batch 6; the client's wished delivery, "plus or minus three to four months", to the timeline Commitment in batch 3 | - | - | ANS; T 0:57:09 | recorded 2026-09-28, no note |
| 36 | no material | Prototype and demo videos | Listed in the slides overview as link-only | - | - | SLIDES 33 | recorded 2026-09-28, no note |
