---
type: source
kind: meeting-transcript
date: 2026-09-28
setting: internal
participants:
  - Mikhail Andrushkevich
  - Anton Oparienko
recording: https://app.bluedothq.com/preview/6aba65dce4876f176a53d7bf
language: ru
removed:
  - turns not about this project - an internal audit of another project, project finance in general (with figures), a process topic, another project's closure (22 whole turns from 00:06:47 to 00:27:50, and the ends of 00:06:26, 00:16:31 and the start of 00:28:01)
  - a price comparison from an earlier hiring (00:00:00)
  - a remark on starting before the formal staffing approvals (00:02:59)
---

# 2026-09-28 Anton and Mikhail 1-1 - transcript

Bluedot recording of "Anton / Mikhail 1:1", in Russian. The recording starts a few minutes into the
call (15:04 Warsaw time, the call from 15:00) and runs 30 min. Word-level segments grouped into speaker
turns by `pm/seed-ingest-scripts/bluedot-json2md.py`. Only the parts about Optimum are kept, verbatim,
including speech-recognition slips; every other turn is marked where it was. Never edited after storing.

[00:00:00] Mikhail Andrushkevich: и в одном, и в другом. Хардскиллы, наверное, по архитектору Техледу, это будут на нашем DM, на Арсении. Но надо тоже как-то попробовать по официальным, по неофициальным каналам пособирать информацию по тем кандидатам, которые будут давать. Убедиться, что чел с клодом дружит. Ну и смотреть дальше уже. По BA, мне кажется, тут больше на нашей стороне будет. Арсений, конечно, тоже там привлечен, если он будет хотеть. Но в целом нам надо будет постараться найти подходящую кандидатуру. Из моего предыдущего опыта поиска BA, он такой очень своеобразный. В прошлый раз, когда я на проекты брал биэ, я только на седьмом кандидате остановился. Не скажу, что все было идеально, но то, что там до этого предлагали, часть они отпадали даже без интервью, потому что предлагали из Польши и [removed: a price comparison]. Тут у нас стоимость, может быть, не так критична, но все равно необходимости, чтобы чел из Польши был, тут нет. Поэтому можно сфокусироваться, наверное, на Беларуси и лучше брать кого-то более сеньорного, там, матюрного, но из РБ. И нам там тоже надо будет, чтобы человек там как-то с клодом... Хочется, чтобы он, конечно, вообще был, там, и с клод-дизайн работал, и прототипчики лепил, и прочее-прочее, но... Не знаю, найдется ли такое. Но надо будет искать. Угу.

[00:02:10] Anton Oparienko: Окей. Хорошо, так. Я адаптирую, тебе вышлю, Макс, когда спросим, что туда вставить по ZP, те данные, которые там были внесены или нет. Вот. И тогда все это в stuffing засуну. Сможем, по идее, завтра начать ранность процесс. Ну, а по процессу я в том числе спрашивал, потому что условно... Ну, я так понимаю, что у нас есть какой-то approval в плане того, что у нас вообще разрешение на stuffing только там с... мишины там, печатили. Ну, короче, кто-то должен сказать, что да, go. Но я так понимаю, раз все там замешаны, включая Лешу и так далее, то проект как бы автоматически go. Надо просто делать то, что нужно.

[00:02:59] Mikhail Andrushkevich: Есть де-юре, есть де-факто. По де-юре там, да, куча документов, куча чек-листов. Аппровал там Миши, Вани, еще кого-то. [removed: a remark on starting before the formal approvals] Но если ты там найдешь, в принципе, можно попробовать и по официальному этому пути катануть. И когда у нас там пенелька будет, правда, лично, попросить approval Миши или там еще кого-нибудь. Или, по крайней мере, у Леши approval взять. [removed: a remark on starting before the formal approvals]

[00:03:59] Anton Oparienko: Хорошо, я понял.

[00:04:06] Mikhail Andrushkevich: Так, по проекту. У тебя еще какие-нибудь есть топики, которые нам надо обсудить? Или можем на более абстрактные темы перейти?

[00:04:19] Anton Oparienko: По самому проекту непонятно будет с Арсением обсуждать из тех людей, потому что Арсений говорит, что там все он премиус. По чатам и везде они три раза меняли это решение, что последнее не ясно, и Арсений не был на 100% уверен. Надо еще проверить нечто. Так вот, начал спрашивать про Flutter и Desktop Application. Ну, по идее, наверное, есть там какая-то обёртка стопудово, но Flutter как веб— да, окей. Десктопы делали обычно там типа электроном или ещё какой-то ерундой. Я подчеркну вообще Flutter как реально десктопная аппликейшн работает или нет, потому что это, ну, не веб, по идее. Вот.

[00:05:13] Mikhail Andrushkevich: А так—

[00:05:14] Anton Oparienko: да.

[00:05:16] Mikhail Andrushkevich: Ну да, там десктопная кликачка, но по идее... не по идее, а она должна потом скидывать инфу на серверы, когда связь появляется.

[00:05:24] Anton Oparienko: Не-не-не, да-да-да, всё верно. Я имею в виду, что, типа, билдит ли Flutter вообще десктопные версии под винду, которая, типа, экзекьютабл, бла-бла-бла. Потому что, насколько я знаю, обычно идут через электрон с таким подходом. Flutter, да, делает мобилку и веб, но я, ну, у себя в голове не нашел кейса, когда Flutter был, ну, типа, desktop executable. Вот, сейчас покурю с кодом эту информацию.

[00:05:54] Mikhail Andrushkevich: Слушай, не трать время, не кури с Клодом. У нас есть чел, который говорит, что он ответственен за все технические моменты. Возьми просто в чатик наш на троих, закинь эту тему, что вот тебе Клод подсветил, или ты не слышал, или есть у тебя какой-то консерв. Арсений все смотрит.

[00:06:15] Anton Oparienko: Я не собираюсь там архитектуру и все спрашивать, просто вообще такие кейсы есть, если это через три колена делается, у нас никто этого не делал, то это определенный риск.

[00:06:26] Mikhail Andrushkevich: Хорошо. Ну да. Ну да. Окей. Окей. [removed: not about this project]

[00:06:47] Anton Oparienko: [removed: not about this project]

[00:07:11] Mikhail Andrushkevich: [removed: not about this project]

[00:07:25] Anton Oparienko: [removed: not about this project]

[00:07:43] Mikhail Andrushkevich: [removed: not about this project]

[00:07:46] Anton Oparienko: [removed: not about this project]

[00:07:57] Mikhail Andrushkevich: [removed: not about this project]

[00:09:36] Anton Oparienko: [removed: not about this project]

[00:10:02] Mikhail Andrushkevich: [removed: not about this project]

[00:13:46] Anton Oparienko: [removed: not about this project]

[00:14:46] Mikhail Andrushkevich: [removed: not about this project]

[00:15:32] Anton Oparienko: Ну, вот как на optimal engineering, условно, пока мы не разрулим все относительно того, Во-первых, кстати, это two-way sync из того, что я понял. Ну, короче, то есть по данным, по тому, как билдится доступный аппликейшн и как он отправляет и получает данные и вообще состав из данных, который идет туда-сюда. Без этого, ну, типа, вебку нет смысла даже... трогать, скорее всего, но только условно, в плане того, что на ней мы хотим, чтобы отображалось. То есть, условно, пока у нас нет точного понимания, как билдится весь этот pipeline с данными, рисовать что-то там на вебе, какую-то функциональность туда заносить, смысла практически нет.

[00:16:31] Mikhail Andrushkevich: Мне кажется, что над веб-приложением, ну, по крайней мере, там, над базой данных, над бэкэндом, надо начинать думать параллельно с планированием десктоп-аппликейшен. То есть это один и тот же вопрос. Там одни и те же данные на десктопе, они собираются, хранятся локально, потом передаются на сервер. Ну, то есть... Структура данных, формат, прочее— это один и тот же вопрос, что для вебовского бэкэнда, что для десктопа. Поэтому там работы будут пересекаться. Когда эти вопросы решены, тогда параллельно можно уже и десктоп, и веб пилить. [removed: not about this project]

[00:19:44] Anton Oparienko: [removed: not about this project]

[00:21:08] Mikhail Andrushkevich: [removed: not about this project]

[00:22:45] Anton Oparienko: [removed: not about this project]

[00:23:40] Mikhail Andrushkevich: [removed: not about this project]

[00:24:46] Anton Oparienko: [removed: not about this project]

[00:25:30] Mikhail Andrushkevich: [removed: not about this project]

[00:25:35] Anton Oparienko: [removed: not about this project]

[00:25:47] Mikhail Andrushkevich: [removed: not about this project]

[00:26:23] Anton Oparienko: [removed: not about this project]

[00:27:04] Mikhail Andrushkevich: [removed: not about this project]

[00:27:09] Anton Oparienko: [removed: not about this project]

[00:27:50] Mikhail Andrushkevich: [removed: not about this project]

[00:28:01] Anton Oparienko: [removed: not about this project] а так я достаточно сильно с головой пытаюсь понять, что что с Optimum делать и что там вообще происходит.

[00:28:43] Mikhail Andrushkevich: Еще раз, пытайся что понять.

[00:28:45] Anton Oparienko: Что с Optimum делать, что это, с чем его есть и как двигаться дальше. Ну и плюс типа с Knowledge Base разобраться. Я там с Кириллом еще общаюсь, с Сердюком. Вот он мне там еще одну доку скинул, короче. пытаюсь подготовить knowledge base, с которым можно будет работать. Так что я в основном про это думаю.

[00:29:13] Mikhail Andrushkevich: Good. Будут интересные находки, делись. Хорошо. Тогда, если каких-то топиков нет, то можем их не придумывать, а разбежаться и пробовать.

[00:29:31] Anton Oparienko: Хорошо, давай. Я думаю, что с Optimum я вернусь в какой-то момент с тем, что вот все пересобрано, накопано, вот что нужно посмотреть и так далее.

[00:29:41] Mikhail Andrushkevich: Хорошо. Спасибо, хорошего дня.

[00:29:44] Anton Oparienko: Пока.

[00:29:44] Mikhail Andrushkevich: Пока.


