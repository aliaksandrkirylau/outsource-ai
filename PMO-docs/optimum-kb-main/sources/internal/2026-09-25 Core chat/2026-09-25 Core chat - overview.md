---
type: source
kind: chat
date: 2026-09-25
original: https://chat.google.com/room/AAQAkfyHFwA
received_from: Google Chat space "[Core] Optimum engineering" (spaces/AAQAkfyHFwA), the delivery team's chat; read by Anton Oparienko's copilot on 2026-10-14
purpose: the delivery team's own working chat since the project was handed to it - what the three PMs shared, asked and agreed between the calls (Anton's ask, 2026-10-14, "may be other chats too")
supersedes:
procedure_version: 5d00575
---
# 2026-09-25 Core chat - overview

kind: chat, one part, rendered by `pm/seed-ingest-scripts/chat2md.mjs` from the Chat tool's output:
[[2026-09-25 Core chat - rendering 1]], 34 messages from 2026-09-25 11:53 to 2026-10-14 08:35 UTC. The
chat is still in use: the next ingest starts a part 2 after 2026-10-14 08:35.

## What it is

The chat Arseniy Klimenko opened on 25 September for the three people who took the project over after
the contract: Arseniy, Mikhail Andrushkevich and Anton Oparienko - "сделал нам чатик, чтобы удобнее было
обсуждать и шарить документы". It holds the links to the working documents (the SOW v10.4, the P&L, the
v1 WBS, the client's materials), short agendas for the daily calls, Anton's list of where the contract
and the SOW disagree, a P&L thread, the first solution diagrams, and Anton's update of the BA position
on 14 October.

People named by first name: "Леша" is most likely Alexey Gamanovich - the 29 September thread is about
the P&L and staffing, and on 12 October Anton asks whether Arseniy has anything from "в пятницу по
архитектуре с Лешей", the architecture talk in which Gamanovich objected to Redis
([[2026-10-12 Optimum Three Caballeros call - minutes]]). "Саша" is most likely Aliaksandr Kavalchuk,
the account manager, who wrote on 29 September that there was nothing to start until the SOW was
sent and signed ([[2025-11-25 Contract chat - rendering 4]] 2026-09-29 12:25). "Джонни" is Johni Algarbi, who translated
the SOW ([[2026-10-13 Optimum Three Caballeros call - minutes]] row 19). "Яна и Юля" (14 October) are not
identified in a stored source.

## How far to trust it

Internal, our own view (`sources/internal/`). Messages between three colleagues: what they knew and
planned on the day, not agreements with the client. The 28 September list of contract and SOW
disagreements was generated from this KB; the KB's notes, not the chat copy, are the reference.

## Not for

Money: the P&L is linked, not read, and the one rate figure is removed. Not for citing the BA position's
wording as a requirement of the project: it is a staffing text, kept in `pm/`.

## Removed at ingest

- A rate figure in Anton's message of 2026-09-29 10:24, replaced in square brackets. The hours figures
  stay.
- Reactions; blank lines inside messages.
- Left out: nothing (no bot, system or empty messages).

Not stored: the P&L (money; linked only); the two screenshots of 29 September (10:00, the P&L's hours;
10:26, unlabelled); the methodology document of 30 September
(Capability_Driven_AI_Delivery_Methodology_RU, about how we work, not the project). Arseniy's two
diagrams of 1 October are stored: [[2026-10-01 Solution vision diagrams - rendering]].

## Summary

25 September: Arseniy opens the chat with the working links - the SOW v10.4, the P&L, the current WBS
("смотрим на оценку с флатером"), the client's materials. 28 September: Mikhail's actions from the
call; RACI postponed. Anton posts the list of where the signed contract and the SOW v10.4 disagree, and
says the questions have to go to business development and the contract group. 29 September: Anton's
version of the P&L plan; Alexey (most likely Gamanovich) agreed to hold staffing while the account
manager says so, and set how money reaches the departments under fixed price - only as work is done
from money received, with resource managers warned up front of possible gaps. 30 September to 1 October:
the KB methodology and Arseniy's first diagrams. 5 October: Anton flags the regional conflict. 8 to
12 October: agendas, cancelled syncs, the SOW translation nearly done. 14 October: Anton's update of the
BA position for the staffing call - the project in a paragraph, full time at the start, location any,
working hours overlapping Saudi Arabia Monday to Thursday, clickable prototypes with AI, documentation
from approved prototypes.

## Proposed changes

In the table of [[2026-10-13 OE Big4 chat - overview]], which covers this chat, the OE Big4 chat, part 5
of the contract chat and the e-mail of 14 October. Source key there: CO.
