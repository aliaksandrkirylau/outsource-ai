---
type: term
id: TRM-001
status: disputed
origin: extracted
author: claude-code/claude-opus-5-5
aliases:
  - отчет
  - daily mud report
  - DMR
  - EOWR
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-29 Client sample daily report - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2026-11-02 Client sample daily mud reports - rendering]]"
  - "[[2026-11-02 Client sample end-of-well recap - rendering]]"
tags:
  - domain
---
# TRM-001 Report

## Definition

Disputed since 2026-09-28 (batch 2): two sources define the unit of a report differently. Both are
kept until the BA settles it with the client's subject expert.

### Version A - a report wraps a shift (Klimenko, internal)

The entity that wraps everything an on-site engineer records in a [[TRM-002 Shift]], and that the
admin staff view in the web app. "Все, что они делают, все оборачивается в некую сущность, назовем
это отчетом" (Arseniy, [[2026-09-25 Optimum Eng sync - transcript]] 00:08:12).

### Version B - a daily report built from four mud checks (the client)

"At the end of the day you should have four complete mud checks ... those four mod checks are what is
going to constitute, you know, a single daily mock report for that day. It's not going to be. Each mod
check is not a report in and of itself. It's just one of the set of data you need to put in to
generate daily mode report." ([[2025-10-22 First call with OES - transcript]] 0:42:22). Two engineers
share the day in 12-hour shifts; the second one, at the end of his shift, "will generate the report and
share that report with the customer and the office" (1:06:48). See [[TRM-008 Mud check]].

## Context and units

The name in version A is provisional ("назовем") and our own. The client says "daily mud report" or
"daily job report" (0:12:27) and, at the end of a well, "the end of well or the end of job reports"
(0:12:27).

The client's report types: "End-of-Day, End-of-Well, Engineering calculation/simulation, and Inventory
reports ... including end-of-section reports"
([[2025-10-29 Client answers to the Q&A register - rendering]] Part 1, 3). The daily one is titled
"Daily Drilling Fluids Report" ([[2025-10-29 Client sample daily report - rendering]] row 1). The report
types are in [[REQ-010 Reports]].

- The client's names in its samples (added 2026-11-02): "Daily Mud Report" ([[2026-11-02 Client sample daily mud reports - DMR Sample 2.pdf|DMR Sample 2]]) and "Daily
  Drilling Fluids Report" ([[2026-11-02 Client sample daily mud reports - DMR Sample 1.pdf|DMR Sample 1]])
  ([[2026-11-02 Client sample daily mud reports - rendering]]), "End Of Well Recap"
  ([[2026-11-02 Client sample end-of-well recap - rendering]]). The files are named "DMR Sample" and
  "EOWR Sample", and the recap refers to daily reports as "DMR 8", "DMR 14".
- For version B (added 2026-11-02): in the samples each mud sample is a column of the one daily
  report - three in [[2026-11-02 Client sample daily mud reports - DMR Sample 2.pdf|DMR Sample 2]] (08:00, 15:00, 23:00), two in [[2026-11-02 Client sample daily mud reports - DMR Sample 1.pdf|DMR Sample 1]] (10:00, 23:00) - not
  four as on the first call.

## Not to be confused with

Printed or exported report formats, which are not defined yet. A [[TRM-008 Mud check]], which is one of
the data sets a daily report is built from.
