---
name: a02-a04-stakeholders-and-description
description: Builds the stakeholder and communication register (A02) and the project description (A04) out of material a handover already harvested. Use when nobody can say who approves what or who to go to for a decision, when a newcomer or a client asks what this project actually is and there is no written answer, or when a pile of harvested handover material needs turning into something readable - "build the stakeholder register", "who are the actors on this project", "who signs off on what", "map decision ownership", "write the project description", "flesh out the project context", "do A02 and A04". Both outputs are distillation from the same source material, which is why they are one skill; it needs a handover (A01) to have run first. The copilot drafts; the PM reviews and owns every call.
---

# a02-a04-stakeholders-and-description - A02 stakeholders + A04 description in one pass

Runs two Standard A steps that share the same source material: A02 (actors, ownership, communication channels - Confluence 4619206702) and A04 (describe the project + define context - Confluence 4619206765). On a real project these are distillation from the A01 harvest, the discovery material, and the project brain - not new analysis - so a single staged skill produces both, stopping between them for review.

Steps are the contract; this skill is one cluster over two steps. Each output is still graded against its own step's Verification Criteria + Control Metrics.

The control contract lives in the standard, not in this file. Read it from `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`, sections A02 and A04. Templates: `${CLAUDE_PLUGIN_ROOT}/references/template-register.md`. Filing rules: `${CLAUDE_PLUGIN_ROOT}/references/pmo-conventions.md`. Output SHAPES (skeletons only, not the contract) are in `references/output-shapes.md`.

Filing matters here and we used to get it wrong: per the artifacts checklist, the Stakeholder Register and the Project Description are CONFLUENCE artifacts. Markdown in the project folder is the working draft; the Confluence page is what counts as the artifact. Say which one you have produced.

## How this skill behaves - read first

Three stages: A02, then the A03 contract checkpoint, then A04. STOP and show each output before moving on. Two hard rules that never relax:
- Never write to or share a persistent store (project brain, shared Sheet, Jira) without showing exactly what and getting a yes.
- Never send to Sales or the client. Where a gap needs a client/Sales answer, draft the question; the PM asks.

## Inputs

The A01 handover brief, the project brain (or the harvested material), and the discovery/call material if any. If A01 has not run, say so and route back to `a01-presale-handover` - this skill builds ON the harvest, it does not re-harvest.

**Look for what exists before drafting anything.** Both of this skill's outputs are the kind of document a project often already has in some form:

- `project-context.md` lists which step outputs exist and where they were filed. Read it first.
- A01 usually leaves a DRAFT stakeholder register behind - it is a declared A01 output. Start from that draft; do not rebuild it from the harvest a second time. On the real Alchemy run the A01 checklist cited a draft matrix with client-side email gaps already flagged, and rebuilding would have lost that work.
- Then the project folder, then Drive and Confluence under the project name and every alias. A Project Description may exist as a charter, a vision-and-scope, or a page someone wrote months ago.

Update what you find and say what changed. Two stakeholder registers that disagree is a worse outcome than one that is out of date.

## Stage 1 - A02: stakeholders, ownership, communication

Assemble from the harvest + brain:
- Client-side stakeholders: person, role, area / ownership, status. Flag EMAIL/CONTACT MISSING explicitly per person.
- Two client-side roles the standard names separately, because they are the ones that block: the **Client Sponsor / Business Owner**, and the **Product Owner / requirements owner**. Each is defined or explicitly marked unknown - never just absent from the table. An unclear requirements owner means scope cannot be treated as stable, and that is a statement worth making out loud rather than leaving implied.
- Internal stakeholders (Innowise): PM, DM, tech/AI lead, BA, account/sales, PMO approver, resource managers, to-staff roles.
- Internal DEPARTMENTS expected to supply people or expertise, which is a different question from which people are named. The standard makes it an ordered dependency: resolve technical delivery ownership FIRST, then with that owner work out which departments supply expertise, and only then go near resource planning. Unresolved technical delivery ownership blocks delivery start, so if it is open, say that plainly rather than listing it as one gap among many.
- Chat membership, not just chat existence: whether the PM is in each chat AND whether the internal stakeholders who need to be there are. Missing participants get documented.
- Decision-ownership map: for each decision area (scope/CR, acceptance, budget/cap, commercial rule values, technical direction, technical-delivery supervision) name the client-side owner and the internal owner.
- Internal communication channels: channel, purpose, id/link, PM-added yes/no. Capture the chat lifecycle (pre-sale becomes common on signing; strategy/others auto-created on Closed Won; internal is PM-created) so a missing chat is explained, not just flagged.
- Technical-ownership check: name who owns the technical decision and is accountable; if nobody owns it and the PM cannot resolve it, mark it to escalate to PMO.
- Gaps list: every missing actor, email, or ownership question, each with an owner (Sales / Account / client-side).

Template: Stakeholder Register (Confluence 2900164811). RACI if the project needs one (Confluence 5057675462 + its Sheet). Chat types and their required pins are in `pmo-conventions.md` - a missing chat usually has a lifecycle explanation, so report the explanation, not just the gap.

Two things that caught real projects, do them:
- Re-scan the discovery TRANSCRIPTS, not just the chat - client-side names often surface only in calls (on Alchemy, the AI-governance and customer-engagement contacts appeared only in the calls, never in the chat).
- Compute the two A02 control metrics. **Build the table first and let the number fall out of it** - the table is the useful thing and the percentage is only a summary. These numbers exist to help the PM judge whether they can go into kick-off, not to grade anyone, so do not optimise them and do not present them as an assessment of the PM's work.

  One row per decision area: `area | client-side owner | internal owner | confirmed / gap / N-A`. Then the ratio is countable by anyone reading the register, and a lead who challenges the number can see the rows. A prose parenthetical is not a basis - on the real Alchemy run both indices were reported as round percentages that cannot be reconstructed from the sentence explaining them.

  - Client Decision Clarity Index = confirmed client-side decision areas / total relevant client-side decision areas x 100. Target 70-80% before kick-off. An unknown counts toward the numerator ONLY if it is documented as a clarification gap with an owner.
  - Internal Ownership Readiness Index = (confirmed internal ownership areas + explicitly not-applicable areas) / total relevant areas x 100. Required 100% before client kick-off. Note the mechanic, because it is easy to read the formula wrong: an explicit N-A counts in the NUMERATOR. An area where the honest answer is "nobody owns this and that is correct" is READY, not a gap - Alchemy's commercial-rule values are exactly that case, applied by the team and owned by the client. Mark it N-A with the reason instead of leaving it blank.

  Report both as `k of n` next to the percentage. There is no scorer for A02, so the table IS the audit trail.

CHECKPOINT: present the A02 register + the two indices + the gaps. "Here are the actors, ownership, channels and gaps, with the two readiness numbers. Anything wrong or missing before we look at the contract (A03)?"

## Stage 2 - The A03 contract checkpoint (do not skip past this)

A03 sits between A02 and A04 in the standard, and the ordering is not decorative: the contract review happens "after actors and channels are identified, before the project description", and its findings "must flow into the project description, scope and estimate validation, risks, roadmap, economy, baseline validation and kick-off preparation." Writing A04 first means building the description before the thing that is supposed to feed it.

So ask, and act on the answer:

- **No contract signed yet.** Note that A03 is open and carry on to A04. The description is provisional until the contract lands, and say so in it.
- **Contract signed, and a Commitments Register already exists.** Read it before writing A04, and make the description consistent with what was actually committed rather than with the proposal.
- **Contract signed, nothing reviewed.** STOP here and offer `a03-contract-commitments`. Do not write A04 on the proposal and quietly hope the contract matches - a signed-versus-agreed difference is an escalation case in the standard, never something to absorb silently. If the PM would rather push on, that is their call: record it as skip-with-justification and flag in A04 that its basis is the proposal, not the contract.

Contract text goes in a SEPARATE confidential container, never the project brain. Same sensitivity as money. The standard defines no control metric for this step - report it as not yet defined rather than inventing one.

CHECKPOINT: "Contract status is [X], so [route to a03 / carry on with the description]. Agreed?"

## Stage 3 - A04: describe the project + context

Consolidate from the A01 problem statement + Vision & Scope + the brain:
- Reuse the A01 client problem statement VERBATIM - the pain, not the deliverable. The description restates the problem in pain/outcome terms; a feature list is not the goal.
- Sections: problem / goals / outcomes / assumptions / constraints / value (see the skeleton).
- The key judgement: split the MVP's observable success criteria from the client's business north-star targets, and mark the north-star numbers non-committal, matching the SOW. Do not let aspirational business metrics read as delivery commitments.
- Feed-forward: note what A04 hands to A05 (validation) and the A09 baseline package.

Template: Project Description (Confluence 2886959244, marked `[Need Update]`). The Project Charter page is a filled example, not a blank - do not hand it to a PM as a template.

Compute both A04 control metrics. Same principle as A02: these help the PM judge whether the description is solid enough to validate scope and plan against, not grade the document. Count, do not estimate.

**Structure the document so the metric is countable by reading it.** The eight denominator areas become the document's numbered sections, in order, the way the real Alchemy description does it. Then "6 of 8 documented" is visible rather than asserted.

- Project Definition Maturity Index = confirmed core definition areas / total relevant core areas x 100. Target >= 80%. The standard FIXES the denominator at 8: client problem / pain, project goals, expected outcomes, high-level scope context, success criteria, key assumptions, key constraints, business or strategic value where applicable. Do not invent a different denominator.

  Because the denominator is fixed, the only possible values are 0, 12.5, 25, 37.5, 50, 62.5, 75, 87.5 and 100 - or 0, 14.3, 28.6, 42.9, 57.1, 71.4, 85.7 and 100 if value is genuinely not applicable and the denominator drops to 7. **If you are about to write ~90%, you estimated instead of counting** - that is not a reachable score, and it happened on the real Alchemy run. Always report `k of 8` next to the percentage.

- Observable Success Criteria Ratio = success criteria with an observable outcome / total defined success criteria x 100. Target >= 70% before kick-off. "The client is happy with performance" is not observable; "p95 response under 400ms on the pricing endpoint" is. List which criteria you counted as observable and which you did not, so the ratio can be checked.

CHECKPOINT: present the A04 description. "Here is the project description, problem reused from A01, MVP success split from the business north-star. Good to finalize the context pack?"

## Outputs and filing
- A02 Stakeholder Register - the filed artifact is a CONFLUENCE page (a mandatory starting artifact). Working draft as markdown in the project folder (General/PM) is fine; say clearly which one exists.
- A02 Internal RACI Matrix (Sales / DM / Competency Center) - mandatory, INTERNAL ONLY, shared in the accounting chat and never with the client. It is the input for the RACI Matrix (Team + Stakeholders) at A12. No template exists yet: draft it from the decision-ownership table this skill already builds, and say it is our draft. Optional alongside it: a Stakeholder Power-Interest Grid where it helps engagement planning.
- A04 Project Description - also a mandatory CONFLUENCE artifact. Same pattern.
- Internal communication channels are verified in Google Chat, not written to a doc (the mandatory Project Chats artifact is the chats themselves, with their pins).
- Both documents are gated before any brain push - show what goes in and what is held back (no money, no contract text), get a yes.

## Close-out
State plainly what A02/A04 leave open and route it: missing emails -> Sales; unresolved technical ownership -> PMO, and say it blocks delivery start rather than filing it as an ordinary gap; an unreviewed signed contract -> `a03-contract-commitments`; scope realism -> A05; risks -> A06. A thin or skipped part is justified-and-recorded, never a silent pass.

Then write the residue down, and say in one line that you did:

- Anything that needs DOING goes in `<workspace>/pm-tasks.md`, tagged with the project - the PM's actions, what is waiting on someone else, what you routed elsewhere. Actions that only ever exist in this conversation are lost when it ends, and the PM re-derives them next week.
- Anything durable you learned about the project goes in `<project folder>/project-context.md` - decisions and who made them, people, links, and what is still open.
- **The project brain gets both artifacts this skill produces.** The stakeholder register and the project description are exactly what a PM queries the brain for six months later - who owns this decision, what was this project for. Offer them at the closing checkpoint via `project-brain` (feed mode); do not upload by hand. Nothing here is money-bearing, so there is no hold-out list to argue about - which makes this one of the easiest brain pushes in the whole A block and there is no reason to skip it.
- Anything the copilot got wrong, or asked for and could not do, goes in `<workspace>/copilot-feedback.md`.
