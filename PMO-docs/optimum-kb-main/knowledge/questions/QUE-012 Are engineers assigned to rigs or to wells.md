---
type: question
id: QUE-012
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
asks: client
sources:
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-10-24 Presale architecture - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
tags:
  - projects
  - roles
  - rigs
---
# QUE-012 Are engineers assigned to rigs or to wells

## Question

Does HQ assign engineers (and supervisors) to a [[TRM-004 Rig]] for a period, or to each
[[TRM-005 Project (well job)]]? And does that assignment decide who may sign in and work on a rig's
computer?

Raised by Mikhail Andrushkevich on 2026-10-14. Our reading of the sources, not yet discussed with the
client.

The client describes people being sent to a rig, not to a well. On the first call: "I have drilling rig
A. I have say two engineers on that job ... I send a computer also to the job site and I send these two
engineers to that job site"; the computer "may do well number one this month until well number two and
three the following month"; "I may have the same two engineers on that job site for the entire period
... maybe one of them maybe reassigned to another job somewhere else ... The two new people are still
going to be using the same computer" ([[2025-10-22 First call with OES - transcript]] 1:06:48). Over a
year one rig computer may see "10 engineers at various point in time, maximum two at the same time"
(0:59:46). Supervisors are "responsible for multiple rigs"
([[2025-10-24 Presale architecture - rendering]]), and the WBS QC line reviews "data streams from their
assigned rigs" (WBS:Development Flutter!29).

The baseline assigns engineers to projects: "CRUD project, assign/reassign engineers"
(WBS:Development Flutter!26, [[2026-09-25 v1 WBS - rendering]]); "assigning/reassigning engineers" and
"Assigning engineers is done on the web, not desktop" (`SOW:M3 Project management (create, edit,
assign)`, `SOW:M3 Project management feature`, [[2026-06-15 SOW v10.4 - rendering]]).

## What it blocks

- WBS:Development Flutter!26 and WBS:Development Flutter!50 - what assignment links to, and whether the
  desktop needs any assignment at all.
- WBS:Development Flutter!19 and WBS:Development Flutter!29 - the user form ("assigned rigs" or
  projects) and which rigs a supervisor sees in QC.
- WBS:Development Flutter!23 "Location Management (Optional)", outside the v1 estimate: assigning people
  to rigs needs rigs as records in the system, at least a plain list of rig names, so the line may come
  back into scope in a minimal form.
- The Milestone 3 deliverable "Written answers to the questions and assumptions left open in Phase 2 (how
  project assignment works, role-permission edge cases, sync behaviour)" (SOW v10.4).

## Options

Envisioned, ours; none agreed.

1. Assign to rigs. HQ assigns engineers and supervisors to a rig on the web; everyone assigned to a rig
   can work on all of its wells, on its computer; a well belongs to one rig. Who worked on a well comes
   from the entries themselves (each check and report records who signed in). Matches the client's
   description; needs a minimal rig list (row 23) and a narrower reading of "assign engineers" agreed
   with the client.
2. Assign to wells, as the WBS and SOW word it. HQ assigns engineers per well; a well created at the rig
   has no engineers until HQ assigns them, unless its creator is added automatically. Reassignment is
   needed at every new well even when the crew has not changed.
3. Both: rig assignment decides access on the rig computer; well assignment records responsibility for
   reports. Most flexible, most to build and explain.

## Answer

Not answered. The team proposes an option, then the client confirms it. Related:
[[QUE-011 Who wins when a project is edited on the web and on an offline desktop]].
