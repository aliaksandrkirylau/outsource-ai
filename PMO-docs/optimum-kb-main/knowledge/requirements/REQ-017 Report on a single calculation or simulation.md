---
type: requirement
id: REQ-017
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-11-03 Solution proposal - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-11-20 Client formula and chart samples - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 1]]"
scope_status: proposed-change
baseline:
  - "WBS:Development Flutter!67"
capabilities:
  - "[[CAP-008 Reports and report approval]]"
tags:
  - reports
  - calculations
  - change-request-candidate
---
# REQ-017 Report on a single calculation or simulation

## Need

The engineer runs one engineering calculation or simulation and produces a report of just that. The
client: "there may be situation whereby we just. The engineer just want to be able to do an
engineering calculation or simulation and generate report just for that, for example."
([[2025-10-22 First call with OES - transcript]] 0:37:48). The client also listed "Engineering
calculation/simulation" among the MVP reports
([[2025-10-29 Client answers to the Q&A register - rendering]] Part 1, 3), and the presale proposal had
"Engineering Calculation reports" as an objective ([[2025-11-03 Solution proposal - rendering]]).

Scope: a change request candidate. The v1 WBS ([[2026-09-25 v1 WBS - rendering]]) and the SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) have four report
types - End-of-Day, End-of-Section, End-of-Well, inventory - with simulation results summarised in the
End-of-Well report; nearest line Development Flutter row 67 (desktop Reporting). This note records
the answer to [[QUE-004 Is a separate engineering calculation report expected]].

## Acceptance criteria

Not written: first settle whether it is in scope.

## Edge cases

| Scenario | Expected behaviour |
|---|---|

## Business rules

- Calculations and simulations: [[REQ-007 Derived values and standard calculations]],
  [[REQ-008 Fluid hydraulics simulation]]. The other report types: [[REQ-010 Reports]].
- The client's samples include three output pages of a hydraulics program, one calculation each, with
  tables and charts ([[2025-11-20 Client formula and chart samples - rendering]] images 8 to 10; added
  2026-09-28, batch 7). The client sent them as examples of calculations and diagrams ("the formulas and
  diagrams that we had already shared which were provided as examples",
  [[2025-11-25 Contract chat - rendering 1]] 2026-01-05 10:59), not as a report layout; what a
  single-calculation report must hold is not stated.

## Out of scope
