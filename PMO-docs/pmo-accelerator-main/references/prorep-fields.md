---
source: live PROREP Epic read via the Atlassian MCP, fields=*all with expand=names (519 field entries on the issue)
observed: 2026-09-03
card profiled: a real project-level Epic in project PROREP (id 10104), issue type Epic (id 10000)
---
# PROREP card - the field map

What is actually on a PROREP card, by field ID, and where each value comes from. Everything marked
OBSERVED came back from a tool call on a live card. Everything marked INFERENCE is a guess and is
labelled as one.

Read this before proposing content for a card. Do NOT guess at custom field names - the card carries
519 fields, many are near-duplicates of each other, and several English fields sit unused beside a
filled Russian equivalent. Field labels on screen are frequently Russian; they are transliterated
here because workspace files stay ASCII.

## Three different things get called "metrics" and they are not the same

This is the distinction that matters most, and getting it wrong means writing to the wrong fields.

**Set A - the eight PMO indicators. The PM's, WEEKLY.** customfield_22759 to customfield_22766,
single-select dropdowns holding GREEN / YELLOW / RED (and a stage value on the last). Set through
transition id 2, "Update PMO Metrics". This is what the `prorep-card` skill's update mode owns, and
the option sets and IDs live in that skill rather than here.

| Field | ID |
|---|---|
| Indicator_Contract_Quality | customfield_22759 |
| Indicator_Handover_Status | customfield_22760 |
| Indicator_Actual_Budget | customfield_22761 |
| Indicator_Budget_Handover_Baseline | customfield_22762 |
| Indicator_Staffing_Status | customfield_22763 |
| Indicator_Delivery_Health_Current | customfield_22764 |
| Indicator_Upsell_Opportunities | customfield_22765 |
| Indicator_Project_Stage | customfield_22766 |

OBSERVED: all eight present and filled on the profiled card. The display names above are the real
ones from the `names` map, not invented.

**Set B - the lozenge fields. The PM's historically, effectively ABANDONED.** Four rich-text fields
holding coloured status lozenges for named sub-measures, plus a date field:

| Field | ID | Sub-measures observed |
|---|---|---|
| Legal and finance | customfield_12006 | margin, revenue, location |
| Focus on Client | customfield_12007 | alignement with client, csat |
| Committed to Delivery | customfield_12008 | productivity, quality, schedule, scope, tech exellence |
| Team Dynamics | customfield_12009 | team retention, staffing, team performance |
| Metrics update | customfield_12004 | a date, not a measure |

OBSERVED: filled on the profiled card, with `Metrics update` reading 2025-12-15 - nine months stale
while Set A was current. CONFIRMED BY THE PM 2026-09-03: this was a PM job that the eight indicators
superseded. It is not maintained and is not being revived.

So: do not write to Set B, do not propose reviving it, and do not report it as a gap. Do say it
exists if a PM asks why their card shows two sets of colours, because that question has a real
answer. The sub-measure spellings above are reproduced as they appear on the card, typos included -
they are data, not a style to copy.

**Set C - Health Check and audit. NOT the PM's.** customfield_10506, 11883, 11884, 10503, 10508,
12013, 11986, 11987 (health-check result, conclusions, content, dates, links), plus 14325 / 14326
PMO Rating, 19125 / 19126 / 19127 Compliance Rate / Project Size / Audit Type, and 22866 Audit
Matrix. OBSERVED: every one of these empty on the profiled card. Owned elsewhere - do not fill and
do not count as gaps.

**Which UI tab is which.** No field on the card is named "METRICS" or "PMO Operational Metrics".
Both are screen-tab labels, and no tool in the Atlassian MCP set exposes which fields sit under
which tab - `getJiraIssue` returns no grouping, and createmeta on PROREP/Epic returns no tab
structure. So which label sits over Set A and which over Set B is UNRESOLVED. Settling it needs
somebody to open a card in a browser and read the two tab headings against the fields beneath them.
Do not assert a mapping.

## Descriptive fields - filled in practice, and A11 is where they get filled

OBSERVED on the profiled card: the descriptive panel is genuinely maintained, not blank. These are
A11's job. `prorep-card` does not touch them - it owns the weekly status and Set A only.

| Field | ID | Source of the value |
|---|---|---|
| Nazvanie proekta (project name) | customfield_10478 | the project |
| Company Name | customfield_12701 | A01 client profile |
| Nachalo proekta (start) | customfield_10297 | A07 roadmap |
| Konets proekta (end) | customfield_10298 | A07 roadmap |
| Strana (country) | customfield_10087 | A01 client profile |
| Model sotrudnichestva (cooperation model) | customfield_10094 | A01 contract type, confirmed at A03 |
| Budget constraint | customfield_11860 | the contract - Yes/No, NOT an amount |
| Technologies | customfield_10096 | A05 and the architecture notes |
| Status proekta (project status) | customfield_10300 | the PM |
| Project stage | customfield_12173 | the PM. NOTE: distinct from Indicator_Project_Stage (22766) and they can disagree |
| Opisanie proekta (project description) | customfield_10204 | A04 |
| Opisanie Klienta (client description) | customfield_11872 | A01 client profile |
| Project Industry | customfield_10413 | A01 |
| Domain | customfield_10183 | A01 |
| Solution | customfield_10414 | A05 |
| Type of service | customfield_10415 | A01 / contract |
| Project portfolio | customfield_12097 | PM profile |
| Project Team Type | customfield_12014 | A10 |
| Project from Presale | customfield_12044 | A01 |
| Initial budget (billable hours) | customfield_12340 | A07/A08 plan - HOURS |
| Total budget (billable hours) | customfield_12341 | A07/A08 plan - HOURS |

**Two budget traps.** `Budget constraint` (11860) is a Yes/No flag, not a figure. `Budget`
(customfield_10543) was OBSERVED empty and is the one field here that could take a money amount -
leave it alone. The billable-hours fields are HOURS and are safe.

**The two project-stage fields.** customfield_12173 `Project stage` and customfield_22766
`Indicator_Project_Stage` are different fields with different option sets, and on the profiled card
they held different values ("Client acceptance" against "UAT (Team)"). Neither is wrong on its face;
just do not treat one as a read of the other, and if a PM asks which leadership sees, say the
indicator is the one the weekly transition drives.

## Links and roles - filled, and worth reading rather than asking the PM

OBSERVED filled: customfield_12100 Chat link, 12101 Accounting Chat link, 12305 Strategy Chat Link,
12142 Webhook Google Chat, 12172 Link to Timesheet, 13163 Project Report link, 11875 SF Project
Link, and **customfield_22865 Knowledge Container - the project's NotebookLM URL**.

That last one matters beyond this file: the card is where a project's brain link is recorded, so a
project whose brain nobody can find has a good chance of having it here. Check the card before
telling a PM their brain is missing, and record what you find in `project-context.md`.

Roles: customfield_10335 PM, 10108 RM, 11878 Delivery Manager, 11859 Account Manager, 12339
Technical Lead, 23368 Solution Architect, 10091 Department, 10130 Stakeholders. Read these for the
A02 stakeholder register rather than interviewing the PM about who is on their own project.

## The presale narrative block

OBSERVED filled: customfield_11971 through 11985, a numbered Russian narrative series beginning
`Informatsiya ot seylza` (information from the sales manager) and running `1. Sut proekta` (the
essence of the project) through `10. Dopolnitelnaya informatsiya`.

This is handover material sitting on the card. A01 should read it before asking Sales for anything,
because some of what a handover checklist marks as missing may already be here. INFERENCE, flagged:
the series looks like a structured presale questionnaire, but its exact question set was not read
field by field, so confirm against a card rather than assuming the ten headings.

## Fields that stay empty, and are not gaps

OBSERVED empty on a well-maintained card, so treat their emptiness as normal rather than as a
finding: customfield_17481 Short Description, 17482 Business Value, 11870 Alternative project name,
10543 Budget, 11897 / 11898 Project overview key / status, 14324 Current status, 14551 / 14552
Estimation Gap / Delivery Gap, 14318 / 14319 Miscalculated budget / Upsale, 11828 / 10424 / 14450 /
14451 the billable and worked hours block, 23601 PMO Delivery Supervisor, plus all of Set C.

Several of these are English duplicates of a Russian field that IS filled. Before filling an
empty-looking field, check whether its counterpart already carries the value - two half-filled
descriptions of one project is the outcome to avoid.

## Two card shapes in project PROREP

OBSERVED: the project holds project-level Epics named for the project ("Philmore Productions",
"Tensi+") and ALSO monthly cards named `<Project> - <PM name> - <Month>, <Year>`.

CONFIRMED BY THE PM 2026-09-03: the weekly status and the eight indicators belong to the
project-level card only. The monthly cards are a separate mechanism. Filter to the project-level
card by name shape, and never post a weekly status to a monthly card - a status on the wrong card
shape is visible to leadership and hard to unpick.

The child issue types hanging off the Epic - `Report`, `Health check` (+ subtask), `Milestone`,
`Action Item`, `Employee`, `Out of office` - are separate work again. The health metrics and the
Weekly Project Report are different issue types, not two names for one thing.
