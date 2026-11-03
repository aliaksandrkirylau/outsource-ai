---
type: commitment
id: COM-017
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
party: us
due: for the term and after it
clause: "12.1-12.4"
sources:
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 3]]"
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
tags:
  - liability
---
# COM-017 Liability, indemnity and force majeure

## What is owed

From the contract ([[2026-09-07 Final contract - rendering]]):

- "Each Party is liable for direct losses caused by its breach, negligence or unlawful conduct." (12.1)
- Innowise indemnifies the client "against third-party claims arising from intellectual property
  infringement, breach of confidentiality, data/security violations attributable to the Second Party,
  or unlawful acts of its personnel." (12.2)
- "Any contractual liability cap shall not apply to fraud, wilful misconduct, gross negligence,
  confidentiality breach, data/security breach, or intellectual property infringement. For other
  claims, the Second Party's aggregate liability shall not be less than the total Contract price."
  (12.3) - a floor, not a cap; the text sets no cap.
- Force majeure only for "a genuine force majeure event beyond reasonable control"; "Lack of personnel,
  subcontractor failure, cost increases, ordinary technical difficulties or foreseeable supply issues
  shall not constitute force majeure." (12.4)

The SOW v10.4 has limits of its own, not in the contract: the Contractor is "responsible only for
compliance with technical tasks and for the quality of the Services"; not for the deliverables' impact
on the client's business, for code changed by others, or for other environments and versions
([[2026-06-15 SOW v10.4 - rendering]] row 37). The contract ranks the Agreement above the SOW (1.3).
Legal reading: ask a PM.

How it came about (added 2026-09-28, batch 6; [[2025-11-25 Contract chat - rendering 3]]): in the
earlier Word version "Лимит ответственности Исполнителя ограничен фактически полученной суммой по
контракту"; in the client's final "Лимит ответственности Исполнителя теперь не может быть ниже общей
стоимости контракта ... По нарушениям IP, конфиденциальности и безопасности данных лимит ответственности
полностью отсутствует" (Lizaveta Shauchenka's summary, 2026-08-12 13:28; the amount removed). Innowise
asked to keep a limited cap (2026-08-25 07:27); the client declined to reopen the contract (2026-09-02
15:55).

The team's reading, 1 October (added 2026-10-02; [[2026-10-01 Optimum Three Caballeros call - transcript]]
00:16:00): a formula bug whose recommendation is followed at a rig could damage a well. "Словно
говоря, у нас там баг, формула не та. Они рекомендациям последовали, скважину поломали, убытки на
[amount removed]. По текущим контрактам все эти убытки, за них несем ответственность мы." (Mikhail
Andrushkevich). Legal reading: ask a PM. [[K-2 Losses from a calculation defect fall on us]].

## By when

Not applicable.

## How it is accepted

Not applicable.

## Drives

- [[COM-010 Qualified personnel and approved subcontractors]] (staffing gaps are not force majeure)
- [[CON-003 Correct calculations]] (a calculation defect, by the team's reading of 1 October)
- [[K-2 Losses from a calculation defect fall on us]]
