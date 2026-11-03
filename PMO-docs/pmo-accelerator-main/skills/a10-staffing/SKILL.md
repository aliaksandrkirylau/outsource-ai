---
name: a10-staffing
description: Drafts the role requirements a PM sends the Delivery Manager to get people, and moves the confirmed team into the Resource Plan and the P&L once names come back. Use at either end of a staffing run - when the PM is about to ask for people and needs the requirements written or checked against the plan, or when the DM has come back and the team has to be recorded - "request the team", "what roles do I need to staff", "position requirements", "check these requirements", "the DM sent role requirements", "am I ready to start staffing", "staffing is done", "move the team into the resource plan", "update the P&L with the confirmed team", "staffing", "A10". Also checks the prerequisites and whether the A09 gate has passed, and hands the PM a checklist for accepting candidates with the DM. The staffing run itself belongs to the Delivery Manager - the copilot never sees a CV and never assesses a candidate. Standard A step A10.
---

# a10-staffing - the ends of a process that runs outside the copilot

A10 has four mandatory outputs: the Staffing Master / Staffing Run, the Confirmed Project Team Composition, the updated Resource Plan and the updated P&L with confirmed candidates. Almost none of that work is the copilot's.

What actually happens: the PM asks the Delivery Manager for the position requirements, the request goes to the Resource Manager, the RM runs staffing in the Staffing Master, candidates come back, and the PM decides with the DM. The copilot is useful at three specific moments and nowhere else:

- **Before** - are the prerequisites and the A09 gate actually in place, and help with the position requirements (draft a starting point, or check what the DM produced).
- **Hand over** - give the PM the checklist of what to go over when accepting candidates. Then get out of the way.
- **After** - on request, move the confirmed data into the Resource Plan copy and the P&L.

Read the contract from `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`, section A10. The P&L mechanics are in `${CLAUDE_PLUGIN_ROOT}/references/pl-structure.md` - read that before touching a sheet.

## The rules that matter here

**The copilot does not see CVs and does not assess candidates.** Not "CVs must not go in the brain" - they do not come to the copilot at all. It has no role in judging a person's competence or fit, and it should say so rather than being helpful about it. If a PM pastes a profile in, do not analyse it: say the assessment is theirs with the DM, and point at the checklist.

- Salary and tax residency stay blank in the P&L. Finance owns them. Never infer a salary from a grade.
- Rates are not the copilot's to write. If a confirmed rate needs to go in, the PM supplies the figure.
- The copilot does not contact a Resource Manager or a Delivery Manager, and does not approve anything.

## Stage 0 - Prerequisites, the gate, and what this skill will and will not do

Say up front what is coming, so the PM is not waiting for the copilot to run staffing: the run happens outside, and the copilot helps with requirements at the front and the data at the back.

The staffing instruction requires three things to exist BEFORE a request goes in. PMs routinely discover this halfway through:

1. **The project P&L** - it has to exist for candidate cost to be checked against anything. If it does not, that is a request to PMO RM, not something to build (see `pl-structure.md`).
2. **The Staffing Master file** - requested from RM PMO. There is no self-serve template; the file is issued.
3. **The project Google Chat space with a webhook** - the staffing process posts into it.

Then the gate. Check `project-context.md` for the recorded A09 outcome. **If A09 has not passed, stop and say so** - the standard is explicit that no internal go means no team appointment. Staffing a project whose baseline was never approved is a governance problem, and the answer is to close A09 first, not to proceed carefully.

Inputs the requirements will be built from or checked against: the Required Roles List (A05), the role-by-month plan (A07), the milestone timeline, and the grades in the P&L staffing tab.

CHECKPOINT: "Prerequisites: [status of each]. A09: [outcome and date, or NOT PASSED]. [Ready to work on requirements / here is what has to exist first]."

## Stage 1 - Position requirements (the DM's content, not ours)

The requirements for each position are the Delivery Manager's to provide - the PM asks the DM for them. So the copilot has three modes, and it should ask which one is wanted rather than assuming:

- **Draft a starting point** from the A05 roles, the WBS and the role-by-month plan, for the PM to send the DM as a basis to correct. Useful when the DM would rather react to something than write from scratch.
- **Check what the DM came back with** against the plan, the WBS hours and the P&L grades. Probably the most common case, and the most useful: a requirement set that quietly asks for a Senior where the economy assumed a Middle is worth catching before the RM starts searching.
- **Help write the ask** to the DM, if that is all that is needed.

### What good requirements contain

Taken from a real set that worked, not invented. Per position:

- **Stack** - the actual technologies, concretely. This is the first thing an RM matches on and it is the most common omission.
- **Must-have versus strong-plus, separated explicitly.** "Must have AWS, FastAPI and queue experience; LLM experience is important but not mandatory at the decision" tells an RM how to trade off. A flat list of skills does not.
- **Hours** for the role, tied to the plan.
- **Tasks** - what this person will actually do. Lets the RM and the candidate both judge fit.
- **Seniority, allocation, start and end period, location or time-zone constraints** including any client-side requirement from A01.
- **Which critical scope area (CS-id) the role exists to deliver.**

Plus, on the document itself: a short **project-in-short paragraph**. An RM working several requests a week needs to know what the project is. And a **basis** line - which WBS version, which plan, which P&L tab the grades came from - so anyone can see where the numbers came from.

### Flag before it goes out

- Roles where seniority is genuinely negotiable versus roles where it is not.
- Roles on the critical path, where unstaffable blocks the plan rather than delaying it.
- Any role whose cost assumption in the P&L is tight, so a more expensive candidate breaks the economy.
- Whether a technical expert needs to be in the candidate review, which is worth lining up now rather than when three profiles arrive.

**Get the DM's approval recorded before the request goes to the RM.** Requirements are their content; a set the DM has not signed off produces candidates nobody wanted. Put the approver's name and the date on the document.

CHECKPOINT: the drafted or checked requirements, the flags, and who still needs to approve them.

## Stage 2 - Hand over, with the checklist

Two things happen here: the copilot gives the PM the acceptance checklist, and then stops.

### The checklist - what to go over when accepting candidates

This is the standard's own verification set, handed to the PM as something to work through with the DM. The copilot holds the list. It does not apply it, and it does not want the CVs.

| Check | Why it is on the list |
|---|---|
| Profile / CV reviewed | Must happen BEFORE approval, not after |
| Competence for the role | Bring a technical expert where deep validation is needed |
| Seniority against the request | A gap here is a re-plan, not a detail |
| Availability and start date | Against the milestone timeline, not in the abstract |
| Allocation | Does the offered allocation match what the plan assumed |
| Location / time-zone constraints | Including any client-side requirement from A01 |
| Project fit | The soft one, and worth a sentence in writing |
| **Cost, paid hours and allocation against the P&L** | The row that catches an approval the economy cannot carry |

That last row is where a project quietly goes underwater, and it is the only one the copilot can genuinely help with later - it is about the plan, not the person. If a candidate's cost materially changes the P&L, the standard says clear it with RM, Head or internal management BEFORE approving, and update the Resource Plan and P&L as part of that rather than afterwards.

Escalations to name now so the PM recognises them later:
- A mandatory role for critical scope that cannot be staffed goes to RM / Head / Delivery before kick-off.
- A candidate who does not match competence, seniority, location, allocation, availability or constraints is not approved without clarification or explicit management acceptance.

### Then hand over properly

> The staffing run is the Resource Manager's process and happens in the Staffing Master. The instruction is at Confluence 4957110283 (the process, marked WiP) and 4954554594 (what it is and why). The candidate decisions are yours with the DM. Come back when the team is confirmed and I can move the data.

Do not simulate it, do not track it, do not chase the RM.

**Record that it is out**, because this pauses for days or weeks and the answer will land in a different session: put the request date, who it went to, and the roles outstanding in `project-context.md`, and add "staffing in progress, waiting on RM" to `pm-tasks.md`. On re-entry, read that first rather than re-drafting requirements that are already with the RM.

CHECKPOINT: the checklist handed over, the hand-off stated, the pending state recorded.

## Stage 3 - Move the confirmed data (only when asked, WRITE GATE)

When the team is confirmed, OFFER this rather than assuming it: "Staffing done - want me to move the confirmed team into your Resource Plan and the P&L?"

Then ask for the three things the copilot cannot know:

1. **Which P&L file, and which TAB** to write to. Do not guess a tab.
2. **The link to the Resource Plan copy** the PM made from the template. The PM makes that copy - Project Resource Plan 3.0, Sheet `1WKcXz9W2BGrtRChNQ8DsZghcUFqvDcqbhOx8u1cDKJU`, instruction Confluence 4757127285 - because the connector cannot create the shared-drive shortcut it needs. Do not offer to build one by hand.
3. **The confirmed team as the PM has it** - names, roles, grades, allocation, start dates. From the PM or the Staffing Master, not from CVs.

Then follow the write sequence in `pl-structure.md` exactly:

1. Work on a dated COPY of the tab.
2. Confirm the active month COLUMNS from a LIVE header read, matching each month code to its column letter. Never infer a column from an array index.
3. Read raw values, not displayed ones.
4. **Write both hour rows and the role or person labels.** Paid = worked by default; a role that is not billable gets worked hours and zero paid. **Rates, salary, tax residency and grade are not yours to fill** - if a confirmed rate needs writing, the PM supplies the figure and you echo it back before writing it.
5. **Verify control totals**, and the one that matters is total BILLABLE hours against the plan and the contract. Then each role's total, and total worked. A total that is not roughly equal is a targeting bug, not rounding - attribute it before moving on.
6. Report cells touched, totals before and after, and anything from the confirmed team that did not make it in.

**Say what the confirmed team does to the plan, before writing.** A different grade, a later start, a changed allocation - name the consequence while the PM can still act on it. That is the moment, not after the sheet is updated.

This is also where fair-hours redistribution legitimately becomes available, unlike at A07/A08 - there are real people, real grades and a real billable pool now. If billed and worked hours diverge across the team, the rules are in `pl-structure.md`. Cards first, write last: surface a proposed split for the PM to look at and nudge before anything goes in. And note the case the plan may already have created - a role carried as worked-but-unpaid, typically an absorbed DM, is a PARTICIPANT in a split, not a line to hold out.

Control metrics:
- Candidate Vetting Coverage = approved candidates with a documented profile, competence and cost review / total approved candidates x 100. Target above 80% before staffing closes. **The copilot can only report what the PM tells it** - it did not run the vetting. Ask which checks were done and say the number is self-reported, rather than presenting it as measured.
- Resource Plan Timeliness (Sep 2026) = the updated Project Resource Plan is finalised no later than 3 working days after staffing closure. Target 100%. Say the date out loud when staffing closes, because it is the one deadline in this step with a clock on it.
- Staffing Data Update Coverage = approved candidates reflected in the Resource Plan AND the P&L / total approved candidates x 100. Target 100% before kick-off. Both files, not one. This one the copilot can check properly, because it did the writing.

CHECKPOINT (mandatory): "I will write these hours for [N] confirmed people to [file / tab / dated copy], columns [letters, confirmed from a live read]. Paid equals worked except [role]. Billable total [n]h, matching the plan. Rates, salary, residency and grade untouched. Confirm and I will write, then re-read the totals to prove it tied."

If the PM would rather paste the numbers themselves, hand over a clean table with the target cells named. That is a perfectly good outcome.

## Outputs
- Prerequisite and A09 gate check, with what is missing and who to ask.
- Position requirements - drafted as a starting point, or a check of the DM's version against the plan, WBS hours and P&L grades, with the flags and the recorded approver.
- The candidate acceptance checklist, handed to the PM.
- Updated Resource Plan copy and updated P&L, behind the write gate, control totals verified.
- Staffing Data Update Coverage (measured), Candidate Vetting Coverage (self-reported by the PM).

Never an output: any assessment of a candidate, or a CV in any form.

## Close-out

Confirmed Team Composition is a mandatory starting artifact and lives in a spreadsheet - in practice the Resource Plan copy, sometimes the Staffing Master. Say which one holds it for this project rather than leaving it implied, and record the link in `project-context.md`.

What stays open: unstaffed roles with their escalation owner, any cost variance not yet cleared, any technical validation still pending. A thin or skipped check is justified-and-recorded, never a silent pass.

Once the team is confirmed, A11 (`a11-project-setup`) and then A12 (`a12-a14-kickoff`) follow - the standard sequences team confirmation before system setup and internal alignment.

Then write the residue down, and say in one line that you did:

- Anything that needs DOING goes in `<workspace>/pm-tasks.md`, tagged with the project - the PM's actions, what is waiting on someone else, what you routed elsewhere. Actions that only ever exist in this conversation are lost when it ends, and the PM re-derives them next week.
- Anything durable you learned about the project goes in `<project folder>/project-context.md` - decisions and who made them, people, links, and what is still open.
- **The project brain gets WHO IS ON THE TEAM and in what role. It never gets the staffing paperwork.** The roster as names and roles is ordinary project knowledge the team itself can see, and it answers a question people ask constantly - offer that via `project-brain` (feed mode). What stays out, per `${CLAUDE_PLUGIN_ROOT}/references/pmo-conventions.md`: candidate CVs, and any staffing sheet or Resource Plan tab carrying personal data or money. The Staffing Master is not a brain document.
  - The distinction to hold on to, because it is easy to blur when the roster and the sheet arrive together: the FACT of the team is shareable, the HR record behind it is not. If the only place a roster exists is a sheet full of PII and rates, put the roster in as a short note rather than pushing the file.
- Anything the copilot got wrong, or asked for and could not do, goes in `<workspace>/copilot-feedback.md`.
