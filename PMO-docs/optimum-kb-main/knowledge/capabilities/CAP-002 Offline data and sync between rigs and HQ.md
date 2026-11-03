---
type: capability
id: CAP-002
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: enabler
baseline:
  - "WBS:Overview!8"
  - "SOW:M2 Database structure setup"
  - "SOW:M3 Synchronization with backend logic"
  - "SOW:M4 Implemented Features: Desktop Application"
depends_on:
  - "[[CAP-011 Platform, environments and handover]]"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - capability
  - offline
  - sync
---
# CAP-002 Offline data and sync between rigs and HQ

## What it must do

Every rig keeps working with no connection, and its data reaches the central database when a
connection returns, with nothing lost or changed
([[CON-001 Offline operation and sync between rigs and HQ]]). The flow is two-way: thresholds,
low-stock levels and user accounts are set on the web and used on the desktop
([[QUE-002 Do managers send anything back to the rigs]]).

No Development Flutter row of the v1 WBS names sync. Its only mention is the Overview tab's stack
cell: "Local storage for site clients SQLite - to keep data ready for server sync"
([[2026-09-25 v1 WBS - rendering]], Overview row 8). The SOW v10.4 is the baseline: the sync
foundation in the schema (Milestone 2), project and measurement data (Milestone 3), and "sync of
modules not yet built is added in their own phases" (row 11, Milestone 3).

## Coverage criteria

Drafted from the SOW v10.4 wording (row 11); the TL owns these.

- C1 Project and measurement data entered on the desktop with no connection reaches the central
  database when the connection returns (M3, Synchronization with backend logic).
- C2 Edits made offline are captured and reconciled "once the connection is back" (M3). The rule
  for two rigs changing the same record is decided and recorded as a Decision.
- C3 Inventory entries work offline and sync the same way: "All of the above works offline and syncs
  with the server when the connection returns" (M4, desktop).
- C4 What is set on the web and used on the desktop (thresholds, low-stock levels, user accounts) is
  available on the desktop offline.
- C5 "99.9% data integrity", the client's second outcome, has a definition and a way to measure it,
  and is met ([[CON-001 Offline operation and sync between rigs and HQ]]).

## Refined by

- [[CON-001 Offline operation and sync between rigs and HQ]]
- [[CON-004 Scale and data volume]]
- [[REQ-001 Record and calculate a shift without internet]]
- [[REQ-012 Documents uploaded at HQ available at the rig]] (a change request candidate: the SOW's
  sync covers project and measurement data)
- [[QUE-002 Do managers send anything back to the rigs]]
- [[DEC-005 Desktop at the rig, web app at HQ]]

## Plan

Starts M2 (the sync foundation in the schema), main work M3 (project and measurement data), continues
M4 (inventory) and with each module after, hardened by M6 (final stabilisation).
