---
type: requirement
id: REQ-005
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-11-05 Proposal slides - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2026-11-02 Client sample daily mud reports - rendering]]"
  - "[[2026-11-02 Client sample end-of-well recap - rendering]]"
scope_status: contracted
baseline:
  - "WBS:Development Flutter!20"
  - "WBS:Development Flutter!29"
  - "WBS:Development Flutter!52"
  - "WBS:Development Flutter!53"
capabilities:
  - "[[CAP-004 Shift measurements and quality control]]"
tags:
  - thresholds
  - alerts
  - data-quality
---
# REQ-005 Parameter thresholds and entry alerts

## Need

HQ sets the acceptable range of each fluid parameter ([[TRM-007 Threshold]]); when an engineer enters
a value on the desktop, the app helps them avoid wrong entries and flags values outside the range.
Why: the client wants "different types of data control alerts. Examples: 1. Alerts to users to prevent
wrong data entry. 2. Alerts to users to highlight critical parameters that are out of threshold"
([[2025-10-29 Client answers to the Q&A register - rendering]] E.20); the first call listed "Alerting if
the inputted parameter is out if the set thresholds" ([[2025-10-22 First call with OES - notes]] key
point 5).

Scope: contracted. v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter rows 20 (Parameter Threshold Definition, web), 52
(Threshold Violation Alerting, desktop) and 53 (Contextual Input Guidance, desktop), all estimated.
Row 29 (Quality Control, web, estimated) is the HQ side; added 2026-09-28, batch 4.

## Acceptance criteria

To be written by the BA.

## Edge cases

| Scenario | Expected behaviour |
|---|---|
| A threshold changes at HQ while a rig is offline | Not defined in these sources |

## Business rules

- A threshold is a minimum and maximum acceptable value per fluid parameter, defined in the web admin
  ([[2025-10-28 BA draft WBS - rendering]] row 5) and checked on the desktop (row 16).
- Field hints: "Contextual hints for specific fields during data entry, providing rules or acceptable
  ranges to prevent incorrect input" (row 20).
- A value past a threshold: "The system should require to input a mandatory comment or reason before
  allowing the data to be saved with a 'flagged' status" (row 16). Batch 1 recorded this as Innowise's
  design, not the client's. Corrected 2026-09-28 (batch 2): the first call's transcript shows it follows
  the client's own words. Out-of-range values are kept, flagged, counted and justified: "It should be
  able to alert when certain agreed upon parameters that have a specification or range that, that is
  required by the customer. Anytime we go outside of the range ... we should be able to flag that. Okay,
  why we'll still capture it, but at the same time we should be able to plug that and be able to count
  that ... and justify the reason why that is and what we're doing about it"
  ([[2025-10-22 First call with OES - transcript]] 0:35:31). The client also wants the app to "prevent
  the input of wrong data that do not make sense" (0:35:31). The proposal slides showed the mandatory
  comment to the client ([[2025-11-05 Proposal slides - rendering]] slide 13).
- The range comes from the client's customer's specification ("required by the customer", 0:35:31) and
  the job's quality and safety requirements.
- The client did not answer how thresholds are set today: "Kindly explain what you meant by
  'threshold'." (E.19). No written explanation or answer is on file. Whether thresholds are global,
  per mud system or per well is open.
- Innowise asked what the difference between alert types 1 and 2 is (comment on E.20); unanswered.
- Alert type 3, materials below minimum stock, is in [[REQ-009 Inventory tracking]].
- Thresholds, like other settings, are managed by "Authorized IT personnel" (D.16).
- At HQ (added 2026-09-28, batch 4): "Feature focused on Quality Control (QC), allowing to easily see
  and review data streams from their assigned rigs with entries flagged for threshold violations
  highlighted" ([[2026-09-25 v1 WBS - rendering]], Development Flutter row 29).
- What the client's samples show (added 2026-11-02): every report puts a range next to each property
  - "Fluid Spec" (density "73.00-90.00" lb/ft^3, [[2026-11-02 Client sample daily mud reports - DMR Sample 1.pdf|DMR Sample 1]]) and "Spec's" ([[2026-11-02 Client sample daily mud reports - DMR Sample 2.pdf|DMR Sample 2]])
  ([[2026-11-02 Client sample daily mud reports - rendering]]), "Mud Spec's" per hole section
  ([[2026-11-02 Client sample end-of-well recap - rendering]] pp [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=5|5]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=19|19]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=24|24]]) - and the end-of-well
  report plots each property per section against "Plan Low" and "Plan High" (pp [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=12|12]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=17|17]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=22|22]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=27|27]]).
  Evaluated: the threshold the client means may be this per-section mud programme range, which would
  make thresholds per well section; to confirm with the client.

## Out of scope
