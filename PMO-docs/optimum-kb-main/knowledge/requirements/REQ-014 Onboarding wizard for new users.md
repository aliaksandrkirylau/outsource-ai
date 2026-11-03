---
type: requirement
id: REQ-014
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-11-03 Solution proposal - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2025-11-05 WBS sent to the client - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
scope_status: out-of-scope
baseline:
  - "WBS:Development Flutter!48"
tags:
  - onboarding
  - out-of-scope
---
# REQ-014 Onboarding wizard for new users

## Need

Recorded so nobody re-asks, and because the client wanted it strongly: an in-app onboarding wizard for
new users is out of scope. Asked "Do you want guided wizards, sets of rules and hints, or checklists
for new engineers and new app users?", the client answered "Yes (very much)!"
([[2025-10-29 Client answers to the Q&A register - rendering]] E.26).

How it left the scope:

- The BA draft had "A step-by-step tutorial or wizard for new users on how to enter daily data"
  ([[2025-10-28 BA draft WBS - rendering]] row 19).
- The WBS sent to the client on 5 November 2025 had it in the MVP, TRUE (added 2026-09-28, batch 4;
  [[2025-11-05 WBS sent to the client - rendering]] Development row 47).
- The v1 WBS ([[2026-09-25 v1 WBS - rendering]]) keeps it as Development Flutter row 48 but outside the estimated total; its Assumptions &
  Risks 20 limits it to "up to 10 hints" in any case.
- The SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]): "User manuals and in-app wizard flow for new users are not
  included in the scope."

In presale (added 2026-09-28, batch 2): the proposal named "a user-friendly, low-latency interface with
guided wizards" among its objectives and put "the sets of rules and hints for new engineers and new app
users" as a "Bonus*" in the desktop phase, while two internal comments on the hints said "я бы сказал,
что это out of scope?" and "Пока да, думаю так, out of scope"
([[2025-11-03 Solution proposal - rendering]]).

What stays in: contextual hints on fields during data entry ([[REQ-005 Parameter thresholds and entry alerts]]).
The client's wish still matters for [[CON-005 Easy and responsive interface]].

## Acceptance criteria

None: out of scope.

## Edge cases

| Scenario | Expected behaviour |
|---|---|

## Business rules

## Out of scope

The whole of this note, and user manuals.
