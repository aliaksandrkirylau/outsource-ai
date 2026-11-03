---
type: question
id: QUE-013
status: proposed
origin: evaluated
author: claude-code/claude-opus-5-5
asks: client
answered_by:
sources:
  - "[[2026-11-02 Client sample engineering reports - rendering]]"
  - "[[2025-11-20 Client formula and chart samples - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - simulation
  - hydraulics
---
# QUE-013 Which calculations from the sample reports the simulation must cover

## Question

Of the calculations in the client's sample program reports, which must our simulation cover?

## What it blocks

The acceptance criteria and the estimate of v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development
Flutter row 60, "Simulation: Fluid Hydraulics": "Output includes "what if" scenarios (e.g., impact
of changing flow rates) with chart visualizations and data tables showing predictive outcomes.
Charts are not complex (bar charts, curves x-y, etc.)". Notes:
[[REQ-008 Fluid hydraulics simulation]], [[CON-003 Correct calculations]].

## Options

1. Fluid hydraulics as row 60 words it: pressure losses, bit hydraulics, ECD, hole cleaning,
   flow-rate what-ifs and the operating window
   ([[2026-11-02 Client sample engineering reports - rendering]], [[2026-11-02 Client sample engineering reports - Hydraulics Design Frame Sample.pdf|Hydraulics Design Frame Sample]],
   [[2026-11-02 Client sample engineering reports - Hydraulics Report Sample.pdf|Hydraulics Report Sample]]).
2. Option 1 plus surge and swab against trip speed ([[2026-11-02 Client sample engineering reports - Surge Report Sample.pdf|Surge Report Sample]]; also in the 2025 samples,
   [[2025-11-20 Client formula and chart samples - rendering]] images 6 and 9).
3. Option 2 plus results at several depths and ROPs ([[2026-11-02 Client sample engineering reports - Hydraulics Report Sample 2.pdf|Hydraulics Report Sample 2]], "MULTIPLE DEPTH"
   and "SENSITIVITY").
4. Option 3 plus torque and drag: loads along the string, torque, buckling and fatigue ([[2026-11-02 Client sample engineering reports - Torque and Drag Sample.pdf|Torque and Drag Sample]]). Drill string mechanics rather than fluid hydraulics (evaluated), outside row 60's
   wording: a change request candidate if the client wants it.

## Answer

None yet. The client sent the six as "the remaining sample reports for your reference" (Ms. Zahra,
2026-11-02 08:26 UTC; [[2026-11-02 Client sample engineering reports - overview]]), without saying
which it expects.
