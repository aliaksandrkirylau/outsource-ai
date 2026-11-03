---
type: question
id: QUE-008
status: proposed
origin: evaluated
author: claude-code/claude-opus-5-5
asks: client
answered_by:
sources:
  - "[[2025-11-20 Client formula and chart samples - rendering]]"
  - "[[2025-10-29 Client sample daily report - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 1]]"
  - "[[2026-11-02 Client sample engineering reports - rendering]]"
  - "[[2026-11-02 Client sample daily mud reports - rendering]]"
tags:
  - calculations
  - simulation
  - hydraulics
---
# QUE-008 Which rheological model the hydraulics must use

## Question

Which rheological model must the hydraulics calculations and the simulation use: the power law,
Herschel-Bulkley, or both?

## What it blocks

The acceptance criteria of v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter row 60
(Simulation: Fluid Hydraulics), and of rows 58 and 59 where they compute n, K or ECD. Notes:
[[REQ-008 Fluid hydraulics simulation]], [[CON-003 Correct calculations]].

## Options

- Power law, as in the client's step-by-step procedures: n and K from the Fann readings, "n_a = 0.5
  log(θ_300 / θ_3)" in the annulus and "n_p = 3.32 log(θ_600 / θ_300)" in the pipe
  ([[2025-11-20 Client formula and chart samples - rendering]] images 3 to 7).
- Herschel-Bulkley, as on the client's program screen: "Rheological Model Herschel-Bulkley" with "K:
  0.749[#sec^n/100ft^2] N: 0.689[-] YP: 9.000[lbf/100ft^2]" (image 8).
- Both, the engineer choosing per calculation. The program shows the model as a field (image 8), which
  suggests a choice there (evaluated).
- Robertson-Stiff (added 2026-11-02), on one of the client's program reports: "Rheological Model:
  Robertson-Stiff", with a "Herschel-Bulkley" line of K, N and YP beside it
  ([[2026-11-02 Client sample engineering reports - rendering]], [[2026-11-02 Client sample engineering reports - Hydraulics Report Sample.pdf#page=1|Hydraulics Report Sample p1]]).
- Bingham, named with the power law on another: "Model: Power Law / Bingham", its parameters
  labelled "H-B K", "H-B n", "H-B YS" ([[2026-11-02 Client sample engineering reports - Hydraulics Report Sample 2.pdf#page=1|Hydraulics Report Sample 2 p1]]).
- A third names "Fluid Model: Yield-Power" ([[2026-11-02 Client sample engineering reports - Hydraulics Analysis Sample.pdf|Hydraulics Analysis Sample]]), the yield power law, which
  is Herschel-Bulkley by another name (evaluated).

## Answer

None yet. The client's daily report has "Behavior Index (n)" and "Consistency Index (k)" under
"Hydrualic Analysis" ([[2025-10-29 Client sample daily report - rendering]] rows 41, 42), which fits
either model. The client said the full set of calculations and modelling is to be defined in discovery
([[2025-11-25 Contract chat - rendering 1]] 2026-01-05 10:59).

Still open after the client's samples of 2 November 2026 (added 2026-11-02): three program reports
name three models, and the daily report gives n and k with no model named
([[2026-11-02 Client sample daily mud reports - rendering]], [[2026-11-02 Client sample daily mud reports - DMR Sample 1.pdf|DMR Sample 1]] "Hydraulic Analysis").
