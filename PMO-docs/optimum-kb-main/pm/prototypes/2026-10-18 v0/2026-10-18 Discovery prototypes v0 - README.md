# 2026-10-18 Discovery prototypes v0 - README

Anton's working material, not evidence (`pm/AGENTS.md`). A copy of the prototype canvas, exported on
18 October 2026 and updated on 23 October 2026 (canvas version 22), so the prototypes open without a
claude.ai account or a link. The canvas stays the master:
[Optimum prototypes v0 - topics 1 and 2](https://claude.ai/artifact/R5mrsrgEuYm1ZznV7mqLnE).
Why and how discovery uses them: [[2026-10-13 Discovery plan - draft]]; the questions behind each
area: [[2026-10-13 Discovery question sheets - draft]]. The 23 October changes follow
[[2026-10-22 Prototypes against MUDPRO and API]].

## How to open

- Rig app: double-click `rig-app/Main.dc.html`. HQ web app: double-click `web-app/Web.dc.html`. Each
  opens in the default browser, needs no account and works without internet; offline, the font falls
  back to a system one.
- Tested on 18 October in Microsoft Edge, opened from the file with the network blocked: both apps
  render and click through. Chrome runs the same engine; Firefox and Safari are not tested. If a
  browser shows a blank page, open a terminal in the app's folder, run `python -m http.server`, and
  open http://localhost:8000/Main.dc.html (or Web.dc.html).
- Tested again on 23 October in the built-in browser of the Claude app (Chromium), from a local
  server: a mud check entered with the example values, saved as flagged, the day's checks with the
  calculated rows, and the HQ QC table with the same rows. No console errors.
- Rig app: it starts offline. Pick an engineer under "Signed in on this computer before", then Sign
  in. "Prototype: fill example values" fills a mud check; the sync status in the header brings the
  connection back.
- Web app: "Prototype only: sign in as" a role; "Prototype: view as" in the header switches role.

## What is in it

- Rig app: D1 sign-in and app frame; D2 jobs and mud checks - entry with hints, values outside the
  range flagged with a reason, impossible values blocked, the day's four checks, oilfield and metric
  units.
- Calculated values on the mud check, since 23 October:
  - plastic viscosity, yield point, retort solids and excess lime are worked out from the readings and
    cannot be typed
  - a panel with n and K by the client's power law (pipe from 600 and 300 RPM, annulus from 300 and 3
    RPM) and the solids analysis by their Equations 10-5 to 10-8, with a line naming the method
  - retort oil, funnel viscosity and the 60 and 30 RPM readings added, as in the client's daily report
- HQ web app: W1 sign-in and menus by role; W3 jobs and mud checks with QC, including the calculated
  values; W2 ranges and units. The other modules are empty frames, drawn after their own sessions.
- Fictional data only; the ranges are examples, not the client's. Not shown to the client: anything
  for the client goes through `procedures/export.md`.
- 564 KB for both. Each folder carries its own copy of the runtime (`support.js`, React in `vendor/`),
  as the canvas exports it.

## Questions for the client

From the canvas's sticky notes, as of 18 October. Each is a guess the prototype makes.

### Rig app

1. Each engineer signs in with their own account. Without a connection, only engineers who have
   signed in on this computer before can sign in.
2. At shift change the next engineer signs in and carries on the same day.
3. The reporting day runs 06:00 to 06:00: four mud checks, two per shift.
4. HQ opens the job and assigns the engineers; the engineer can also open one at the rig. Fields
   marked as set at HQ cannot be changed at the rig.
5. A mud check holds the properties of today's Daily Drilling Fluids Report. Volumes, pits, pumps,
   bit, solids control and comments are not drawn yet: are they entered here too?
6. Only measured depth and density are required.
7. A value outside the range is kept, flagged, and needs a reason. A value that is not possible (pH
   above 14, a lower speed reading higher than a faster one) cannot be saved.
8. Ranges are set per job at HQ.
9. A saved check is locked; a correction goes to HQ for approval.
10. Units: oilfield and metric. The third set is open.
11. Plastic viscosity, yield point, retort solids and excess lime are calculated from the readings,
    as API RP 13B-1 and your Equation 10-4 define them, and cannot be typed. Do your engineers type
    them today? A calculated value outside the range is flagged like any other.
12. Retort oil is entered next to retort water. Water and oil adding up to more than 100% cannot be
    saved.
13. Your daily report also lists 60 and 30 RPM readings and three user-defined properties (weight,
    funnel viscosity, filtrate). We added the two readings and funnel viscosity. Are these fixed
    fields, or a list each job can extend?
14. When a check is saved, the app also works out n and K by your power-law procedures (Figures 2-1
    and 2-3), and the solids analysis by your Equations 10-5 to 10-8. The hydraulics program in your
    samples uses Herschel-Bulkley, as API RP 13D does today. Which one governs?
15. Your daily report has one n and one k. Which pair: the pipe's (600 and 300 RPM) or the annulus's
    (300 and 3 RPM)?
16. ECD needs the well's geometry and the flow rate, so it is drawn after the session on
    calculations.

### HQ web app

1. Four roles: Engineer (rig app only), Supervisor, Manager, Admin. Are Supervisor and Manager one
   role or two? Where do project engineers and operations support fit?
2. A supervisor sees only the rigs assigned to them; a manager sees every rig.
3. Managers and admins approve corrections to saved mud checks.
4. Admins manage users, ranges, units and the audit log, and do not see operations.
5. Sign-in with email and password.
6. Modules not drawn yet are empty frames; each is drawn after its own session.
7. Engineers are assigned to each job here. Or does HQ send them to a rig, where they stay from well
   to well? Does the assignment decide who can sign in on the rig computer?
8. Which job details does HQ own: job number, operator, contractor, rig, well, location, spud date?
   Are order details or quality requirements needed too?
9. Who opens and edits jobs at HQ: supervisors, managers, or both? Who closes a job? Can a job ever
   be deleted?
10. If HQ and the rig change the same job, or both open the same well, before the rig syncs, which
    one stands?
11. Mud checks reach HQ only when the rig syncs, so each rig shows when it last synced. Should
    someone be told when a rig has not synced for a day?
12. QC here is read only: the supervisor sees every check, the flagged values and the engineers'
    reasons. Does QC need an outcome, such as reviewed or correction requested?
13. How is a supervisor's list of rigs decided, and where does the list of rigs come from?
14. Ranges are set per job here, with a default for properties a job has none for. Or are they
    global, per mud system, or from the customer's specification? Who sets them: IT admins or
    supervisors?
15. A changed range reaches the rig at its next sync, and checks already saved keep their flag. Is
    that right?
16. Each property has two limits: outside the range a value is saved as flagged, with a reason;
    outside the possible values it cannot be saved. Are these your two alert types? Who sets the
    possible values?
17. Which three unit sets? Your samples give density in ppg, lb/ft³ and g/cm³.
18. One default unit set, and each user may switch to another. Or are units fixed per job, or for
    the whole company?

Calculated values:

19. HQ sees the calculated values with each check, as the rig worked them out when the check was
    saved. HQ does not recalculate them.
20. Ranges can be set on plastic viscosity, yield point, retort solids and excess lime, as on measured
    values.

## Updating this copy

When the canvas changes: open it, play "Rig app - sign-in (D1)", click the export icon at the top
right and choose HTML (.zip); then the same for "HQ web app - sign-in (W1)". Unzip each over its
folder here (`rig-app`, `web-app`), leave out the zip's own README.md, and bring the questions above
in line with the sticky notes. These two exports are the whole prototype: the other frames on the
canvas are the same two apps opened at another screen.

The export differs from the canvas files only by two lines after the title, which load React from
`vendor/` (checked on 23 October). So copying the canvas's `project/Main.dc.html` and
`project/Web.dc.html` here and adding those two lines gives the same result; the 23 October update was
made that way.
