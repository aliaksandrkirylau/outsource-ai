---
type: question
id: QUE-010
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
asks: client
sources:
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
tags:
  - calculations
  - formulas
  - thresholds
---
# QUE-010 Are past results recalculated when a formula or threshold changes

## Question

When a new desktop version brings changed formulas, coefficients or thresholds, must the results
already computed at the rig be recalculated from the stored inputs?

Raised by Alexey Gamanovich: "нужно ли, как те результаты, которые ранее были по старым формулам
отчета, обсчитаны, иметь возможность пересчитать по новым формулам? То есть, грубо говоря, система
должна хранить оригинальный слепок, первичных данных, чтобы всегда иметь возможность переранить этот
слепок данных, но через новую формулу" ([[2026-10-01 Optimum Three Caballeros call - transcript]]
00:12:26). Arseniy Klimenko: "надо этот вопрос подумать и с ними обсудить" (00:13:34).

## What it blocks

The data model of the calculation lines, WBS:Development Flutter!58-60 (derived values, the standard
calculator, the hydraulics simulation): whether raw inputs and the formula version are kept with every
result. [[CON-003 Correct calculations]],
[[DEC-006 Calculations run in the desktop app, formulas fixed in the code]].

## Options

1. Recalculate history: keep the raw inputs and re-run them under the new version (Alexey, 00:12:26).
2. Apply new values from then on, with no batch recalculation. Mikhail's expectation: formulas
   "меняться, скорее всего, не будут. Но там упоминалось, что будут меняться треш-холды, какие-то
   границы, какие-то лимиты. То есть, условно говоря, раньше был коэффициент 2.75, а потом ... вместо
   2.75 используют 2.71"; "Это был какой-то batch job, который должен перелопатить все данные и
   пересчитать по-новому. Скорее всего, такого не будет." (00:14:13). Arseniy: the formulas are physics;
   the unit of measure or the decimal places may change, the formula itself "вряд ли" (00:13:34).
3. Keep each result with the version it was computed with, and recalculate only on request (our
   option, envisioned).

Why it matters beyond a formula change: "Фундаментальная формула не может поменяться, но то, как мы ее
написали и имплементировали, может" (Anton Oparienko, 00:15:35). Without option 1 or 3, a defect can be
fixed only going forward; [[K-2 Losses from a calculation defect fall on us]].

## Answer

Not answered. For the client.
