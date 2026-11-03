---
type: source
kind: chat
date: 2025-10-20
original: https://chat.google.com/room/AAQAMdfmWl4
received_from: Google Chat space "T1 - EST - Optimum Engineering Standards - ASnot - SA - Big data - 023690" (spaces/AAQAMdfmWl4), the presale request chat; read by Anton Oparienko's copilot on 2026-09-28
purpose: how the presale solution, the estimate and the scope cuts came about, and what the client said about the proposal - the history behind the WBS and the SOW
supersedes:
procedure_version: b4cb7da
---
# 2025-10-20 Presale chat - overview

kind: chat, in two parts by period. 461 messages from 2025-10-20 12:07 to 2026-09-25 11:48 UTC; none
after that when read on 2026-09-28.

| Part | First message | Last message | Rendered | Left out |
|---|---|---|---|---|
| [[2025-10-20 Presale chat - rendering 1]] | 2025-10-20 12:07 | 2025-11-05 15:57 | 304 | 10 |
| [[2025-10-20 Presale chat - rendering 2]] | 2025-11-07 08:08 | 2026-09-25 11:48 | 142 | 5 |

The break is the proposal presentation to the client on 5 November 2025.

## What it is

The chat Sales opened for the lead on 2025-10-20 and used through presale: the first call, the question
lists, the architecture, the BA's draft WBS, the estimate gathered from each department on 3 to 5
November, the presentation of 5 November, the client's feedback on the proposal (24 November), the
re-estimate in the v1 WBS (25 November), contract preparation, then a fresh review of the estimate in
May 2026 and the Flutter estimate. People: Sales (Lizaveta Shauchenka, Polina Yanovskaya, Anton
Snotov), presale (Aliaksei Tsitou, Marina Zaretskaya, Andrey Lapikov), the BA Kira Barshchevich, the
architect Aliaksei Sauta, estimators from each department, later Alexey Gamanovich, Arseniy Klimenko and
others. In Russian, with the client's messages in English.

Attachments already stored: Questions.docx and the Q&A register
([[2025-10-29 Client answers to the Q&A register - rendering]]), Daily.xlsx
([[2025-10-29 Client sample daily report - rendering]]), the first-call transcript PDF
([[2025-10-22 First call with OES - transcript]]), Marina's follow-up
([[2025-10-22 First call with OES - notes]]), the company research, the presale architecture, the BA
draft WBS, the solution proposal, the v1 WBS. Stored with this batch as link-only overviews:
[[2025-11-04 Working estimate - overview]] (the sheet the team estimated in on 4 and 5 November),
[[2025-11-05 DevOps estimate - overview]] (the on-premises DevOps estimate) and
[[2025-11-24 AWS infrastructure breakdown - overview]] (money). The client's materials folder:
[[2025-11-20 Client formula and chart samples - overview]]. The chat names two more places not stored: a separate chat with the Flutter estimate ("чата с
флатером", 2026-05-25) and the economy chat opened for the margin calculation (2025-11-25).

## How far to trust it

Medium (`sources/presale/`): what the presale team said to each other while preparing, not what the
client agreed. Two messages carry the client's own words, relayed by Polina Yanovskaya: the answers of
29 October (stored separately) and the feedback on the proposal of 24 November (part 2, 12:10). What
Aliaksei Tsitou drafted in reply (12:44) was proofread before sending ("пруфридните плз перед
отправкой"); the chat does not show the text that was sent. "Все понравилось" after the presentation
(5 November, 15:03) is not acceptance.

## Not for

Scope checks (use the v1 WBS and the SOW), or the figures behind "деньги" and "рейты" (removed; in the
P&L). The hours people quote here were their estimates at the time.

## Removed at ingest

- Money: two amounts in Aliaksei Tsitou's reply of 2025-11-24 12:44 (the AWS monthly range and the
  credit), and a multiplier of the client's budget in Marina Zaretskaya's message of 2025-11-12 10:12.
- Left out, and counted: 7 task-system messages ("Created a task (via Tasks)", "Completed a task"), 6
  bot messages (innostaff; one lists e-mail addresses), 2 empty messages. One bot message, 2025-11-17
  08:18, carries a person's answers to the sales tool's feedback form: "Demo Presented - в демо не было
  необходимости на данном этапе ... Proposal Review - не проводили ввиду нехватки времени между
  финализацией решения и митом с клиентом".
- Redacted in place: one message, 2025-10-22 09:08, a heated personal remark to a colleague; its project
  content is kept as a note in the rendering. Anton to confirm.
- Reactions, and blank lines inside messages.

## Summary

After the first call (22 October) presale chose the solution type and storage with an architect: a
Windows desktop app with a local database at the rig, a central server, and a web app for managers.
The web app came from the manager role, not from the client asking: "на звонке он говорил про десктоп и
мобилку, нигде не просил веб" (Kira Barshchevich, 3 November). The estimate was put together in about
two days, 3 to 5 November, department by department, the MAUI desktop and mobile front end on the
morning of the presentation with "минут 40" to do it. The calculations were estimated for one algorithm
because nobody knew how many there would be. The presentation went well; the questions were about the
budget, and the client was steered from on-premises to a cloud.

On 24 November the client answered the proposal: the fixed price should cover the whole lifecycle
"across the 5-month duration"; calculations and modelling, reporting, dashboards and inventory "remain
essential requirements for the desktop application"; a cloud provider to be recommended; the warranty
to go "from 3 weeks to 6 weeks"; and a pro forma contract. The same day the WBS was re-estimated for the
full desktop, with no mobile and with a choice of units, in the v1 sheet (25 November), briefly:
"Антон просит не тратить ресурсы на детальную переработку оценки" (Polina Yanovskaya; which Anton is not
said). The client's calculation samples and charts arrived on 20 November; the team
judged the formulas mixed, the charts partly non-standard, and found no description of the modelling
logic. Contract preparation began on 26 November; the client's CEO was on leave in December.

In May 2026 a fresh reviewer found that the scope had been cut several times with the cuts recorded
only in the WBS assumptions, and that sync, conflict handling, reports, charts and edge cases were
likely underestimated. The Flutter estimate followed (22 May 2026, "по стеку все релевантно"). The last
message (2026-09-25) tags Anton Oparienko and Mikhail Andrushkevich.

Cross-references to the stored WBS: Marina's "минут 40" (5 November, 08:21) is the "40 минут" Arseniy
recalled at the 25 September sync, about ten months earlier, not over a year; Anton Soshnikau's
"накинул процент" (2026-05-25) is likely the Flutter roll-up's BA line at 25% of development (our
reading, not checked against the sheet's history).

## Proposed changes

The batch 5 table. Source keys: C1 = [[2025-10-20 Presale chat - rendering 1]], C2 =
[[2025-10-20 Presale chat - rendering 2]], each with the date and UTC time of the message. No new notes;
all rows update existing ones. Approved by Anton on 2026-09-28: all rows; the redaction of 2025-10-22
09:08 stands; the Flutter chat is not sought for now.

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | update | DEC-005 Desktop at the rig, web app at HQ | History: the web app came from the manager role ("нигде не просил веб ... роли Manager нужно видеть данные с нескольких подконтрольных локаций"). On 24 Nov 2025 the client: "calculations & modeling, reporting, dashboard, and inventory management are not included in the desktop application under project scope. These items remain essential requirements for the desktop application"; our draft reply: limiting the desktop was a budget choice, "Features like reporting and dashboards heavily rely on server-side resources and data", functions could be duplicated from web to desktop; the WBS was re-estimated for "фул скоупа десктопного приложения" | extracted | - | C1 11-03 16:09; C2 11-24 12:10, 12:44, 15:35 | applied 2026-09-28 |
| 2 | update | DEC-006 Calculations run in the desktop app, formulas fixed in the code | Context: the client's 24 Nov 2025 statement that calculations and modelling "remain essential requirements for the desktop application" | extracted | - | C2 11-24 12:10 | applied 2026-09-28 |
| 3 | update | CON-003 Correct calculations | Why the estimate was per one algorithm: "у нас эффорт за один и мы не знаем сколько их ... калькуляция и моделирование могут оказаться самыми дорогими и времязатратными" (Marina). We asked for calculation samples and "используемую для них нормативную документацию" (18 Nov); they came on 20 Nov. The team's reading: "4 сложных формулы ..., 3 простых ..., 2 графика ... и 1 таблица общая", back end "под 100" against 36-48 estimated; front end "надо докинуть 100 ... нет библиотек у MAUI"; the consultant: formulas "разной сложности", "Не нашел описания логики моделирования" | extracted | - | C1 11-05 10:08; C2 11-18 08:37, 11-20 12:21 to 14:41, 11-24 12:37 | applied 2026-09-28 |
| 4 | update | REQ-008 Fluid hydraulics simulation | The client's materials carry no description of the modelling logic ("Не нашел описания логики моделирования"); an option without the hydraulics calculation was considered to fit the budget | extracted | contracted (unchanged) | C2 11-24 12:37, 11-12 11:58 | applied 2026-09-28 |
| 5 | update | QUE-003 Do calculations and modelling need 3D or complex visuals | The team read the client's chart samples both ways: "не совсем стандартные графики, на такие нет библиотек у MAUI, придется рисовать самим" and "Графики несложные, наверно только конструкция скважин". The samples come in with batch 7; still for the client | evaluated | blocks Development Flutter!60 (unchanged) | C2 11-20 14:41, 11-24 12:37 | applied 2026-09-28 |
| 6 | update | REQ-018 Units of measure and conversion | Where it came from: "Я бы сразу закладывал работу и с метрическими единицами измерения и конвертацию одних единиц измерения в другие, тут надо уточнить" (24 Nov 2025); the re-estimate the same day added "(+выбор системы измерения)" | extracted | contracted (unchanged) | C2 11-24 12:37, 15:35 | applied 2026-09-28 |
| 7 | update | REQ-013 Mobile app | When it left: the prototype of 19 Nov was desktop and web ("мобилку не нужно"); the 24 Nov re-estimate was for "отсутствия мобильного" | extracted | out-of-scope (unchanged) | C2 11-19 09:37, 11-24 15:35 | applied 2026-09-28 |
| 8 | update | CON-002 Deployment outside public cloud | Hosting history, Nov to Dec 2025: after the presentation "он прем им и не нужен скорее всего ... лучше на gcp всё сделать"; 12 Nov "Заменяем он прем хранение на клауд GCP"; 24 Nov to the client "we suggest AWS"; 25 Nov DevOps re-estimated as the client "уходит от онпрем и выбирает клауд ( ассампшн AWS)"; 24 Dec "6 месяцев бесплатной инфры от старта разработки дадим". The later move to GCP comes with the contract chat (batch 6) | extracted | - | C1 11-05 15:03; C2 11-12 10:12, 11-24 12:44, 11-25 09:37, 12-24 11:25 | applied 2026-09-28 |
| 9 | update | CON-001 Offline operation and sync between rigs and HQ | The May 2026 review: "разработка механизма синхронизации локальных данных с удаленным сервером" and "обработка конфликтов синхронизации и поддержка offline-first сценариев" are "вероятно, не учтены либо существенно недооценены"; what the client was told on 24 Nov 2025 about reports and dashboards relying on server-side data | extracted | - | C2 2026-05-15 13:46, 2025-11-24 12:44 | applied 2026-09-28 |
| 10 | update | CON-004 Scale and data volume | The presale architect saw no need for a data engineer: "судя по описанию данных не много" | extracted | - | C1 11-04 11:30 | applied 2026-09-28 |
| 11 | update | DEC-004 Backend stack | The estimate's dates from the chat: the MAUI desktop and mobile front end estimated on 5 Nov 2025 with "минут 40" (the "40 минут" of the 25 Sep sync); re-estimated for the full desktop on 25 Nov 2025; the Flutter estimate on 22 May 2026, "по стеку все релевантно, проблем с реализацией под требования не будет", and "актуальная оценка из чата с флатером". One back end for web and desktop: "back end не разделяется на десктоп и веб, технически на деле это будет одно решение" | extracted | - | C1 11-05 08:12 to 09:27; C2 11-25 13:24, 2026-05-22 15:33, 2026-05-25 14:14 | applied 2026-09-28 |
| 12 | update | COM-001 Delivery within six months | History: the client in Nov 2025 read the proposal as "the fixed cost covers the full project lifecycle from inception through final release, across the 5-month duration" | extracted | - | C2 11-24 12:10 | applied 2026-09-28 |
| 13 | update | COM-004 Twelve-month warranty | History: the six weeks was the client's request, "extend it from 3 weeks to 6 weeks" (24 Nov 2025); the optional monthly support package offered then (bug fixing and incidents, technical support and administration, updates) | extracted | - | C2 11-24 12:10, 12:44 | applied 2026-09-28 |
| 14 | no material | The May 2026 review's other findings | Reports, charts, edge cases and app state likely underestimated; "проект рассчитывался под junior-level resource". A risk for the PMO risk register when it is filed | - | - | C2 2026-05-15 13:46 | recorded 2026-09-28, no note |
| 15 | no material | Cuts recorded only in WBS assumptions | The reviewer: "за исключением assumption-секции в WBS, практически нигде не зафиксировано, какие именно функциональные блоки были упрощены или исключены". The out-of-scope Requirements now record them | - | - | C2 2026-05-15 13:46 | recorded 2026-09-28, no note |
| 16 | no material | Presale process | Who estimated what, the WBS-or-proposal argument, deadlines, sales-tool statuses: history, kept in the source | - | - | C1, C2 | recorded 2026-09-28, no note |
| 17 | no material | The prototype | Desktop and web only; clients get "только видео прототипа"; already named in the slides overview. Marina's ideas for report and user tables were ours, not the client's | - | - | C2 11-19 | recorded 2026-09-28, no note |
| 18 | no material | BA staffing | "БА тут будет Марина Зарецкая" (May 2026): the A02 register, not a note | - | - | C2 2026-05-25 14:07 | recorded 2026-09-28, no note |
| 19 | no material | How the SOW was reworked in May 2026 | Two tracks: a fresh look at assumptions, risks and dependencies, and the PMO contract group on the MSA and SOW. The SOW v10.4 is stored | - | - | C2 2026-05-11 14:09 | recorded 2026-09-28, no note |
| 20 | new | DEC-007 Flutter for the desktop app (draft: the lint needs deciders for proposed, and none are named) | Added after the table, at Anton's request: MAUI with ReactJS (presale) against Flutter (chosen for expertise; the Flutter estimate of 22 May 2026). No deciders named; the web framework left open; Anton checks Flutter's desktop capabilities separately | extracted | - | C2 2026-05-22 15:33, 2026-05-25 14:14; [[2026-09-25 Optimum Eng sync - transcript]] 00:22:01 | applied 2026-09-28 |
