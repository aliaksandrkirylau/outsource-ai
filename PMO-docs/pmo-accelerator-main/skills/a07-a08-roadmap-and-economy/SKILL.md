---
name: a07-a08-roadmap-and-economy
description: Builds the roadmap and milestones with owners and dates (A07), then the role-by-month hours plan, and gets it into the project economy file for the PM and the Resource Manager to work on (A08). Use when the PM owes a client or leadership dates and has none, when the economy file is still empty so staffing cannot be requested, or when someone asks how long this will take and the honest answer is a guess - "build the roadmap", "milestone schedule", "plan the resources", "role by month", "how long will this take", "put the plan in the P&L", "does this fit the cap". Reads the validated scope and the WBS FIRST and proposes a plan with defaults already chosen, rather than opening with questions. It does NOT calculate margin or profitability - it has no rates, salaries or overhead model on a new project, and the economy judgement belongs to the PM with the RM. Writes planned HOURS and role labels only, behind a hard gate; never rates, salary or currency.
---

# a07-a08-roadmap-and-economy - A07 roadmap and role plan, then hand the economy to the RM

Covers A07 (initial roadmap, milestone schedule, preliminary resource plan - Confluence 4619207137) and the part of A08 (Confluence 4619206956) that the copilot can honestly do.

**Be clear about the boundary, because it is the whole shape of this skill.** The copilot helps the PM build a plan and a roadmap that make sense, and then FILLS the economy file's staffing tab with the planned roles and hours. It does NOT calculate the economy. On a new project it has no rates, no salaries and no validated overhead model, and producing a margin from assumed inputs is worse than not answering.

**The order matters and it is easy to get backwards.** The economy cannot be judged outside the P&L file - the PM and the RM look at the FILLED file and form a judgement from what it computes. So filling the file is not a hand-off courtesy, it is the prerequisite. Plan, then fill, then they judge. The copilot's job afterwards is to make sure the judgement comes back and gets recorded, because A09 needs it.

That does not mean staying silent until then. Concerns visible from the PLAN - hours over the WBS envelope, a peak month no single person can absorb, a role whose hours rest on an unvalidated assumption, oversight being absorbed rather than billed - get raised while the plan is being built, when changing it is still cheap.

Same pattern as `a10-staffing`: we do the two ends properly and say plainly that the middle is not ours.

Read the contract from `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`, sections A07 and A08. How our economy files are structured and how to write to one safely: `${CLAUDE_PLUGIN_ROOT}/references/pl-structure.md` - read it before touching a sheet. Roadmap heuristics: `references/planning-rules.md`. Output shapes: `references/output-shapes.md`. Templates: `${CLAUDE_PLUGIN_ROOT}/references/template-register.md`.

**The formal Resource Plan is NOT produced here.** Project Resource Plan 3.0 (Sheet `1WKcXz9W2BGrtRChNQ8DsZghcUFqvDcqbhOx8u1cDKJU`, instruction Confluence 4757127285) needs confirmed people, so it comes after staffing (A10). What A07 produces is the preliminary role-by-month plan - the standard's "Preliminary Project Resource Plan" is satisfied by that table, not by the template sheet. Say which one exists so nobody thinks the artifact is filed.

If the project has no economy file yet, the action is to REQUEST one from PMO RM. There is no self-serve template, by design.

## How this skill behaves - read first

**Read first, then propose, then ask.** Do not open with a list of questions - a PM who is asked to choose an hour basis before anyone has looked at the WBS is being made to do the copilot's homework. Read the material, form a view, present a plan with the defaults already chosen, and ask only about the calls that genuinely need the PM.

Two hard rules that never relax, and one hard gate:
- Never send to Sales or the client. The copilot drafts; the PM sends.
- The economy file is MONEY. It never enters the project brain and never leaves the sensitive Drive (no client currency, salaries, rates, margins or profit figures - worked and paid HOURS are fine anywhere).
- **The copilot does not operate sensitive financial data on its own initiative.** It writes planned hours and role labels. It does not write rates, does not convert currency, does not touch salary or tax residency, and does not look up or derive a rate from anywhere. If the PM explicitly wants a rate in, the PM supplies the number.

## Inputs
The validated scope + Required Roles + Critical Scope (A05), the WBS / estimate, the risks (A06), the contract window and timeline constraints, and `project-context.md`. If scope is not validated, route back to `a05-a06-scope-and-risks` - this plans on a validated scope, it does not re-validate.

## Stage 0 - Read the material, then propose a starting plan

Read before you ask: the A05 Required Roles List and critical scope (CS-ids), the WBS totals and which lines are largest, the A06 risks that bear on sequencing, the contract or SOW window, and anything `project-context.md` already records. Only then talk to the PM.

Present the three planning choices as a PROPOSAL with defaults, not as questions:

1. **Hour basis - default MAX.** The WBS max is the safe envelope for a T&M cap: the ceiling, not the expectation, with real burn landing under it. State that you are using max and offer min / mid / risk-blend if the PM wants a different envelope. Do not make them choose blind.
2. **Role set - propose one.** Build it from the A05 roles list and what the WBS actually contains, then ask only the calls you cannot settle from the material: whether lead or DM oversight is billed or absorbed (a commercial call), and whether QA sits as its own line or folds into the build. Those two genuinely need the PM; the rest you can read off the scope.
3. **Duration and ramp - propose from the window.** Take the contract or SOW duration, apply a ramp to a partial start month, and say where acceptance and UAT land. Ask if the window is wrong.

CHECKPOINT: "Here is what the scope and WBS suggest: [basis, role set, window, with the reasoning]. I have taken max hours as the envelope. Two things I cannot call from the material - [the billed-oversight question] and [the QA question]. Change anything, then I will build the roadmap."

## Stage 1 - A07: roadmap + role-by-month plan (iterate)

Build from the WBS, scope, timeline, risks, and the base rules in `references/planning-rules.md` (1 FTE ~168-176 usable h/month; ramp on a partial start month; front/back-load per role; QA at the tail; when hours run out against a cap, pull UAT/acceptance earlier rather than exceed the cap):

- Phases + milestone schedule + critical path (name the long pole). On a **Fixed-Price project over 3,500h** the critical path is a mandatory A07 output, documented on the milestone timeline (Critical Path Coverage: 100% of critical-chain activities identified before the timeline becomes the planning baseline). Ask the contract type and size before assuming it does not apply.
- Role x month hour table - this IS the preliminary resource plan at this stage. Keep month and role totals consistent when a role is added, removed or rescaled; make that cheap, because the composition WILL churn.
- Dependency order and the gating client dependencies.
- Map every CS-id from A05 onto the roadmap. An unmapped critical scope area is the thing the first metric exists to catch.

Iterate with the PM until the plan is realistic. Single-source any shared number (for example the PM's monthly split) - if it must appear in several artifacts, flag divergence rather than silently copying one version. This bit real projects.

**Keep a short options log as you iterate.** Each variant tried: basis, role mix, window, what it produced, why the PM rejected it. Three rounds in, nobody remembers what was already ruled out, and A08's mandatory "documented economy assumptions and concerns" is largely this log. It also saves A09 from re-litigating a decision that was already made.

Control metrics, with denominators stated:
- Critical Scope Roadmap Coverage = critical scope areas mapped to the roadmap / total critical scope areas x 100. Target 100% before resource planning and economy work. Name the CS-ids on both sides.
- Resource Timeline Coverage = roadmap or milestone areas with a defined role, seniority, allocation and timing / total roadmap areas requiring delivery resources x 100. Target >= 90% before stakeholder baseline validation.

The standard also expects these ON the timeline where applicable, and they are the ones PMs forget: demo / review / UAT / acceptance / release validation checkpoints, environment readiness points, and required client inputs, approvals, access or decisions.

**Placing them is not enough.** Per A07's escalation, a critical environment-readiness or client-input point needs a clarified RESPONSIBLE SIDE and an EXPECTED DATE before the roadmap becomes the planning baseline. A box on a chart with nobody's name against it is not a dependency, it is a hope. Give each one a side and a date, or mark it explicitly as unowned and route it.

CHECKPOINT: present the roadmap + role-by-month table + the two coverage numbers. "Here is the plan. Adjust roles, months or the basis - or shall I put the roles and hours into the economy file so you and the RM can work the economy on it?"

## Stage 2 - Fill the economy file with the planned hours (HARD GATE, only on explicit go)

This comes before any economy judgement, because the judgement is made ON the filled file. Only after the PM has seen and approved the plan. Follow the write sequence in `${CLAUDE_PLUGIN_ROOT}/references/pl-structure.md` exactly, in order:

1. Work on a dated COPY of the tab, not the live tab. Promoting the copy is a separate PM decision.
2. Confirm the active-month COLUMNS from a LIVE header read. Match each month code (726 = Jul-26, 826 = Aug, 926 = Sep) to its actual column LETTER. Never infer a column from a values-array index - index does not equal column, and an off-by-one invents a phantom month. This has actually happened; the story is in `pl-structure.md`.
3. Read raw values, not displayed ones, for anything you build on.
4. **Write BOTH hour rows, plus the role labels. Nothing else.** The role block carries Paid (billable) at offset +3 and Worked at offset +4 - fill both.

   The default is **paid = worked** for every role. Depart from it only where something explicitly says otherwise, and the usual case is a role that is not billable: a DM carried as oversight but absorbed rather than billed gets worked hours and ZERO paid. That is precisely the Stage 0 question about billed-or-absorbed, so the answer to it decides these cells. If the PM has not settled it, ask before writing rather than guessing - a wrongly billable DM changes the invoice total.

   Leave alone, always: **rates, currency conversion, salary, tax residency, grade.** Do not derive a rate, do not convert one, do not carry a conversion factor, and do not look one up. Those are finance-owned and the copilot has no business putting a number in any of them on its own initiative.

   If the PM explicitly wants a rate written, they supply the figure and the currency and you write exactly that, echoing it back first. Say plainly that you are not checking it, because you have nothing to check it against. The standard is explicit that rate, salary, location and exchange-rate data must be provided or confirmed by the responsible owner before any result is treated as reliable.

   A positive profit with a blank salary column is EXPECTED at plan stage - explain that rather than reporting it as a result.
5. **Verify the control totals, and one of them is the real check.** Total BILLABLE (paid) hours across every role must equal the plan's billable total, which is what the contract sold. If it does not tie, something is wrong - a non-billable role written as billable, a month written to the wrong column, or a role missed. Attribute it before moving on.

   Total WORKED hours may legitimately EXCEED total billable when a role is absorbed. That gap is expected and it is worth naming out loud, because it is the visible cost of carrying oversight unbilled.

   Also check each role's own total against the plan table. A total that is not roughly equal is a targeting bug, not rounding. Do not report profit or margin - that is not yours to report.
6. Report what you wrote: cells touched, billable and worked totals against the plan, the absorbed-hours gap if there is one, and any role-period from the plan that did NOT make it in.

Control metric: Resource-to-Economy Coverage = role-periods from the plan present in the economy file / total required role-periods x 100. Target 100% before the summary is used for baseline validation. Because the copilot places the hours, it can check this properly - count the role x month cells the plan requires, count what is in the sheet after the write, name any that are missing.

Fair-hours redistribution does NOT apply here. There are no actuals on a new project, and a zero-paid role at plan stage is a deliberate commercial choice rather than an unfairness to correct. Those rules in `pl-structure.md` are for A10 and for later work against real worked hours - though note the DM case reappears there, because a worked-but-unpaid desk is a participant in a later split.

CHECKPOINT (mandatory, no express-mode exception): "I will write these hours to [sheet / tab copy], columns [letters, confirmed from a live header read]. Paid equals worked for every role except [role], which is absorbed and gets zero paid. Billable total [n]h, which matches the plan and the contract. Rates, salary, residency and grade untouched. Here are the numbers [show them]. Confirm and I will write, then re-read the totals to prove it tied."

Write only on an explicit yes on these specific numbers. If the PM would rather paste them in themselves, that is a perfectly good outcome - hand over a clean table with the target cells named.

## Stage 3 - A08: the economy judgement (PM + RM, on the filled file)

Now the file computes something and the PM and the RM can read it. The copilot does not produce the verdict. What it does here is make sure the judgement actually happens, is complete, and comes back.

**Assemble the assumptions and concerns first.** A08's "Documented Economy Assumptions / Concerns" is a MANDATORY output where applicable and the one most likely to be skipped. It is largely already written - the options log from Stage 1, plus A05's flagged estimate assumptions. Assemble rather than starting fresh, and note explicitly any place the plan depends on unrealistic staffing, seniority, allocation or UNPAID work. The absorbed-oversight decision is exactly that kind of assumption and the standard makes it a revise-before-validation trigger.

**Name what has to come back**, because A09 needs it: the classification in the standard's own vocabulary - healthy, questionable, risky, negative, or acceptable only with strategic justification - plus any concerns raised, who worked it and when.

**Two escalations that are the PM's to trigger and easy to miss:**
- An economy below target, negative, OR materially worse than pre-sale expectations escalates to Head of PMO / Delivery management BEFORE baseline validation completes. Ask explicitly how the filled file compares to what pre-sale assumed - a distinct check from "does it fit the cap", and the one that catches a project degrading quietly between sale and start.
- Low profitability justified by strategic value requires the reason DOCUMENTED before acceptance, and someone NAMED who owns realising that value. Feeds A09.

If the verdict is weak, loop back to Stage 1 and reshape the plan - fewer hours, different mix, tighter window, a different billed-or-absorbed call - then refill and re-judge. Do not push a plan the PM does not believe in.

CHECKPOINT: "The file is filled and tied. Over to you and the RM for the economy read. When you have it, tell me the classification and any concerns and I will record them for A09 - the gate cannot run without them."

## Outputs and filing
- A07 roadmap + milestone schedule + role-by-month plan - markdown / working note in the project folder (General/PM); the shareable roadmap can be a native Google Doc. HOURS are fine to share.
- The options log and the economy assumptions / concerns - project folder. No figures.
- Planned hours in the economy file's staffing tab - the sensitive Drive ONLY (Economy chat / sensitive storage), never the project folder or the brain, never a link from either.
- EVM Baseline (Planned Value), **Fixed-Price only** - mandatory at A08 since Sep 2026, tracked afterwards as SPI = EV / PV and CPI = EV / AC at every economy recalculation. PV is normally a money figure, so it lives with the economy in the Sensitive folder and this skill does not compute it. Check it exists for an FP project and say so if not; offer a PV curve in HOURS from the role-by-month plan only if the PM wants one. On T&M it is N/A, not missing. Whether PMO wants PV in hours or money is an open question - I am not sure what we usually do here.
- NOT produced here: the formal Project Resource Plan 3.0 (needs confirmed people, so post-A10), and the economy calculation itself (PM + RM).

## Close-out

Route what stays open: unlocked scope that could move hours - flag it, do not bake it in; cap, rate and advance blanks -> PMO / Sales / contracts; staffing of the planned roles -> A10, which is also where the formal Resource Plan and any fair-hours split belong.

**Make sure the economy outcome comes back.** The PM and the RM produce it, but A09 cannot run without it, so record in `project-context.md` when it lands: the classification in the standard's vocabulary, who worked it, the date, and any concerns raised. A weak-but-taken economy is recorded with its justification AND the named owner of realising that value - that is the record someone will want in six months, and it is A09's input, not a footnote.

If the economy has not come back by the time the PM asks about A09, say so plainly: the gate needs it.

Then write the residue down, and say in one line that you did:

- Anything that needs DOING goes in `<workspace>/pm-tasks.md`, tagged with the project - the PM's actions, what is waiting on someone else, what you routed elsewhere. Actions that only ever exist in this conversation are lost when it ends, and the PM re-derives them next week.
- Anything durable you learned about the project goes in `<project folder>/project-context.md` - decisions and who made them, people, links, and what is still open.
- **The project brain gets the ROADMAP and nothing else from this skill. Read that line twice.** The roadmap, its milestones and the dates belong in the brain - offer them via `project-brain` (feed mode). The Resource Plan and the P&L do NOT, ever, in any form: no link, no summary, no "just the totals", no redacted copy. Money lives in the Sensitive folder and the Economy chat, and this is the step that produces the money, so this is where the rule gets tested.
  - The trap worth naming: the roadmap and the resource plan are produced in the same breath here, and the plan is the natural thing to attach when you have just finished it. Planned HOURS and role labels are fine in the brain. Rates, salaries, margins and any figure with a currency on it are not, and a plan tab that carries them is a money artifact whatever else is on it. When in doubt, offer the roadmap and say plainly that the economy stays out.
- Anything the copilot got wrong, or asked for and could not do, goes in `<workspace>/copilot-feedback.md`.
