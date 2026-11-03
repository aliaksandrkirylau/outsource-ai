---
type: question
id: QUE-011
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
asks: client
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
tags:
  - projects
  - offline
  - sync
---
# QUE-011 Who wins when a project is edited on the web and on an offline desktop

## Question

Projects ([[TRM-005 Project (well job)]]) can be created and updated in both apps: on the web at HQ
and on the desktop at the rig. The desktop works offline and syncs only when a connection appears
([[CON-001 Offline operation and sync between rigs and HQ]]). Which app owns which project data, and
what happens when the same project was changed in both before a sync?

Raised by Mikhail Andrushkevich on 2026-10-14. Our reading of the SOW, not yet discussed with the
client.

Both apps edit projects, per the SOW v10.4 Milestone 3
([[2026-06-15 SOW v10.4 - rendering]], Phase 3):

- Web: "Creating and editing projects, assigning and reassigning engineers, and viewing the project
  list with basic filter and search."
- Desktop: "The engineer can create a new project entry, or select and update an existing one, and
  enter the required details (location, client information, and so on), with the project receiving an
  active status and an ID."

What can go wrong while a rig is offline:

- HQ and the rig change the same field (location, client information) - two versions meet at sync.
- The engineer creates a project offline that HQ has also created - a duplicate of the same well job.
- The desktop gives the project "an active status and an ID" offline - the ID must stay unique across
  all rigs and the web, and survive the sync.
- HQ reassigns engineers, deactivates or (if the WBS "CRUD project" stands) deletes a project while the
  rig keeps recording shifts against it.

Consistency across desktops cannot be total: "здесь нельзя рассчитывать на 100% консистенции среди
всех десктопов ... Но можно это минимализировать как-то" (Arseniy Klimenko,
[[2026-10-01 Optimum Three Caballeros call - transcript]] 00:11:38).

## What it blocks

- WBS:Development Flutter!26, WBS:Development Flutter!27 and WBS:Development Flutter!50 - the project
  data model and what each app may edit
  ([[REQ-020 Create and manage well jobs and assign engineers]], its offline edge case).
- `SOW:M3 Project management (create, edit, assign)` and `SOW:M3 Project management feature`, and the
  Milestone 3 deliverable "Written answers to the questions and assumptions left open in Phase 2 (how
  project assignment works, role-permission edge cases, sync behaviour)" (SOW v10.4).
- The sync design in [[CON-001 Offline operation and sync between rigs and HQ]]: projects are the first
  data that flows both ways, so their conflict rule sets the pattern for later modules.

## Options

Envisioned, ours; none agreed.

1. One owner per field: HQ owns the master data (name, client, location, assignment, status); the rig
   only selects a project and fills the rig-side details. No conflicts by design; the desktop's
   "create a new project entry" would need a narrower reading agreed with the client.
2. Create on the web only; the desktop selects and updates. Removes duplicates and offline IDs, but
   departs from the SOW wording, so it needs the client's agreement.
3. Both edit everything, with a conflict rule: HQ wins, or last write wins (rig clocks cannot be
   trusted, and the losing edit disappears silently), or conflicts are held for a person to resolve on
   the web - the "sync errors and data conflicts log" the BA draft planned
   ([[2025-10-28 BA draft WBS - rendering]] row 7), not in the v1 WBS.

Whatever the choice: a project created offline gets a temporary local ID, or an ID scheme that cannot
collide, and the rule is written into the Milestone 3 specification.

## Answer

Not answered. The team proposes an option (TL), then the client confirms it.
