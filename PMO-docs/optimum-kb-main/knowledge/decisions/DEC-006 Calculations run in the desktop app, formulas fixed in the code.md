---
type: decision
id: DEC-006
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: architecture
sources:
  - "[[2025-12-30 Answers to the client's questions - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
  - "[[2025-11-20 Client formula and chart samples - overview]]"
  - "[[2025-11-25 Contract chat - rendering 1]]"
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
capabilities:
  - "[[CAP-005 Mud engineering calculations and simulation]]"
tags:
  - calculations
  - offline
  - desktop
---
# DEC-006 Calculations run in the desktop app, formulas fixed in the code

## Context

Engineers calculate and simulate on rig computers that are often offline
([[CON-001 Offline operation and sync between rigs and HQ]]). The client asked in December 2025 "in
what situation would access to central server become necessary for the calculations and modeling?"
([[2025-12-30 Answers to the client's questions - rendering]], quoted in the comments). Treats
[[CON-001 Offline operation and sync between rigs and HQ]] and [[CON-003 Correct calculations]].

The client, answering the proposal (added 2026-09-28, batch 5): calculations and modelling, with
reporting, dashboards and inventory, "remain essential requirements for the desktop application"
([[2025-10-20 Presale chat - rendering 2]] 2025-11-24 12:10); see
[[DEC-005 Desktop at the rig, web app at HQ]].

The formulas the answers mean by "algorithms and formulas you shared" (Decision, below) are the client's
samples of 2025-11-20, the only formulas the stored sources show the client sending before then
(evaluated, added 2026-09-28, batch 7): [[2025-11-20 Client formula and chart samples - overview]]. The
client, on 2026-01-05: "we were referring to the formulas and diagrams that we had already shared which
were provided as examples" ([[2025-11-25 Contract chat - rendering 1]] 2026-01-05 10:59).

## Options considered

1. The calculation and modelling logic inside the desktop app, formulas fixed in the code. Chosen.
2. Formulas configurable in the web admin panel. Lost: "if in the future you decide to make the
   formulas flexible or allow different rate values via the Admin panel of the web application, the
   lack of connection to a central server may cause issues, as the calculations would no longer work
   offline in that scenario" (answers, Page 2).
3. Calculations on the central server. Lost for the same reason: it "will require evaluation of such
   calculations on central server" whenever data from the server or "online data from other job sites"
   is needed (answers, Page 2).

## Decision

"At this stage it is assumed that all calculation and modeling logic resides within the app code, and
using a central server for these calculations is not required ... (note - calculations will be
hardcoded based on algorithms and formulas you shared at the current version of the solution)"
([[2025-12-30 Answers to the client's questions - rendering]], Page 2). Told to the client in the answers
of 2025-12-30. The v1 WBS ([[2026-09-25 v1 WBS - rendering]]) has the same assumption (Assumptions & Risks 9) and the SOW v10.4 too ([[2026-06-15 SOW v10.4 - rendering]]). Who decided is not named in these sources, so no deciders.

Restated on 1 October as a working assumption (added 2026-10-02; [[2026-10-01 Optimum Three Caballeros call - transcript]]): "Пока что делаем strong
assumption, что в этой вебовской части пересчета формул нету, это делается на толстом клиенте" (Alexey,
00:09:32). Arseniy: "Если честно, надо уточнить. По-моему, только на десктопе было." (00:08:55);
Mikhail: "так как очень high-level scope описан, то такое исключать нельзя" (00:09:18).

## Rationale

Calculations must work with no connection.

## Consequences

- Downside: a formula change means a new desktop release installed on every rig computer, many of them
  offline; Zaretskaya's internal comment: "if formulas are required to be changed frequently it might
  have difficulties with desktop client update".
- Downside: nothing that needs other rigs' or live central data can be calculated at the rig.
- New obligation: the client supplies the formulas before they are coded (v1 WBS, Assumptions & Risks
  12); [[CON-003 Correct calculations]].
- Tension: the client's vision of AI-assisted scenario analysis and suggested actions
  ([[2025-10-22 First call with OES - transcript]] 0:47:25) may not fit fixed formulas;
  [[REQ-007 Derived values and standard calculations]].
- Hard to reverse once the calculation modules are built.
- Downside (added 2026-10-02): rigs on different app versions calculate with different
  implementations, "Нет центрального места, где одной транзакцией или одним диплойментом стабилизируется
  единообразность этой логики" (Alexey, [[2026-10-01 Optimum Three Caballeros call - transcript]] 00:09:32).
  Arseniy: "Как сделать это в виде расчетного двигателя, который может легко считать все актуальные
  изменения. Мы про это сейчас думаем." (00:11:38). Whether past results are recalculated: [[QUE-010 Are past results recalculated when a formula or threshold changes]].
- Open (added 2026-10-02): what-if forecasts on the management side; if they run on the web, "нам нужно
  знать формулы там, где это происходит" (Anton, 00:11:07). Not answered; the KB has "what if"
  scenarios only in the desktop hydraulics simulation ([[REQ-008 Fluid hydraulics simulation]]).
