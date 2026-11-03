---
type: decision
id: DEC-002
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: delivery
deciders:
  - human:alexey.gamanovich
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-11-25 Contract chat - rendering 3]]"
  - "[[2026-09-28 Optimum discuss next steps - transcript]]"
  - "[[2026-09-30 Optimum Three Caballeros call - transcript]]"
  - "[[2025-11-25 Contract chat - rendering 4]]"
  - "[[2026-10-13 Optimum Three Caballeros call - transcript]]"
valid_from: 2026-09-25
tags:
  - staffing
---
# DEC-002 Senior engineers first

## Context

Staffing launches the week of 28 Sep. Alexey spoke to Sergei Gubkin (Flutterstack) about finding
the right people for the first part of the project ([[2026-09-25 Optimum Eng sync - transcript]]
00:00:04).

The same line was agreed on the 7 September call that decided to sign (added 2026-09-28, batch 6):
"Команду планируем подключать постепенно. На старте нужны сильные специалисты для проработки
архитектуры/логики и особенно расчетных формул; после стабилизации требований можно оптимизировать
состав и стоимость команды." (Yauheni Krasner's summary, [[2025-11-25 Contract chat - rendering 3]]
2026-09-07 10:32, point 5; [[DEC-009 Sign the client's final contract as it stands]]). `valid_from`
stays 2026-09-25 until the decider says otherwise.

Which roles first (added 2026-09-28, the call of that day;
[[2026-09-28 Optimum discuss next steps - transcript]]):

- "прямо сейчас нам BA, дизайнер, не знаю, архитекторов слэш техлит, вот кого-то такого искать"
  (Mikhail, 00:09:06), the tech lead or architect "кто сможет сам и код пописать" (00:07:44); regular
  developers "прям сейчас не надо, потому что писать неизвестно когда там первая строчка будет
  написано" (00:08:49). The designer then went down to token hours:
  [[DEC-010 Confirm the product with the client through prototypes in code]].
- A tech lead from the mobile department is worth considering, since that department builds it, rather
  than an architect from another department with a different view: "Возможно, стоит рассмотреть тех
  лидов из отдела мобайл" (Arseniy, 00:10:29).
- Arseniy's own role: DM, with a "технически валидационная" role - "или я эту роль займу, или я буду как
  бы в любом случае финальным проволокой технической части", and AI in delivery (00:05:25).
- The solution architect, planned in the P&L for the first month only, becomes a position that stays
  with the project (Anton, 00:24:54); the P&L gets a staffing tab (00:26:47).
- The BA is not sought in the Emirates: "Тогда ищем без... не в Эмиратах." (Mikhail, 00:13:04). Where our
  people may sit at all: [[QUE-009 Where may our team members be located]].

The tech lead from the mobile department, 30 September (added 2026-10-13; [[2026-09-30 Optimum Three Caballeros call - transcript]]): Arseniy would
have Sergei Gubkin, whom he sees as a possible tech lead, draw the diagrams first - "А если в итоге он
не будет техником, то диаграммы у нас все равно будут более валидные, чем у меня" (00:02:52); "Пусть
кто-то будет там проверенный" (00:05:59). Anton doubts the time: "у него не будет хватать времени. С
него никто не снимет всю внутреннюю нагрузку, слежение за 20 интернами" (00:05:36). Not decided.

The team shape since 29 September (added 2026-10-13):
[[DEC-014 Staff on demand, seniors who work with Claude, fewer developers]] - seniors who work with
Claude rather than the cheaper team the presale considered, brought in on demand. No longer holds: the
solution architect as a position that stays with the project (Anton, 28 September, above). On 13
October the architect became an on-demand consultant, "Вот здесь просто на уровне консультации"
(Kavalchuk, [[2026-10-13 Optimum Three Caballeros call - transcript]] 00:15:24). The tech lead from the mobile department is still open.

## Options considered

1. A cheaper team mix from day one. Not taken now; to be looked at later: "Дальше будем смотреть с
   точки зрения удешевления стоимости работ" (00:00:04).
2. The right senior people for the first part, so they can put the key parts of the system in place.
   Chosen.

## Decision

"На первом этапе обязательно, чтобы были такие правильные, подходящие бойцы" (Alexey, 00:00:04).
Senior engineers first; cost optimisation of the team is revisited later.

## Rationale

The first part sets up the backbone of the system; seniors reduce the risk there.

## Consequences

- Downside: a more expensive team in the first months.
- New obligation: a point at which the team mix is reviewed for cost. Not set yet; the 7 September
  summary ties it to requirements stabilising ("после стабилизации требований").
