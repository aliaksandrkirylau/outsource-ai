---
name: a03-contract-commitments
description: Read the signed contract and work out what it actually commits the project to, then check that against what the project has planned. Use when a contract or SOW is signed or nearly signed - "review the contract", "what did we commit to", "what does the contract oblige us to do", "check the contract against our plan", "contract commitments", "does the contract match our scope", "what are our obligations here", "read the SOW", "A03", "contractual baseline". Produces a Commitments Register (delivery obligations, client obligations, acceptance rules, reporting duties, constraints) and an alignment check against the handover, scope, roadmap and economy. Contract text goes in a separate confidential notebook, never the project brain. The copilot reads and flags; it does not give legal advice.
---

# a03-contract-commitments - what did we actually sign up to

The PMO standard has this as step A03 (Confluence 5142544653), accountable to the PM. Copilot releases before 0.45.0 called it A02.5. Read the contract section of `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md` for the full contract, which includes an agreed-versus-signed version comparison this skill deliberately does not do.

**What this skill covers:** reading the ready contract, extracting what it commits us to, and checking that against what the project already believes. That is the part a PM needs in order to run the project.

**What it does not cover:** producing, negotiating or version-comparing the contract. The contract preparation group drafts it, Legal signs it, and the signed version is requested through Head PMO.

Be straight about the consequence: the agreed-versus-signed **Contract Version Comparison Result is a MANDATORY output of this step**, and this skill does not produce it. So A03 can be ADVANCED here but not closed as complete. Say that rather than letting a PM think the step is done, and point them at contracts and PMO leadership for the comparison itself.

And if a difference between the agreed and signed versions comes up - the PM mentions one, or you notice the signed text does not match what the handover described - **that is an escalation case, not a discussion topic.** The standard is explicit that a signed-versus-agreed difference is never silently accepted as the baseline. Route it to the contract preparation group plus Head PMO or Deputy Head PMO, and say plainly that it needs to be resolved rather than absorbed.

## Two hard rules

**Contract text goes in a separate confidential container.** Never the shared project brain, never the common project folder, never a chat the wider team can read. Same sensitivity class as money. If the PM asks you to add the contract to the project brain, refuse and explain why - the standard is explicit and this is the rule most likely to be broken by accident.

**The copilot is not a lawyer and does not read like one.** It extracts what a clause obliges the project to DO, in delivery terms. It does not interpret legal enforceability, advise on liability, or tell the PM whether a term is acceptable. Anything that smells like a legal question - indemnity, liability caps, termination consequences, IP ownership disputes, jurisdiction - gets named and routed to the contracts team, not answered. Say "this needs contracts to look at" rather than having a view.

If the PM has no contract access (probation or another restriction), the standard says the assigned buddy, PM Lead or manager does the review. Check that first rather than working around it.

## Stage 0 - What we have and what we are checking against

Confirm: which contract document, and is it the signed version or a draft. A draft is worth reading but its commitments are provisional - say which one you are working from in every output.

Then gather what the project already believes, because the alignment check is only as good as this:
- The A01 handover brief and the assumptions and commitments list.
- The A04 project description, if it exists.
- The A05 validated scope and acceptance criteria.
- The A07 roadmap and milestone dates.
- The A08 economy, for cap and payment-trigger structure (existence and structure only, no figures into anything shareable).
- The A06 risks.

If most of those do not exist yet, say so. Reading the contract early is still useful - it becomes an input to those steps rather than a check on them. Just be clear which direction you are working in.

CHECKPOINT: "Reading [document, signed/draft] against [what exists]. Contract text stays in a confidential container and out of the project brain. OK?"

## Stage 1 - Extract the commitments

Go through the contract and write down what it obliges someone to do. Not a summary of the contract - a register of obligations, each traceable to a clause.

Cover these, because they are the ones that bite:

**What we deliver.** Scope and deliverables as the contract defines them - which may be narrower, broader or differently worded than the WBS. Note the wording, not your paraphrase, where it matters.

**When, and what happens if not.** Milestone dates, delivery windows, and any consequence attached to missing them. A date with a consequence is a different animal from a date in a plan.

**How it gets accepted.** The acceptance process as contracted: who accepts, on what basis, in what timeframe, and what happens on silence. Many contracts have a review period after which work is deemed accepted - that is a fact the PM needs before the first milestone, not after.

**What the client owes us.** Access, data, environments, decisions, review turnaround, named contacts, their own dependencies. This is the most commonly missed category and the most useful - a client obligation you did not know about is a delay you cannot defend.

**What we must report and when.** Status reports, timesheets, burn reporting, demo cadence, any contractually required format.

**Constraints on how we work.** Named people, team locations, exclusivity, subcontractor restrictions, security or compliance requirements, tooling the client mandates, working hours or time zones.

**Change and budget control as contracted.** How scope changes are handled, who approves, and for T&M what the cap is and what notification the contract requires as it is approached.

**Post-delivery obligations.** Warranty, support period, defect response times, handover of source and documentation, IP and licence terms as they affect what we must produce.

For each: what the obligation is, who owes it (us or the client), the trigger or date, the clause reference, and a plain-language note on what it means in practice.

On money: record the obligation and its trigger, not the amount. "Milestone 2 acceptance triggers invoicing" is a delivery fact the PM needs. The figure belongs in the Sensitive folder.

CHECKPOINT: present the register. "Here is what I read the contract as committing us to, and what it commits the client to. Anything I have misread, and anything you know that is not written here?"

## Stage 2 - Check it against what the project believes

This is the comparison a PM actually needs in order to run the project. Go obligation by obligation against the project's own artifacts and sort each into one of four buckets:

- **Aligned.** The contract says it and the plan reflects it. Say so briefly; most items land here and do not need discussion.
- **In the contract but not in our plan.** A commitment nobody has planned for. These are the findings. A warranty period nobody budgeted, a report nobody scheduled, an environment nobody costed.
- **In our plan but not in the contract.** Usually harmless, occasionally important - work we assumed we would do that we are not actually obliged to do, which is a scope conversation and sometimes a saving.
- **Contradictory.** The contract says one thing and the plan or the handover says another. Dates, scope wording and acceptance rules are where this shows up. Every one of these needs resolving before the A09 gate.

Pay particular attention to:
- Dates in the contract versus dates in the roadmap.
- Contracted acceptance criteria versus the observable criteria written at A05.
- Contract type versus how the economy was actually built - a fixed-price contract planned as if it were T&M is a serious finding.
- Assumptions recorded at A01 that the contract does not support.

CHECKPOINT: the four buckets, worst first. "These [N] are in the contract and not in our plan, and these [M] contradict what we assumed. Agree with the read?"

## Stage 3 - Route, record, and say what it changes

Nothing here gets resolved in this skill. Each finding goes somewhere:

- Scope differences -> A05, and the CR process if the contract is already signed.
- New risks and obligations with no owner -> A06.
- Date conflicts -> A07.
- Anything affecting cap, payment triggers or the commercial model -> A08 and the Economy chat.
- Anything material and unresolved -> the A09 baseline gate, as an open point with an owner.
- Anything legal -> the contracts team. Named, not answered.

### Propagate the operating parameters - do not leave them in the register

Most of the register is reference material. A handful of items are not: they are parameters the project has to OPERATE by, and a register nobody re-reads does not protect anyone in month three. Pull these out and put them where the PM actually works:

| Parameter | Where it has to land |
|---|---|
| **Deemed-acceptance window** - submit, N days of silence, accepted | `project-context.md` as a standing fact, AND `pm-tasks.md` with the first real deadline the moment a milestone is submitted |
| Client review / turnaround obligations - they owe a response in N days | the Communication Plan (it sets the cadence) and `project-context.md` |
| Cap notification thresholds - e.g. notify at 70% and 85% | the Communication Plan, and a watch item in `pm-tasks.md`. Also the kick-off deck's commercial slide |
| Contractually required reporting cadence and format | the Communication Plan. A contracted report is not a nice-to-have rhythm |
| Milestone dates that carry a CONSEQUENCE | the roadmap, marked as contractual rather than planned |
| Warranty / support window and defect response times | `project-context.md`, and A07 if it extends past the current plan |
| Named-people, location or exclusivity constraints | `project-context.md`, and A10 before staffing goes out |
| Invoicing triggers (the trigger, never the amount) | `project-context.md` |

The deemed-acceptance window is the one to be most deliberate about. It is the clause that turns into "we submitted on the 3rd, they went quiet, and it was accepted on the 17th whether anyone noticed or not" - which cuts both ways and is only useful if the PM knows the date before it passes.

Say in one line what you propagated and where. If a parameter belongs in the Communication Plan and that plan does not exist yet, note it for A11 rather than dropping it.

**Record the outcome in Contract Chat.** That is where the standard says the review lands. Draft the message; the PM posts it. Include who performed the review and their access status - the standard asks for review responsibility to be defined, and on a project where the PM had no contract access and a buddy or PM Lead did it, that matters.

**File the Commitments Register** in the project folder - and note carefully: the REGISTER can live with the project documents, because it is your own summary of obligations in delivery terms. The CONTRACT ITSELF cannot. Keep that distinction; it is what makes the register useful to the team without leaking the document.

The standard defines no control metric for this step. Do not invent one - say it is not yet defined and report coverage plainly instead: how many obligations extracted, how many aligned, how many open.

CHECKPOINT: the routed findings, the drafted Contract Chat message, and the register ready to file.

## Outputs

Named against the standard's own three outputs, so the work is recognisable to anyone checking A03 rather than reading this skill:

| Standard's output | What this skill produces |
|---|---|
| 1. Contract Version Comparison Result `[M]` | **NOT PRODUCED** - contracts and PMO leadership own it. A03 stays open until it exists |
| 2. Contractual Baseline Review Confirmation | the Contract Chat message recording the review outcome, who performed it and their access status - drafted for the PM to post |
| 3. Contract Discrepancy / Clarification Items `[M]` | the alignment findings in four buckets, each routed with an owner, worst first |

Plus, ours rather than the standard's:
- **Commitments Register** - delivery obligations, client obligations, acceptance rules, reporting duties, constraints, post-delivery obligations. Filed with the project documents. The contract itself is not.
- **Operating parameters propagated** to `project-context.md`, the Communication Plan, the roadmap and `pm-tasks.md`, with a one-line note of what went where.
- Open items carried to the A09 gate.

## Close-out
Say plainly what is unresolved and what it blocks. A contradiction between the contract and the plan that reaches kick-off unresolved becomes an argument in month three, and the register is what makes it findable before then.

Say too that A03 is not closed while the version comparison is outstanding, and name who owns getting it.

If the contract turned out to be a draft rather than the signed version, say that in every output. A commitments register built on a draft is a working document, not a baseline.

Then write the residue down, and say in one line that you did:

- Anything that needs DOING goes in `<workspace>/pm-tasks.md`, tagged with the project - the PM's actions, what is waiting on someone else, what you routed elsewhere. Actions that only ever exist in this conversation are lost when it ends, and the PM re-derives them next week.
- Anything durable you learned about the project goes in `<project folder>/project-context.md` - decisions and who made them, people, links, and what is still open.
- **NOTHING from this skill goes in the project brain. This is the exception, and it is absolute.** Contract text lives only in the separate confidential notebook, and the Commitments Register is derived from the contract and carries its terms - so it follows the contract, not the project. The always-on rule says an artifact produced at a checkpoint gets offered to the brain; this skill overrides it. Do not offer, do not ask, do not upload a redacted version. If the PM asks for it in the brain, say why it cannot go there. The brain is shared with the project team; the contract container is not, and that difference is the whole point.
- Anything the copilot got wrong, or asked for and could not do, goes in `<workspace>/copilot-feedback.md`.
