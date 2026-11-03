---
type: source
kind: meeting-minutes
date: 2026-10-27
setting: internal
participants:
  - Anton Oparienko
  - Mikhail Andrushkevich
  - Arseniy Klimenko
transcript: "[[2026-10-27 Optimum Three Caballeros call - transcript]]"
recording: https://app.bluedothq.com/preview/6ae0774306b1fd276aeae4bc
purpose: the delivery team's sync - the BA, the kick-off date, the tech lead and how to look at the client's old tool
procedure_version: 5d00575
---
# 2026-10-27 Optimum Three Caballeros call - minutes

Internal, no client present. "Optimum E.: Three Caballeros call", 10:04 to 10:28 UTC (11:04 to 11:28
Warsaw time); in Russian. Transcript: [[2026-10-27 Optimum Three Caballeros call - transcript]]
(Bluedot, in Russian, the call's language). The recording starts mid-sentence.

Not used as a source: Bluedot's own summary. It calls Kavalchuk "the client" and the client American,
and carries the BA candidates' relative cost.

Removed from the transcript and marked in place:

- Remarks about BA candidates, their cost and the BA department (00:00:00 to 00:15:43: 30 turns whole
  and parts of four). This includes the candidates' relative cost (money) and a remark about the
  client. Kept: which candidate would be the BA ("то ли у нас Лев, то ли Валерия",
  00:06:09) and the news that the BA was confirmed (00:14:43 to 00:15:41).
- Another project's schedule (part of 00:07:32).
- Reverse engineering of a third-party product, the client's old tool (parts of 00:20:44, 00:20:55 and
  00:21:40), including how to get Claude to do it. Kept out by default as a remark that could embarrass
  colleagues and adds little: the client does not want a copy of that tool
  ([[2026-10-20 Introductory call - transcript]] 00:40:42). Kept: running the installer, and asking the
  client for a licence.

Anton can ask for any of these to change.

Speaker labels match the transcript: Mikhail asks "Арсений, есть у тебя новости какие-нибудь?"
(00:16:36) and Arseniy answers (00:16:46); Anton asks Arseniy for the profile ("Нет, Арсений", 00:16:55)
and Arseniy answers (00:19:47); Anton agrees to move the e-mail after Mikhail argues for Monday
(00:06:09, 00:07:22).

Speech-recognition slips that matter: "Лев", "льва" is Leu, most likely Leu Dorakhau
([[2026-10-29 PM handover]]); "Саша" is Kavalchuk; "BI" is the BA; "тех льда", "техледа", "техлит"
are the tech lead; "супабейде" is Supabase; "флотериста", "платеристами" are Flutter developers;
"Губкин", "губкен", "Бубкин" are most likely one person, Gubkin; "реками", "реки" are requirements;
"киков", "иков" are the kick-off; "читергу" is четвергу, Thursday, and "мандай" Monday; "экзешник" is
the .exe installer. Not identified: "ажур" (00:18:15), "Сергеем", "Сереге" (00:19:47, 00:22:31; someone
on the mobile side, "Ребята с мобилы", 00:16:46).

## Summary

The BA was confirmed during the call; the discussion before it is removed. With the BA known, the
kick-off and the official start could move from Monday to Thursday. Anton wants the tech lead from
the start or middle of Discovery: reviewing the prototypes, talking to the client technically, then
writing the core, with a second Flutter developer added only when work can run in parallel. Gubkin
would mentor the tech lead. Arseniy sends the tech lead profile for staffing and sets up a call with
the mobile side. Anton downloaded the installer of the client's old tool; if it needs a licence, we
ask the client for one.

## Decisions

- The BA: "Всё, нам дают Льва." (Mikhail, 00:14:43); "Ладно, все, вопрос решился, едем со Львом."
  (Anton, 00:15:35)
- The tech lead, a proposal: "В начале, в серединке discovery берем техледа ... Этот же человек в
  течении проекта дальше начинает писать код, он начинает писать core функциональность" and a second
  developer "как только он говорит, что есть возможность" (Anton, 00:18:15); "Скорее всего, у нас
  будет техлит, и Губкин будет за ним смотреть" (Arseniy, 00:19:47).

## Agreements with the client

None - internal meeting.

## Internal agreements

- The kick-off e-mail moves to Monday: "хорошо, я переделаю на понедельник" (Anton, 00:07:22), dates
  for the reports and formulas included (Mikhail, 00:07:54). Reopened once the BA was confirmed:
  "Старт проекта понедельник или четверг? ... В четверг провести киков, пообщаться, и официальный
  старт." (Mikhail, 00:16:10)

## Actions

- Arseniy: the tech lead profile, "стек, реквайерменты", so Anton can open the staffing (00:16:55,
  00:19:47).
- Arseniy: a call with the mobile side on the tech lead, Anton and Mikhail invited (00:16:55,
  00:20:19).
- Arseniy: try to run the old tool's installer (00:20:55, 00:22:31).
- Anton: the kick-off e-mail, dates moved (00:07:22).

No Jira keys yet; there is no board.

## Questions raised

- Monday or Thursday for the kick-off and the start (00:05:34 to 00:07:22, 00:16:10). Settled later
  outside the call.
- Supabase with full-stack developers, to need fewer people: "Я уже много про это говорил, просто мы
  все не залайлились" (Arseniy, 00:17:46). Open, [[DEC-004 Backend stack]].

## New scope mentioned

None.

## Proposed changes

In the table of [[2026-10-20 Introductory call - minutes]], which covers this call, the introductory
call of 20 October and the sync of 28 October: rows 10 (the start), 13 (the BA), 14 (the tech lead),
19 (the Discovery approach), 20 (the old tool's installer) and 22 (the kick-off e-mail).
