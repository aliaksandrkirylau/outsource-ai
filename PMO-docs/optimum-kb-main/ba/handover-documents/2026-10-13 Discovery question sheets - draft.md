# 2026-10-13 Discovery question sheets - draft

The BA's preparation for discovery, split out of [[2026-10-13 Discovery plan - draft]] on 13 October.
Working material, not evidence (`ba/AGENTS.md`); moved from `pm/` to `ba/` on 29 October, for the BA. The plan, the
schedule and the seven session topics are in the plan; this file is what the BA works from inside
each topic. Updated on 23 October with questions from [[2026-10-21 MUDPRO research]],
[[2026-10-22 API standards research]] and [[2026-10-22 Prototypes against MUDPRO and API]] (D2, D3,
D5, X, and a limit on formulas). Updated on 2 November: sessions are one hour, one topic each
([[00 discovery-BA-plan]]); the UI kit is chosen in the vision session, S00
([[DEC-017 Choose the UI kit with the client from three variants]]); a few questions from the
20 October call ([[CON-008 Compliance with ISO 9001, ISO 14001 and API standards]]). From
2 November the working questions live in the session plans S00 to S08 in `ba/workshops/`;
each marks the sheet section it came from. This file stays as the handover record.

## Rules for the BA

- Hybrid: we arrive with our own picture of each area from the WBS and the SOW, and ask as if we knew
  nothing.
- Minimal: each prototype is the smallest version that meets its WBS line. Anything bigger is logged as
  a delta with hours, not drawn.
- Out of scope and change-request candidates are never drawn as working screens: mobile, the onboarding
  wizard, the API, historical import, documents from HQ, lab equipment, the engineering-calculation
  report. What a prototype shows, the client can argue is in scope (contract 4.4,
  [[COM-005 Change requests]]).
- Fictional data only, no real customer names ([[CON-006 Confidentiality of the client's customers' data]]).
- A demo or a nod is not acceptance. Each area closes with a written OK by email from the named client
  contact.
- Development on an area starts once its prototype has the written OK. Areas are accepted one by one;
  nobody waits for all of them.
- Prototypes in Claude (HTML artifacts). No Figma.

## The 12 areas

From the section names of the WBS tab "Development Flutter", MVP lines only. Left out: Base project
setup, both Other sections, General activities, Mobile (all FALSE, [[REQ-013 Mobile app]]) and the
optional lines (location, templates, onboarding wizard). Login/Logout alone is too thin to prototype,
so D1 and W1 are each app's frame: sign-in plus navigation by role, which is where the role model
(row 12) belongs.

| # | Area | WBS Development Flutter rows | SOW builds it in | Session topic | Needs first |
|---|---|---|---|---|---|
| D1 | Desktop sign-in and app frame | 47, 12 | M2 | 1 | rig PC specs |
| W1 | Web sign-in and app frame | 17, 12 | M2 | 1 | the role list |
| D2 | Desktop job and measurements | 50-54 | M3 (alerts M4) | 2 | parameter list, units (X4) |
| W2 | Web admin panel | 19 users, 20 thresholds, 21 audit and edit approval, 22 units | M2 to M4, audit M6 | 2 (20, 22), 3 (19, 21) | thresholds go with D2 |
| W3 | Web job management and QC | 26-29 | M3 | 2 |  |
| D4 | Desktop inventory | 62-66 | M4 | 4 | the product catalogue |
| W4 | Web inventory | 39-41 | M4 | 4 |  |
| D3 | Desktop calculations and modelling | 58-60 | M5 | 5 | the formulas, asked for in week 1 |
| D5 | Desktop reports | 68-71 | M6 | 6 | D2, D4 |
| W5 | Web reports and approval | 33-37 | M6 | 6 | D5 |
| D6 | Desktop dashboard | 56 | M6 | 7 | KPI definitions |
| W6 | Web dashboard | 31 | M5 | 7 | KPI definitions |

Not prototypes, but discovery has to settle them, in one tech session with the client's IT, Arseniy
and the architect: X1 offline work and sync, X2 the rig PCs and how updates reach them, X3 hosting and
Saudi cybersecurity. X4 units feeds D2 and D3; X5 import, documents from HQ and the API decides CR or
out; X6 users and roles feeds everything. The gaps between the SOW and the WBS are in Mikhail's
[[2026-10-01 SOW v10.4 to v1 WBS scope mapping]]; what they change here is in the next section. The
mapping reads the SOW as stored in June; the SOW was reworked to the Agreement in late September, so the
mapping is re-run once the SOW as sent is stored.

Which areas share a session: topic 1 is D1 and W1; topic 2 is D2, W3 and W2's thresholds and units;
topic 3 is the rest of W2; topic 4 is D4 and W4; topic 5 is D3; topic 6 is D5 and W5; topic 7 is D6
and W6. X1 to X3 are the technical session. Before topic 1, the vision session (S00). Each session is
one hour: heavy topics (2 and 5) cover their must-have questions in the hour, the rest in writing.

## What the scope mapping changes

The mapping finds SOW promises with no WBS line behind them, or only part of one. Discovery is where
each gets either an estimate in the revised WBS or a limit in writing:

- Sync has no WBS line at all (mapping 1a #1), the largest unestimated item. Its design and its
  estimate are a discovery output, from the tech session and the architect, and go into the revised
  WBS.
- Rig updates and the final handover to the client's servers are not estimated (1a #5), and the
  DevOps tab is written for a cloud. Settled in the tech session (X2, X3), estimated in the revised WBS.
- Where the SOW asks for more than an area's WBS line, the per-area numbers should expect a delta and
  not book it as the client's ask:
  - D1: offline sign-in and token storage; no UI/UX hours for the desktop frame (1a #2, 1b #8).
  - D2: no line for the desktop job list and details view (1b #9).
  - W1: applying the role model screen by screen is not estimated (1b #10).
  - W2: the users list with filter and search is only implied by the CRUD line (1b #7).
  - W4: no line for "basic validation rules" or for viewing consumption entries at HQ, both promised
    (1a #3, #6). Both go into the W4 prototype.
  - D4 and W4: nothing lets anyone enter low-stock levels or expiry dates, and the SOW contradicts
    itself on where (1a #4).
- Who provisions the environments is open, and monitoring, load balancing, backup and post-release
  support are in the WBS but not in the SOW (mapping 2a). For the tech session.
- "Project documentation as agreed" (WBS row 93, SOW M6) is not defined; agree in discovery what our
  technical documentation consists of.

## Limits to put in writing

Some limits exist only in the WBS, so the SOW cannot hold them against a change request
([[COM-005 Change requests]], [[K-5 Scope grows through the prototypes]]). The V&S document and each
area's acceptance criteria carry them: up to 50 parameters per mud check (row 28); up to 30 logged
actions in the audit trail (row 21 - the SOW says "the agreed volume" with no number); three unit sets
(rows 22, 54); simple charts only (Assumptions 11, 13); English only (Assumption 19). From the SOW: a
single desktop resolution and no dark mode (M2 mockups).

Formulas: the SOW makes deriving and validating the engineering formulas the customer's, and has them
provide the compliance requirements before the start ([[2026-06-15 SOW v10.4 - rendering]] lines 339
and 451). On 20 October Mr. Lawal still expected "a level of double-checking from your side", and said
the tool must align with API ([[2026-10-22 API standards research]]). Mikhail and Aliaksandr Kavalchuk
settle internally how far we check, before the D3 session.

## Context for every session

"Blocks" means the prototype cannot be drawn honestly without the answer; v0 is what we draw before
it. Built from the client's own material - the Q&A answers of 29 October 2025, the first call of 22
October 2025, the sample daily report, the formula samples - and the KB notes named. Not from the
generic banks in `reference/`.

The client's top three, in their words (Q&A A.1): "Must generate complete and accurate reports.";
"99.9% data integrity and efficient synchrony between job sites and HQ server."; "User friendly
interface with low latency and minimal bugs." Their pain (first call): Excel calculators that "each
engineer will have its own set of", "not standardized", data "difficult to centralize and mine".

Client people known (contract chat, 29 Sep): Ishaq Lawal, General Manager (introduced himself on the
first call; decisions "largely be made by myself. Of course, with the ultimate approval of my CEO");
Dr. Jaber, CEO, the contract's signatory; Dr. Yahya Alsayel, lawyer; Ayaa Khalid, assistant, through
whom everything is coordinated. Zahra Ahmed wrote the first inquiry; role unknown.

Contradictions to keep in mind (detail in the notes): three or four roles
([[REQ-004 Roles and what each role can do]], disputed); what a "report" is ([[TRM-001 Report]],
disputed); hosting on-premises or cloud ([[DEC-012 Host the central system on Google Cloud in the Kingdom]]);
the client wants a mobile app, the onboarding wizard and an API, all out of scope.

## Sheets per area

### D1 Desktop sign-in and app frame (rows 47, 12)

v0: personal accounts created on the web; offline sign-in for anyone who has signed in on that PC
before; left navigation with the SOW desktop modules; a header with rig, well job, current 12-hour shift,
engineer and "last synced"; English; 1440x1024 until the rig PC specs are known.

Blocks:
1. Personal account per engineer, or one login per rig PC? They "prefer" personal, find device login
   "acceptable" (Q&A D.11; [[REQ-003 Sign in on a shared rig computer]]).
2. Can an engineer who never signed in on this PC sign in offline? How do new crew accounts reach a rig
   with no connection?
3. At shift change, does the next engineer carry on the same day's checks and report, or open his own
   shift? Does signing out close the shift? ([[TRM-002 Shift]])
4. The rig PC screens and resolution.

Later: may an engineer edit a colleague's entries; auto-lock on a shared PC; who resets a password at
an offline rig; should the engineer see sync state.

Ask for: the rig PC standard (OS, screen, domain, shared Windows account), a crew rotation for one rig,
the IT password policy.

### W1 Web sign-in and app frame (rows 17, 12)

v0: email and password; four roles as in the client's own Q&A D.13 (Engineer desktop only; Supervisor,
Manager, Admin on the web) to test the REQ-004 dispute in the demo; navigation per the SOW web modules,
filtered by role; a rig or job selector.

Blocks:
1. The role list. Are Supervisor and Manager one role or two (the SOW says both)? Where do "Project
   Engineers, Operations Support, and Operations Manager" (Q&A C.10) fit?
2. Which roles see all rigs, and which only "their assigned rigs" (row 29)?

Later: number of HQ users per role; MFA for admins (NCNICC-1 asks for it, the SOW excludes it;
[[CON-007 Saudi cybersecurity and data protection rules]]); customer access confirmed out.

Ask for: the HQ org chart with roles and headcounts, the supervisor-to-rig mapping.

### D2 Desktop job and measurements (rows 50-54)

v0: HQ creates the job and assigns engineers, the desktop shows assigned jobs, the engineer can also
create one; the job header = the daily report header fields; the mud-check form = the daily report's
property list plus the 600-3 RPM readings, four checks a day, two per shift; since 23 October,
plastic viscosity, yield point, retort solids and excess lime calculated, and n, K and the solids
analysis by the client's power-law procedures and equations shown when a check is saved; out-of-range values
highlighted, a reason required, saved "flagged"; impossible values blocked; oilfield units with a
toggle.

Blocks:
1. When a rig moves to a new well, who opens the job, HQ or the engineer? Which header fields come from
   HQ and which are typed at the rig? ([[REQ-020 Create and manage well jobs and assign engineers]])
2. The exact mud-check parameter list with units and which are mandatory. Does it differ by mud type or
   system (water-based, oil-based)?
   - The daily report follows the API water-based tests. For oil-based mud, which of the RP 13B-2
     tests are run on the rig: electrical stability, oil/water ratio, whole-mud alkalinity, chloride
     and calcium, CaCl2 or water-phase salinity, HTHP filtrate, activity?
     ([[2026-10-22 API standards research]])
   - The daily report also lists 60 and 30 RPM readings (rows 36, 37), which neither prototype has, and
     three "User Defined Properties" (weight, funnel viscosity, filtrate, row 46). Are these fixed
     fields, or a list each job can extend?
3. Besides mud checks, does the engineer enter volumes and pits, pumps, bit and BHA, solids control,
   comments and treatments? The daily report has them; row 51 says only "measured fluid parameters".
4. When does the reporting day start and end, and which day does a check belong to?
5. The two alert types (Q&A E.20): does type 1 block the entry, and type 2 only flag? Asked, never
   answered.
6. What is a "threshold" for them (they asked us, Q&A E.19), and is a range per well or customer spec,
   per mud system, or global? ([[REQ-005 Parameter thresholds and entry alerts]], [[TRM-007 Threshold]])
7. Can an engineer change his own check before the shift closes without approval? When does approval
   start? ([[REQ-006 Edit or backfill past entries with approval]])
8. Do engineers type plastic viscosity, yield point, excess lime and retort solids today, or does a sheet
   calculate them? API RP 13B-1 derives all four from other readings, and the client said yes to derived
   values on save (Q&A E.21, [[REQ-007 Derived values and standard calculations]]). Both prototypes
   have the engineer type some of them.

Later: how a well section starts and ends ([[TRM-006 Well section]]); who closes a job; a job changed
offline at the rig and at HQ at once; should a supervisor be told about a flag; did engineers copy the
previous day's report in the tool used before (MUDPRO does it with one button,
[[2026-10-21 MUDPRO research]]), and should copied values count as measured.

Ask for: the parameter list per mud system with units and typical ranges, a customer spec or mud
program for one well, 2-3 filled daily reports (anonymised, to Drive), the Job# format, the list of mud
types and systems, current thresholds.

### W2 Web admin panel (rows 19-22)

v0: users list and form (name, username, role, assigned rigs, active); threshold table (parameter, unit,
min, max; global with an override per job); approval queue (old and new value, the engineer's reason,
approve or reject); audit table (when, who, what, old and new, status); units as a system default plus a
user preference.

Blocks:
1. Who approves edits and backfills ("operations manager and/or system admin", Q&A E.22)? Does the
   change wait for approval? What does the rig see while a request is pending offline?
2. A threshold's scope and who sets it - IT staff or supervisors (Q&A D.16)?
3. Where rig names and numbers come from, since location management is out. If people are assigned to
   rigs, a plain rig list is needed ([[QUE-012 Are engineers assigned to rigs or to wells]]).

Later: what "up to 30 logged actions" means; how long the audit log is kept, and whether their ISO 9001
record control applies ([[CON-008 Compliance with ISO 9001, ISO 14001 and API standards]]); units per
user, per job or system-wide ([[REQ-018 Units of measure and conversion]]); where low-stock levels are
set (see W4).

Ask for: the HQ user list (names and roles), current ranges per customer or mud system, who may approve
corrections, the list of rigs.

### W3 Web job management and QC (rows 26-29)

v0: jobs list (rig, well, operator, status, engineers, last sync) with filter and search; job detail
with header, engineers, sections, and a checks-by-parameters table with flagged cells and the reasons;
read-only QC; a supervisor sees the jobs on his rigs.

Blocks:
1. Does QC have an outcome - reviewed, sent back, correction requested? They said "Not at the moment"
   to review workflows (Q&A D.15), yet fear unchecked data reaching customers.
2. Which job fields HQ owns: operator, rig, well, Job#, "order details, quality requirements".
3. Engineers assigned per job or per rig? Does assignment decide who may sign in on that rig PC? The
   client describes crews sent to a rig and staying across wells; the WBS and SOW assign per project
   ([[QUE-012 Are engineers assigned to rigs or to wells]]).

Later: how a supervisor's rigs are defined; the job lifecycle; can jobs be deleted (WBS says CRUD, the
SOW has no delete); trend charts in the measurements view; do managers send anything back to the rigs
([[QUE-002 Do managers send anything back to the rigs]]).

Ask for: active rigs and wells (anonymised), job numbering, the supervisor's daily QC routine today.

### D4 Desktop inventory (rows 62-66)

v0: catalogue synced from HQ; stock per rig and job, starting from an initial loadout; the daily report's
products columns (Start, Received, Returned, Lost, Daily Use, Final, Active and Reserve ending
concentration); concentration entered; low-stock and expiry badges from HQ levels and dates entered at
receipt; no costs on the rig screens.

Blocks:
1. Who owns the product catalogue? Can an engineer add a product at the rig?
2. Stock per rig or per well job? Does it carry over to the next well ("per section and well", Q&A E.24)?
3. Consumption in sacks and drums, or in weight? The sample has two unit sizes for the same product.
4. Concentration entered, or calculated from use and volume?
5. Where are low-stock levels and expiry dates entered? Is expiry kept per lot at receipt?
6. Is mud volume accounting part of the app (pits, active and reserve, losses)? The daily report and
   KPI 3 need it; no WBS line names it.

Later: lab equipment, reagents and calibration - CR or out
([[REQ-016 Inventory of lab equipment and reagents]]); should the engineer see costs.

Ask for: the product catalogue (brand, generic name, material #, unit size, unit, density), a typical
loadout, one real day's products table, low-stock and expiry rules. The price list's structure only;
its figures stay in Drive.

### W4 Web inventory (rows 39-41)

v0: catalogue table and form with low-stock level and shelf life; basic validation on stock entries; the
consumption entries per rig and job, read-only (both promised by the SOW, no WBS line); per-rig stock with quantity, use trend
and cost; rig movements read-only.

Blocks:
1. One company catalogue, or lists and prices per customer or contract? Who provides the "Price List",
   and how often does it change?
2. Who records "Received" - the HQ warehouse or the rig? If both, what happens on sync?
3. Where low-stock levels and expiry dates are set (the SOW contradicts itself; Mikhail's mapping row 4).

Later: how the first catalogue is loaded, with import out of scope; warehouse stock; cost visibility by
role.

Ask for: a catalogue export, how products are dispatched to rigs today.

### D3 Desktop calculations and modelling (rows 58-60)

v0: retort solids computed on save and shown next to the inputs; a weight-up calculator (barite, CaCO3
or a blend, output in sacks and metric tonnes) and an oil/water ratio calculator; a hydraulics form with
the Q&A E.25 inputs, an output table at about 10 flow rates and an x-y operating window with a max
pressure line, as in their program screens; power law; no 3D.

Blocks:
1. The numbered MVP list: which derived values run on save; which calculator functions; which of the
   five hydraulics procedures and outputs ([[CON-003 Correct calculations]],
   [[REQ-007 Derived values and standard calculations]], [[REQ-008 Fluid hydraulics simulation]]).
2. Power law or Herschel-Bulkley, or the engineer's choice?
   ([[QUE-008 Which rheological model the hydraulics must use]])
   - Their step-by-step procedures (Figures 2-1 to 2-5) are the power-law method API used before
     2006. Their program screen, and API RP 13D today (8th edition, April 2026), use
     Herschel-Bulkley.
   - On one test well the two give annular pressure losses about 28 % apart
     ([[2026-10-22 Prototypes against MUDPRO and API]]).
   - When their procedures and API disagree, which governs, and which edition?
3. The units each formula expects; the constants depend on them.
4. Is well geometry, drill string and bit stored on the job, or typed for each run? ECD on save needs
   them.
5. Are the operating-window and surge charts and the well drawing required?
   ([[QUE-003 Do calculations and modelling need 3D or complex visuals]])
6. Which n and k go on the daily report? It has one pair (rows 41, 42). Their procedures have two: the
   pipe from the 600 and 300 RPM readings, the annulus from 300 and 3.

Later: suggested treatments and knock-on effects confirmed out; are past results recalculated when a
formula changes ([[QUE-010 Are past results recalculated when a formula or threshold changes]]); what-ifs
on the web; are calculator results saved to the job; who on their side signs off the test cases, and
what deviation from their reference results is acceptable (MUDPRO's vendor quotes "≤3%" or "±0.3 ppg");
constants that differ between sources: 3.50 in their Equation 10-8 against 3.49 in the API procedure,
and the filtrate density formula.

Ask for: the full formula set with the manual's name and edition, and the missing Figure 3-1, and
whether it is their company standard or an example; units per formula; worked examples with expected
results; the engineers' current Excel calculators; the name of the hydraulics program in their
screenshots and a few exports, and how it gets its yield stress (9 on the screen, 8 by API's
2θ3 - θ6); product specific gravities, and the product data sheets with their weight-up formulas
(whether the OES-BAR formula counts 50-kg sacks); the API documents and editions they work to (RP
13B-1, 13B-2, 13D, 13C), and whether the team can use licensed copies; a named subject expert.

### D5 Desktop reports (rows 68-71)

v0: End-of-Day built from the day's checks, products and volumes in the order of their daily report,
with a PDF preview and CSV/XLSX export; End-of-Section and End-of-Well as summary tables plus simple
trends; the inventory report as the products table per day, section or well; no email button.

Blocks:
1. Is End-of-Day their current "Daily Drilling Fluids Report" with all its blocks, or a subset? Which
   blocks are typed and which computed?
2. What goes into End-of-Section and End-of-Well? No sample on file.
3. Does each operator require its own template or logo?
4. Which daily report form is the reference: their own Daily.xlsx, an operator's form, or the API form
   in the RP 13B annexes? Is Daily.xlsx their own template, or an export from a package, and which one?
   It does not match a MUDPRO report ([[2026-10-21 MUDPRO research]]).

Later: is data locked once the day's report is out; regeneration and versions; what "filterable" means;
report numbering; do their ISO 9001 procedures set how reports are kept, signed or controlled (CON-008);
the engineering-calculation report
([[REQ-017 Report on a single calculation or simulation]], CR candidate).

Ask for: 2-3 real End-of-Day reports, one End-of-Section, one End-of-Well, one inventory report; any
operator templates; OES branding.

### W5 Web reports and approval (rows 33-37)

v0: per-job report list (type, date, engineer, sync time, status: generated, approved, locked); preview
and export; Approve or Lock on End-of-Section and End-of-Well only, by Supervisor or Manager; no reject;
no email.

Blocks:
1. Who approves, in one step or two? What does "Lock" freeze? Can a report be sent back? What happens to
   a locked report if a backfill is approved later? ([[REQ-010 Reports]])
2. Does the web generate reports from synced data, or only show what the desktop generated? Which one
   counts?

Later: fleet-wide or analytics reports - out or CR; a stamp or signature on the PDF.

Ask for: how End-of-Section and End-of-Well are signed today, with examples; recipients by role.

### D6 Desktop dashboard (row 56)

v0: home for the current job - checks done and due today, flagged values, latest properties against
their ranges, top-5 products (section and well), volume and mud-loss trend if volumes are captured,
low-stock and expiry alerts, depth over days.

Blocks:
1. Which KPIs an engineer needs for one rig, as against HQ (their five, Q&A F.27).
2. Where the "targets" come from - the mud program per section, planned depth or days? If from the mud
   program, is it entered in the app? No WBS line names it.

Later: offset-well comparison needs past wells, and import is out ([[REQ-015 Import of historical data]]);
is the dashboard the home screen.

Ask for: KPI definitions, a mud program with target ranges and planned depths, the charts they use today.

### W6 Web dashboard (row 31)

v0: fleet table (rig, well, section, depth today, last check, last sync, flags in 24 hours, stock and
expiry alerts) filtered by supervisor or customer; drill-down with parameter by depth, top-5 products,
volume and loss trend; no offset wells.

Blocks:
1. Which KPIs on the fleet view and which on the drill-down? Define "critical mud parameter",
   "volume-out alert" and "drilling progress status", and where targets come from
   ([[REQ-011 Dashboards and KPIs]]).
2. Drop the offset-well comparison from the MVP, given no historical import and 1-2 years' retention?

Later: flagging rigs not synced for X hours; the layout for 70 to 100 rigs.

Ask for: KPI formulas and targets, current management dashboards or Excel, the list of critical
parameters.

### X - the tech session and the cross-cutting questions

- X1 Offline and sync ([[CON-001 Offline operation and sync between rigs and HQ]]): actual
  connectivity per rig; rigs never online, and is USB transfer acceptable; what "99.9% data integrity"
  means and how it is measured; the longest acceptable delay before HQ sees data; recovery when a rig
  PC is replaced.
- X2 Rig PCs, updates and handover ([[CON-002 Deployment outside public cloud]]): what the final
  handover delivers to their servers and what our technical documentation consists of; the PC inventory (OS, specs,
  admin rights, endpoint security); how OES installs software on rig PCs today and who does it; forced
  or optional updates, and may a rig run an old formula version; who owns the code-signing
  certificate; install at HQ before the PC ships, or at the rig.
- X3 Hosting and compliance: who provisions the environments, and whether monitoring, backup and
  load balancing are ours (in the WBS, not the SOW); their own server or GCP in Dammam, who opens the account and who pays
  (DEC-012, K-1); NCA category A or B ([[QUE-005 Is the client an NCA Category A or B entity]]); their
  list of applicable requirements, which the SOW has them provide before the start; who owns
  cybersecurity at OES; do customers such as Saudi Aramco impose rules on data about them. On 20
  October Mr. Lawal named ISO 9001, ISO 14001 and API. Which of their procedures touch the app, such as
  record control and traceability of results? Does "API compliance" mean the test and calculation
  methods (RP 13B-1, 13B-2, 13D), or more?
- X4 Units ([[CAP-007 Units of measure]]): which three sets, chosen per user, per job or per report;
  precision per parameter.
- X5 Out of scope, to confirm out or CR: past-well data at go-live, the documents HQ needs at the rig,
  who would use an API, any ERP holding the catalogue and prices, calibration records for the rig
  instruments (the RP 13B annexes; the viscometer is checked monthly) and their intervals under ISO 9001.
- X6 People: who gives the written OK per area; can we have 2-3 mud engineers and a supervisor in
  sessions; is an interpreter needed for demos to the decision-maker.
- X7 The tool they used before ([[2026-10-21 MUDPRO research]]). "Mod4" on the 20 October call is most
  likely MUDPRO 4.
  - Which product and version: MUDPRO 4, MUDPRO+, MudManager as well? Is it still in use?
  - What fell short, in their words: features, cost, or how data moves between rig and office?
  - Do past wells sit in its files ([[REQ-015 Import of historical data]], out of scope)?
  - Ask for: a daily report and an end-of-well recap exported from it. Could an engineer show it on a
    screen share in one session?
