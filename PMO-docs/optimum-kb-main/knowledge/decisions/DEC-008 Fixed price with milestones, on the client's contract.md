---
type: decision
id: DEC-008
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: business
sources:
  - "[[2025-11-25 Contract chat - rendering 1]]"
  - "[[2025-11-25 Contract chat - rendering 2]]"
  - "[[2026-09-07 Final contract - rendering]]"
valid_from: 2026-05-22
tags:
  - contract
  - fixed-price
  - payments
---
# DEC-008 Fixed price with milestones, on the client's contract

## Context

From November 2025 to May 2026 the deal was time and materials with a budget cap. PMO's finalisation of
28 November 2025: "TM with Budget CAP", with an advance payment
([[2025-11-25 Contract chat - rendering 1]] 2025-11-28 19:49; figures removed). PMO's reading in May
2026: "Контракт на проект рассматриваем как TM + CAP, где CAP - это, исключительно, верхняя граница
бюджета клиента", with no commitment "кроме как какой-то initial scope, в котором мы будем уверены на
100%" (Yauheni Krasner, [[2025-11-25 Contract chat - rendering 2]] 2026-05-12 07:44).

The client's drafts did not read that way. PMO's review of 6 May: "Очень верхнеуровневый scope и
deliverables при модели TM + CAP (по сути близко к FP)", and "Мы идем в проект с Фиксированным скоупом и
бюджетом без предварительной дискавери (будет выполнена внутри проекта), при этом проектная часть
описана хай-левел" (2026-05-06 14:53). Sales on 20 May: "Текущий вариант с “предварительными
договоренностями” и снятием с себя ответственности за ранее согласованный скоуп нерабочий. Клиент это
воспримет как попытку откатить все назад без конкретики." (Lizaveta Shauchenka, 2026-05-20 15:27)

## Options considered

1. Time and materials with a budget cap, on our frame and SOW: the model from November 2025 to May 2026.
   Lost: "клиент не примет такой договоренности. Потому решили выйти к нему с фиксой" (Lizaveta
   Shauchenka, 2026-05-21 11:27).
2. A new commercial proposal. PMO saw no point: "предлагать "новый" пропоузал не вижу смысла"; the
   original estimate showed nothing wrong ("криминала в оригинальной оценки не нашли"), and "с учетом
   нашей версии контракта у PM-а есть возможность вести переговоры по срокам, скоупу, "глубине фич" и
   бюджету" (Alexey Gamanovich, 2026-05-20 15:51).
3. Fixed price with milestones, on the client's contract adapted to our terms. Chosen.

## Decision

The call of 22 May 2026, in Yauheni Krasner's summary: "Формат - fixed price с milestone-ами. Используем
текущую версию контракта клиента, дорабатываем ее под свои условия." (2026-05-22 13:07). The call was
to include "Иван и Миша" (Alexey Gamanovich, 2026-05-21 12:15). Who decided is not stated, so no deciders
are named.

## Rationale

The client would not take time and materials, and the model it was offered already behaved like a fixed
price (options 1 and 2 above). The same call moved the desktop app to Flutter to lower the risk
([[DEC-007 Flutter for the desktop app]]) and set the economics to be recomputed, with a profitability
floor (figure in the P&L).

## Consequences

- The WBS stands as the requirements: "@Arseniy Klimenko подтвердил достаточность скоупа прописанного
  в SOW. Также получено подтверждение@Michael Labutin, что описание требований на основании WBS является
  достаточным для этого контракта." Everything outside it is a change request: "Все, что не в WBS —
  оформлять как Change Request" (2026-05-22 13:07; [[DEC-003 Handling small change requests]]).
- Downside: scope, budget and time are fixed before discovery, which runs inside the same six months
  ([[COM-001 Delivery within six months]]); the formulas are not known yet
  ([[CON-003 Correct calculations]]).
- New obligation: the SOW redone for fixed price, with a milestone and payment table (Yauheni Krasner,
  2026-06-12 10:11); see [[COM-012 Payment schedule]] and [[COM-020 Milestone plan and deliverables]].
- The second half, adapting the client's contract to our terms, did not hold: the client declined
  further changes and management decided to sign its final version
  ([[DEC-009 Sign the client's final contract as it stands]]). Whether DEC-009 supersedes this note in
  part is for the deciders.
- Hard to reverse: the contract is signed on these terms ([[2026-09-07 Final contract - rendering]]).
