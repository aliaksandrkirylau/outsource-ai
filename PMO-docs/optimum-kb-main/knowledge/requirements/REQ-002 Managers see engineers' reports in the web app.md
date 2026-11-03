---
type: requirement
id: REQ-002
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
scope_status: contracted
baseline:
  - "WBS:Development Flutter!28"
  - "WBS:Development Flutter!32-37"
capabilities:
  - "[[CAP-008 Reports and report approval]]"
tags:
  - web
---
# REQ-002 Managers see engineers' reports in the web app

## Need

Administrative staff see the result of the on-site engineers' work - each [[TRM-001 Report]] - in a
web admin panel, plus related functions not detailed in this source
([[2026-09-25 Optimum Eng sync - transcript]] 00:08:12).

Scope: contracted. v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter row 32 (web Reporting: approval flow and the four report
types, rows 33 to 37, estimated). The report types themselves are in [[REQ-010 Reports]]. Row 28
(Measurements, web, estimated) covers the raw entries; added 2026-09-28, batch 4.

## Acceptance criteria

To be written by the BA.

## Edge cases

| Scenario | Expected behaviour |
|---|---|

## Business rules

Added 2026-09-28 from the client's October 2025 answers
([[2025-10-29 Client answers to the Q&A register - rendering]]):

- Who reads reports at HQ: "Access to Report and System: Field Supervisors, Project Engineers,
  Operations Support, and Operations Manager." (C.10)
- "Supervisor: Review and generate reports"; "Manager: Access dashboards, oversee multiple sites"
  (D.13). The role set is disputed: [[REQ-004 Roles and what each role can do]].
- Section and well reports are signed off; nothing else is (D.14).

Added 2026-09-28 (batch 4): HQ also sees what the engineers entered, before any report: "View the raw
measurement entries inputted by the Engineers (up to 50 parameters)" ([[2026-09-25 v1 WBS - rendering]],
Development Flutter row 28). Projects and their assignment are [[REQ-020 Create and manage well jobs and assign engineers]].

## Out of scope
