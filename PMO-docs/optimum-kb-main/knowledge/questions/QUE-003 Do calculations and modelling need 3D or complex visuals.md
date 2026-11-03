---
type: question
id: QUE-003
status: proposed
origin: evaluated
author: claude-code/claude-opus-5-5
asks: client
answered_by:
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-11-03 Solution proposal - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
  - "[[2025-11-20 Client formula and chart samples - rendering]]"
tags:
  - calculations
  - simulation
  - visualisation
---
# QUE-003 Do calculations and modelling need 3D or complex visuals

## Question

Do the calculation and modelling features need 3D models or complex visualisations, or are simple
charts (bar, pie, x-y curves) enough?

## What it blocks

v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter rows 60 (Simulation: Fluid Hydraulics) and 59 (Standard Engineering
Calculator): both are estimated on simple charts. The v1 WBS assumptions: "The vizualization
capabilities for reports/dashboards are estimated for simple chart types (e.g., pie chart, bar chart)"
(11), "3D visualisations, comlpex charts designing, animations are not in the scope" (13), "Complex
modelling is not required" (17). Notes: [[REQ-008 Fluid hydraulics simulation]],
[[REQ-011 Dashboards and KPIs]].

## Options

- Simple charts only, as estimated.
- Some complex or 3D views (for example a well profile): a change request.

## Answer

None usable yet. We asked the client to confirm the simple reading: "Is it confirmed that
Modeling/Calculation features do not require 3D models or complicated visualizations?" The answer was
"No" ([[2025-10-29 Client answers to the Q&A register - rendering]] Part 1, 4). It reads both ways: "no,
not confirmed - they are required" or "no, they are not required". It is the only "No" in Part 1. The SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) excludes "Complex modeling, custom or
3D visualizations, and animations", which the client may or may not have read as settling it.

More evidence (added 2026-09-28, batch 2), pointing both ways:

- The client on the first call, about the simulation: "It's not overly complicated ... we used to do
  this on the, on a big HP programmable calculator or Excel" ([[2025-10-22 First call with OES - transcript]]
  1:10:43) - but the traditional tools give "all the hot foods, you know, and graphics" and the client
  wants more than that (0:47:56).
- Dashboards: "I think it's still too early to define the nature of the dashboard" (0:39:42).
- Presale read the "No" as a warning: "The client's response to confirming simple models indicates a
  potential desire for complex visualizations. This scope must be strictly defined during the Discovery
  phase to avoid significant scope creep." ([[2025-11-03 Solution proposal - rendering]], Challenges)

How the team read the client's chart samples of 20 November 2025 (added 2026-09-28, batch 5), again
both ways: "тут не совсем стандартные графики, на такие нет библиотек у MAUI, придется рисовать самим"
(Vitaly Ponteley, [[2025-10-20 Presale chat - rendering 2]] 2025-11-20 14:41) and "Графики несложные,
наверно только конструкция скважин" (the consultant, 2025-11-24 12:37). The samples are stored as
[[2025-11-20 Client formula and chart samples - overview]]. Our reading of samples does not answer what
the client needs.

What the chart samples are (added 2026-09-28, batch 7;
[[2025-11-20 Client formula and chart samples - rendering]] images 9, 10): 2D x-y charts from the
client's current hydraulics program - the operating window, with two vertical axes (pressure, ECD) and
five series against flow rate, and surge pressure by depth against trip speed, with filled safe and
unsafe areas and a reversed axis - and a drawing of the well (casing, liner, open hole, drill string)
with its inclination, the consultant's "конструкция скважин". Nothing 3D or animated. They show what the
client uses today, not what it needs from the app.

Still open.
