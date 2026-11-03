---
type: decision
id: DEC-014
status: proposed
origin: extracted
author: claude-code/claude-opus-5-5
kind: delivery
deciders:
  - human:mikhail.andrushkevich
  - human:anton.oparienko
  - human:arseniy.klimenko
sources:
  - "[[2025-11-25 Contract chat - rendering 4]]"
  - "[[2026-10-13 Optimum Three Caballeros call - transcript]]"
  - "[[2025-11-25 Contract chat - rendering 5]]"
  - "[[2026-10-13 OE Big4 chat - rendering 1]]"
  - "[[2026-09-25 Core chat - rendering 1]]"
  - "[[2026-10-27 Optimum Three Caballeros call - transcript]]"
  - "[[2026-10-28 Optimum sync - transcript]]"
valid_from: 2026-09-29
tags:
  - staffing
  - delivery
---
# DEC-014 Staff on demand, seniors who work with Claude, fewer developers

## Context

The first plan was the fastest possible start, with staffing before the project officially started.
After talking to the project's account manager, Aliaksandr Kavalchuk, who has worked with clients in
the region, the team judged delays on the client's side likely, both in signing and later in access,
information, feedback and decisions. Mikhail, recording the change "к которым мы пришли в обсуждениях
с @Anton Oparienko и @Arseniy Klimenko": "мы оценили как высокий риск задержек со стороны клиента как
на этапе подписания документов, так и в дальнейшем при предоставлении доступов, информации, обратной
связи и принятии решений" ([[2025-11-25 Contract chat - rendering 4]] 2026-09-29 15:51).

The presale staffing plan had, among other roles, two back-end and two front-end developers and a
solution architect, and the presale had considered relatively cheap specialists because the average
rate was low (the figure is removed). Deciders confirmed by Anton Oparienko in the ingest session,
2026-10-13.

## Options considered

1. The fastest start: "не терять время и начинать стаффинг еще до официального запуска проекта". Not
   taken: idle time if the client is slow.
2. The presale team of cheaper specialists. Not taken: "Для Fixed Price проекта такой подход, на наш
   взгляд, не является оптимальным."
3. On demand, seniors who work with AI, fewer developers. Chosen.

## Decision

The planning principle moves "с «максимально быстрый старт» на «минимизацию потерь из-за вероятных
простоев команды»". In practice (Mikhail, 2026-09-29 15:51):

- "По возможности специалисты будут подключаться на on-demand основе."
- "Если on-demand формат невозможен, специалист на фиксированной аллокации будет подключаться только
  тогда, когда для него разблокирован объем работ хотя бы на ближайшие 2-3 недели."
- Instead of the presale's 2 BE + 2 FE and a solution architect: "начать с сильного TL / AR/ Full-stack
  разработчика, хорошо работающего с Claude; добавлять Full-stack разработчиков только по мере
  устойчивого роста backlog задач, действительно готовых к разработке; одновременно нам, вероятно,
  понадобится не более двух таких разработчиков, причем не с самого старта проекта."
- "Также потребуется BA, умеющий работать с Claude Design и быстро создавать кликабельные прототипы для
  согласования с клиентом"; "дизайнер потребуется на существенно меньшую аллокацию либо может не
  понадобиться вовсе."

Acknowledged: Kavalchuk listed the SOW, the client's contact and backlog clarity as what sets the pace
(16:05); Alexey Gamanovich: "все правильно говоришь ... продолжаем подготовку" (16:06).

Refined on 12 and 13 October: no tech lead from day one; an architect on demand, "чтобы наш аналитик
не нафантазировал себе систему, которую нельзя собрать. Вот здесь просто на уровне консультации"
(Kavalchuk, [[2026-10-13 Optimum Three Caballeros call - transcript]] 00:15:24), after Mikhail: "я вот и
не был уверен, что нам нужен техлит прямо вот на дискавере" (00:14:13). Arseniy: "архитекторского
опыта прямо коммерческого у меня нет. Но в целом да, почему нет?" (00:15:43). Anton: "Потенциально TL
на парттайм хотя бы с флаттера тоже может нужен быть" ([[2025-11-25 Contract chat - rendering 4]]
2026-10-12 11:05).

In the record of 13 October (added 2026-10-14; [[2025-11-25 Contract chat - rendering 5]] 2026-10-13 09:55): "Ключевая роль на старте — BA,
который работает с Claude Design: быстро генерирует прототипы, собирает обратную связь и получает
acceptance клиента." - the draft had "с кодом и Claude", struck by Mikhail ([[2026-10-13 OE Big4 chat - rendering 1]] 2026-10-13 09:18); "→
Андрушкевич, Клименко, Опариенко: привлечение других специалистов on demand по необходимости (например,
для подготовки SAD)." The SAD, the Solution Architecture Design, is a Milestone 1 deliverable
([[COM-020 Milestone plan and deliverables]]). The BA's allocation in the position Anton posted on 14
October: "full-time at the start of the project, fewer hours later in development" ([[2026-09-25 Core chat - rendering 1]] 2026-10-14
08:35).

The tech lead, 27 and 28 October (added 2026-10-30). No longer holds: no tech lead in Discovery (13
October, above). Anton: "В начале, в серединке discovery берем техледа. Он начинает смотреть на наши
прототипы, технически общаться с клиентом"; "Этот же человек в течении проекта дальше начинает писать
код, он начинает писать core функциональность"; a second Flutter developer, "можно не такого
сеньориста", added "как только он говорит, что есть возможность. То есть мы не будем там троих людей
ставить"; not "человечек, который приходит на миты, что-то там говорит и сваливает в закат"
([[2026-10-27 Optimum Three Caballeros call - transcript]] 00:18:15). Arseniy: "Скорее всего, у нас будет
техлит, и Губкин будет за ним смотреть. Мы говорили, что он будет постоянно здесь, как раз таким
ментором." (00:19:47); fewer developers, full-stack on Supabase, again (00:17:46;
[[DEC-004 Backend stack]]). Arseniy sends the tech lead profile, "стек, реквайерменты", for staffing
(00:16:55). Mikhail, 28 October, for the kick-off deck: "основные люди для Discovery— это BI, это
TechLead. По необходимости будет UI и X-дизайнер привлекаться в OnDemand. Разработчики подключатся
позже." ([[2026-10-28 Optimum sync - transcript]] 00:03:25; "BI" is the BA). Deciders as listed; this
change not separately confirmed (Anton Oparienko, ingest session 2026-10-30).

## Rationale

"лучший ROI здесь может дать сочетание AI и более опытных специалистов, умеющих эффективно его
использовать" (2026-09-29 15:51). On 13 October Mikhail called Claude the one factor that can change the
picture: fewer people, "минус дизайнер, меньше разработчиков"
([[2026-10-13 Optimum Three Caballeros call - transcript]] 00:16:21).

## Consequences

- Downside: "такой подход усложнит предварительное планирование ресурсов" (2026-09-29 15:51).
- Downside: "с высокой вероятностью приведет к увеличению фактического срока и мы можем не успеть за 6
  месяцев, зафиксированных в контракте. К сожалению, по текущим условиям контракта задержки со стороны
  клиента не освобождают нас от обязательства выполнить delivery в установленный срок" (same message;
  [[COM-001 Delivery within six months]], [[COM-008 Client cooperation and dependencies]]).
- New obligation: a BA who prototypes with Claude, which is hard to find ([[K-6 No suitable BA in time]]),
  and estimates that assume Claude-assisted development ([[K-7 Estimates for Claude-assisted development do not hold]]).
- Against the SOW (evaluated): the UI Kit and "Main UI/UX mockups" stay Milestone 1 deliverables with a
  much smaller designer ([[COM-020 Milestone plan and deliverables]];
  [[DEC-010 Confirm the product with the client through prototypes in code]]).
- Easy to reverse: people are added as the backlog grows.
- Related: [[DEC-002 Senior engineers first]], [[DEC-015 Discovery - our own picture of the system, questions as if from scratch]].
