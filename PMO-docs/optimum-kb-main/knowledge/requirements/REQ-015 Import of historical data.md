---
type: requirement
id: REQ-015
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-11-03 Solution proposal - rendering]]"
  - "[[2025-12-30 Answers to the client's questions - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
scope_status: out-of-scope
baseline:
tags:
  - data-migration
  - out-of-scope
---
# REQ-015 Import of historical data

## Need

Recorded so nobody re-asks: importing the client's existing data is out of scope, although the client
expects to bring data in. Asked how big a historical Excel import would be, the client answered:
"Import data will not be Excel. Actual data format and size estimate to be confirmed later."
([[2025-10-29 Client answers to the Q&A register - rendering]] C.9)

How it left the scope:

- The BA draft had a "Historical Data Import Utility", marked Optional
  ([[2025-10-28 BA draft WBS - rendering]] row 10).
- The v1 WBS ([[2026-09-25 v1 WBS - rendering]]): "Existing data migration is out of scope" (Assumptions & Risks 23).
- The SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]): "Current data migration is out of scope."

In presale (added 2026-09-28, batch 2): the proposal: "Migration of historical data (format to be
defined) is not part of the MVP and will be scoped separately"
([[2025-11-03 Solution proposal - rendering]], Assumptions). Yet the internal draft answer on AWS
credits, in December 2025, defined go-live as including it: "By 'go-live,' we mean the application is
fully ready, all data is migrated, and it is ready for employee usage"
([[2025-12-30 Answers to the client's questions - rendering]], comment on AWS credits). Whether that
wording reached the client is not in the doc; if it did, it assumes a migration the scope leaves out.

It matters beyond the import itself: the client's first KPI compares mud parameters "to offset wells"
([[REQ-011 Dashboards and KPIs]]), which needs past wells' data in the system.

## Acceptance criteria

None: out of scope.

## Edge cases

| Scenario | Expected behaviour |
|---|---|

## Business rules

## Out of scope

The whole of this note.
