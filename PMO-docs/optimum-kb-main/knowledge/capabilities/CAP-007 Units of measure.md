---
type: capability
id: CAP-007
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: enabler
baseline:
  - "WBS:Development Flutter!22"
  - "WBS:Development Flutter!54"
  - "SOW:M3 Metric and unit customizing"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - capability
  - units
---
# CAP-007 Units of measure

## What it must do

Users choose the units their entries are in and convert between units, with validation. The SOW
"assumes three unit sets", and "The same units carry through to the web measurement views"
([[2026-06-15 SOW v10.4 - rendering]] row 11, Milestone 3, Metric and unit customizing). Measurements,
calculations, inventory and reports all depend on it.

## Coverage criteria

Drafted from the SOW v10.4 wording (row 11); the TL owns these.

- C1 A user chooses the measurement units for entries, from three unit sets (M3).
- C2 A value converts from one unit to another, with the related validation rules (M3).
- C3 The same units carry through to the web measurement views (M3).

Open: which three sets is not stated, and the client's samples mix units within one set
([[REQ-018 Units of measure and conversion]]).

## Refined by

- [[REQ-018 Units of measure and conversion]]

## Plan

M3.
