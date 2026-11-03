---
type: source
kind: client-material
date: 2025-10-29
original: https://chat.google.com/room/AAQAMdfmWl4/HpWQqfEXnEw/HpWQqfEXnEw
received_from: the client, forwarded by Polina Yanovskaya in the presale chat
purpose: seed the KB with the client's own written answers, the main requirements source from presale
supersedes:
procedure_version: b4cb7da
---
# 2025-10-29 Client answers to the Q&A register - overview

kind: client-material. original: the Questions.docx the client sent back, posted in the presale
chat on 2025-10-29 21:34 UTC. Rendering: [[2025-10-29 Client answers to the Q&A register - rendering]].

## What it is

Innowise's "Q&A register" (dated October 24, 2025): 8 assumptions to confirm and 29 open questions,
with the client's answers typed in. Polina Yanovskaya forwarded it with the client's words: "I
believe the attached documents should provide the clarity and direction you need moving forward."
The client's sample daily report came in the same thread:
[[2025-10-29 Client sample daily report - overview]].

On 2025-10-30 Kira Barshchevich copied the answers into the Innowise Google Doc
(https://docs.google.com/document/d/1ZbIYC6VGfa2TB9EPVC03cvgCh_iCXmKDEa1KIzGHGbo). She marked in red
"то что они недопоняли или обещают доуточнить" (what they misunderstood or promise to clarify) and
left three comments. The Doc's text is the same as the docx (checked); the red marks are lost in any
export, the three comments are at the end of the rendering.

Drafts of this register, listed here and not stored on their own (procedures/ingest.md, versions):

- "Questions" by Marina Zaretskaya, 2025-10-23 to 2025-10-25,
  https://docs.google.com/document/d/1aqiolUtG7vHY0dF3LVfdbxKnqJiam5dtP2fSFG2RKO0 - the first
  question set.
- The "Questions" tab of "OES: Company Research" by Andrey Lapikov,
  https://docs.google.com/document/d/14yvl0zOD_vuEQnVkUbUYlguNroIgxvYpPUGvJSEU6NE - a longer set,
  with an internal comment thread between Zaretskaya and Lapikov on which questions to keep.

## How far to trust it

High for what the client said in October 2025 and for their words for things (`sources/client/`).
Not a requirement until confirmed: the answers are 11 months old at project start and nothing shows
they were checked again. Some are superseded: hosting (C5) moved later (contract chat, batch 6), and
mobile (B3, B4) was dropped from the SOW v10.4. Where an answer contradicts the WBS or the SOW, the
note keeps both.

## Not for

The report layout (that is the sample report, and only as a visual reference). The answers in A.1 are
the client's outcomes, not measured targets.

## Removed at ingest

Nothing. No amounts, personal data or credentials in it. The two letterhead images are left out.

## Summary

The client confirmed the MVP shape: under 50 parameters entered by hand about 4 times a day, about 70
rigs (maybe 100), a central database at HQ with local data at each rig and automatic sync, shared rig
computers, English only, four report types plus an engineering calculation/simulation report,
inventory tracking, alerts, derived values, hydraulics simulation with a long input list, KPIs per
12-hour shift. They asked for a mobile app, onboarding wizards, uploads from HQ and, later, a data
import - which the WBS and the SOW v10.4 exclude or leave out. Two answers are unclear: "No" to "no 3D
or complicated visualizations", and "what do you mean by threshold". The client wants on-premises
hosting but has no staff to run it.

## Scope references used

The scope check uses the v1 WBS ("Development Flutter" rows, "Assumptions & Risks") and the SOW v10.4.
Both are read here as the scope reference but stored later (SOW v10.4 in batch 3, WBS in batch 4), so
the notes name them in plain text for now; batch 3 and 4 add the links. In the table, WBS rows are
`Development Flutter!<row>`, and a row's "estimated" status means the sheet's MVP column is TRUE for it
(the Flutter total counts only those).

Source keys in the table:

- QA = this rendering (Part 1 as "P1 n", Part 2 by letter and number)
- CALL = [[2025-10-22 First call with OES - notes]] (key point n)
- RES = [[2025-10-23 OES company research - rendering]]
- DESC = [[2025-11-25 Project description - rendering]]
- BAW = [[2025-10-28 BA draft WBS - rendering]] (row n of the WBS tab)
- SAMPLE = [[2025-10-29 Client sample daily report - rendering]] (row n of "Report #1")

## Proposed changes

The whole batch 1 table is here, because most rows draw on several of the batch's sources; the
other overviews and the minutes point to their rows.

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | update | CON-001 Offline operation and sync between rigs and HQ | Add the client's words: a local database at each rig with automatic sync when internet is available; the central database at HQ, each location with local access to its own data; offline access "ideally"; "99.9% data integrity and efficient synchrony" is outcome 2. Treatment: HQ also sends data to the rigs (row 2), so sync is two-way. The BA draft planned a sync-monitoring screen; the v1 WBS has no line for sync at all | extracted | - | QA C7, P1 8, A1, A2; BAW 7, 21, 22 | applied 2026-09-28 |
| 2 | answer | QUE-002 Do managers send anything back to the rigs | Yes: thresholds are set in the web admin and checked on the desktop (BAW 5, 16; the SOW v10.4 says the same); documents uploaded at HQ must be accessible on the job site (QA E23). answered_by REQ-005; stays draft until the TL verifies | evaluated | - | QA E23; BAW 5, 16 | applied 2026-09-28 |
| 3 | update | QUE-001 Why a desktop at the rig, and tablets later | Add: "no strict limitations requiring the use of desktop or mobile applications", offline is the constraint; the first ask was "preferably desktop (OS windows)" with a mobile app later for supervisors, and the client asked our opinion; mobile meant iPhone and Android for essential field tasks. Stays open | extracted | - | QA A2, B3, B4; CALL 4 | applied 2026-09-28 |
| 4 | new | DEC-005 Desktop at the rig, web app at HQ | Options: one web app for all / desktop plus mobile (the client's first ask) / desktop plus web, chosen in presale. Rationale in DESC. Who decided is not in these sources (Klimenko on 25 Sep: a requirement of the client's leadership), so no deciders. Consequences: no mobile app (REQ-013); a desktop to install and update on about 70 rig computers (CON-002). Draft | extracted | - | DESC; CALL 4; QA A2; 25 Sep transcript 00:12:12 | applied 2026-09-28 |
| 5 | update | DEC-004 Backend stack | Context only: the presale stack was .NET or Java, MAUI, ReactJS, SQLite, PostgreSQL, ASP.NET Identity or Keycloak, "TBC after the discovery stage"; the two options in the note came later | extracted | - | DESC | applied 2026-09-28 |
| 6 | update | REQ-001 Record and calculate a shift without internet | Add: under 50 parameters entered by hand about 4 times a day; 12-hour shifts; 1 to 4 engineers share the rig computer; each location sees its own data. Scope contracted, wbs Development Flutter!51 (estimated). Sync has no WBS line; the SOW v10.4 has it in Milestone 3 | extracted | contracted, Development Flutter!51 | QA P1 2, P1 8, P1 9, F28; CALL 5 | applied 2026-09-28 |
| 7 | update | REQ-002 Managers see engineers' reports in the web app | Add who reads reports: Field Supervisors, Project Engineers, Operations Support, Operations Manager; the Supervisor reviews and generates reports, the Manager sees dashboards across sites. wbs Development Flutter!32 (web reporting group) | extracted | contracted, Development Flutter!32 | QA C10, D13 | applied 2026-09-28 |
| 8 | new | REQ-003 Sign in on a shared rig computer | Each engineer signs in with their own account on the rig computer that 1 to 4 engineers share; device login alone is "also acceptable" to the client; reuse of an existing identity provider "probably not"; the desktop is for engineers only (v1 WBS assumption 14) | extracted | contracted, Development Flutter!47 | QA D11, D12, P1 9; BAW 12 | applied 2026-09-28 |
| 9 | new | REQ-004 Roles and what each role can do | Four roles with the client's scenarios (QA D13; CALL 5; DESC) against three with Supervisor/Manager as one (BAW 3; v1 WBS row 19). Both kept, status disputed. The client also names Project Engineers, Operations Support and Operations Manager; users and roles are run by "Authorized IT personnel"; no other workflows "at the moment" | extracted | contracted, Development Flutter!12 | QA D13, C10, D15, D16; CALL 5; BAW 3; DESC | applied 2026-09-28 |
| 10 | new | REQ-005 Parameter thresholds and entry alerts | Min/max limits per fluid parameter set at HQ, checked on the desktop, with hints on fields; the client's alert types 1 and 2 (prevent wrong entry, parameters out of threshold); the client asked what we mean by "threshold" and got no written answer; the mandatory comment and "flagged" save are our design, not the client's | extracted | contracted, Development Flutter!52 | QA E19, E20; BAW 5, 16, 20; CALL 5 | applied 2026-09-28 |
| 11 | new | REQ-006 Edit or backfill past entries with approval | Required, "subject to approval by operations manager and/or system admin"; who approves is open (Innowise comment); every edit logged with when, by whom and what | extracted | contracted, Development Flutter!21 | QA E22; BAW 6 | applied 2026-09-28 |
| 12 | new | REQ-007 Derived values and standard calculations | Derived values calculated on save; quick calculations such as "How many bags of barrites do I need?" and oil to add for a new oil-water ratio; formulas come from the client (v1 WBS assumption 12); also Development Flutter!59 | extracted | contracted, Development Flutter!58 | QA E21; CALL 5; BAW 15, 17 | applied 2026-09-28 |
| 13 | new | REQ-008 Fluid hydraulics simulation | "What if" scenarios on the well profile; the client's input list (well architecture, casing and open hole size and depth, survey, drill string and BHA, fluid, mud pump, bit and formation parameters); runs offline (v1 WBS assumption 9); how rich the charts are is QUE-003 | extracted | contracted, Development Flutter!60 | QA E25; CALL 5; BAW 18 | applied 2026-09-28 |
| 14 | new | REQ-009 Inventory tracking | What the client tracks (loadout, inflow, daily and cumulative consumption per section and well, daily balance, product details, concentration in lb/bbl and %, expiry, unit size, unit and total cost); low-stock and expiry alerts; stock events; the sample's product table. Also Development Flutter!38 (web) | extracted | contracted, Development Flutter!61 | QA E20, E24, F27; CALL 5; BAW 30-36; SAMPLE rows 94-98 | applied 2026-09-28 |
| 15 | new | REQ-010 Reports | End-of-Day, End-of-Section, End-of-Well and inventory reports; filter and export to PDF, CSV and Excel; approval only for End-of-Section and End-of-Well; no masking, filtering yes; the sample as the visual reference; "complete and accurate reports" is outcome 1. Out of scope: sending reports from the app (engineers "email reports to the supervisors" today; v1 WBS assumption 18 excludes sending). The fifth type the client names is QUE-004 | extracted | contracted, Development Flutter!67 | QA A1, P1 3, C10, D13, D14, D17, F29; CALL 5; BAW 28, 38-41; SAMPLE | applied 2026-09-28 |
| 16 | new | REQ-011 Dashboards and KPIs | The client's five KPIs, per 12-hour shift, every operating day, all active rigs; a web view across sites and an engineer view on the desktop (also Development Flutter!56). Edge cases: KPI 1 compares with offset wells, but historical import is out of scope (REQ-015) and data is kept 1-2 years; "real-time monitoring" in the first request can only mean as fresh as the last sync, since entry is manual and rigs go offline | extracted | contracted, Development Flutter!31 | QA F27, F28, C8; RES; BAW 26 | applied 2026-09-28 |
| 17 | new | REQ-012 Documents uploaded at HQ available at the rig | "Document upload required from HQ but accessible on the job site"; which features need uploads is open (Innowise comment). No line in the v1 WBS or the BA draft: a change request candidate | extracted | proposed-change, nearest Development Flutter!27 | QA E23 | applied 2026-09-28 |
| 18 | new | REQ-013 Mobile app | Out of scope, recorded so nobody re-asks. Asked for: "mobile app integration", mobile for supervisors later, iPhone and Android for essential field tasks, [+Mobile] across the BA draft. The v1 WBS keeps mobile rows 75-88 outside the estimate; the SOW v10.4 excludes mobile expressly | extracted | out-of-scope, Development Flutter!75 | RES; CALL 4; QA B3, B4; BAW 14, 17, 21, 25, 32, 35, 36, 42 | applied 2026-09-28 |
| 19 | new | REQ-014 Onboarding wizard for new users | Out of scope. The client wants wizards, rules and hints: "Yes (very much)!"; v1 WBS row 48 sits outside the estimate, and the SOW v10.4 excludes the in-app wizard and user manuals. Field hints stay in (REQ-005) | extracted | out-of-scope, Development Flutter!48 | QA E26; BAW 19, 20 | applied 2026-09-28 |
| 20 | new | REQ-015 Import of historical data | Out of scope. The client: "Import data will not be Excel. Actual data format and size estimate to be confirmed later."; optional in the BA draft; excluded by v1 WBS assumption 23 and the SOW v10.4 | extracted | out-of-scope, none | QA C9; BAW 10 | applied 2026-09-28 |
| 21 | new | CON-004 Scale and data volume | About 70 rigs, "can potentially reach 100", "Solution should be scalable"; about two engineers per rig, 1 to 4 on one computer; under 50 parameters about 4 times a day; 12-hour shifts; a well takes about 2 months; data kept 1-2 years | extracted | - | QA P1 2, P1 7, P1 9, C8, F28; CALL 5 | applied 2026-09-28 |
| 22 | new | CON-005 Easy and responsive interface | Outcome 3: "User friendly interface with low latency and minimal bugs"; "intuitive user interface" in the first request; better designed than the sample. No measure yet | extracted | - | QA A1, F29; RES | applied 2026-09-28 |
| 23 | new | CON-006 Confidentiality of the client's customers' data | "concern on confidentiality of data storing - especially his customers' details"; no masking in reports, filtering yes; reports go to the client's customers. Treatment comes with the cybersecurity framework (batch 2) | extracted | - | CALL 7; QA D17, C10 | applied 2026-09-28 |
| 24 | update | CON-002 Deployment outside public cloud | Add: the client wanted a central server on-premises with local caches at the rigs, but has no staff or infrastructure to deploy and maintain on-premises services; did not want to depend on the cloud only and expected our advice. Both kept, not a dispute (one source). The later hosting history comes with the contract chat | extracted | - | QA C5, C6; CALL 6 | applied 2026-09-28 |
| 25 | update | CON-003 Correct calculations | Add: derived values on save; the calculations are explained at 47:00 of the first call's recording, which has no transcript; formulas come from the client (v1 WBS assumption 12) | extracted | - | QA E21; CALL 5 | applied 2026-09-28 |
| 26 | new | QUE-003 Do calculations and modelling need 3D or complex visuals | We asked the client to confirm they do not; the answer was "No", which reads both ways. The v1 WBS assumes simple charts and excludes 3D and complex modelling (assumptions 11, 13, 17). Asks: client. Blocks Development Flutter!60 and !59 | evaluated | blocks Development Flutter!60 | QA P1 4 | applied 2026-09-28 |
| 27 | new | QUE-004 Is a separate engineering calculation report expected | The client lists "Engineering calculation/simulation" among the MVP reports; the BA draft and the v1 WBS have four types, End-of-Well summarising the simulation results. Asks: client. Blocks Development Flutter!67 to !71 | evaluated | blocks Development Flutter!67 | QA P1 3; CALL 5; BAW 38-41 | applied 2026-09-28 |
| 28 | update | TRM-001 Report | Add the client's report types and the daily one's title, "Daily Drilling Fluids Report". The client's daily report covers a day, not a shift, so "a report wraps a shift" stays unconfirmed | extracted | - | QA P1 3; SAMPLE row 1; CALL 5 | applied 2026-09-28 |
| 29 | update | TRM-002 Shift | Add: "Per 12-hour shift every operating day" | extracted | - | QA F28 | applied 2026-09-28 |
| 30 | new | TRM-003 Mud engineer | The client's name for the engineer at the rig; the system role "Engineer"; aliases field engineer, site engineer, sites engineer, on-site engineer | extracted | - | QA D13, C10; RES; CALL 5; BAW 3 | applied 2026-09-28 |
| 31 | new | TRM-004 Rig | Where a mud engineer works, one of about 70; the computer belongs to the rig, not to a person; OES does not own the rigs; aliases location, job site, rig site, site, work location | extracted | - | QA P1 7, P1 9; CALL 4; RES | applied 2026-09-28 |
| 32 | new | TRM-005 Project (well job) | In the product, a project is one well job, created with an ID, location, client info, order details and quality requirements, lasting about 2 months; aliases well/project, job. Not our delivery project | extracted | - | CALL 5; BAW 13; SAMPLE rows 3-6 | applied 2026-09-28 |
| 33 | new | TRM-006 Well section | Used for End-of-Section reports, their approval, and consumption "per section and well"; no source defines it, so the drilling meaning goes in as an assumption for the client's expert to confirm | evaluated | - | QA P1 3, D14, E24 | applied 2026-09-28 |
| 34 | new | TRM-007 Threshold | Our term: the minimum and maximum acceptable value of a fluid parameter; the client asked us to explain it; alias limit | extracted | - | QA E19, E20; BAW 5, 16 | applied 2026-09-28 |
| 35 | no material | Company profile | Founded 2006, Al-Khobar, mud engineering and chemical supply, Saudi Aramco the main customer, QA/QC benchmarked on Aramco specifications. For the A02 and A04 drafts; not a KB type | - | - | RES | recorded 2026-09-28, no note |
| 36 | no material | English only, no Arabic later | The same in every source (QA P1 6, D18; CALL 9; v1 WBS assumption 19); nothing to decide | - | - | QA P1 6, D18; CALL 9 | recorded 2026-09-28, no note |
| 37 | no material | BA draft features the v1 WBS dropped | Sync-monitoring screen, location management, templates, historical import; history, kept in the source | - | - | BAW 7-10 | recorded 2026-09-28, no note |
| 38 | no material | The first call's recording | Recorded in the minutes as the recording link; no transcript exists | - | - | CALL | recorded 2026-09-28, no note |
