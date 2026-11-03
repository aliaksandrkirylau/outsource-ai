---
type: capability
id: CAP-006
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: business
baseline:
  - "WBS:Development Flutter!39-41"
  - "WBS:Development Flutter!62-66"
  - "SOW:M4 Inventory management (add, update, track)"
  - "SOW:M4 Basic validation rules for inventory operations"
  - "SOW:M4 Daily consumption log"
  - "SOW:M4 Stock movements log"
  - "SOW:M4 Product concentration tracking"
  - "SOW:M4 Low stock alerting"
  - "SOW:M4 Expiration date alerting"
depends_on:
  - "[[CAP-002 Offline data and sync between rigs and HQ]]"
  - "[[CAP-003 Well jobs and engineer assignment]]"
  - "[[CAP-007 Units of measure]]"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - capability
  - inventory
---
# CAP-006 Inventory

## What it must do

HQ keeps the list of chemicals and materials used on the rig and their stock events; the engineer
logs consumption, stock movements and concentrations on the desktop and is warned about low stock and
expiring material. Low-stock levels are set on the web
([[2026-06-15 SOW v10.4 - rendering]] row 11, Milestone 4).

## Coverage criteria

Drafted from the SOW v10.4 wording (row 11); the TL owns these.

- C1 On the web, inventory items (the chemicals and materials used on the rig) are added, updated and
  tracked with brand name, material number, unit size and unit of measure, with the key events:
  initial loadout, received, returned, lost (M4).
- C2 Inventory entries get field-level checks: required fields, valid numbers and units, sensible
  ranges (M4).
- C3 On the desktop, the engineer logs daily consumption, stock movements, and the ending
  concentration of specific mud components (M4).
- C4 On the desktop, a material below its low-stock level, or approaching or past its expiration
  date, is highlighted (M4).
- C5 All of it works offline and syncs ([[CAP-002 Offline data and sync between rigs and HQ]] C3).

## Refined by

- [[REQ-009 Inventory tracking]]
- [[REQ-016 Inventory of lab equipment and reagents]] (a change request candidate: the inventory
  lines cover "products (chemicals, materials)", Development Flutter row 39)

## Plan

M4.
