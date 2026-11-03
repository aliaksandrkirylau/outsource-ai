---
type: source
kind: document
date: 2026-09-25
original: https://docs.google.com/spreadsheets/d/10H7vDQCbev_-jC6y0J5zeCw1Os2n-6MfJiAVb0k2hbg
received_from: Arseniy Klimenko (DM), in the [Core] Optimum engineering chat on 2026-09-25, as the current WBS
purpose: the scope reference for scope checks - the current estimate (the Flutter roll-up) the delivery is planned against
supersedes: "[[2025-11-05 WBS sent to the client - overview]]"
procedure_version: b4cb7da
---
# 2026-09-25 v1 WBS - overview

kind: document, internal (`sources/internal/`). The date is the day Arseniy named it the current WBS;
the sheet was read on 2026-09-28. Rendering: [[2026-09-25 v1 WBS - rendering]]. It supersedes, as the
estimate, the version sent to the client on 5 November 2025,
[[2025-11-05 WBS sent to the client - overview]], which is a separate sheet.

## What it is

The Google Sheet "v1 EST - Optimum Engineering Standards - ASnot - SA - Big data - 023690", with ten
tabs: Overview, Sheet11 (empty), Total Estimation Discovery, Total Estimation Development (the MAUI
roll-up), Total Estimation Development Flutter (the Flutter roll-up), Development MAUI, Development
Flutter, DevOps, Assumptions & Risks, Infrastructure Costs. Rendered: Overview, Total Estimation
Discovery, the Flutter roll-up, Development Flutter, DevOps, Assumptions & Risks.

The current estimate is the Flutter roll-up. Arseniy's pack in the [Core] chat, 2026-09-25 11:53 UTC:
"Здесь актуальная WBS (смотрим на оценку с флатером. Тут есть еще один столбец, в девелопменте. Это
просто обычные часы + стабилизация)". The same message links the SOW v10.4, the P&L and the client's
materials folder. The chat's only other message (2026-09-28) belongs to that day's call and is not used
here.

History, from the contract chat ([[2025-11-25 Contract chat - rendering 1]]): Marina Zaretskaya shared "v1 EST" with the project
description on 2025-11-25; it was linked into the SOW exhibit on 2025-11-26; on 2025-11-28, asked
whether the grand total is the development roll-up alone or discovery plus development, Marina
Zaretskaya answered "сложить" (add them).

How it was estimated, from [[2026-09-25 Optimum Eng sync - transcript]] (Arseniy, 00:22:01):
"Эстимации по старинке делались. уже больше года назад"; the time given was "40 минут"; it was
estimated for "myui, десктоп дотнетовский"; "все цифры, когда были даны тогда, они актуальны"; the
stack moved to Flutter, "Флаттер тут безопаснее, просто по наличию экспертизы". Estimated the
traditional way, not for AI-assisted coding (00:21:50, 00:22:01). Arseniy did not make the estimate; he
reviewed it, "недавно еще одно делали" (00:21:38).

## How far to trust it

Our own view (`sources/internal/`), and the scope reference for scope checks. It is not a commitment:
"should not be considered as a commitment from the implementation team to meet these hours and
timelines" (Overview, row 25). The client never saw this sheet; what they saw is the 5 November 2025
version.

Read it with these in mind:

- Only lines with TRUE in "Development Flutter" column Q count: the roll-up reads the "Total MVP" row
  (98). Mobile (rows 75 to 88), the onboarding wizard (48), location management (23) and project
  templates (24) are FALSE, so outside the estimate.
- The Overview tab and some Flutter text are from the MAUI estimate: ".NET or Java", MAUI, ReactJS in
  the Overview, "Created 05.07.2025", "the same NET MAUI both for desktop and mobile" (row 75),
  "ASP.NET or Keylock" (rows 17, 47, 77).
- Two columns headed "Rate, USD/hour" hold hours, not rates: the roll-up's column E is the max plus 15%
  (Arseniy's "обычные часы + стабилизация"); the Discovery tab's column D is the max plus 10 hours from
  "Other" (Marina Zaretskaya, contract chat 2025-11-28: "это не рейт").
- "Development Flutter" columns C and D ("MLT") mostly add up the wrong rows and are not used anywhere;
  row 99 "Total sum" mixes the Flutter MVP hours with the MAUI roll-up's QA, PM and DevOps. The
  roll-up's TOTAL (row 28) is the figure.
- Every "Development Flutter" row and every "Assumptions & Risks" number the notes cited from batches 1
  to 3 matches the sheet (checked 2026-09-28).

## Not for

Technical decisions from the estimate hours (they are a planning landmark, not a design input), or
current estimates in notes (AGENTS.md rule 6: they live in Jira and the P&L; a note may quote a line's
initial estimate as history). Not a statement of what
the client agreed: that is the contract and the SOW.

## Removed at ingest

The company address and phone number; the "Estimate, USD" columns and the "Forecasted Cost (USD)" row,
which hold only zeros or nothing. Not rendered: the MAUI tabs (Total Estimation Development and
Development MAUI, kept as link-only parts of this sheet, with their totals named in the rendering where a
Flutter formula uses them), Infrastructure Costs (money), Sheet11 (empty).

## Summary

Flutter roll-up: design, four development lines (web and desktop, back and front end), QA at 30% of
development plus 15% stabilization, PM over four to five months, BA at 25% of development, DevOps from
its own tab, architecture "accounted in discovery"; timeline 4 to 6 months. The team shape in the
Overview: 2 front-end, 2 back-end, 1 BA, 1 UI/UX, 1 QA, 0.5 PM, 0.5 DevOps, a data engineer on demand.
Discovery is estimated separately (PM, BA, UI/UX, SA - "Solution Architect" - and "Other"). The DevOps
tab is written for a cloud (Terraform modules, CloudWatch, load balancers) and has no line for
updating the rig desktops or for security testing. 24 assumptions (numbered to 25, no 24) and 8 risks,
the same as in the 5 November 2025 version except that version's assumption 26.

Compared with the version sent to the client on 5 November 2025
([[2025-11-05 WBS sent to the client - rendering]]): MAUI and "Cross Platform" there, Flutter and
desktop plus web here; mobile, the onboarding wizard, location management and templates in the MVP
there, outside it here; an on-premises DevOps tab with a desktop update pipeline there, a cloud one
without it here; a units line here only (rows 22, 54); the calculator and simulation lines estimated
"per 1 algorithm" there (its assumption 26), with no such assumption here.

Companion files to store link-only (old estimate, DevOps estimate, resource plan, April hours plan):
not stored here; their links are to be taken from the presale chat in batch 5.

## Proposed changes

The batch 4 table. Source keys: WBS = [[2026-09-25 v1 WBS - rendering]] (tab and row, or
"Assumptions & Risks" number); SENT = [[2025-11-05 WBS sent to the client - rendering]] (tab and row, or
assumption number); SOW = [[2026-06-15 SOW v10.4 - rendering]]; SYNC =
[[2026-09-25 Optimum Eng sync - transcript]]; CC = [[2025-11-25 Contract chat - rendering 1]].

No note in this batch carries hours. New notes are draft. Approved by Anton on 2026-09-28: all rows;
the companion files go to batch 5; the folder date and `supersedes` stand. After the rows were applied,
Anton changed rule 6 (initial estimates may be quoted as history), and the initial hours were added to
CON-002, CON-003, REQ-007 and REQ-008 the same day.

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | new | REQ-020 Create and manage well jobs and assign engineers | At HQ: create and edit projects (well jobs), assign and reassign engineers, list and filter projects, view details. On the desktop the engineer creates a project entry, or selects and updates one, with its details (location, client info), and it gets an active status and an ID. Assigning is on the web only. Out: project templates, bulk assignment, location management. No note held this; the SOW puts it in Milestone 3 | extracted | contracted, Development Flutter!26 (also !27, !50) | WBS Development Flutter 23, 24, 26, 27, 50; SOW Milestone 3 | applied 2026-09-28 |
| 2 | update | REQ-002 Managers see engineers' reports in the web app | Add the HQ view of the raw measurement entries, "up to 50 parameters" | extracted | contracted, Development Flutter!32 (unchanged), adds !28 | WBS Development Flutter 28 | applied 2026-09-28 |
| 3 | update | REQ-005 Parameter thresholds and entry alerts | Add the HQ side: "review data streams from their assigned rigs with entries flagged for threshold violations highlighted" | extracted | contracted, adds Development Flutter!29 | WBS Development Flutter 29 | applied 2026-09-28 |
| 4 | update | REQ-013 Mobile app | History: the WBS sent to the client on 5 November 2025 had mobile in the MVP ("Web application and Cross Platform application", mobile rows all TRUE); the v1 WBS moved it out | extracted | out-of-scope (unchanged) | SENT Overview 7, Development 71-84; CC 2025-12-01 | applied 2026-09-28 |
| 5 | update | REQ-014 Onboarding wizard for new users | History: in the MVP of the WBS sent to the client (TRUE), outside the v1 estimate (FALSE) | extracted | out-of-scope (unchanged) | SENT Development 47; WBS Development Flutter 48 | applied 2026-09-28 |
| 6 | update | CON-003 Correct calculations | What the client was shown: the calculations and simulation estimated "per 1 algorithm" because of "uncertainty regarding the complexity of calculations/simulation and the number of algorithms required"; the v1 WBS has no such assumption. Replace the "stored in batch 4" placeholder with the link | extracted | - | SENT assumption 26; WBS assumption 12 | applied 2026-09-28 |
| 7 | update | REQ-007 Derived values and standard calculations | The same "per 1 algorithm" line (SENT rows 54, 55) | extracted | contracted (unchanged) | SENT assumption 26 | applied 2026-09-28 |
| 8 | update | REQ-008 Fluid hydraulics simulation | The same "per 1 algorithm" line (SENT row 56) | extracted | contracted (unchanged) | SENT assumption 26 | applied 2026-09-28 |
| 9 | update | CON-002 Deployment outside public cloud | The v1 WBS DevOps tab is written for a cloud (ready-made Terraform modules, CloudWatch, load balancers) and has no line for getting updates to the rig desktops. The WBS sent to the client was on-premises (VMs, Ansible/Terraform) and had "CRITICAL: ... a robust auto-update/forced-update mechanism for 70+ remote Windows clients over sketchy connectivity" | evaluated | - | WBS DevOps 6-16; SENT DevOps 6-14 | applied 2026-09-28 |
| 10 | update | CON-001 Offline operation and sync between rigs and HQ | Confirmed: neither WBS has a development line for sync; the v1 architecture line is "accounted in discovery"; the WBS sent to the client had monitoring alarms for "Site Synchronization Lag (70+ unique alarms)" | extracted | - | WBS roll-up 27; SENT DevOps 17 | applied 2026-09-28 |
| 11 | update | QUE-005 Is the client an NCA Category A or B entity | Checked: no penetration testing in either WBS. The v1 DevOps tab has no security testing line, and QA is a percentage of development with no breakdown; the WBS sent to the client had SAST in CI and RBAC tests, not penetration testing. Name the lines it blocks | evaluated | blocks Total Estimation Development Flutter!25 (and !17) | WBS DevOps 6-16, roll-up 17, 25; SENT DevOps 12, 21 | applied 2026-09-28 |
| 12 | update | QUE-001 Why a desktop at the rig, and tablets later | Name the lines it blocks: the roll-up's Total design and the UI Kit line | evaluated | blocks Total Estimation Development Flutter!9 (and Development Flutter!6) | WBS roll-up 9; Development Flutter 6 | applied 2026-09-28 |
| 13 | update | DEC-004 Backend stack | Context: the v1 WBS Overview still names the presale stack (".NET or Java", MAUI, ReactJS) and 2 front-end and 2 back-end developers; the Flutter roll-up names no backend and has four development lines. Arseniy: the original estimate's backend is "какой-то там нода питон". How the estimate was made (MAUI, over a year ago, 40 minutes, "все цифры ... актуальны") | extracted | names Total Estimation Development Flutter!11 to !14 | WBS Overview 8, 10, 11; roll-up 11-14; SYNC 00:16:40, 00:22:01 | applied 2026-09-28 |
| 14 | update | COM-004 Twelve-month warranty | The v1 WBS carries no effort for the warranty: "Post-deployment support efforts are not included"; the DevOps post-release line is "Optional", otherwise "the development team remains responsible for the first weeks after release" | evaluated | - | WBS assumption 25, DevOps 15 | applied 2026-09-28 |
| 15 | update | The 26 notes that name the v1 WBS in plain text | Link the first mention in each to the rendering and add it to `sources` (script in `pm/seed-ingest-scripts/`) | - | - | - | applied 2026-09-28 |
| 16 | no material | Row numbers in the notes | Every "Development Flutter" row and "Assumptions & Risks" number cited in batches 1 to 3 matches the sheet | - | - | WBS | recorded 2026-09-28, no note |
| 17 | no material | Hours, team shape, timeline | Stay in the source (rule 6); the sheet itself says it is not a commitment | - | - | WBS Overview 10-25 | recorded 2026-09-28, no note |
| 18 | no material | The WBS risks | Eight risks in each version; they belong in the PMO risk register when it is filed, linked from notes | - | - | WBS Assumptions & Risks 37-44 | recorded 2026-09-28, no note |
| 19 | no material | Units line | Only in the v1 WBS (rows 22, 54), as REQ-018 already records ("added to the scope") | - | - | WBS Development Flutter 22, 54 | recorded 2026-09-28, no note |
| 20 | no material | Discovery plan | The Discovery tab's notes (SAD, vision and scope, user stories for two sprints, designs, plan, WBS, UI kit) overlap with the SOW's Milestone 1 deliverables in COM-020; nothing new | - | - | WBS Discovery L6-P12 | recorded 2026-09-28, no note |
