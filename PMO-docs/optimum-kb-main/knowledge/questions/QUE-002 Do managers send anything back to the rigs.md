---
type: question
id: QUE-002
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
asks: client
answered_by: "[[REQ-005 Parameter thresholds and entry alerts]]"
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
tags:
  - sync
---
# QUE-002 Do managers send anything back to the rigs

## Question

Does anyone in the web app (managers, supervisors, admins) send anything back to the shift
engineers on the rigs - instructions, corrections, reference data - or does data only flow from the
rigs to HQ?

## What it blocks

Whether sync is one-way or two-way, in [[CON-001 Offline operation and sync between rigs and HQ]].

## Options

- One-way: rigs to HQ only.
- Two-way: HQ also sends data to the rigs.

## Answer

Raised by Anton: "Интересно, должны ли они обратно что-нибудь еще отправлять этим
сменщикам" ([[2026-09-25 Optimum Eng sync - transcript]] 00:15:00).

Answered 2026-09-28 from sources already on file (origin: evaluated), not by asking the client again:
two-way.

- Thresholds are defined at HQ and checked on the desktop: "UI to define threshold limits
  (minimum/maximum acceptable values) for each of the fluid parameters tracked" in the administration
  module, and the desktop flags values past "a predefined threshold"
  ([[2025-10-28 BA draft WBS - rendering]] rows 5, 16). Recorded in
  [[REQ-005 Parameter thresholds and entry alerts]]. The SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) says the same, and
  that low-stock levels and user accounts are set in the web app too.
- Documents: "Document upload required from HQ but accessible on the job site."
  ([[2025-10-29 Client answers to the Q&A register - rendering]] E.23;
  [[REQ-012 Documents uploaded at HQ available at the rig]]).

Whether managers send instructions or corrections back to the rigs, the other half of the question,
is still not answered.
