---
type: source
kind: rendering
date: 2026-05-06
original: https://chat.google.com/room/AAQAXooObiI
removed:
  - 0 bot messages, 0 task-system messages, 0 empty messages
  - money amounts, rates, margin, discount and payment-split percentages, replaced in square brackets
  - Zoom meeting passwords, IDs and passcodes; e-mail addresses; user IDs in Drive links
  - reactions; blank lines inside messages
---

# 2025-11-25 Contract chat - rendering 2

Google Chat space "(Contract) Optimum Engineering Standards" (spaces/AAQAXooObiI), part 2 of 3: from 2026-05-06 08:08 UTC to 2026-06-30 15:13 UTC. Read on 2026-09-28; rendered by `pm/seed-ingest-scripts/chat2md.mjs` from the Chat tool's output. Every message in order: time in UTC, author, text verbatim (typos kept; blank lines inside a message dropped), links and attachments. "↳ YYYY-MM-DD HH:MM" marks a reply in the thread started by the message of that time, which may be in another part. Money amounts, credentials and e-mail addresses are replaced in square brackets. Where an attachment is stored in the KB, its rendering is named. Never edited after storing.

## 2026-05-06

- 08:08 **Lizaveta Shauchenka**: Привет, клиент вернулся с правками в контракте и предлагают встречу для обсуждения завтра (7 мая) в 11 РБ
  @Marina Zaretskaya @Andrey Polovinkin @Alex Petrushkevich Вы можете?
  Сов: UPD Optimum Software Development Services Contract 06May2026 (2).docx 
  "I hope you are doing well, and thank you for your continued follow-ups.
  Please accept our apologies for the delay in getting back to you. We truly appreciate your patience.
  Dr. Yehya would like to arrange a meeting to discuss the scope of work in detail. I have attached the revised contract for your review ahead of the meeting. The discussion will primarily focus on the SOW as well as the amendments made to the contract.
  I have also added Dr. Yehya to this email thread for direct coordination.
  We would like to propose a meeting via Zoom on Thursday, May 7, 2026, at 11:00 AM (KSA time). Please let us know if this time works for you, or if you would prefer an alternative.
  Should you have any questions or require any clarification in advance, please feel free to reach out".
  - Link: https://docs.google.com/document/d/1rchgWbBdNEDVgvubIK7_uihtH-y-VI5m/edit
  - Attachment: UPD Optimum Software Development Services Contract 06May2026 (2).docx (in the chat) - a contract draft, listed in [[2026-09-07 Final contract - overview]]
- 08:09 **Marina Zaretskaya** (↳ 2026-05-06 08:08): я смогу
- 08:10 **Tanya Pinchuk** (↳ 2026-05-06 08:08): привет, если что, Андрей работал в компании до 30 апреля
  если понадобится помощь по ревью контракта, пингуйте либо @Yauheni Krasner либо меня
- 08:12 **Lizaveta Shauchenka** (↳ 2026-05-06 08:08): @Yauheni Krasner и тут привет)
  тогда на звонок можешь опшнл, главное Марина, чтобы была, и Леша
- 09:08 **Lizaveta Shauchenka** (↳ 2026-05-06 08:08): Внутренний синк поставила нам на 4.30 рб @Yauheni Krasner @Marina Zaretskaya
- 11:30 **Lizaveta Shauchenka** (↳ 2026-05-06 08:08): Встреча завтра в 12 рб
  Kindly find the details for the Zoom meeting below.
  Time: May 7, 2026 12:00 PM Riyadh
  Join Zoom Meeting
  [Zoom link removed: it carries the meeting password]
  Meeting chat link
  [Zoom chat link removed]
  Meeting ID: [removed]
  Passcode: [removed]
- 14:20 **Tanya Pinchuk**: @Marina Zaretskaya @Lizaveta Shauchenka а можете сориентировать пожалуйста, вы запускать проект тут сами планировали или нужен будет РМ от РМО? 
  если нужен будет, то нам нужно показать контракт еще нашему новому руководителю
- 14:38 **Marina Zaretskaya**: у нас ПМ заложен в бюджете на всю продолжительность проекта
- 14:38 **Tanya Pinchuk** (↳ 2026-05-06 14:38): ок, тогда сориентируем ресурсную, чтобы запланировали  от нас РМа
- 14:50 **Marina Zaretskaya**: @Tanya Pinchuk нужен ПМ, потому что нет смысла идти завтра на колл с клиентом, а отношения уже оч накаленные и от нас ожидают алаймента
- 14:53 **Yauheni Krasner**: Всем привет!
  Сделал ревью документов:
  Frame: Software Development Services Contract 10/03.docx 
  SOW: SOW Optimum 11.03.docx 
  Ниже основные риски, которые стоит обсудить до подписания.
  1. Очень верхнеуровневый scope и deliverables при модели TM + CAP (по сути близко к FP). 
  В контракте deliverables описаны слишком абстрактно, например: “Web application: implemented dashboard” и “Desktop application: implemented calculations”.
  Это создает высокий риск для нас, так как клиент сможет трактовать scope значительно шире фактической оценки и ожидать дополнительный функционал внутри текущего бюджета.
  2. Слишком широкая обязанность бесплатно исправлять дефекты.
  Сейчас формулировки обязывают нас исправлять дефекты без нормальных ограничений:
  не определен warranty/support period;
  не зафиксировано, что Minor/Trivial defects не блокируют acceptance.
  Риск: бесконечный цикл бесплатных доработок и поддержки.
  3. Противоречие по 12 месяцам поддержки + сам факт поддержки, длинной в год.
  В одном разделе указано, что 12 месяцев поддержки уже включены после запуска.
  В другом разделе написано, что support/support terms должны регулироваться отдельным соглашением. 12 месяцев бесплатной поддержки уже входят в стоимость проекта.
  4. Discovery заявлен как этап уточнения требований и архитектуры, однако Development уже заранее зафиксирован как обязательный scope, при этом общий CAP уже установлен.
  Мы идем в проект с Фиксированным скоупом и бюджетом без предварительной дискавери (будет выполнена внутри проекта), при этом проектная часть описана хай-левел.
  Это создает риск того, что клиент будет ожидать выполнение полного development scope в рамках первоначального cap даже после изменения/уточнения требований.
  FYI @Alexey Gamanovich
  - Links: https://docs.google.com/document/d/1p18R8CVGVwnJljDiE39Lr5uC1BPwvzxE/edit · https://docs.google.com/document/d/1Cwg4e70_cwlON4zdIq4zmhEZCmTeVfoQ/edit
  - Attachment: Software Development Services Contract 10/03.docx (in the chat) - a contract draft, listed in [[2026-09-07 Final contract - overview]]
  - Attachment: SOW Optimum 11.03.docx (in the chat) - an SOW draft, listed in [[2026-09-07 Final contract - overview]]
- 14:55 **Yauheni Krasner**: @Marina Zaretskaya, на звонке ты говорила, что был аппрув от менеджмента на старт проекта, с учетом больших  рисков. Можешь плиз дать ссылку на сообщение, где был аппрув.
- 14:55 **Yauheni Krasner**: @Marina Zaretskaya, @Lizaveta Shauchenka, подскажите также, кто будет DM на этом проекте
- 14:57 **Tanya Pinchuk** (↳ 2026-05-06 14:50): вы хотите, чтобы РМ уже завтра был на звонке или я не так поняла может? 
  в целом я подсветила уже Яне, что тут планируется старт
- 15:01 **Marina Zaretskaya** (↳ 2026-05-06 14:50): здесь еще нет подписанного контракта, пожтому старт планировать рановато вроде как
  нам нужен кто-то со стороны ПМО (раньше был Половинкин+Лаврисюк) для решения вопросов, относящихся к стадии подписания контракта
- 15:08 **Tanya Pinchuk** (↳ 2026-05-06 14:50): Андрей входил в контрактную группу РМО - а я ее возглавляю, сейчас назначила Женю для ревью - он уже риски описал
  сейчас я передала это также нашему новому руководителю, Алексею, с учетом рисков, обозначенных Женей
  если можешь поделиться апрувом от Игоря Медюхи, о котором говорили я так понимаю, то поделитесь , пожалуйста (Contract) Optimum Engineering Standards 
  если что, не препятствуем старту, просто наша обязанность как контрактной группы подсвечивать риски, что мы сейчас и сделали. Понимаю, что проект может быть потенциально для нас интересным за счет домена, это тоже подсветила
  - Link: https://chat.google.com/room/AAQAXooObiI/HPly2Dl2TiM/HPly2Dl2TiM?cls=10
- 15:32 **Marina Zaretskaya** (↳ 2026-05-06 14:50): Аппрув был в ноябре.
  С учетом времени прошедшего с момента этого согласования, реструктуризацию в компании, занятость сейлз менеджера, замену сотрудников со стороны PMO, которые были вовлечены в процесс подготовки и обсуждения условий контракта, недовольство клиента, серию итераций контракта, а также по результату сегодняшенего обсуждения стало очевидным, что необходимо определить здесь лиц,  принимающих решение о том, что мы берем этот проет (повторное согласование) и тех, кто пойдет на колл с клиентом говорить предметно.
  Мит , предложенный клиентом, завтра нужно отменять, потому что идти туда без подготовки - мы просто 100% потеряем этот контракт при том сколько сил и времени уже вложено.
  С формальной точки зрения, Ангелина (принмала обсуждение в кастомной версии предудущей итерации и рисков), уже не хэд деливери, я не могу брать ответственность - я уже  не хэд практики (но там к слову и вопросы не по тех скоупу), реакт разработчик со знанием арабского помогал на прошлом мите с коммуникацией, но он никак не относился к пресейл активности и не его долж обязанность этот контракт ранить, ПМ новый не в курсе происходящего - что очевидно - за час не разберешбся что тут происходило и как - не отсмотришь все артефакты,  ассистента сейлз менеджера мы тоже не можем считать тут ответственным за все. 
  Поэтому мы решили на звонке что @Lizaveta Shauchenka, отпишется в чате отдельно по этому вопросу и тегнет менеджмент для решения вопроса.
  - Attachment: image.png (in the chat)
- 16:09 **Lizaveta Shauchenka**: @Michael Labutin Привет.
  В связи с недавними изменениями в команде (уход ПМ, который вел проект, и изменение роли @Marina Zaretskaya , которая теперь не является DM), хотели бы уточнить актуальную структуру ответственности по данному контракту.
  Просьба подтвердить, кто сейчас будет выступать ответственным за delivery по проекту, а также кто со стороны PMO будет курировать рассмотрение и согласование данного контракта.
  Также, с учетом того, что контракт изменился в процессе последних итераций, просим подтвердить, что с нашей стороны сохраняется намерение продолжать работу по данному проекту и выходить на подписание договора.
- 19:51 **Michael Labutin**: @Alexey Gamanovich @Lizaveta Loseva
- 19:56 **Alexey Gamanovich**: привет, 
  1) контракт уже посмотрела контрактная группа (выше выжимка от Жени указана). 
  2) я только завтра начну погружаться в этот кейс, но уже видны "красные флажки" получить еще один похожий на Lotus проект, если не перепровериться/внести изменения. 
  3) по поводу выделения PM-а, пока не смотрели, нужно сначала разобраться с чем имеем дело

## 2026-05-07

- 06:22 **Tanya Pinchuk** (↳ 2026-05-06 16:09): привет, отвечая на твой вопрос по курированию контракта -  со стороны РМО ревью сделал и будет продложать коммуникацию@Yauheni Krasner
- 06:39 **Tanya Pinchuk** (↳ 2026-03-06 13:53): For Financial plan 
  @Lizaveta Shauchenka @Marina Zaretskaya подскажите, пожалуйста, это финальная версия расчетов наших? 
  если да, то есть пару вопросов наверное 
  есть ли где-то указанные рейты в таблице  (для клиента и для нас, если отличаются суммы) или есть отдельная может?
  заложен ли риск на уточнение требований после дискавери? 
  входит ли 12 месячный саппорт в эти часы и кэп?
  если после дискавери эффорт увеличится, есть ли механизм остановки/переоценки доп бюджета? 
   пока, если я правильно поняла, то при кэпе [amount removed] мы будем работать по средней ставке [rate removed], верно? 
  в общем, хочу понять, чтобы было на что опираться, может где-то еще есть экономика подсчитанная с примерной маржой, а не только распределение по ролям? 
  @Yauheni Krasner CC
  - Link: https://docs.google.com/spreadsheets/d/1dKqzASeychscrSDlKlQSFQj6Mv_ubi31nGmAi4XrstA/edit?gid=0#gid=0
  - Attachment: For Financial plan (Google Sheet)
- 08:35 **Lizaveta Shauchenka** (↳ 2026-03-06 13:53): Вот финансовый план, отправленный клиенту
  - Attachment: Financial plan - Optimum Engineering (1).xlsx (in the chat) - [[2026-03-11 Financial plan sent to the client - rendering]]
- 08:38 **Marina Zaretskaya** (↳ 2026-03-06 13:53): есть ли где-то указанные рейты в таблице  (для клиента и для нас, если отличаются суммы) или есть отдельная может?
  Первый пропоузал с рейтами до того, как клиент назвал свои ожидания
  - Attachment: image.png (in the chat)
- 08:40 **Marina Zaretskaya** (↳ 2026-03-06 13:53): есть ли где-то указанные рейты в таблице  (для клиента и для нас, если отличаются суммы) или есть отдельная может?
  Фмнальная итерация с дисконтом
  - Attachment: image.png (in the chat)
- 08:41 **Marina Zaretskaya** (↳ 2026-03-06 13:53): заложен ли риск на уточнение требований после дискавери? 
  мы считали изначально все по максам, в том числе P&L.
- 08:43 **Marina Zaretskaya** (↳ 2026-03-06 13:53):  пока, если я правильно поняла, то при кэпе [amount removed] мы будем работать по средней ставке [rate removed], верно? 
  [rate removed] @Yana Hotuleva прошу тут подтвердить
- 08:44 **Marina Zaretskaya** (↳ 2026-03-06 13:53): в общем, хочу понять, чтобы было на что опираться, может где-то еще есть экономика подсчитанная с примерной маржой, а не только распределение по ролям? 
  @Yana Hotuleva 
  Из того, что  вижу в P&L прибыль [amount removed]
- 08:50 **Marina Zaretskaya** (↳ 2026-03-06 13:53): входит ли 12 месячный саппорт в эти часы и кэп?
  согласно SoW , Assumptions and Constraints
  The Contractor is committed to support and maintenance services for twelve (12) months after system launch. Support and maintenance services shall be governed exclusively by a separate Service Level Agreement (‘SLA’). All terms and conditions relating to scope, service levels, costs, support structure, and associated obligations shall be set forth in the SLA and are expressly excluded from the scope of this Agreement.
- 09:08 **Yana Hotuleva** (↳ 2026-03-06 13:53): @Marina Zaretskaya Привет, мы считали P&L ещё осенью 2025 года, используя накладные расходы за 2025 год, поэтому на те цифры сейчас уже опираться нельзя. В чат economy могу отправить актуальный template с накладными 2026 года лучше считать уже от него и с новыми вводными.
- 09:12 **Matvey Matveev** (↳ 2026-03-06 13:53): Какая итоговая сумма часов будет в контракте? 
  Хотим может сначала предложить ему купить Дискавери и сказать, что он потом будет включен в основной проект
- 09:12 **Marina Zaretskaya** (↳ 2026-03-06 13:53): 4901
- 09:13 **Matvey Matveev** (↳ 2026-03-06 13:53): Какого числа высылали клиенту итоговый бюджет
- 09:13 **Matvey Matveev** (↳ 2026-03-06 13:53): А чего в 3 итерации 3803
- 09:13 **Marina Zaretskaya** (↳ 2026-03-06 13:53): @Lizaveta Shauchenka @Anton Snotov
- 09:14 **Marina Zaretskaya** (↳ 2026-03-06 13:53): потому что клиент демпинговал, когда мы показали первый раз пропоузал - он сразу сказал, что это оч дорого, мы сначала урезали часть функционала во 2 итерации, а в третьей (когда он сообщил свой макс) начали считать экономику и просить согласрвания - после чего показали бюджет со скидкой
- 09:15 **Matvey Matveev** (↳ 2026-03-06 13:53): Так мы тогда и в контракте должны указать 3803 и сделать по ним)
- 09:16 **Lizaveta Shauchenka** (↳ 2026-03-06 13:53): Финансовый план высылали 11 марта
- 09:18 **Marina Zaretskaya** (↳ 2026-03-06 13:53): Мы за 3808 вряд ли сделаем такой проект - 3800 это по самой мин оценке
- 09:19 **Matvey Matveev** (↳ 2026-03-06 13:53): Давайте тогда считать экономику по Максам и давайте прикинем, за сколько мы сделаем в среднем  проект
- 12:23 **Tanya Pinchuk** (↳ 2026-03-06 13:53): @Marina Zaretskaya @Lizaveta Shauchenka а подскажите, пожалуйста, кто по итогу ответственный дальше за подготовку? 
  Кто-то взял в работу экономику
- 12:25 **Marina Zaretskaya** (↳ 2026-03-06 13:53): Насчет формально ответственного (деливери менеджмент) не отписались нам. Пока я Яне часы для расчета экономики передала
- 14:28 **Matvey Matveev** (↳ 2026-03-06 13:53): когда пересчитаем пнл
- 14:29 **Matvey Matveev** (↳ 2026-05-06 19:51): правильно ли я понимаю, что Алексей - ДМ запроса
- 14:29 **Marina Zaretskaya** (↳ 2026-03-06 13:53): ждем Яну, она считает
- 14:30 **Matvey Matveev** (↳ 2026-05-06 19:51): @Michael Labutin
- 14:30 **Matvey Matveev** (↳ 2026-03-06 13:53): я понимаю, я же специально на ее сообщение отвечаю
- 14:35 **Tanya Pinchuk** (↳ 2026-05-06 19:51): Если так, то нам нужно будет с самого начала погрузиться и  все разобрать ещё раз, чтобы точно понимать текущую ситуацию по проекту
- 14:44 **Michael Labutin** (↳ 2026-05-06 19:51): руководитель ПМО который решит кто то тут главный
- 14:45 **Matvey Matveev** (↳ 2026-05-06 19:56): Привет, Алексей!
  Было время погрузиться и собрать первичную инфу?
  Есть понимание, кто будет ДМ и ПМ
- 14:45 **Matvey Matveev** (↳ 2026-05-06 19:51): ДМ тоже он назначит
- 14:48 **Michael Labutin** (↳ 2026-05-06 19:51): да, но скорее всгео глянет сам. Тут огромный риск контракта как Лотус
- 14:48 **Michael Labutin** (↳ 2026-05-06 19:51): @Vitaly Medyuha @Ivan Shatuho fyi
- 14:52 **Matvey Matveev** (↳ 2026-05-06 19:51): ок, сильно ждем фидбек
  и тогда расклад, при котором мы готовы стартануть
- 14:58 **Michael Labutin** (↳ 2026-05-06 19:51): да, Алексей, даст у него тут таких чатов уже очень много по этому доходит чуть медленнее
- 15:11 **Lizaveta Loseva** (↳ 2026-05-06 19:56): Как человек, который изучал контракт Lotus, в дополнение к Тому, что написал выше @Yauheni Krasner  
  Если посмотреть основную формы договора, то там сказано о том что все работы должны быть выполнены в течение заданного периода времени согласно этого контракта, по истечении которого мы должны будем деньги клиенту, то есть эта история про пеню. 
  Каждый блок работ, каждая фаза имеет строгое ограничение месяц, да там есть пункт говорящий о том, что можно увеличить время работы и таймлайн может быть изменён, но мы никогда не комитимся под длительность каждого конкретного этапа и вообще под жестокие сроки не зная реальный скоп(и это не ТМ). В SOW уже заявленна длительность проекта шесть месяцев, наша исполнительность должна соответствовать выполнению работ по каждой из шести фаз. 
  Результат работы НЕ очевиден. Очень похоже на лотус. Бюджет достаточно небольшой если разложить на 6 месяцев. 
  Нет никаких требований по перформансу, но при этом система ожидается скейлабл.
  - Attachment: Image_20260507_171118_784.jpeg (in the chat)
  - Attachment: Image_20260507_171118_752.jpeg (in the chat)
- 15:11 **Lizaveta Loseva** (↳ 2026-05-06 19:56): @Yauheni Krasner не совсем понимаю что нас защищает по договору и как выйти из него если что
- 15:11 **Alexey Gamanovich** (↳ 2026-05-06 19:56): Начал смотреть ....
- 15:13 **Tanya Pinchuk** (↳ 2026-05-06 19:56): Так а нас там мало что защищает в целом
- 15:19 **Lizaveta Loseva** (↳ 2026-05-06 19:56): Значит верно поняла. Там нет ограничений для клиента. Это действительно очень похоже на Лотус по условиям.
- 15:24 **Tanya Pinchuk** (↳ 2026-05-06 19:56): По факту похоже на кабальную сделку в целом, но для чистоты эксперимента нужно наверное вбс проанализировать, экономику посмотреть и тд 
  Но в целом ты все верно пишешь
- 17:33 **Alexey Gamanovich**: Коллеги, квинт-эссенция этого контракта (MSA ... он же "Frame") в том что Innowise обязуется:
  сделать  за 6 календарных месяцев, то что еще не определено де-факто ... что-то что будет опредяляться до конца только в Discovery Phase, кот. также входить в эти же 6 месяцев;
  стоимость строго зафиксирована и не может быть превышена. CR-ы не меняют этой картинки, потому что де-факто нет опредления что входит в изначальный scope. По-сути, это определяется субъективным мнением клиента, что считается начальным scope;
  CR-ы накладывают обязательство пересчитать команду IRON TRIANGLE в течении 5 дней. Клиент при этом ничем не ограничен (хоть каждый день может закидывать CR-ами);
  это что-то - "high quality computer software with ready-to-operate deliverables and distinguished performance" ... 
  это что-то должно соответсвовать ВСЕМ законам KSA, и ВСЕМ стандартам software development, cybersecurity, data compliance (пункт 6.5) ... штраф только за PDPL [amount removed] за первый раз, потом удваиваится;
  выход за пределы 6 месяцев может влечь за собой пенальти для исполнителя (пункт 6.3)
  defects, fully obligated to correct & maintain them at no additional costs (пункт 6.2);
  компенсировать "any losses" (пункт 6.10)
  may  not use any open-source code (пункт 8.3)
  нет выхода из контракта (пункт 11.2 подпункт 4) ... по-сути с согласия клиента, кот. может "чаржить" пенальти
  ...  и еще много чего там есть, что опускаю для краткости.
  Выводы: 
  1) этот контракт НЕЛЬЗЯ подписывать в том виде в кот. он есть сейчас; даже не погружаясь в SOW (там тоже неисполнимые обязательства) и в WBS;
  2) cудя по поверхностному описанию deliverables согласование деталей может занять очень много времени, например, функционалы на UI, как offline изменения будут синхронизироваться с online сервисом.
- 17:34 **Alexey Gamanovich**: @Michael Labutin , краткое саммари как обсудили
- 17:35 **Alexey Gamanovich**: проект в PMO в данном виде стартовать не можем
- 17:41 **Michael Labutin**: @Alexey Gamanovich предлагайте правки
- 17:43 **Alexey Gamanovich**: что здесь со сроками, надо разбирать в чем приложение, чтобы предложить опции если клиент уже настроен на 6 месяцев и определенную сумму
- 17:46 **Michael Labutin**: @Marina Zaretskaya
- 17:46 **Michael Labutin**: Была ДМом и имеет весь контексь
- 17:48 **Alexey Gamanovich**: @Marina Zaretskaya , забрось пож. нам митинг на завтра (вечер в моем календаре пока свободен ... пока что)
- 17:49 **Alexey Gamanovich**: заранее спасибо
- 23:34 **Aliaksei Tsitou**: Закинул на троих на вечер в единственный свободный слот

## 2026-05-08

- 13:30 **Pavel Martysuk** (↳ 2026-05-07 17:33): @Alexey Gamanovich @Lizaveta Loseva Тут пообщался с @Alex Havansky .  Леша помогал делать прототип на этот запрос и помнит его. Леша сказал, что в  целом в эти часы можно влезть, недоценка чуток есть на админку. Но с таким контрактом лучше сюда не идти. Только если с нашим или через дискавери, а потом такой контракт
- 15:33 **Marina Zaretskaya**: @Alexey Gamanovich 
  WBS https://docs.google.com/spreadsheets/d/10H7vDQCbev_-jC6y0J5zeCw1Os2n-6MfJiAVb0k2hbg/edit?gid=572873180#gid=572873180
  Solution architect's artefact https://docs.google.com/document/d/1Iw685h0d8EJ2NCetSxWNEXei46ggl20hZ8KSpiVv_RM/edit?usp=sharing
  Proposal Леша Титов пошарил (в тч с итерациями) https://docs.google.com/presentation/d/10-oqb8y1x7Eq-4Ami6uAZCGwxC5gJuXlbdg-M2T9ges/edit?usp=sharing
  Request: 
  5)EST - Optimum Engineering Standards - ASnot - SA - Big data - 023690
  Energy, Oil & Gas
  Planned Project Budget [amount removed]
  Proposal Deadline 4.11.2025
  Запрос лида:
  We are a Saudi-based company specializing in mud engineering services for the oil and gas sector. We’re looking to develop a custom software solution that enables real-time monitoring of drilling fluid properties, supports data collection for future analysis, and includes simulation capabilities for planning and risk mitigation. The solution should feature an intuitive user interface, robust database management, and mobile app integration. We’re keen to discuss how your team can support us in bringing this project to life.
  - Attachment: v1 EST - Optimum Engineering Standards - ASnot - SA - Big data - 023690 (Google Sheet) - [[2026-09-25 v1 WBS - rendering]]
  - Attachment: T1 - EST - Optimum Engineering Standards - ASnot - SA - Big data - 023690 (Google Doc) - [[2025-10-24 Presale architecture - rendering]]
  - Attachment: Proposal from Innowise - Optimum Engineering Standards (Google Slides) - [[2025-11-05 Proposal slides - rendering]]

## 2026-05-11

- 09:42 **Lizaveta Shauchenka** (↳ 2026-05-07 23:34): Привет
  Расскажите, плиз, о чем договорилсь? @Aliaksei Tsitou
- 10:11 **Aliaksei Tsitou** (↳ 2026-05-07 23:34): Привет. Сегодня в 15 по рб будет раунд 2, докинул тебя на всяк случай
- 12:30 **Yauheni Krasner**: Всем привет!
  @Lizaveta Shauchenka @Marina Zaretskaya, можете зафиксировать плиз последние версии Frame и SOW по этому контракту.
- 12:58 **Yauheni Krasner** (↳ 2026-05-11 12:30): прикрепить ссылки в этом треде
- 13:04 **Lizaveta Shauchenka** (↳ 2026-05-11 12:30): Привет!
  Contract: ​ UPD Optimum Software Development Services Contract 06May2026 (2) (1).docx 
  Сов:  UPD SOW Optimum 10.04 (3).docx
  - Links: https://docs.google.com/document/d/1fBAOf_2-qAy-mv9FfDrvkSfRZlT-S5LZ/edit · https://docs.google.com/document/d/1A__Ddn5_SD1NUYcF_wQYFgZ45zMy_Lnp/edit?usp=drive_web&rtpof=true
  - Attachment: UPD Optimum Software Development Services Contract 06May2026 (2) (1).docx (in the chat) - a contract draft, listed in [[2026-09-07 Final contract - overview]]
  - Attachment: UPD SOW Optimum 10.04 (3).docx (in the chat) - an SOW draft, listed in [[2026-09-07 Final contract - overview]]
- 14:00 **Yauheni Krasner** (↳ 2026-05-11 12:30): SOW не открывается. 
  а во фрейме, можно саджестинги принимать
- 14:39 **Lizaveta Shauchenka** (↳ 2026-05-11 12:30): что-то с файлом, у меня тоже не открывает 
  вот ворд
  саджестинг лучше оставить, чтобы было понятно, что еще не согласовано
  - Attachment: UPD SOW Optimum 10.4.docx (in the chat) - the SOW v10.4 document, [[2026-06-15 SOW v10.4 - rendering]]

## 2026-05-12

- 07:35 **Yauheni Krasner** (↳ 2026-05-11 12:30): @Lizaveta Shauchenka, можете загрузить SOW в гугл докс плиз
- 07:44 **Yauheni Krasner**: Всем привет!
  Начинаю ревью рамочного договора со стороны PMO.
  @Lizaveta Shauchenka, также жду от тебя рабочую ссылку с последней актуальной версией SOW.
  Контракт на  проект рассматриваем как TM + CAP, где CAP - это, исключительно, верхняя граница бюджета клиента, за которой мы будем следить и сообщим заранее, в случае ее приближения.
  Под кэпом не подразумевается, какой-то определенный скоуп и конкретные деливераблс. Никакого коммитмента с нашей стороны в этом контракте не будет, кроме как какой-то initial scope, в котором мы будем уверены на 100%. 
  В ином случае, нам нужно расписывать детально проектную часть и требования.
- 08:09 **Lizaveta Shauchenka** (↳ 2026-05-11 12:30): ранее грузили, он выдает ошибку при открытии через гугл док
- 08:10 **Lizaveta Shauchenka** (↳ 2026-05-11 12:30): пока пробуем еще
- 09:22 **Yauheni Krasner** (↳ 2026-05-11 12:30): получилось что-нибудь
- 09:46 **Yauheni Krasner** (↳ 2026-05-12 07:44): Рассмотрел Frame: Copy of UPD Optimum Software Development Services Contract 06May2026 (2) (1).docx 
  Что было добавлено: 
  Классификация багов и правила их приемки
  Описание процедуры приемки
  Пункт о Deemed Acceptance
  Добавил несколько комментариев про сомнительные пункт о дефектах. 
  Также добавил вопрос по фазе дискавери проекта. @Arseniy Klimenko, помоги тут плиз. Я тебя тегнул. 
  @Alex Petrushkevich, можешь плиз посмотреть со своей стороны. Возможно есть какие-то пункты из нашего шаблона, которые было бы неплохо добавить в клиентскую версию.
  - Link: https://docs.google.com/document/d/1rSVdsd3ASB_Jmz5nqNfPKZitSTFfWpq8/edit
  - Attachment: Copy of UPD Optimum Software Development Services Contract 06May2026 (2) (1).docx (in the chat) - a contract draft, listed in [[2026-09-07 Final contract - overview]]
- 09:48 **Lizaveta Shauchenka** (↳ 2026-05-11 12:30): SOW: UPD SOW Optimum 10.4
  - Link: https://docs.google.com/document/d/1bzY2oTz7nEbwalBQXC3dAPhmzVPRzZL2pf7iEAVG6-g/edit?tab=t.0 - [[2026-06-15 SOW v10.4 - rendering]]
  - Attachment: UPD SOW Optimum 10.4  (Google Doc) - the SOW v10.4 document, [[2026-06-15 SOW v10.4 - rendering]]
- 13:20 **Lizaveta Shauchenka** (↳ 2026-05-11 12:30): @Yauheni Krasner открывается у тебя сов
- 13:22 **Yauheni Krasner** (↳ 2026-05-11 12:30): да, все гуд

## 2026-05-13

- 13:11 **Yauheni Krasner**: Привет!
  Текущий апдейт: 
  Мы с @Alex Petrushkevichсделали ревью клиентского SOW. Он готов.
  Сейчас @Arseniy Klimenko готовит проектную часть. В течение завтрашнего дня / первой половины пятницы, мы подготовим SOW и сможем отправить клиенту на рассмотрение.
  FYI @Alexey Gamanovich @Lizaveta Shauchenka
- 13:29 **Lizaveta Shauchenka** (↳ 2026-05-13 13:11): Привет
  Подскажи, пожалуйста, в этой версии сова будут вноситься изменения?
  SOW: UPD SOW Optimum 10.4
  - Link: https://docs.google.com/document/d/1bzY2oTz7nEbwalBQXC3dAPhmzVPRzZL2pf7iEAVG6-g/edit?tab=t.0 - [[2026-06-15 SOW v10.4 - rendering]]
  - Attachment: UPD SOW Optimum 10.4  (Google Doc) - the SOW v10.4 document, [[2026-06-15 SOW v10.4 - rendering]]
- 13:32 **Yauheni Krasner** (↳ 2026-05-13 13:11): предлагаю взять наш шаблон и вносить изменения в него, т.к. вся проектная часть будет изменена
- 13:33 **Lizaveta Shauchenka** (↳ 2026-05-13 13:11): @Marina Zaretskaya Можете ли перенести звонок пятничный на понедельник после 13 по рб, плиз
- 13:34 **Lizaveta Shauchenka** (↳ 2026-05-13 13:11): а кто тогда будет переводить на арабский язык?
  клиенту важно сохранять их формат
- 13:35 **Yauheni Krasner** (↳ 2026-05-13 13:11): ну, нам в любом случае нужно будет переводить ее, т.к. проектная часть будет новая. 
  не знаю, кто будет. а кто до этого переводил
- 14:06 **Marina Zaretskaya** (↳ 2026-05-13 13:11): @Alexey Gamanovich может нам оставить пт как промежуточный статус чек-колл и назнаить тогда финальный с сейл на пн
- 14:09 **Alexey Gamanovich** (↳ 2026-05-13 13:11): я ок чтобы с сейлс в понедельник синкаться. в пятницу нужно "подбивать" результат
  по переводу, мы переводить на арабский не будем. сначала нужно понять готов ли клиент двигаться на этих условиях. если там выровнялись, то с переводом определимся позже (если у Innowise есть свое юр лицо на территории KSA)
- 14:20 **Lizaveta Shauchenka** (↳ 2026-05-13 13:11): сначала они сами все полностью, потом изменения вносились только на англ, они пожаловались на это. В последней итерации переводили мы, но как это по итогу выглядит юридически никто не может проверить
- 14:26 **Lizaveta Shauchenka** (↳ 2026-05-13 13:11): @Yauheni Krasner @Arseniy Klimenko дайте тогда, плиз, по готовности, ссылку на новый SOW
- 14:27 **Yauheni Krasner** (↳ 2026-05-13 13:11): да, конечно

## 2026-05-14

- 11:21 **Yauheni Krasner** (↳ 2026-03-06 13:53): Всем привет!
  @Yana Hotuleva, подскажи, а мы считали тут экономику проекта
- 11:24 **Yana Hotuleva** (↳ 2026-03-06 13:53): Привет, да, добавила тебя в группу
- 13:20 **Lizaveta Shauchenka** (↳ 2026-05-13 13:11): @Marina Zaretskaya договорились сегодня с Алексеем, что пятничный колл как промежуточный убираем и оставим только в пн
  отмени, плиз, пт мит

## 2026-05-15

- 07:04 **Yauheni Krasner**: Привет!
  Подготовлена новая версия SOW: UPD SOW Optimum 10.4  
  В документ были добавлены и доработаны ключевые ассампшены для TM + CAP модели, чтобы снизить риски для нас как исполнителя и избежать описанных выше рисков ((Contract) Optimum Engineering Standards ).
  Основные улучшения:
  зафиксировано, что оценка, сроки и CAP являются preliminary и могут быть пересмотрены после уточнения требований;
  добавлен полноценный механизм re-estimation и supplementary agreement при расхождении требований с первоначальными assumptions;
  закреплено, что requirements clarification является ongoing collaborative process и требует активного участия заказчика;
  добавлено право приостановки работ/termination при отсутствии обратной связи или невозможности согласовать требования;
  четко выделены out-of-scope items и ограничения MVP;
  зафиксировано, что support/SLA не входят в scope и оформляются отдельным соглашением;
  ограничена ответственность подрядчика за third-party systems, infrastructure, integrations, customer data и external dependencies;
  добавлены protections по change requests, acceptance process, infrastructure ownership и responsibility boundaries.
  Дополнительно были добавлены важные operational protections:
  право Contractor заменять специалистов на equivalent resources с предварительным уведомлением заказчика;
  обязанность Contractor самостоятельно проводить knowledge transfer за свой счет;
  travel costs, licenses и special hardware/software explicitly excluded from quoted fees;
  30-дневный notice period для снятия специалистов со стороны заказчика;
  защита against sudden roll-off: если заказчик не уведомляет заранее, затраты покрываются из Advance Payment;
  взаимное право termination for convenience с 30-дневным notice period.
  @Lizaveta Shauchenka, оставил для тебя несколько комментариев в документе.
  @Arseniy Klimenko, жду от тебя дополнения скоупа и деливераблс для каждой из фаз + апдейт по экономике проекта + также ревью документов от тебя, как от DM.
  FYI @Alexey Gamanovich
  - Links: https://docs.google.com/document/d/1bzY2oTz7nEbwalBQXC3dAPhmzVPRzZL2pf7iEAVG6-g/edit?tab=t.0 - [[2026-06-15 SOW v10.4 - rendering]] · https://chat.google.com/room/AAQAXooObiI/2HUIRam_i04/2HUIRam_i04?cls=10
  - Attachment: UPD SOW Optimum 10.4  (Google Doc) - the SOW v10.4 document, [[2026-06-15 SOW v10.4 - rendering]]
- 07:29 **Yauheni Krasner** (↳ 2026-05-15 07:04): @Anton Soshnikau, тут также Discovery внутри проекта. Важно чтобы ты посмотрел Deliverables проекта по части BA и оценку в целом.
- 09:32 **Anton Soshnikau** (↳ 2026-05-15 07:04): @Yauheni Krasner или кто-нибудь еще, дайте плиз больше контекста. Пресейл готовила практика (у меня нет чата такого пресейла)? Где можно посмотреть описание проекта и оценку дискавери и последующих фаз (проп что в этом чате и вбс не совпадают по оценкам)
- 14:13 **Yauheni Krasner** (↳ 2026-05-15 07:04): контекст можно уточнить у @Arseniy Klimenko. Он тут DM
- 14:16 **Yauheni Krasner** (↳ 2026-05-06 14:53): Дополнение к рискам со стороны разработки: T1 - EST - Optimum Engineering Standards - ASnot - SA - Big data - 023690 . 
  Выглядит как серьезная недооценка, причем не все задачи, которые нужно будет реализовать - учтены.
  FYI @Alexey Gamanovich @Arseniy Klimenko
  - Link: https://chat.google.com/room/AAQAMdfmWl4/KkJ9Ez1jSrk/PLi78-trVhc?cls=10 - the presale chat, [[2025-10-20 Presale chat - overview]]
- 14:20 **Yauheni Krasner** (↳ 2026-05-15 07:04): @Anton Soshnikau, @Arseniy Klimenko, поставил нам звонок на пн

## 2026-05-18

- 12:57 **Yauheni Krasner** (↳ 2026-05-15 07:04): @Arseniy Klimenko, добавил 3 новых ассампшена:
  разработка только для десктоп и веб
  не разрабатываем мобильное приложение
  адаптив не включен в скоуп
  посмотри плиз, все ли корректно
- 16:14 **Anton Soshnikau** (↳ 2026-05-15 07:04): обсудил с @Marina Zaretskaya и хочу подсветить еще один риск. БА эфорт оценен на мидл БА с пониманием логарифмических высчислений, и (ввиду пуша на попадание в бюджет заказчика) с немного занижеными часами на проработку математической части солюшена. по скромным подсчетам это примерно дифицит в 10% по БА эфорту 
  @Arseniy Klimenko @Yauheni Krasner  fyi

## 2026-05-20

- 15:27 **Lizaveta Shauchenka**: Привет.
  @Alexey Gamanovich @Yauheni Krasner @Marina Zaretskaya @Michael Labutin @Anton Snotov @Arseniy Klimenko 
  Текущий вариант с “предварительными договоренностями” и снятием с себя ответственности за ранее согласованный скоуп нерабочий. Клиент это воспримет как попытку откатить все назад без конкретики.
  До конца этой недели хотим получить от вас новую реальную оценку проекта, за которую delivery готов поручиться.
  Не Discovery ради Discovery, а именно оценка delivery.
  за какую сумму команда реально готова поручиться;
  с каким scope;
  с какими ограничениями и допущениями;
  что именно входит в ответственность delivery.
  Если нужны доп. встречи с клиентом для оценки -  сделаем; Discovery оставляем только как вторую опцию, основной сценарий - новая коммерческая оценка проекта.
  Также поставили встречу в календарь на пятницу в 14:00 РБ,  где нужно будет зафиксировать:
  что реально можем взять в delivery;
  какая новая оценка;
  какие данные еще нужны, если нужны вообще.
- 15:51 **Alexey Gamanovich** (↳ 2026-05-20 15:27): мне кажется мы пошли по кругу.
  1) в изначальном виде контракт = новый Lotus и иже с ним проблемы для компании -> предлагаем вариант в рамках кот. клиент с тем же бюджетом получает решение, но без невыполнимых условий и в колаборации с клиентом + сливаться намерений нет
  2) По деливери Арсений прошелся по задаче - там есть привязка к технологии кот в компании есть у 1 девелопера и нет понимания насколько хорошо владеет = bus factor -> предложение обсудить с клиентом альтернативу кот. есть в компании в виде большего кол-ва сотрудников и пониманием возможностей технологии
  3) там есть риски того что что-то пойдет не так (экосистема клиента, рекваременты до конца не проработаны), НО в рамках предложенного контракта это можно будет решать по мере движения проекта
  4) предлагать "новый" пропоузал не вижу смысла
  а) HealthCare практика уже с клиентом прорабатывала альтернативы и в ценовом диапозоне и по части функционала;
  b) криминала в оригинальной оценки не нашли;
  c) с учетом нашей версии контракта у PM-а есть возможность вести переговоры по срокам, скоупу, "глубине фич" и бюджету -> есть возможность "вытягивать" недооценки
- 15:55 **Alexey Gamanovich** (↳ 2026-05-20 15:27): что нужно - > вести переговоры по этим 2 ключевым пукнтам

## 2026-05-21

- 11:27 **Lizaveta Shauchenka** (↳ 2026-05-20 15:27): В этом и проблема, клиент не примет такой договоренности. Потому решили выйти к нему с фиксой, но на ту сумму, которая для нас удобна.
- 12:15 **Alexey Gamanovich** (↳ 2026-05-20 15:27): привет, 
  в пятницу на звонке будет Иван и Миша. я думаю там будет понятно что с этим делать дальше

## 2026-05-22

- 13:07 **Yauheni Krasner**: Краткое саммари ключевых договоренностей и дальнейших шагов:
  Контракт:
  Формат - fixed price с milestone-ами.
  Используем текущую версию контракта клиента, дорабатываем ее под свои условия.
  Технологии:
  Переходим с MAUI на Flutter (или другую кроссплатформу), чтобы снизить риски и упростить подбор команды.
  Проверяем, подходит ли Flutter под требования проекта.
  Экономика:
  Пересчитываем экономику под новую технологию. Важно добиться рентабельности не ниже [figure removed].
  При необходимости - поднять бюджет на [amount removed], обосновать клиенту.
  Требования:
  @Arseniy Klimenko подтвердил достаточность скоупа прописанного в SOW. Также получено подтверждение@Michael Labutin, что описание требований на основании WBS является достаточным для этого контракта. Мы готовы идти с ним в разработку.
  Все, что не в WBS — оформлять как Change Request.
  Перевод:
  Контракт и ключевые документы подготовить сразу на английском и арабском, привлечь профессионального переводчика со стороны юристов или DMO/GDO.
  Дедлайны:
  До среды (27.05) : финализировать технологию, экономику, проектную часть и драфт контракта.
  После - выйти на встречу с клиентом с обновленными документами.
  Ответственные:
  Контракт/Assumptions: @Arseniy Klimenko / @Yauheni Krasner 
  Технологии: @Arseniy Klimenko / @Marina Zaretskaya 
  Экономика: @Yauheni Krasner 
  Перевод: @Alex Petrushkevich 
  FYI @Alexey Gamanovich
- 13:28 **Alex Petrushkevich** (↳ 2026-05-22 13:07): Договоренность про перевод - гениальная
  Переводчика на арабский в юротделе нет, поэтому с арабским помочь не сможем
- 13:33 **Yauheni Krasner** (↳ 2026-05-22 13:07): есть еще выходные, чтобы подтянуть ))
- 15:17 **Lizaveta Shauchenka** (↳ 2026-05-22 13:07): @Yauheni Krasner По дедлайну - в среду (27.05) уже будет звонок с клиентом. Финальный внутренний звонок поставим на вторник вечером.

## 2026-05-25

- 08:29 **Yauheni Krasner** (↳ 2026-05-22 13:07): Всем привет!
  @Arseniy Klimenko, жду от тебя апдейт по возможности перехода на Flutter.
  После этого сможем с тобой пересчитать экономику.
- 13:53 **Arseniy Klimenko** (↳ 2026-05-22 13:07): Привет! Со своей стороны по флатеру даю апрув, у нас гораздо больше гибкости с флатеорм. Ребята даже чуть меньше насчитали. в районе 100 часов меньше. Я бы эти часы оставил все равно и не снижал бы цифру. Также ребята пересчитали и фронт на вебе в флатер, там тоже экономия получается, но это как опция. Можем созвониться и уже посмотреть детально и экономику подогнать
- 14:04 **Yauheni Krasner** (↳ 2026-05-22 13:07): Поставил нам звонок на завтра, чтобы подготовить все

## 2026-05-26

- 11:38 **Matvey Matveev**: @Vadim Borisov 
  вот тут перевод
  Языки:
  Английский и арабский 
  @Yauheni Krasner 
  Бета-версию нам пока внутри помогут перевести?
  Когда в теории понадобится финалить последнюю версию
- 12:01 **Yauheni Krasner** (↳ 2026-05-26 11:38): Привет!
  Пока договорились все вместе на звонке, что сначала сходим на несколько дополнительных звонков с клиентом, чтобы уточнить скоуп и требования, насколько это возможно. 
  После того, как сделаем это -> подготавливаем предложение клиенту и финализируем контракт и делаем перевод
  Сейчас драфт готов и его можно перевести, но не целесообразно, т.к. он может сильно поменяться. 
  @Matvey Matveev
- 12:40 **Vadim Borisov** (↳ 2026-05-26 11:38): @Yauheni Krasner Женя, что по срокам? Когда потребуется проф переводчик на контракт
- 12:41 **Yauheni Krasner** (↳ 2026-05-26 11:38): я бы сказал, что скорее во второй половине следующей недели
- 12:45 **Vadim Borisov** (↳ 2026-05-26 11:38): не уверен, но будем искать.
- 13:48 **Tanya Pinchuk** (↳ 2026-05-26 11:38): у нас вроде на воке были переводчики арабского, вдруг это чем-то поможет

## 2026-06-02

- 14:05 **Vadim Borisov** (↳ 2026-05-26 11:38): @all Коллеги, мы подобрали пару бюро переводов (английский <-> арабский) и уже в финальной стадии подписания договора с одним из бюро в Варшаве. 
  Матвей, подскажи только, чей мэйл с нашей сэйл стороны указывать как контактный для целей обсуждений переводов и коммуникации с бюро переводами? @Matvey Matveev

## 2026-06-03

- 11:28 **Matvey Matveev** (↳ 2026-05-26 11:38): Спасибо, Вадим!
  @Dana Kavalchuk @Lizaveta Shauchenka 
  предлагаю чей-то из ваших
- 11:29 **Dana Kavalchuk** (↳ 2026-05-26 11:38): Привет, давайте мой
- 11:51 **Vadim Borisov** (↳ 2026-05-26 11:38): Всем привет! 
  Мы уже подписали один договор, второй на подходе.
  Здесь в таблице собраны цены, условия и контакты где заказывать переводы.
  https://docs.google.com/spreadsheets/d/18nRKgEJGJsoeezjqrddwNzZpKSJcJLgMLl2PZhFxEgU/edit?gid=0#gid=0
  - Attachment: Информация о бюро переводов_Арабский - Английский_Варшава_03.06.26 (Google Sheet)
- 11:52 **Vadim Borisov** (↳ 2026-05-26 11:38): @Maksim Szpic Максим, обнови пожалуйста в договорах контактное лицо на @Dana Kavalchuk
- 12:04 **Maksim Szpic** (↳ 2026-05-26 11:38): @Vadim Borisov хорошо - сообщу им, что контактной стороны у нас будет @Dana Kavalchuk

## 2026-06-08

- 08:40 **Dana Kavalchuk**: Привет, клиент вышел на связь, буду просить слоты на завтра. Предположительно в 12 или в 4 СЕТ подходит? @Arseniy Klimenko @Yauheni Krasner @Alexey Gamanovich @Marina Zaretskaya @Alex Petrushkevich
- 08:49 **Marina Zaretskaya** (↳ 2026-06-08 08:40): я могу на 16:00 не успеть, если затянется предыдущий мит с клиентом, 12 - норм
- 08:59 **Yauheni Krasner** (↳ 2026-06-08 08:40): могу и так и так
- 11:27 **Dana Kavalchuk** (↳ 2026-06-08 08:40): подскажите, можем ли синк сегодня в 4.30 СЕТ? @Yauheni Krasner @Arseniy Klimenko @Alexey Gamanovich @Marina Zaretskaya @Alex Petrushkevich
- 11:28 **Yauheni Krasner** (↳ 2026-06-08 08:40): я могу
- 11:28 **Marina Zaretskaya** (↳ 2026-06-08 08:40): я нет, у меня мит по проекту
- 11:44 **Alexey Gamanovich** (↳ 2026-06-08 08:40): я пока перегружен
- 11:44 **Dana Kavalchuk** (↳ 2026-06-08 08:40): завтра перед звонком тогда поставлю

## 2026-06-09

- 08:30 **Yauheni Krasner** (↳ 2026-06-08 08:40): Привет!
  @Dana Kavalchuk, подскажи, а сегодня будет звонок
- 08:37 **Dana Kavalchuk** (↳ 2026-06-08 08:40): @Yauheni Krasner Привет,мне так и не ответили по времени, так что видимо нет
- 09:58 **Dana Kavalchuk** (↳ 2026-06-08 08:40): Привет, @Arseniy Klimenko @Yauheni Krasner @Alexey Gamanovich @Marina Zaretskaya @Alex Petrushkevich Would Wednesday, 10 June 2026, at 2:00 PM (KSA time) be convenient for you and your team? Please confirm if this date and time work for you so that we can send the meeting invitation. The meeting will be conducted via Zoom.
  In preparation for the meeting, we kindly request that you provide the meeting agenda and the list of participants by the end of today, given the importance of the discussion and to allow sufficient time for preparation.
  Additionally, we would appreciate it if a technical translator could be included in the meeting.
  Время подтверждаю? И может есть дополнения к агенде? To discuss the updates and proposed adjustments regarding the contract
- 11:23 **Maksim Szpic** (↳ 2026-05-26 11:38): @Matvey Matveev @Dana Kavalchuk привет!
  Сообщаю, что сегодня мы подписали уже и договор со вторым бюро переводов (арабский - английский). Внес соответствующие изменения в таблицу со всей информацией для вас и для выбора на заказ перевода.
  P.S. Теперь у нас есть два договора с двумя фирмами на переводы (арабский - англ). Вы уже можете выбирать по условиям и срокам, которое вам больше подходит и контактировать с ними напрямую. Вся для этого информация указана в таблице.
- 13:14 **Dana Kavalchuk** (↳ 2026-06-08 08:40): по просьбе Джони поставила синк сегодня, ему нужно больше времени, чтобы разобраться. Подключитесь, пожалуйста, 5.15 СЕТ @Alexey Gamanovich @Arseniy Klimenko @Yauheni Krasner @Marina Zaretskaya @Alex Petrushkevich

## 2026-06-10

- 11:00 **Dana Kavalchuk**: call 10/06
- 11:02 **Dana Kavalchuk** (↳ 2026-06-10 11:00): @Yauheni Krasner @Arseniy Klimenko @Anton Snotov @Johni Algarbi @Marina Zaretskaya @Alex Petrushkevich
- 11:03 **Dana Kavalchuk** (↳ 2026-06-10 11:00): тут коммуникация по звонку
- 11:04 **Yauheni Krasner** (↳ 2026-06-10 11:00): он ругается?)
- 11:09 **Dana Kavalchuk** (↳ 2026-06-10 11:00): не могу шарить
- 11:09 **Dana Kavalchuk** (↳ 2026-06-10 11:00): доступа нет
- 11:10 **Alex Petrushkevich** (↳ 2026-06-10 11:00): тоже нет доступа
- 11:10 **Johni Algarbi** (↳ 2026-06-10 11:00): one moment
- 11:21 **Johni Algarbi** (↳ 2026-06-10 11:00): Обновление контракта сделано на основании того, что клиент нам отправил в мае
- 11:27 **Yauheni Krasner** (↳ 2026-06-10 11:00): @Dana Kavalchuk @Anton Snotov @Marina Zaretskaya , подскажите плиз
- 11:28 **Dana Kavalchuk** (↳ 2026-06-10 11:00): насколько я знаю, да
- 11:28 **Dana Kavalchuk** (↳ 2026-06-10 11:00): мы редактировали их версию
- 11:31 **Marina Zaretskaya** (↳ 2026-06-10 11:00): я не принимала участие в последней итерации
- 11:49 **Marina Zaretskaya** (↳ 2026-06-10 11:00): а депозит сохранятсся
- 11:52 **Marina Zaretskaya** (↳ 2026-06-10 11:00): инвойсы должны выставляться каждый месяц
- 11:52 **Marina Zaretskaya** (↳ 2026-06-10 11:00): это нам говорили финансисты
- 11:54 **Marina Zaretskaya** (↳ 2026-06-10 11:00): мы не можем гарантировать сейчас что 1 майлстоун равен 1 месяцк
- 11:57 **Dana Kavalchuk** (↳ 2026-06-10 11:00): @Yauheni Krasner не развивай плиз
- 12:01 **Yauheni Krasner** (↳ 2026-06-10 11:00): что именно
- 12:01 **Marina Zaretskaya** (↳ 2026-06-10 11:00): я откдючаюсь, у меня другой мит
- 12:02 **Yauheni Krasner** (↳ 2026-06-10 11:00): будем поднимать тему дискавери
- 12:03 **Dana Kavalchuk** (↳ 2026-06-10 11:00): нет
- 12:15 **Johni Algarbi** (↳ 2026-06-10 11:00): Так, надо ещё раз созвониться с всеми, можем сегодня
- 12:15 **Johni Algarbi** (↳ 2026-06-10 11:00): Только через 40 минут хотя-бы
- 12:17 **Dana Kavalchuk** (↳ 2026-06-10 11:00): у Антона внешний звонок, я поставила мит после него
- 12:24 **Johni Algarbi** (↳ 2026-06-10 11:00): Отлично

## 2026-06-11

- 09:47 **Alex Petrushkevich**: Ссылки на доки для работы:
  Software Development Services Contract 10/03.docx 
  UPD SOW Optimum 15.05 (v10.4)  
  Добавил в раздел 2 условие про возврат [share removed] стоимости + пару правок подкинул
  - Links: https://docs.google.com/document/d/1p18R8CVGVwnJljDiE39Lr5uC1BPwvzxE/edit · https://docs.google.com/document/d/1bzY2oTz7nEbwalBQXC3dAPhmzVPRzZL2pf7iEAVG6-g/edit?tab=t.0 - [[2026-06-15 SOW v10.4 - rendering]]
  - Attachment: Software Development Services Contract 10/03.docx (in the chat) - a contract draft, listed in [[2026-09-07 Final contract - overview]]
  - Attachment: UPD SOW Optimum 15.05 (v10.4)  (Google Doc) - [[2026-06-15 SOW v10.4 - rendering]]
- 11:17 **Johni Algarbi**: Отлично!
  Завтра начну сделать перевод. В воскресенье утром точно будет всё готово.

## 2026-06-12

- 07:18 **Yauheni Krasner** (↳ 2026-06-11 11:17): @Johni Algarbi, привет!
  Начни, пожалуйста, перевод сначала с этого дока: Software Development Services Contract 10/03.docx 
  В течение дня зафиналим SOW и его потом тоже можно будет брать в работу.
  - Link: https://docs.google.com/document/d/1p18R8CVGVwnJljDiE39Lr5uC1BPwvzxE/edit
  - Attachment: Software Development Services Contract 10/03.docx (in the chat) - a contract draft, listed in [[2026-09-07 Final contract - overview]]
- 07:25 **Johni Algarbi** (↳ 2026-06-11 11:17): Принял, договорились.
- 10:11 **Yauheni Krasner** (↳ 2026-06-11 09:47): Со своей стороны также внес правки в документы. 
  Что из основного:
  переделал SOW под FP тип;
  добавил таблицу с майлстоунами и расписанием оплат
  немного видоизменил + добавил новые ассампшены. 
  @Arseniy Klimenko, @Alex Petrushkevich, @Dana Kavalchuk прошу вас также финально посмотреть редакцию.
  @Dana Kavalchuk, в таблице с майлстоунами оставил незаполненным последний столбец. Если он тебе не нужен, то можем удалить его.
- 10:56 **Dana Kavalchuk** (↳ 2026-06-11 09:47): столбец нужно удалить, у меня ошибка выскакивает, когда удаляю
  - Attachment: image.png (in the chat)
- 11:03 **Yauheni Krasner** (↳ 2026-06-11 09:47): готово
- 11:34 **Alex Petrushkevich** (↳ 2026-06-11 09:47): В целом нет замечаний
  Оставил только предложение поменять срок действия SoW (не путать с дедлайнами оказания услуг) с бессрочного на срок действия контракта, чтобы не триггерить лида

## 2026-06-14

- 12:10 **Johni Algarbi**: Всем привет! Перевод контракта и SOW уже готов. Я проверил несколько раз. Пожалуйста, проверьте английскую версию ещё раз и напишите мне, если что-то нужно добавить или исправить. Антон сказал, что желательно отправить клиенту сегодня. Спасибо.

## 2026-06-15

- 07:25 **Lizaveta Loseva** (↳ 2026-06-14 12:10): Привет! Смотрим версию 10.4?  https://docs.google.com/document/d/1bzY2oTz7nEbwalBQXC3dAPhmzVPRzZL2pf7iEAVG6-g/edit?tab=t.0
  - Attachment: UPD SOW Optimum 15.05 (v10.4)  (Google Doc) - [[2026-06-15 SOW v10.4 - rendering]]
- 07:25 **Lizaveta Loseva** (↳ 2026-06-14 12:10): @Johni Algarbi
- 07:26 **Yauheni Krasner** (↳ 2026-06-14 12:10): Привет, да
- 07:27 **Yauheni Krasner** (↳ 2026-06-14 12:10): @Arseniy Klimenko @Dana Kavalchuk, важно чтобы вы сделали ревью также со своей стороны. Договор и контракт - большие.
- 11:17 **Dana Kavalchuk** (↳ 2026-06-14 12:10): @Arseniy Klimenko @Lizaveta Loseva @Yauheni Krasner Привет, будут ещё правки
- 11:24 **Yauheni Krasner** (↳ 2026-06-14 12:10): С моей стороны - нет. Все готово
- 11:39 **Dana Kavalchuk** (↳ 2026-06-14 12:10): @Alex Petrushkevich отправляю
- 13:24 **Dana Kavalchuk**: Документы отправлены, всем спасибо!

## 2026-06-19

- 13:55 **Yauheni Krasner** (↳ 2026-06-15 13:24): привет!
  пока ничего не ответили
- 13:56 **Yauheni Krasner** (↳ 2026-06-15 13:24): @Dana Kavalchuk
- 13:57 **Dana Kavalchuk** (↳ 2026-06-15 13:24): Привет, только подтвердили получение, сказали изучают, пока не нужен звонок, в понедельник предложу ещё раз
- 13:58 **Yauheni Krasner** (↳ 2026-06-15 13:24): точно!
  нашел email. спасибо!

## 2026-06-30

- 15:13 **Lizaveta Shauchenka**: Документы все еще на ревью у клиента
  We appreciate following up. We are currently still reviewing the agreement internally. Kindly note that we will get back to you with any updates or comments as soon as possible.
  We appreciate your patience and understanding.
