---
type: requirement
id: REQ-020
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
scope_status: contracted
baseline:
  - "WBS:Development Flutter!26"
  - "WBS:Development Flutter!27"
  - "WBS:Development Flutter!50"
capabilities:
  - "[[CAP-003 Well jobs and engineer assignment]]"
tags:
  - projects
  - web
  - desktop
---
# REQ-020 Create and manage well jobs and assign engineers

## Need

HQ sets up each well job ([[TRM-005 Project (well job)]]) and decides which engineers work on it; the
engineer at the rig opens or updates the job the shift's readings belong to. Why: measurements,
inventory and reports belong to a project, and supervisors review "their assigned rigs"
([[REQ-005 Parameter thresholds and entry alerts]]).

The lines: on the web, "Manage projects" - "CRUD project, assign/reassign engineers" - and "Project
details" - "View list of projects, filter projects"; on the desktop, "Project Setup & Management" -
"Ability to create a new (or select and update an existing) well/project entry and input the required
details (location, client info, etc.) with project assigned active status and ID as a result."
([[2026-09-25 v1 WBS - rendering]], Development Flutter rows 26, 27 and 50)

Scope: contracted. v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter rows 26, 27 and 50,
all in the estimate. The SOW v10.4: "Project Management: Full project lifecycle management, including
project setup and editing, assigning/reassigning engineers, viewing project lists and details", built
in Milestone 3 ([[2026-06-15 SOW v10.4 - rendering]]).

## Acceptance criteria

To be written by the BA.

## Edge cases

| Scenario | Expected behaviour |
|---|---|
| The engineer creates or updates a project on the desktop while the rig is offline | Not defined in these sources; the SOW v10.4 tests "desktop project management and synchronization" in Milestone 3, "offline-to-online sync scenarios" included. Open: [[QUE-011 Who wins when a project is edited on the web and on an offline desktop]] |

## Business rules

- Web, from the SOW v10.4 Milestone 3: "Creating and editing projects, assigning and reassigning
  engineers, and viewing the project list with basic filter and search."
- Desktop, from the same: "The engineer can create a new project entry, or select and update an
  existing one, and enter the required details (location, client information, and so on), with the
  project receiving an active status and an ID. Assigning engineers is done on the web, not desktop".
- How assignment works is left open: Milestone 3 delivers "Written answers to the questions and
  assumptions left open in Phase 2 (how project assignment works, role-permission edge cases, sync
  behaviour)" (SOW v10.4).
- The first call listed more: "Projects module: create a project (add id, basic details, location,
  info on client, order details, quality requirements, etc), edit, remove, assign responsible"
  ([[2025-10-22 First call with OES - notes]] key point 5). The WBS says "CRUD project", with delete;
  the SOW says create, edit and assign, and does not mention deleting.
- Who may create and assign projects is part of [[REQ-004 Roles and what each role can do]].
- Whether engineers are assigned to wells, as the WBS and SOW word it, or to rigs, as the client
  describes the work: [[QUE-012 Are engineers assigned to rigs or to wells]].

## Out of scope

- Project templates: "Project templates and bulk assignment are not included" (SOW v10.4 Milestone 3);
  "Project Template Management (Optional)" is outside the v1 estimate (Development Flutter row 24).
- Bulk assignment (SOW v10.4).
- Managing the list of rig sites, "Location Management (Optional)", is outside the v1 estimate
  (Development Flutter row 23); the SOW v10.4 does not mention it.
