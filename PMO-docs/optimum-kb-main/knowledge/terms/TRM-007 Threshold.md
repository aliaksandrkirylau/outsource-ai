---
type: term
id: TRM-007
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
aliases:
  - limit
  - threshold limit
sources:
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2026-11-02 Client sample daily mud reports - rendering]]"
  - "[[2026-11-02 Client sample end-of-well recap - rendering]]"
tags:
  - thresholds
---
# TRM-007 Threshold

## Definition

Our word, not yet the client's: the minimum and maximum acceptable value of a tracked fluid
parameter. "UI to define threshold limits (minimum/maximum acceptable values) for each of the fluid
parameters tracked" ([[2025-10-28 BA draft WBS - rendering]] row 5). A value outside it is flagged on
entry ([[REQ-005 Parameter thresholds and entry alerts]]).

## Context and units

- Set at HQ in the web admin, checked on the desktop (BA draft rows 5 and 16).
- Per parameter, in that parameter's unit. Whether a threshold is global, per mud system or per well is
  open.
- The client's samples carry a "Spec's" range per property and, per hole section, "Plan Low" and
  "Plan High" ([[2026-11-02 Client sample daily mud reports - rendering]],
  [[2026-11-02 Client sample end-of-well recap - rendering]]); whether that is the threshold:
  [[REQ-005 Parameter thresholds and entry alerts]] (added 2026-11-02).
- The client asked us to explain the word: "Kindly explain what you meant by 'threshold'."
  ([[2025-10-29 Client answers to the Q&A register - rendering]] E.19). Their answer on alerts speaks of
  "critical parameters that are out of threshold" (E.20), so the idea is familiar; the client's own
  term is not known.

## Not to be confused with

- The minimum stock level of a material (E.20, type 3), which is an inventory setting
  ([[REQ-009 Inventory tracking]]).
