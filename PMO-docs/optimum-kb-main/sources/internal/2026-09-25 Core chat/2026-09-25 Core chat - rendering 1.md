---
type: source
kind: rendering
date: 2026-09-25
original: https://chat.google.com/room/AAQAkfyHFwA
removed:
  - 0 bot messages, 0 task-system messages, 0 empty messages
  - a rate figure, replaced in square brackets
  - reactions; blank lines inside messages
---

# 2026-09-25 Core chat - rendering 1

Google Chat space "[Core] Optimum engineering" (spaces/AAQAkfyHFwA), part 1 of 1: from 2026-09-25 11:53 UTC to 2026-10-14 08:35 UTC. Read on 2026-10-14; rendered by `pm/seed-ingest-scripts/chat2md.mjs` from the Chat tool's output. Every message in order: time in UTC, author, text verbatim (typos kept; blank lines inside a message dropped), links and attachments. "↳ YYYY-MM-DD HH:MM" marks a reply in the thread started by the message of that time, which may be in another part. Money amounts, credentials and e-mail addresses are replaced in square brackets. Where an attachment is stored in the KB, its rendering is named. Never edited after storing.

## 2026-09-25

- 11:53 **Arseniy Klimenko**: @Anton Oparienko @Mikhail Andrushkevich 
  сделал нам чатик, чтобы удобнее было обсуждать и шарить документы 
  Здесь есть проектная часть
  UPD SOW Optimum 15.05 (v10.4)  
  Здесь экономика 
  P&L Optimum Engineering Standards 2026 
  Здесь актуальная WBS (смотрим на оценку с флатером. Тут есть еще один столбец, в девелопменте. Это просто обычные часы + стабилизация)
  v1 EST - Optimum Engineering Standards - ASnot - SA - Big data - 023690 
  Здесь все материалы что они прислали, по графикам и формулам
  materials
  - Links: https://docs.google.com/document/d/1bzY2oTz7nEbwalBQXC3dAPhmzVPRzZL2pf7iEAVG6-g/edit?tab=t.0 - [[2026-06-15 SOW v10.4 - rendering]] (the document as stored on 2026-09-28; edited since) · https://docs.google.com/spreadsheets/d/1OEcvaQtpwPDKw93vmxLSc624xQleLHhW5nCaPHiuxO8/edit?gid=2103856801#gid=2103856801 · https://docs.google.com/spreadsheets/d/10H7vDQCbev_-jC6y0J5zeCw1Os2n-6MfJiAVb0k2hbg/edit?gid=1084138282#gid=1084138282 - [[2026-09-25 v1 WBS - rendering]] · https://drive.google.com/drive/folders/1pC29fiMRRpXLm4ikHdjY4qJbZyH8TFKx - [[2025-11-20 Client formula and chart samples - rendering]]
  - Attachment: UPD SOW Optimum 15.05 (v10.4)  (Google Doc) - [[2026-06-15 SOW v10.4 - rendering]] (the document as stored on 2026-09-28; edited since)
  - Attachment: P&L Optimum Engineering Standards 2026 (Google Sheet)
  - Attachment: v1 EST - Optimum Engineering Standards - ASnot - SA - Big data - 023690 (Google Sheet) - [[2026-09-25 v1 WBS - rendering]]
  - Attachment: materials (Drive folder) - [[2025-11-20 Client formula and chart samples - rendering]]

## 2026-09-28

- 09:46 **Mikhail Andrushkevich**: По результатам сегодняшнего колла:
  Я: разузнаю про доступность Снотова - на связи ли он, когда выходит из отпуска, когда встречается
  Арсений: сделает требования к TL\\AR
  Антон: отразит текущий вижн в P&L
  RACI - postponed
- 20:37 **Anton Oparienko**: Разница в sow и контракте  и прочие нюансы.
- 20:45 **Anton Oparienko** (↳ 2026-09-28 20:37): Прочитайте завтра, можем обсудить на синке.
  Я общался с Лешей вечером и мне кажется что у него в представлении некоторые вещи, что его волновали были пофикшены в контракте. На самом деле как я понимаю их пытались пофиксить в сов, не договорились и что-то осталось в основном контракте, который доминирует. И клиент сейчас забирает только основной контракт, что с совом вообще не очень понятно.
  Я из КБ сейчас нагенерил список, по идее эти вопросы надо как-то с биздевом и контрактной группой поднимать.
  Here's where the signed Optimum contract and the SOW v10.4 disagree, from the KB. 5 commitments are marked disputed there, both versions are kept in the notes, and nothing is settled yet. No figures here, those stay in Drive and the P&L. Internal only, not for the client.
  Two things up front. The contract's order of precedence (1.3) puts the Agreement above the SOW, so on the face of it the contract wins every clash below. But nobody has confirmed the SOW v10.4 is actually Annex 1. Also, the Arabic text prevails (15.3), and we only have the English in the KB.
  Delivery term (COM-001):
  Contract - 6 months from the Effective Date, extended only by a CR the client signs (2.2). Clarification requests give no extra time (2.5).
  SOW - "approximately six (6) months" from a start agreed by email. It extends for client or third-party delays, and if discovery finds more work (row 14).
  We asked on Aug 25 that client delays extend the term day for day, and the client declined on Sep 2. The English text has no penalty clause for late delivery. What happens instead: a month's payment isn't due until that month's work is done (7.5), and the final payment waits for final acceptance (7.6).
  Late client input (COM-008):
  Contract - we can pause only a task that is objectively impossible, and only after the client missed its 3 business day answer. Even then only that task pauses (4.5). No idle time compensation, and we can't terminate over it (11.3).
  SOW - we can suspend the affected work or start termination, and the client pays for idle time after written notice (row 13).
  Payments (COM-012), three versions:
  Contract - a capped advance, then a payment at the end of months 1-5, each only on verified completion of that month's work. The final payment comes at the end of month 6, on final acceptance (7.3-7.7). The client can withhold disputed amounts without it counting as a payment default (7.12).
  SOW fee schedule - a cost for each of milestones 1-4. Milestone 5's cell says milestones 4 and 5 are "deemed covered by the Advance Payment", and milestone 6 has no cost of its own. The advance is paid per "Clause 4.6 of the Agreement", which doesn't exist in the final contract.
  Plan sent on March 11 - an advance, then a payment each month April to September. It's from the T&M days, before fixed price.
  Saudi compliance (COM-015):
  Contract - we warrant compliance with all applicable Saudi cybersecurity and data rules, NCA included, plus hosting, data residency and cross-border transfers. "No category of applicable Saudi requirement is excluded" (10.1-10.2).
  SOW - the client provides the compliance requirements before the start.
  Our July 14 letter tried to narrow it to NCNICC-1:2025 + PDPL, and the client widened it instead. It was accepted as a known risk on Sep 7. Related open point: is the client NCA category A or B? We think B, but the client hasn't confirmed. If it's A, pen testing is mandatory, and it isn't in the WBS.
  Termination (COM-016):
  Contract - the client can terminate for convenience on 10 business days' notice, or for a breach not cured in 15 business days (immediately for "repeated material delay"). We can terminate only for an undisputed payment default that lasts 20 business days (11.1-11.3). On termination we're paid only for work that is completed, delivered and usable (11.4).
  SOW - either party can terminate for convenience on 30 days' notice (row 37).
  We asked for mutual rights on Aug 25, the client declined on Sep 2, and it was accepted as a known risk on Sep 7.
  Smaller mismatches, not marked disputed:
  Acceptance (COM-002) - the SOW points to clauses 7.9-7.10 of the Agreement, which in the final contract are the progress report and the price cap. The real terms are 3.2-3.3: 14 business days per delivery, the clock restarts after each fix, and there's no deemed acceptance.
  SOW header - it names "Contract No. (1/26) dated 15/05/2026" and a different client registration number from the contract.
  Defect fixing (COM-003) - the contract leaves remediation times to the SOW, and the SOW has none. Minor and Trivial defects have to be fixed too.
  Liability (COM-017) - the SOW's limits (business impact, code changed by others, other environments) aren't in the contract. Contract 12.3 is a floor, "not less than the total Contract price", with no cap.
  Warranty (COM-004) - 12 months from final acceptance, and the SOW puts support under a separate SLA. On Sep 2 the client clarified that the warranty covers defects in our work only. There's no WBS line for it.
  Specialists (COM-010) - not a conflict. The contract needs approval only for subcontracting or assigning part of the work (6.2), and the SOW lets us replace a specialist on 15 days' notice. Neither commits to a named team.
  14.2 reads "within thirty (15 ) days".

## 2026-09-29

- 09:23 **Anton Oparienko**: P&L Optimum Engineering Standards 2026 таба с моим вариантом
  - Link: https://docs.google.com/spreadsheets/d/1OEcvaQtpwPDKw93vmxLSc624xQleLHhW5nCaPHiuxO8/edit?gid=1229356725#gid=1229356725
  - Attachment: P&L Optimum Engineering Standards 2026 (Google Sheet)
- 09:29 **Anton Oparienko** (↳ 2026-09-29 09:23): больше дальше тут не колдую, жду ваш фидбэк тогда @Arseniy Klimenko @Mikhail Andrushkevich
- 10:00 **Anton Oparienko** (↳ 2026-09-29 09:23): Вот как выглядят часики, чтобы было легче понять
  - Attachment: image.png (in the chat)
- 10:17 **Anton Oparienko**: @Mikhail Andrushkevich Выцепил Лешу:
  1) По старту и стаффингу - он сказал ок, пока придерживаем если Саша так сказал, готовимся сами что можем, те условно у нас тогда есть время по процессу пройти. Сказал что синхронизируется с Сашей и Снотовым - тк у них может быть разное видение и разные истории Клиенту рассказывать.
  2) По тому как будет работать p&l и распределение в отделы. Леша сказал делать следующим образом - деньги поступают на счет, не обязательно их все распределять. Распределяем деньги (пейды) по мере того как выполняем работы из тех денег что уже получили. Если деньги кончились - не отдаем ничего, у нас кассовый разрыва, как деньги пуступили - раздали что должны\\что есть. RM сразу при входе предупредить что такая ситуация возможно, тк траншевые платежи и фикс прайс. А вот наш общий план по часам из которого расчет - сделаем за меньшее количество часов - будет выше наш плавающий рейт.
- 10:19 **Mikhail Andrushkevich** (↳ 2026-09-29 10:17): а "наш плавающий рейт" это что?
- 10:20 **Mikhail Andrushkevich**: @Arseniy Klimenko @Anton Oparienko у проекта еще нет strategy & accounting чатов или у вас что-то есть?
- 10:21 **Anton Oparienko** (↳ 2026-09-29 10:17): Технически наш рейт не установлен - это сумма контракта/на нашу текущую оцнку воркед часов. Если мы справимся за меньшее количество воркедов, то наш рейт растет, но с этим надо очень аккуратненько.
- 10:22 **Mikhail Andrushkevich** (↳ 2026-09-29 10:17): Сейчас же подразумевается средний рейт по проекту?
- 10:23 **Anton Oparienko** (↳ 2026-09-29 10:20): они скорее всего создаются при переходе сделки в другой статус (может и созданы уже но там только сейлы и лидершип). В любом случае мы вроде не создаем их руками.
  Какой-то статус по идее сейчас есть смысл писать в контрактном чате?
- 10:24 **Anton Oparienko** (↳ 2026-09-29 10:17): сейчас да, рейт это сумма\\4901 час который вышел из эстима, получилось [rate removed]
- 10:24 **Mikhail Andrushkevich** (↳ 2026-09-29 10:20): Насколько я помню наши процессы там или ПМ или RM их делает. Но когда именно не помню, речекну.
- 10:25 **Anton Oparienko** (↳ 2026-09-29 10:17): Если под конец проекта мы видим что заложив время на гарантию и все мы видим что часов например будет потрачено 4000, то по идее надо пересчитывать что кому идет. До этого момента надо еще дожить и чтобы он случился)
- 10:26 **Anton Oparienko** (↳ 2026-09-29 10:20): 95% уверен что создаются автоматизацией. Просто иногда возможно это игнорят
- 10:26 **Anton Oparienko** (↳ 2026-09-29 10:20): (no text)
  - Attachment: image.png (in the chat)

## 2026-09-30

- 09:13 **Anton Oparienko**: (no text)
  - Attachment: Capability_Driven_AI_Delivery_Methodology_RU (1).docx (in the chat)
- 09:14 **Anton Oparienko**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- 12:38 **Arseniy Klimenko**: Хочу к завтра подготовить наше тех видение. Что вообще думаете будет полезно увидеть, пару диаграм (контейнеры,контекст) и общее тех видение достаточно?
- 14:38 **Anton Oparienko** (↳ 2026-09-30 12:38): @Arseniy Klimenko Думаю для начала точно достаточно, давай с чего-то начнем и от этого будем плясать дальше и обсудим с Лешей.
  И жду еще твой юзернейм

## 2026-10-01

- 12:56 **Arseniy Klimenko**: Вот диаграммы от технарей. Как вариант видения солюшена
  - Attachment: Optium_Engineering_Architecture.png (in the chat) - [[2026-10-01 Solution vision diagrams - rendering]]
  - Attachment: Optium_Engineering_frontend.png (in the chat) - [[2026-10-01 Solution vision diagrams - rendering]]
- 12:56 **Arseniy Klimenko**: Здесь варант с бэком на супабейз

## 2026-10-05

- 07:02 **Anton Oparienko**: А гляньте новости, там ребятки вроде в войну влезли и нефтепроводы бомбят. Думаю это на нас может повлиять.

## 2026-10-08

- 08:10 **Mikhail Andrushkevich**: @all , есть у кого-нибудь повестка для созвона или отменяем мит сегодня?

## 2026-10-09

- 06:41 **Mikhail Andrushkevich**: @all , на сегодня есть агенда на мит?
- 07:35 **Anton Oparienko** (↳ 2026-10-09 06:41): Думаю нет особо, как там контракт?
  Леше вчера еще отправил диаграммы, что скидывал Арсений.
  Сегодня наверное хватит времени посмотреть сенситив и что мы еще на прошлом мите обсуждали.
- 07:39 **Mikhail Andrushkevich** (↳ 2026-10-09 06:41): Полчаса назад с Джонни общался, почти готов, финальные штрихи
- 07:43 **Mikhail Andrushkevich** (↳ 2026-10-09 06:41): Нда, перепроверил клодом, что-то там еще не финал

## 2026-10-12

- 08:59 **Mikhail Andrushkevich**: @all , есть топики на сегодня?
- 09:00 **Anton Oparienko** (↳ 2026-10-12 08:59): Думаю только если Арсению есть расскахать что наобсуждал в пятницу по архитектуре с Лешей.
- 09:00 **Mikhail Andrushkevich** (↳ 2026-10-12 08:59): ок, задержусь на пару минут

## 2026-10-14

- 08:35 **Anton Oparienko**: @Mikhail Andrushkevich 
  Сегодня на звонке надо будет кое-что обсудить по стаффингу, там надо цифры посмотреть и немного подготовить Яну и Юлю по нюансам проекта, оплатам и тп.
  Я немного обновил описание, посмотри если так ок
  Project: an offline-first Windows desktop app for mud engineers on about 70 oil rigs in Saudi Arabia,
  plus a web app for HQ, with data sync between them. Fixed price, six monthly milestones; the first is a
  one-month discovery.
  Allocation: full-time at the start of the project, fewer hours later in development. Location: any.
  Working hours must overlap with Saudi Arabia (UTC+3), Monday to Thursday.
  We are looking for a proactive, solution-oriented BA who can turn high-level client needs into practical, cost-effective solutions with minimal client involvement.
  Key Requirements:
  Product mindset: Takes ownership of solution design rather than just gathering and documenting
  requirements.
  Prototyping: Can independently create clickable UI prototypes, ideally with AI tools such as Claude,
  validate proposed solutions with the client, incorporate feedback, and secure acceptance.
  Pragmatic approach: Prioritizes simple, feasible solutions over complex functionality, balancing
  business value with implementation effort.
  Fixed-price awareness: Proactively manages scope and avoids unnecessary development costs.
  Client communication: Drives decisions by presenting concrete solutions rather than relying on the
  client to define detailed requirements. Runs regular client workshops in fluent English.
  Documentation: Turns approved prototypes into user stories with acceptance criteria and a
  vision-and-scope document.
  Nice to have: Experience with Claude Design or similar AI-powered prototyping tools; oil and gas or
  drilling; offline-first or desktop applications; engineering calculations; clients in the Gulf; Arabic.
  Key differentiator: We need a BA who can propose and validate solutions, not just collect requirements.
