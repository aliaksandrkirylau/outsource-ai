# S06 Reports and approval

Session plan, topic 6, week 4. One hour. Part of [[00 discovery-BA-plan]]. Working material, not evidence.

## Elicitation goal

What each report is (the daily report first), which blocks are typed and which computed, and how HQ
approves and locks section and well reports.

## Scope

- D5 desktop reports: WBS:Development Flutter!68 (End-of-Day), !69 (End-of-Section), !70 (End-of-Well),
  !71 (inventory)
- W5 web reports: WBS:Development Flutter!33 (approval and lock), !34 to !37 (generation)
- [[REQ-010 Reports]], [[CAP-008 Reports and report approval]], [[TRM-001 Report]] (disputed)

## Participants

Client: a mud engineer, a field supervisor, Mr. Lawal. Ours: Anton, Leu.

## Preparation and inputs

- 2-3 real End-of-Day reports, one End-of-Section, one End-of-Well, one inventory report, anonymised;
  any operator templates.
- S02 and S04 agreed, since the reports are built from checks and products.
- Prototype: End-of-Day built from the day's checks, products and volumes in the order of their
  Daily.xlsx, with a PDF preview and export; section and well as summary tables with simple trends;
  the web report list with status (generated, approved, locked); Approve or Lock on section and well
  reports only. No e-mail button.

## Agenda

| Min | Item | Fails without |
|---|---|---|
| 0-5 | Recap, goal | - |
| 5-25 | The daily report: reference form, blocks, one per day or shift | A1, A2, A3 |
| 25-35 | Section and well reports | B1 |
| 35-48 | Approval and lock | C1, C2 |
| 48-55 | Click through the preview and the web list | Corrections noted |
| 55-60 | Next steps | - |

## Questions register

Grouped by topic in agenda order; must-haves first. Blocks: the WBS line the answer is needed for, as its row in the WBS tab "Development Flutter" and a short name. When: Call, or Written after the session.

| ID | Question | Blocks | Must | When | Ahead | Source |
|---|---|---|---|---|---|---|
| | **A. The daily report** | | | | | |
| A1 | Which daily report form is the reference: your Daily.xlsx, an operator's form, or the API form? Is Daily.xlsx your own template? | 68 End-of-Day report (desktop) | Yes | Call | Yes | Sheet D5 B4 |
| A2 | Should the daily report have all the blocks of your current one, or a subset? Which are typed and which calculated? | 68 End-of-Day report (desktop) | Yes | Call | Yes | Sheet D5 B1; [[REQ-010 Reports\|REQ-010]] |
| A3 | One report per day from both shifts, or one per shift? Who produces it? | - | Yes | Call | - | Agent, near Sheet D1 B3; [[TRM-001 Report\|TRM-001]] |
| A4 | Does each operator need its own template or logo? | - | - | Call | - | Sheet D5 B3 |
| A5 | How long may producing a report take before it feels too slow? | - | - | Written | - | Client Q&A A.1 (NFR); [[CON-005 Easy and responsive interface\|CON-005]] |
| A6 | You asked for "complete and accurate reports". What makes a daily report incomplete or wrong today? An example helps. | - | - | Written | - | Client Q&A A.1; moved from S00 |
| | **B. Section, well and inventory reports** | | | | | |
| B1 | What goes into the End-of-Section and End-of-Well reports? | 69 End-of-Section report (desktop); 70 End-of-Well report (desktop) | Yes | Call | Yes | Sheet D5 B2 |
| B2 | Should the inventory report show quantity, use trend and cost per rig? Who may see costs? | - | - | Written | - | Agent |
| | **C. Approval and lock** | | | | | |
| C1 | Who approves reports, in one step or two? What does "lock" freeze? Can a report be sent back, and what happens if a correction comes later? | 33 Report approval (web) | Yes | Call | Yes | Sheet W5 B1 |
| C2 | Does the web produce reports from synced data, or show what the rig produced? Which version counts? | 34-37 Report generation (web) | Yes | Call | - | Sheet W5 B2 |
| C3 | Is data locked once the daily report is out? Are versions, filters and report numbers needed? | - | - | Written | Yes | Sheet D5 L |
| C4 | Do your ISO 9001 procedures say how reports are kept or signed? | - | - | Written | - | Sheet D5 L; [[CON-008 Compliance with ISO 9001, ISO 14001 and API standards\|CON-008]] |
| | **D. Out of scope** | | | | | |
| D1 | Are fleet-wide or analytics reports, or signatures on the PDF, needed? | - | - | Written | - | Sheet W5 L |
| D2 | Is a separate engineering calculation report needed? | - | - | Written | - | Sheet D5 L; [[REQ-017 Report on a single calculation or simulation\|REQ-017]] |

Materials to request: 2-3 real End-of-Day reports, one End-of-Section, one End-of-Well, one inventory report, any operator templates, OES branding, how section and well reports are signed today, recipients by role (Sheet D5, W5).

## Confirm with the client

| Ours | Plain wording |
|---|---|
| [[TRM-001 Report]] Version B | One daily report per well per day, built from the day's mud checks and products. |
| [[REQ-010 Reports]] | The reports as the blocks agreed here, exported as PDF, CSV and Excel; a supervisor or manager approves or locks section and well reports on the web. |

## Outputs

- KB: [[TRM-001 Report]] settled or narrowed with the subject expert; [[REQ-010 Reports]] updated with
  the report contents and the approval rules.
- The report contents written into the V&S.
