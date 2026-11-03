---
type: requirement
id: REQ-010
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-10-29 Client sample daily report - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2026-11-02 Client sample daily mud reports - rendering]]"
  - "[[2026-11-02 Client sample end-of-well recap - rendering]]"
scope_status: contracted
baseline:
  - "WBS:Development Flutter!32-37"
  - "WBS:Development Flutter!67-71"
capabilities:
  - "[[CAP-008 Reports and report approval]]"
tags:
  - reports
---
# REQ-010 Reports

## Need

Engineers produce the reports the client runs on: the day's report, the report at the end of a well
section, the end-of-well report and the inventory report; HQ views them and signs off the section and
well reports. Why: "Must generate complete and accurate reports" is the client's first outcome
([[2025-10-29 Client answers to the Q&A register - rendering]] A.1).

Report types, as the client confirmed them: "End-of-Day, End-of-Well, Engineering
calculation/simulation, and Inventory reports" - "Yes, including end-of-section reports" (Part 1, 3).
The BA draft and the v1 WBS ([[2026-09-25 v1 WBS - rendering]]) have four: End-of-Day, End-of-Section, End-of-Well (which summarises "all
data, inventory, and simulation results"), Inventory ([[2025-10-28 BA draft WBS - rendering]] rows
38-41). Whether the client expects a separate engineering calculation/simulation report is
[[QUE-004 Is a separate engineering calculation report expected]].

Scope: contracted. v1 WBS Development Flutter rows 67-71 (desktop reporting) and 32-37 (web reporting,
including the approval flow in row 33), all estimated.

## Acceptance criteria

To be written by the BA.

## Edge cases

| Scenario | Expected behaviour |
|---|---|
| A report is generated on an offline rig before the day's data is synced | Not defined in these sources |

## Business rules

- Export: "with the opportunity to export them in pdf, csv and xls formats"
  ([[2025-10-22 First call with OES - notes]] key point 5); "filterable and exportable to the PDF and
  CSV/Excel formats" (BA draft rows 38-41).
- Approval: "No. Sign-off or approval only required for end-of-section or end-of-well reports" (D.14);
  the approver approves or locks them (BA draft row 28).
- "Data masking/redaction feature not required. However, filtering of data for specific reports should
  be possible." (D.17)
- The client's current daily report is the visual reference: "Envisioned product is expected to be
  better designed, intuitive and detailed" (F.29;
  [[2025-10-29 Client sample daily report - rendering]]).
- Who receives reports: "Client personnel, field supervisors and management" (C.10).

From the first call's transcript (added 2026-09-28, batch 2):

- Format: "the tool will be able to generate PDF based reports that is like the standard ... And then
  this PDF based report, you know, can be, can now be sent by email to authorized or relevant
  recipients"; CSV or Excel too, "because you want to be able to use them for further analysis outside
  of the system or only select. Only present some specific aspect of data to a particular interested
  individual" ([[2025-10-22 First call with OES - transcript]] 0:29:42).
- Selective reports: "you will be able to selectively generate certain types of report, you know, other
  than the complete standard report" (0:37:48). A report of a single calculation or simulation is
  [[REQ-017 Report on a single calculation or simulation]].
- Who generates the daily report: the day's second engineer, at the end of his shift, "will generate
  the report and share that report with the customer and the office using the same computer" (1:06:48).
  What a report is made of is disputed: [[TRM-001 Report]].
- Open: whether the client's customers get access to the software to see their reports. The client:
  "I'm kind of ambivalent about that at the moment because the danger of while that is a good feature to
  have the risk that comes with that is that if you have not QCed the data prior to your customer having
  access can open you up to issues ... So at this time I will suspend my full comment on that." (0:29:42)

From the client's sample reports of 2 November 2026 (added 2026-11-02):

- The daily mud report, on two forms: "Daily Drilling Fluids Report" ([[2026-11-02 Client sample daily mud reports - DMR Sample 1.pdf|DMR Sample 1]], the 2025 form
  filled in) and "Daily Mud Report No. 11" ([[2026-11-02 Client sample daily mud reports - DMR Sample 2.pdf|DMR Sample 2]])
  ([[2026-11-02 Client sample daily mud reports - rendering]]). Both hold the header, drilling
  assembly and casing, volumes, pumps and circulation, two or three mud samples against a spec
  range, solids analysis, rheology and hydraulics, solids control equipment, time distribution,
  products used, stock and costs; [[2026-11-02 Client sample daily mud reports - DMR Sample 2.pdf|DMR Sample 2]] adds pit volumes and a "Rig Tanks Status" page.
- The end-of-well report, "End Of Well Recap"
  ([[2026-11-02 Client sample end-of-well recap - rendering]]): an executive summary by casing
  interval, the well's cost summary and total product and engineering consumption (pp [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=2|2-4]]), then per
  hole section a "Section Fluids" sheet, costs, concentrations, "Property Tracking" against plan,
  and a "Time, Volume & Cost Summary" with charts (pp [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=5|5-32]]).
- No end-of-section and no inventory report came with them. The end-of-well report is built from
  per-section sheet sets, each closing on a daily report number ("DMR 8", "DMR 14"), so the
  end-of-section report may be that set for one section (evaluated; to confirm with the client).
- They are samples, not the required layout (`sources/client/AGENTS.md`).

## Out of scope

- Sending reports from the app. Today the engineer will "email reports to the supervisors" (D.13),
  but "Reports sending to Client is out of the solution scope. Users can generate reports, but their
  sending is made via other solutions" (v1 WBS, Assumptions & Risks 18). The SOW v10.4 says the same.
