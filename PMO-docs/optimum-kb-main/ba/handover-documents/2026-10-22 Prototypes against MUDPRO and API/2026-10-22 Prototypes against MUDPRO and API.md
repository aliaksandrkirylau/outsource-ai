# 2026-10-22 Prototypes against MUDPRO and API

Anton's working note for Mikhail, the BA and the TL. Written by Anton's agent
(claude-code/claude-opus-5-5) on 22 October. It checks the two prototypes against
[[2026-10-21 MUDPRO research]] and [[2026-10-22 API standards research]], before the client sends more
material. It is working material, not evidence (`ba/AGENTS.md`; moved from `pm/` on 29 October). Nothing here is ingested, no typed note
changes, and neither prototype was changed. Everything below is our conclusion (evaluated). Figures
marked "our arithmetic" come from the two scripts in this folder ("How the numbers were made").

The prototypes checked:

- **OE prototype** (Mikhail, 14-15 October): [[OE prototype - read me]], with its
  [[OE prototype - calculation notes]] and [[OE prototype - issues, inconsistencies and client questions]].
- **Discovery prototypes v0** (Anton, 16-18 October): [[2026-10-18 Discovery prototypes v0 - README]].

## What they are built on

Both are built on the client's presale material.

| | OE prototype | v0 |
|---|---|---|
| Mud check fields | Daily.xlsx mud properties ([[2025-10-29 Client sample daily report - rendering]] rows 19-44), plus funnel viscosity from its "User Defined Properties" and retort oil | Daily.xlsx rows 19-44, field for field |
| Job or well header | Daily.xlsx header (desktop plan, S-10 in the issues note) | Daily.xlsx rows 2-6 |
| Calculations | Equations 10-2 to 10-8 (solids) and Figures 2-1 to 2-5 (hydraulics) from [[2025-11-20 Client formula and chart samples - rendering]]; weight-up from the OES-BAR data sheet; bit and surface losses are our standard formulas, because Figure 3-1 never came | None: an empty frame |
| Daily report | Daily.xlsx order; volumes, pumps, bit, solids control and costs left out | Not drawn |
| Rheometer speeds | 600, 300, 200, 100, 6, 3 | The same |

Daily.xlsx also lists 60 and 30 rpm readings (rows 36 and 37); neither prototype has them.

The two research notes mostly tell us what that material is:

- **Daily.xlsx is a water-based report.** Its property list closely follows the RP 13B-1 water-based
  test list.
- **The formula samples are the older power-law method.** It is the family RP 13D replaced in 2006. The
  client's own program screen (image 8) uses Herschel-Bulkley, the current RP 13D model.

The client called the samples "examples", not the required set (overview of the formula samples). So
both prototypes rest on examples, which is fine for discovery but has to be said when they are shown.

## Against the API note

### 1. Values the engineer types that API calculates

RP 13B-1 derives four of the values the prototypes ask the engineer to type:

- PV = θ600 - θ300
- YP = θ300 - PV
- excess lime = 0.26 × (Pm - Fw × Pf)
- retort solids = 100 - (oil + water)

What the prototypes do:

- **v0** has all four as typed fields (`rig-app/Main.dc.html` lines 383, 384, 390, 396). Its client
  question 11 assumes they stay typed, "as in today's report".
- **OE** types PV and YP and shows "PV / YP from dial" next to them (`source/MudCheckNew.dc.html`).
  Nothing checks that the two agree:
  - The demo hint on that screen says to change plastic viscosity to 30 so the flag disappears. The
    dial readings then still give 41.
  - The sample excess lime is typed as 0.3 lb/bbl. The formula gives 0.18 from the same check's Pm 1.2,
    Pf 0.6 and water 86 % (our arithmetic).
  - OE already calculates retort solids from oil and water, as API does.
- The client already said yes to derived values calculated on save (Q&A E.21, quoted in
  [[REQ-007 Derived values and standard calculations]]).

Proposal:

- Calculate the four on save and show them read-only.
- If the client wants them typed, warn when a typed value does not match the readings.
- Reword v0 question 11: "API derives these from the readings. Do you type them today, and do you want
  the app to calculate them?"

### 2. Water-based mud only

Both prototypes record the mud type on the job, but the mud check form does not change with it.

- RP 13B-2 adds tests for oil-based mud: electrical stability, oil/water ratio, whole-mud alkalinity,
  chloride and calcium, CaCl2 and water-phase salinity.
- MUDPRO's report has a different property list for each mud type.
- The client's program screen (image 8) is an oil-based well, as Mikhail's `calc/test.js` reads it.
- OE already has an "oil-based mud only" oil/water calculator that takes retort oil. v0's form has no
  retort oil field.

Proposal: the field list follows the job's mud type. Draw it once the client says which tests they run
for each mud type (already in the API note's questions). We could not read the RP 13B-2 sections that
define the oil-based calculations, so we should not guess them.

### 3. Hydraulics method: the largest effect

The OE engine (`calc/engine.js`) implements the client's Figures 2-1 to 2-5:

- power law, with the annulus from θ300 and θ3
- laminar friction 24/Re in the annulus
- the bit pressure drop with the 0.95 nozzle coefficient (constant 156)

We ran OE's test well DW-217 through RP 13D's Herschel-Bulkley set as the API note writes it (our
arithmetic). This shows the size of the difference, not a verified result. At 650 gal/min:

| | OE now (client's power law) | RP 13D Herschel-Bulkley |
|---|---|---|
| Drill string loss | 1,199 psi | 1,208 psi |
| Annular loss | 107 psi | 77 psi (28 % lower) |
| ECD at bit | 10.65 ppg | 10.58 ppg |
| Bit pressure drop | 918 psi | 866 psi (nozzle coefficient 0.98) |

The other flow rates (400 to 750 gal/min) show the same pattern: the annular loss is 27 to 29 % lower,
and the ECD at bit is 0.05 to 0.08 ppg lower.

- **Within one tolerance, not the other.** The ECD difference is within the "±0.3 ppg" that MUDPRO's
  vendor quotes, but the annular loss is far outside its "≤3 %".
- **Image 8 is a ready test case.** RP 13D's parameter formulas give the n and K on the client's program
  screen to within 1 %: flow behaviour index 0.691 against 0.689, consistency index 0.743 against
  0.749 (our arithmetic).
- **One mismatch to ask about.** The screen shows a yield stress of 9 (its "YP: 9.000"), where RP 13D's
  2θ3 - θ6 gives 8. A least-squares fit over all six readings also gives about 8, so we do not know how
  the program gets 9.

Proposal:

- Do not rebuild the hydraulics until the client answers
  [[QUE-008 Which rheological model the hydraulics must use]].
- Name the method on the hydraulics screen and on the report line, for example "client procedure, power
  law".
- Make the model a setting in the engine, so that a switch later is cheap.

### 4. Weight-up may be about 10 % too high

The calculator uses "Sacks of 50 kg OES-BAR per 100 bbl = 1472 (W2 - W1) / (35.05 - W2)"
(`calc/engine.js` line 140, screen 4.1).

- **What 1472 is.** It is 42 gal/bbl × 35.05 ppg (barite at SG 4.2), so the formula gives pounds of
  barite per barrel of mud. That is the same number as 100-lb sacks per 100 bbl, not 50-kg sacks.
- **The effect.** For 10.4 to 11.0 ppg on 820 bbl, the prototype says 302 sacks (15.1 t), rounded up.
  A mass balance gives 36.7 lb/bbl, which is about 273 sacks of 50 kg (13.7 t). Our arithmetic.
- **Not checked against the data sheet.** It is not public: on oes.com.sa's product page, "OES BAR"
  links nowhere. Mikhail, which copy did you use, and does it state the sack size?

An engineer will check this figure in their head, so it is worth settling before any demo.

### 5. Smaller items

- **Entry checks.**
  - OE checks each field against its own limits only. It does not block a 300 rpm reading above the
    600 rpm one; v0 does (lines 605-619).
  - Add the API note's checks: yield stress not above YP, oil plus water not above 100 %, and the two
    electrical stability readings within 5 % (oil-based).
  - Pf not above Mf is our inference from how the titration runs (Mf continues from the Pf end point).
    Confirm it before using it.
- **Reading precision.** v0's decimals already match API: density 0.1 ppg or 0.01 SG, filtrate 0.1 cc,
  cake in 1/32 in. OE's fields take free text.
- **Solids constant.** The client's sheet uses 3.50, the OFITE manual 3.49. The difference is small
  (low-gravity solids 98.1 against 97.8 lb/bbl on the OE sample, our arithmetic), but we need one
  agreed value. The filtrate density formula also differs between sources (API note).
- **Unit set name.** OE calls its US set "API (oilfield)" (Settings, web Thresholds). The client now
  uses "API" to mean standards compliance, so "Oilfield (US)", as in v0, is safer.
- **Method on every stored result.** OE already marks its results "Not verified - for discussion" and
  names the client's formulas. When a result is stored, it should also carry the method and its
  version ([[DEC-006 Calculations run in the desktop app, formulas fixed in the code]],
  [[CAP-010 Audit trail and change approval]]).
- **Calibration.** Neither prototype has it, and it is not in the WBS (OE I-05,
  [[REQ-016 Inventory of lab equipment and reagents]]). Leave it as a question.

## Against the MUDPRO note

MUDPRO shows the minimum an OES engineer already expects. Mr. Lawal asked for something better, "not a
copy", so this is a checklist, not a design.

### Report coverage

MUDPRO's daily report has ten sections. How the client's template and the two prototypes cover them:

| # | MUDPRO section | Daily.xlsx | OE prototype | v0 |
|---|---|---|---|---|
| 1 | Header | Yes, rows 2-6 | Yes | Job header |
| 2 | Wellbore and drill strings | Yes: drilling assembly, wellbore geometry, bit | Kept with the well as hydraulics inputs; not on the report | No |
| 3 | Drilling, volume, circulation | Partly: bit RPM, WOB, pumps, circulation times | No | No |
| 4 | Solids control equipment | Yes | No, marked "not yet" | No |
| 5 | Mud properties, up to 4 samples | Yes, 4 columns | Yes, 4 checks a day, water-based | Yes, 4 checks a day, water-based |
| 6 | Inventory | Yes | Yes | Not drawn |
| 7 | Treatments and remarks | Yes: drilling comments, treatment and recommendations | Comments | Flag reasons only |
| 8 | Volume tracking | Yes, and the "Vol Report" sheet | No | No |
| 9 | Hydraulics | Yes: velocities, critical velocity, bit hydraulics, n, k, ECD | Calculated block and simulation screen | No |
| 10 | Solids analysis, time distribution | Solids analysis; IADC hours | Solids analysis calculated; no time distribution | No |

Both prototypes say that sections 2 to 4 and 8 have no WBS line (OE S-11, v0 question 5). Keep it that
way. But an engineer will likely ask "where are my volumes?" first: MUDPRO will not let them start the
next report until the volumes balance. Have the answer ready ([[K-5 Scope grows through the prototypes]]).

### Other gaps

- **Copy the previous report.** This is MUDPRO's main time-saver, and neither prototype has it. It is
  cheap to draw, but copied values look measured. Mark them as copied until the engineer confirms them.
- **Stock between wells.** OE starts each well with a loadout entered product by product (S-15, I-14).
  MUDPRO carries the ending stock over as the next well's starting stock. Make carry-over the default
  (OE question Q-12 asks this).
- **Model choice.** MUDPRO offers Bingham plastic, power law and Herschel-Bulkley. That supports making
  the model a setting (item 3).
- **Units.** MUDPRO offers US oilfield, metric and custom. OE has three sets, the third "Mixed". v0 has
  two, the third open. This is a data point for [[REQ-018 Units of measure and conversion]].
- **Already in OE:**
  - range warnings, plus a low-stock minimum
  - section and well reports (MUDPRO's interval summaries and recap)
  - prices on the web only
- **Not drawn, as planned:** well comparison (OE I-05), WITSML export
  ([[REQ-019 API for other systems]]), the well as a template.

### Where we are already better

Make these explicit in both demos:

- automatic sync, instead of a case file e-mailed by hand
- out-of-range values flagged with the engineer's reason, and reviewed at HQ
- locked checks, approvals and an audit trail: the record controls ISO 9001 leans on, which the vendor
  material does not show
- once added, the method named on every result (item 5)

## What to change now, and what to hold

| Item | Prototype | Owner | When |
|---|---|---|---|
| Weight-up sack size (4) | OE | Mikhail | Now: check the data sheet |
| Derived PV, YP, excess lime, retort solids (1) | Both | Mikhail, Anton | Now |
| v0 question 11 reworded (1) | v0 | Anton | Now |
| Entry checks (5) | OE | Mikhail | Now |
| "API (oilfield)" renamed (5) | OE | Mikhail | Now |
| Method named on the hydraulics screen and report (3) | OE | Mikhail | Now |
| Field list by mud type (2) | Both | Mikhail, Anton | After the client lists the tests per mud type |
| Herschel-Bulkley, or a model choice (3) | OE | Mikhail, with the TL | After QUE-008 |
| Report sections 2-4, 8, 10 | Both | - | Only if scope allows (K-5) |
| Copy the previous report, carry-over of stock | Both | Mikhail, Anton | After discovery confirms them |

The OE read me says to agree which prototype goes to the client before either is shown. The two
overlap on the mud check, so the "now" changes should land in the one that goes.

## New questions for discovery

None of these blocks a WBS line, so they are not Question notes. The API and MUDPRO notes have the rest.

- Do your engineers type PV, YP, excess lime and retort solids today, or does a sheet calculate them?
- Which program made the hydraulics screens you sent, and how does it get its yield stress (9 on the
  screen, 8 from 2θ3 - θ6)?
- Do you read 60 and 30 rpm, as Daily.xlsx lists?
- Did your engineers copy the previous day's report in the tool you used before?

## How the numbers were made

Two Node scripts in this folder:

- `hb-compare.js`: runs the OE engine on its own test well, the same inputs as `calc/test.js`. It runs
  the same well through RP 13D's Herschel-Bulkley equations as the API note writes them, the turbulent
  friction factor included. It also prints the weight-up, solids-constant and excess-lime checks. Run
  `node hb-compare.js` from this folder.
- `img8.js`: the n, K and yield stress of the client's program screen (image 8), by RP 13D's formulas
  and by a least-squares fit.

Our implementation of the Herschel-Bulkley set has not been checked against RP 13D itself or a worked
example. Its figures show the size of the difference between the methods, not correct answers
([[CON-003 Correct calculations]], [[K-2 Losses from a calculation defect fall on us]]).
