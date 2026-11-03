---
type: requirement
id: REQ-007
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-12-30 Answers to the client's questions - rendering]]"
  - "[[2025-11-05 WBS sent to the client - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 1]]"
  - "[[2025-11-20 Client formula and chart samples - rendering]]"
  - "[[2025-10-29 Client sample daily report - rendering]]"
scope_status: contracted
baseline:
  - "WBS:Development Flutter!58"
  - "WBS:Development Flutter!59"
capabilities:
  - "[[CAP-005 Mud engineering calculations and simulation]]"
tags:
  - calculations
  - desktop
---
# REQ-007 Derived values and standard calculations

## Need

On the rig computer, the engineer gets derived values computed when they save their readings, and can
run quick standard calculations to decide a treatment. The client: "Should the app calculate derived
values (e.g., density corrections) automatically on save?" - "Yes"
([[2025-10-29 Client answers to the Q&A register - rendering]] E.21). The first call: "standard
calculations and 'experimenting' - How to increase the mud weight? How many bags of barrites do I
need? I want to change the high water ratio - how much oil do I need to add?"
([[2025-10-22 First call with OES - notes]] key point 5).

Scope: contracted. v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter rows 58 (Derived Value Calculation) and 59 (Standard
Engineering Calculator), both estimated.

## Acceptance criteria

To be written by the BA once the client's formulas are in ([[CON-003 Correct calculations]]).

## Edge cases

| Scenario | Expected behaviour |
|---|---|
| No connection when the engineer calculates | Works: the calculations do not need a central server (v1 WBS, Assumptions & Risks 9) |

## Business rules

- The formulas come from the client (v1 WBS, Assumptions & Risks 12).
- The first call's recording explains the calculations at 47:00 (notes, key point 5); it has no
  transcript.
- The BA draft: "Backend logic to automatically calculate derived values (e.g., density corrections)
  upon the Engineer saving the raw input data" and a calculator "using a set of input variables (e.g.,
  desired weight, current volume)" ([[2025-10-28 BA draft WBS - rendering]] rows 15 and 17).

From the first call's transcript (added 2026-09-28, batch 2):

- Two kinds: "we should have a calculator mode, okay. The, the software will calculate some things
  naturally before it can report them based on the input data. Those are I'll say standard
  calculations, okay. That will be done automatically by the software" - and calculations the
  engineer runs to get something done operationally ([[2025-10-22 First call with OES - transcript]]
  0:52:09).
- Why: today "each engineer will have its own set of tools, you know, that is developed on Excel or
  some basic simple software ... that is not standardized"; with the calculators in the company's tool,
  "everybody's using the same set of calculators" (0:52:09).
- The client's example: "I need to get the mud width from 10 pounds per gallon or SG of 1.4 to 1.6.
  Okay. And I only want to use this chemical. I want to use barite for that. I want to use calcium
  carbonate for that. I want to use a combination of both. Tell me what quantity, how many bag or how
  many metric ton of this to use." (0:47:25) Units: [[REQ-018 Units of measure and conversion]].
- Beyond a calculator, a scope risk: the client expects the tool to point out knock-on effects and
  suggest actions - "by the time you change this mud weight, some of these other parameters will
  change. Please note. And if these parameters change, do you want to do something about it? Okay, and
  these are the suggested things you should do about it ... So if we are building a tool today that
  cannot do that, then I think we've not done a good job." (0:47:25) Nothing in the v1 WBS or the SOW
  v10.4 covers suggestions.
- AI: "Some form of artificial intelligence might be involved, but not heavily" (0:47:25); AI is out of
  scope for the MVP ([[2025-10-29 Client answers to the Q&A register - rendering]] Part 1, 5).
- The formulas are fixed in the desktop app's code: [[DEC-006 Calculations run in the desktop app, formulas fixed in the code]].
- What the client was shown (added 2026-09-28, batch 4): the WBS sent on 5 November 2025 estimated the
  derived values and the calculator "per 1 algorithm" (assumption 26, its Development rows 54 and 55;
  [[2025-11-05 WBS sent to the client - rendering]]). The v1 WBS has no such assumption. See
  [[CON-003 Correct calculations]].
- The initial estimates, as history (AGENTS.md rule 6), hours min to max. v1 WBS: Derived Value
  Calculation, desktop FE 12 to 16, desktop BE 12 to 14, BA 4 to 6 (Development Flutter row 58);
  Standard Engineering Calculator, desktop FE 48 to 56, desktop BE 48 to 64, UI/UX 8 to 10, BA 4 to 6
  (row 59). The WBS sent to the client: derived values, FE 6 to 8, BE 6 to 8, BA 4 to 6 (Development
  row 54); calculator, FE 12 to 16, UI/UX 8 to 10, BA 4 to 6 (row 55).
- Which calculations (added 2026-09-28, batch 6): the client asked to "retain only 'engineering
  calculations'" and to list the essential ones as "included but not limited to the listed items"
  (2025-12-23), then said its samples "were provided as examples" and "the full set of calculations and
  modeling activities is intended to be defined, detailed, and completed during the discovery stage"
  ([[2025-11-25 Contract chat - rendering 1]] 2025-12-23 08:36, 2026-01-05 10:59). See
  [[CON-003 Correct calculations]].
- The client's example derived values (added 2026-09-28, batch 7): the retort solids analysis,
  Equations 10-2 to 10-8 of the client's samples
  ([[2025-11-20 Client formula and chart samples - rendering]] images 1, 2) - volume percent water, oil
  and retort solids, then suspended solids, low-gravity solids and weighting material, and their
  concentrations in lb/bbl, from the retort volumes, the chloride concentration (mg/L) and the fluid
  weight (lb/gal). Defaults where a density is unknown are part of the formulas: "use 4.2 for barite and
  5.0 for hematite", "use 2.6 if unknown" (low-gravity solids), "use 0.84 if unknown" (oil). The
  client's daily report has the inputs (Retort Water %, Retort Solids %, Chlorides mg/l) and an empty
  "Solids Analysis" block ([[2025-10-29 Client sample daily report - rendering]] rows 20, 40, 42, 44).
  Whether these run on save or in the calculator is not stated, and the samples are examples (above).

## Out of scope
