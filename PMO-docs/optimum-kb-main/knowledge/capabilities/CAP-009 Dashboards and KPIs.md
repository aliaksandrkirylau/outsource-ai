---
type: capability
id: CAP-009
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: business
baseline:
  - "WBS:Development Flutter!31"
  - "WBS:Development Flutter!56"
  - "SOW:M5 Dashboard"
  - "SOW:M6 Dashboard"
depends_on:
  - "[[CAP-002 Offline data and sync between rigs and HQ]]"
  - "[[CAP-004 Shift measurements and quality control]]"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - capability
  - dashboards
---
# CAP-009 Dashboards and KPIs

## What it must do

Two dashboards, a milestone apart: on the web, a one-page snapshot of operational status, key
indicators and progress against targets across job sites (Milestone 5); on the desktop, "a different,
engineer-focused view" (Milestone 6) ([[2026-06-15 SOW v10.4 - rendering]] row 11). Which indicators
is part of the Milestone 5 specifications ("the chart and indicator definitions").

## Coverage criteria

Drafted from the SOW v10.4 wording (row 11); the TL owns these.

- C1 The web dashboard shows operational status, key indicators and progress against targets across
  job sites, with filter and search to narrow to one project (M5).
- C2 The desktop dashboard shows the engineer's status, key indicators and progress (M6).
- C3 Charts are the simple types (bar, pie and similar); complex or custom visualisations, 3D views
  and animations are not included (M5, M6).

## Refined by

- [[REQ-011 Dashboards and KPIs]]
- [[QUE-003 Do calculations and modelling need 3D or complex visuals]]

## Plan

Starts M5 (web), completes M6 (desktop).
