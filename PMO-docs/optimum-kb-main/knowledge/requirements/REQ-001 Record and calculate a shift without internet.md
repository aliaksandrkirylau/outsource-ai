---
type: requirement
id: REQ-001
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
scope_status: contracted
baseline:
  - "WBS:Development Flutter!51"
  - "SOW:M3 Synchronization with backend logic"
capabilities:
  - "[[CAP-002 Offline data and sync between rigs and HQ]]"
  - "[[CAP-004 Shift measurements and quality control]]"
tags:
  - offline
  - desktop
---
# REQ-001 Record and calculate a shift without internet

## Need

An on-site engineer opens a [[TRM-002 Shift]], enters readings, runs the calculations and closes the
shift on the desktop with no internet connection; the data syncs to the central database when a
connection appears ([[2026-09-25 Optimum Eng sync - transcript]] 00:08:12). Why: the rigs cannot rely
on connectivity ([[CON-001 Offline operation and sync between rigs and HQ]]).

Scope: contracted. v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter row 51 (Measurements input, desktop, estimated). The v1
WBS has no line for sync; the SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) puts syncing project and measurement data
in Milestone 3.

## Acceptance criteria

To be written by the BA.

## Edge cases

| Scenario | Expected behaviour |
|---|---|

## Business rules

Added 2026-09-28 from the client's October 2025 answers:

- Readings are entered by hand: "Are the measurement parameters limited to less than 50, and are they
  manually inputted approximately 4 times per day?" - "Yes"
  ([[2025-10-29 Client answers to the Q&A register - rendering]] Part 1, 2); "input measured onsite
  data manually" ([[2025-10-22 First call with OES - notes]] key point 5). No sensors: data collection
  from sensors is out of scope (Part 1, 5).
- Shifts are 12 hours (F.28).
- One rig computer is shared by 1 to 4 engineers (Part 1, 9); each signs in
  ([[REQ-003 Sign in on a shared rig computer]]).
- "Each work location should have local access to their own data." (Part 1, 8)
- Derived values are calculated on save ([[REQ-007 Derived values and standard calculations]]).

## Out of scope

- Data collection from sensors (Part 1, 5).
