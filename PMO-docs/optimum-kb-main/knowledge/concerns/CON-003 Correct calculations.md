---
type: concern
id: CON-003
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: quality
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-11-05 WBS sent to the client - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 1]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
  - "[[2025-11-25 Contract chat - rendering 1]]"
  - "[[2025-11-25 Contract chat - rendering 2]]"
  - "[[2025-11-20 Client formula and chart samples - rendering]]"
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
  - "[[2026-11-02 Client sample daily mud reports - overview]]"
  - "[[2026-11-02 Client sample end-of-well recap - rendering]]"
capabilities:
  - "[[CAP-005 Mud engineering calculations and simulation]]"
tags:
  - formulas
---
# CON-003 Correct calculations

## What must hold

The calculations give the right result for the client's formulas, on the desktop, offline.

## Why

Alexey: "В ядре всей этой системы находятся некие формулы" - primary data comes in, is recalculated
by formula, and the result is visualised and synced ([[2026-09-25 Optimum Eng sync - transcript]]
00:00:04). Arseniy judges the formulas simple - fractions and brackets, reference-type percentages,
2D dependency graphs (00:08:12). Both views stand; they are not in conflict.

The client wants derived values computed on save - "Yes"
([[2025-10-29 Client answers to the Q&A register - rendering]] E.21) - and a long list of inputs for
hydraulics (E.25). On the first call they explained the calculations; the notes point to the recording:
"(see details, record 47:00 explanation)" ([[2025-10-22 First call with OES - notes]] key point 5).
The recording has no transcript.

Added 2026-10-02, from the call of 1 October ([[2026-10-01 Optimum Three Caballeros call - transcript]]):
the case to guard against is a right formula implemented wrong - "Фундаментальная формула не может
поменяться, но то, как мы ее написали и имплементировали, может" (Anton, 00:15:35) - and, by the team's
reading, its losses are ours: "По текущим контрактам все эти убытки, за них несем ответственность мы"
(Mikhail, 00:16:00; [[COM-017 Liability, indemnity and force majeure]], [[K-2 Losses from a calculation defect fall on us]]).

## Affected requirements

- [[REQ-001 Record and calculate a shift without internet]]
- [[REQ-007 Derived values and standard calculations]]
- [[REQ-008 Fluid hydraulics simulation]]

## Treatment

A BA picked to work out the formulas (00:00:04, 00:07:05), and a review of Arseniy's formula analysis
with Alexey (00:05:03). No Decision yet.

The formulas come from the client: "Efforts for calculationg and modelling features are assessed by
assuming the Client provides Innowisewith clear formulars to be used"
([[2026-09-25 v1 WBS - rendering]], Assumptions & Risks 12). The SOW v10.4 makes it the client's: "The Customer shall provide the Contractor
with clear formulas, calculation logic, algorithms, and related business rules", and "deriving or
validating the engineering formulas themselves is the Customer's responsibility"
([[2026-06-15 SOW v10.4 - rendering]], assumptions and Milestone 5); see
[[COM-008 Client cooperation and dependencies]].

What the client was shown (added 2026-09-28, batch 4): the WBS sent on 5 November 2025 estimated the
calculations and the simulation for one algorithm each - "Due to uncertainty regarding the complexity of
calculations/simulation and the number of algorithms required, the efforts were accounter per 1
algorithm (rows 54-56 of Development tab)" ([[2025-11-05 WBS sent to the client - rendering]],
assumption 26). The v1 WBS ([[2026-09-25 v1 WBS - rendering]]) has no such assumption. How many formulas and algorithms the client will
supply is not stated in any source ingested so far.

The initial estimates, as history (AGENTS.md rule 6), in hours, min to max as the sheets have them.
Front end and back end of the desktop app (in the version sent to the client, the "Application"
columns, desktop and mobile); the UI/UX and BA hours are the same in both versions.

| Line | v1 WBS, Development Flutter | WBS sent to the client, Development |
|---|---|---|
| Derived Value Calculation | FE 12 to 16, BE 12 to 14 (row 58) | FE 6 to 8, BE 6 to 8 (row 54) |
| Standard Engineering Calculator | FE 48 to 56, BE 48 to 64 (row 59) | FE 12 to 16, BE "-" (row 55) |
| Simulation: Fluid Hydraulics | FE 80 to 88, BE 56 to 72 (row 60) | FE 24 to 32, BE "-" (row 56) |

From the presale chat (added 2026-09-28, batch 5):

- Why one algorithm: "нам все равно придется клиенту отдать таблицу в кликабельном виде, чтобы он мог
  прикинуть разработку в зависимости от количества алгоритмов, потому что у нас эффорт за один и мы не
  знаем сколько их. Если не приложить таблицу wbs, у него может сложиться ложное представление, что это
  тотал цена, а на деле калькуляция и моделирование могут оказаться самыми дорогими и времязатратными по
  факту" (Marina Zaretskaya, [[2025-10-20 Presale chat - rendering 1]] 2025-11-05 10:08).
- What we asked for: "образцы расчетов (к примеру, пошарить одну из икселей, которые они сейчас юзают) и
  используемую для них нормативную документацию", and how the expected charts look
  ([[2025-10-20 Presale chat - rendering 2]] 2025-11-18 08:37). The client's materials came on
  2025-11-20 (12:21): [[2025-11-20 Client formula and chart samples - overview]].
- How the team read them. Back end: "там получается 4 сложных формулы (\*6=24), 3 простых (\*3=9), 2
  графика (\*6=12) и 1 таблица общая ... ~75 часа, и я бы закладывал ещё побольше", against the
  "Dashboard View как 36-48" estimated, "понадобится под 100" (Artsiom Bulakh, 14:11). Front end: "По
  Application FE надо докинуть 100, тут не совсем стандартные графики, на такие нет библиотек у MAUI,
  придется рисовать самим" (Vitaly Ponteley, 14:41). The consultant: "Здесь разной сложности формулы. По
  некоторым я проконсультировать могу, по другим можно найти помощь у моих бывших коллег", and "Не нашел
  описания логики моделирования" (2025-11-24 12:37). Risk, in Artsiom's words: "надо понимание, чтобы
  закодить без ошибок, частично решается человеком, который им просто проконсультирует" (2025-11-20
  14:13).

What the client said about the calculations during the contract talks (added 2026-09-28, batch 6;
[[2025-11-25 Contract chat - rendering 1]]):

- 23 December 2025: "Please remove the words 'quick' and 'standard,' and retain only 'engineering
  calculations,' to avoid ambiguity regarding the depth of the calculations. Additionally, please add a
  section outlining the essential engineering calculations and modeling activities, noting that these
  should be included but not limited to the listed items." (2025-12-23 08:36)
- 5 January 2026: "Regarding the engineering calculations and modeling activities, we were referring to
  the formulas and diagrams that we had already shared which were provided as examples. As mentioned by
  Anton, the full set of calculations and modeling activities is intended to be defined, detailed, and
  completed during the discovery stage." (2026-01-05 10:59)
- The BA estimate for the mathematical part, May 2026: "по скромным подсчетам это примерно дифицит в 10%
  по БА эфорту" (Anton Soshnikau, [[2025-11-25 Contract chat - rendering 2]] 2026-05-18 16:14).

What the client's samples give and do not (added 2026-09-28, batch 7;
[[2025-11-20 Client formula and chart samples - rendering]]):

- Ten images: two pages of retort solids equations, five hydraulics procedures, three screens of a
  hydraulics program. Artsiom's count above ("4 сложных формулы ... 3 простых ... 2 графика ... 1
  таблица общая") adds up to ten; which image he counted as which is not stated.
- No source is named, and no normative documentation came with them, though we asked for it
  (2025-11-18 08:37). The numbering (Figures 2-1 to 2-5, Equations 10-2 to 10-8) and Figure 2-2's
  pointer to a "Figure 3-1" that was not sent suggest pages of a longer manual.
- No units on the procedures, and their constants (0.052 in the ECD step, 0.408, 928, 25.81, 2.45; 3.50
  in Equation 10-8) hold only in the units they were written for (evaluated):
  [[REQ-018 Units of measure and conversion]].
- Two rheological models: the procedures use the power law, the program screens Herschel-Bulkley:
  [[QUE-008 Which rheological model the hydraulics must use]].
- Defaults for unknown densities are part of the formulas ("use 2.6 if unknown", "use 0.84 if
  unknown"): [[REQ-007 Derived values and standard calculations]].
- A possible check case (envisioned): image 8 gives one well's inputs (fluid, rheology, drill string,
  casing, flow rates) and outputs (pressure losses, ECD), and is consistent in one check (PV 32 = 92 -
  60, YP 28 = 60 - 32 from its Fann readings). It could test the hydraulics once the client confirms the
  model and what produced the screen.

The formula set (added 2026-11-02): not sent with the sample reports - "As for the formula set,
we'll work on compiling it and share it with you at a later stage" (Ms. Zahra, 2026-11-02 07:20 UTC,
quoted in [[2026-11-02 Client sample daily mud reports - overview]]), after Ms. Ayaa had written on
1 November that it would come ahead of the meeting. No sample prints a formula; one standard is
named, "Interval Dilution factor | 0.07 | API 13-C, 5.4.9"
([[2026-11-02 Client sample end-of-well recap - rendering]] [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=28|p28]]).

Whether past results are recalculated when a formula or threshold changes: [[QUE-010 Are past results recalculated when a formula or threshold changes]] (added
2026-10-02).

Who checks the formulas, the SOW against what the client said on 20 October:
[[COM-008 Client cooperation and dependencies]] (added 2026-10-30).
