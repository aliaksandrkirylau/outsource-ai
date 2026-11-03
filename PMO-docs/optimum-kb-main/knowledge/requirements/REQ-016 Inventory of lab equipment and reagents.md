---
type: requirement
id: REQ-016
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-10-24 Presale architecture - rendering]]"
  - "[[2025-11-03 Solution proposal - rendering]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
scope_status: proposed-change
baseline:
  - "WBS:Development Flutter!39"
capabilities:
  - "[[CAP-006 Inventory]]"
tags:
  - inventory
  - lab
  - change-request-candidate
---
# REQ-016 Inventory of lab equipment and reagents

## Need

Besides chemicals and materials, the engineer keeps track of the lab tools, reagents and equipment on
the rig, and can report what they had at the start, have now and have used. The client: "The inventory
of their own tools and reagents and equipment that they use in the lab for the testing"
([[2025-10-22 First call with OES - transcript]] 0:12:27); "if the manager in office is asking the
engineers, send me the list of lab equipments or tools that you have and the consumables that you have
on the, on the rig side. Okay, I want to know what you got at the end of, at the beginning of the job
against what you presently have and what you have used. It should be able, with a click of a button,
generate that." (0:37:48)

Presale carried it: "inventory of drilling fluid, long list of chemicals/materials, and lab
tools/equipment on the rig site" ([[2025-10-24 Presale architecture - rendering]]); reports "(e.g.,
inventory, lab tools)" ([[2025-11-03 Solution proposal - rendering]]).

Scope: a change request candidate. The v1 WBS ([[2026-09-25 v1 WBS - rendering]]) inventory lines are for "products (chemicals,
materials)" (Development Flutter row 39, nearest line) and the SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) for "the
chemicals and materials used on the rig". Neither names lab equipment or reagents.

## Acceptance criteria

Not written: first settle whether it is in scope.

## Edge cases

| Scenario | Expected behaviour |
|---|---|

## Business rules

- Calibration: the client's KPIs include "alerts on upcoming expirations of products, reagents,
  stock- outs, or equipment calibration" ([[2025-10-29 Client answers to the Q&A register - rendering]]
  F.27), which touches the same equipment.

## Out of scope
