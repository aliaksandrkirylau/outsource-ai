---
type: requirement
id: REQ-003
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
scope_status: contracted
baseline:
  - "WBS:Development Flutter!47"
capabilities:
  - "[[CAP-001 Identity, roles and access]]"
tags:
  - login
  - desktop
---
# REQ-003 Sign in on a shared rig computer

## Need

Each engineer signs in to the desktop app with their own account, so that on a computer shared by
several engineers across shifts the system knows who entered what. Why: "the computers ... are shared
among multiple engineers (1 to 4 people), as the computer is assigned to the rig site, not the
individual" - "Yes" ([[2025-10-29 Client answers to the Q&A register - rendering]] Part 1, 9); the
client "Prefer In-app accounts per user/shift but device level login is also acceptable" (D.11).

The BA draft's wording: "Login screen uitilizing unique credentials to ensure that on the shared
computer individual user activity is recorded for Engineers on different shifts"
([[2025-10-28 BA draft WBS - rendering]] row 12).

Scope: contracted. v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter row 47 (desktop Authorization/Authentication,
estimated); the SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) includes desktop login with offline sign-in in
Milestone 2.

## Acceptance criteria

To be written by the BA.

## Edge cases

| Scenario | Expected behaviour |
|---|---|
| The rig computer has no connection when the engineer signs in | Not defined in these sources; the SOW v10.4 includes offline sign-in |

## Business rules

- The desktop app is for engineers only (v1 WBS, Assumptions & Risks 14).
- Reusing the client's existing identity provider: "Need further clarifications but probably not"
  (D.12).
- What a "user" is, the client's own question on the first call (added 2026-09-28, batch 2): "if I
  have a computer on a particular job site and that job site is operating for one year and I cause that
  one year period, I have 10 engineers at various point in time, maximum two at the same time, they
  will all be using the same computer ... are we going to define each of those 10 engineers as users or
  are we going to define the computer itself that they are all using at various points?"
  ([[2025-10-22 First call with OES - transcript]] 0:59:46). Not answered on the call; the October
  answers (D.11) prefer per-user accounts.
- Device-level (Windows) login alone is "also acceptable" to the client (D.11); Marina Zaretskaya
  noted on the first call that a password for the laptop might be enough
  ([[2025-10-22 First call with OES - notes]], comments).

## Out of scope
