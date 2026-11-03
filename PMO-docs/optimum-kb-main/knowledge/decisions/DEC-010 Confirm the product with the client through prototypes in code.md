---
type: decision
id: DEC-010
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: delivery
deciders:
  - tbd
sources:
  - "[[2026-09-28 Optimum discuss next steps - transcript]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
  - "[[2026-09-28 Anton and Mikhail 1-1 - transcript]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-10-13 Optimum Three Caballeros call - transcript]]"
  - "[[2025-11-25 Contract chat - rendering 4]]"
  - "[[2026-10-13 OE Big4 chat - rendering 1]]"
  - "[[2025-11-25 Contract chat - rendering 5]]"
  - "[[2026-10-20 Introductory call - transcript]]"
valid_from: 2026-09-28
capabilities:
  - "[[CAP-011 Platform, environments and handover]]"
tags:
  - delivery
  - prototypes
  - staffing
---
# DEC-010 Confirm the product with the client through prototypes in code

## Context

The client's decision-makers are hard to reach remotely and do not speak English
([[COM-008 Client cooperation and dependencies]]), and the contract accepts each milestone in writing,
with no automatic acceptance ([[COM-002 Written acceptance of each deliverable]]). Anton, on the
danger: "как мы должны сделать всё без багов и с теми аксептансами, которые указаны, как мы вообще всё
это вдаём помесячно по мейлстоуну, у нас должна быть спека с описаниями такая, что её слупая
рассматривает два дня, она всё равно имеет только одно чтение. Потому что иначе мы, мне кажется,
жесточайших встрянем." ([[2026-09-28 Optimum discuss next steps - transcript]] 00:21:07)

Presale made a desktop and web prototype, shared with the client as a video only
([[2025-10-20 Presale chat - rendering 2]] 2025-11-19 10:30). Whether the client gave feedback is not
recorded; Arseniy: "Только Антон Снотов. Может, Леша Титов." (00:22:32).

## Options considered

1. A precise specification first, then build and accept against it (Anton, 00:21:07). Not taken:
   "Мы тут все равно встрянем. И я не верю, что у нас тут получилось бы со спеккой, даже если бы она
   была, что-то доказывать." (Mikhail, 00:21:33)
2. Designer mockups between the BA and the developers. Not taken: a BA who works with Claude, or the
   mobile team, removes "вот эту прокладку между BEA и дизайнером" (Mikhail, 00:30:27); "они делают
   прикачку для инженеров ... Мне кажется, они не будут очень-очень сильно заморачиваться по дизайну"
   (00:30:27).
3. Prototypes in code, by screens, shown and clicked through at demos until the client says it is what
   they need, then the final app built from them. The direction taken.

## Decision

Mikhail: "Мне кажется, единственный вариант вытащить этот проект, это делать такие вот прототипчики,
может, не один цельный, а по скринам как-то, им показывать на демо, прокликивать, когда они говорят,
Зашибись. Вы уже имеете то, что нам надо, ну тогда брать и уже по этим прототипам делать финальную
аппликацию." (00:23:25); "Мне хочется делать этот проект кодом." (00:28:25). Arseniy: "это make sense"
(00:24:21); "в целом мы можем без него запросто делать эти прототипы ... Мы все можем аишкой запросто
сделать" (00:29:40).

The designer, for the plan: "оставь там на дизайнера какие-нибудь часы, но не в первый месяц, а
где-нибудь там подальше, и что-нибудь такое, не знаю, символическое" (Mikhail, 00:31:03); "возможно,
через месяц посмотрим и решим, нет, дизайнер не нужен" (00:31:39); Arseniy: "Хорошо." (00:32:12).

Proposed in the call, not stated as decided by named people, so no deciders; draft until they are named.

Confirmed with the account manager on 13 October (added 2026-10-13; [[2026-10-13 Optimum Three Caballeros call - transcript]]): the prototypes are
Claude's HTML - "Нет, к черту фигму. Клодовские. HTML-ка" - one linked prototype or "10-15 HTML,
которые были прокликаны с клиентом", the feedback reflected, "и в конце было там аксептанс от клиента"
(Mikhail, 00:41:16); "разработчики будут подключаться только после того, как прототип показан,
прокликан, заопроводен" (00:14:13). Kavalchuk's summary of the output: "VBS выровненная плюс прототипы
каждой фичи VBS, грубо говоря, и плюс аксептанс от клиента" (00:42:03; "VBS" is the WBS). Mikhail: "Да,
но это программа максимум" (00:42:13), doubting it fits in a month. Kavalchuk asked whether a company
tool or Lovable would suit better; left to the team (00:44:29 to 00:48:04). The designer, 29 September:
"дизайнер потребуется на существенно меньшую аллокацию либо может не понадобиться вовсе"
([[2025-11-25 Contract chat - rendering 4]] 2026-09-29 15:51; [[DEC-014 Staff on demand, seniors who work with Claude, fewer developers]]).
How discovery uses the prototypes:
[[DEC-015 Discovery - our own picture of the system, questions as if from scratch]]. Deciders still not
named: tbd (Anton Oparienko, ingest session 2026-10-13).

The tool, from 13 October (added 2026-10-14): Kavalchuk's draft record had "BA, который работает с кодом
и Claude"; Mikhail: "Не надо с кодом. ВА должен работать с Claude Design для быстрой генерации
прототипов, сбора фидбека и получения акцептанса." ([[2026-10-13 OE Big4 chat - rendering 1]] 2026-10-13 09:18); Kavalchuk: "Согласен -
опечатка, про код" (09:25). The published record: "кликабельные прототипы (Claude Design)" ([[2025-11-25 Contract chat - rendering 5]]
2026-10-13 09:55). Acceptance in parts: "Прототип акцептить будем частями, необязательно ждать
акцептанса всех частей" (Mikhail, 09:18); the record: "Порядок acceptance прототипа (целиком или по
частям) и момент старта разработки определяют PM и DM." The BA starts before we meet the client: "ставим
задачу ему изучить контекст и начать придумывать систему и делать прототипы в Клоде. Чтобы когда мы
пойдем к клиенту общаться, то можно было уже показывать что-то кликающееся" (Mikhail, [[2025-11-25 Contract chat - rendering 5]] 2026-10-13
13:58). Our reading: "in code" in the title means prototypes Claude generates rather than designer
mockups; the BA need not code. A rename is the curator's call. Deciders still not named (ingest session
2026-10-14).

Presented to the client on 20 October (added 2026-10-30; [[2026-10-20 Introductory call - transcript]]):
Discovery "like 4 or 5 weeks", "probably 2 or 3 meetings a week with heavy emphasis on working through
the prototypes" (Anton, 00:28:59); "our plan is to utilize the prototyping heavily", clickable
prototypes shown, feedback, corrections, and at the end "the final prototypes, the UI kit available
from them, the, and the plan for the, our next milestone and overall like rough idea of the whole
project", "though we will have the text description"; "only after that we start the exact build and
writing the code" (00:33:17). Mr. Lawal: "Yeah, that sounds like a good plan to me." (00:36:41) - not
acceptance. He accepts the prototypes and requirements (00:37:16;
[[COM-008 Client cooperation and dependencies]]). Against [[COM-020 Milestone plan and deliverables]]
(evaluated): the Vision & Scope document and the solution architecture design, also Milestone 1
deliverables, were not named on the call. Deciders still not named (ingest session 2026-10-30).

## Rationale

With decision-makers who settle things in person and do not read English, a specification is unlikely
to settle a dispute; a working screen they have clicked through is closer to what they will accept
(Mikhail, 00:21:33, 00:23:25). The client is an engineering organisation building a tool for its
engineers and will not care much about design (00:30:27).

## Consequences

- Downside: rework is expected - "Делать, показывать, потом все переделывать, пока они не устроят"
  (Mikhail, 00:21:33).
- Downside: a click-through at a demo is not acceptance; the milestones are still accepted in writing
  ([[COM-002 Written acceptance of each deliverable]]).
- It runs against a line of the 7 September management call: "Разработку не начинаем, пока не закроем
  основные вопросы и не убедимся, что команда одинаково понимает scope - чтобы минимизировать переделки
  на FP." ([[DEC-009 Sign the client's final contract as it stands]]). Not settled here; for the
  deciders.
- New obligation: a BA who can build prototypes with AI, or the mobile team doing it
  ([[DEC-002 Senior engineers first]]); designer hours kept in the plan only as a token, reviewed after a
  month.
- Downside: such a BA may be hard to find. Mikhail, the same day: "Хочется, чтобы он, конечно, вообще
  был, там, и с клод-дизайн работал, и прототипчики лепил, и прочее-прочее, но... Не знаю, найдется ли
  такое." ([[2026-09-28 Anton and Mikhail 1-1 - transcript]] 00:00:00)
- The designer part is still to decide, because design is a contract deliverable (Anton Oparienko, in the
  seed-ingest session, 2026-09-28): Milestone 1 delivers a "UI Kit" and "Main UI/UX mockups mandatory
  and enough to start the project implementation", and the screens of Milestones 2 to 5 are each "built
  on the approved UI Kit" ([[2026-06-15 SOW v10.4 - rendering]], Milestone 1 deliverables, and the UI
  lines of Milestones 2 to 5; [[COM-020 Milestone plan and deliverables]]). Nobody in the call of
  28 September referred to these deliverables.
- Related: [[DEC-011 Move scope between milestones and start building in the first month]].
