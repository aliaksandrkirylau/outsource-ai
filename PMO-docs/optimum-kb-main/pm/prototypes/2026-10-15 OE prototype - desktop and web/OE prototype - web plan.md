# OE web app (HQ) prototype - plan

Status: proposed 2026-10-15; decisions taken (below) and built 2026-10-15. Shared in optimum-kb 2026-10-17.
Same file as the desktop: new pages "Web W0" ... "Web W8" in the Claude Design file "OE Desktop Prototype",
so the demo can jump between rig and HQ (rig submits, HQ approves). Local copy in this folder as before.

## Same rules as the desktop
- MVP lines only (WBS "Development Flutter" rows 15-41, Stage = TRUE). Out: Location Management (row 23),
  Project Template Management (row 24) - optional in the WBS.
- Standard Flutter Material 3 widgets (also valid for React + MUI if the web stack changes). Same theme:
  seed #ED712E, orange app bar + amber line, #F6CD96 highlights, dark-orange #A14000 buttons, same status
  colours, Segoe UI, Material Symbols. Same shared top bar and rail pattern.
- One desktop browser resolution, English only (SOW M3: "single desktop resolution, English only").
  Frame 1440, checked at 1280.
- Tables: one search box, one filter (rig or status) where the WBS says "filter", sort on 1-2 columns.
- Same mock data as the desktop, plus 4 more rigs and HQ users. Calculations reuse the desktop engine
  (web shows results, does not calculate anything new).
- The web reads what rigs synced; it never edits a rig's measurement directly (corrections go through
  approval).

## Roles (proposal)
Three roles, as the WBS (row 19): Admin, Supervisor/Manager, Engineer (desktop only). Supervisor/Manager
sees only the rigs assigned to them; a manager is simply assigned all rigs. A role switcher in the top bar
is for the demo only. (Client Q&A D.13 lists four roles - discovery W1.1.)

## Steps
- W0 Foundations: web frame (top bar: OES, "HQ", rig filter, user menu with role switcher; rail:
  Dashboard, Wells, Approvals, Reports, Inventory, Admin), mock data (7 rigs, 3 HQ users), UI kit
  additions only if needed (none expected).
- W1 Sign-in and users (rows 16, 17, 19): email + password sign-in; Admin: user list (name, role, rigs,
  active, last sign-in), user form (role, rigs assigned), deactivate/reactivate; plain rig list (name,
  active) - needed if people are assigned to rigs (QUE-012).
- W2 Wells (rows 26-28): wells list across rigs (rig, well, operator, section, depth, status, last sync)
  with search + rig filter; create/edit well (same form as desktop 1.5/1.6); well detail with tabs:
  Mud checks (checks x parameters table, flagged cells with reason), Inventory, Reports.
- W3 Approvals and quality control (rows 21, 29, 33): one inbox for the supervisor: flagged checks to
  review (read-only, "reviewed" mark), corrections to approve or reject (old -> new, reason), section/well
  reports to approve or send back. Linked to desktop 2.3 and 5.3.
- W4 Admin settings (rows 20-22): thresholds table (parameter, unit, min, max; company default with an
  override per well), default unit set, audit log (who, when, what, old -> new, status).
- W5 Inventory (rows 39-41): product catalogue (brand name, generic name, material #, unit size, unit,
  density, minimum level) with add/edit; price list (unit price per product); stock by rig (read-only,
  from sync) and stock movements log across rigs.
- W6 Reports (rows 33-37): report list across rigs (type, well, period, made by, status); preview reusing
  the desktop layouts, with costs (daily cost, cumulative) shown on the web only; PDF/Excel/CSV export;
  approve / send back on section and well reports.
- W7 Dashboard (row 31): fleet one-page view with search + rig filter: KPI tiles (active rigs, rigs not
  synced 24 h, flagged checks 24 h, pending approvals, stock alerts), rig status table, simple bar/pie
  charts (flags per rig, product use), drill-down = well detail (W2).
- W8 Demo walkthrough HQ: a supervisor's morning, linked to the desktop demo at the hand-over points.

## Open decisions for Mikhail (before W0)
1. Web stack: Flutter Web or React (DEC-007 left it open). Prototype is drawn the same either way; say if
   React so components are named as MUI.
2. Rig list: add the plain rig list (QUE-012, row 23 is optional/out) or not.
3. Roles: three as the WBS, or four as the client's Q&A to test in the demo.
4. Prices and costs: visible to all HQ roles or Admin/Manager only.
5. Same Claude Design file (recommended) or a separate one.

## Decisions (14 Oct 2026)
Flutter Web; plain rig list included; three roles (Admin, Supervisor / Manager, Engineer); prices and
costs for Admin and Supervisor / Manager only; same Claude Design file. Build all steps without review
stops; questions and issues collected in "OE prototype - issues, inconsistencies and client questions.md".

## Log
- 2026-10-15: W0-W8 done in one go and published to the same Claude Design file (now "OE Prototype -
  desktop and web"), pages Web demo walkthrough, W0 Components, W1 Supervisor (sign in, dashboard,
  approvals, wells, well DW-217, new well), W2 Supervisor (reports, section report with cost and
  approve / send back, inventory across rigs), W3 Admin (users, rigs, thresholds with per-well override
  and default units, products with prices, audit log). 17 web files (15 screens + top bar + menu).
  Mock time 14 Oct 2026 15:30, same data as the desktop after Rig 07's 15:20 sync. Story aligned with
  the desktop: Faisal approved the 08:00 correction at 13:20 (desktop Settings 13:31), xanthan minimum
  10 -> 12, section products used 1,889 sacks (desktop fixed from 1,908). Desktop demo now points to
  the web demo. Tests: calc/webtest.js (logic and bindings), link check over 41 screens: no broken links.
  Not checked visually in a browser yet.
