# OE prototypes - issues, inconsistencies and client questions

Working material (pm/), not evidence. Written 15 Oct 2026, shared 17 Oct 2026. Covers the desktop prototype (steps 0-8) and the web prototype (W0-W8) in Claude Design "OE Prototype - desktop and web".
Sources: WBS v1 (Development Flutter), SOW v10.4, presale ASR doc, Q&A register (2025-10-29), first-call notes (2025-10-22), client sample daily report and formula sheets, optimum-kb decisions and questions.
IDs are for reference in reviews; KB question numbers (QUE-xxx) are given where one exists.

## 1. Inconsistencies between the sources

| ID | Topic | What conflicts | How the prototype handles it |
|---|---|---|---|
| S-01 | Roles | WBS: 3 roles (Admin, Supervisor / Manager, Engineer). Q&A D.13: 4 (engineer, supervisor, operations manager, admin). | 3 roles. Supervisor and manager differ only in rig scope. |
| S-02 | Who approves | Q&A answers and desktop text: "operations manager or system admin". WBS web row 21/33: supervisor approval. | Desktop says "HQ"; on the web the supervisor (Khalid) and the manager (Faisal) both approve. |
| S-03 | Engineer assignment | WBS and SOW: engineers assigned per project (well). Our decision: engineers assigned to rigs (QUE-012). | Assigned to rigs on the web Users page; desktop shows "Engineers on this rig" read only. |
| S-04 | Rig list | Assigning to rigs needs a rig list, but WBS row 23 (Location Management) is optional / out. | Plain rig list on the web (name, active). Scope point. |
| S-05 | Where wells are created | SOW M3: create and edit projects on both desktop and web; engineers assigned on the web only. | Wells created on both sides; duplicates possible (QUE-011). |
| S-06 | Two-factor sign-in | NCNICC-1 asks for MFA; the SOW excludes it. | Email and password only. |
| S-07 | Rheology model | Client formulas are power law; their sample hydraulics program uses Herschel-Bulkley (QUE-008). | Power law. |
| S-08 | Critical velocity | Fig. 2-2 as transcribed gives about 18 ft/min, which is unrealistic. With ×100 (as in Fig. 2-1's μea) it gives about 380 ft/min. | ×100 applied, marked unverified. |
| S-09 | Bit hydraulics | Figure 3-1 is referenced in the client material but was not sent. | Standard formulas used (calc notes, assumption 1). |
| S-10 | Well fields | Not specified anywhere. WBS/SOW say "location, client information, and so on"; the first call adds "order details, quality requirements". | Fields taken from the client daily report header. The field list is an SOW M3 deliverable. |
| S-11 | Daily report blocks | The client's sample daily report has volumes/pits, pumps, bit/BHA, solids control and costs; no WBS line covers entering them. | Left out of the daily report and marked "not yet". |
| S-12 | Unit setting scope | REQ-018 leaves open whether units are per user, per job or system-wide. | Per computer, 3 sets (API / SI / mixed). Web Admin sets the default for new rig computers. |
| S-13 | Costs | WBS web row 41 has a price list; rig screens show no costs; the client daily report has a cost block. | Prices and costs on the web only (Admin, Supervisor / Manager). |
| S-14 | Web stack | DEC-007 left Flutter Web or React open. | Flutter Web (Mikhail, 14 Oct). Needs recording as a decision in the KB. |
| S-15 | Stock per well or per rig | Not stated (discovery D4.2). Rig stock physically carries over to the next well. | Stock per well, with a loadout at the start of each well. |

## 2. Inconsistencies found in the prototype data and fixed

| ID | What was wrong | Fix |
|---|---|---|
| F-01 | Critical velocity unrealistic (18 ft/min) | ×100 added (see S-08) |
| F-02 | OES-BAR concentration 85 lb/bbl did not match the solids calculation | 18 lb/bbl |
| F-03 | Loadout total did not match the product list | 2,700 sacks |
| F-04 | Well inventory: barite received did not add up | 3,200 sacks |
| F-05 | End-of-well products used did not match the inventory | 5,045 sacks |
| F-06 | Daily report dial readings did not give the shown PV/YP | Readings made consistent |
| F-07 | 12¼ in section report: products used 1,908 vs 1,889 in its own inventory table | 1,889 on desktop and web |
| F-08 | Desktop Settings shows HQ approving the 08:00 correction; the first web draft still had it pending at 15:30 | Web: Faisal approved at 13:20 (audit log, well page); rig received it at 13:31 |
| F-09 | Desktop Settings receives "new xanthan minimum"; web catalogue still showed 10 | Web shows 12 (Products, Inventory, well page), with an audit entry |
| F-10 | Web threshold override on DW-217 contradicted the desktop ranges for DW-217 | Override moved to KH-104 (density 10.5 - 12.0 ppg) |
| F-11 | Web section report figures (74 checks, 2 flags) differed from the desktop (94, 6) | 94 checks, 6 flags, with 6 reasons listed |

## 3. Inconsistencies still in the prototype (known, not fixed)

| ID | Where | Issue | Suggested handling |
|---|---|---|---|
| P-01 | Desktop 2.1 vs 2.3 | The mud check list (2.1) ends at 08:00 and shows 08:00 as "Pending approval". The detail screen (2.3) shows a 14:00 check with the PV correction. The screens show different moments of the day. | Say so in the demo, or add the 14:00 row to 2.1 |
| P-02 | Desktop dashboard vs Settings | Dashboard: "08:00 correction waiting for HQ approval". Settings after sync: "approved". Before and after the sync, but nothing on screen says so. | Mention it in the demo |
| P-03 | Desktop Inventory vs web | Xanthan minimum is 10 on the desktop (before the sync) and 12 on the web (after) | Intentional; explain if asked |
| P-04 | Mud check PV 41 story | Flag reason "fine solids building up" contradicts the later correction reason "re-ran the test after cleaning the viscometer cup" | Change one of the two reasons before the client demo |
| P-05 | Web "View as" Faisal | Faisal (manager, all rigs) lands on Khalid's dashboard: "Good afternoon, Khalid" and 3 rigs | Draw a manager variant, or tell the client it is the same screens with all rigs |
| P-06 | Web menu badge | Approvals badge stays at 5 after items are approved (static) | Prototype limitation |
| P-07 | Web reports list | Every row opens the same 12¼ in section report | Prototype limitation, stated on the screen |
| P-08 | Web dashboard | The plan said "rigs not synced 24 h"; the screen uses "> 12 h" | Ask the client (Q-29) |
| P-09 | Charts | Desktop dashboard and reports use pie and line charts (needs a chart package such as fl_chart); web uses plain bars only | Decide one approach (I-03) |
| P-10 | Web Rigs | "7 of about 70" rigs: the 70 is our assumption | Confirm (Q-05) |
| P-11 | Prices | All prices and costs are invented | Do not show figures as estimates; say they are mock data |

## 4. Issues and risks (internal)

### Scope
- I-01 **Rig list.** Added although WBS row 23 is optional (S-04). Needs an estimate line or a change request.
- I-02 **Costs on the web.** These need a price per product, a cost per section (use × price) and cost on dashboards. Check the WBS (row 41 covers the price list only).
- I-03 **Chart package.** Pie, line and x-y charts (desktop dashboard, hydraulics, reports) need a third-party package, outside standard Material. This conflicts with the "standard widgets only" rule; agree it once (fl_chart).
- I-04 **Hydraulics.** No calculation report and results are not saved (QUE-004, change-request candidate). The list of outputs is not confirmed; surge/swab and hole cleaning are shown but may be beyond what was estimated.
- I-05 **"Not yet" items the client may expect:**
  - offset-well comparison (needs past wells; import is out);
  - volume and loss trends (no volume entry);
  - calibration alerts (lab equipment not in the WBS);
  - email from the app;
  - per-operator report templates;
  - ordering and transfers from HQ;
  - email/SMS alerts;
  - export of the audit log.
- I-06 **Demo risk.** Whatever the prototype shows may be read as in scope. Each area needs a written OK by email; a nod in a call is not acceptance.

### Behaviour we assumed (each one needs confirmation)
- I-07 Any edit of a saved mud check needs HQ approval, even in the same shift (D2.7).
- I-08 An out-of-range value needs a reason and is flagged. An impossible value blocks saving. Nothing else blocks.
- I-09 Threshold changes reach the rig with the next sync, and existing checks are not re-flagged (QUE-010).
- I-10 Rejected corrections keep the original value; the engineer sees the comment after his next sync (QUE-002).
- I-11 One approval step. An approved section report is locked on the rig. An end-of-well report can be submitted only when the well is completed.
- I-12 HQ is read-only for rig data (mud checks, stock); it only decides, and never edits values.
- I-13 Admin sees setup screens only, not rig data.
- I-14 Stock movements are corrected by an opposite movement, never edited. The loadout is entered one product at a time.
- I-15 Concentration is entered by the engineer (active only; reserve is left out).
- I-16 A missed check can't be backfilled (not drawn).
- I-17 Units are set per computer and stored in one base unit.
- I-18 One well in progress per rig; completed wells are read-only.

### Calculations (from calc notes)
- I-19 Nothing is verified against worked examples; screens are marked "Not verified - for discussion".
- I-20 **Our own assumptions:**
  - bit pressure drop, jet velocity and HSI;
  - surface loss constant E = 4.2e-5;
  - surge/swab velocity unit conversion;
  - oil/water ratio by volume balance;
  - ECD without cuttings or temperature effects;
  - low-shear K without the 5.11 factor.
- I-21 Hole cleaning uses the ×100 critical velocity (S-08).

### Sync and data
- I-22 The same well can be created at the rig and at HQ while offline, giving duplicates. Edits to the same well on both sides before a sync conflict (QUE-011). The prototype only shows a warning.
- I-23 There is no live data at HQ: everything is as of each rig's last sync. The client must understand that the web is not real-time.

### Prototype quality
- I-24 Tested with the logic harness and the link check (41 screens, no broken links). On 20 Oct 2026 all 41 files were rendered in Chromium (local server): no errors; approvals and menu links click through. Not yet checked: Edge on Windows, and every screen by eye.
- I-25 "View as" in the web user menu is a demo aid, not a feature.
- I-26 The Claude Design prototype is not shared yet (owner Mikhail), and the KB has no Question notes for the new client questions yet.

## 5. Questions for the client

### Users, roles and access
- Q-01 Three roles as in the WBS, or four as in Q&A D.13? With three, supervisor and manager can't differ in rights (S-01).
- Q-02 Does each supervisor cover a fixed set of rigs, and do managers see all rigs?
- Q-03 How many HQ users are there? Who adds engineers and resets passwords?
- Q-04 A personal account per engineer on the shared rig computer, or is a Windows login enough?
- Q-05 Can you send the rig list (about 70?) and which rigs each person works on?
- Q-06 Are engineers assigned to a rig for a period, or to each well? Is one engineer on several rigs normal? (QUE-012)
- Q-07 MFA is asked for by NCNICC-1 but excluded in the SOW: which applies? Is single sign-on needed?
- Q-08 Should Admin see rig data, or only setup?

### Wells
- Q-09 Who usually opens a new well, HQ or the rig engineer? Which fields come from HQ?
- Q-10 If HQ and the rig both create or change the same well offline, which one wins? (QUE-011)
- Q-11 What are "order details" and "quality requirements" on a well? Can you send the full field list?
- Q-12 Is stock kept per well, or does it carry over to the next well on the rig?

### Mud checks, ranges and approvals
- Q-13 Is the sample daily report's parameter list the right one? Does it change for water- vs oil-based mud?
- Q-14 Are ranges set per customer (operator), per mud system or per well? Can you send the ranges you use today?
- Q-15 Which out-of-range values block saving and which only flag?
- Q-16 Can an engineer fix his own check in the same shift without approval?
- Q-17 Who approves corrections and section/well reports: supervisor, operations manager or admin? One step or two? (S-02)
- Q-18 Do flagged checks need a review at HQ, or is the engineer's reason enough?
- Q-19 Is "send back with a comment" needed for reports and corrections? (QUE-002)
- Q-20 When a threshold or formula changes, must past results be recalculated or re-flagged? (QUE-010)

### Inventory and prices
- Q-21 Is concentration typed in or calculated? Where are expiry dates entered?
- Q-22 Who records deliveries: the rig when they arrive, or HQ when they ship?
- Q-23 Who maintains the product catalogue and prices? Is there one price list for all rigs and contracts, in SAR?
- Q-24 Do you need a stock report across all rigs?

### Calculations and hydraulics
- Q-25 Which calculations do engineers use daily besides weight-up and oil/water ratio?
- Q-26 Can you send worked examples with expected results for each formula, the manual's name and edition, and one well's export from your current hydraulics program?
- Q-27 Power law, or Herschel-Bulkley like your current program? (QUE-008)
- Q-28 Figure 2-2 seems to be missing a factor of 100: can you confirm? Can you send Figure 3-1?
- Q-29 Which hydraulics outputs are needed for the first release? Is a separate calculation report expected? (QUE-004)

### Reports
- Q-30 Is the sample your full daily report or a subset? Which blocks are must-have (volumes, pumps, bit, solids control, costs)?
- Q-31 What must a section and a well report contain? Can you share one of each, and 2-3 real daily reports?
- Q-32 Does each operator need its own template or logo?
- Q-33 Does HQ only receive the reports made on the rig, or must the web build reports itself? Should cost appear on an internal PDF?

### Dashboard, sync and alerts
- Q-34 Which of your five KPIs does the engineer need on the rig, and which only HQ? Where do targets come from (mud program, planned depth by day)?
- Q-35 After how many hours without a sync should a rig be shown as late (12 h or 24 h)? Are email or SMS alerts needed?
- Q-36 Which unit sets do you use, and are they set per computer, per user or company-wide? (REQ-018)

### Audit
- Q-37 How long must the audit log be kept, who may see it, and is an export needed?

### What to ask them to send
- Parameter list per mud system.
- Threshold ranges in use.
- Worked calculation examples, the manual reference and Figure 3-1.
- One hydraulics program export.
- 2-3 real daily reports, one section report and one well report.
- Unit sets in use.
- Rig list and the users with their roles.
- Product catalogue with prices.
