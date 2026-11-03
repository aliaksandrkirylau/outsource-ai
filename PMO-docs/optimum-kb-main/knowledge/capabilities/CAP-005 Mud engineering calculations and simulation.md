---
type: capability
id: CAP-005
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: business
baseline:
  - "WBS:Development Flutter!58"
  - "WBS:Development Flutter!59"
  - "WBS:Development Flutter!60"
  - "SOW:M5 Derived value calculation"
  - "SOW:M5 Standard engineering calculator"
  - "SOW:M5 Fluid hydraulics simulation"
depends_on:
  - "[[CAP-004 Shift measurements and quality control]]"
  - "[[CAP-007 Units of measure]]"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - capability
  - calculations
---
# CAP-005 Mud engineering calculations and simulation

## What it must do

The desktop calculates from the client's formulas: derived values when raw input is saved, a
calculator for standard engineering calculations, and a fluid hydraulics simulation that shows "what
if" outcomes as data tables and simple charts. "All three calculation features run offline without
needing a central server" ([[2026-06-15 SOW v10.4 - rendering]] row 11, Milestone 5;
[[DEC-006 Calculations run in the desktop app, formulas fixed in the code]]).

The estimate assumes the client provides clear formulas, no 3D and no complex modelling (v1 WBS tab
Assumptions & Risks, assumptions 12, 13 and 17), and presale rated two of its risks high: the
complexity of the calculation modules and the client's support for them (risks 2 and 5;
[[2026-09-25 v1 WBS - rendering]]).

## Coverage criteria

Drafted from the SOW v10.4 wording (row 11); the TL owns these.

- C1 Derived values (for example density corrections) are calculated automatically when the engineer
  saves raw input, using the client's formulas (M5).
- C2 The calculator runs the standard calculations from a set of input variables, using the client's
  formulas (M5).
- C3 The hydraulics simulation takes well architecture, rheology data and flow rates and shows what-if
  outcomes as data tables and simple charts (M5).
- C4 All three run offline, with no central server (M5).
- C5 Results match the client's formulas, confirmed by the client's subject expert
  ([[CON-003 Correct calculations]]). Which rheological model applies is open
  ([[QUE-008 Which rheological model the hydraulics must use]]).

## Refined by

- [[REQ-007 Derived values and standard calculations]]
- [[REQ-008 Fluid hydraulics simulation]]
- [[CON-003 Correct calculations]]
- [[DEC-006 Calculations run in the desktop app, formulas fixed in the code]]
- [[QUE-003 Do calculations and modelling need 3D or complex visuals]]
- [[QUE-004 Is a separate engineering calculation report expected]]
- [[QUE-008 Which rheological model the hydraulics must use]]
- [[QUE-010 Are past results recalculated when a formula or threshold changes]]
- [[TRM-009 ECD]]

## Plan

Built M5. The Milestone 5 specifications need "the formulas and calculation logic supplied by the
Customer" (row 11, Milestone 5), so the formulas have to be in hand before then. Asking for them,
and for a named client expert, in Discovery is our proposal, not the SOW's.
