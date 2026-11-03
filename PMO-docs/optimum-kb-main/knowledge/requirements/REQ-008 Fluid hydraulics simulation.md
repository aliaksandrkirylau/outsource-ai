---
type: requirement
id: REQ-008
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-10-23 OES company research - rendering]]"
  - "[[2025-10-29 Client sample daily report - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-11-05 WBS sent to the client - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
  - "[[2025-11-20 Client formula and chart samples - rendering]]"
  - "[[2026-11-02 Client sample engineering reports - rendering]]"
  - "[[2026-11-02 Client sample daily mud reports - rendering]]"
scope_status: contracted
baseline:
  - "WBS:Development Flutter!60"
capabilities:
  - "[[CAP-005 Mud engineering calculations and simulation]]"
tags:
  - simulation
  - hydraulics
  - desktop
---
# REQ-008 Fluid hydraulics simulation

## Need

The engineer models how the drilling fluid behaves in the well for different scenarios, to plan and
reduce risk. The first call: "The client wants to see what's the fluid hydraulics looking like on
that different scenario, based on the architecture or the profile of the well that we are drilling"
([[2025-10-22 First call with OES - notes]] key point 5). The first request asked for "simulation
capabilities for planning and risk mitigation" ([[2025-10-23 OES company research - rendering]],
Initial Request).

Scope: contracted. v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter row 60 (Simulation: Fluid Hydraulics, estimated).

## Acceptance criteria

To be written by the BA once the client's modelling logic is in ([[CON-003 Correct calculations]]).

## Edge cases

| Scenario | Expected behaviour |
|---|---|
| No connection when the engineer runs a simulation | Works: modelling does not need a central server (v1 WBS, Assumptions & Risks 9) |

## Business rules

- Inputs, in the client's words: "The well architecture/configuration (including casing size/depth,
  open hole size/depth, well survey data), drill string/BHA details, drilling fluids parameters
  (density, rheology etc), mud pump parameters, bit parameters, formation parameters (fracture
  pressure, pore pressure, bottom hole static/dynamic temperature etc)"
  ([[2025-10-29 Client answers to the Q&A register - rendering]] E.25).
- What the client was shown (added 2026-09-28, batch 4): the WBS sent on 5 November 2025 estimated the
  simulation "per 1 algorithm" (assumption 26, its Development row 56;
  [[2025-11-05 WBS sent to the client - rendering]]). The v1 WBS has no such assumption. See
  [[CON-003 Correct calculations]].
- The client's materials of November 2025 carry no description of the modelling logic: "Не нашел
  описания логики моделирования" (the consultant who read them,
  [[2025-10-20 Presale chat - rendering 2]] 2025-11-24 12:37; added 2026-09-28, batch 5). To fit the
  budget, an option without it was considered: "подготовила опцию без расчета гидравлики еще"
  (Marina Zaretskaya, 2025-11-12 11:58).
- The initial estimates, as history (AGENTS.md rule 6), hours min to max. v1 WBS: desktop FE 80 to 88,
  desktop BE 56 to 72, UI/UX 12 to 14, BA 4 to 6 (Development Flutter row 60). The WBS sent to the
  client: FE 24 to 32, no back end, UI/UX 12 to 14, BA 4 to 6 (Development row 56).
- Output: "'what if' scenarios (e.g., impact of changing flow rates) with chart visualizations and
  data tables showing predictive outcomes" ([[2025-10-28 BA draft WBS - rendering]] row 18).
- How rich the charts must be is open: [[QUE-003 Do calculations and modelling need 3D or complex visuals]].
  The v1 WBS estimates simple charts and excludes complex modelling (Assumptions & Risks 11, 13, 17).
- The client's hydraulics report sheet is empty in the sample
  ([[2025-10-29 Client sample daily report - rendering]], "Hydraulics Report").
- The operating window (added 2026-09-28, batch 2): "maybe they're drilling with 500 gpm gallons flow
  rate and they're thinking of increasing the flow rate. And I want to see, okay, what will be impacted
  ... and can the system determine an ideal flow rate, that there should be flow it window that they
  should be operating within, below which, okay, maybe they are not cleaning the well properly or above
  which they will, you know, practically fracture or damage the well"
  ([[2025-10-22 First call with OES - transcript]] 0:52:09).
- How hard: "it's a big word. It's not overly complicated ... when I started my career, we used to do
  this on the, on a big HP programmable calculator or Excel" (1:10:43); "they're mostly fluid mechanics
  type simulation and specifically on the hydraulic side of things" (0:52:09).
- What the client's samples show (added 2026-09-28, batch 7;
  [[2025-11-20 Client formula and chart samples - rendering]]): five step-by-step procedures - annular
  pressure drop and ECD, critical velocity and pump rate, drillstring pressure drop, swab and surge
  pressures, slip velocity and hole cleaning (images 3 to 7) - and three output screens of a hydraulics
  program: pressures, ECD and bit hydraulics at ten flow rates (image 8), surge pressure against trip
  speed by depth (image 9), and the "Hydraulics Operating Window" next to a drawing of the well
  (image 10). The operating window - pressure and ECD against flow rate, with "Max SPP" and "Required
  Flowrate" - is the "flow it window" the client described on the first call (0:52:09, above). The
  screens' inputs are the ones the client listed in E.25: casing and open hole, drill string, fluid and
  rheology, flow rate, bit, pore and frac pressure. Figure 2-2 compares against a "Figure 3-1" that was
  not sent. The samples are examples, not the required set
  ([[CON-003 Correct calculations]]).
- Which rheological model: the procedures use the power law, the screens Herschel-Bulkley -
  [[QUE-008 Which rheological model the hydraulics must use]].
- What the client's sample program reports compute (added 2026-11-02;
  [[2026-11-02 Client sample engineering reports - rendering]]): pressure losses by component and
  the standpipe pressure, bit hydraulics, annular velocity and flow regime, ECD at the shoe and at
  the bit with and without cuttings, cuttings transport and hole cleaning, sensitivities to flow
  rate and ROP, results at several depths, the operating window again, surge pressure against trip
  speed and the maximum trip speed by depth, and torque and drag. Four of the six are one commercial
  program's outputs for one planned well (the PDF metadata names INTEQ "Advantage" report templates,
  2012): a reference for what engineers are used to, not the scope, against row 60's charts that
  "are not complex" (evaluated). Which of them the simulation covers:
  [[QUE-013 Which calculations from the sample reports the simulation must cover]].
- The daily reports carry hydraulics too: per annular section, annular and critical velocity,
  critical rate, flow regime, ECD, pressure drop, slip velocity, CTR and CCI ([[2026-11-02 Client sample daily mud reports - DMR Sample 2.pdf|DMR Sample 2]]), and n,
  k and ECD at bit and shoe ([[2026-11-02 Client sample daily mud reports - DMR Sample 1.pdf|DMR Sample 1]])
  ([[2026-11-02 Client sample daily mud reports - rendering]]) - derived values in the sense of
  [[REQ-007 Derived values and standard calculations]].

## Out of scope

- "Simulation for predicting equipment maintenance" (notes, Out of scope; Q&A Part 1, 5).
