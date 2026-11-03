---
type: source
kind: rendering
date: 2026-10-13
original: https://chat.google.com/room/AAQAXooObiI
removed:
  - 0 bot messages, 0 task-system messages, 0 empty messages
  - reactions; blank lines inside messages
---

# 2025-11-25 Contract chat - rendering 5

Google Chat space "(Contract) Optimum Engineering Standards" (spaces/AAQAXooObiI), part 5 of 5: from 2026-10-13 09:55 UTC to 2026-10-14 12:47 UTC. Read on 2026-10-14; rendered by `pm/seed-ingest-scripts/chat2md.mjs` from the Chat tool's output. Every message in order: time in UTC, author, text verbatim (typos kept; blank lines inside a message dropped), links and attachments. "↳ YYYY-MM-DD HH:MM" marks a reply in the thread started by the message of that time, which may be in another part. Money amounts, credentials and e-mail addresses are replaced in square brackets. Where an attachment is stored in the KB, its rendering is named. Never edited after storing.

## 2026-10-13

- 09:55 **Aliaksandr Kavalchuk**: @Mikhail Andrushkevich @Arseniy Klimenko @Anton Oparienko 
  1. Коммуникация с клиентом
  Отправляем клиенту текущую версию SOW и просим назначить ответственного за проект. Он станет точкой контакта для нашей delivery-команды (DM, PM, BA) на этапе Discovery.
  2. SOW
  2.1 Текущую версию SOW не меняем и высылаем как есть. Риск расхождения между обещаниями в SOW и фактической работой выравнивают PM и DM по ходу проекта.
  → Андрушкевич, Опариенко, Клименко: начать вести реестр рисков проекта.
  2.2 Скоуп уточняется по ходу Discovery и переоценивается с учётом сроков и таймлайна. Основная задача DM и PM — сохранять баланс между качеством и бюджетом.
  2.3 Есть формальное расхождение: фреймворк предполагает отдельное приложение с финпланом и таймлайном, а по факту эти данные включены в SOW.
  → Андрушкевич, Опариенко, Клименко: урегулирование вопроса в ходе Discovery.
  3. Подход к Discovery
  Гибридный формат: приходим с подготовленной структурой системы (модули, блоки), но требования собираем с клиентом заново.
  По SOW мы уже взяли на себя обязательства по результатам Discovery в большем объёме, чем запланировали внутри. Подход к их выполнению определяют PM и DM.
  Целевые результаты Discovery:
  1) уточнённая WBS;
  2) кликабельные прототипы (Claude Design);
  3) acceptance клиента.
  Если Discovery не уложится в месяц, управление сроками и готовностью результатов — на PM и DM.
  Порядок acceptance прототипа (целиком или по частям) и момент старта разработки определяют PM и DM.
  → Андрушкевич, Опариенко, Клименко:
  план Discovery и таймлайн в виде артефакта для передачи клиенту;
  подход к выполнению обязательств по Discovery, заявленных в SOW.
  4. Команда
  Ключевая роль на старте — BA, который работает с Claude Design: быстро генерирует прототипы, собирает обратную связь и получает acceptance клиента.
  Если BA найдём раньше, чем клиент даст контакт, он начинает прототипирование за счёт бюджета проекта, с заранее определёнными часами и результатами.
  → Андрушкевич: старт поиска BA (ориентир 1–2 недели).
  → Андрушкевич, Клименко, Опариенко: привлечение других специалистов on demand по необходимости (например, для подготовки SAD).
  5. Бюджет и скоуп
  Высокий риск выхода за бюджет. В ходе Discovery PM, BA и DM регулярно делают переоценку и сообщают об изменениях по четырём показателям: бюджет, скоуп, качество, ожидания клиента.
  Задача — найти оптимальное сочетание этих показателей с попаданием в бюджет.
  По итогам Discovery — уточнённый прогноз, включая границу возможного выхода за бюджет.
  → Андрушкевич, Опариенко, Клименко (+ BA после подключения): регулярная переоценка и отчётность по этим показателям; по итогам Discovery — прогноз с границей перерасхода.
  6. Риски (контрактные риски приняты менеджментом ранее)
  Fixed price при размытых критериях приёмки.
  Митигация: прототипы и acceptance клиента до старта разработки соответствующих частей (п. 3), реестр рисков (п. 2.1).
  → Андрушкевич, Опариенко, Клименко.
  Возможная низкая вовлечённость или медленные ответы со стороны клиента.
  Митигация: запрос назначенного ответственного со стороны клиента (п. 1); BA может начать прототипирование до получения контакта (п. 4).
  → Ковальчук (контакт), Андрушкевич (BA).
  Риск расширения скоупа через прототипы.
  Митигация: регулярная переоценка и отчётность по бюджету, скоупу, качеству и ожиданиям клиента (п. 5).
  → Андрушкевич, Опариенко, Клименко (+ BA).
  С ребятами мы связаны, все неоднозначности формулировок рад прояснить.
- 12:57 **Aliaksandr Kavalchuk**: Письмо клиенту с запросом о контактном лице отправлено.
- 13:30 **Alexey Gamanovich**: @Aliaksandr Kavalchuk, по фактической дате старта что-то яснее стало ?
- 13:50 **Aliaksandr Kavalchuk** (↳ 2026-10-13 13:30): Она зависит от нас и нашего плана. На сколько я понял, у нас нет понимания сколько времени у нас займёт объём работ, прописанный в ВБС и контракте. Поэтому я бы сказал, что официальный старт будет как только будет лицо со стороны клиента и наша готовность начинать.
  Я дату пока не называю клиенту, чтобы нас в рамки не загонять.
  Ребята могут начинать внутри разбираться, а что же мы делаем, какие у нас риски, и какие мб варианты.
- 13:58 **Mikhail Andrushkevich** (↳ 2026-10-13 13:30): Начинаем искать хорошего ВА, как находим, то ставим задачу ему изучить контекст и начать придумывать систему и делать прототипы в Клоде. Чтобы когда мы пойдем к клиенту общаться, то можно было уже показывать что-то кликающееся и собирать более предметный фидбек.
- 14:00 **Mikhail Andrushkevich**: @Anton Oparienko , можешь открыть позицию для ВА со следующими требованиями?
  Senior Business Analyst with Product Mindset
  We are looking for a proactive, solution-oriented BA who can turn high-level client needs into practical, cost-effective solutions with minimal client involvement.
  Key Requirements:
  Product mindset: Takes ownership of solution design rather than just gathering and documenting requirements.
  Prototyping: Can independently create UI prototypes, validate proposed solutions with the client, incorporate feedback, and secure acceptance.
  Pragmatic approach: Prioritizes simple, feasible solutions over complex functionality, balancing business value with implementation effort.
  Fixed-price awareness: Understands project economics, proactively manages scope, and avoids unnecessary development costs.
  Client communication: Drives decisions by presenting concrete solutions rather than relying on the client to define detailed requirements.
  Nice to have: Experience with Claude Design or similar AI-powered prototyping tools.
  Key differentiator: We need a BA who can propose and validate solutions, not just collect requirements.
- 14:03 **Anton Oparienko** (↳ 2026-10-13 14:00): Сейчас сравню с тем что у нас в репо я складывал по требованиям и запущу процесс тогда. Уточню еще пару моментов у тебя, когда до тулы дойду.

## 2026-10-14

- 12:47 **Aliaksandr Kavalchuk**: По дате старта:
  1. Сегодня получили контактное лицо для проекта (возможно будет ещё кто-то)
  2. Начали тред, представил Антона Опариенко в письме. Запросил слот на следующей неделе для знакомства.
  3. Теперь старт зависит от:
  3.1. нашей готовности
  3.2 вопроса SOW. Мы его пока не подписали, это будет одним из вопросов на звонке с контактным лицом, можем ли мы это решить на нашем уровне или же нужно будет вернуться на уровень Джабера и признать свою ошибку (что мы вовсе забыли про SOW).
  Антон и Миша должны сейчас дать план. Элайнимся. И начинаем.
