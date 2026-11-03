---
type: requirement
id: REQ-006
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
scope_status: contracted
baseline:
  - "WBS:Development Flutter!21"
capabilities:
  - "[[CAP-004 Shift measurements and quality control]]"
  - "[[CAP-010 Audit trail and change approval]]"
tags:
  - audit
  - data-quality
---
# REQ-006 Edit or backfill past entries with approval

## Need

Engineers can correct or add past entries, but only with approval, and every change is traceable. The
client: "Backfill or edit feature required but subject to approval by operations manager and/or system
admin" ([[2025-10-29 Client answers to the Q&A register - rendering]] E.22).

Scope: contracted. v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter row 21 (Audit Logging & Modification Approval, web,
estimated); the SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) has audit logs in Milestone 6.

## Acceptance criteria

To be written by the BA.

## Edge cases

| Scenario | Expected behaviour |
|---|---|
| The engineer edits an entry offline and approval happens at HQ | Not defined in these sources |

## Business rules

- Every edit or backfill is logged: "when, by whom and what was changed) and their approval status"
  ([[2025-10-28 BA draft WBS - rendering]] row 6).
- Who approves is open: "operations manager and/or system admin" (E.22); Innowise's comment: "Need to
  determine exact role of the approver." Neither "operations manager" nor "system admin" is in the
  role set yet ([[REQ-004 Roles and what each role can do]]).

## Out of scope
