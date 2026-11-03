---
type: source
kind: meeting-minutes
date: 2026-10-12
setting: internal
participants:
  - Arseniy Klimenko
  - Mikhail Andrushkevich
  - Anton Oparienko
transcript: "[[2026-10-12 Optimum Three Caballeros call - transcript]]"
recording: https://app.bluedothq.com/preview/6acca243ea85b97a1b8ccac0
purpose: the delivery team's sync - Redis taken out of the architecture, the SOW's Arabic translation, the contract's risks
procedure_version: 5d00575
---
# 2026-10-12 Optimum Three Caballeros call - minutes

Internal, no client present. "Optimum E.: Three Caballeros call", 09:03 to 09:21 UTC (11:03 to 11:21
Warsaw time); in Russian. Transcript: [[2026-10-12 Optimum Three Caballeros call - transcript]]
(Bluedot, in Russian, the call's language). The recording starts mid-sentence, in Arseniy's account of
the architecture discussion; the first minutes were not recorded.

Removed from the transcript and marked in place: margin figures (00:13:55); a colleague's past
employment (00:00:56), a story about a person outside the project (00:06:09) and a remark about a
colleague's reaction (00:11:16), none with project content; remarks about a colleague's employment
status (00:12:29, 00:12:47, 00:12:49). Anton can ask for any to change.

Speaker labels match the transcript: Mikhail asks Arseniy about Redis and Arseniy answers; Anton
proposes the load test. Speech-recognition slips that matter: "радиус", "RADIUS", "реддит" are Redis;
"кавка" is Kafka; "опишка", "альпишка", "IP-шку" are the API; "вышки" are rigs; "кусочины" is
"вкусовщины"; "ZOO" is Sp. z o.o.; "рента" is margin. Not identified: "BlinkTech" (00:05:15), "Ваня"
(00:13:38).

## Summary

Alexey Gamanovich had objected to Redis in the mobile team's architecture; Arseniy held a session with
the mobile team and they agreed to go without it for now - direct writes to the API, with Kafka or
horizontal scaling if a need appears. Mikhail and Arseniy see the volumes as small; Anton suggested a
load test, Mikhail would leave it for later. The SOW's Arabic translation was done by hand and checked
by Mikhail with Claude. The contract's risks - fixed dates, broad liability - were gone over again: a
leap of faith on the client relationship. Arseniy and Mikhail wait for news on the contract from Anton
or Kavalchuk.

## Decisions

- Redis out for now: "Решили, типа, идти без него. Но, как сказать, вот архитектура, которая есть, это
  же первое такое приближение ... Если вдруг такая необходимость возникнет, то подключим там, ну, может,
  не RADIUS, а кавку" (Arseniy, 00:00:56). Agreed with the mobile team: "Мобильщики сказали, окей, нам не
  принципиально, мы можем идти без него" (00:00:56). No deciders named.

## Agreements with the client

None - internal meeting.

## Internal agreements

None beyond the decision above.

## Actions

None stated. Anton's load test of "30 вышек одновременно" (00:06:58) was left for later: "нам этим
надо будет заниматься, если делать нечего будет" (Mikhail, 00:07:23).

No Jira keys yet; there is no board.

## Questions raised

- Whether the contract goes to the client first or is signed and attested on our side first (Anton,
  00:09:38; Mikhail, 00:09:47). Overtaken: the client had signed on 7 October
  ([[2025-11-25 Contract chat - rendering 4]] 2026-10-12 10:01, 12:22).

## New scope mentioned

None.

## Proposed changes

In the table of [[2026-10-13 Optimum Three Caballeros call - minutes]], which covers this call, the
call of 13 October and part 4 of the contract chat: rows 11 (Redis), 19 (the translation) and 22
(liability and margin).
