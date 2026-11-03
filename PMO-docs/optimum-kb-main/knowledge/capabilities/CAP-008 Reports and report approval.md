---
type: capability
id: CAP-008
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: business
baseline:
  - "WBS:Development Flutter!33-37"
  - "WBS:Development Flutter!68-71"
  - "SOW:M6 Reporting"
depends_on:
  - "[[CAP-004 Shift measurements and quality control]]"
  - "[[CAP-005 Mud engineering calculations and simulation]]"
  - "[[CAP-006 Inventory]]"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - capability
  - reports
---
# CAP-008 Reports and report approval

## What it must do

The desktop generates the four operational reports; the web views and exports reports per project
and formally approves or locks the end-of-section and end-of-well reports
([[2026-06-15 SOW v10.4 - rendering]] row 11, Milestone 6, Reporting on the web and on the desktop).
What a report is, is disputed ([[TRM-001 Report]]).

## Coverage criteria

Drafted from the SOW v10.4 wording (row 11); the TL owns these.

- C1 The desktop generates the end-of-day, end-of-section, end-of-well (summarising the data,
  inventory and simulation results across the project) and inventory reports (M6).
- C2 Every report is filterable and exportable to PDF, CSV and spreadsheet (M6).
- C3 On the web, reports are viewed and exported per project (M6).
- C4 On the web, end-of-section and end-of-well reports can be formally approved or locked (M6).

Not included: sending reports to anyone. "Reports sending to Client is out of the solution scope"
([[2026-09-25 v1 WBS - rendering]], Assumptions & Risks, assumption 18).

## Refined by

- [[REQ-010 Reports]]
- [[REQ-002 Managers see engineers' reports in the web app]]
- [[REQ-017 Report on a single calculation or simulation]] (a change request candidate: the rows name
  four report types)
- [[TRM-001 Report]] (disputed)
- [[QUE-004 Is a separate engineering calculation report expected]]

## Plan

M6.
