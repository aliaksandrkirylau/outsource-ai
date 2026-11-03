---
type: source
kind: meeting-minutes
date: 2026-10-13
setting: internal
participants:
  - Mikhail Andrushkevich
  - Aliaksandr Kavalchuk
  - Anton Oparienko
  - Arseniy Klimenko
transcript: "[[2026-10-13 Optimum Three Caballeros call - transcript]]"
recording: https://app.bluedothq.com/preview/6acdd74d9ea75bad0930246f
purpose: how to start the project now that the client has signed the Agreement - the SOW, the six months, the discovery approach, the BA, budget control
procedure_version: 5d00575
---
# 2026-10-13 Optimum Three Caballeros call - minutes

Internal, no client present. "Optimum E.: Three Caballeros call", 07:01 to 07:58 UTC (09:01 to 09:58
Warsaw time); in Russian. Transcript: [[2026-10-13 Optimum Three Caballeros call - transcript]]
(Bluedot, in Russian, the call's language). Called by Mikhail after Kavalchuk's messages of 12 October
in the contract chat ([[2025-11-25 Contract chat - rendering 4]] 2026-10-12 10:07 to 13:04).

One table of proposed changes below covers three sources ingested together: this call, the call of
12 October ([[2026-10-12 Optimum Three Caballeros call - minutes]]) and part 4 of the contract chat
([[2025-11-25 Contract chat - rendering 4]], 2026-09-28 12:52 to 2026-10-12 14:05 UTC).

Not used as a source: Bluedot's own summary, which carries contract figures. Kavalchuk's written
summary of this call and Mikhail's corrections to it, posted in the four-person "OE Big4" chat
(spaces/AAQAMr_El5o, 2026-10-13 09:06 and 09:18 UTC), are not stored; Anton can ask for them to be.

Removed from the transcript and marked in place: contract and budget figures in three turns, and the
part of the closing exchange about a colleague's employment status and past roles (00:53:28 to
00:56:09). Kept: that she was raised as a candidate and that Arseniy is to find out whether she is
available. Anton can ask for either to change.

Speaker labels match the transcript: Mikhail opens by addressing Aliaksandr, Kavalchuk addresses
Anton ("Антон?", 00:11:51) and Arseniy ("Арсений, а у тебя такой опыт есть?", 00:15:24), and each
answers. Doubtful turn edges: "Да, Миша?" labelled Arseniy at 00:23:46 is most likely Kavalchuk's;
"Мне" ending Mikhail's turn at 00:14:13 starts Kavalchuk's at 00:15:24; "бизнес-аналитика," opening
Kavalchuk's turn at 00:41:03 most likely ends Mikhail's sentence at 00:41:00.

Speech-recognition slips that matter: "код", "плод", "клад", "кода" are Claude ("дружить с кодом"
00:14:13, "это плод" 00:16:21, "с активным использованием кода" 00:36:03, "человек с кодом" 00:48:04);
"VBS", "ВБС", "VPS" are the WBS; "соф", "сол", "SOF", "SOA", "SOV", "сов" are the SOW, and "SIS" (00:22:39)
is "as is"; "рабы" (00:42:13) is "арабы"; "Novice" (00:25:46) is Innowise; "Думанович" and "Гоманович"
are Gamanovich; "Женя Преченко" and "Женя Краснов" are Yauheni Krasner; "Шатуха" is Shatuho; "Джобера"
is Jaber; "ReStream" (00:34:21) is a re-estimate; "яичных" (00:17:24) is "AI-шных"; "PNL", "pnl-ку" are
the P&L; "лавэбл" is Lovable. Not identified: "ГДО" (00:36:55), "на ВАЗе" (00:19:40), "E-PASS"
(00:44:29), Kavalchuk's example of a local sign-in service.

## Summary

The client has signed the Agreement, the SOW is not signed, and nobody can say whether the six months
have started. The team, who all joined after the estimate, finds the WBS too high-level to plan from.
Mikhail put two ways to start: go to the client with open questions, or design the system ourselves,
prototype it and then show it. Anton proposed a hybrid - come with our picture of the modules from the
WBS, but ask as if from scratch - and Kavalchuk backed a middle way. Kavalchuk will send the SOW as it
stands and ask the client for a responsible person, without naming a start date. Mikhail starts the BA
search: a BA who builds prototypes in Claude, gets them confirmed by the client, and only then hands an
area to development. If the BA comes before the client's contact, the BA starts prototyping on the
project budget, with hours and deliverables agreed up front. Kavalchuk asked for a discovery plan and
timeline as an artifact he can give the client's contact. Budget and scope are re-estimated through
discovery, with an internal call after it on who carries an overrun.

## Decisions

Proposals and agreements; none recorded with named deciders.

- Send the SOW as it stands: "сов, нет смысла сейчас тормозить, надо высылать, как есть" (Kavalchuk,
  00:31:29); "Соф, который мы подписали, ну, судя по всему, я его тоже засылаю" (00:29:33). Scope is
  refined after discovery: "После discovery мы пишем письмо и говорим, клиент дорогой, с изменениями
  после дискавери" (00:22:39). Mikhail: "Мы уже подставились, подписав framework agreement" (00:22:21).
- The hybrid discovery: "почему мы не можем замаскировать полный Discovery под наличие плана?"
  (Anton, 00:11:56); "наверное, я склоняюсь согласиться с тобой о том, что надо где-то промежуточное
  что-то такое делать" (Kavalchuk, 00:12:43).
- The BA and prototypes: "садится бизнес-аналитик, делает прототипчики. Естественно, бизнес-аналитику
  дается установка, что вот ты на VBS, на SOF смотришь, но делаешь все там минималистично" (Mikhail,
  00:33:15); "Клодовские. HTML-ка ... у нас была HTML либо с одним входом ... либо ... 10-15 HTML,
  которые были прокликаны с клиентом ... и в конце было там аксептанс от клиента" (00:41:16);
  "разработчики будут подключаться только после того, как прототип показан, прокликан, заопроводен"
  (00:14:13). Kavalchuk: "VBS выровненная плюс прототипы каждой фичи VBS ... и плюс аксептанс от
  клиента" (00:42:03); Mikhail: "это программа максимум ... сомневаюсь, что за месяц на все это
  получится" (00:42:13).
- The BA starts before the client's contact: "если мы найдем подходящего кандидата, то я предлагаю
  начинать жрать бюджет проекта прямо сейчас, и чтобы BA начинал готовить эти прототипы" (Mikhail,
  00:49:37); "Можешь." (Kavalchuk, 00:49:51); "договариваемся с аналитиком ... давайте неделя, такие-то
  Deliverable от аналитика, первая итерация такая" (Arseniy, 00:52:32).
- No tech lead from day one; an architect on demand: "нужен будет, скорее, даже не техлит, а потом
  архитектор, чтобы наш аналитик не нафантазировал себе систему, которую нельзя собрать. Вот здесь
  просто на уровне консультации" (Kavalchuk, 00:15:24). Arseniy: "архитекторского опыта прямо
  коммерческого у меня нет. Но в целом да, почему нет?" (00:15:43). Left to the tasks: "потом от задачи
  будем плясать" (00:15:51).

## Agreements with the client

None - internal meeting.

## Internal agreements

- Kavalchuk asks the client for a responsible person and does not name a start date: "я в любом
  случае пишу письмо, я в любом случае не говорю о каких-то сроках, когда мы начали" (00:20:39).
- Watch the budget through discovery and raise it early: "Как только будут такие факты выясняться,
  будем красный флаг поднимать" (Mikhail, 00:43:53). After discovery: "Мы либо забираем этот
  перерасход на себя, либо скидываем его на клиента, либо делаем гибрид" (Kavalchuk, 00:36:55).

## Actions

- Kavalchuk: write to the client asking for a responsible person, and send the SOW (00:48:04).
- Mikhail: start looking for the BA (00:48:04). In the contract chat of 12 October Mikhail had asked
  Anton to request a senior BA, and Anton took the BA search on ([[2025-11-25 Contract chat - rendering 4]]
  2026-10-12 12:51, 13:04).
- "кто из вас": review the scope, sketch a timeline and give a discovery plan as an artifact for the
  client (Kavalchuk, 00:48:04). Mikhail asked Anton for it after the call. Draft in `pm/`.
- Arseniy: find out whether Marina Zaretskaya is available (00:53:48), through her department
  (00:55:46 to 00:55:55).
- Agree the BA's hours and first deliverables up front if the BA starts before the client's contact
  (Arseniy, 00:52:32).

No Jira keys yet; there is no board.

## Questions raised

- Whether the six months have started: no Effective Date is written, "это вопрос такой в серой зоне"
  (Mikhail, 00:06:30); [[QUE-007 What is the Effective Date]].
- Annex 2: "второй аннекс - это остаточный ... payment plan был изначально отдельным аннексом, потом
  его запихнули в основной агримент, а вот эта одна ссылка осталась" (Anton, 00:02:02);
  [[QUE-006 Which SOW and which plan are Annex 1 and Annex 2]].
- Starting without the advance: "Вопрос, возможно, к лидершику будет, а стартанем ли мы, например, без
  prepayment" (Anton, 00:02:02). Not answered.
- How long the project will really take: "мы не можем сказать, сколько это займет. Просто потому, что
  информации о том, что надо делать, очень мало" (Mikhail, 00:07:02); the estimators "эстимировали
  какого-то сферического коня в вакууме", with "буквально один митинг" of client input (00:10:29).
- Whether Claude-assisted delivery makes the budget: Mikhail's view that it is the only factor that can
  (00:16:21); Anton "в какой-то мере верю" (00:17:41); estimating it "я не уверен, что у нас кто-нибудь
  сможет" (Mikhail, 00:36:03).
- Whether in-house prototyping tools exist beyond Claude (Kavalchuk, 00:44:29 to 00:47:48). Anton:
  "Клод все еще генерирует HTML, и это сейчас самое эффективное в целом везде" (00:47:48).

## New scope mentioned

None.

## Proposed changes

Source keys: T13 = [[2026-10-13 Optimum Three Caballeros call - transcript]]; T12 =
[[2026-10-12 Optimum Three Caballeros call - transcript]]; CC4 = [[2025-11-25 Contract chat - rendering 4]]
(date and UTC time of the message); FC = [[2026-09-07 Final contract - rendering]]; QA =
[[2025-10-29 Client answers to the Q&A register - rendering]].

Approved by Anton Oparienko on 2026-10-13: all rows. DEC-014's deciders confirmed by him (human:mikhail.andrushkevich, human:anton.oparienko, human:arseniy.klimenko), so it is proposed; DEC-015, DEC-016 and the DEC-010 update have deciders tbd and stay draft. The 30 September row 3 was approved too, so the numbers stand.

New Decisions are numbered after DEC-013, which the 30 September minutes propose
([[2026-09-30 Optimum Three Caballeros call - minutes]] row 3); if that row is dropped, they move down
by one. New risks continue from K-2.

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | update | QUE-007 What is the Effective Date, with a pointer line in COM-001 Delivery within six months | Where signing stands: the client has signed. "Подписанный с обеих сторон контракт" (Lizaveta Shauchenka); "Контракт подписан 07.10.2026" (Kavalchuk). The readings, all kept: Aliaksandra Kalevich-Palonskaya, who prepared the legalisation (29 Sep) - the contract sets no date of entry into force, so it takes effect on the last party's signature, the annexes on theirs, and "Срок на разработку по моему мнению в данном случае не начался" (the client had not signed then); Kavalchuk, 12 Oct - "По поводу начала от даты подписания контракта срок пошёл"; Mikhail, 13 Oct - not written down, "в серой зоне". Anton's question "срок 6 месяцев откуда считаем?" is unanswered. 13 Oct: no start date is named to the client. Stays proposed | extracted | - | CC4 2026-09-29 12:27, 2026-10-12 10:01, 11:05, 12:22; T13 00:06:30, 00:20:39 | applied 2026-10-13 |
| 2 | update | QUE-006 Which SOW and which plan are Annex 1 and Annex 2 | Since 28 Sep: only the frame is signed and attested, no annex; the expected annexes are the SOW and the approved financial plan (Kalevich-Palonskaya). The SOW v10.4 document was reworked "в соответствии с фреймом + добавил несколько новых формулировок" (Krasner, 29 Sep); PMO review done 5 Oct, Legal review done 5 Oct; the changed Arabic text translated in-house, finished 9 Oct. The client last saw the SOW of 15 June and never returned it, only the contract PDF (Lizaveta, 6 Oct). Annex 2: "мисэлаймент формулировок" (Kavalchuk); the payment plan moved into the Agreement and the reference stayed (Anton, 12 and 13 Oct); to settle in one of the first letters to the client's responsible person (Kavalchuk). Contract 7.2 makes Article 7's plan part of the SOW; 7.11 pays only to the account "identified in the approved Financial Plan" (K-8). The SOW goes as it stands (row 10). The reworked SOW is stored when it is sent, and the five disputed Commitments are re-checked against it | extracted | - | CC4 2026-09-29 07:47, 12:27, 12:28, 2026-10-05 09:51, 14:12, 2026-10-06 09:10, 10:31, 2026-10-09 12:07, 2026-10-12 12:54 to 13:00; T13 00:02:02; FC 7.2, 7.11 | applied 2026-10-13 |
| 3 | update | COM-008 Client cooperation and dependencies | Who the client's people are, filling "not known yet": "Ishaq Lawal - General Manager", "Dr.Yahya Alsayel - юрист", "Dr. Jaber - CEO", "Ayaa Khalid - ассистент", "Через Айю координируем все" (Lizaveta, 29 Sep). No project contact yet; the client is to name one after a letter (Kavalchuk, 29 Sep and 13 Oct). What we ask for (Mikhail, 29 Sep): an English-speaking project lead, a product owner with authority to approve, access to subject experts, an escalation path, a kickoff, executive help with IT security and access, Monday to Thursday as the overlap. "по текущим условиям контракта задержки со стороны клиента не освобождают нас от обязательства выполнить delivery в установленный срок" (Mikhail). Kavalchuk's experience of the region: the person named may not engage, or may not know the project (13 Oct). Stays disputed | extracted | - | CC4 2026-09-29 07:02, 08:21, 08:22, 12:25, 15:51; T13 00:12:43, 00:18:18, 00:48:04 | applied 2026-10-13 |
| 4 | update | COM-006 Information sufficient for scope and price | The team's reading after signing: the WBS is too high-level to build or to prototype from, "Нам надо сделать inventory management, и на этом тоже две или три строчки"; the estimate rested on "буквально один митинг" (Mikhail). Kavalchuk: by 2.3-2.5 "мы подвтердили, что задача нам понятно и вопросов не осталось". Mikhail: a conscious decision, the client demanded signing without edits | extracted | - | CC4 2026-10-12 12:22, 12:37; T13 00:07:02, 00:10:29 | applied 2026-10-13 |
| 5 | new | DEC-014 Staff on demand, seniors who work with Claude, fewer developers | Delivery. Mikhail's message of 29 Sep, "к которым мы пришли в обсуждениях с @Anton Oparienko и @Arseniy Klimenko": the planning principle moves from the fastest start to the least loss from idle time, given a high risk of client delays. On demand where possible; a fixed allocation only with 2-3 weeks of work unblocked. Instead of the presale's 2 BE + 2 FE and a solution architect: a strong TL / architect / full-stack developer who works well with Claude; full-stack developers added as ready backlog grows, at most two at once, not from the start; a BA who builds clickable prototypes with Claude; a designer at much lower allocation or none. Options: the presale's cheaper team (not taken for fixed price; the rate removed); a fast start with staffing before the official start (the original line). Consequences: harder resource planning; "с высокой вероятностью приведет к увеличению фактического срока"; client delays do not release us (COM-001, COM-008); the UI Kit and mockups are still Milestone 1 deliverables (COM-020). 13 Oct: no TL from day one, an architect on demand; Anton, 12 Oct: a part-time Flutter TL may be needed. Alexey: "все правильно говоришь ... продолжаем подготовку". Deciders from the message: Mikhail, Anton, Arseniy - confirm. Pointer in DEC-002 | extracted | - | CC4 2026-09-29 15:51 to 16:06, 2026-10-12 11:05; T13 00:14:13 to 00:15:51 | applied 2026-10-13 |
| 6 | update | DEC-002 Senior engineers first | The team shape since 29 Sep is DEC-014: seniors who work with Claude rather than the cheaper team the presale considered. No longer holds: the solution architect as a position that stays with the project (28 Sep) - on demand, "на уровне консультации" (13 Oct). The TL from the mobile department is still open | extracted | - | CC4 2026-09-29 15:51; T13 00:15:24 | applied 2026-10-13 |
| 7 | update | DEC-010 Confirm the product with the client through prototypes in code | Confirmed with the AM on 13 Oct: prototypes in Claude as HTML, "к черту фигму"; one linked prototype or 10-15 HTML pages clicked through with the client, feedback reflected, "аксептанс от клиента" at the end; developers join an area only after its prototype is approved; output "VBS выровненная плюс прототипы каждой фичи VBS ... плюс аксептанс" (Kavalchuk) - "программа максимум", not likely in a month (Mikhail). Other tools (Lovable, in-house kits) raised by Kavalchuk, left to the team. The designer: much lower allocation or none (29 Sep). Still draft; who decided - name them | extracted | - | T13 00:14:13, 00:33:15, 00:41:16 to 00:42:13, 00:44:29 to 00:48:04; CC4 2026-09-29 15:51 | applied 2026-10-13 |
| 8 | update | DEC-011 Move scope between milestones and start building in the first month | No longer holds: starting to code in the first month. "С разработкой я бы не спешил, дождался первых результатов работы ВА" (Mikhail, 12 Oct); developers join an area only after its prototype is approved (13 Oct). Moving scope between milestones was not discussed | extracted | - | CC4 2026-10-12 10:28; T13 00:14:13 | applied 2026-10-13 |
| 9 | new | DEC-015 Discovery: our own picture of the system, questions as if from scratch | Delivery. Options: (1) open questions, a full discovery from zero - shows we signed without understanding; (2) design the system ourselves, prototype it, then show it - looks better, may miss; (3) Anton's hybrid, "замаскировать полный Discovery под наличие плана": the WBS modules as our picture, questions asked so the client tells us everything; Kavalchuk backed a middle way with prepared questions and a plan. Chosen: 3. Consequences: a discovery plan and timeline as an artifact for the client; the BA may start prototyping before the client's contact, on the project budget, with hours and deliverables agreed up front; the BA keeps solutions minimal; per area the WBS line, the BA's minimal solution and the client's ask are compared and a red flag raised early; after discovery an internal call - absorb the overrun, ask the client to pay, or a mix. Against the SOW (evaluated): the plan has to produce every Milestone 1 deliverable (COM-020), not only prototypes. Who decided - name them | extracted | - | T13 00:10:01 to 00:14:13, 00:33:15, 00:36:55, 00:39:09, 00:43:53, 00:48:04 to 00:52:32 | applied 2026-10-13 |
| 10 | new | DEC-016 Send the SOW as it stands and start preparing without waiting for its signature | Commercial. Options: hold all work until the SOW is signed (Kavalchuk, 29 Sep: "пока стартовать нечего, нам нужно довыслать SOW и подписать его"; Mikhail, 12 Oct: its signing "является поводом к старту"); hold the SOW and rewrite its scope first (Kavalchuk, 13 Oct); send it as it stands and refine scope by letter after discovery. Chosen: the third - the client would not accept changes to the statements, "Мы уже подставились" (Mikhail). Preparation starts now: the BA search and the discovery plan ("я бы уже начинал разбираться", Kavalchuk; "Я займусь сетапом и поском БА в параллели", Anton). Open: starting before the advance is paid (Anton, to leadership). Consequences: whatever scope the SOW fixes binds acceptance "столько раз, пока клиент тебе не скажет «да, хорошо»" (Kavalchuk, 00:24:33); the SOW as sent is to be stored. Against DEC-009: consistent (the Agreement as it stands). Who decided - name them | extracted | - | CC4 2026-09-29 12:25, 2026-10-12 12:51, 13:01, 13:04; T13 00:02:02, 00:22:21 to 00:24:33, 00:29:33, 00:31:29 | applied 2026-10-13 |
| 11 | update | DEC-004 Backend stack; CON-001 Offline operation and sync between rigs and HQ; CON-004 Scale and data volume | Redis out for now, 12 Oct: Alexey Gamanovich objected to Redis in the mobile team's architecture as a single point of failure that scales badly; Arseniy held a session with the mobile team; "Решили, типа, идти без него" - direct writes to the API, Kafka or horizontal scaling behind a load balancer if a need appears. Why it is enough, Mikhail's reading: 70 to about 100 rigs, data typed by hand, "это может быть десяток параметров или пара десятков за сутки", rigs online at different times. Anton: a load test of, say, 30 rigs at once; Mikhail: only if there is nothing else to do. For CON-004: Mikhail's daily volume is below the client's own figures (under 50 parameters about 4 times a day, QA Part 1, 2) - both kept. DEC-004 option 2 loses its Redis queue and worker; the decision stays open | extracted | - | T12 00:00:56, 00:04:01, 00:06:58, 00:07:23, 00:08:48; QA Part 1, 2 | applied 2026-10-13 |
| 12 | new | K-3 The six months run from the client's signature, before discovery starts | Internal register. Cause: the contract defines no Effective Date, and Kalevich-Palonskaya's reading (29 Sep) puts entry into force at the last signature, given on 7 Oct (row 1). Event: the client counts the six months from that date. Effect: the client contact, the BA hire and discovery eat into a term already running, with no relief for client delays (COM-001, COM-008). Draft, not scored | evaluated | - | CC4 2026-09-29 12:27, 2026-10-12 12:22; T13 00:06:30 | applied 2026-10-13 |
| 13 | new | K-4 No client contact with authority, or a slow one | Internal. Cause: no project contact named; Kavalchuk's experience of the region; Mikhail's 29 Sep reading of a high risk of delays in signing, access, information, feedback and decisions. Event: the contact comes late, does not engage, or cannot answer or approve. Effect: discovery idles while the term runs; areas cannot be accepted. Response so far: Kavalchuk asks the client to name a responsible person; the BA may start before (DEC-015). Draft | extracted | - | CC4 2026-09-29 15:51; T13 00:12:43, 00:18:18 | applied 2026-10-13 |
| 14 | new | K-5 Scope grows through the prototypes | Internal. Cause: fixed price with acceptance repeated until the client says yes ("по 5, 10, 20, 100 раз", Mikhail; COM-002), and a BA who designs beyond the WBS line ("нафантазируем космолет", Kavalchuk). Event: the client sees and asks for more than each line holds. Effect: hours many times the estimate ("бюджет x5", Kavalchuk). Response: DEC-015's minimal solutions, per-area comparison, early flag, post-discovery call. Draft | extracted | - | T13 00:24:33, 00:25:22, 00:31:29, 00:42:44 | applied 2026-10-13 |
| 15 | new | K-6 No suitable BA in time | Internal. Cause: a senior BA who works at product level and prototypes with Claude is rare; Mikhail's last search took about two weeks and seven candidates, with two escalations, and ended in a compromise. Event: no such BA within 1-2 weeks. Effect: discovery starts late or with a weaker BA. Draft | extracted | - | T13 00:19:40 | applied 2026-10-13 |
| 16 | new | K-7 Estimates for Claude-assisted development do not hold | Internal. Cause: the plan counts on fewer developers working with Claude (DEC-014), and "Делать эстимации на разработку с активным использованием кода я не уверен, что у нас кто-нибудь сможет" (Mikhail; "кода" is Claude). Event: delivery speed below what the plan assumes. Effect: overrun or delay. Draft | extracted | - | T13 00:16:21, 00:36:03 | applied 2026-10-13 |
| 17 | new | K-8 Payments held for want of an approved Financial Plan | Internal. Cause: contract 7.11 pays only to the account "identified in the approved Financial Plan"; Annex 2 is named but is neither the Agreement nor the stored SOW, which names no account (QUE-006); "мисэлаймент формулировок" (Kavalchuk). Event: the client holds an invoice, the advance first, until a Financial Plan is approved. Effect: work without payment. Our reading | evaluated | - | FC 7.2, 7.11; CC4 2026-10-12 12:54 to 13:00 | applied 2026-10-13 |
| 18 | new | K-9 Conflict in the region disrupts the client | Internal. Cause: Houthi strikes on Riyadh and Khurais reported on 4-5 Oct, the East-West pipeline stopped again, an offensive in Yemen (Anton). Event: the escalation reaches the client's operations or decisions. Effect: contacts, feedback and approvals slow down. "Вряд ли у нас есть прямо экшн айтемы по этому поводу, но в голове держать стоит". Draft | extracted | - | CC4 2026-10-05 09:25 | applied 2026-10-13 |
| 19 | no material | The SOW's Arabic translation | In-house by Johni Algarbi, by hand, rather than a bureau (Kavalchuk: "Запускай на бюджетный перевод"); Legal: no legal difference, both can be signed; done 9 Oct. Process, covered by row 2 | - | - | CC4 2026-10-06 10:52 to 10:59, 2026-10-09 12:07; T12 00:09:15 | recorded 2026-10-13, no note |
| 20 | no material | The SOW's notice e-mail | The English and Arabic texts had different company addresses; Legal chose one. A contract detail of the SOW, to read when it is stored | - | - | CC4 2026-10-09 11:03, 11:08 | recorded 2026-10-13, no note |
| 21 | no material | Roles on our side | "Антон Опариенко будет ПМ, а я лид ПМом" (Mikhail); Kavalchuk is the project's AM. Roles belong in the stakeholder register, not the KB | - | - | CC4 2026-09-28 13:02, 2026-09-29 15:51 | recorded 2026-10-13, no note |
| 22 | no material | Liability, margin and the decision to sign | The formula-defect liability again (already K-2, COM-017); the margin talk is money; the contract group had told Arseniy to decline and management decided to sign (already DEC-009) | - | - | T12 00:12:29 to 00:16:34; T13 00:27:04 to 00:29:33 | recorded 2026-10-13, no note |
| 23 | no material | The client's CEO in Warsaw, 29 Sep | Handing over the original and a company visit; "Не думаем, что будет обсуждаться проект" (Kavalchuk) | - | - | CC4 2026-09-28 12:52 to 13:07 | recorded 2026-10-13, no note |
| 24 | no material | Kavalchuk's example letter | The shape of the letter to the client: analyst and PM for N weeks, X sessions a week of Y hours, result Z; input to the discovery plan in `pm/` | - | - | CC4 2026-10-12 12:45 | recorded 2026-10-13, no note |
| 25 | no material | Marina Zaretskaya as the BA | Raised as the best-placed candidate from the presale; her availability is a staffing matter. The remarks about her status were removed from the transcript | - | - | T13 00:53:03; CC4 2026-10-12 12:51 | recorded 2026-10-13, no note |
