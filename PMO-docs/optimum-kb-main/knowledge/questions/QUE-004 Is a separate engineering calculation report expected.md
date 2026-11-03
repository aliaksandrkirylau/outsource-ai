---
type: question
id: QUE-004
status: proposed
origin: extracted
author: claude-code/claude-opus-5-5
asks: client
answered_by: "[[REQ-017 Report on a single calculation or simulation]]"
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-11-03 Solution proposal - rendering]]"
  - "[[2025-11-05 Proposal slides - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - reports
---
# QUE-004 Is a separate engineering calculation report expected

## Question

Besides the End-of-Day, End-of-Section, End-of-Well and inventory reports, does the client expect a
separate engineering calculation or simulation report?

## What it blocks

v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter rows 67 to 71 (desktop reporting) and 34 to 37 (web reporting), which
estimate four report types. Note: [[REQ-010 Reports]].

## Options

- Four types; calculation and simulation results appear in the End-of-Well report, which summarises
  "all data, inventory, and simulation results" ([[2025-10-28 BA draft WBS - rendering]] row 40).
- A fifth report for calculations and simulations: a change request.

## Answer

Yes, in the client's own words (answered 2026-09-28, batch 2, from the first call's transcript; the
client was not asked again): "there may be situation whereby we just. The engineer just want to be able
to do an engineering calculation or simulation and generate report just for that, for example."
([[2025-10-22 First call with OES - transcript]] 0:37:48). Recorded in
[[REQ-017 Report on a single calculation or simulation]] as a change request candidate.

The trail: the client confirmed "End-of-Day, End-of-Well, Engineering calculation/simulation, and
Inventory reports" as the MVP reports, "including end-of-section reports"
([[2025-10-29 Client answers to the Q&A register - rendering]] Part 1, 3); the first call's notes listed
"engineering calculation or simulation reports" ([[2025-10-22 First call with OES - notes]] key point 5);
the presale proposal kept "Engineering Calculation reports" among its objectives
([[2025-11-03 Solution proposal - rendering]]); the client-facing slides already listed only four types
([[2025-11-05 Proposal slides - rendering]] slides 12, 13); the BA draft and the v1 WBS have four. No
source records why it was dropped.
