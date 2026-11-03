---
type: capability
id: CAP-010
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: hybrid
baseline:
  - "WBS:Development Flutter!21"
  - "SOW:M6 Audit logs"
depends_on:
  - "[[CAP-001 Identity, roles and access]]"
  - "[[CAP-004 Shift measurements and quality control]]"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - capability
  - audit
---
# CAP-010 Audit trail and change approval

## What it must do

Data entry, edit and backfill actions are tracked - when, by whom, what changed - with their
approval status, viewable on the web. "Bounded to the agreed volume of logged actions; anything
beyond that is a Change Request" ([[2026-06-15 SOW v10.4 - rendering]] row 11, Milestone 6, Audit
logs). The WBS line says "Up to 30 logged actions" ([[2026-09-25 v1 WBS - rendering]], Development
Flutter row 21); whether that means 30 kinds of action or something else is not stated.

## Coverage criteria

Drafted from the SOW v10.4 wording (row 11); the TL owns these.

- C1 Data entry, edit and backfill actions are recorded with when, by whom and what changed (M6).
- C2 Each recorded action carries its approval status, and the log is viewable on the web (M6).
- C3 The logged volume stays within the agreed bound (M6; the bound itself to be defined).

## Refined by

- [[REQ-006 Edit or backfill past entries with approval]]

## Plan

M6. Entries start in M3 ([[CAP-004 Shift measurements and quality control]]) and the audit log and
approval come in M6; how edits and backfills between M3 and M6 are handled is not stated in the SOW.
