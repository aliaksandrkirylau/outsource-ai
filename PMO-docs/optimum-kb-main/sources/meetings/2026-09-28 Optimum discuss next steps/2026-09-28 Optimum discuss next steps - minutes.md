---
type: source
kind: meeting-minutes
date: 2026-09-28
setting: internal
participants:
  - Mikhail Andrushkevich
  - Arseniy Klimenko
  - Anton Oparienko
transcript: "[[2026-09-28 Optimum discuss next steps - transcript]]"
recording: https://app.bluedothq.com/preview/6aba2d2818ccfef63d8c78ca
purpose: the delivery team's first working call after the kick-off sync - who to staff first, how discovery and the milestones will run, how to work with the client
procedure_version: d6eb286
---
# 2026-09-28 Optimum discuss next steps - minutes

Internal, no client present. 11:00 to 11:32 Warsaw time, called by Mikhail that morning; in Russian.
Transcript: [[2026-09-28 Optimum discuss next steps - transcript]] (Bluedot).

Two other records of the call, not used as sources:

- Gemini's notes (https://docs.google.com/document/d/1uJ-MhHhmQ6nnJ01Fm_AOMJZKgwJwTZmUDqWE-WxUZYw): its
  transcript renders the Russian speech as English fragments ("Foreign speech. Foreign speech",
  "bread."), and its summary is built on them. Link-only, not rendered.
- Mikhail's results in the [Core] Optimum engineering chat, 2026-09-28 09:46 UTC
  (https://chat.google.com/room/AAQAkfyHFwA/iZijtf5ahJQ/iZijtf5ahJQ), quoted in full under Actions.

Speech-recognition slips that matter: "BI", "BIA", "BIE", "BEA", "бей" are BA; "дем" is DM;
"тихлид", "техледоархитектор" are tech lead and architect; "Rise of Matrix", "Raytheon Matrix" are the
RACI matrix; "пенелька", "ПНЛ", "PNG" (00:09:29) are the P&L; "СolutionArchitectBuy" is the solution
architect line; "Клод" is Claude; "аишка" is AI; "мобила", "мобайл" is the mobile department. "Леша"
(00:02:14, 00:17:53) is most likely Alexey Gamanovich; "Леша Титов" (00:22:32) most likely Aliaksei
Tsitou of presale; "Паша Мальцюк" (00:15:40) most likely Pavel Martysuk; "Ваня" (00:04:37) is not
identified.

## Summary

Mikhail wanted to move the project on before he had taken in all its material. The contract: the client
refused further changes, the team agreed to sign, and Snotov, on leave, was to tell the client so on
site; no update from him since. Arseniy's role: DM and the final say on the technical side, possibly the
tech lead too. Staffing now: a BA and a tech lead or architect who can code; regular developers later.
Discovery is not a classical one, since the estimate can hardly change after it, so the team treats the
project as started. Mikhail proposed moving scope between milestones and coding from the first month,
and confirming the product with the client through prototypes in code rather than a specification;
the designer is kept only as token hours later. The client's decision-maker speaks only Arabic; who the
team will work with day to day is not known. Whether our people may sit outside the EU, in Belarus, was
never raised with the client.

## Decisions

Proposals, not yet decisions, unless marked:

- Confirm the product through prototypes in code: "Мне кажется, единственный вариант вытащить этот
  проект, это делать такие вот прототипчики, может, не один цельный, а по скринам как-то, им показывать
  на демо, прокликивать, когда они говорят, Зашибись. Вы уже имеете то, что нам надо, ну тогда брать и
  уже по этим прототипам делать финальную аппликацию" (Mikhail, 00:23:25); "Мне хочется делать этот
  проект кодом" (00:28:25). Arseniy: "это make sense" (00:24:21), and prototypes without a designer, with
  AI (00:29:40).
- No designer at the start (Mikhail, agreed by Arseniy - the one point settled for the plan): "Окей,
  тогда давайте дизайнера пока... Антон, будешь перенолику обдать, ты оставь там на дизайнера какие-нибудь
  часы, но не в первый месяц, а где-нибудь там подальше, и что-нибудь такое, не знаю, символическое. 10%
  в месяц, 16 часов, что-нибудь такое." (00:31:03); "возможно, через месяц посмотрим и решим, нет,
  дизайнер не нужен" (00:31:39); Arseniy: "Хорошо." (00:32:12).
- Move scope between milestones and start coding in month 1: "Я предлагаю посчитать за Assumption, что
  сколп между milestone'ами мы подвигать сможем ... полный discovery на полный сколп мы за один месяц все
  равно не сделаем. А какой-то сколп там из следующего milestone'а имеет смысл начинать делать в первый
  же месяц, закладывать в базу проекта. и начинать что-то уже кодировать." (Mikhail, 00:28:25). Not
  answered in the call.
- Treat the project as started: discovery "не классическое ... мы же там особо показания потом не можем
  поменять сильно после него в плане оценки" (Arseniy, 00:09:39); "Имеет смысл считать, что проект
  стартанул, и нам его делать при любом раскладе" (Mikhail, 00:09:54).

The first three run against a line of the 7 September management call, recorded in
[[DEC-009 Sign the client's final contract as it stands]]: "Разработку не начинаем, пока не закроем
основные вопросы и не убедимся, что команда одинаково понимает scope - чтобы минимизировать переделки на
FP." Nobody in this call referred to it. Not settled here.

## Agreements with the client

None - internal meeting.

## Internal agreements

- Roles, for now: Arseniy "технически валидационная" role - the tech lead himself or the final approver
  of the technical side, plus AI in delivery (00:05:25); Mikhail and Anton one PM role in the first RACI
  (00:06:45). The RACI is drawn once the tech lead is settled.
- First hires: "прямо сейчас нам BA, дизайнер, не знаю, архитекторов слэш техлит" (Mikhail, 00:09:06),
  the tech lead "кто сможет сам и код пописать" (00:07:44); regular developers "прям сейчас не надо"
  (00:08:49). The designer then moved to token hours (above). A tech lead from the mobile department is
  worth considering, since that department builds it (Arseniy, 00:10:29). The BA is not sought in the
  Emirates (Mikhail, 00:13:04).
- The P&L gets a staffing tab with the current picture, in the same P&L (00:26:47); the solution
  architect, planned there for the first month only, becomes a position that stays (Anton, 00:24:54).

## Actions

Mikhail's results in [Core], 2026-09-28 09:46 UTC, verbatim:

```text
По результатам сегодняшнего колла:
Я: разузнаю про доступность Снотова - на связи ли он, когда выходит из отпуска, когда встречается
Арсений: сделает требования к TL\AR
Антон: отразит текущий вижн в P&L

RACI - postponed
```

From the call, beyond those:

- Mikhail: set up a direct line to the salesperson on site (00:02:14).
- Anton: open the positions BA, architect or tech lead, and designer in a master document (Mikhail's
  ask, 00:24:28); Anton ties it to the P&L first (00:24:54).
- Anton: look further into the contract's milestone scope (00:28:16).
- Anton: show Arseniy the knowledge base (00:00:21).

No Jira keys yet; there is no board.

## Questions raised

- Where may our people be located - "только Евросоюз, или мы можем там прям честно показывать, что у нас
  люди в Беларуси?" (Mikhail, 00:13:20). "мы это никогда не поднимали ... у Снотова надо спросить"
  (Arseniy, 00:13:33).
- Who the team will work with at the client (Anton, 00:15:22). Arseniy, from hearsay: "ребята, с
  которыми мы будем уже работать, которые ответственны за реализацию с их стороны, они англоязычные ...
  и нам выделят конкретных людей. вот просто decision-maker. вот этот чел, который говорит только на
  арабском" (00:15:40).
- How the monthly milestones are set: agreed at the start of each month, or fixed (Anton, 00:26:55).
  Mikhail: "В контракте прописан скоп на каждый milestone, он довольно краткий, но high-level он есть"
  (00:27:37); Arseniy: the client is probably open to "свой вид распределения по мейлстоунам" (00:27:48).
- Was the presale prototype shown and is there feedback (Mikhail, 00:21:33). Arseniy does not know:
  "Только Антон Снотов. Может, Леша Титов." (00:22:32). The KB has part of it: a desktop and web
  prototype of 19 November 2025, shared with the client as a video only
  ([[2025-10-20 Presale chat - rendering 2]] 2025-11-19 10:30); feedback is not recorded.
- Why the WBS has the BA figure Mikhail read as a rate (00:11:35). Arseniy does not know; the presale BA,
  Marina Zaretskaya, has left (00:11:53). Our note, not checked: the v1 WBS columns headed "Rate,
  USD/hour" hold hours ([[2026-09-25 v1 WBS - overview]]; seed findings 33), so the figure may be hours.
- A contract risk, Anton's reading: "мы можем типа не заделерить это никогда по текущим условиям
  контракта и работать типа очень долго, бесплатно" (00:16:40). For the PMO risk register (not filed
  yet); the same risk is in the 7 September list (DEC-009).

## New scope mentioned

None.

## Proposed changes

One table for the call. Source keys: T = [[2026-09-28 Optimum discuss next steps - transcript]];
C2 = [[2025-10-20 Presale chat - rendering 2]].

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | new | DEC-010 Confirm the product with the client through prototypes in code | Delivery. Prototypes in code, by screens, shown and clicked through at demos until the client says it is what they need, then the final app built from them; made by a BA who works with Claude or by the mobile team, with AI; no designer at the start, token hours later, dropped if not needed after a month. Lost: a precise specification first (Anton, 00:21:07; Mikhail: "я не верю, что у нас тут получилось бы со спеккой, даже если бы она была, что-то доказывать"), designer mockups between BA and developers (00:30:27). Context: the presale prototype (C2 2025-11-19). Consequences: rework is expected ("Делать, показывать, потом все переделывать, пока они не устроят", 00:21:33); a demo is not acceptance (COM-002); it runs against DEC-009's "минимизировать переделки на FP". Draft, deciders not named | extracted | - | T 00:21:07 to 00:31:39; C2 | applied 2026-09-28 |
| 2 | new | DEC-011 Move scope between milestones and start building in the first month | Delivery. Mikhail's proposal to take as an assumption that scope moves between milestones, and to start next-milestone scope and coding in month 1, because full discovery of the full scope does not fit one month; discovery is "не классическое". Lost: Milestone 1 as pure discovery, as the SOW has it (COM-020). Consequences: the milestone scope is in the contract, so the client has to agree the new split (Arseniy thinks it would); it runs against DEC-009's "Разработку не начинаем, пока не закроем основные вопросы". Draft, a proposal, deciders not named | extracted | - | T 00:09:39, 00:09:54, 00:27:37 to 00:28:25 | applied 2026-09-28 |
| 3 | update | COM-020 Milestone plan and deliverables | The team's reading (28 Sep): the contract's scope per milestone is "довольно краткий, но high-level"; how strictly to follow it is open; the client may accept our own split; Milestone 1 "описывает чистый discovery". Link DEC-011 | extracted | - | T 00:26:55 to 00:28:25 | applied 2026-09-28 |
| 4 | update | DEC-002 Senior engineers first | Which roles first (28 Sep): BA and a tech lead or architect who can code; regular developers later; the designer to token hours (DEC-010); a tech lead from the mobile department considered; Arseniy's own role; the solution architect becomes a position that stays; the BA not sought in the Emirates | extracted | - | T 00:05:25 to 00:13:04, 00:24:54 | applied 2026-09-28 |
| 5 | update | COM-008 Client cooperation and dependencies | The contract has the client "nominate authorized contacts" (5.1); who they are is not known (Anton's question). As Arseniy heard: the client's people responsible for implementation speak English and specific people will be assigned; the decision-maker speaks only Arabic; the presale call ran through an interpreter. Mikhail: questions will need the decision-makers ("без них никуда") | extracted (Arseniy's is hearsay, marked) | - | T 00:14:17, 00:15:22 to 00:18:47 | applied 2026-09-28 |
| 6 | new | QUE-009 Where may our team members be located | "только Евросоюз, или ... люди в Беларуси?" Never raised with the client. No stored source answers it: the contract's subcontractor approval (COM-010) and the Saudi cross-border rules (COM-015) do not say where people sit (evaluated). asks: Sales (Snotov) first, then the client. Blocks: the first hires (DEC-002) | extracted; evaluated (no source answers) | - | T 00:13:20, 00:13:33 | applied 2026-09-28 |
| 7 | update | DEC-009 Sign the client's final contract as it stands | Restated 28 Sep ("или подписывайте ее, или все ... И мы сказали, будем подписывать"). Anton's reading of acceptance, the same risk as the 7 Sep list's "потенциальная бесконечная приемка без оплаты"; Arseniy on taking it on: "меня спросили, готов ли я поставить свою пятую точку. Я сказал, что готов". The 28 Sep proposals (DEC-010, DEC-011) run against point 6 | extracted | - | T 00:03:10, 00:16:40, 00:17:01 | applied 2026-09-28 |
| 8 | no material | QUE-007 What is the Effective Date | The signing steps Mikhail mentions ("через какие-то платы проводить, заверять") are already recorded there | - | - | T 00:02:14 | recorded 2026-09-28, no note |
| 9 | no material | QUE-001 Why a desktop at the rig, and tablets later | Its route "through Snotov while he is on site": Snotov is on leave, "Сейчас он не работает официально"; a person's availability is state, not a note change (rule 6) | - | - | T 00:04:22 | recorded 2026-09-28, no note |
