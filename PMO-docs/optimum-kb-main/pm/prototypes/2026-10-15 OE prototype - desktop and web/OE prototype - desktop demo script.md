# Demo script - an engineer's shift, end to end

Internal. About 20 minutes. Ali Hassan, day shift on OES Rig 07, well DW-217. In Claude Design: page "Demo walkthrough", press Play, Start the demo.

**Say at the start:** clickable prototype to agree what the app does, screen by screen. Data is invented. Calculations use the client's formula sheets but are not verified; ask for worked examples.

**How we agree:** note every comment; send a written summary and open questions after the demo; each area is agreed by a written OK by email from the named contact. A nod in the call is not acceptance.

**Keep in mind:** what the prototype shows may be read as in scope. Do not promise items marked "not yet"; log them as questions or change requests. Desktop only; the HQ web app comes next.

## 1. Sign in on the rig computer (1 min)

Screens: 1.1 Pick user, 1.3 Wrong password

- **Do:** Pick Ali Hassan, type the password, Sign in. Show the wrong-password state.
- **Say:** One shared computer per rig, each engineer has his own account. Works offline; HQ adds people and resets passwords.
- **Ask:**
  - Is a personal account per engineer right, or is a Windows login enough?
  - Who adds engineers and resets passwords at HQ?

## 2. The dashboard (2 min)

Screens: 6.1 Dashboard

- **Do:** Walk the tiles, the "needs attention" list, then switch product use between section and whole well.
- **Say:** Everything here comes from what the engineer entered: checks, stock, calculations. Each item opens its screen.
- **Ask:**
  - Which of your five KPIs does the engineer need on the rig, and which only HQ?
  - Where do targets come from: mud program, planned depth by day?
- **Not yet:** offset-well comparison, volume and loss trend, calibration alerts.

## 3. The well (2 min)

Screens: 1.6 View / edit well, 1.5 New well, 1.4 No well yet

- **Do:** Open the well switcher in the top bar, the pencil on DW-217; then New well.
- **Say:** A rig drills one well after another on the same computer. The engineer can open a new well offline; HQ can too.
- **Ask:**
  - Who usually opens a new well, HQ or the engineer? Which fields come from HQ?
  - Are engineers assigned to a rig for a period, or to each well?
  - What are "order details" and "quality requirements" on a well?

## 4. A mud check with an out-of-range value (3 min)

Screens: 2.1 Mud checks, 2.2 New mud check

- **Do:** New mud check. PV 41 is red; type 19 in pH to show it is blocked, set it back; Save, give the reason, Save as flagged.
- **Say:** Ranges show under each field. Out of range needs a reason and is flagged for HQ; impossible values cannot be saved. Solids and n, K are calculated as you type.
- **Ask:**
  - Is this the right parameter list? Does it change with water- or oil-based mud?
  - Are ranges set per customer or per well? Which alerts block and which only flag?
- **Not yet:** volumes and pits, pumps, bit, solids control entry.

## 5. Correcting a saved check (1 min)

Screens: 2.3 Mud check

- **Do:** Edit, change PV 41 to 34, Send for approval.
- **Say:** Saved checks change only with a reason and HQ approval; until then reports keep the original.
- **Ask:**
  - Can an engineer fix his own check in the same shift without approval?
  - Who approves: operations manager, admin, supervisor?

## 6. Inventory for the day (2 min)

Screens: 3.1 Inventory, 3.2 Today’s use, 3.3 Movement

- **Do:** Show the alerts, Record today’s use (type 1000 for OES-BAR), then a Received movement with an expiry date.
- **Say:** Same columns as your daily report. Products, unit sizes and minimum levels come from HQ.
- **Ask:**
  - Is stock kept per well, or does it carry over to the next well on the rig?
  - Is concentration typed in or calculated? Where are expiry dates entered?

## 7. Calculator (2 min)

Screens: 4.1 Calculator

- **Do:** Weight up from 10.4 to 11.0 ppg; change the target and watch the result.
- **Say:** Uses the formula on your OES-BAR data sheet. Live, but to be checked against your examples.
- **Ask:**
  - Which calculations do engineers use daily besides weight up and oil/water ratio?
  - Can you send worked examples with expected results?

## 8. Hydraulics simulation (3 min)

Screens: 4.2 Hydraulics

- **Do:** Results tab: pick flow rates; then Drilling fluid tab, set density to 12.6 and go back to Results.
- **Say:** Your Figures 2-1 to 2-5, power law. Pressures, ECD against pore and fracture, hole cleaning, surge and swab.
- **Ask:**
  - Power law, or Herschel-Bulkley like your current program?
  - Figure 2-2 seems to miss a factor 100: can you confirm? Can you send Figure 3-1?
  - Which outputs are needed for the first release?

## 9. End-of-day report (2 min)

Screens: 5.1 Reports, 5.2 End of day

- **Do:** Open 13 Oct, untick a block, Export PDF.
- **Say:** Built from the day’s data in your report’s order; PDF, Excel, CSV; sent by email as today.
- **Ask:**
  - Is this your full daily report, or a subset? Which blocks are must-have?
  - Does each operator need its own template or logo?
- **Not yet:** volumes, pumps, bit, solids control, costs in the daily report.

## 10. Section report and approval (1 min)

Screens: 5.3 Section, well, inventory

- **Do:** Submit the 12¼ in section for approval; show the approved 17½ in section; switch to inventory.
- **Say:** Only section and well reports need sign-off, as you told us. Approved means locked.
- **Ask:**
  - What must a section and a well report contain? Can you share one of each?
  - Who signs them off?

## 11. Settings and sync (1 min)

Screens: 7.1 Settings

- **Do:** Switch units API, SI, Mixed; then Sync now.
- **Say:** Units change everywhere, ranges too. Nothing is lost offline; sync sends the queue and brings back approvals.
- **Ask:**
  - Which unit sets do you use, and is it per computer, per user or company-wide?
  - If HQ and the rig change the same thing offline, which one wins?

## After the demo

Send within a day: what was shown, comments per screen, answers given, open questions with an owner each, and what we ask them to send (parameter list per mud system, worked calculation examples, 2-3 real daily reports, one section and one well report, unit sets in use). Ask for a written OK per area once the comments are in.
