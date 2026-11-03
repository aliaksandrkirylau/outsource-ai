---
type: requirement
id: REQ-018
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-11-05 Proposal slides - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-29 Client sample daily report - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
  - "[[2025-11-20 Client formula and chart samples - rendering]]"
  - "[[2026-11-02 Client sample daily mud reports - rendering]]"
  - "[[2026-11-02 Client sample end-of-well recap - rendering]]"
  - "[[2026-11-02 Client sample engineering reports - rendering]]"
scope_status: contracted
baseline:
  - "WBS:Development Flutter!22"
  - "WBS:Development Flutter!54"
capabilities:
  - "[[CAP-007 Units of measure]]"
tags:
  - units
---
# REQ-018 Units of measure and conversion

## Need

Measurements are entered and shown in the unit system the user works in, and the app converts between
units. Added in presale's third iteration: "Additionally unit management system was added to the
scope." ([[2025-11-05 Proposal slides - rendering]] slide 28)

Where it came from (added 2026-09-28, batch 5): the consultant who read the client's calculation
samples: "Я бы сразу закладывал работу и с метрическими единицами измерения и конвертацию одних единиц
измерения в другие, тут надо уточнить" ([[2025-10-20 Presale chat - rendering 2]] 2025-11-24 12:37);
the WBS was re-estimated the same day with "(+выбор системы измерения)" (15:35).

The client works in several units in one breath: "I need to get the mud width from 10 pounds per
gallon or SG of 1.4 to 1.6 ... Tell me what quantity, how many bag or how many metric ton of this to
use" ([[2025-10-22 First call with OES - transcript]] 0:47:25); concentration "in pounds/barrel & %"
([[2025-10-29 Client answers to the Q&A register - rendering]] E.24); the client's sample report mixes
ppg, ft, bbl, psi, cP, lb/bbl and gal/min
([[2025-10-29 Client sample daily report - rendering]]).

Scope: contracted. v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter rows 22 (web) and 54 (desktop), both "Metric system
customizing": "Choosing metric units used for measurements and the conversion of one unit of
measurement into another, including validation rules. Assumption - 3 data sets." (row 22; row 54 says
"3 sets"), estimated. The SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) has "metric and units handling" among the
Milestone 1 clarifications.

## Acceptance criteria

To be written by the BA.

## Edge cases

| Scenario | Expected behaviour |
|---|---|
| A value entered in one unit is shown to a user who works in another | Not defined in these sources |

## Business rules

- Three unit sets are assumed (v1 WBS rows 22 and 54); which three is not stated.
- The client's samples mix units within one set (added 2026-09-28, batch 7;
  [[2025-11-20 Client formula and chart samples - rendering]]): mud weight and ECD in lb/ft^3 on the
  program screens (images 8 to 10), fluid weight in lb/gal in Equation 10-6 (image 2), ECD in ppg in
  the daily report (rows 43, 44); densities in g/cm^3, chloride in mg/L, concentrations in lb/bbl,
  pressure in psi, flow in USgal/min, depth in ft, diameters in in, volumes in bbl, trip speed in s/std.
  The constants in the procedures (0.052, 0.408, 928, 25.81, 2.45, 3.50) hold only in the units the
  formulas were written for, which the procedures do not state (evaluated): converting the inputs, or
  the formulas, needs the client to confirm each unit.
- Units in the client's samples of 2 November 2026 (added 2026-11-02): mud weight and ECD in lb/ft^3
  in both daily reports, the end-of-well report and every program report
  ([[2026-11-02 Client sample daily mud reports - rendering]],
  [[2026-11-02 Client sample end-of-well recap - rendering]],
  [[2026-11-02 Client sample engineering reports - rendering]]), where the 2025 form had ppg; solids
  density in g/cc and lb/gal ([[2026-11-02 Client sample daily mud reports - DMR Sample 1.pdf|DMR Sample 1]]); chlorides in mg/l in the daily reports and g/l in the
  end-of-well report (pp [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=19|19]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=24|24]]); one program report mixes metric and field units (m, L/min, sg, m³
  with psi, in, ft/s; [[2026-11-02 Client sample engineering reports - Hydraulics Analysis Sample.pdf|Hydraulics Analysis Sample]]); products in lb, kg, gal, L, bbl and m3.

## Out of scope
