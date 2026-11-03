---
type: source
kind: chat
date: 2026-10-13
original: https://mail.google.com/chat/u/0/#chat/space/AAQAMr_El5o
received_from: Google Chat group chat "OE Big4" (spaces/AAQAMr_El5o); read by Anton Oparienko's copilot on 2026-10-14
purpose: how the record of the 13 October call was corrected before it was published, and how the four leads prepared the first contact with the client (Anton's ask, 2026-10-14, "other chats too like oe big4")
supersedes:
procedure_version: 5d00575
---
# 2026-10-13 OE Big4 chat - overview

kind: chat, one part, rendered by `pm/seed-ingest-scripts/chat2md.mjs` from the Chat tool's output:
[[2026-10-13 OE Big4 chat - rendering 1]], 53 messages from 2026-10-13 09:05 to 2026-10-14 12:31 UTC.
The chat is still in use: the next ingest starts a part 2 after 2026-10-14 12:31.

This overview also carries the extraction and the proposed changes for three sources ingested with it:
[[2025-11-25 Contract chat - rendering 5]] (2026-10-13 09:55 to 2026-10-14 12:47),
[[2026-09-25 Core chat - rendering 1]] (2026-09-25 to 2026-10-14) and
[[2026-10-14 Project email thread - rendering 1]] (14 October).

## What it is

A private chat Mikhail Andrushkevich opened on 13 October for four people: "Чат на нас четверых, чтобы
почаще синкаться в приватной обстановке" - Mikhail, Aliaksandr Kavalchuk (the account manager), Anton
Oparienko and Arseniy Klimenko. In it Kavalchuk drafted the record of that morning's call
([[2026-10-13 Optimum Three Caballeros call - minutes]]), Mikhail corrected it, and the published version
went to the contract chat at 09:55 ([[2025-11-25 Contract chat - rendering 5]]). On 14 October the client
named a contact, and the four agreed who goes into the letters and drafted them.

## How far to trust it

Internal, our own view (`sources/internal/`). The draft record of 09:06 is not the agreed one: where
the draft and the published version (contract chat, 09:55) differ, the published one stands, and
Mikhail's corrections explain why. Kavalchuk's letter of 11:33 is a draft; what was sent is not stored.

## Not for

Client contact details (removed). Not for quoting the draft record as what was agreed.

## Removed at ingest

- The client contact's e-mail address and phone number (2026-10-14 08:25) and his profile link (08:21);
  a colleague's GitHub username (2026-10-13 12:44).
- A remark about a colleague's working arrangements (2026-10-13 09:20), in two places, marked in place.
  Kept: that she cannot join the project. Anton can ask for this to change.
- Reactions; blank lines inside messages. Left out: nothing (no bot, system or empty messages).
- Not stored: the screenshot of 2026-10-13 11:01, a KB answer about the client's stakeholders.

Kept, and put to Anton as remarks about colleagues that carry project content: Kavalchuk on who should
approve on our side, "по логике такое должен @Arseniy Klimenko апрувить и делать, но пока вижу что
@Mikhail Andrushkevich больше вовлечён" (2026-10-13 09:52), and on how many of us face the client, "не
понимаю необходимости остальных" (2026-10-14 11:42). "[PM name]" in the draft letter of 11:33 is the
author's own placeholder.

## Summary

13 October. Kavalchuk drafted the call's record. Mikhail corrected it: let the missing Annex 2 slide
rather than raise it with the client, taking responsibility for that; discovery results as a programme
maximum, with a minimum of acceptance of the next phase's deliverables in a month; a refined, not a
reconciled, WBS; the prototype accepted in parts; a BA who works with Claude Design, not code; refined
forecasts after discovery, not a full picture. Kavalchuk kept the points as tasks and responsibilities
for the PMs and the DM, fixed the BA line, and published the record. Anton raised the advance; Kavalchuk
took it. Mikhail proposed a RACI for the four. Marina Zaretskaya cannot join. Kavalchuk got access to the
KB; the sensitive material sits in Mikhail's separate repository while Anton tries a folder inside the
main one.

14 October. The client named Ishaq Lawal, its General Manager, as the contact and asked for payment.
Mikhail named Anton the main PM; Mikhail and Arseniy are introduced at the kick-off. Kavalchuk sent a
reply in the client's "Contract Review" thread (the advance invoice and bank details to follow from
Lizaveta), then opened a new thread introducing Anton and asking for a kick-off slot the following week
([[2026-10-14 Project email thread - rendering 1]]). Before the call: a timeline, a plan artifact, the
questions, and a rehearsal. Whether we can start without the signed SOW is to be asked of the contact;
if not, Kavalchuk goes back to the CEO.

## Decisions

Proposals and agreements; deciders as the sources name them.

- The published record of the 13 October call (Kavalchuk, contract chat 2026-10-13 09:55): "Текущую
  версию SOW не меняем и высылаем как есть"; discovery "Гибридный формат"; "Целевые результаты
  Discovery: 1) уточнённая WBS; 2) кликабельные прототипы (Claude Design); 3) acceptance клиента"; "Если
  Discovery не уложится в месяц, управление сроками и готовностью результатов — на PM и DM"; "Порядок
  acceptance прототипа (целиком или по частям) и момент старта разработки определяют PM и DM";
  "Ключевая роль на старте — BA, который работает с Claude Design"; the BA may start on the project
  budget "с заранее определёнными часами и результатами"; regular re-estimation "по четырём
  показателям: бюджет, скоуп, качество, ожидания клиента". Acknowledged with three thumbs; deciders
  not named.
- Annex 2 (Mikhail, 2026-10-13 09:18, 09:42): "Есть предложение спустить этот момент на тормозах";
  "Если за принятое решение, то оно уже есть - спускать на тормозах, не привлекать внимание клиента
  ... Ответственность на мне." The published record: "урегулирование вопроса в ходе Discovery".
- Programme minimum and maximum (Mikhail, 09:18): "Коммитаться на такое не можем, это
  программа-максимум ... Программа-минимум - акцептанс на деливераблс для следующей фазы (1 месяц)."
- The BA's tool (Mikhail, 09:18): "Не надо с кодом. ВА должен работать с Claude Design для быстрой
  генерации прототипов, сбора фидбека и получения акцептанса." Kavalchuk: "Согласен - опечатка, про
  код" (09:25).
- Who faces the client (2026-10-14 11:39): "В письмо ставим контакты Антона, меня с Арсением введем на
  кикоффе" (Mikhail); Kavalchuk sent on Mikhail's approval (11:58).

## Agreements with the client

None. Our letter of 14 October states our side's position; the client has not answered
([[2026-10-14 Project email thread - overview]]).

## Internal agreements

- The kick-off: "в идеале нам на кикофф надо идти с ВА, но мы пока не знаем когда мы его найдем.
  Предлагаю оставить это за скобками данного письма и потом уже в переписке с Антоном уведомить
  клиента, что мы начали стаффинг команды и дадим знать когда будем готовы стартовать дискавери"
  (Mikhail, 2026-10-14 11:39); Kavalchuk's plan: a separate thread, then a call the PM organises on what
  is happening, what is unclear, the next step and when (11:42).
- A RACI for the four (Mikhail, 2026-10-13 09:53; "делайте", Kavalchuk). Draft in `pm/`.

## Actions

From the published record (contract chat 2026-10-13 09:55) unless noted:

- Mikhail, Anton, Arseniy: keep the project's risk register; settle the Annex 2 point during discovery;
  a discovery plan and timeline as an artifact for the client; the approach to the SOW's discovery
  commitments; specialists on demand, for example for the SAD; regular re-estimation and reporting,
  with the BA once there, and after discovery a forecast with the bound of an overrun.
- Mikhail: start the BA search, "ориентир 1–2 недели". Anton: open the position with Mikhail's
  requirements (contract chat 2026-10-13 14:00, 14:03).
- Kavalchuk: the letter asking for a responsible person - sent 2026-10-13 12:57. The payment: "Пеймент
  - разберусь - сделаю" (2026-10-13 09:51).
- Lizaveta Shauchenka: the advance invoice and bank details in the "Contract Review" thread (the draft,
  2026-10-14 11:33).
- Anton: the kick-off invitation once the client gives slots ([[2026-10-14 Project email thread - rendering 1]]);
  a timeline, the plan artifact and the questions; a joint rehearsal before the call (Kavalchuk,
  2026-10-14 12:31).
- Kavalchuk: ask the contact whether we can start without the signed SOW; if not, back to Jaber
  (2026-10-14 12:31; contract chat 2026-10-14 12:47).
- Anton: an introduction to the KB for Kavalchuk; a proposal for the sensitive material (2026-10-13
  12:53, 13:18).

No Jira keys yet; there is no board.

## Questions raised

- Can the work start before the SOW is signed? To the client's contact at the kick-off.
- How far does the named contact decide? "насколько это контактное лицо будет что-то решать"
  (Kavalchuk, 2026-10-14 08:32). Asked in the letter.
- Who approves on our side? To the RACI (2026-10-13 09:52, 09:53).
- When is the actual start? Gamanovich asked; Kavalchuk: it depends on us (contract chat 2026-10-13
  13:30, 13:50).

## New scope mentioned

None.

## Proposed changes

Source keys: B4 = [[2026-10-13 OE Big4 chat - rendering 1]]; CC5 = [[2025-11-25 Contract chat - rendering 5]];
CO = [[2026-09-25 Core chat - rendering 1]]; EM = [[2026-10-14 Project email thread - rendering 1]];
CC4 = [[2025-11-25 Contract chat - rendering 4]]. Date and UTC time of the message.

New Decisions continue from DEC-017, new risks from K-10.

Approved by Anton Oparienko on 2026-10-14: all rows but 3. Row 3, DEC-017, is skipped for now: the two
positions on Annex 2 go into QUE-006 as facts, and rows 4 and 17 point there instead of to DEC-017.
Row 4 also carries Anton's statement that, as far as he knows, the SOW was sent as a document for
review - to be checked. No deciders named: DEC-010, DEC-013, DEC-015 and DEC-016 stay tbd. Anton on
row 18: the RACI is a draft; how documents we generate (the RACI, the discovery plan) are treated as
sources is a separate topic. The e-mail stays in `sources/client/`.

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | update | DEC-015 Discovery - our own picture of the system, questions as if from scratch | The published record of 13 Oct: target results "1) уточнённая WBS; 2) кликабельные прототипы (Claude Design); 3) acceptance клиента"; "Если Discovery не уложится в месяц, управление сроками и готовностью результатов — на PM и DM"; the order of prototype acceptance and the start of development are the PM and DM's; "По SOW мы уже взяли на себя обязательства по результатам Discovery в большем объёме, чем запланировали внутри" (an action: the approach to them). What Mikhail changed in the draft: "выверенная WBS" to "Уточненная. Не получится у нас хорошей WBS даже через месяц дискавери"; prototypes per feature and acceptance per module "Коммитаться на такое не можем, это программа-максимум ... Программа-минимум - акцептанс на деливераблс для следующей фазы (1 месяц)". Budget control: PM, BA and DM re-estimate and report changes in budget, scope, quality and client expectations; after discovery "уточнённый прогноз, включая границу возможного выхода за бюджет" (Mikhail: forecasts updated "на основании фидбека от команды клиента и уровня ее вовлеченности и кооперативности"). Told to the client on 14 Oct: discovery is Milestone 1, its deliverables named. Deciders still tbd - name them | extracted | - | CC5 2026-10-13 09:55; B4 2026-10-13 09:06, 09:18, 09:25, 09:42, 09:45; EM | applied 2026-10-14 |
| 2 | update | DEC-010 Confirm the product with the client through prototypes in code | The tool: "Не надо с кодом. ВА должен работать с Claude Design для быстрой генерации прототипов, сбора фидбека и получения акцептанса" (Mikhail, correcting "BA, который работает с кодом и Claude"); the record: "кликабельные прототипы (Claude Design)". "Прототип акцептить будем частями, необязательно ждать акцептанса всех частей"; the order and the start of development are the PM and DM's. The BA studies the context and prototypes before we go to the client, "Чтобы когда мы пойдем к клиенту общаться, то можно было уже показывать что-то кликающееся" (Mikhail). The title's "in code" no longer names the tool, and the BA need not code: a rename is the curator's call. Deciders still tbd | extracted | - | B4 2026-10-13 09:18, 09:25; CC5 2026-10-13 09:55, 13:58 | applied 2026-10-14 |
| 3 | new | DEC-017 Do not raise the missing Financial Plan annex with the client | Business. Context: the Agreement names Annex 2 "Approved Financial Plan and Milestones" and pays only to the account identified in "the approved Financial Plan" (7.11); the plan's content sits in Article 7 and the SOW (QUE-006, K-8). Options: (1) settle the wording in one of the first letters to the client's responsible person (Kavalchuk, 12 Oct, "предложение"); (2) leave it and draw no attention: "Есть предложение спустить этот момент на тормозах. В какой-то редакции фин план предполагал план по часам для каждой роли. Этого хотелось бы избежать." - the internal plan had 4 developers for 6 months against a hope of 1-2 with Claude, "но возможно дольше 6 месяцев. Объяснить клиенту на старте, что мы закладываемся на задержки сложно" (Mikhail). Chosen, per Mikhail: (2), "Если за принятое решение, то оно уже есть - спускать на тормозах, не привлекать внимание клиента ... Ответственность на мне." The published record words it as "урегулирование вопроса в ходе Discovery" on the three PMs; Kavalchuk: "Ответственность, что ПМ/ДМ это контролируют". Anton: the plan is in effect monthly, the SOW adds delivery by milestone; raise the advance when the SOW goes. Consequences: K-8 stays open; if the client asks for the plan, no answer is prepared (evaluated); DEC-016's Annex 2 line no longer holds (row 4). Deciders: Mikhail names himself - confirm | extracted | - | B4 2026-10-13 09:18, 09:25, 09:42, 09:45, 09:50; CC5 2026-10-13 09:55; CC4 2026-10-12 13:00 | rejected 2026-10-14 (skipped for now, Anton; the facts are in QUE-006) |
| 4 | update | DEC-016 Send the SOW as it stands and start preparing without waiting for its signature | Recorded on 13 Oct: "Текущую версию SOW не меняем и высылаем как есть. Риск расхождения между обещаниями в SOW и фактической работой выравнивают PM и DM по ходу проекта". The letter asking for a responsible person went on 13 Oct; whether the SOW went with it is not stated. 14 Oct: the SOW is still unsigned, and whether we can start without it goes to the client's contact at the kick-off - "можем ли мы это решить на нашем уровне или же нужно будет вернуться на уровень Джабера" (Kavalchuk). No longer holds: "the Annex 2 wording settled in one of the first letters" - DEC-017. The advance: the client asked for payment on 14 Oct; the invoice and bank details go from Lizaveta (K-8). Deciders still tbd | extracted | - | CC5 2026-10-13 09:55, 12:57, 2026-10-14 12:47; B4 2026-10-14 08:25, 11:33, 12:31 | applied 2026-10-14 |
| 5 | update | QUE-006 Which SOW and which plan are Annex 1 and Annex 2 | Since 13 Oct: Annex 2 is not to be raised with the client (DEC-017). Anton: "фин план в целом есть помесячный в совновном, в СоВ уточнение что мы пы майлстоунам собираемся деливерить". The SOW is still unsigned on 14 Oct; starting without it goes to the client's contact (row 4). Stays proposed | extracted | - | B4 2026-10-13 09:18, 09:42, 09:50; CC5 2026-10-14 12:47 | applied 2026-10-14 |
| 6 | update | QUE-007 What is the Effective Date | Asked by Alexey Gamanovich, 13 Oct; Kavalchuk: "официальный старт будет как только будет лицо со стороны клиента и наша готовность начинать. Я дату пока не называю клиенту". 14 Oct: the start depends on our readiness and the SOW. In writing to the client, 14 Oct: "Following the kick-off call and alignment on these points, we will be ready to officially start the work on the Project." Not answered by the client. Mikhail: tell the client later that staffing has started and when we are ready to start discovery. Stays proposed | extracted | - | CC5 2026-10-13 13:30, 13:50, 2026-10-14 12:47; EM; B4 2026-10-14 11:39 | applied 2026-10-14 |
| 7 | update | K-3 The six months run from the client's signature, before discovery starts | Response so far: we told the client in writing that the official start follows the kick-off and the alignment, asked for slots the following week - "Специально просил на след неделе чтобы выиграть вам чуть времени" (Kavalchuk) - and named no date. The client has not answered | extracted | - | EM; B4 2026-10-14 12:31; CC5 2026-10-13 13:50 | applied 2026-10-14 |
| 8 | update | COM-008 Client cooperation and dependencies | The client named a project contact on 14 Oct: Ishaq Lawal, General Manager - "пока получил это лицо как контакт"; "возможно будет ещё кто-то" (Kavalchuk). Our letter asks for kick-off slots, who on the client's side "will review and approve final decisions on the Project scope and the Milestone deliverables" ("We would be glad if this could be you"), and other business stakeholders; it names Anton our PM and "main point of contact for day-to-day project coordination". Kavalchuk: the letter is to find out how far the contact decides, "может этот человек условно чуть выше, и будет кто-то ещё ниже". Stays disputed | extracted | - | B4 2026-10-14 08:21, 08:32; CC5 2026-10-14 12:47; EM | applied 2026-10-14 |
| 9 | update | K-4 No client contact with authority, or a slow one | No longer holds: "the client has named no project contact" - named 14 Oct (row 8); whether he can answer and approve is open. The 13 Oct record lists the risk, "Возможная низкая вовлечённость или медленные ответы со стороны клиента", with "запрос назначенного ответственного со стороны клиента (п. 1); BA может начать прототипирование до получения контакта (п. 4). → Ковальчук (контакт), Андрушкевич (BA)". Owner and score still for a PM | extracted | - | CC5 2026-10-13 09:55, 2026-10-14 12:47; B4 2026-10-14 08:21, 08:32 | applied 2026-10-14 |
| 10 | update | K-5 Scope grows through the prototypes | The 13 Oct record lists it, "Риск расширения скоупа через прототипы", with "регулярная переоценка и отчётность по бюджету, скоупу, качеству и ожиданиям клиента (п. 5). → Андрушкевич, Опариенко, Клименко (+ BA)", under the heading "Высокий риск выхода за бюджет". Owner and score still for a PM | extracted | - | CC5 2026-10-13 09:55 | applied 2026-10-14 |
| 11 | new | K-10 Fixed price with vague acceptance criteria | Internal. The first of the record's three risks: "Fixed price при размытых критериях приёмки"; "контрактные риски приняты менеджментом ранее". Cause: a fixed price and the SOW's high-level acceptance criteria; written acceptance, the clock restarting after each fix, no deemed acceptance (COM-002). Event: the client withholds acceptance and asks for rework of what was built to the line. Effect: rework beyond the estimate, and monthly payments held, each due only on verified completion (COM-012). Not K-5, which is new scope through prototypes. Response in the record: "прототипы и acceptance клиента до старта разработки соответствующих частей (п. 3), реестр рисков (п. 2.1). → Андрушкевич, Опариенко, Клименко." Draft, not scored | extracted | - | CC5 2026-10-13 09:55; B4 2026-10-13 09:06 | applied 2026-10-14 |
| 12 | update | K-6 No suitable BA in time | The search started 13 Oct, "ориентир 1–2 недели", on Mikhail. Mikhail asked Anton to open the position: a senior BA "with Product Mindset" who proposes and validates solutions "with minimal client involvement"; Anton's version of 14 Oct adds full time at the start, location any, working hours overlapping Saudi Arabia (UTC+3) Monday to Thursday, fluent English. Marina Zaretskaya, raised as a candidate: "К нам на проект зайти не сможет" (Mikhail). "в идеале нам на кикофф надо идти с ВА, но мы пока не знаем когда мы его найдем" - the kick-off may come before the BA | extracted | - | CC5 2026-10-13 09:55, 13:58, 14:00, 14:03; CO 2026-10-14 08:35; B4 2026-10-13 09:20, 2026-10-14 11:39 | applied 2026-10-14 |
| 13 | update | DEC-014 Staff on demand, seniors who work with Claude, fewer developers | From the 13 Oct record: "Ключевая роль на старте — BA, который работает с Claude Design" (Mikhail struck "с кодом"); "привлечение других специалистов on demand по необходимости (например, для подготовки SAD)" on Mikhail, Arseniy and Anton - the Solution Architecture Design being a Milestone 1 deliverable (COM-020). The BA: "full-time at the start of the project, fewer hours later in development" (Anton). Consistent with the decision; deciders unchanged | extracted | - | CC5 2026-10-13 09:55; B4 2026-10-13 09:18; CO 2026-10-14 08:35 | applied 2026-10-14 |
| 14 | update | DEC-013 Where the PMs keep sensitive working material | In use: a separate repository for sensitive data that Mikhail runs; he invited Kavalchuk to it (option 3). Anton: "возможно это все еще отдельный репо будет, но папкой внутри основного с игнором. Я досмотрю, поэкспереминтирую и предложу" (option 1 still being tried). Kavalchuk asked whether "подход Sensetive General" is kept; Anton: "Сам подход есть, фолдеров этих еще небыло". Not decided; deciders tbd | extracted | - | B4 2026-10-13 09:58, 10:54, 12:51, 12:53, 13:18 | applied 2026-10-14 |
| 15 | update | COM-020 Milestone plan and deliverables | Told to the client on 14 Oct: "the Project begins with the Discovery Phase (Milestone 1)", with "the Milestone 1 deliverables (Vision & Scope document, solution architecture design, UI kit and main mockups, revised WBS and project plan)". Evaluated: the letter's list leaves out the communication plan, which the SOW names among them. Internally, 13 Oct: "По SOW мы уже взяли на себя обязательства по результатам Discovery в большем объёме, чем запланировали внутри"; Mikhail's minimum for the month: "акцептанс на деливераблс для следующей фазы" | extracted | - | EM; CC5 2026-10-13 09:55; B4 2026-10-13 09:18 | applied 2026-10-14 |
| 16 | update | QUE-009 Where may our team members be located | Not an answer: the BA position of 14 Oct says "Location: any." - our working assumption while the question is open; if the client restricts where people sit, that hire may not fit. Stays proposed | extracted | - | CO 2026-10-14 08:35 | applied 2026-10-14 |
| 17 | update | K-8 Payments held for want of an approved Financial Plan | 14 Oct: "Так же они сделали запрос на оплату" (Kavalchuk) - the client asked for payment; the advance invoice and bank details go from Lizaveta in the client's "Contract Review" thread (the draft). Kavalchuk took the payment on 13 Oct: "Пеймент - разберусь - сделаю". The Financial Plan is not to be raised (DEC-017). To watch: whether the invoice is paid without an approved plan | extracted | - | B4 2026-10-13 09:50, 09:51, 2026-10-14 08:25, 11:33 | applied 2026-10-14 |
| 18 | no material | Roles on our side | Anton is the main PM and the client's day-to-day contact ("Антон - основной ПМ", Mikhail; the letter); Mikhail and Arseniy introduced at the kick-off; Kavalchuk steps back from day-to-day work and would keep one, at most two of us facing the client; who approves on our side goes to the RACI ("RACI в процессе", draft in `pm/`). Roles belong in the stakeholder register and the RACI | - | - | B4 2026-10-13 09:52, 09:53, 2026-10-14 08:25 to 08:30, 11:39 to 11:45; EM | recorded 2026-10-14, no note |
| 19 | no material | The kick-off preparation | The invitation once the client gives slots; a timeline, a plan artifact, the questions; "До звонка обязательно репитиция совместная нам". Actions above | - | - | B4 2026-10-14 12:31; EM | recorded 2026-10-14, no note |
| 20 | no material | The client's people | Kavalchuk's list of 13 Oct is the one COM-008 already holds | - | - | B4 2026-10-13 10:00 | recorded 2026-10-14, no note |
| 21 | no material | KB access for the account manager | Kavalchuk invited to the KB repository; an introduction to follow. Process, not project knowledge | - | - | B4 2026-10-13 10:54 to 13:19 | recorded 2026-10-14, no note |
| 22 | no material | The BA position's wording | The staffing text, kept in `pm/`; the facts it carries are in rows 12, 13 and 16 | - | - | CC5 2026-10-13 14:00; CO 2026-10-14 08:35 | recorded 2026-10-14, no note |
| 23 | no material | [Core], 25 Sep to 12 Oct | Working links; the 28 Sep call's actions (that call is ingested); Anton's contract and SOW list (generated from the KB); the KB methodology; Arseniy's diagrams (stored); the conflict news (K-9 holds it); agendas and cancelled syncs; the SOW translation nearly done (13 Oct minutes row 19) | - | - | CO 2026-09-25 11:53 to 2026-10-12 09:00 | recorded 2026-10-14, no note |
| 24 | no material | The P&L thread of 29 Sep | How money reaches the departments under fixed price and tranches, the floating rate, a hold on staffing while the account manager says so (since replaced by DEC-014 and DEC-015). P&L and staffing process; the rate figure removed | - | - | CO 2026-09-29 09:23 to 10:26 | recorded 2026-10-14, no note |
