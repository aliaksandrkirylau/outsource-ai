---
type: concern
id: CON-004
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: quality
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 1]]"
  - "[[2026-10-12 Optimum Three Caballeros call - transcript]]"
capabilities:
  - "[[CAP-002 Offline data and sync between rigs and HQ]]"
  - "[[CAP-011 Platform, environments and handover]]"
tags:
  - scale
  - retention
---
# CON-004 Scale and data volume

## What must hold

The system works for the client's size today and the growth they expect, and keeps the data as long as
they need it. The figures, as the client gave them:

- Rigs: "Yes. But can potentially reach 100 based on market activity. Solution should be scalable." -
  to "approximately 70 locations (rigs/sites) with around two engineers working at each location"
  ([[2025-10-29 Client answers to the Q&A register - rendering]] Part 1, 7).
- Users per computer: 1 to 4 engineers share one rig computer (Part 1, 9).
- Data entered: "less than 50" parameters, "manually inputted approximately 4 times per day" - "Yes"
  (Part 1, 2).
- Shifts: "Per 12-hour shift every operating day on all active locations (rigs)." (F.28)
- A well: "Well drilling duration is about 2 month avg" ([[2025-10-22 First call with OES - notes]] key
  point 5).
- Retention of raw measurements, logs and attachments: "Between 1-2 years" (C.8) - a range, not one
  figure.

From the first call's transcript (added 2026-09-28, batch 2):

- "at the height of some of our operation simultaneously, we can be on up to 70 location at the same
  time with engineers in all these 70 locations" ([[2025-10-22 First call with OES - transcript]]
  0:12:27).
- A well: "each well can take between 30 to 45, sometimes 60 or more days" (0:12:27) - the notes' "about
  2 month avg" is the notes' summary of the same.
- "it's a 24, 24 hour operation every single day until you complete the job" (0:42:22).
- A project supervisor "may has 10, 15 grilling rig under his domain" (0:25:39).
- "That's quite a large amount of data that is being generated on daily basis" (0:12:27), and the client
  wants to "query the database and get more insights in terms of data analytics" (0:12:27).

The team's reading of daily volume (added 2026-10-13; [[2026-10-12 Optimum Three Caballeros call - transcript]]): Mikhail - "это может быть десяток
параметров или пара десятков за сутки" per rig, entered by hand (00:07:23); "порядка 70 вышек, ну,
там, окей, до сотни" (00:04:01). This is below the client's own figures above (under 50 parameters
about 4 times a day per rig, plus inventory). Both kept; it was the argument for dropping the Redis
queue ([[CON-001 Offline operation and sync between rigs and HQ]]).

## Why

The architecture, the sync and the reporting load are sized on these numbers. The SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) says its architecture assumes "the expected data volumes, user activity, reporting workloads,
synchronization frequency" known at estimation, and that "Dedicated high-load optimization, advanced
scalability engineering, stress testing" are not included.

In presale the architect saw no need for a data engineer: "Я не вижу необходиости в Data Engineer -
судя по описанию данных не много" ([[2025-10-20 Presale chat - rendering 1]] 2025-11-04 11:30; added
2026-09-28, batch 5).

## Affected requirements

- [[REQ-001 Record and calculate a shift without internet]]
- [[REQ-010 Reports]]
- [[REQ-011 Dashboards and KPIs]]

## Treatment

Not decided. The number of HQ users (managers, supervisors, admins) is not in any source.
