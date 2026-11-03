---
type: risk
id: K-10
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
register: internal
sources:
  - "[[2025-11-25 Contract chat - rendering 5]]"
  - "[[2026-10-13 OE Big4 chat - rendering 1]]"
  - "[[2026-10-13 Optimum Three Caballeros call - transcript]]"
  - "[[2026-10-20 Introductory call - transcript]]"
  - "[[2026-11-02 Client sample engineering reports - rendering]]"
tags:
  - acceptance
  - contract
---
# K-10 Fixed price with vague acceptance criteria

## Risk

Cause: a fixed price ([[DEC-008 Fixed price with milestones, on the client's contract]]) with
acceptance criteria the team calls vague; each deliverable is accepted in writing, the review clock
restarts after each fix, and nothing is accepted by default
([[COM-002 Written acceptance of each deliverable]]). Event: the client withholds acceptance and asks for
rework of what was built to the WBS line. Effect: rework beyond the estimate, and the monthly payments
held, each being due only on verified completion of that month's work ([[COM-012 Payment schedule]]).

Not [[K-5 Scope grows through the prototypes]], which is new scope asked for after seeing the
prototypes; this one is the same scope, accepted late or not at all.

## Why we think so

- The record of the 13 October call lists it first of three: "6. Риски (контрактные риски приняты
  менеджментом ранее)", "Fixed price при размытых критериях приёмки." ([[2025-11-25 Contract chat - rendering 5]]
  2026-10-13 09:55; the draft, [[2026-10-13 OE Big4 chat - rendering 1]] 2026-10-13 09:06).
- Mikhail: "Это fixed price под очень туманные acceptance критерии. по которым клиент может просить нас
  переделывать по 5, 10, 20, 100 раз" ([[2026-10-13 Optimum Three Caballeros call - transcript]]
  00:25:22).
- Kavalchuk: "ты по факту юридически будешь их переделывать ровно столько раз, пока клиент тебе не
  скажет «да, хорошо»" (00:24:33).
- A further cause, outside the baseline (evaluated, added 2026-10-30): the client may judge the tool by
  ISO 9001, ISO 14001 and API compliance, which neither the contract nor the SOW names - "there's no
  point in designing a tool, however user-friendly it is and stuff, that is out of compliance to the
  international standards" (Mr. Lawal, [[2026-10-20 Introductory call - transcript]] 00:45:35);
  [[CON-008 Compliance with ISO 9001, ISO 14001 and API standards]].
- A further cause (evaluated, added 2026-11-02): the client's hydraulics references are a commercial
  program's outputs, with multi-depth sensitivities, cuttings transport and torque and drag
  ([[2026-11-02 Client sample engineering reports - rendering]]); read as the target, they would set
  acceptance against a commercial package. Treated through
  [[QUE-013 Which calculations from the sample reports the simulation must cover]].

## Response and next action

In the record: "Митигация: прототипы и acceptance клиента до старта разработки соответствующих частей
(п. 3), реестр рисков (п. 2.1). → Андрушкевич, Опариенко, Клименко." The prototypes:
[[DEC-010 Confirm the product with the client through prototypes in code]],
[[DEC-015 Discovery - our own picture of the system, questions as if from scratch]]. A PM scores it and
names the owner.

## History

- 2026-10-14 written as a draft from the record of the 13 October call (the contract chat's part 5) and
  the OE Big4 chat; not scored.
- 2026-10-30 updated: compliance with ISO and API standards as a further cause (the call of 20 October); not scored.
- 2026-11-02 updated: the client's sample program reports as a further cause; not scored.
