# S02 Well job, mud checks and QC

Session plan, topic 2, week 2. One hour. Part of [[00 discovery-BA-plan]]. Working material, not evidence. The heaviest topic: in the hour only the
must-haves; the parameter detail goes in writing on the client's own list.

## Elicitation goal

What a well job is and who opens it; whether people are assigned to rigs or wells; what a mud check
holds; when a value is flagged and against what range; units; what QC at HQ does.

## Scope

- D2 desktop job and measurements: WBS:Development Flutter!50 to !54 (alerts built in M4)
- W3 web jobs and QC: WBS:Development Flutter!26 to !29
- W2 thresholds and units: WBS:Development Flutter!20, !22
- [[REQ-020 Create and manage well jobs and assign engineers]], [[QUE-012 Are engineers assigned to rigs or to wells]],
  [[REQ-005 Parameter thresholds and entry alerts]], [[REQ-018 Units of measure and conversion]],
  [[TRM-007 Threshold]], [[TRM-008 Mud check]]

## Participants

Client: a mud engineer (essential), a field supervisor, Mr. Lawal, Ms. Zahra. Ours: Anton, Leu.

## Preparation and inputs

- **The parameter list per mud system**, with units and ranges, and 2-3 filled daily reports
  (anonymised). Without them, keep the hour to the flow and send the list as a question.
- Prototype: the job screens on both apps (job header as their daily report has it); the mud-check
  form with flagged values and a reason; the QC view; ranges and units. Assignment drawn per job, as
  estimated; no rig list.
- [[2026-10-22 API standards research]] and [[2026-10-22 Prototypes against MUDPRO and API]] reread.

## Agenda

| Min | Item | Fails without |
|---|---|---|
| 0-5 | Recap, goal | - |
| 5-17 | A rig moving to a new well: who opens the job; rig or well assignment | A1, A2 |
| 17-35 | What a mud check holds; ranges and alerts | B1, B2, C1, C2 |
| 35-45 | QC at HQ | D1 |
| 45-55 | Click through job, mud check, QC | Corrections noted |
| 55-60 | Next steps: the full parameter list in writing, with a date | - |

## Questions register

Grouped by topic in agenda order; must-haves first. Blocks: the WBS line the answer is needed for, as its row in the WBS tab "Development Flutter" and a short name. When: Call, or Written after the session.

| ID | Question | Blocks | Must | When | Ahead | Source |
|---|---|---|---|---|---|---|
| | **A. Well job and assignment** | | | | | |
| A1 | When a rig moves to a new well, who opens the job, HQ or the engineer? Which details come from HQ and which are typed at the rig? | 50 Project setup (desktop); 26 Manage projects (web) | Yes | Call | Yes | Sheet D2 B1, W3 B2; [[REQ-020 Create and manage well jobs and assign engineers\|REQ-020]] |
| A2 | Does the same crew stay on the rig from well to well? Do you assign people to a rig or to each well, and does that decide who can sign in on the rig computer? (Ask open: per well is estimated; per rig needs a rig list.) | 26 Manage projects (web); 29 Quality control (web); 50 Project setup (desktop) | Yes | Call | Yes | Sheet W3 B3; [[QUE-012 Are engineers assigned to rigs or to wells\|QUE-012]] |
| A3 | Where do rig names and numbers come from? | - | - | Call | - | Sheet W2 B3 |
| A4 | How does a well section start and end? Who closes a job? | - | - | Call | - | Sheet D2 L, W3 L; [[TRM-006 Well section\|TRM-006]] |
| A5 | If a job is changed at the rig and at HQ at the same time, whose change counts? | - | - | Written | - | Sheet D2 L; [[QUE-011 Who wins when a project is edited on the web and on an offline desktop\|QUE-011]] |
| A6 | How are a supervisor's rigs defined? What is the job lifecycle? Can jobs be deleted? Do you need trend charts of measurements? | - | - | Written | - | Sheet W3 L |
| | **B. The mud check** | | | | | |
| B1 | Which parameters does a mud check hold, with units, and which are mandatory? Does the list differ by mud system (e.g. which oil-based tests run on the rig)? | 51 Measurements input (desktop) | Yes | Call | Yes | Sheet D2 B2 |
| B2 | Besides mud checks, does the engineer enter volumes and pits, pumps, bit and BHA, solids control, treatments, comments? | 51 Measurements input (desktop) | Yes | Call | - | Sheet D2 B3 |
| B3 | Are the 60 and 30 RPM readings and the "User Defined Properties" fixed, or can each job add its own? | - | - | Call | - | Sheet D2 B2 |
| B4 | When does the reporting day start and end? | - | - | Call | - | Sheet D2 B4 |
| B5 | Do engineers type PV, YP, excess lime and retort solids, or are they calculated? (Also S05.) | - | - | Written | - | Sheet D2 B8 |
| B6 | Did engineers copy the previous day's values in the old tool? Should copied values count as measured? | - | - | Written | - | Sheet D2 L |
| B7 | What does "99.9% data integrity" mean for a mud check: nothing lost, nothing changed without a trace? | - | - | Written | - | Sheet X1; client Q&A A.1 (NFR); [[CON-001 Offline operation and sync between rigs and HQ\|CON-001]] |
| | **C. Ranges and alerts** | | | | | |
| C1 | Of your two alert types, does one block the entry and the other only flag it? | 52 Threshold alerts (desktop) | Yes | Call | Yes | Sheet D2 B5 |
| C2 | What is a range for you, and at what level: per well, customer, mud system, or global? Who sets it? | 20 Thresholds (web) | Yes | Call | Yes | Sheet D2 B6, W2 B2; [[REQ-005 Parameter thresholds and entry alerts\|REQ-005]] |
| C3 | Can an engineer correct his own check before the shift ends without approval? (Detail in S03.) | - | - | Call | - | Sheet D2 B7; [[REQ-006 Edit or backfill past entries with approval\|REQ-006]] |
| C4 | Should a supervisor be notified of a flagged value? | - | - | Written | - | Sheet D2 L |
| | **D. Quality control** | | | | | |
| D1 | Does reviewing data at HQ lead to an action (reviewed, sent back, correction requested), or is it view only? | 29 Quality control (web) | Yes | Call | Yes | Sheet W3 B1 |
| D2 | Apart from limits for mud properties (thresholds) and documents, does HQ send anything to the rig, such as instructions or corrections? | - | - | Call | - | Sheet W3 L; [[QUE-002 Do managers send anything back to the rigs\|QUE-002]]; moved from S00 |
| | **E. Units** | | | | | |
| E1 | Which three unit sets, and chosen per user, per job or per report? | 22 Units (web); 54 Units (desktop) | Yes (if not settled in S01) | Call | - | Sheet X4; [[REQ-018 Units of measure and conversion\|REQ-018]] |
| E2 | How many decimals per parameter? | - | - | Written | - | Sheet X4 |

Materials to request: a screen share of an engineer using the old software (Sheet X7; past-well import is out, [[REQ-015 Import of historical data]], do not promise it), the parameter list per mud system with units and typical ranges, a customer spec or mud program for one well, 2-3 filled daily reports, the Job# format, the list of mud types and systems, current thresholds, active rigs and wells (anonymised), the supervisor's daily QC routine (Sheet D2, W3).

## Confirm with the client

| Ours | Plain wording |
|---|---|
| [[TRM-005 Project (well job)]] | A job is one well at one rig, divided into sections. |
| [[REQ-020 Create and manage well jobs and assign engineers]] | HQ creates jobs and assigns engineers on the web; the engineer can open or update the job at the rig. |
| [[REQ-005 Parameter thresholds and entry alerts]] | A value outside its range is kept, flagged, and needs a reason; an impossible value cannot be saved. |
| The limits | A mud check holds up to 50 parameters; three unit sets. |

## Outputs

- KB: QUE-012 answered or narrowed; [[REQ-020 Create and manage well jobs and assign engineers]],
  [[REQ-005 Parameter thresholds and entry alerts]], [[REQ-018 Units of measure and conversion]],
  [[TRM-001 Report]], [[TRM-006 Well section]], [[TRM-007 Threshold]] updated.
- The full parameter list asked in writing, with a date.
- If the answer is rig assignment: the option to the PMs to price (rows 23, 26).
