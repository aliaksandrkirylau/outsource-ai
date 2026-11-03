# OE desktop app prototype - plan

Status: working draft. Created 2026-10-14; shared with the team in optimum-kb pm/prototypes/ on 2026-10-17.
Tool: Claude Design (artifact on claude.ai, owner Mikhail) + the HTML sources in this folder.

## Inputs
- WBS v1, tab "Development Flutter" - desktop lines marked MVP only.
- Presale architecture doc (ASRs, NFRs, proposed solution).
- Client answers to the Q&A register (2025-10-29) and notes of the first call with OES (2025-10-22).
- Client sample daily report (parameter list, report layout), client formula and chart samples.
- KB decisions: DEC-005 (desktop at rig, web at HQ), DEC-007 (Flutter), DEC-010 (prototypes in code).

## Decisions taken (Mikhail, 2026-10-14; 4 changed 2026-10-15)
1. Colours for the UI kit come from screenshots of oes.com.sa and its product data sheet PDFs.
2. MVP scope only (WBS Stage = TRUE). Optional lines out: onboarding wizard, location management,
   project templates.
3. Measurement parameters come from the client's sample daily report (~30 mud properties).
4. Static mock data first - REPLACED 2026-10-15: real calculations with the client's formulas, marked
   "Not verified - for discussion" (see calc/OE prototype - calculation notes.md).
5. Everything stays private for now (until 2026-10-17, when it was added to optimum-kb pm/prototypes/).

## Ground rules for every screen
- Standard Flutter Material 3 widgets only: NavigationRail, AppBar, Card, TextFormField,
  DropdownMenu, DataTable / PaginatedDataTable, TabBar, Dialog, SnackBar, Chip, FilledButton /
  OutlinedButton, Badge. Charts: line / bar / pie only (fl_chart-level).
- Theme: ColorScheme.fromSeed(OES orange), light theme only, English only.
- Tables: one search box at most, sorting on 1-2 columns, no per-column filters.
  Report "filters" = date range + well section only.
- Rig laptop: frame 1440x900, check at 1366x768.
- One mock data set across all modules (one well, one rig, two engineers, fixed product list).
- Desktop = Engineer role only. Approvals happen in the web app; desktop shows the status.

## Per-module loop
1. Screen list + main flow -> Mikhail confirms or cuts.
2. Build in Claude Design.
3. Review, comments.
4. 1-2 revision rounds, freeze, link into the shared app frame. Save local HTML copy.

## Steps
- Step 0 - Foundations: brand palette, UI kit (also candidate for SOW M1 "UI Kit"), app frame
  (rail, top bar with current project, offline/sync label), mock data.
- Step 1 - Sign-in and projects: pick user on the shared rig PC + password; project list,
  create/edit project (location, client details), set active.
- Step 2 - Measurements: mud check form per shift (<50 params, grouped as in the daily report),
  range hints on fields, out-of-range highlight + mandatory comment -> "flagged", derived values
  after save, shift history, edit past entry with reason -> "Pending approval".
- Step 3 - Inventory: products on rig (stock, min level, expiry), daily consumption, movements
  (loadout / received / returned / lost), concentration lb/bbl, low stock and expiry warnings.
- Step 4 - Calculations: calculator (3-4 standard calcs from client samples, e.g. barite to raise
  mud weight); hydraulics simulation (input tabs: well, string/BHA, fluid, pumps, bit, formation ->
  results table across flow rates + 2 x-y charts).
- Step 5 - Reports: EOD, EOS, EOW, Inventory; preview + PDF/CSV/XLSX export buttons; EOS/EOW
  submit for approval + status.
- Step 6 - Dashboard: one page for the current well (parameter trend, top-5 products,
  volumes/losses, alerts).
- Step 7 - Settings: unit set (1 of 3), sync status.
- Step 8 - End-to-end "engineer's shift" walkthrough for the client demo.
- Later - Web app, same approach.

## Brand palette (sampled from Mikhail's screenshots, 2026-10-14)
- Data sheet banner / site nav orange: #ED712E (nav variant #EE8438)
- Site header amber: #F2A743
- Light orange (data sheet arrow gradient): #F6CD96
- Logo red (low-res sample): ~#B83830
- Greys: logo grey #585858, band #CCCCCC, page background #F7F7F7, side slate #B1B3B8

## Where things are
- Claude Design (owner Mikhail, ask him for access): "OE Prototype - desktop and web", https://claude.ai/artifact/2LxwhYmHh42ktCAqQnEdDu
  Pages: "Demo walkthrough" (opens first; script with links into every screen), "Step 0 - Foundations" (UI kit, app frame, mock data, top bar and rail components),
  "Step 1 - Sign-in and wells" (start at 1.1 and press Play), "Step 2 - Measurements" (start at 2.1), "Step 3 - Inventory" (start at 3.1), "Step 4 - Calculations" (start at 4.1), "Step 5 - Reports" (start at 5.1), "Step 6 - Dashboard", "Step 7 - Settings".
- Here: "OE prototype - desktop demo script.md" (printable copy of the walkthrough); "calc/" = calculation engine, test values and notes (formulas, our assumptions);
  "UI Kit v0.2.html" opens in a browser; "source/" = all Claude Design files, exported with the runtime
  so they also open in a browser (see the read me); superseded versions are not copied here.

## Theme (Step 0, approved; v0.2 overrides 2026-10-14)
- ColorScheme.fromSeed(seedColor: Color(0xFFED712E), dynamicSchemeVariant: DynamicSchemeVariant.fidelity)
  .copyWith(secondaryContainer: Color(0xFFF6CD96))
  -> primary #A14000 (buttons; white on #ED712E is only 3:1), primaryContainer #ED712E (exact brand).
- App bar: background primaryContainer #ED712E, text #521D00, 4 px amber #F2A743 line below (site header).
- secondaryContainer #F6CD96 (data sheet tint): menu highlight, tonal buttons, "watch" chips.
- Status: red errorContainer = act now (flagged, out of range, expired, out of stock); orange
  secondaryContainer (#F6CD96) = watch (low stock, expiring); blue outline = waiting (pending approval/sync);
  grey outline = done/neutral. Always icon + word.
- Font Segoe UI (Windows default), icons Material Symbols (= Flutter Icons.*).

## Navigation and project decisions (2026-10-14)
- Project = one well job (TRM-005), not a rig. A rig drills one well after another (5-10 in six months)
  and the computer stays with the rig (TRM-004). One well in progress at a time; completed ones read-only.
- Top bar: OES, this computer's rig (fixed label), well switcher, sync status, user menu (Settings, Sign out).
- Left rail = the chosen well only: Dashboard, Measure, Inventory, Calculate, Reports.
- Wells: created and edited on BOTH desktop and web, as in SOW v10.4 (scope rows 7-8; Milestone 3 web
  "Project management (create, edit, assign)" and desktop "Project management feature"). Engineers are
  assigned only on the web (SOW M3). Mikhail, 2026-10-14 (replaces the earlier web-only call).
- Engineers: assigned to RIGS at HQ on the web (Mikhail, 2026-10-14; replaces "assign on desktop").
  Everyone on a rig works on all its wells; desktop forms show "Engineers on this rig" read-only.
  Differs from WBS/SOW wording (assign per project) and needs a plain rig list (WBS row 23 Location
  Management is optional/out): raised as QUE-012 in optimum-kb.
- Well details: no separate read-only page. The switcher lists wells (= "project list"); the pencil
  opens the form (= "details", view and edit). SOW M3 desktop: "Viewing the project list and details".
- Well fields are not specified anywhere (WBS/SOW: "location, client information, and so on"; first
  call: "id, basic details, location, info on client, order details, quality requirements, etc").
  Prototype fields come from the client daily report header. Field list is an SOW M3 deliverable
  ("Detailed user and project management specifications: fields, statuses ...").
- OPEN for discovery (SOW M3 already lists "how project assignment works ... sync behaviour"): the same
  well created at the rig and at HQ (duplicates), and edits to the same well on both sides before sync.

## Log
- 2026-10-14: plan agreed; Step 0 started.
- 2026-10-14: Step 0 draft built (UI kit, app frame, mock data); waiting for Mikhail's review.
- 2026-10-14: Step 0 approved by Mikhail: dark orange buttons + brand orange accent, warm M3 background,
  status colours as proposed; rail items and mock data kept as is for now. Step 1 screen list proposed.
- 2026-10-14: Mikhail: wells created and engineers assigned only in web; project switch moved to top bar,
  rail = chosen well only. App frame updated (well switcher, user menu, read-only state for completed wells).
- 2026-10-14: Mikhail reversed: desktop creates and edits wells too (per SOW). App frame: New well in the
  switcher, Edit in Well details.
- 2026-10-14: Mikhail: site oranges missing in the screens. Fixed: orange app bar + amber line, #F6CD96 for
  highlights (UI kit v0.2). Top bar and rail made shared components.
- 2026-10-14: Step 1 built: 1.1 pick user, 1.2 password, 1.3 wrong password, 1.4 no well yet, 1.5 well
  details, 1.6 create/edit well. Waiting for review.
- 2026-10-14: Mikhail's Step 1 review: switcher note removed; Well details removed from the menu and the
  read-only page dropped (pencil per well opens view/edit); New well is its own empty form (1.5); engineers
  assignable on the desktop (checkbox card in both forms).
- 2026-10-14: engineers assigned to rigs (web); tick boxes removed from 1.5/1.6, read-only rig list shown.
  QUE-012 added to optimum-kb and pushed (adf4ac3).
- 2026-10-14: Step 2 built (WBS desktop rows 51-53, 58; edit approval per REQ-006 / web row 21):
  2.1 mud check list (2 days, statuses Saved / Waiting to sync / Flagged / Pending approval),
  2.2 new check (32 fields in 6 cards, range hints, live check: out of range -> reason dialog -> Flagged;
  impossible value -> save blocked), 2.3 check detail (flag, calculated n/k/ECD, Edit -> reason ->
  Pending approval). Assumptions: any edit of a saved check needs approval (discovery D2.7 open);
  backfill of a missed check not drawn; units fixed to oilfield (toggle in Step 7). Waiting for review.
- 2026-10-14: Step 3 built (WBS desktop rows 61-66; columns as the client daily report's products table):
  3.1 products table (start, received, returned, lost, used today, final, min, concentration, expiry,
  status) + stock movements tab; 3.2 today's use for all products at once, live final and low-stock /
  out-of-stock, using more than available blocks save; 3.3 movement form (loadout / received / returned /
  lost; expiry for received and loadout; reason required for lost). Assumptions: catalogue, unit sizes,
  minimum levels from HQ; no costs on rig screens (web row 41); active concentration only (reserve left
  out); loadout one product at a time; movements corrected by an opposite movement, no edit; stock per
  well (discovery D4.2 open). Waiting for review.
- 2026-10-15: Mikhail kept the 12-column inventory table as is (columns trace to WBS rows 62-66 and the
  client daily report products table).
- 2026-10-15: Step 4 built (WBS desktop rows 59-60; row 58 derived values already in 2.3): 4.1 calculator
  with weight-up (OES-BAR data sheet formula) and oil/water ratio (OBM only), static results;
  4.2 hydraulics inputs in 6 tabs per Q&A E.25 (well, string/BHA, fluid from last check, pumps with
  flow-rate range, bit, formation); 4.3 results: 5 summary cards for a chosen flow rate, SPP operating
  window with max SPP line, ECD vs pore/fracture chart, table across 8 flow rates. Assumptions: power law
  (QUE-008 open), outputs list to confirm (surge/swab, hole cleaning not drawn), results not saved and no
  calculation report (QUE-004, CR candidate). Waiting for review.
- 2026-10-15: real calculations added (Mikhail: all three parts): 2.2 live n/K, retort solids, LGS, barite
  (retort solids now calculated from water + oil); 2.3 shows engine values; 4.1 weight-up and OWR live with
  input checks; 4.2 and 4.3 merged into one live screen (inputs tabs + Results tab: SPP, ECD, bit, HSI,
  charts, table, hole cleaning, surge/swab). Finding: client Fig. 2-2 as transcribed is missing x100
  (critical velocity 18 vs 380 ft/min) - ask the client. OES-BAR concentration in inventory mock set to 18
  lb/bbl to match the solids calculation.
- 2026-10-15: Step 5 built (WBS desktop rows 68-71; approval per Q&A D.14, web row 33): 5.1 report list
  (4 types, statuses: day not closed / exported / waiting for HQ approval / approved, locked); 5.2 end-of-day
  preview in the order of the client's daily report (header, mud properties for 4 checks with flag in red,
  calculated rheology/ECD/solids from the engine, products used, comments) with include/exclude blocks
  (= "filterable") and PDF/Excel/CSV export; 5.3 one screen for end of section (submit -> waiting for HQ;
  17½ in shown approved and locked), end of well (submit only when the well is completed) and inventory
  (section or whole well). Assumptions: no email button (export, then email as today); volumes/pits, pumps,
  bit/BHA, solids control, costs left out of the daily report (no entry screen or WBS line; discovery D4.6,
  D5.1); section and well report content is our proposal (no client sample, D5.2). Waiting for review.
- 2026-10-15: Step 6 built (WBS desktop row 56; KPIs from Q&A F.27): 6.1 dashboard = home after sign-in
  (sign-in, logo, wells, new/edit well now lead here). 5 KPI tiles (depth and % of planned TD, checks done
  today, flagged this section, stock alerts, ECD at bit), "needs attention" list linking to the screens
  (out of stock, below minimum, expiring, flagged check, approval pending, sync), latest check vs ranges,
  density/PV by depth, product use top 5 + others with pie (section / whole well), drilling progress
  depth vs days. Left out until confirmed: offset-well comparison (needs past wells; import out), volume
  trend and mud losses (no volume entry), calibration alerts (lab equipment not in WBS). Settings still
  goes to the placeholder (Step 7). EOW mock "products used" aligned to 5,045 sacks. Waiting for review.
- 2026-10-15: Step 7 built (WBS desktop row 54; sync per CAP-002): 7.1 settings from the user menu.
  Units: 3 sets (API oilfield / SI / mixed: SG, m, L/min, bar, m3, lbf/100ft2, kg/m3, degC) with live
  example values and converted ranges for 8 quantities; applies on this computer, values stored in one
  base unit. Sync: offline status, queue of 3 changes, Sync now -> synced with 2 items received from HQ
  (approval of the 08:00 correction, new minimum level). Placeholder app frame (Shell) removed; every
  screen now leads to a real one. Assumptions: units per computer (REQ-018: per user, job or system is
  open), the three sets to be confirmed by the client. Waiting for review. Next: Step 8 walkthrough.
- 2026-10-15: Step 8 done: "Demo walkthrough" page, opens first. 11 steps (sign-in, dashboard, well, mud
  check with flag, correction, inventory, calculator, hydraulics, end-of-day report, section approval,
  settings and sync), each with links to its screens, what to do, what to say, questions for the client
  (from the discovery sheets and our open points) and what is "not yet". Opening and closing notes: data is
  invented, calculations unverified, a demo is not acceptance - written OK per area. Link check: 23 screens,
  no broken links. Desktop prototype complete; next: review, then the web app (same approach).
- 2026-10-15: Web prototype built (see OE prototype - web plan.md, log). Desktop changes: ReportSummary 12¼ in
  products used 1,908 -> 1,889 sacks; Demo "Keep in mind" points to the web demo.
