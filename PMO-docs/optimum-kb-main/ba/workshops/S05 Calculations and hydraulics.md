# S05 Calculations and hydraulics

Session plan, topic 5, week 3. One hour. Part of [[00 discovery-BA-plan]]. Working material, not evidence. Heavy: in the hour the numbered list, the
rheological model and who signs off; the formula detail goes in writing.

## Elicitation goal

A numbered MVP list of calculated values, calculators and hydraulics outputs; the rheological model;
who on their side signs off the test cases, and with what tolerance.

## Scope

- D3: WBS:Development Flutter!58 (derived values), !59 (calculator), !60 (hydraulics); built in M5
- [[REQ-007 Derived values and standard calculations]], [[REQ-008 Fluid hydraulics simulation]],
  [[CON-003 Correct calculations]], [[QUE-008 Which rheological model the hydraulics must use]],
  [[QUE-003 Do calculations and modelling need 3D or complex visuals]],
  [[CON-008 Compliance with ISO 9001, ISO 14001 and API standards]]

## Participants

Client: Mr. Lawal (the subject expert), a mud engineer. Ours: Anton, Leu, Mikhail (his calculation
engine).

## Preparation and inputs

- **Internal, before anything is said to the client:** how far we check the client's formulas.
  Mikhail and Kavalchuk decide ([[COM-008 Client cooperation and dependencies]],
  [[K-2 Losses from a calculation defect fall on us]]).
- **The full formula set** with the manual's name and edition, and worked examples (asked since
  18 November 2025). Without it, swap with S06.
- Prototype: values calculated on save next to the inputs; a weight-up and an oil/water ratio
  calculator; a hydraulics form with an output table at about 10 flow rates and an x-y operating
  window, power law, no 3D.
- A calculation specification skeleton: the numbered list from the WBS lines and their formula sheets.

## Agenda

| Min | Item | Fails without |
|---|---|---|
| 0-5 | Recap, goal | - |
| 5-20 | The numbered list: on save, calculators, hydraulics outputs | A1 |
| 20-32 | The rheological model and the standards | B1, B2 |
| 32-45 | Correctness: who signs off, tolerance, inputs stored | C1, C2, D1 |
| 45-55 | Click through | - |
| 55-60 | Next steps: the specification in writing | - |

## Questions register

Grouped by topic in agenda order; must-haves first. Blocks: the WBS line the answer is needed for, as its row in the WBS tab "Development Flutter" and a short name. When: Call, or Written after the session.

| ID | Question | Blocks | Must | When | Ahead | Source |
|---|---|---|---|---|---|---|
| | **A. The MVP list** | | | | | |
| A1 | Which values are calculated on save, which calculators are needed, and which hydraulics outputs? | 58 Derived values (desktop); 59 Engineering calculator (desktop); 60 Hydraulics simulation (desktop) | Yes | Call | - | Sheet D3 B1; [[REQ-007 Derived values and standard calculations\|REQ-007]], [[REQ-008 Fluid hydraulics simulation\|REQ-008]] |
| A2 | Confirm suggested treatments are out of scope. | - | - | Written | - | Sheet D3 L |
| A3 | Are calculator results saved to the job? Are what-if runs needed on the web? | - | - | Written | - | Sheet D3 L |
| | **B. Model and standards** | | | | | |
| B1 | Power law, Herschel-Bulkley, or the engineer's choice? When your procedures and API differ, which governs? (Results can differ by about 28%.) | - | Yes | Call | Yes | Sheet D3 B2; [[QUE-008 Which rheological model the hydraulics must use\|QUE-008]] |
| B2 | What does "API compliance" mean for the app: the test and calculation methods, or more? (Listen and log.) | - | Yes | Call | - | Sheet X3; [[CON-008 Compliance with ISO 9001, ISO 14001 and API standards\|CON-008]] |
| B3 | Which n and K go on the daily report: pipe or annulus? | - | - | Written | - | Sheet D3 B6 |
| | **C. Formulas and inputs** | | | | | |
| C1 | Which units does each formula expect? | - | Yes | Call | - | Sheet D3 B3 |
| C2 | Is the well's geometry, drill string and bit stored on the job, or entered for each run? | - | Yes | Call | - | Sheet D3 B4 |
| C3 | Do engineers type PV, YP, excess lime and retort solids today? | - | - | Written | - | Sheet D2 B8 |
| C4 | Some constants differ between sources (e.g. 3.50 vs 3.49 in Equation 10-8): which do we use? | - | - | Written | - | Sheet D3 L |
| | **D. Correctness and changes** | | | | | |
| D1 | Who signs off the test cases, and what deviation from your reference results is acceptable? | - | Yes | Call | Yes | Sheet D3 L; [[CON-003 Correct calculations\|CON-003]] |
| D2 | When a formula changes, are past results recalculated? | - | - | Written | - | Sheet D3 L; [[QUE-010 Are past results recalculated when a formula or threshold changes\|QUE-010]] |
| | **E. Charts** | | | | | |
| E1 | Are the operating-window and surge charts and a well drawing needed? (Simple charts only.) | - | - | Call | - | Sheet D3 B5; [[QUE-003 Do calculations and modelling need 3D or complex visuals\|QUE-003]] |

Materials to request: the missing Figure 3-1; units per formula; the name of the hydraulics program in their screenshots and a few exports, and how it gets its yield stress; product specific gravities and data sheets with their weight-up formulas (whether the OES-BAR formula counts 50-kg sacks); licensed copies of the API documents; a named subject expert (sent ahead) (Sheet D3).

## Confirm with the client

| Ours | Plain wording |
|---|---|
| [[REQ-007 Derived values and standard calculations]] | The app calculates the agreed values on save, by your formulas, and they cannot be typed. |
| [[REQ-008 Fluid hydraulics simulation]] | The hydraulics outputs agreed here, by the model agreed here, with simple charts. |
| The list | The calculations in the first release are the numbered list; anything else is a change. |

## Outputs

- **Calculation specification** into REQ-007 and REQ-008: numbered list, inputs, outputs, units, source,
  worked examples, tolerance, who signs off; sent for written sign-off.
- KB: [[QUE-008 Which rheological model the hydraulics must use]] answered or narrowed;
  [[QUE-003 Do calculations and modelling need 3D or complex visuals]], [[CON-003 Correct calculations]] updated.
- The compliance expectations to Mikhail and Kavalchuk.
