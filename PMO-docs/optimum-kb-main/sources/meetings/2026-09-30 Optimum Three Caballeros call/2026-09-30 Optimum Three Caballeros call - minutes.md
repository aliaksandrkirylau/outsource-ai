---
type: source
kind: meeting-minutes
date: 2026-09-30
setting: internal
participants:
  - Anton Oparienko
  - Mikhail Andrushkevich
  - Arseniy Klimenko
transcript: "[[2026-09-30 Optimum Three Caballeros call - transcript]]"
recording: https://app.bluedothq.com/preview/6abcd09425128043931a9024
purpose: the delivery team's prep for Alexey's review of 1 October, a walkthrough of the knowledge base, and where the PMs keep sensitive material
procedure_version: 5d00575
---
# 2026-09-30 Optimum Three Caballeros call - minutes

Internal, no client present. "Optimum E.: Three Caballeros call", 09:04 to 09:34 UTC (11:04 to 11:34
Warsaw time); in Russian. Transcript: [[2026-09-30 Optimum Three Caballeros call - transcript]]
(Bluedot, in Russian, the call's language).

The call's chat (spaces/AAQA2smCwAE) has two messages: Mikhail's link at 09:06 UTC to the document he
calls "architectural significant requirements" - the stored presale architecture, the same Drive file
([[2025-10-24 Presale architecture - overview]]) - and Gemini's recap at 10:01 UTC, a bot message with a
few English lines, not used.

Removed from the transcript and marked in place, by the ingest rule for remarks about people: a
comparison with a colleague on another project (00:03:36), a remark about a colleague outside the
project (00:04:21), the speaker's past employment and a remark about a former colleague (00:04:21), and
a story about a past project of another team, with names (00:05:59). Kept: what was said about the tech
lead candidate's time, since it bears on staffing, and the remarks on preparing for Alexey. Anton can
ask for either to change.

Speaker labels match the transcript: Anton addresses Mikhail and Arseniy by name and they answer. One
turn edge is doubtful: "Да, хорошо, я скину." ending Anton's turn at 00:26:13 is most likely Arseniy's.

Speech-recognition slips that matter: "КБ" is the KB; "китограмму" (00:02:52) and "биограмму" (00:05:59)
are a diagram; "технорей" are технарей; "Техлидомова", "техником" (00:02:52) are a tech lead; "Андрея
Карпатова" is Andrej Karpathy; "LLMWiki" is the LLM wiki; "гид", "GIT" are git, and "свой кит", "гид"
(00:14:37, 00:26:13) the person's git account; "coworker", "cowork" are Claude Cowork; "код табе",
"CodeTab" are the Code tab; "PMU Copilot" is the PMO Copilot; "PNL", "пионерок" (00:27:35) are the P&L;
"Пиары" are pull requests; "общий подбородок" (00:25:18) is most likely the shared branch; "ажуры" is
Azure. "Сергей Губкин" is Sergei Gubkin, of the mobile department
([[DEC-002 Senior engineers first]]); "Кирилл Сердюк" is named as the author of the KB concept document.
Not identified: "Таня" (00:09:25), "Николацием" (00:26:13), "App City" (00:09:25).

## Summary

Anton told the others that Alexey would join the next day to see whether the team knows what the
system is made of, in what order it will be built and how the app reaches the rigs; Mikhail expected
him to ask for a context diagram and components. Arseniy would have his tech people draw the diagrams,
possibly Sergei Gubkin of the mobile department, whom he sees as a possible tech lead; Anton doubts
Gubkin would have the time. Anton walked through the knowledge base: sources, typed notes, git sync,
Obsidian, working with it through Claude, and no money in it. Mikhail had opened a pull request from
his copy, which Anton had not seen; kb-sync commits to main without pull requests. How the three PMs
keep sensitive material - money, team performance, internal statuses - outside the shared KB was
discussed with four options and left open.

## Decisions

None taken. Open, with options: where the PMs keep sensitive working material (Questions raised, and
row 3 below).

## Agreements with the client

None - internal meeting.

## Internal agreements

- Arseniy prepares for Alexey's review: "Я подготовлю всё нам необходимое и посмотрим, чего не хватает"
  (00:08:52); the diagrams to be drawn by the tech people, "пусть они биограмму адресуют" (00:05:59).

## Actions

- Arseniy: have the tech people draw the diagrams for 1 October (00:02:52, 00:05:59). Done: posted in
  [Core] on 2026-10-01 12:56 UTC ([[2026-10-01 Solution vision diagrams - overview]]).
- Arseniy: send his git account so Anton can add him to the KB repository (00:14:37, 00:26:13); asked
  again in [Core] the same day, "И жду еще твой юзернейм" (Anton, 2026-09-30 14:38 UTC).
- Arseniy: think about how to share sensitive information (00:26:33, 00:28:04).
- Anton: look at Mikhail's pull request (00:26:13). Checked 2026-10-02: GitHub shows no pull request and
  no fork of the repository, so it did not reach the shared repo.

No Jira keys yet; there is no board.

## Questions raised

- What Alexey wants before delivery starts: "понимает ли Арсений, из каких кусков состоит система, что
  мы будем билдить, в каком порядке, как мы будем идти. Апки деливерись там на собственно Риге" (Anton,
  00:00:00); "Леша, скорее всего, будет просить контекстную диаграмму и как-то на уровне компонент"
  (Mikhail, 00:02:05). Answered by the call of 1 October:
  [[2026-10-01 Optimum Three Caballeros call - minutes]].
- The tech lead: Arseniy would try Sergei Gubkin, "потому что он, типа, всегда, вроде, когда обещал, все
  выполнял" (00:05:59); "Пусть кто-то будет там проверенный" (00:05:59). Anton: "у него не будет
  хватать времени. С него никто не снимет всю внутреннюю нагрузку, слежение за 20 интернами" (00:05:36).
  Not settled.
- How the KB works with the PMO Copilot (Mikhail, 00:17:15): the plugin's skills work in any folder and
  take the context of the folder they run in (Anton, 00:17:36).
- Where sensitive material lives (Mikhail, 00:20:24): "в GIT ты не заливал сознательно какую-то sensitive
  информацию, финансовые данные. Соответственно, они должны храниться где-то еще, потому что, по крайней
  мере, нам троим надо работать и с этой инфой"; the kinds: internal statuses, "информация про то, что
  кто-то в команде не перформит", statuses for the client, "Риски, финансовые projection" (00:22:30).
  Options: a local folder kept out of git by gitignore (Anton, 00:23:16); encrypted data in the
  repository, "как это делают в программировании" (Arseniy, 00:26:33); a second repository for the three
  (Mikhail, 00:28:14), which Arseniy finds "рутинный, муторный" to keep in step (00:28:35); a Drive
  folder, "Sensitive находится в Sensitive папке в Drive фолдере ... эта инфа никогда не уходит в КБ, но
  Клод знает, что за Sensitive нужно туда ходить" (Anton, 00:29:39). Not settled: Anton had to leave, and Arseniy, "Да, я подумаю тоже. Хорошо." (00:30:12).
- Mikhail's pull request: "я там pull-request сделал. Я так понимаю, тебе его надо опробовать"
  (00:25:18), "там на тебе висит уже пару дней" (00:26:07). Anton: "сейчас так сделано, что мы всегда
  пушим в мейн, мы не создаем бранча ... мы не аппрувим каждый чих, который кто-то сделал" (00:25:41).

## New scope mentioned

None.

## Proposed changes

Source key: T = [[2026-09-30 Optimum Three Caballeros call - transcript]].

Approved by Anton Oparienko on 2026-10-13: all rows; DEC-013's deciders tbd, so it is draft. Before applying, a quote in Questions raised and in row 3 that is not in the transcript ("обсудим") was replaced with the transcript's words.

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | update | DEC-002 Senior engineers first | The tech lead from the mobile department, 30 Sep: Arseniy would ask Sergei Gubkin, whom he sees as a possible tech lead, to draw the diagrams first, "А если в итоге он не будет техником, то диаграммы у нас все равно будут более валидные, чем у меня"; he wants someone proven. Anton doubts Gubkin would have the time alongside his department work. Not decided | extracted | - | T 00:02:52 to 00:07:40 | applied 2026-10-13 |
| 2 | update | 2026-10-01 Solution vision diagrams - overview | A pointer: who drew images 01 and 02 is most likely the mobile department's people, possibly Sergei Gubkin, as Arseniy planned on 30 Sep; not confirmed | evaluated | - | T 00:02:52, 00:05:59 | applied 2026-10-13 |
| 3 | new | DEC-013 Where the PMs keep sensitive working material | Delivery. Money, team performance, internal statuses and financial projections stay out of the shared KB (AGENTS.md rule 7), but the PMs need them. Options: a gitignored local folder (Anton); encrypted data in the repository (Arseniy); a second repository for the three (Mikhail; the two must be kept in step, Arseniy); a Drive "Sensitive" folder the three can open, which Claude reads and never brings into the KB (Anton). Not decided (Arseniy, "Да, я подумаю тоже", 00:30:12). Touches AGENTS.md "Where the rest lives" (the PMO Drive folder, not created yet), so a curator matter too. Draft, deciders tbd unless you name them | extracted | - | T 00:20:24 to 00:29:39 | applied 2026-10-13 |
| 4 | no material | The KB walkthrough | Sources, types, git sync, Obsidian, the PMO Copilot alongside it: how the KB works, already in AGENTS.md and the README | - | - | T 00:09:25 to 00:20:24, 00:24:03 to 00:24:27 | recorded 2026-10-13, no note |
| 5 | no material | Mikhail's pull request | kb-sync commits to main without pull requests; the request is not on GitHub; an action for Anton | - | - | T 00:25:18 to 00:26:13 | recorded 2026-10-13, no note |
| 6 | no material | Alexey's review of 1 October | What he would ask; the call took place and is ingested | - | - | T 00:00:00 to 00:02:37 | recorded 2026-10-13, no note |
| 7 | no material | 2025-10-24 Presale architecture | Mikhail's link in the call's chat is that stored source | - | - | the call's chat, 09:06 UTC | recorded 2026-10-13, no note |
