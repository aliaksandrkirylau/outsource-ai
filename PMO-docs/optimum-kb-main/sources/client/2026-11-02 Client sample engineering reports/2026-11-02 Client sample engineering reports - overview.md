---
type: source
kind: client-material
date: 2026-11-02
original: https://mail.google.com/mail/u/0/#all/1a19b5e2dc6a7a8a
received_from: the client, Ms. Zahra Ahmed, attachments to her e-mail of 2026-11-02 08:26 UTC in the project thread "Optimum Engineering Standards × Innowise | Project"
purpose: what hydraulics and drilling calculations the client's engineers use and read today, for the Discovery sessions on the simulation and the calculations
supersedes:
procedure_version: 5d00575
---
# 2026-11-02 Client sample engineering reports - overview

kind: client-material. original: the Gmail message above, six attachments: "Hydraulics Analysis
Sample.pdf" (11.5 KB, 1 page), "Hydraulics Design Frame Sample.pdf" (66.8 KB, 1), "Hydraulics Report
Sample.pdf" (94.5 KB, 2), "Hydraulics Report Sample 2.pdf" (834.6 KB, 5), "Surge Report Sample.pdf"
(72.0 KB, 2), "Torque and Drag Sample.pdf" (75.4 KB, 1). Rendering:
[[2026-11-02 Client sample engineering reports - rendering]].

Stored next to this overview (procedures/ingest.md step 2; added 2026-11-02):

- [[2026-11-02 Client sample engineering reports - Hydraulics Analysis Sample.pdf]]
- [[2026-11-02 Client sample engineering reports - Hydraulics Design Frame Sample.pdf]]
- [[2026-11-02 Client sample engineering reports - Hydraulics Report Sample.pdf]]
- [[2026-11-02 Client sample engineering reports - Hydraulics Report Sample 2.pdf]], as received
- [[2026-11-02 Client sample engineering reports - Surge Report Sample.pdf]]
- [[2026-11-02 Client sample engineering reports - Torque and Drag Sample.pdf]]

Five of them were rebuilt page for page without their document metadata, which held the author's
account IDs (see Removed at ingest); every page renders the same as the file received, and the text
layer is unchanged.

Drive copy for the team (added 2026-11-02, the same six files as stored here, the five rebuilt ones
included): `General > 02_Documentation > Requirements > Client sample reports`,
https://drive.google.com/drive/folders/19v1u3AwVR82NS7yu5Lqr51fqEfK-jG7o, each as
`2026-11-02_<name>.pdf`.

The second e-mail of the two of 2 November: "As promised, please find attached the remaining sample
reports for your reference." The request and the first e-mail are in
[[2026-11-02 Client sample daily mud reports - overview]], with the proposed changes for all three
sources. Source keys there: H-A, H-DF, H-R, H-R2, S, TD, in the order above.

## What it is

Six outputs of engineering programs, none naming its program on the page:

- H-A "Drilling Hydraulics Analysis": one bit run at 4535.00 m, 2.35 sg mud, "Fluid Model:
  Yield-Power"; bit hydraulics, system pressure losses, drill string, annular summary. Metric and field
  units mixed (m, L/min, sg, m³ with psi, in, ft/s). PDF made 2011, titled "8.5 Original YPL".
- H-DF "DesignFrame Including Cuttings Transport": well schematic with inclination, the "Hydraulics
  Operating Window" (pressure and ECD against flow rate, with "Max SPP" and "Required Flowrate"), ECD
  and ESD at the shoe and bottom, pore and frac pressure, pressure losses.
- H-R "Hydraulics Spreadsheet Report Including Cuttings Transport", 2 pages: inputs, drill string,
  bit hydraulics and system pressure loss with cuttings at flow rates from 380 to 200 USgal/min,
  annular velocities and flow regime, circulation times. "Rheological Model: Robertson-Stiff", with a
  "Herschel-Bulkley" line of K, N and YP next to it.
- H-R2 "HYDRAULICS - SUMMARY", "SENSITIVITY" and "MULTIPLE DEPTH", 5 pages: an 8.5" BHA run from
  12800.0 to 16673.0 ft in oil-based mud; pressure drops, ECD and bit figures against flow rate and
  ROP and at several depths, cuttings and hole cleaning, five charts (SPPA, ECD against depth and flow
  rate). "Model: Power Law / Bingham" with "H-B K", "H-B n", "H-B YS".
- S "Surge Report", 2 pages: running a 7" liner in 8 1/2" hole to 18410 ft, closed end; surge pressure
  and equivalent mud weight against trip speed (5 to 600 s/std), maximum trip speed against depth.
- TD "T&D Calculation - Summary Report": loads along the string against MD for drilling, slack-off,
  pick-up and rotating off bottom, torque, drag, stretch, stresses and safety factors; it prints
  "Buckling occurs and the danger of Fatigue exist".

H-DF, H-R and TD are one planned well and case ("6 1/8" / 20872 Ft / Plan", same inputs and results);
S is most likely the same well one section earlier (its liner matches H-R's, its shoe depth does not).
Their PDF metadata, as received, names report templates of INTEQ's "Advantage" (BHIHYD_OnePageGraphic.htm,
BHIHYD_SpreadsheetReport.htm, SwabSurge.htm, TdBHISummaryChart.htm), made on 2012-04-02, and all four
carry the same disclaimer. H-A and H-R2 are other jobs. Field units except H-A; density in
lb/ft^3 throughout.

## How far to trust it

High as examples of what the client's engineers use and read. They are third-party program outputs
of 2011 and 2012, not the client's statement of what our simulation must do (sources/client/AGENTS.md):
the v1 WBS estimates the simulation with charts that "are not complex"
([[2026-09-25 v1 WBS - rendering]] Development Flutter row 60).

## Not for

The scope of the simulation; the formulas (none printed); reference values.

## Removed at ingest

From the stored PDFs (2026-11-02): the document metadata of H-A, H-DF, H-R, S and TD, whose author
fields held account IDs; the files were rebuilt from their pages, so the titles and dates went with
it (what they said is recorded above). The well identifier in H-R's case line was first removed, then
put back as printed on Anton's call, before anything was synced. No money and no personal data on the
pages; the rendering never carried the metadata. Transcribed from the page images by an agent working for Anton's session
and screened with kb-money (clean).

## Summary

What a commercial hydraulics package prints for one bit run: pressure losses, bit hydraulics, ECD with
and without cuttings, hole cleaning, flow-rate and ROP sensitivities, the operating window, plus surge
against trip speed and torque and drag. Three of the six name a rheological model, each a different one.

## Proposed changes

In the table of [[2026-11-02 Client sample daily mud reports - overview]].
