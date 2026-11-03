---
type: commitment
id: COM-004
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
party: us
due: twelve (12) months from final written acceptance
clause: "3.5"
sources:
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2025-11-05 Proposal slides - rendering]]"
  - "[[2025-12-30 Answers to the client's questions - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
  - "[[2025-11-25 Contract chat - rendering 3]]"
tags:
  - warranty
---
# COM-004 Twelve-month warranty

## What is owed

"The Second Party warrants all Deliverables for twelve (12) months from final written acceptance.
During the warranty period, defects attributable to the Second Party shall be corrected without
additional charge." ([[2026-09-07 Final contract - rendering]] 3.5)

Not in the estimate (added 2026-09-28, batch 4): "Post-deployment support efforts are not included"
([[2026-09-25 v1 WBS - rendering]], Assumptions & Risks 25). Its DevOps post-release line is "Optional";
without it "the development team remains responsible for the first weeks after release" (DevOps row 15).
So correcting defects over the twelve months has no line in the WBS (our reading).

## By when

Twelve months from final written acceptance.

## How it is accepted

Not stated beyond defect correction.

History, not in force: presale offered "3 weeks warranty period after project release date"
([[2025-11-05 Proposal slides - rendering]] slide 32); the client asked on 24 November 2025: "Kindly
review the minimum guarantee period post-production and extend it from 3 weeks to 6 weeks"
([[2025-10-20 Presale chat - rendering 2]] 2025-11-24 12:10; added 2026-09-28, batch 5); in December 2025
"The warranty period has been
increased to six (6) weeks" ([[2025-12-30 Answers to the client's questions - rendering]], 1). The
optional monthly support package offered then, in the draft reply: "Bug Fixing and Incident Resolution",
"Technical Support and Administration", "Keeping Systems Updated" (2025-11-24 12:44). Support is
a separate matter: the SOW v10.4 says "Support and maintenance services shall be governed exclusively
by a separate Service Level Agreement ('SLA'). All support-related obligations are expressly excluded
from the scope of this Agreement unless otherwise agreed in writing."
([[2026-06-15 SOW v10.4 - rendering]], assumptions)

How the twelve months came in (added 2026-09-28, batch 6;
[[2025-11-25 Contract chat - rendering 3]]): in the client's final contract of August 2026 ("Введена
бесплатная гарантия на 12 месяцев с момента финальной приемки", Lizaveta Shauchenka, 2026-08-12 13:28).
Innowise proposed a paid SLA with a small team instead (2026-08-25 07:27). The client declined and
clarified on 2 September: "The twelve-month warranty under the Agreement is not intended to require
INNOWISE to provide unlimited operational support, consultancy services, enhancements, or new development
without compensation. The warranty relates specifically to the quality of the work delivered under the
Agreement. Accordingly, where a defect, programming error, malfunction, non-conformity, or failure to
meet the agreed requirements is attributable to the work performed by INNOWISE, its correction falls
within the contractual warranty and should not result in an additional cost to the Customer. This is
fundamentally different from post-delivery support or further development." New functionality goes
through change requests, and an SLA "if and when such services are required" (2026-09-02 15:55).
Accepted as a known risk on 2026-09-07 ([[DEC-009 Sign the client's final contract as it stands]]). The
contract does not define the defect classes beyond Critical, Major, Minor and Trivial (2026-09-03
11:35).

## Drives

- [[COM-003 Quality and defect correction at no charge]]
