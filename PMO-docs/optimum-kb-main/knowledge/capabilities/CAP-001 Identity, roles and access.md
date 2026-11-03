---
type: capability
id: CAP-001
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: hybrid
baseline:
  - "WBS:Development Flutter!12"
  - "WBS:Development Flutter!17"
  - "WBS:Development Flutter!19"
  - "WBS:Development Flutter!47"
  - "SOW:M2 Authorization/Authentication"
  - "SOW:M2 User creation flow"
  - "SOW:M2 Users list"
  - "SOW:M3 User management (edit, update, deactivate)"
  - "SOW:M3 Role-based access adjustments"
depends_on:
  - "[[CAP-011 Platform, environments and handover]]"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - capability
  - identity
---
# CAP-001 Identity, roles and access

## What it must do

People sign in to the web app and the desktop app against the project's own identity service, each
role sees and does only what it is permitted, and administrators manage the accounts. On the desktop,
sign-in works offline: "cached token and credential validation so an engineer can sign in and keep
working without a connection" ([[2026-06-15 SOW v10.4 - rendering]] row 11, Milestone 2, desktop
Authorization/Authentication).

## Coverage criteria

Drafted from the SOW v10.4 wording (row 11); the TL owns these.

- C1 A user signs in and out of the web app and the desktop app against the project's identity
  service, with session handling (M2).
- C2 An engineer signs in on the desktop with no connection and keeps working (M2).
- C3 An administrator creates a user with one predefined role (M2), then edits it, changes its role,
  deactivates and reactivates it (M3).
- C4 The users list shows user, role and status, paginated, with basic filter and search (M2).
- C5 Each role sees only the screens and actions it is permitted, on the web and the desktop (M2,
  M3). How many roles there are is disputed in [[REQ-004 Roles and what each role can do]].

Not included, per the SOW: MFA, single sign-on, social login, bulk operations, a per-user
permissions editor.

## Refined by

- [[REQ-003 Sign in on a shared rig computer]]
- [[REQ-004 Roles and what each role can do]] (disputed: three roles or four)
- [[DEC-005 Desktop at the rig, web app at HQ]]
- [[CON-007 Saudi cybersecurity and data protection rules]] (which controls apply to accounts and
  sign-in is not yet mapped)

## Plan

M1: the identity solution and offline-login expectations are among the open points Milestone 2
answers in writing. Starts M2 (sign-in, user creation, users list), completes M3 (user management,
role-based access across the new screens).
