---
type: commitment
id: COM-002
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
party: client
due: fourteen (14) business days after a formal delivery
clause: "3.2, 3.3"
sources:
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 3]]"
tags:
  - acceptance
---
# COM-002 Written acceptance of each deliverable

## What is owed

The client tests each formal delivery and either accepts it in writing or issues a defect list.
"Deliverables shall be subject to testing and written acceptance by the First Party. Silence, use for
testing, partial use, access to a staging environment, or lapse of time shall not constitute deemed
acceptance." ([[2026-09-07 Final contract - rendering]] 3.2)

## By when

"The First Party shall have fourteen (14) business days after a formal delivery to test and either
accept the Deliverable or issue a defect/non-conformity list. The acceptance period shall restart after
corrected delivery." (3.3)

## How it is accepted

In writing only; there is no deemed acceptance. The SOW v10.4 says "The Customer accepts Deliverables
in accordance with the procedure and within the terms set forth in clauses 7.9 – 7.10 of the
Agreement" ([[2026-06-15 SOW v10.4 - rendering]], assumptions), but 7.9-7.10 of this contract are the
monthly progress report and the price cap; see
[[QUE-006 Which SOW and which plan are Annex 1 and Annex 2]].

How it came about (added 2026-09-28, batch 6; [[2025-11-25 Contract chat - rendering 3]]): Innowise's
frame had deemed acceptance after 14 days (7.10); the client's final contract removed it - "Прямо
указано, что молчание, тестирование или использование системы не являются приемкой. Если Заказчик
находит баг, 14 дней на проверку запускаются заново с нуля после исправления" (Lizaveta Shauchenka,
2026-08-12 13:28). Innowise asked to keep deemed acceptance (2026-08-25 07:27); the client declined to
reopen the contract (2026-09-02 15:55). Accepted as a known risk on 2026-09-07: "отсутствие automatic
acceptance (потенциальная бесконечная приемка без оплаты)" (2026-09-07 10:32;
[[DEC-009 Sign the client's final contract as it stands]]).

## Drives

- [[COM-012 Payment schedule]] (payments follow accepted work)
- [[COM-013 Source code, IP and third-party components]]
