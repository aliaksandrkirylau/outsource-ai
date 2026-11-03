---
type: decision
id: DEC-001
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: business
deciders:
  - human:alexey.gamanovich
  - human:mikhail.andrushkevich
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2026-09-25 Optimum Eng sync - minutes]]"
  - "[[2025-11-25 Economy chat - overview]]"
  - "[[2025-11-25 Contract chat - rendering 1]]"
valid_from: 2026-09-25
tags:
  - quality
  - economy
---
# DEC-001 Delivery quality over margin

## Context

Why we take the project: a reference and an entry to the MENA oil and gas market, where the local
companies know each other, rather than commercial success (Alexey relaying Snotov,
[[2026-09-25 Optimum Eng sync - transcript]] 00:24:34). The contract is fixed price and the
economics are tight after a large discount (00:26:11). So the recurring choice is between saving
hours and building it properly.

How tight, without figures (added 2026-09-28, batch 6). In November 2025 the presale margin was
already "ниже допустимой нормы" (Yana Hotuleva, [[2025-11-25 Economy chat - overview]], 2025-11-26).
Management then conceded on rates: "руководством было принято решение идти на уступку по рейтам и
брать проект с учетом необходимости развития домена нефтянки и расширения нас в регионе" (Marina
Zaretskaya, [[2025-11-25 Contract chat - rendering 1]] 2025-12-03 10:06). In May 2026: "Для подписания
скидку и давали" (Matvey Matveev, economy chat, 2026-05-08).

## Options considered

1. Build to the estimate even when that means a crutch - keeps the economy. Lost: "Он приведет к
   тому, что клиент будет гарантированно недоволен результатом, и мы не получим то, что хотим"
   (Mikhail, 00:28:16).
2. Spend more hours where needed and build it properly - the client is satisfied. Chosen.

Anton's framing: "За 20 часов мы типа пилим жесткий костыль здесь ... если мы потратим 40 часов,
мы можем сделать получше и клиент будет доволен" (00:27:41).

## Decision

No minimal or crutch implementations to save hours. The priority is delivery the client is very
satisfied with, over keeping the margin (Anton, 00:25:42; Mikhail, 00:28:16; Alexey: "Гуд",
00:28:34).

## Rationale

A dissatisfied client defeats the reason for taking the project; the reference value depends on
delivery quality, not on margin.

## Consequences

- Downside: hours above the estimate come out of an already tight economy.
- New obligation: scope discipline matters more - how small change requests are handled is open in
  [[DEC-003 Handling small change requests]].
- Hard to reverse once the client has seen the quality level.
