---
source: Innowise PMO Confluence (Google Drives instruction 5257166927, Drive Structure Description 5257167110, Project Folder Structure Template 5262049359, Google Chats 3006398548, PROREP 3723624953, Reporting, NotebookLM Project Brain 4955406559) + confirmed practice
synced: 2026-07-28
---
# PMO conventions - where things live and what they are called

House practice a PM is expected to already know. The copilot reads this so it can file things correctly and so it never has to guess at convention.

Rule that overrides everything in this file: if the copilot is unsure what we usually do, it SAYS SO. "I am not sure what we usually put here, this is my draft, let us check it" beats presenting a guess as house practice. The people who hold the real conventions are the PMO leads, contracts and presales - the copilot brings content, not authority.

## Drive structure per project

Source of truth: Confluence 5257166927 (Google Drives instruction; "1 Creating Project Folders" is 5257166944), 5257167110 (Drive Structure Description) and 5262049359 (Project Folder Structure Template), all Aug 2026. Read them when advising a PM.

Two Shared Drives, split by sensitivity:

- **PMO Private** - the General side, shareable with the team and the client. Project folder: `PMO Private > Projects <YYYY> > <Client> - <Project>` (the live name uses a long dash). Subfolders:
  - `01_Presale` - presale material, COPIED in (never moved); commercial terms excluded
  - `02_Documentation` - Requirements, Architecture, Design
  - `03_Delivery` - delivery artifacts and working files
  - `04_Meetings` - Notes & Recordings
  - `05_Reports` - client-facing reports
- **PMO Sensitive** - PM only, never shared with the team. `PMO Sensitive > Projects <YYYY> > <Client> - <Project>` with `Finance (P&L)`, `Legal & Contracts`, `Internal`. Separately, `Projects P&L` holds project economics.

Who does what: the **Resource Manager creates the project's main folder** in PMO Private, with a shortcut to the project's Sensitive folder inside it, and gives the PM the Content Manager role. The PM creates the inner folders per the template and copies the presale material into `01_Presale`, sending commercial terms, rates, margins and signed documents to Sensitive instead. Active projects sit in the current-year folder - a shortcut from the original year is the recommended way.

Naming: numbered subfolders `NN_Name`; dated files `YYYY-MM-DD_<Name>`.

Sharing: share the whole General folder by default, or a subfolder when only part of it is for someone. A "hidden" subfolder is never a place for sensitive content - that goes to PMO Sensitive.

Projects set up before Aug 2026 may still use the older layout (`<Project> - General` with PM / BA / Presale / Project Documentation / Meeting Recordings, a `- Sensitive` shortcut and a `- Presale Final` shortcut). Map an old layout rather than restructuring it unasked.

Default placement: A-block working documents in `03_Delivery`, specs in `02_Documentation`. Economy and P&L in Sensitive, only. Contract documents in Sensitive. Nothing money-bearing gets a shortcut into General.

Known MCP limits on shared drives: creating and copying work, but moving, trashing and shortcut-making do not. Create in place rather than creating then moving.

## Chats

Source of truth: Confluence 3006398548, "Google Chats (How to use Internal)", PMO space. Verified against it 2026-07-28. Read that page when advising a PM - the copilot does not create chats or invite anyone, it points at the requirements.

**Rule that applies to all of them: every project chat is PRIVATE**, to keep sensitive data out of reach. Artifacts go on the chat's BOARD with a description, not just posted in the stream.

| # | Chat | Purpose | Who creates it |
|---|---|---|---|
| 1 | Pre-sale | estimates, preliminary solution, proposal prep, pre-sale data | Presale/Sales Manager from the CRM |
| 2 | Contract | contract and SOW content, addendums, protective clauses, under PMO supervision | Sales, sometimes automatic |
| 3 | Common | history and continuing context after pre-sale; new contracts or extensions | RENAMED from the pre-sale chat by the PM |
| 4 | Internal | day-to-day team coordination. Team participants only | PM, once the team is defined |
| 5 | Strategy | stakeholder alignment at M2 and above: risks, escalations, TL allocation, release planning, reporting without finance | bot, on CRM Closed-Won |
| 6 | Accounting | sensitive discussion and high-management escalation; budget and billing WITHOUT rates or salaries | bot, on CRM Closed-Won |
| 7 | Economy | economy calculations, cost, profitability. Confidential to its participants ONLY | PMO RM, PM or Sales |
| 8 | Staffing | the page carries the heading with no content yet - a real gap in the standard, not a lookup failure | - |

**The pre-sale to Common conversion is a PM action with a naming convention.** Once the deal hits Closed-Won and a PROREP card exists, the PM renames the pre-sale chat to match the PROREP card name: `(Common) <CRM deal name>`, for example `(Common) PromoveTM`. Participants carry over.

**Strategy and Accounting are bot-created on Closed-Won**, so a missing one usually has an explanation - but the PM must check with the Sales Manager that they exist and that the PM is IN them. Links to auto-created chats should also appear on the PROREP card.

### Required pins, per the source page

Only three chats specify pins. Do not invent pins for the others; say the page does not specify them.

- **Internal**: Project NotebookLM, project Jira board, project Confluence, project Drive folder. Nice to have: roadmap/timeline, vacation calendar.
- **Strategy**: Jira PROREP card, project Jira board, the project's Jira dashboards, Resource Plan. Nice to have: roadmap/timeline.
- **Accounting**: Jira PROREP card, Resource Plan, reports (project Drive), a link to the Economy chat, a link to the Contract chat.

### Money boundaries between chats, which are strict

- Economy chat is the ONLY place economy calculations live, and only its participants may see them.
- Strategy chat: any finance or payment discussion goes to Accounting instead. External reporting shared here carries no finance information.
- Accounting chat: budget and billing WITHOUT rates or salaries. Where a project uses different rates per role, rates must not be communicated there at all - Resource Managers and Department Heads cannot see rates for departments they do not belong to.
- Contract chat: PMO does not proceed without the DM's completed Mandatory Materials file (Sheet `1IkVpQPPc-TzImiis0kAi_vgXLzSSo-0opDvUhjIW8tc`).

## Knowledge containers - two brains, kept apart

**Superbrain** - the org-wide NotebookLM holding PMO standards, instructions and the knowledge base. One per org, shared with the PM team. Notebook `158e107b-0f3e-47b9-9566-f481595ab399`, 46 sources as of this sync.

Query it rather than guessing whenever a question is about house process. What is in there:

- Project Standards A through F - initiation, monthly/milestone initiation, weekly/sprint management, daily management, monthly/milestone closure, project closure. Also the Minimal Required Project Management Framework.
- Instructions - PROREP project card, Project Budget, Reporting.
- Knowledge Base - Risk Framework and Risk Library, Project Charter, Project Roles, Project Templates, Projects Guidelines, DoR/DoD, Agile, Technical Delivery Fundamentals, internal education.
- PMO Overview - management structure, Contracts and Legal processes, project audit process, onboarding, chats and syncs.

This matters most OUTSIDE initiation. The copilot's STEP skills cover only the A block - plus the artifact skills `project-brain`, `risk-register` and `prorep-card`, which work at any point in a project - but Superbrain carries B through F, so "there is no skill for this" is never the same as "we have nothing on this". Query the standard, read its requirements out, and work through it with the PM.

Where it sits against the reference pack: the bundled pack is authoritative for a step's contract and for the artifact checklist, because it is versioned and exact. Superbrain is better for narrative and for the "how do we usually handle this" questions a checklist cannot answer. If the two disagree, Confluence settles it.

**Project brain** - one per project, mandatory (A01, updated A11). Holds that project's knowledge. Never holds money. Never holds contract text.

**Confidential contract notebook** - a separate container used only for the A03 contract version comparison. Never the project brain, never anything the broader team can reach.

Seeding rules for the project brain:
- Native Google Docs and Slides add cleanly as Drive sources. Office files and Sheets pushed via MCP do not sync reliably.
- Combine many small documents into one source (all transcripts into one text source, meeting notes into one compiled Doc) to stay under the source limit.
- Hold out: anything money-bearing, P&L, contracts, candidate CVs and staffing sheets with personal data, and large raw client data files. For a big data file, put a data dictionary note in the brain instead of the file.
- Show the upload inventory and the hold-out list before pushing. Every time.

## PROREP

The project card in Jira: project `PROREP`, board 1500, at `https://innowise-group.atlassian.net/jira/software/c/projects/PROREP/boards/1500`. Instruction: Confluence 3723624953 and its field subpages.

**The card is an EPIC.** Verified against the project 2026-07-28. Hanging off it are these issue types, which is why the card is a container rather than a single form:

| Type | What it is for |
|---|---|
| Epic | THE project card - key project information, links, control artifacts |
| Report | the reporting deliverable (e.g. the Weekly Project Report) |
| Health check (+ subtask) | the card's health metrics |
| Milestone | milestones |
| Action Item | actions |
| Employee | people on the project |
| Out of office | absences |

So the health metrics are literally a different issue type from the Report deliverable - that is the distinction not to conflate, and it is structural rather than a matter of naming.

### The Epic's Key details panel

Only the EPIC matters for the copilot - the child issue types are other people's work or are computed. The Epic's Key details panel is tabbed, and the tab labels are Russian (transliterated here because workspace files stay ASCII):

| Tab | Copilot |
|---|---|
| Description (OPISANIE) | HELPS FILL |
| Client (KLIENT) - incl. domain / industry | HELPS FILL |
| Implementation (REALIZATSIYA) | HELPS FILL |
| Technologies (TEKHNOLOGII) | HELPS FILL |
| Other (PROCHEE) | helps where it is plainly project detail |
| METRICS / PMO Operational Metrics | THREE different field sets get called this and they are not the same thing. `prorep-fields.md` separates them by field ID - read it before writing anything here. Short version: the eight `Indicator_*` fields are the PM's weekly job and belong to `prorep-card`; a set of older lozenge fields is abandoned; Health Check and audit are owned elsewhere. Which UI tab label sits over which set is unresolved and no tool exposes it. |
| Marketing materials | NOT ours |

**The full field map, by ID, with what is filled in practice and where each value comes from, is in
`prorep-fields.md`.** It was built from a live card read (519 fields) and it supersedes the partial
list below for anything operational - the card carries near-duplicate English and Russian fields,
two different project-stage fields, and two different card shapes, none of which is safe to guess at.

Fields on the Implementation tab, observed on a live card 2026-07-28:

| Field | Where the content comes from |
|---|---|
| Project start (Nachalo proekta) | A07 roadmap |
| Project end (Konets proekta) | A07 roadmap |
| Project status (Status proekta) | the PM |
| Project stage | the PM |
| Alternative project name | the aliases in `project-context.md` and the PM profile |
| Country (Strana) | A01 client profile |
| Cooperation model (Model sotrudnichestva) - e.g. FP | A01 contract type, confirmed at A03 |
| Budget constraint | the cap, from the contract |
| Project from Presale | A01 |
| Initial budget (billable hours) | the billable total from the A07/A08 plan |
| Miscalculated budget | derived - negative means over |

Note that the budget fields here are HOURS, not currency, so they are safe to discuss and to write. Do not put a money figure on the card.

The other tabs' field lists are not captured here - read them off the card, and read the instruction subpages, rather than guessing at custom field names.

Links to bot-created chats (Strategy, Accounting) should appear on the card, so it is also the place to check whether those exist.

## Reporting and filing

- PMO Weekly Report goes to "Internal Reports", filed as Year / Month_Project_Weekly Reports.
- Client-facing reports go to the General side, `05_Reports` (Project Folder Structure Template 5262049359). Older projects may still keep them in Sensitive, "External (Sent to Client)".
- The billable report is Jira Done crossed with HRM hours, Salesforce IDs stripped, sent to Sales.

## Documents strategy

The vault or local markdown is the WORKING DRAFT. The filed artifact is the Confluence page, the Google Doc, or the Sheet - whichever the artifacts checklist specifies. Say which one you are producing so the PM knows whether it counts yet.

Per the artifacts checklist: Project Description, Stakeholder Register, Critical Scope with Acceptance Criteria, Risk Register, Communication Plan and Onboarding / Team Working Rules are CONFLUENCE artifacts. WBS, Team Composition, Resource Plan are SPREADSHEETS. P&L is a spreadsheet in the Sensitive folder. The Kick-off deck is Google Slides.

## Editing gotchas worth knowing before you try

**Google Docs.** Content often lives in a tab; passing no tab_id returns an empty structure, so always pass it. Delete a range with the `delete_text` batch op. `create_table_with_data` does not inherit the previous table's look - column widths, header shading and bold all have to be restored. A table inserted after a heading inherits the heading's bold across every cell.

**Google Slides.** Tables and grouped graphics report as type Unknown and do not expose child object IDs, so a table inside a group is not cell-addressable - delete the group and create a fresh table, then re-style it. Object IDs you create must be at least 5 characters. Deleting and re-inserting text collapses run styling to the box default, so re-apply size, bold and colour afterwards, and re-apply or remove bullets. A native timeline is better built from shapes than embedded as an image. Canvas is 10 x 5.625 inches, 914400 EMU per inch.

**Both.** `replaceAllText` with zero matches does NOT error - a silent no-op looks exactly like success. Always verify visually afterwards. Match anchors without apostrophes or ampersands so curly-quote mismatches cannot cause a silent miss.

**Adapting an existing deck or doc for a new client is not a name swap.** Read the rendered content, including table cells, before editing. Fix every embedded reference - vendor names, portal names, feature names, team names - and check that every number still foots (hour splits against totals, line items against subtotals).

## File writing on Windows

Workspace files must be plain ASCII. Non-ASCII UTF-8 bytes get double-encoded by Windows tooling and turn into garbage. Use `-` instead of dashes and arrows, straight quotes instead of smart ones.

## Writing voice for anything the PM sends

Lives in the `pm-voice` skill now, not here: length budgets by channel, the house register of PMO chat spaces, and the English and Russian AI tells. A PM with their own voice skill uses that instead. The short version for when neither is loaded: no em dashes, no preamble or postamble, keep English delivery vocabulary in Cyrillic rather than translating it, and keep it short.
