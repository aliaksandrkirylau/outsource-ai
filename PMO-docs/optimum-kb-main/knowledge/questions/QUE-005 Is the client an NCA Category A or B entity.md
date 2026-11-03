---
type: question
id: QUE-005
status: proposed
origin: evaluated
author: claude-code/claude-opus-5-5
asks: client
answered_by:
sources:
  - "[[2026-07-14 Cybersecurity framework - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-11-05 WBS sent to the client - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 3]]"
tags:
  - security
  - compliance
---
# QUE-005 Is the client an NCA Category A or B entity

## Question

Under the Saudi National Cybersecurity Authority's classification, is Optimum Engineering Standards a
Category A or a Category B entity?

## What it blocks

Whether regular penetration testing is required: "If the client is Category A, you are required to
perform regular penetration testing (you may need to outsource this to an NCA-approved entity). For
Category B, it is recommended." ([[2026-07-14 Cybersecurity framework - rendering]], Framework 1).
Note: [[CON-007 Saudi cybersecurity and data protection rules]].

Neither WBS has penetration testing (checked 2026-09-28, batch 4). The v1 WBS ([[2026-09-25 v1 WBS - rendering]]) DevOps tab has no security
testing line, and its Quality Assurance line is a share of development with no breakdown (DevOps rows
6 to 16, Total Estimation Development Flutter rows 17 and 25). The WBS sent to the client had "security scanning (SAST)" in CI and "RBAC Security Testing
Integration", not penetration testing ([[2025-11-05 WBS sent to the client - rendering]], DevOps rows 12
and 21). So it blocks Total Estimation Development Flutter!25 (DevOps) and !17 (Quality Assurance).

## Options

- Category A: penetration testing required, by an NCA-approved entity if outsourced.
- Category B: recommended.

## Answer

Not confirmed by the client. Our reading (added 2026-09-28, batch 6): Category B. Alexey Gamanovich
checked the client against the category table of NCNICC-1 and concluded "= category B" after Uladzislau
Murashka's "вроде бы у них до 100 сотрудников" and a revenue threshold
([[2025-11-25 Contract chat - rendering 3]] 2026-07-14 11:42 to 11:56); later that day: "документ сверх
естественный условий не диктует для Category B (наш кейс)" (12:05). "вроде бы" - it seems - is a guess
at the client's size, not the client's statement. For Category B, penetration testing is recommended,
not required ([[2026-07-14 Cybersecurity framework - rendering]]). Open until the client confirms, or
Anton accepts our reading.
