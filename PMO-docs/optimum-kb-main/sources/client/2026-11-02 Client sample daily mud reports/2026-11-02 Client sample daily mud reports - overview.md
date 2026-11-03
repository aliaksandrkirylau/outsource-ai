---
type: source
kind: client-material
date: 2026-11-02
original: https://mail.google.com/mail/u/0/#all/1a19b2173a2cea60
received_from: the client, Ms. Zahra Ahmed, attachments to her e-mail of 2026-11-02 07:20 UTC in the project thread "Optimum Engineering Standards × Innowise | Project"
purpose: what the client's daily report holds today, field by field, for the Discovery sessions on reports, mud checks, thresholds, inventory and hydraulics (we asked for the field reports before the kick-off, Anton's e-mail of 2026-10-28)
supersedes:
procedure_version: 5d00575
---
# 2026-11-02 Client sample daily mud reports - overview

kind: client-material. original: the Gmail message above, attachments "DMR Sample 1.pdf" (1281.3 KB, 4
pages) and "DMR Sample 2.pdf" (699.1 KB, 3 pages), stored next to this overview as received
(procedures/ingest.md step 2; added 2026-11-02):
[[2026-11-02 Client sample daily mud reports - DMR Sample 1.pdf]],
[[2026-11-02 Client sample daily mud reports - DMR Sample 2.pdf]]. A note links a page as
`[[2026-11-02 Client sample daily mud reports - DMR Sample 1.pdf#page=4|p4]]`; PDF page numbers, as in
the rendering. Rendering: [[2026-11-02 Client sample daily mud reports - rendering]].

Drive copy for the team (added 2026-11-02, the same files as stored here): `General >
02_Documentation > Requirements > Client sample reports`,
https://drive.google.com/drive/folders/19v1u3AwVR82NS7yu5Lqr51fqEfK-jG7o, as `2026-11-02_DMR Sample
1.pdf` and `2026-11-02_DMR Sample 2.pdf`.

Three sources came in on 2 November and were ingested together: this one,
[[2026-11-02 Client sample end-of-well recap - overview]] (the same e-mail) and
[[2026-11-02 Client sample engineering reports - overview]] (the e-mail of 08:26
UTC). The proposed changes for all three are in the table below.

## What it is

On 2026-10-28 Anton asked in the project thread: "If you can share the field reports and the formula
set before the call, we will go through them before the first session." Ms. Ayaa Khalid, 1 November:
"Ms. Zahra will share the requested field reports and formula set ahead of the meeting." Ms. Zahra
Ahmed, 2 November 07:20 UTC: "As requested, I've attached a few sample reports for your reference.
We'll share some additional reports shortly. As for the formula set, we'll work on compiling it and
share it with you at a later stage." The thread's messages after 14 October are not stored yet (its
rendering 2).

Two daily mud reports on two different forms:

- DMR Sample 1, "Daily Drilling Fluids Report - 44": the form of
  [[2025-10-29 Client sample daily report - rendering]] (same sections, same disclaimer), here filled
  in, for a horizontal well at 8850.00 ft MD. Drilling assembly, casing, volumes, pumps, circulation
  times; 36 mud properties for up to three samples, two taken (Active Pit and Flow Line, at 10:00 and
  23:00), against a "Fluid Spec" (density "73.00-90.00" lb/ft^3); annular velocities, bit information
  and hydraulics, solids analysis, rheology readings, "Hydraulic Analysis" (n, k, ECD at bit depth and
  at the casing shoe); solids control equipment, volume additions and losses, IADC hours; products and
  services with start, transferred in, received, returned, lost, daily use, final, unit price, daily
  cost and ending concentrations. A scan; PDF page 2 is blank.
- DMR Sample 2, "Daily Mud Report No. 11": a NaCl polymer mud at 8650 ft. Volumes, circulation and bit
  data, three samples (08:00, 15:00, 23:00) against "Spec's", products used, solids control, time
  distribution, solids analysis, "Rheology and Hydraulics" per annular section (annular and critical
  velocity, critical rate, flow regime, ECD, pressure drop, slip velocity, CTR, CCI), cost fields; a
  second page of pit volumes and volume tracking and an inventory of 66 products (initial, received,
  used, interval, cumulative, final, expire date, cost, concentration at start and end); a scanned
  "Rig Tanks Status" page (33 tanks: status, capacity, volume, fluid, weight).

Neither names a program or vendor. Mud weight and ECD are in lb/ft^3 in both. Operator, well, rig,
field and every name, phone and signature field are empty.

## How far to trust it

High for what the client's daily report holds today and what the client calls things. A sample, not
the required layout (sources/client/AGENTS.md); the client sent the 2025 form "for visual
appreciation" and expects the product to be better. Which of the two forms is the client's own today
is not stated.

The prices and costs are kept as printed: the rendering is flagged `money: client-domain` (Anton's
call, 2026-11-02; AGENTS.md rule 7), so the cost arithmetic can be checked against it. They are the
client's confidential commercial data: notes cite the rendering, never copy the figures, and no export
carries them.

## Not for

The required report format or field list; the formulas behind the computed values (none printed).

## Removed at ingest

Nothing. The money figures were first removed at ingest and then put back on Anton's call, before
anything was synced. No personal data in the originals. Transcribed from the page images by agents
working for Anton's session, the figures in a second pass.

Two well identifiers are printed in the other two sources (a page title of the end-of-well recap, a
case line of a hydraulics report), although the client blanked every other operator and well field
([[CON-006 Confidentiality of the client's customers' data]]). They were first removed, then restored
as printed on Anton's call, before anything was synced.

## Summary

The client's daily report today: one report a day with two or three mud samples against a spec range,
plus volumes, hydraulics per annular section, solids, equipment, time distribution, product use and
stock, and costs. The two forms differ in layout, not in what they hold.

## Proposed changes

For all three sources of 2 November. Source keys: D1, D2 = DMR Sample 1, 2
([[2026-11-02 Client sample daily mud reports - rendering]]); E = the end-of-well recap, with its page
([[2026-11-02 Client sample end-of-well recap - rendering]]); H-A, H-DF, H-R, H-R2, S, TD = Hydraulics
Analysis, Hydraulics Design Frame, Hydraulics Report, Hydraulics Report 2, Surge Report, Torque and
Drag ([[2026-11-02 Client sample engineering reports - rendering]]). No Decision is
proposed, so no deciders to name.

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | update | REQ-010 Reports | What the client's reports hold today. The daily mud report, on two forms (D1 "Daily Drilling Fluids Report", the 2025 form filled in; D2 "Daily Mud Report No. 11"): header, drilling assembly and casing, volumes, pumps and circulation, two or three mud samples against a spec range, solids analysis, rheology and hydraulics, solids control equipment, time distribution, products used, stock and costs; D2 adds pit volumes and a rig tanks status page. The end-of-well report (E "End Of Well Recap"): an executive summary by casing interval, the well's cost summary and total product and engineering consumption, then per hole section a "Section Fluids" sheet, costs, concentrations, property tracking against plan, and a time, volume and cost summary with charts. No end-of-section and no inventory report was sent. Evaluated: E is built from per-section sheet sets, each closing on a daily report number ("DMR 8", "DMR 14"), so the end-of-section report may be that set for one section; to confirm with the client. Samples, not the required layout | extracted, one line evaluated | clarifies WBS:Development Flutter!35-36 and 67-71 | D1 pp 1, 3, 4; D2 pp 1-3; E pp 2-4, 9-13 | applied 2026-11-02 |
| 2 | update | TRM-001 Report | The client's names: "Daily Mud Report" (D2), "Daily Drilling Fluids Report" (D1), "End Of Well Recap" (E); add aliases DMR and EOWR (the file names, and E's "DMR 8"). For version B: each sample is a column of the one daily report, three in D2 (08:00, 15:00, 23:00), two in D1 (10:00, 23:00), not four as on the first call. Stays disputed | extracted | - | D1 p1, D2 p1, E p1, p12 | applied 2026-11-02 |
| 3 | update | TRM-008 Mud check | The property set depends on the mud: the water-based sheets have MBT, Pm, Pf, Mf and API filtrate; the oil-based section adds HTHP filtrate at 300 °F, electrical stability, O/W ratio and the CaCl2 water phase; the completion brine adds TSS and turbidity. D1 lists 36 properties. A sample records where and when it was taken ("Sample From" Active Pit, Flow Line; "Check Time"; D2 "Time sample taken"). Fits "less than 50" | extracted | - | D1 p1, D2 p1, E pp 5, 19, 24, 29 | applied 2026-11-02 |
| 4 | update | REQ-005 Parameter thresholds and entry alerts, with a line in TRM-007 Threshold | Every sample puts a range next to each property: "Fluid Spec" (D1, density "73.00-90.00" lb/ft^3), "Spec's" (D2), "Mud Spec's" per hole section (E); E plots each property per section against "Plan Low" and "Plan High". Evaluated: the threshold the client means may be this per-section mud programme range, which would answer "global, per mud system or per well" with per well section; to confirm with the client | extracted, evaluated | clarifies WBS:Development Flutter!20, 52 | D1 p1, D2 p1, E pp 5, 12, 17 | applied 2026-11-02 |
| 5 | update | QUE-008 Which rheological model the hydraulics must use | More models in the samples: "Fluid Model: Yield-Power" (H-A), "Rheological Model: Robertson-Stiff" with a "Herschel-Bulkley" line of K, N, YP beside it (H-R), "Model: Power Law / Bingham" with parameters labelled "H-B K", "H-B n", "H-B YS" (H-R2); D1 gives n and k with no model named. Two options to add, Robertson-Stiff and Bingham. Still open, for the client | extracted | - | H-A, H-R p1, H-R2 p1, D1 p1 | applied 2026-11-02 |
| 6 | update | REQ-008 Fluid hydraulics simulation | What the sample programs compute: pressure losses by component and SPP, bit hydraulics, annular velocity and flow regime, ECD at the shoe and the bit with and without cuttings, cuttings transport and hole cleaning, flow-rate and ROP sensitivities, results at several depths, the operating window again, surge pressure against trip speed and the maximum trip speed by depth. Evaluated: four of the six are one commercial program's outputs for one planned well (PDF metadata: INTEQ "Advantage" templates, 2012), a reference for what engineers are used to, not the scope; row 60 estimates charts that "are not complex". The daily reports also carry hydraulics: per annular section (D2) and n, k, ECD (D1), the derived values of REQ-007 | extracted, evaluated | clarifies WBS:Development Flutter!60; the daily block row 58 | H-A, H-DF, H-R, H-R2, S; D1 p1, D2 p1 | applied 2026-11-02 |
| 7 | new | QUE-013 Which calculations from the sample reports the simulation must cover | asks: client. Blocks: the acceptance criteria and the estimate of WBS:Development Flutter!60 (Simulation: Fluid Hydraulics). Options: 1) fluid hydraulics as row 60 words it - pressure losses, bit hydraulics, ECD, hole cleaning, flow-rate what-ifs, the operating window; 2) plus surge and swab against trip speed (S; also the 2025 samples, images 6 and 9); 3) plus the sensitivities at several depths and ROPs (H-R2); 4) plus torque and drag - loads, torque, buckling, fatigue (TD), drill string mechanics rather than fluid hydraulics (evaluated), a change request candidate if wanted | evaluated | option 4 outside row 60's wording (evaluated) | H-DF, H-R, H-R2, S, TD | applied 2026-11-02 |
| 8 | update | REQ-018 Units of measure and conversion | Units in the samples: mud weight and ECD in lb/ft^3 in D1, D2, E and every hydraulics output, against ppg in the 2025 form; solids density in g/cc and lb/gal (D1); chlorides in mg/l (D1, D2) and g/l (E); H-A mixes metric and field (m, L/min, sg, m³ with psi, in, ft/s); product units in lb, kg, gal, L, bbl and m3 | extracted | - | D1 pp 1, 4; D2 pp 1-2; E pp 19, 24; H-A | applied 2026-11-02 |
| 9 | update | REQ-009 Inventory tracking | Stock as the client keeps it: D1 "Start, Transferred In, Received, Returned, Lost, Daily Use, Final" with ending concentration in the active and reserve system; D2 "Initial, Received, Used, Interval, Cumulative, Final, Expire Date" with concentration at start and end (ppb). Whole mud moves as stock too: "OBM Transferred In / Out (LMP/Other Well/Other Section)" with volumes, and volume in "From LMP / Other rigs" (E); no note has this yet. Costs in every sample, per day, section and well, plus an engineering service cost; E sets "Planned Units" and "Planned Cost" against actual, with "Not Planned Costs" and a cost analysis; the figures are in the renderings. The arithmetic holds as printed: unit price x units = line cost, lines sum to the section cost, sections to the well (E pp 4, 6, 10, 15, 20, 25, 30), daily costs to the daily product cost and final stock x price to the inventory value (D1 p4). The cost per bbl does not: its divisor changes between pages - volume used, volume in (p23), initial plus make-up volume (pp 3, 15) - and p3's "Fluids Cost / bbl of fluid" row holds the per-ft values. Evaluated: row 41 links consumption to a price list; planned against actual cost, the engineering cost and which volume a cost per bbl uses are not in its wording, for the BA | extracted, evaluated | clarifies WBS:Development Flutter!41 and 61-66; planned cost and engineering cost possibly outside (evaluated) | D1 p4, D2 p2, E pp 4, 6, 25, 28 | applied 2026-11-02 |
| 10 | update | TRM-006 Well section | E is split by hole section, each named by hole and casing size ("16” x 13 ⅜” casing", "8 3/8” OH (ith WBM) x 7” liner") with its own mud system, spec and costs, plus a "Completion" section in CaCl2 brine with no new hole. Supports the assumption (a hole section between casing points) and adds the completion as a section of its own; the [ASSUMPTION] stays until the client's expert confirms. D1 has "Section Name/No", D2 "Section" | extracted | - | E pp 2, 3, 29; D1 p1, D2 p1 | applied 2026-11-02 |
| 11 | update | REQ-011 Dashboards and KPIs | E already charts, per section: each property against depth with plan limits, volume in and out by source and by loss, mud cost per bbl and per ft, the cost breakdown by chemical category with and without weight material. Evaluated: close to the client's KPI "Top 5 product consumption and general products use pie chart for current well section & cumulative" (F.27); report charts, not a dashboard | extracted, evaluated | - | E pp 8, 12, 13, 17, 18 | applied 2026-11-02 |
| 12 | update | CON-006 Confidentiality of the client's customers' data | The client anonymised its samples before sending: operator, well, rig, field and every person blank, the property tracking headers blacked out (E); two well identifiers are left in (E p16, H-R p2), kept as printed on Anton's call. Evaluated: the client strips its customers' identity before data leaves the company; the samples stay inside the team | extracted, evaluated | - | D1, D2, E pp 12, 17, 22, 27 | applied 2026-11-02 |
| 13 | update | CON-003 Correct calculations | The formula set is not in yet: "As for the formula set, we'll work on compiling it and share it with you at a later stage" (Ms. Zahra, 2026-11-02 07:20 UTC), after Ms. Ayaa had said it would come before the kick-off. No sample prints a formula; one standard is named, "Interval Dilution factor 0.07 API 13-C, 5.4.9" (E p28) | extracted | - | this overview, What it is; E p28 | applied 2026-11-02 |
| 14 | update | K-10 Fixed price with vague acceptance criteria | A further cause (evaluated): the client's hydraulics references are a commercial program's outputs, with multi-depth sensitivities, cuttings transport and torque and drag; read as the target, they would set acceptance against a commercial package. Treated through QUE-013 | evaluated | - | H-DF, H-R, H-R2, S, TD | applied 2026-11-02 |
