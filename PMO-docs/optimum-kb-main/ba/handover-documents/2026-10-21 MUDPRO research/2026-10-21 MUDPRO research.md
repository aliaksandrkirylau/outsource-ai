# 2026-10-21 MUDPRO research

Anton's research note for the BA, the TL and Mikhail. Written by Anton's agent
(claude-code/claude-opus-5-5) on 21 October from public vendor material and a conference paper. It is
working material, not evidence (`ba/AGENTS.md`; moved from `pm/` on 29 October). Nothing here is ingested, and no typed note changes.
The client has not confirmed which tool it means: that part is our conclusion (evaluated), not a fact.
Updated on 22 October with whether the tool was named before ("Was it named before 20 October").

## Why we looked

On the introductory call of 20 October, Mr. Lawal named the off-the-shelf tool OES used before (Bluedot
recording 6ad73c7c657f708925b041c5, not ingested, 43:42 to 44:36):

> Before now, we've used a solution from one of the industry leaders. You know, providing third-party
> solutions, which is Mod4. [...] However, whatever we're going to do should be able to better any of
> those. I don't want, I don't want a copy of what someone has done 20, 15, 10 years ago.

Straight after, at 45:35, came the compliance point (ISO 9001, ISO 14001, API), left out of the
follow-up for the 21 October internal meeting ([[2026-10-20 Introductory call follow-up]]).

A year earlier, on 22 October 2025, Zahra Ahmed said the third-party software they adopted "can only do
so much" and is "not sustainable also from a cost standpoint"
([[2025-10-22 First call with OES - transcript]], 0:19:02).

## Which tool it most likely is

- "Mod4" is most likely MUDPRO version 4. The LINQX downloads page lists the current installer as
  "MUDPRO" with the version "4", and "Mod4" reads like a transcription of "MudPro 4". Not confirmed: ask
  Mr. Lawal.
- MUDPRO was developed by Pegasus Vertex, Inc. with Anchor Drilling Fluids and released in 2009. The 2012
  AADE paper says it was used "by more than 20 companies in the past 2 years".
- LINQX (Houston) sells it today, with Pegasus Vertex material hosted on its site. I found no source that
  says how the product passed from one to the other.
- The family:
  - **MUDPRO**: the Windows desktop program for the mud engineer.
  - **MUDPRO+**: the current version, called MUDPRO again in the 2026 brochure. It adds pad drilling,
    more rheology models, "AI data analysis" and dashboards.
  - **MudManager**: a web database for supervisors that MUDPRO users upload reports to.
  - **HYDPRO**: hydraulics software that MUDPRO exports to.

## Was it named before 20 October

Checked on 22 October. I searched the KB (`sources/`, `knowledge/`, `pm/`) and the Optimum folder of the
copilot workspace (`projects/optimum-engineering`, the presale harvest included) for MUDPRO, Mod4,
Pegasus Vertex, LINQX, MudManager and HYDPRO. None of them appears before the 20 October call. Presale
knew OES had off-the-shelf tools, but never which one:

- **First call, 22 October 2025.** Zahra Ahmed: "We've adopted some third party software solutions"
  ([[2025-10-22 First call with OES - transcript]], 0:19:02). No name was given. Marina Zaretskaya's
  notes say the client "tried to use Excel and adapt ready solutions"
  ([[2025-10-22 First call with OES - notes]]). Nobody asked which software.
- **Solution proposal and slides, November 2025.** Both speak only of "current tools"
  ([[2025-11-03 Solution proposal - rendering]], [[2025-11-05 Proposal slides - rendering]]).
- **The client's sample daily report, 29 October 2025**, "Daily.xlsx"
  ([[2025-10-29 Client sample daily report - rendering]]). This is the only possible trace. The A01
  handover analysis in the copilot workspace (`projects/optimum-engineering/harvest/07-presale-requirements.md`)
  says its layout "reads like an export from an off-the-shelf mud-reporting package", marked as an
  inference. I compared it with the 2012 MUDPRO sample (image 02), and it does not match:
  - **Different disclaimers.** The client's begins "Any opinion and/or recommendation, expressed orally
    or written herein, has been prepared carefully" (rows 64 and 121). MUDPRO's begins "The information
    in this report is based on our experience".
  - **Fields the MUDPRO sample lacks:** primary and secondary currency, debit/credit, deck load, riser
    booster rate and IADC hours, plus a separate volume report by pit (frac tanks, trip tank, cement
    tanks) and a products price list sheet.
  - **What both share** is what any mud report has: four sample columns, rheometer readings from 600 to
    3 RPM, bit hydraulics, solids control equipment and a product table.

  So the template is not a 2012 MUDPRO report. It may come from another package, or from MUDPRO 4 if
  that version looks different, or the client may have built it. A web search for the client's
  disclaimer wording found no source.

## How it is deployed

- **Desktop.** Windows 10 or later, Microsoft Office 2016 or later, 8 GB RAM, 600 MB free disk, a 1,280 x
  768 display.
- **One file per pad.** In the vendor's FAQ, "each pad (including well information) is saved as a case
  file". Backups go to a
  local "Backup" folder, and the vendor's fix for a crashed database is to copy an older case file.
- **No server, no sync.** The AADE paper calls it "point to point": the engineer e-mails the well file,
  and the receiver opens it, reviews it or prints the same report. Without internet the data stays on
  the laptop and is sent later.
- **MudManager** (web): any modern browser, on desktop, tablet or phone. It runs on Windows Server 2019
  or later, IIS 10 and SQL Server 2016 Express or later, on one server or two. It holds:
  - a company-wide master product database with price schedules, pushed to MUDPRO users
  - user levels for role-based access, and data by district or region
  - daily mud report upload and download
  - comparison of up to 10 wells
- **Licensing.** Lease or subscription. The installer comes from a portal and needs an activation
  passcode. There is no public trial, manual or video.

Our conclusion: the shape is the one OES asked us for, an offline desktop app on the rig and a central
web app for managers ([[CAP-002 Offline data and sync between rigs and HQ]]). The difference is that
MUDPRO moves data as files sent by hand, not by automatic sync.

## How the engineer works with it

From the AADE paper and the Pegasus Vertex guide to the daily mud report:

1. Create a report. The report number goes up by itself, and a report time tells apart several reports
   on one day.
2. Copy the previous day's report with one button and change only what moved.
3. Enter up to 4 mud samples, one column each, from different places or times.
4. Enter inventory: products, services and engineering, received, used and returned, with BOL tracking.
5. Fill in the wellbore, drill string, bit, up to 4 pumps, pits and solids control equipment.
6. Balance the volumes. "The volume should balance before the engineer can move forward and create the
   next report."
7. Print or send the report.

Along the way:

- An input warning system flags wrong entries and missing required fields, and there is a low inventory
  warning.
- Past reports can be edited. A changed price can be applied to a date range, and the cost of every day
  in it is recalculated.
- When a well ends, its data carries over to the next one, and its ending inventory becomes the next
  well's starting inventory. A finished well can also be used as a template.

## What the daily mud report holds

The guide splits a report into ten sections:

1. Header: well, operator, contractor, report number, date and time, MD, TVD, inclination, azimuth.
2. Wellbore and drill strings: cased hole, open hole, BHA, bit (TFA), pumps.
3. Drilling, volume and circulation: WOB, rotating, slack-off and pick-up weights, RPM, ROP, circulation
   times and strokes.
4. Solids control equipment: running hours, screens.
5. Mud properties, up to 4 samples. The list differs for water-based and oil- or synthetic-based mud:
   MW, funnel viscosity, PV, YP, gels (10 sec, 10 min, 30 min), API and HTHP filtrate and cake,
   solids, oil, water, sand, MBT, pH, Pm, Pf, Mf, calcium, hardness, chlorides, excess lime, K+, LCM,
   oil/water ratio, WPS, CaCl2, brine density, electrical stability, water activity.
6. Inventory: each product, service and engineering line, with daily, previous and cumulative totals.
7. Recommended tour treatments and remarks: free text.
8. Volume tracking: additions, losses, from and to storage.
9. Hydraulics: annular (velocities, critical velocity and rate, ECD, slip velocity) and bit (jet impact
   force, bit hydraulic horsepower).
10. Solids analysis and time distribution.

Two formulas as the guide prints them: "Excess lime (lb/bbl) = 0.26 [Pm - (Fw x Pf)]" and
"HHP=Delta P*Q/1714".

Report options:

- The vendor says the report "meets the standards of API mud report format".
- One, two or three pages, printed on Letter, Legal or A4.
- Product prices and costs can be hidden, leaving only the daily total.
- Units: US oilfield, metric or custom.
- WITSML export for fluids, ops, rig, well and wellbore reports, and an export to HYDPRO.

Rheology models: Bingham Plastic, Power Law and Herschel-Bulkley. Salts: NaCl, CaCl2 and dual salts.

## Recap and analysis

- **End-of-well recap.** Generated with one click. By hand it takes "about 5 hours or even more" for a
  60-day well (AADE).
- **Planned against actual**, for example MD against drilling days.
- **Summaries by interval**: conductor, surface casing, intermediate casing.
- **Cost distribution** by product and by category.
- **Comparison of up to 10 wells** on drilling speed, daily cost, mud properties, cost per foot and cost
  per day.
- **Daily report views in MUDPRO+** (image 03): Summary, Detail, Daily Cost, Total Cost, Concentration,
  Time Distr., Survey, Alert.
- **Recap views in MUDPRO+** (image 04): Summary, Cost Distr., Daily Cost, Depth Cost, Cum. Cost,
  Drilling Data, Mud Prop., Hydraulics, Solids, Vol., Usage, Conc., Time Distr., SCE, Bit, Remarks,
  Interval, Survey, 3D Well, Customized, Engineer, Safety.
- **"AI-driven insights"** are claimed. Nothing I found says what they do.

## How it looks

The four images are for internal reference only. Their copyright is the vendor's, so they never go into
an export (`procedures/ingest.md`, step 2). Anton's agent checked each image before storing it. Money
figures, e-mail addresses and phone numbers are greyed out. Names are the vendor's sample data. All
four are under 1 MB.

Image 01: the 2012 MUDPRO input screen (AADE paper, Fig. 3). Classic Windows forms. On the left is a
tree of the well's reports by date and time. On the right are tabs (Well, Mud, Inventory, Pump), and
each tab is a dense form with grids for cased hole, open hole, drill string, bit and nozzles.

![[2026-10-21 MUDPRO research - image 01.png]]

Image 02: a 2012 printed daily mud report, oil-based mud (AADE paper, Fig. 4). One dense sheet in the
ten sections above.

![[2026-10-21 MUDPRO research - image 02.png]]

Image 03: the MUDPRO+ daily report summary, dated 5/7/2022 in the title bar (LINQX brochure, page 1).
It has an Office-style ribbon (Home, Report, Utilities, Help) and a menu of views on the left. The
page holds a wellbore schematic, gauge KPIs (depth, cost against plan, days) and the top 10 products by
share. The progress charts show depth, cumulative cost and mud weight.

![[2026-10-21 MUDPRO research - image 03.png]]

Image 04: the MUDPRO+ recap, product usage by day, with received, used and final quantities per product
(LINQX brochure, page 2).

![[2026-10-21 MUDPRO research - image 04.png]]

## What it means for us

Our conclusions (evaluated):

- **A benchmark, not a model.** Mr. Lawal asked for something that betters these tools, "not a copy".
  MUDPRO is a fair picture of what an engineer at OES already expects as a minimum. Take it to the
  Discovery workshops and the prototype as a checklist, not as a design.
- **Against our Capabilities:**
  - The daily cycle and the checks fit [[CAP-004 Shift measurements and quality control]].
  - Calculations and hydraulics fit [[CAP-005 Mud engineering calculations and simulation]].
  - Inventory, BOL and carry-over fit [[CAP-006 Inventory]].
  - Units fit [[CAP-007 Units of measure]].
  - The report, recap and comparison fit [[CAP-008 Reports and report approval]].
  - The dashboards fit [[CAP-009 Dashboards and KPIs]].
- **Possibly beyond the WBS.** Whether these are in it is for the TL to check, not settled here:
  - price changes recalculated over past days
  - well comparison
  - interval summaries
  - WITSML export
  - solids analysis
  - bit hydraulics
- **What the vendor material doesn't show:** approval of a report, locking it once sent, or an audit
  trail. These are the record controls ISO 9001 leans on ([[CAP-010 Audit trail and change
  approval]]). Their absence from marketing material proves nothing either way.

## To ask OES

Not Question notes: these are for the Discovery sessions, and none of them blocks a WBS line.

- Which product and version: MUDPRO 4, MUDPRO+, MudManager as well? Is it still in use? "Before now"
  may mean they stopped.
- A daily mud report and an end-of-well recap exported from it, next to their own Excel daily report.
- Where the "Daily.xlsx" template comes from: their own, or an export from a package, and which one.
- What fell short, in their words: features, cost, or the way data moves between rig and office.
- Whether past wells sit in MUDPRO files that would have to come over
  ([[REQ-015 Import of historical data]]).
- Whether an engineer could show it on a screen share in one of the sessions.

## Sources

All read on 21 October 2026.

- [LINQX, MUDPRO page](https://linqx.io/solutions/mudpro/): features, FAQ, system requirements.
- [LINQX, MUDPRO brochure](https://linqx.io/brochure/MUDPRO-Drilling_Mud_Reporting_Model.pdf), 2026, 2
  pages: key features, images 03 and 04.
- [LINQX, MudManager page](https://linqx.io/solutions/mudmanager/): the web database and its server
  requirements.
- [LINQX, downloads](https://linqx.io/downloads/): MUDPRO, version 4, licence passcode.
- [Y. Yao and C. Light, "Streamline Mud Reporting and Management", AADE-12-FTCE-28, 2012](https://www.aade.org/application/files/1815/7260/6789/AADE-12-FTCE-28_-_Yao.pdf):
  history, workflow, data transfer, recap, images 01 and 02.
- [Pegasus Vertex, "How to Read a Daily Mud Report"](https://linqx.io/wp-content/uploads/2025/09/How_to_Read_a_Daily_Mud_Report.pdf),
  13 pages: the ten report sections, terms and formulas.
- [Pegasus Vertex, "Mud Reporting: Streamlined Process and Data Management", white paper on SlideShare](https://www.slideshare.net/slideshow/mud-reporting-streamlined-process-and-data-management/32401680):
  the same content as the AADE paper.
- Searches for user reviews, forum posts and demo videos found none. A search on 22 October for the
  disclaimer wording of the client's "Daily.xlsx" found no source either.
