---
type: decision
id: DEC-003
status: proposed
origin: evaluated
author: claude-code/claude-opus-5-5
kind: scope
deciders:
  - human:alexey.gamanovich
  - human:anton.snotau
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 2]]"
tags:
  - change-requests
  - scope
---
# DEC-003 Handling small change requests

## Context

The contract narrows the room (added 2026-09-28, batch 3): "completion of omitted functions already
implicit in the SOW, or measures necessary to achieve the agreed purpose shall not constitute Change
Requests" ([[2026-09-07 Final contract - rendering]] 4.4); no change request counts until the client
signs it (4.3); and Innowise warrants it had the information to scope and price the project (2.3-2.5).
See [[COM-005 Change requests]] and [[COM-006 Information sufficient for scope and price]].

Where the rule comes from (added 2026-09-28, batch 6): the call of 22 May 2026 that moved to fixed
price agreed "Все, что не в WBS — оформлять как Change Request", with the WBS as the requirements
description for the contract (Yauheni Krasner's summary,
[[2025-11-25 Contract chat - rendering 2]] 2026-05-22 13:07;
[[DEC-008 Fixed price with milestones, on the client's contract]]). The final contract, signed later,
is the narrower text above.

Fixed price; anything outside the WBS is a change request. The client obtained a large discount, so
the economics are tight ([[2026-09-25 Optimum Eng sync - transcript]] 00:26:11). At the same time
[[DEC-001 Delivery quality over margin]] puts delivery quality first.

## Options considered

1. Absorb small changes within reason and close our eyes to the economy for them (Mikhail,
   00:27:02).
2. Absorb only trivial changes ("ради каких-то там лейблок или часа работы можно и не лезть",
   00:26:11); anything from about a day of work becomes a change request, telling the client openly
   that the discount leaves no room (Mikhail, 00:26:11, 00:27:02).

## Decision

Open. Mikhail: "Ну, будем еще по ситуации смотреть" (00:26:11). Alexey: the client strategy is to be
worked out with Snotov (00:27:33; the transcript reads "со снопами", most likely a recognition slip
for Snotov).

## Rationale

To be written when decided.

## Consequences

To be written when decided. Either way the threshold has to be known to the team, or each developer
decides it alone.
