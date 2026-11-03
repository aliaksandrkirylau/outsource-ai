---
type: concern
id: CON-006
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: compliance
sources:
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2026-11-02 Client sample daily mud reports - rendering]]"
  - "[[2026-11-02 Client sample end-of-well recap - rendering]]"
  - "[[2026-11-02 Client sample engineering reports - rendering]]"
capabilities:
  - "[[CAP-012 Security and compliance]]"
tags:
  - security
  - confidentiality
---
# CON-006 Confidentiality of the client's customers' data

## What must hold

Data about the client's own customers (oil companies such as Saudi Aramco) is stored and shared only
as the client allows. No measure yet.

## Why

"Security: Client has concern on confidentiality of data storing - especially his customers' details."
([[2025-10-22 First call with OES - notes]] key point 7). Reports go out to "Client personnel, field
supervisors and management" ([[2025-10-29 Client answers to the Q&A register - rendering]] C.10). Asked
whether customer details need masking in shared reports: "Data masking/redaction feature not required.
However, filtering of data for specific reports should be possible." (D.17)

In the client's words on the first call (added 2026-09-28, batch 2): "Confidential customer data and we
have confidentiality to protect" - the reason not to depend fully on a cloud
([[2025-10-22 First call with OES - transcript]] 0:44:41). Letting the client's customers into the
software is a risk the client named itself: "if you have not QCed the data prior to your customer having
access can open you up to issues" (0:29:42).

The client's samples of 2 November 2026 came anonymised (added 2026-11-02): operator, well, rig,
field and every person blank, the headers of the property tracking pages blacked out
([[2026-11-02 Client sample end-of-well recap - rendering]] pp [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=12|12]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=17|17]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=22|22]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=27|27]];
[[2026-11-02 Client sample daily mud reports - rendering]]). Two well identifiers are left in (the
recap, [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=16|p16]]; [[2026-11-02 Client sample engineering reports - rendering]], [[2026-11-02 Client sample engineering reports - Hydraulics Report Sample.pdf#page=2|Hydraulics Report Sample p2]]), kept as printed on Anton's call. Evaluated: the client strips its customers' identity before
data leaves the company. The prices and costs kept in those renderings are the client's commercial
data (AGENTS.md rule 7).

## Affected requirements

- [[REQ-010 Reports]]
- [[REQ-004 Roles and what each role can do]]

## Treatment

Not decided. The Saudi rules presale set out in July 2026 are
[[CON-007 Saudi cybersecurity and data protection rules]]; where the data may live is
[[CON-002 Deployment outside public cloud]].
