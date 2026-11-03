---
type: requirement
id: REQ-012
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
scope_status: proposed-change
baseline:
  - "WBS:Development Flutter!27"
capabilities:
  - "[[CAP-002 Offline data and sync between rigs and HQ]]"
tags:
  - documents
  - sync
  - change-request-candidate
---
# REQ-012 Documents uploaded at HQ available at the rig

## Need

HQ uploads documents, and engineers can open them at the rig. Asked whether files must be attached to
measurements, the client answered: "Document upload required from HQ but accessible on the job site."
([[2025-10-29 Client answers to the Q&A register - rendering]] E.23)

Scope: a change request candidate. No line in the v1 WBS ([[2026-09-25 v1 WBS - rendering]]) or in the BA draft covers uploading or
distributing documents; the nearest is Development Flutter row 27 (Project details, web). The SOW
v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) does not mention it either.

## Acceptance criteria

Not written: first settle whether it is in scope.

## Edge cases

| Scenario | Expected behaviour |
|---|---|
| The rig is offline when HQ uploads a document | Not defined; the document would have to reach the rig by sync ([[CON-001 Offline operation and sync between rigs and HQ]]) |

## Business rules

- Which features need uploads is open. Innowise's comment on the answer: "Need a list of the features
  requiring file upload."
- What kind of documents (the question mentioned lab sheets and calibration certificates) is not
  stated in the answer.

## Out of scope
