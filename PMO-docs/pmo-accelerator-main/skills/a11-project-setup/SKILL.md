---
name: a11-project-setup
description: Sets up the places a project keeps things - its Drive folders, its NotebookLM notebook, its chats, its board and its PROREP card - plus the Communication Plan and Team Working Rules. Use when a project has nowhere to put anything, or when what it has is a mess - "the project has no folders", "our folder structure is a mess", "set up the project in Drive", "create the Drive folders", "is my project set up properly", "check the project structure", "what chats do I need", "set up the project structure", "A11". Creates the folders and the notebook with the PM's approval and fills in the PROREP card's descriptive fields; for chats and Confluence it advises rather than acting. Two boundaries - FILLING the notebook with content is `project-brain`, and the card's weekly status and metrics are `prorep-card` - this skill builds the containers, those two keep them alive. Not the copilot's own installation, which is `copilot-setup`. Never renames, moves or deletes anything that already exists. Standard A step A11.
---

# a11-project-setup - A11, the containers everything else assumes

A11 sets up the minimal project management system: the folders, the brain, the chats, the tracker, and the working documents. It matters more than its number suggests, because every earlier step assumes these already exist. A01 has nowhere to file a handover brief without a Drive folder; A08 has nowhere safe to put money without a Sensitive folder.

Read the contract from `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`, section A11. Conventions - the Drive layout, the chat taxonomy with its pin requirements, PROREP's structure, the two brains - are in `${CLAUDE_PLUGIN_ROOT}/references/pmo-conventions.md`. The 23 mandatory starting artifacts are in `${CLAUDE_PLUGIN_ROOT}/references/initiation-artifacts-checklist.md`; this step touches nine of them - 1, 2, 3, 14, 16, 17, 18, 19 and 20.

## Two halves with different prerequisites - do not run them as one block

The standard places A11 after team composition is confirmed, and lists the confirmed team, updated resource plan and updated P&L as its inputs. That is right for the documents and wrong for the containers, and the difference matters:

- **The containers - Drive structure, sensitive storage, the brain - should be built EARLY**, whenever the project needs somewhere to put things. They depend on nothing. A01 has nowhere to file a handover brief without a Drive folder; A08 has nowhere legitimate for money without a Sensitive folder. `project-router` is right to send PMs here out of sequence for this.
- **The documents - PROREP content, Communication Plan, Working Rules, the Project Description update - need A10 done.** A communication plan written before the team exists describes meetings nobody will hold.

So at Stage 0, work out which half the PM is here for and say so. Running the container half on a project with no team is correct and complete for what it covers; running the document half without a confirmed team produces paperwork that has to be redone.

## What this skill does and does not do

Be straight with the PM about this at the start, because the boundaries are deliberate.

| Area | What the copilot does |
|---|---|
| Drive folder structure | CREATES it, with approval. Gap-fills an existing structure without touching what is there. |
| NotebookLM project brain | CREATES or verifies it, with approval. Seeding is gated separately. |
| Project chats | ADVISES only, from the source of truth. Which chats, who belongs, what to pin. Never creates a chat, never invites anyone. |
| Tracker / board | ADVISES. Confirms whether one exists and is usable. |
| PROREP card | HELPS FILL IT IN. Asks for the card link, reads what is there, proposes content from what the project already has, writes on approval. Does not create the card. |
| Confluence documentation space | OPTIONAL. Offers it if the PM wants documents there; does not treat its absence as a blocker. |
| Communication Plan draft | DRAFTS it, gated before filing. |
| Onboarding / Team Working Rules | DRAFTS it, gated. There is no company template - say so. |
| Project Description | UPDATES the A04 document, gated. A mandatory A11 output that is easy to forget. |

## Hard rules that never relax

- **Never rename, move, trash or reorganise anything that already exists.** Not a folder, not a file. The only structural action is CREATING something that is missing, alongside what is there. A PM's existing structure may be untidy but it is load-bearing - links point at it, people know where things are.
- **Adapt to the project, do not impose.** If a project uses different folder names consistently and everyone understands them, map the standard onto their names rather than creating a parallel set. Two competing structures is a worse outcome than one imperfect structure.
- **Show the plan before creating anything.** A three-column view: what the standard expects, what exists now, what would be created. Then get a yes.
- **Never create a chat, never invite a person.** Membership is a real-world act with real-world consequences. Draft the list; the PM does it.
- Money and contract text never enter the project brain. Standard gates apply to every write.

## Stage 0 - Frame and read what exists

Confirm the project and client name, and where its Drive folder is or should be. Then LOOK before proposing anything: list what is actually in Drive, which chats exist, whether a brain exists, whether there is a tracker.

Say which situation you are in, because the rest of the flow differs:
- **New project, nothing exists** - you are building from scratch. Straightforward.
- **Something exists but is partial or non-standard** - you are gap-filling. Slower and more careful, and the PM's existing choices win where they conflict with the standard.

CHECKPOINT: "Here is what exists for [project] today: [inventory]. I will propose the missing pieces - nothing gets created until you approve each one. OK?"

## Stage 1 - Drive structure

The PMO layout, from `pmo-conventions.md` (live pages 5257166944, 5262049359):

```
PMO Private > Projects <YYYY> > <Client> - <Project>      General: team and client
    01_Presale              presale material, COPIED in
    02_Documentation        Requirements / Architecture / Design
    03_Delivery
    04_Meetings             Notes & Recordings
    05_Reports              client-facing reports
    (shortcut)              -> the project's PMO Sensitive folder
PMO Sensitive > Projects <YYYY> > <Client> - <Project>    PM only
    Finance (P&L)
    Legal & Contracts
    Internal
```

**The main folder is the Resource Manager's job, not the PM's and not the copilot's.** The RM creates it in PMO Private with the Sensitive shortcut inside and gives the PM the Content Manager role. If it does not exist, draft the PM's ask to the RM and stop this stage there. The PM, through the copilot, creates the inner folders.

**Presale material is copied into `01_Presale`, never moved** - the presale folder keeps its history. Commercial terms, rates, margins and signed documents go to Sensitive instead. Copying works on shared drives; moving does not.

A project set up before Aug 2026 may use the older layout (`<Project> - General` with PM / BA / Presale / Project Documentation / Meeting Recordings, plus `- Sensitive` and `- Presale Final` shortcuts). Map it onto the new one in the comparison; do not restructure it unless the PM asks.

**Present it as a three-column comparison** before doing anything: Standard / Exists now / Proposed action. Mark each row create, already there, or their-name-differs-and-that-is-fine.

Then the gap-fill rules:
- Only CREATE what is missing. Leave everything else exactly as it is.
- If they have `Docs` where the standard says `Project Documentation`, that is not a gap. Note the mapping and move on. Do not create a second folder.
- If a folder exists but in the wrong place, say so and let the PM decide. Do NOT move it - see the tooling limit below.
- Create one at a time, or in one batch the PM has explicitly approved as a batch. Report exactly what was created.

**A real tooling limit, say it plainly rather than failing halfway.** On shared drives the connector can CREATE folders but cannot move, trash, or make shortcuts. Two consequences:
- The Sensitive entry in the General folder is a SHORTCUT (on older projects, Presale Final too). Those cannot be created from here. Create the folder structure that can be created, then tell the PM exactly which shortcuts to add by hand and where. Do not create a real folder where a shortcut belongs just because a real folder is what the tool can make - that quietly forks the structure.
- Create in place. Never create-then-move, because the move will fail and leave things stranded.

The Common & Sensitive Project Folder is a mandatory starting artifact. If the Sensitive folder does not exist, flag that the project currently has nowhere legitimate to keep its P&L.

**And if you find money in the wrong place, that is an immediate correction, not a note.** The standard says sensitive information stored outside the approved location must be corrected immediately, and the scanner produces exactly this finding - it flags money-bearing files sitting in the common project folder. A11 owns sensitive storage, so this is the step that acts on it: name the file, say where it belongs, and get it moved. The connector cannot move files on a shared drive, so this is the PM's action - but it goes at the top of their list, not into a general gap register.

CHECKPOINT: "Created [list]. These need you to add by hand because shortcuts cannot be made from here: [list, with where each points]. Anything look wrong?"

## Stage 2 - The project brain

A mandatory starting artifact, and the one PMs most often skip.

Check whether one exists. If not, create it with approval, following the brain-seeding rules in `pmo-conventions.md` - native Docs and Slides sync cleanly, Office files and MCP-pushed Sheets do not, combine many small documents into one source.

Seeding is a SEPARATE gate from creating. Show the upload inventory and the hold-out list before pushing anything: no money, no contract text, no candidate CVs, no large raw client data. If `map-existing-project` already ran, its source register tells you what is worth adding.

Keep the two brains apart: the org Superbrain holds PMO standards, the project brain holds this project. A confidential contract notebook is a third thing and is not created here.

CHECKPOINT: brain located or created, with what went in and what was held back.

## Stage 3 - Chats (advisory only, from the source of truth)

Do not create anything here and do not invite anyone. The job is to point the PM at what is required and let them act.

**Read the source rather than reciting.** The requirements live at Confluence 3006398548, "Google Chats (How to use Internal)" in the PMO space, and `pmo-conventions.md` carries a verified summary including the per-chat pin lists. If the PM wants detail, give them the page - it is the source of truth, not this skill.

Eight chats: Pre-sale, Contract, Common, Internal, Strategy, Accounting, Economy, Staffing. Facts worth stating because PMs trip on them:

- **Every project chat is PRIVATE**, and artifacts belong on the chat's BOARD with a description, not just posted in the stream.
- **Common is the RENAMED pre-sale chat**, not a new one. Once the deal is Closed-Won and a PROREP card exists, the PM renames it to match the card: `(Common) <CRM deal name>`. Creating a fresh Common chat loses the pre-sale history, which is the whole point of it.
- **Strategy and Accounting are bot-created on Closed-Won.** So missing usually has an explanation - but the PM must confirm with the Sales Manager that they exist AND that the PM is in them. Their links should also be on the PROREP card, so that is where to check.
- **Staffing is chat 8 and the source page defines it with an empty section.** A genuine gap in the standard. Say that rather than inventing its purpose.

For each chat tell the PM: does it exist, are they a member, who else belongs, what should be pinned. Pins are part of the mandatory Project Chats artifact, so an existing chat with no pins is still a gap - but only Internal, Strategy and Accounting have specified pin lists. **Do not invent pins for the other five**; say the page does not specify them.

The money boundaries are strict and worth repeating to the PM, because breaking them is a policy incident rather than an untidiness: Economy chat only for economy calculations and only for its participants; finance and payments go to Accounting, never Strategy; Accounting carries budget and billing but no rates or salaries at all where the project uses different rates per role.

Say plainly: "these are the chats you need and who belongs in them - creating them and adding people is yours, not mine."

CHECKPOINT: the chat table with existence, membership, pins and the PM's actions.

## Stage 4 - Tracker and PROREP

**Tracker.** Confirm a board exists and is usable for delivery (a mandatory starting artifact). If none exists, the standard is blunt: the team should not start delivery work without one unless a temporary approach is agreed. Report that; do not configure Jira from here.

**PROREP (a mandatory starting artifact) - fill in the descriptive side of the EPIC.** A11 owns this. The copilot does not create the card - it should exist from Closed-Won, and a PM who cannot find one has a finding to route to the Sales Manager rather than something to work around.

**Read `${CLAUDE_PLUGIN_ROOT}/references/prorep-fields.md` first, and work by field ID.** It is a live map of what is on the card, what gets filled in practice, and where each value comes from. This is not optional care: the card carries over 500 fields including English and Russian near-duplicates of the same thing, and two different project-stage fields with different option sets. Filling the wrong one of a pair leaves the project described twice and inconsistently on a leadership-visible record.

Most of the content already exists in what earlier steps produced - the A04 description, the A01 client profile and industry, the A07 roadmap dates, the A05 stack, the A03 cooperation model, the aliases in `project-context.md`. Map it across rather than interviewing the PM.

Four things A11 specifically owes:

- **The billable-hours tie.** If the card's initial budget in billable hours and the A07/A08 plan disagree, one of them is wrong, and it is better found here than in a report. Check it explicitly and name the discrepancy.
- **Hours, never currency.** The billable-hours fields are HOURS and are safe. `Budget constraint` is a Yes/No flag, not an amount. There is one field that could take a money figure and the map says to leave it alone. **Do not put a money figure anywhere on the card.**
- **Read the links and roles rather than asking.** The card usually already carries the chat links, the timesheet link, the report link, the DM, AM, TL and RM - and the project's NotebookLM URL in its Knowledge Container field. Harvest those into `project-context.md` instead of asking the PM about their own project. If the brain link is there, the brain may exist even where the folder looks empty.
- **The presale narrative block.** The card carries a numbered Russian series starting "information from the sales manager". That is handover material sitting in Jira, so read it before A01 concludes anything is missing from Sales.

**The metrics are NOT part of setup.** The eight `Indicator_*` fields are a weekly job that `prorep-card` runs for the life of the project. Do not fill them here and do not count them as an A11 gap - but do tell the PM the weekly cycle exists and which skill runs it, because a card set up once and then never updated is the common failure. The other two metric-ish field sets on the card are abandoned or owned elsewhere; the map says which is which.

Child issue types are separate work again: `Report`, `Health check`, `Milestone`, `Action Item`, `Employee`, `Out of office`. Worth knowing so you do not conflate them - the health metrics and the Weekly Project Report are different issue types, not two names for one thing.

Writing to the card is a gated write like any other: show the content field by field WITH its field ID, get a yes, write, report what changed.

CHECKPOINT: tracker status; the card read, the proposed content shown field by field, the hours tie, what was harvested into `project-context.md`, and what still needs the PM.

## Stage 5 - The documents A11 owns

**Project Description update** (mandatory A11 output, and the one most easily missed because A04 already wrote it). By now the team is confirmed, the plan exists, and the contract may have been reviewed - so the description written at A04 is out of date in specific ways. Read it, then update: the confirmed team and roles, anything A03 changed about commitments, the agreed roadmap and dates, and any assumption the plan settled or invalidated.

Per the baseline rule, UPDATE the existing document rather than writing a second one, and say what changed. Two project descriptions that disagree is a worse outcome than one that was stale.

**Communication Plan draft** (a mandatory starting artifact). Format spec at Confluence 3272082121, worked example at 3271000087. Draft it from what is actually true: the chats that exist, the meeting cadence already in the calendar, the stakeholders from A02 if that ran. A communication plan that describes meetings nobody holds is worse than none.

**Project Onboarding / Team Working Rules** (a mandatory starting artifact). There is NO company template - the standard's own task ends with `[Link TBD]`. Say that to the PM rather than presenting your structure as house practice. Draft from the project's real working model: cadence, definition of done, review rules, environments, who to ask about what.

Both are drafts for review. Filing them is a separate yes, and the artifacts checklist puts both in Confluence.

## Stage 6 - Documentation space (optional)

The mandatory Project Documentation Space says Confluence / Drive / Other. In practice the copilot produces Google Docs and puts them in the brain, and that satisfies "other" for now.

So: offer, do not insist. If the PM wants documents in Confluence, help set that up. If they are happy with Drive plus the brain, record that as the documentation space and move on. Do not treat the absence of a Confluence space as a blocker at this stage.

## Stage 7 - Access and link readiness

The A11 control metric: Access and Link Readiness Coverage = required resources with verified access and links / total required resources x 100. Target 100% before the readiness review, except documented pending external access.

List every resource this project needs - folders, brain, chats, tracker, PROREP card, key documents - with a real link and a confirmed access state. State the number with its denominator and name what is in it.

**Everything mandatory stays in the denominator, including anything still outstanding.** Do not drop a resource to make the number reach 100. A coverage of 8 of 11 with the three gaps named is a useful number; a 100% achieved by excluding what is missing is worse than no number at all.

**"Verified" means you actually opened it.** Not that it appears in a list, and not that it probably exists. Where the copilot cannot check something itself - a chat it has no access to, a Jira permission - ask the PM to confirm and record it as PM-confirmed rather than verified. The two are different and the distinction is the whole value of the metric.

CHECKPOINT: the readiness table and the number, plus the short list of what is still the PM's to do (shortcuts, chats, invites, PROREP).

## Outputs

Containers (no dependency on staffing):
- Drive folder structure created or gap-filled, with the list of shortcuts the PM must add by hand.
- Project brain created or verified; seeding behind its own gate.
- Any sensitive file found in the wrong place, named for immediate correction.

Documents (need the confirmed team from A10):
- PROREP card content proposed and, on approval, written.
- Project Description UPDATED for the confirmed team, plan and contract state.
- Communication Plan draft and Team Working Rules draft, gated before filing.

Both halves:
- Chat plan: what is needed, who belongs, what to pin, from the source page - for the PM to action.
- Tracker status.
- Access and Link Readiness table with the coverage number and its denominator intact.

## Close-out
Route what stays open: shortcuts, chat creation and invites, and PROREP are the PM's actions - list them plainly. If the Sensitive folder is still missing, say that the project has nowhere legitimate for its P&L and that A08 is blocked until it exists.

A thin or skipped part is justified-and-recorded, never a silent pass.

Then write the residue down, and say in one line that you did:

- Anything that needs DOING goes in `<workspace>/pm-tasks.md`, tagged with the project - the PM's actions, what is waiting on someone else, what you routed elsewhere. Actions that only ever exist in this conversation are lost when it ends, and the PM re-derives them next week.
- Anything durable you learned about the project goes in `<project folder>/project-context.md` - decisions and who made them, people, links, and what is still open.
- **This skill builds the brain's CONTAINER; `project-brain` is what keeps it alive afterwards.** Record the notebook ID in `project-context.md` so nothing later has to go hunting for it by name. Then hand the seeding itself to `project-brain` (feed mode) rather than doing it here - one definition of what goes in and what is held out, and this skill's job is the containers.
  - Worth saying out loud to the PM at hand-off, because it is the thing that actually decays: an empty or one-off-seeded brain scores as a present artifact and is still useless. Tell them the copilot will offer to add things as they are produced, and that they can ask "is the brain current" any time - that is a real answer, not a platitude, because `project-brain` has a review mode that reports the newest source and what is missing.
- Anything the copilot got wrong, or asked for and could not do, goes in `<workspace>/copilot-feedback.md`.
