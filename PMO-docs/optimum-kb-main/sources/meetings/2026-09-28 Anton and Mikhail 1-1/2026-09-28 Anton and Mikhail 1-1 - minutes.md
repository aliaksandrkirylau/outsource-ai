---
type: source
kind: meeting-minutes
date: 2026-09-28
setting: internal
participants:
  - Mikhail Andrushkevich
  - Anton Oparienko
transcript: "[[2026-09-28 Anton and Mikhail 1-1 - transcript]]"
recording: https://app.bluedothq.com/preview/6aba65dce4876f176a53d7bf
purpose: the Optimum parts of a 1:1 - how the first hires are assessed and approved, the Flutter desktop doubt, the order of the desktop and web work
procedure_version: d6eb286
---
# 2026-09-28 Anton and Mikhail 1-1 - minutes

Internal, a 1:1 between the two PMs; in Russian. Transcript:
[[2026-09-28 Anton and Mikhail 1-1 - transcript]] (Bluedot), which keeps only the Optimum parts. The
rest of the 1:1 was not about this project and is not stored: an internal audit of another project,
project finance in general, a process topic, another project's closure. The recording starts a few
minutes into the call. Anton reviewed the 1:1 before its ingest.

Speech-recognition slips that matter: "Техлед" is tech lead; "Клод", "клод-дизайн" are Claude and
Claude Design; "РБ" is Belarus; "пенелька" is the P&L; "stuffing", "ставфинг" are staffing; "ZP" is
salary data (no figures said). "Миша" and "Ваня" among the approvers (00:02:59) are most likely
Michael Labutin and Ivan Shatuho, whom PMO named as the approvers on 3 September
([[DEC-009 Sign the client's final contract as it stands]]); "Леша" most likely Alexey Gamanovich;
"Макс" (00:02:10) is not identified, most likely Maksim Lebedev of the staffing process
([[2026-09-25 Optimum Eng sync - minutes]]).

## Summary

The first hires: Arseniy assesses the tech lead's or architect's hard skills; the PMs lead the BA
search. Both should work well with Claude; the BA ideally also builds prototypes. Mikhail would focus
the BA search on Belarus and on a more senior person. Staffing formally needs approvals; the plan is to
ask for them once the P&L is ready, at least Alexey's. Anton doubts that Flutter builds a Windows
desktop executable and notes that nobody here may have done it; Mikhail asked him to raise it with
Arseniy. The data structure and format are one question for the desktop and the web backend, to be
settled first; then both can be built in parallel.

## Decisions

None. Mikhail's view on the BA and on the order of work is recorded under the notes below.

## Agreements with the client

None - internal meeting.

## Internal agreements

- Assessment: "Хардскиллы, наверное, по архитектору Техледу, это будут на нашем DM, на Арсении" and "По
  BA, мне кажется, тут больше на нашей стороне будет" (Mikhail, 00:00:00); information on candidates
  also "по официальным, по неофициальным каналам"; "Убедиться, что чел с клодом дружит" (00:00:00).
- The BA: "можно сфокусироваться, наверное, на Беларуси и лучше брать кого-то более сеньорного, там,
  матюрного, но из РБ"; "Хочется, чтобы он, конечно, вообще был, там, и с клод-дизайн работал, и
  прототипчики лепил, и прочее-прочее, но... Не знаю, найдется ли такое." (Mikhail, 00:00:00)
- Approvals: "По де-юре там, да, куча документов, куча чек-листов. Аппровал там Миши, Вани, еще
  кого-то." ... "И когда у нас там пенелька будет, правда, лично, попросить approval Миши или там еще
  кого-нибудь. Или, по крайней мере, у Леши approval взять." (Mikhail, 00:02:59). Anton's reading: "раз
  все там замешаны, включая Лешу и так далее, то проект как бы автоматически go" (00:02:10).
- The Flutter doubt goes to Arseniy, in the three-person chat: "У нас есть чел, который говорит, что он
  ответственен за все технические моменты. Возьми просто в чатик наш на троих, закинь эту тему"
  (Mikhail, 00:05:54).

## Actions

- Anton: adapt the staffing document, ask Max what goes in for the salary data, and put it into
  staffing; "Сможем, по идее, завтра начать" (00:02:10).
- Anton: raise the Flutter desktop question with Arseniy in the [Core] chat (00:05:54).
- Anton: come back on Optimum once everything is gathered (00:29:31).

No Jira keys yet; there is no board.

## Questions raised

- Does Flutter build a Windows desktop executable, and has anyone here built one: "билдит ли Flutter
  вообще десктопные версии под винду, которая, типа, экзекьютабл" (Anton, 00:05:24); "если это через три
  колена делается, у нас никто этого не делал, то это определенный риск" (00:06:15). And which stack is
  final: "По чатам и везде они три раза меняли это решение, что последнее не ясно, и Арсений не был на
  100% уверен" (00:04:19).
- The order of the desktop and web work (00:15:32, 00:16:31), below.

## New scope mentioned

None.

## Proposed changes

One table for the 1:1. Source key: T = [[2026-09-28 Anton and Mikhail 1-1 - transcript]].

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | update | DEC-002 Senior engineers first | How the first hires are assessed and approved: Arseniy the tech lead's hard skills, the PMs the BA; candidates checked also through informal channels; both must work well with Claude; the BA more senior, from Belarus; formal approvals (Misha, Vanya and others; at least Alexey's once the P&L is ready) | extracted | - | T 00:00:00, 00:02:10, 00:02:59 | rejected 2026-09-28 |
| 2 | update | QUE-009 Where may our team members be located | Mikhail would focus the BA search on Belarus ("необходимости, чтобы чел из Польши был, тут нет"), which makes the question pressing; not an answer | extracted | - | T 00:00:00 | rejected 2026-09-28 |
| 3 | update | DEC-010 Confirm the product with the client through prototypes in code | The BA they want also builds prototypes with Claude and Claude Design - "Не знаю, найдется ли такое": a downside, such a BA may be hard to find | extracted | - | T 00:00:00 | applied 2026-09-28 |
| 4 | update | DEC-007 Flutter for the desktop app | Anton's doubt: whether Flutter builds a Windows desktop executable, and whether anyone here has built one ("определенный риск"); the stack choice changed three times in the chats and Arseniy was not fully sure which is final; to be raised with Arseniy. Adds to the existing obligation "check what Flutter offers on the Windows desktop" | extracted | - | T 00:04:19 to 00:06:15 | rejected 2026-09-28 |
| 5 | update | CON-001 Offline operation and sync between rigs and HQ | The order of work: the data structure and format are one question for the desktop and the web backend, to be settled first, then both built in parallel (Mikhail); until the pipeline is clear, web functionality makes little sense (Anton) | extracted | - | T 00:15:32, 00:16:31 | rejected 2026-09-28 |
| 6 | no material | QUE-002 Do managers send anything back to the rigs | Anton's "это two-way sync из того, что я понял" matches the answer already recorded; not a new source for it | - | - | T 00:15:32 | recorded 2026-09-28, no note |
