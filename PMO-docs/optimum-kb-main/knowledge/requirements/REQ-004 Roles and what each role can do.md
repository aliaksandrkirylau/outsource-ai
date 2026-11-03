---
type: requirement
id: REQ-004
status: disputed
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-11-25 Project description - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-10-24 Presale architecture - rendering]]"
  - "[[2025-11-03 Solution proposal - rendering]]"
  - "[[2025-11-05 Proposal slides - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
scope_status: contracted
acceptance_measure: For every agreed role and every screen and action, the role can use exactly what the agreed role matrix grants it, and nothing else
baseline:
  - "WBS:Development Flutter!12"
  - "WBS:Development Flutter!19"
capabilities:
  - "[[CAP-001 Identity, roles and access]]"
tags:
  - roles
  - access
---
# REQ-004 Roles and what each role can do

## Need

Each person sees and does only what their role allows. Who the roles are is disputed: the sources
disagree on three or four roles. Both versions are kept until the BA settles it with the client;
the role model is a Milestone 1 clarification in the SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]).

### Version A - four roles

- The client's own scenarios ([[2025-10-29 Client answers to the Q&A register - rendering]] D.13):
  "Mud Engineer: Enter measurements, perform calculations and simulations, generate reports and email
  reports to the supervisors", "Supervisor: Review and generate reports", "Manager: Access dashboards,
  oversee multiple sites", "Admin: Manage users, roles, and system settings".
- First call: "around 3-4 user group types: sites engineer, admin, supervisor, manager"
  ([[2025-10-22 First call with OES - notes]] key point 5).
- Presale description: "designed for Mud Engineers, Supervisors, Managers, and Administrators"
  ([[2025-11-25 Project description - rendering]]).
- The SOW v10.4 assumptions: "four primary user roles: Engineers, Managers, Supervisors, and
  Administrators".

### Version B - three roles, Supervisor and Manager as one

- BA draft: "one of the three required roles (Admin, Engineer, Supervisor/Manager)"
  ([[2025-10-28 BA draft WBS - rendering]] row 3).
- v1 WBS ([[2026-09-25 v1 WBS - rendering]]), Development Flutter row 19: the same wording.
- The SOW v10.4, Milestone 2: "a predefined role (Administrator, Engineer, Supervisor/Manager)".

### Also on file (added 2026-09-28, batch 2; the dispute stands)

- The client on the first call names three groups, with no admin: "the primary users will have the
  same rights because they're all, they're all job sites engineers ... but there will be some level of
  user on supervisory levels who are the projects supervisors ... may has 10, 15 grilling rig under his
  domain ... QC the data that is in the system, you know, and do some other higher level things in the
  system. And of course the management is there." ([[2025-10-22 First call with OES - transcript]]
  0:25:39)
- The presale architecture: "at least three user groups: Job Site Engineers ..., Project Supervisors
  ..., and Management" ([[2025-10-24 Presale architecture - rendering]]).
- The presale proposal and the client-facing slides: four, Mud Engineer, Supervisor, Manager, Admin
  ([[2025-11-03 Solution proposal - rendering]]; [[2025-11-05 Proposal slides - rendering]] slide 14).

Scope: contracted. v1 WBS Development Flutter row 12 (Role model, estimated) and row 19.

## Acceptance criteria

To be written by the BA once the role set is settled.

## Edge cases

| Scenario | Expected behaviour |
|---|---|

## Business rules

- The client also names roles neither version maps: "Access to Report and System: Field Supervisors,
  Project Engineers, Operations Support, and Operations Manager" (C.10).
- Users and roles are administered by "Authorized IT personnel" (D.16), the same who manage
  thresholds and templates. The client also says it has no staff to run on-premises services (C.6);
  who exactly administers is not stated.
- Other internal workflows (sending a report for review): "Not at the moment" (D.15).
- The desktop is for engineers only; mobile was for managers and engineers; the web for admins,
  managers and supervisors (v1 WBS, Assumptions & Risks 14).

## Out of scope
