---
type: decision
id: DEC-015
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: delivery
deciders:
  - tbd
sources:
  - "[[2026-10-13 Optimum Three Caballeros call - transcript]]"
  - "[[2025-11-25 Contract chat - rendering 4]]"
  - "[[2025-11-25 Contract chat - rendering 5]]"
  - "[[2026-10-13 OE Big4 chat - rendering 1]]"
  - "[[2026-10-14 Project email thread - rendering 1]]"
valid_from: 2026-10-13
tags:
  - discovery
  - delivery
---
# DEC-015 Discovery - our own picture of the system, questions as if from scratch

## Context

The client has signed the Agreement, and the team that now runs the project joined after the estimate.
Mikhail: "Нам надо сделать project management модуль, и на него две или три строчки. Нам надо сделать
inventory management, и на этом тоже две или три строчки. Ну, come on, это просто несерьезно."
([[2026-10-13 Optimum Three Caballeros call - transcript]] 00:07:02); the estimators worked from
"буквально один митинг" with the client (00:10:29). Kavalchuk did not want to go to the client "без
плана Discovery, без списка вопросов ... без какой-то собственной идеи", since we estimated and signed a
budget (00:07:41). By contract, clarifying questions are no evidence that our information was
insufficient ([[COM-006 Information sufficient for scope and price]]).

## Options considered

Mikhail put the first two (00:10:01 to 00:11:51):

1. Go to the client with open questions, a full discovery from zero. Not taken: it shows we signed
   without understanding what.
2. Design the system ourselves, prototype it and then show it. "Скорее всего, нам скажут, что все
   везде там не так, но, возможно, выглядеть мы будем немножко получше". Not taken on its own: a risk
   of missing (Anton, 00:11:56).
3. Anton's hybrid: "почему мы не можем замаскировать полный Discovery под наличие плана? ... вот смотрите,
   вот как мы представляем себе сейчас там приложение ... На самом деле начинать Discovery с ними как с
   нуля" (00:11:56). Kavalchuk: "я склоняюсь согласиться с тобой о том, что надо где-то промежуточное
   что-то такое делать" (00:12:43). Chosen.

## Decision

Discovery starts from our own picture of the system - the WBS modules and blocks - and asks the client
as if from scratch. The BA builds it as prototypes
([[DEC-010 Confirm the product with the client through prototypes in code]]), minimal: "ты на VBS, на
SOF смотришь, но делаешь все там минималистично, а дальше расширяем уже, когда клиент приходит и
начинает говорить" (Mikhail, 00:33:15). ("VBS" is the WBS, "SOF" the SOW.)

Agreed with it in the call:

- The BA starts before the client names a contact, on the project budget: "если мы найдем подходящего
  кандидата, то я предлагаю начинать жрать бюджет проекта прямо сейчас, и чтобы BA начинал готовить эти
  прототипы" (Mikhail, 00:49:37); "Можешь." (Kavalchuk, 00:49:51) - with hours and deliverables set up
  front: "договариваемся с аналитиком ... давайте неделя, такие-то Deliverable от аналитика, первая
  итерация такая" (Arseniy, 00:52:32).
- A discovery plan and timeline as an artifact for the client's contact (Kavalchuk, 00:39:09,
  00:48:04).
- Budget watched per area: "у нас в ВБС-ке было три строчки, они были оценены вот так-то, B предложил
  минималистичное решение ... Клиент пришел, требует вот такое ... будем красный флаг поднимать"
  (Mikhail, 00:43:53).
- After discovery, an internal call on any overrun: "Мы либо забираем этот перерасход на себя, либо
  скидываем его на клиента, либо делаем гибрид" (Kavalchuk, 00:36:55). Mikhail: by contract there is no
  go/no-go (00:42:31); Kavalchuk means not keeping quiet about it (00:42:44).

Not named as decided by anyone; deciders tbd (Anton Oparienko, ingest session 2026-10-13).

The record of the call, published on 13 October (added 2026-10-14; [[2025-11-25 Contract chat - rendering 5]] 2026-10-13 09:55, after
Mikhail's corrections in [[2026-10-13 OE Big4 chat - rendering 1]]): "Гибридный формат: приходим с подготовленной структурой системы (модули,
блоки), но требования собираем с клиентом заново." Target results: "1) уточнённая WBS; 2) кликабельные
прототипы (Claude Design); 3) acceptance клиента". "Если Discovery не уложится в месяц, управление
сроками и готовностью результатов — на PM и DM." "Порядок acceptance прототипа (целиком или по частям) и
момент старта разработки определяют PM и DM."

Mikhail's corrections to the draft, which had "выверенная WBS", prototypes "по каждой фиче" and
acceptance "по каждому модулю": "Коммитаться на такое не можем, это программа-максимум. Хотелось бы
получить за месяц, но тот же акцептанс и длительность фидбек лупов зависит от клиента.
Программа-минимум - акцептанс на деливераблс для следующей фазы (1 месяц)."; on the WBS, "Уточненная. Не
получится у нас хорошей WBS даже через месяц дискавери - не факт, что ВА успеет все проработать с
клиентом, эстимации на работу с клодом тоже условные." ([[2026-10-13 OE Big4 chat - rendering 1]] 2026-10-13 09:18). Kavalchuk: "Я согласен,
что она у вас за месяц может не получиться, но управлять изменением срока и готовностью - вам." (09:25)

Budget, in the record: "В ходе Discovery PM, BA и DM регулярно делают переоценку и сообщают об изменениях
по четырём показателям: бюджет, скоуп, качество, ожидания клиента", and "По итогам Discovery —
уточнённый прогноз, включая границу возможного выхода за бюджет". Mikhail: "После дискавери будут
обновлены прогнозы по бюджету и срокам на основании фидбека от команды клиента и уровня ее
вовлеченности и кооперативности." (09:42)

Told to the client on 14 October: "as agreed between our teams, the Project begins with the Discovery
Phase (Milestone 1)", the discovery plan to cover "the Milestone 1 deliverables (Vision & Scope document,
solution architecture design, UI kit and main mockups, revised WBS and project plan)" ([[2026-10-14 Project email thread - rendering 1]]). Deciders
still not named (ingest session 2026-10-14).

## Rationale

We look prepared without pretending to know what we do not (Anton, 00:11:56), and the client is more
likely to engage with something to react to; Kavalchuk expects a contact who may push for results
rather than explain (00:12:43). Prototyping before the contact uses the waiting time.

## Consequences

- Downside: the BA's own picture can run ahead of the WBS lines, and what the client sees, the client
  will want ([[K-5 Scope grows through the prototypes]]).
- Downside: prototyping before the contact spends budget on guesses the client may overturn.
- New obligation: the plan has to produce every Milestone 1 deliverable the SOW lists - V&S document,
  Solution Architecture Design, UI Kit, main UI/UX mockups, communication plan, revised WBS - not only
  prototypes ([[COM-020 Milestone plan and deliverables]]; evaluated).
- New obligation: per-area tracking and the post-discovery call, owned by the PMs and Arseniy.
- Related: [[DEC-014 Staff on demand, seniors who work with Claude, fewer developers]],
  [[DEC-016 Send the SOW as it stands and start preparing without waiting for its signature]].
- New obligation (added 2026-10-14): the record says "По SOW мы уже взяли на себя обязательства по
  результатам Discovery в большем объёме, чем запланировали внутри. Подход к их выполнению определяют PM
  и DM." and gives Mikhail, Anton and Arseniy the approach to them ([[2025-11-25 Contract chat - rendering 5]] 2026-10-13 09:55;
  [[COM-020 Milestone plan and deliverables]]).
- New obligation: regular re-estimation and reporting on budget, scope, quality and client
  expectations, and after discovery a forecast with the bound of an overrun
  ([[K-5 Scope grows through the prototypes]], [[K-10 Fixed price with vague acceptance criteria]]).
