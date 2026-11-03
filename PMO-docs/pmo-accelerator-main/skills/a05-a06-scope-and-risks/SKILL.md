---
name: a05-a06-scope-and-risks
description: Interrogates the pre-sale scope, estimates and economy for realism (A05), then builds the project's first risk register out of what that turns up (A06). Use when the sold estimate looks thin and the PM has to say so before committing to it, when nobody has compared what was sold against what the team can actually deliver, or when a project about to start has no risk register at all - "validate the scope", "check the estimates", "are we underestimating", "sold vs what we can actually deliver", "sanity-check the pre-sale", "what could go wrong on this project". It questions the assumptions behind the numbers before producing any. NOT for adding or closing one risk on a running project, and NOT for reviewing a register that already exists - both of those are `risk-register`, which owns the register's IDs and conventions and which this skill calls to build the first one. The copilot interrogates and drafts; the PM owns every call.
---

# a05-a06-scope-and-risks - A05 scope/estimate realism + A06 risks

Runs two Standard A steps that share source material: A05 (validate pre-sale scope, estimates, economy, delivery approach - Confluence 4619206785) and A06 (initial risks, dependencies, blockers, assumption gaps - Confluence 4619206806). The realism check and the risk register are two views of the same interrogation, so one staged skill produces both.

Steps are the contract; this skill is one cluster over two steps. Each output is graded against its own step's Verification Criteria + Control Metrics. Read the contract from `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`, sections A05 and A06. Templates: `${CLAUDE_PLUGIN_ROOT}/references/template-register.md`. Output SHAPES in `references/output-shapes.md`.

Note the standard is explicit that A05 does NOT validate profitability - that is A08, after the roadmap and resource plan exist. Do not let a scope conversation turn into a margin conversation here.

## How this skill behaves - read first

A05 is ADVISOR-FIRST, and this is the important difference from the generator skills. Do not open by producing a re-estimate. Interrogate first: surface the assumptions behind the biggest estimate lines and the sold-vs-deliverable gaps, one line of questioning at a time, until the ambiguity is low enough that a realism judgement means something. Producing confident numbers on top of unexamined assumptions is exactly the failure this step exists to catch. Then draft the A05 outputs, then A06.

Staged: A05 interrogate + draft, checkpoint, A06, checkpoint. STOP and show before proceeding. Two hard rules that never relax:
- Never write to or share a persistent store (brain, shared Sheet, P&L, Jira) without showing what and getting a yes.
- Never send to Sales or the client. Draft the clarification questions; the PM asks.

## Inputs
The A01 handover brief + candidate risks, the A04 description if done, the project brain, and any pre-sale estimate / WBS / P&L reference. If A01 has not run, route back to `a01-presale-handover` - this validates the harvest, it does not re-harvest.

## Stage 1 - A05: validate scope, estimates, economy (advisor-first)

Interrogate before you produce:
- What does the sold scope actually COMMIT us to vs what was described? Name every sold-vs-deliverable gap.
- Which estimate lines are largest, and what assumption is each resting on? Probe those assumptions hardest - the biggest lines hide the biggest risk (on Alchemy the two largest ML lines silently assumed analysis-ready data that did not exist; the value was catching that, not re-adding hours).
- Ownership / liability lens: who owns the commercial rules, the data, acceptance, and storage? A missing owner is a liability, not just a gap - route it to A06.

Then draft the A05 outputs (the standard flags both as mandatory):
- Required Project Roles List (role, seniority, why needed / which critical scope). Role vocabulary: BA, SA, Architect, Tech Lead, FE, BE, QA, DevOps, Designer, Data, Mobile, ML, other.
- A WORK-CATEGORY completeness sweep, which is a different question from the role list and a named verification criterion. Walk the delivery categories and mark each present in the WBS, not applicable with a reason, or MISSING: analysis and BA, architecture and design, UI/UX, implementation per component, integrations, data work and migration, QA and test design, automation, DevOps and environments, security, documentation, deployment and release, UAT support, handover and training, PM and coordination. Having a QA role named is not the same as having QA work estimated - that gap is exactly what "the WBS does not cover what is needed to deliver the expected result" means in the escalation.
- Validated WBS / Scope Baseline with high-level Acceptance Criteria and estimations. The High-Level Critical Scope with Acceptance Criteria is part of one mandatory artifact with the WBS (filed in Confluence - 5 is the Stakeholder Register) - each critical area gets an OBSERVABLE acceptance criterion. There is no dedicated template for it; the WBS templates are the nearest thing (Sheet `19P47nYbey6oKLuXfEeb8bojojrmTfxPO2aYotTa9Hp4` for fixed price, `12B4wRsuI_aEmttlcZN3mMtK5t6dk3Ot3ikBNtQRDX3k` optimised). Say that plainly rather than implying a house format exists.
- Validation summary: sold-vs-context mapping, estimate realism (with the flagged assumptions), roles/capability check, delivery-approach fit.
- Re-estimation / clarification needs, each routed to an owner (client / Sales / tech lead / kickoff).
- WHO REVIEWED THE ESTIMATES, recorded by name and date. "Estimates reviewed by relevant team members or technical experts" is a verification criterion, and it is the whole difference between the copilot's read and an expert's. If no technical expert has looked at them yet, the criterion is NOT met - say so and make the review an action with an owner rather than letting your own analysis stand in for it.

Number the critical scope areas `CS-1`, `CS-2` and so on, and keep those ids stable. Later documents cite them - on the real Alchemy run A05's own coverage caveat points at CS-4, and the roadmap and acceptance work reference them again.

If a contract is signed, connect any contractual delivery mismatch back to the A03 contract review outcome (page 5142544653) rather than treating it as a fresh finding.

Control metric: Critical Scope Estimate Coverage = critical scope areas with a usable estimate / total critical scope areas x 100. Target >= 80% before roadmap and resource planning. Count only project-level critical scope areas identified in this step. List the areas on both sides of the ratio. Flag any critical area whose estimate rests on an unvalidated assumption even when it counts as covered - a covered-but-unsound estimate is the failure this step exists to catch.

CHECKPOINT: present the interrogation findings + the A05 outputs + the coverage number. "Here is what the sold scope commits us to, where I think we are thin or underestimated, and the realism read. Agree before I turn this into the risk register (A06)?"

## Stage 2 - A06: risk register + issue/blocker log

**The register itself is owned by the `risk-register` skill. Use it - do not rebuild the register here.** Call it in `create` mode and hand it the A01 candidate risks, the A05 findings from Stage 1, and any existing risk log. It holds the ID conventions, the row shape, the risk-versus-issue split, the traceability and dispositions rule, the PMO Risk Library pass, the response vocabulary, and both control metrics with the rules for counting them.

There is exactly one definition of how a register works, and it is over there. A second copy in this file would go stale the first time one of them changed, and neither would say which was right.

What belongs to THIS step, and what you are accountable for at the checkpoint below:

- **Hand over good source material.** The register is only as good as the distillation feeding it, and Stage 1 is where that comes from. Candidates the interrogation raised but did not resolve are risks; say so rather than dropping them.
- **Update the assumptions and constraints that the validation changed.** That is an A05 output, not a register row, and nothing else will do it.
- **Report both control metrics at the checkpoint.** `risk-register` computes them; A06 is the step that has to state them, because they gate the roadmap and resource plan that come next.
- **Say what routes onward.** A06 findings feed A07/A08 and the A09 gate. A risk that changes the plan is a routing decision, not just a row.

If `risk-register` is not available for any reason, say so rather than improvising a register from memory - the conventions in it are cited by other documents, and an invented format breaks them.

CHECKPOINT: present the risk register + issue/blocker log + the two metrics. "Here are the live risks, the active blockers, and the coverage. Good to finalize the validation pack?"

## Outputs and filing
- Required Project Roles List and the validation summary - working markdown in the project folder (General/PM).
- WBS / Critical Scope Baseline with Acceptance Criteria and Estimates - one mandatory artifact since Sep 2026: the critical scope and acceptance criteria in CONFLUENCE, the estimates in a SPREADSHEET.
- Risk Register - JIRA or CONFLUENCE (a mandatory starting artifact). Issue / Blocker log - the Issue Log Sheet in the Sensitive folder.
- Opportunity & Internal Risk Register - a SEPARATE mandatory artifact since Sep 2026, built in the same pass as the Risk Register. Opportunities (upsell, scope expansion, reference or case-study potential, process improvement) and Innowise-only risks (profitability, internal staffing, anything a client must not read). INTERNAL ONLY: never in a client-facing space, never merged into the client-visible Risk Register. The checklist has no template for it yet - draft it with the register's ID discipline and say it is our draft.
- Gated before any brain push. No money, no contract text in the brain.

## Close-out

**A gap that may change what was sold is a CR candidate and is NEVER absorbed into baseline scope.** This is the sharpest rule in A06's escalation and it is the default failure mode of a helpful PM: the scope grew a little, the estimate can probably carry it, so it quietly becomes part of the plan and nobody is told. Any scope, budget, timeline or acceptance gap that could change sold commitments gets recorded as a clarification item or a CR candidate with an owner, and the PM decides whether it goes to the client. Absorbing it silently is the one outcome this step exists to prevent.

Escalation paths the standard names, so use them rather than filing everything as an ordinary gap:
- A critical issue or blocker that prevents roadmap planning, resource planning, economy calculation, customer validation or acceptance is escalated BEFORE that step is called complete.
- A material risk to profitability, contractual obligations, feasibility, the client relationship or strategic value goes to Head of PMO / Delivery management before formal acceptance. Say that out loud when you see one; it is not a line item.
- If the team concludes the sold scope cannot be delivered with the proposed approach, that escalates to Delivery, Account and Sales - it is not a re-estimate.

Route what stays open: estimate/scope realism -> the client/kickoff and A07/A08/A09; risks carry their own owners; ownership/liability gaps -> A02 + PMO; a contractual delivery mismatch connects back to the A03 review rather than being raised fresh. Significant estimate assumptions must stay VISIBLE into roadmap, resource, risk and economy planning - hand them forward explicitly, do not let them die in this document.

A thin or skipped part is justified-and-recorded, never a silent pass. A sub-80% scope coverage or an uncovered critical risk is surfaced, not buried.

Then write the residue down, and say in one line that you did:

- Anything that needs DOING goes in `<workspace>/pm-tasks.md`, tagged with the project - the PM's actions, what is waiting on someone else, what you routed elsewhere. Actions that only ever exist in this conversation are lost when it ends, and the PM re-derives them next week.
- Anything durable you learned about the project goes in `<project folder>/project-context.md` - decisions and who made them, people, links, and what is still open.
- **The project brain gets the risk register, the critical scope and the validation findings.** Offer them at the closing checkpoint via `project-brain` (feed mode). These are the highest-value things this skill produces for a later query, because the questions they answer - what did we think could go wrong, what did we agree was in scope - get asked constantly and are otherwise reconstructed from memory. Include the dispositions table: the record of which candidate risks were dropped and why is the part that survives an audit, and it is worthless if it only exists in one chat.
  - Two format points, from `${CLAUDE_PLUGIN_ROOT}/references/pmo-conventions.md`. The WBS is a spreadsheet, and Sheets pushed via MCP do not sync reliably - so put in a link plus a short summary note, not the file, and do not report a Sheet upload as done. Estimates in HOURS are fine in the brain; anything that turns them into money is not.
- Anything the copilot got wrong, or asked for and could not do, goes in `<workspace>/copilot-feedback.md`.
