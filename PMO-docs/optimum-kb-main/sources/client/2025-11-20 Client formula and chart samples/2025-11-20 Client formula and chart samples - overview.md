---
type: source
kind: client-material
date: 2025-11-20
original: https://drive.google.com/drive/folders/1pC29fiMRRpXLm4ikHdjY4qJbZyH8TFKx
received_from: the client, shared with Sales; posted in the presale chat by Polina Yanovskaya on 2025-11-20
purpose: the client's example formulas and charts for the calculations and the hydraulics simulation, which the estimate of those lines was checked against
supersedes:
procedure_version: b4cb7da
---
# 2025-11-20 Client formula and chart samples - overview

kind: client-material (`sources/client/`). original: the Drive folder "materials", 20 PNG files, each
last edited by Polina Yanovskaya on 2025-11-20 between 12:19 and 12:21 UTC. Rendering:
[[2025-11-20 Client formula and chart samples - rendering]]. The ten full-size images are stored next to
it, renamed "2025-11-20 Client formula and chart samples - image 01.png" to "image 10.png" in the order
of the table below, and embedded in the rendering (2.4 MB, the largest 440 KB); the thumbnails stay in
Drive.

## What it is

What the client sent when we asked, on 2025-11-18, for "образцы расчетов (к примеру, пошарить одну из
икселей, которые они сейчас юзают) и используемую для них нормативную документацию" and for how the
charts expected in the modelling module look (Marina Zaretskaya,
[[2025-10-20 Presale chat - rendering 2]] 2025-11-18 08:37). Polina posted the folder on 2025-11-20
12:21: "Нам пошарили материалы"; Marina passed it on as "примеры расчетов для модуля моделирования и
калькуляций и образцы графиков" (12:33). The client later called them "the formulas and diagrams that
we had already shared which were provided as examples"
([[2025-11-25 Contract chat - rendering 1]] 2026-01-05 10:59).

Ten images, each with a 256-pixel thumbnail (same aspect ratio, not rendered):

| # | Image | Kind |
|---|---|---|
| 1 | Equations 10-2 to 10-4 (volume percent water, oil, retort solids) | formula page |
| 2 | Equations 10-5 to 10-8 (suspended, low-gravity and weighting solids, concentrations) | formula page |
| 3 | Figure 2-1: Annular Pressure Drop and ECD | calculation flowchart |
| 4 | Figure 2-2: Critical Velocity and Pump Rate | calculation flowchart |
| 5 | Figure 2-3: Drillstring Pressure Drop | calculation flowchart |
| 6 | Figure 2-4: Swab and Surge Pressures | calculation flowchart |
| 7 | Figure 2-5: Slip Velocity and Hole Cleaning | calculation flowchart |
| 8 | Hydraulics summary of one well at ten flow rates | program screen, tables |
| 9 | Surge: Depth Vs Maximum Trip Speed, and a Tripping In Table | program screen, chart and table |
| 10 | Inclination, Hydraulics Operating Window, Numerical Data | program screen, charts and tables |

The folder names no source. The file names look machine-made ("Dating luil-40.png",
"100-108-918s-1214a-o-polval-34.png") and carry numbers 24 to 43, as if the images were cut out of a
longer document; one name has a character-set error ("ΓåÆ-Fieto-24.png"). The numbering of the
figures and equations (chapters 2 and 10) and Figure 2-2's pointer to a "Figure 3-1" that is not in the
folder also point to a longer manual. The screens do not name the program; they name "AutoTrak" (a
pressure-loss line), "ATK - 9-1/2" ATK G3" (a drill string item) and "PERFORMAX" (the mud system).
Images 8 and 9 show the same well (casing to 5271.00 ft, total depth 10000.00 ft); image 10 shows
another (measured depth to about 5300 ft, mud density 78.00 lb/ft^3).

On 2026-09-25 Arseniy's pack in the [Core] chat linked "the client's materials folder" with the
current WBS ([[2026-09-25 v1 WBS - overview]]).

## How far to trust it

High for what the client computes and draws today and what it calls things (`sources/client/AGENTS.md`).
Examples, not the required set: "provided as examples", and "the full set of calculations and modeling
activities is intended to be defined, detailed, and completed during the discovery stage" (the client,
2026-01-05 10:59). A formula here becomes a requirement only once the client confirms it; units and
model need the client's subject expert.

The rendering is ours: typeset formulas written as one line each, checked against the images, with the
two-way readings marked. Nobody codes from it: code is written from the formulas the client confirms.
The images are probably from a published manual and a commercial program; their copyright is not
checked. Anton's call (2026-09-28): the images come into the KB as a reference copy for internal use
only, never in an export (`procedures/ingest.md` step 2, changed the same day).

## Not for

The complete or required list of calculations, the required chart designs, a report layout, or the
values of the curves (described, not digitised).

## Removed at ingest

Nothing: the images hold no money, personal data or credentials. Each of the ten was looked at, image
by image, by claude-code/claude-opus-5-5 before it was stored; the money screen cannot read an image.
The ten thumbnails are not rendered or stored; they are smaller copies of the ten images. The chart
curves are described, not digitised.

## Summary

Two families of calculation and three screens of a hydraulics program.

- Solids analysis from the retort (images 1, 2): volume percent water, oil and retort solids, then
  suspended solids, low-gravity solids and weighting material, and their concentrations in lb/bbl, from
  the retort volumes, the chloride concentration and the fluid weight, with default densities where
  unknown. The client's daily report has the inputs (Retort Water %, Retort Solids %, Chlorides mg/l)
  and an empty "Solids Analysis" block ([[2025-10-29 Client sample daily report - rendering]] rows 20,
  40, 42, 44).
- Hydraulics, step by step (images 3 to 7): annular pressure drop and ECD, critical velocity and pump
  rate, drillstring pressure drop, swab and surge pressures as EMW, slip velocity and hole cleaning. All
  use the power-law parameters n and K from the Fann readings, and one friction-factor scheme (laminar,
  transitional, turbulent).
- Program output (images 8 to 10): pressures, ECD and bit hydraulics at ten flow rates; surge pressure
  against trip speed with a safe and an unsafe area by depth; and the "Hydraulics Operating Window",
  pressure and ECD against flow rate with the maximum pump pressure and the required flow rate, next to a
  drawing of the well and its inclination.

Our reading (evaluated):

- Two rheological models: the flowcharts use the power law, the screens say "Rheological Model
  Herschel-Bulkley" (K, N, YP). The client has not said which the app must use.
- The flowcharts state no units, and their constants (0.052 in the ECD step, 0.408, 928, 25.81, 2.45,
  and 3.50 in Equation 10-8) hold only in the units they were written for. The screens give mud weight
  and ECD in lb/ft^3, Equation 10-6 the fluid weight in lb/gal, the daily report ECD in ppg.
- The operating window chart is what the client described on the first call: "there should be flow it
  window that they should be operating within" ([[2025-10-22 First call with OES - transcript]] 0:52:09).
- Image 8 is consistent in one check: PV 32 = 92 - 60 and YP 28 = 60 - 32 from its Fann readings.
- Artsiom Bulakh's count on 2025-11-20 (14:11), "4 сложных формулы (\*6=24), 3 простых (\*3=9), 2
  графика (\*6=12) и 1 таблица общая", adds up to ten, the number of images. Which image he counted as
  which is not stated.

## Proposed changes

Batch 7 (client images), one table. Source keys:
R = [[2025-11-20 Client formula and chart samples - rendering]], image number;
C2 = [[2025-10-20 Presale chat - rendering 2]];
K1 = [[2025-11-25 Contract chat - rendering 1]];
T = [[2025-10-22 First call with OES - transcript]];
D = [[2025-10-29 Client sample daily report - rendering]], row;
QA = [[2025-10-29 Client answers to the Q&A register - rendering]];
A = [[2025-12-30 Answers to the client's questions - rendering]].

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | update | REQ-007 Derived values and standard calculations | The client's example derived values: the retort solids analysis, Equations 10-2 to 10-8, from retort volumes, chloride (mg/L) and fluid weight, with defaults ("use 2.6 if unknown", "use 0.84 if unknown", "use 4.2 for barite and 5.0 for hematite"). The daily report has the inputs and an empty "Solids Analysis" block. Whether they run on save or in the calculator is not stated | extracted; evaluated (the daily report link) | in WBS Development Flutter!58 (unchanged) | R 1, 2; D 20, 40, 42, 44 | applied 2026-09-28 |
| 2 | update | REQ-008 Fluid hydraulics simulation | What the samples show: five calculation procedures (annular pressure drop and ECD, critical velocity and pump rate, drillstring pressure drop, swab and surge, slip velocity and hole cleaning) and three program screens. The "Hydraulics Operating Window" is the "flow it window" of the first call. The screens' inputs are the ones the client listed (casing, open hole, drill string, fluid and rheology, flow rate, bit, pore and frac pressure). Figure 2-2 needs a "Figure 3-1" that was not sent | extracted; evaluated (the first call link) | in WBS Development Flutter!60 (unchanged) | R 3 to 10; T 0:52:09; QA E.25 | applied 2026-09-28 |
| 3 | update | CON-003 Correct calculations | "they are stored in batch 7" becomes the link. What the samples give and do not: no source or normative document named (we asked for it on 2025-11-18); no units on the flowcharts, whose constants fit particular units; two rheological models (row 7); defaults for unknown densities. Image 8 carries one well's inputs and outputs, consistent in the PV/YP check: a possible check case once the client confirms what produced it. Artsiom's count adds up to the ten images | extracted; evaluated; envisioned (the check case) | - | R; C2 11-18 08:37, 11-20 14:11; K1 2026-01-05 10:59 | applied 2026-09-28 |
| 4 | update | QUE-003 Do calculations and modelling need 3D or complex visuals | "stored in batch 7" becomes the link. The chart samples are 2D x-y charts - one with two vertical axes and five series, one with filled areas and a reversed axis - and a drawing of the well with its inclination (the consultant's "наверно только конструкция скважин"); nothing 3D or animated. Still open: they show the client's current program, not what the client needs | evaluated | blocks Development Flutter!60 (unchanged) | R 9, 10; C2 11-24 12:37 | applied 2026-09-28 |
| 5 | update | REQ-018 Units of measure and conversion | The samples mix units: mud weight and ECD in lb/ft^3 on the screens, fluid weight in lb/gal in Equation 10-6, ECD in ppg in the daily report; g/cm^3, mg/L, lb/bbl, psi, USgal/min, ft, in, bbl, s/std. The formulas' constants hold only in the units they were written for, which the flowcharts do not state | extracted; evaluated (the constants) | in WBS Development Flutter!54 (unchanged) | R 1 to 10; D 25, 43, 44 | applied 2026-09-28 |
| 6 | update | DEC-006 Calculations run in the desktop app, formulas fixed in the code | Context: the "algorithms and formulas you shared" of our answers (2025-12-30) and the client's "formulas and diagrams that we had already shared" (2026-01-05) are these samples, the only formulas the stored sources show the client sending before then | evaluated | - | A Page 2; K1 2026-01-05 10:59 | applied 2026-09-28 |
| 7 | new | QUE-008 Which rheological model the hydraulics must use | The flowcharts use the power law (n and K from the Fann 600/300 and 300/3 readings); the screens use "Herschel-Bulkley" (K, N, YP), shown as a setting. Options: power law; Herschel-Bulkley; both, the engineer choosing. asks: client | evaluated | blocks the acceptance criteria of Development Flutter!60 | R 3 to 8 | applied 2026-09-28 |
| 8 | new | TRM-009 ECD | Equivalent circulating density: the fluid's density plus the annular pressure loss above a depth, expressed as a density; Figure 2-1 step 11, "ECD = P_aT / ((0.052)(TVD)) + ρ". Used in the daily report (ECD @ Bit Depth, ECD @ Casing Shoe, ppg) and on the screens (with and without cuttings, at the casing shoe and the bottom, lb/ft^3). Not ESD (static) or EMW (swab and surge). The sources write only "ECD"; the expansion is the industry's | extracted; evaluated (the expansion) | - | R 3, 6, 8, 10; D 43, 44 | applied 2026-09-28 |
| 9 | update | REQ-017 Report on a single calculation or simulation | The three screens are output pages of a hydraulics program, one calculation per page with tables and charts; the client sent them as examples of calculations and diagrams, not as a report layout | evaluated | change request candidate, nearest Development Flutter!67 (unchanged) | R 8 to 10; K1 2026-01-05 10:59 | applied 2026-09-28 |
| 10 | link swap | 2025-10-20 Presale chat - overview; 2025-10-20 Presale chat - rendering 2 | "The client's materials folder comes in batch 7" (overview) and "to be stored in batch 7" (rendering 2, the 2025-11-20 12:21 attachment line) become links to this overview. Stored sources: link swaps only, as in batch 6 (finding 51) | - | - | - | applied 2026-09-28 |
| 11 | no material | COM-008 Client cooperation and dependencies | The client still owes the formulas; these are "provided as examples". No change to what is owed | - | - | K1 2026-01-05 10:59 | recorded 2026-09-28, no note |
