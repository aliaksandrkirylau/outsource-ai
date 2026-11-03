# OE prototype - UI kit and clickable prototype (desktop and web)

Working material in pm/ (Mikhail): not evidence and not agreed with the client. Built 14-15 Oct 2026, shared here 17 Oct 2026, exported to open in a browser 20 Oct 2026.
Supports [[DEC-010 Confirm the product with the client through prototypes in code]].
Not the same as Anton's [[2026-10-18 Discovery prototypes v0 - README]] (a separate canvas for discovery topics 1 and 2). The two overlap on sign-in, wells/jobs, mud checks and ranges. Agree with Anton which one to take to the client, or how to merge them, before either is shown.

## What it is
- A clickable prototype of both apps, built in Claude Design (Flutter Material 3 look, standard widgets only):
  - Desktop app at the rig (engineer): 23 screens covering sign-in, wells, mud checks, inventory, calculations, reports, dashboard and settings.
  - Web app at HQ (supervisor / manager, admin): 15 screens covering dashboard, approvals, wells, reports, inventory, users, rigs, thresholds, products and audit log.
- MVP lines of WBS v1 ("Development Flutter", Stage = TRUE) only.
- Colours come from oes.com.sa and its product data sheets.
- One invented data set: rigs 07, 12 and 21, well DW-217, mock time 14 Oct 2026. People, prices and costs are invented, not real figures.
- Calculations (rheology, hydraulics, solids, weight-up) use the client's formula sheets and run live, but are not verified against worked examples.

## How to open it
- **Clickable version:** Claude Design artifact "OE Prototype - desktop and web" (owner Mikhail; ask him to share it). It opens on the desktop demo page.
  - Pages "Step 0" to "Step 7" hold the desktop screens; "Web W0" to "W3" hold the web screens.
  - Each screen runs with Play.
- **UI kit:** `UI Kit v0.2.html` opens in any browser.
- **In a browser, without Claude Design:**
  - On Windows, double-click `source/start-prototype.cmd`. It starts a small local web server (needs Python: `py` or `python`) and opens the desktop demo page. Close the server window to stop.
  - On a Mac, run `python3 -m http.server 8000` in the `source` folder, then open http://localhost:8000/Demo.dc.html.
  - Entry pages:
    - `Demo.dc.html` (desktop demo script)
    - `WDemo.dc.html` (web demo script)
    - `SignIn.dc.html` (desktop app)
    - `WSignIn.dc.html` (web app)
    - `Main.dc.html` (UI kit)
  - A local server is needed because the screens load the shared top bar and menu from separate files, and browsers block that for pages opened straight from disk. Double-clicking a `.dc.html` file shows the screen without its top bar and menu.
  - The icons come from Google Fonts. Without internet they show as words (e.g. "dashboard").
  - Tested on 20 Oct 2026 in Chromium through a local server: all 41 files render without errors, approvals and menu links click through.
- **Runtime:** `source/support.js` and `source/vendor/` are the Claude Design runtime, the same files as in [[2026-10-18 Discovery prototypes v0 - README]]. `canvas.json` is the canvas layout, used only in Claude Design.
- **Calculation engine:** `calc/engine.js`. Run `node calc/test.js` for the test values.

## Files
| File | What |
|---|---|
| [[OE prototype - desktop plan]] | Plan, rules, theme, decisions and build log for the desktop prototype |
| [[OE prototype - web plan]] | The same for the web prototype |
| [[OE prototype - issues, inconsistencies and client questions]] | Source conflicts, fixed and remaining data issues, risks, and 37 questions for the client |
| [[OE prototype - desktop demo script]] | Printable script for the desktop demo. The web demo script is the page "Web demo walkthrough" in Claude Design. |
| [[OE prototype - calculation notes]] | Formulas, our assumptions and test values |
| `UI Kit v0.2.html` | Palette, typography, components and status colours |
| `source/` | 41 screen and component files, the canvas, the runtime and `start-prototype.cmd` |

## Before showing it to the client
- Fix or explain P-04 and P-05 in the issues note.
- Whatever the prototype shows may be read as in scope. Each area needs a written OK; a demo is not acceptance.
- Client questions that block a WBS line should become QUE notes through the usual ingest. None have been created from this list yet.
