---
source: Innowise PMO Confluence, "Starting Project Artifacts Checklist"
page: 5166432427
page_version: 16
page_last_modified: 2026-09-24
synced: 2026-09-24
---
# Starting Project Artifacts Checklist - the 23 mandatory starting artifacts

The standard describes what should be DONE and why. This page describes what should EXIST by the end of initiation. Treat the live page as final whenever you read it - it keeps moving (21 rows in July, 20 then 23 on 23-24 Sep 2026), so build against today's version and let the next sync catch the change. When in doubt, re-read the live page by ID.

This is the copilot's definition of done for initiation, and the scoring rubric for the state scanner and the takeover skill. Two sibling checklists exist and serve other phases: the In-Progress Project Artifacts Checklist (5402329256) for a running project, and the [DRAFT] Project Closure Artifacts Checklist (5414322413) for F and G.

**Refer to an artifact by its NAME, never by its row number.** The rows were renumbered twice in two months; a number in a skill or a note goes false without anyone noticing.

## The list

| # | Artifact / Output | Storage location | Produced mainly at | Copilot key |
|---|---|---|---|---|
| 1 | Project Knowledge Container (NotebookLM) | NotebookLM | A01, updated A11 | knowledge_container |
| 2 | Common & Sensitive Project Folder | Google Drive - PMO Private (General) and PMO Sensitive | A11 (needed from A01) | project_folders |
| 3 | Project Description | Confluence | A04, updated A11 | project_description |
| 4 | Stakeholder Register | Confluence | A02 | stakeholder_register |
| 5 | WBS / Critical Scope Baseline with Acceptance Criteria and Estimates | Confluence / Spreadsheet | A05 | wbs_critical_scope |
| 6 | Risk Register | Jira / Confluence | A06 | risk_register |
| 7 | Opportunity & Internal Risk Register | internal only, never client-facing; the checklist names no location | A06 | opportunity_register |
| 8 | Project Team Composition | Spreadsheet | A10 | team_composition |
| 9 | RACI Matrix (Team + Stakeholders) | the checklist names no location | A12 (from the Stakeholder Register and A02's internal RACI) | raci |
| 10 | Staffing Master | Staffing Folder | A10 | staffing_master |
| 11 | Resource Plan | Spreadsheet | A07, updated A10 | resource_plan |
| 12 | Project Economy (P&L) | Sensitive Folder | A08, updated A10 | pl |
| 13 | EVM Baseline - Fixed-Price projects only | with the project economy | A08 | evm_baseline |
| 14 | Roadmap / Timeline / Project Schedule | Confluence / MS Project | A07 | roadmap |
| 15 | Project Chats with pinned sources per the chat's purpose | Google Chat | A02, verified A11 | chats |
| 16 | Baseline Validation (Expectations Matrix) - the client-facing half of A09 | Mail / Google Chat | A09 | baseline_validation |
| 17 | Project (Start) Approval - the internal half of A09, including the value classification | Mail / Google Chat | A09 | start_approval |
| 18 | Communication Plan | Confluence | A11 draft, A12 updated, A14 final | communication_plan |
| 19 | Project Card / PROREP | PROREP (Jira) | A11 | prorep |
| 20 | Progress Tracking System / Board configured | Jira / Other | A11 | tracker |
| 21 | Project Documentation Space | Confluence / Drive / Other | A11 | docs_space |
| 22 | Project Onboarding / Team Working Rules | Confluence | A11 | onboarding_rules |
| 23 | Kick-off Slide Deck | Google Slides | A13 | kickoff_deck |

What moved from the 21-row version: the two folders became one row, Critical Scope and WBS became one row, the baseline approval split into Baseline Validation and Project (Start) Approval, and three rows are new - the Opportunity & Internal Risk Register, the RACI Matrix (Team + Stakeholders) and the EVM Baseline.

Templates: the live page marks the Opportunity & Internal Risk Register, the RACI Matrix, the EVM Baseline and the Project (Start) Approval as TBD - no instruction, no template, no wiki yet. Several other rows carry a partial gap in the page's own comment column (WBS / Critical Scope and the Roadmap are "full documentation gap"). Where there is no template, the copilot drafts to the step's verification criteria and says plainly that it is our draft, not the house template.

## Per-step mandatory outputs NOT on the list

The checklist is the artifact inventory. Several steps carry mandatory outputs that are not separate filed artifacts. Do not treat their absence from the list as permission to skip them.

- A01: Collected Pre-sale Handover Package; Initial Project / Opportunity Context Summary with Client Problem Statement; Initial Assumptions and Commitments List.
- A02: Internal RACI Matrix (Sales / DM / Competency Center) - internal only, never client-facing, shared in the accounting chat. It feeds the RACI Matrix (Team + Stakeholders) at A12.
- A03: Contract Version Comparison Result; Contract Discrepancy / Clarification Items.
- A05: Required Project Roles List.
- A07: Critical Path documentation - Fixed-Price projects over 3,500h only.
- A08: Documented Economy Assumptions / Concerns.
- A09: Internal Stakeholder Validation Outcome; Client Baseline Validation Outcome.
- A12: Team Feasibility Confirmation / Concerns.
- A13: Kick-off Agenda / Materials; Client Kick-off Invite sent.
- A14: Kick-off Meeting Notes / Follow-up sent.

## How the copilot uses this list

Scoring. Artifact Coverage = artifacts confirmed to exist / applicable artifacts x 100. The EVM Baseline applies to Fixed-Price projects only; on T&M it is N/A and leaves the denominator, it is never "missing". Report the score alongside the A-step map, not instead of it - the A-step map says what work is left, the artifact score says what the PMO will look for.

Where to look for each. Most of these do NOT live in the project folder on disk. The scanner alone cannot confirm them. The knowledge container, the project folders, the P&L, the EVM Baseline, the chats, the baseline validation, the start approval, PROREP, the tracker, the documentation space and the kick-off deck all need the connectors (Drive, Chat, Jira, NotebookLM, Gmail). This is exactly why the takeover skill sweeps systems rather than folders.

Storage discipline. Note where the standard puts things, because our earlier drafts got this wrong: Project Description, Stakeholder Register, Critical Scope, Risk Register, Communication Plan and Onboarding Rules belong in CONFLUENCE, not as loose markdown. Markdown in the project folder is a working draft; the filed artifact is the Confluence page or the Sheet. Say which one you are producing.

Internal only. The Opportunity & Internal Risk Register and A02's internal RACI are never shared with the client and never go in a client-facing space. Opportunities and Innowise-only risks (profitability, internal staffing) are exactly what a client must not read.

Money. The P&L lives in the Sensitive Folder only. Never in the common folder, never in the knowledge container, not even as a link. The EVM Baseline sits with it: Planned Value is normally a money figure, so treat it as money unless the PM has built it in hours. Contract documents get the same treatment (see A03).

Never mark an artifact confirmed on inference. "There is probably a Jira board" is not confirmation. Either a tool call found it, or the PM confirmed it, or it is unconfirmed.
