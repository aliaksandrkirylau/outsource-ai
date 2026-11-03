---
type: requirement
id: REQ-019
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-12-30 Answers to the client's questions - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 1]]"
scope_status: out-of-scope
baseline:
tags:
  - api
  - integration
  - out-of-scope
---
# REQ-019 API for other systems

## Need

Recorded so nobody re-asks: an API for other systems and integrations with external systems are out
of scope.

- The client: out of scope for the MVP "Yes. Unsure about API design."
  ([[2025-10-29 Client answers to the Q&A register - rendering]] Part 1, 5).
- On the first call: "in terms of integration into some other systems, I don't think this is required"
  - the integration wanted is internal, all rigs' data stored centrally
  ([[2025-10-22 First call with OES - transcript]] 0:27:12, 0:28:04). Marina Zaretskaya suggested an API
  as "a good tool for data exchange if you need to provide it to third parties" (0:32:10).
- The client asked for it in December 2025, commenting on the draft SOW: "Page 2 also notes that API
  development is out of scope. We would like the API to be included. Kindly confirm feasibility."
  ([[2025-11-25 Contract chat - rendering 1]] 2025-12-23 08:36; added 2026-09-28, batch 6)
- Our answer in December 2025: "If API development is required, we can address it during the discovery
  stage and provide a separate scope estimation based on the specific requirements."
  ([[2025-12-30 Answers to the client's questions - rendering]], Page 2)
- The v1 WBS ([[2026-09-25 v1 WBS - rendering]]): "API design is out of scope" (Assumptions & Risks 15), external integrations out "apart
  from identity management provider" (16). The SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]): "API design and
  integrations with external systems are out of scope."

If the client asks for it, it is a change request.

## Acceptance criteria

None: out of scope.

## Edge cases

| Scenario | Expected behaviour |
|---|---|

## Business rules

## Out of scope

The whole of this note. Sensors and third-party integrations are out as well (Q&A Part 1, 5).
