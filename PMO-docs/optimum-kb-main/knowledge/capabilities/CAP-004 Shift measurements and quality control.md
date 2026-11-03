---
type: capability
id: CAP-004
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: business
baseline:
  - "WBS:Development Flutter!20"
  - "WBS:Development Flutter!28"
  - "WBS:Development Flutter!29"
  - "WBS:Development Flutter!51"
  - "WBS:Development Flutter!52"
  - "WBS:Development Flutter!53"
  - "SOW:M3 Basic project viewing and interaction"
  - "SOW:M3 Contextual input guidance"
  - "SOW:M3 Measurement viewing and quality control"
  - "SOW:M4 Admin panel, parameter threshold definition and configuration"
  - "SOW:M4 Threshold violation alerting"
depends_on:
  - "[[CAP-002 Offline data and sync between rigs and HQ]]"
  - "[[CAP-003 Well jobs and engineer assignment]]"
  - "[[CAP-007 Units of measure]]"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - capability
  - measurements
  - thresholds
---
# CAP-004 Shift measurements and quality control

## What it must do

The engineer enters the raw measurements of a [[TRM-008 Mud check]] for the current
[[TRM-002 Shift]] and project, with guidance and validation. A value past a
[[TRM-007 Threshold]] set at HQ is flagged, and "Before the data can be saved with a flagged status,
the system requires the engineer to enter a mandatory comment or reason"
([[2026-06-15 SOW v10.4 - rendering]] row 11, Milestone 4, Threshold violation alerting). HQ reviews
the entries and the flagged values.

## Coverage criteria

Drafted from the SOW v10.4 wording (row 11); the TL owns these.

- C1 An engineer manually enters the raw measurement entries linked to the current shift and project,
  with basic input validation (M3, desktop).
- C2 Fields show hints with the acceptable rules or ranges during entry (M3, Contextual input
  guidance).
- C3 An administrator defines the minimum and maximum acceptable values for each tracked fluid
  parameter in the web admin panel (M4).
- C4 A value past a threshold is highlighted and can be saved flagged only with a mandatory comment
  or reason (M4, desktop).
- C5 HQ views the raw entries, and a quality-control view highlights the flagged ones (M3, web; the
  highlighting once thresholds exist in M4).

## Refined by

- [[REQ-001 Record and calculate a shift without internet]]
- [[REQ-005 Parameter thresholds and entry alerts]]
- [[REQ-006 Edit or backfill past entries with approval]] (the approval side is
  [[CAP-010 Audit trail and change approval]])
- [[TRM-002 Shift]], [[TRM-003 Mud engineer]], [[TRM-007 Threshold]], [[TRM-008 Mud check]]

## Plan

Starts M3 (entry, guidance, web viewing), completes M4 (thresholds and alerts).
