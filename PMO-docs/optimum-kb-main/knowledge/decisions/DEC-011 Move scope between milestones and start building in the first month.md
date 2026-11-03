---
type: decision
id: DEC-011
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: delivery
sources:
  - "[[2026-09-28 Optimum discuss next steps - transcript]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
  - "[[2025-11-25 Contract chat - rendering 4]]"
  - "[[2026-10-13 Optimum Three Caballeros call - transcript]]"
valid_from: 2026-09-28
tags:
  - delivery
  - milestones
  - discovery
---
# DEC-011 Move scope between milestones and start building in the first month

## Context

The SOW v10.4 makes Milestone 1 the discovery: analysis, requirements, scope, risks, architecture and
UI/UX design, with its own deliverables ([[COM-020 Milestone plan and deliverables]]). The team's
reading on 28 September: this discovery is "не классическое ... мы же там особо показания потом не
можем поменять сильно после него в плане оценки" (Arseniy,
[[2026-09-28 Optimum discuss next steps - transcript]] 00:09:39), so "Имеет смысл считать, что проект
стартанул, и нам его делать при любом раскладе" (Mikhail, 00:09:54). The contract's scope per milestone
"довольно краткий, но high-level он есть" (Mikhail, 00:27:37); how strictly to follow it is open
(Arseniy, 00:27:48).

## Options considered

1. Milestone 1 as pure discovery, as the SOW has it, and building from Milestone 2. Not taken, in
   Mikhail's view: "полный discovery на полный сколп мы за один месяц все равно не сделаем" (00:28:25).
2. Take as an assumption that scope can move between milestones, start some of the next milestone's
   scope in the first month and start coding. Proposed.

## Decision

A proposal: "Я предлагаю посчитать за Assumption, что сколп между milestone'ами мы подвигать сможем.
Потому что, да, первый он там описывает чистый discovery. На мой взгляд, полный discovery на полный
сколп мы за один месяц все равно не сделаем. А какой-то сколп там из следующего milestone'а имеет смысл
начинать делать в первый же месяц, закладывать в базу проекта. и начинать что-то уже кодировать."
(Mikhail, 00:28:25). Not answered in the call; no deciders named, so draft.

Alexey Gamanovich's view, 1 October (added 2026-10-02; [[2026-10-01 Optimum Three Caballeros call - transcript]]):
"Когда проект стартует, то первые шаги там условно не девелоперские, типа сидеть и код крафтить, а
зайти к клиенту и просто показать это. Вот смотрите, мы видим это вот так, это будет работать так, так,
так, вот так будут отправляться новые версии приложений и так далее, чтобы они сразу на этом этапе дали
обратную связь" (00:09:32); "первые шаги они будут не девелоперские, первые шаги они будут запитчить"
(00:26:17). Recorded beside Mikhail's proposal; the call did not settle whether the two clash (pitch
first, then code within month 1) or not.

What no longer holds (added 2026-10-13): starting to code in the first month. Mikhail, 12 October: "С
разработкой я бы не спешил, дождался первых результатов работы ВА." ([[2025-11-25 Contract chat - rendering 4]] 2026-10-12 10:28); on 13
October developers join an area only "после того, как прототип показан, прокликан, заопроводен"
([[2026-10-13 Optimum Three Caballeros call - transcript]] 00:14:13; [[DEC-010 Confirm the product with the client through prototypes in code]]).
Moving scope between milestones was not discussed.

## Rationale

Discovery of the full scope does not fit one month, and the estimate will hardly change after it, so
waiting a month to start building buys little (00:09:39, 00:28:25).

## Consequences

- New obligation: the milestone scope is in the contract, so the client has to agree the new split,
  in writing ([[COM-020 Milestone plan and deliverables]],
  [[COM-018 Written minutes, notices and amendments]]). Arseniy: "наверное, он открыт будет, если мы
  предложим свой вид распределения по мейлстоунам" (00:27:48).
- Downside: Milestone 1's written acceptance then covers a different set of deliverables than the SOW
  lists ([[COM-002 Written acceptance of each deliverable]]).
- It runs against a line of the 7 September management call: "Разработку не начинаем, пока не закроем
  основные вопросы и не убедимся, что команда одинаково понимает scope - чтобы минимизировать переделки
  на FP." ([[DEC-009 Sign the client's final contract as it stands]]). Not settled here; for the
  deciders.
- Related: [[DEC-010 Confirm the product with the client through prototypes in code]].
