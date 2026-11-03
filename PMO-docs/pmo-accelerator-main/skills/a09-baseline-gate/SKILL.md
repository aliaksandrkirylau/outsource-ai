---
name: a09-baseline-gate
description: Run Standard A step A09 - validate the project baseline with internal and external stakeholders. This is the go/no-go gate - after it the baseline is approved or accepted with constraints, and only then does setup begin. Use when scope, roadmap and economy exist and the project needs a decision - "run the baseline gate", "A09", "go no-go", "is this project approved to start", "validate the baseline", "get sign-off to start", "present the project to management", "confirm the baseline with the client", "we need approval before staffing", "why is the project classified this way", "the economy is weak, can we still take it". Assembles the baseline package, works out the value classification and who owns realising it, drafts the internal ask and the client confirmation, and records the decision. The copilot never approves anything - it prepares the decision and captures what the stakeholders actually decided.
---

# a09-baseline-gate - A09, the go/no-go

The hinge of the whole A-block. A01 to A08 answer "should and how can this project move forward"; A09 is where someone actually answers it. After A09 the baseline is approved or accepted with constraints, and only then does setup begin. The standard is blunt about the consequence: no internal go means no team appointment and no project setup.

Read the contract from `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`, section A09 (Confluence page 4619206835). Output shapes are in `references/output-shapes.md`. The Baseline Validation and Project (Start) Approval are two mandatory starting artifacts since Sep 2026 (the client half and the internal half), and both live in mail or Google Chat, not in a document.

## The one rule that defines this skill

**The copilot does not approve anything.** It assembles the package, sharpens the judgement, drafts the asks, and RECORDS what real stakeholders actually decided. It never writes "approved" on the strength of its own analysis, never infers a decision from silence, and never softens a "requires rework" into something more comfortable.

A gate the copilot can pass on its own is not a gate.

Two more that never relax:
- Never send. The internal ask and the client confirmation are both drafted here and sent by the PM.
- The internal package may discuss economy. **The client-facing package may not** - no margin, no rates, no internal cost. Two audiences, two documents, and the money one never leaves the approved channel.

## Stage 0 - Is the gate even ready to run, and is an ask already out

**First: check whether this gate is already in flight.** A09 pauses on other people for days. Read `project-context.md` for a pending A09 ask before assembling anything - who it went to, what was asked, when, and the deadline. If one is outstanding, do NOT re-draft it; say what is pending and offer to record the outcome, chase it, or work something else. Re-sending a leadership ask because a session ended is a real way to look disorganised.

Then check readiness. Run the scanner for a starting number:

```
python3 "<PLUGIN_ROOT>/skills/project-router/scripts/scan_initiation_state.py" "<project folder>"
```

`python3` in the Cowork sandbox; `python` on a Windows machine directly. It reports "Ready for the A09 gate (A01-A08)" as a fraction.

**Correct that number before you quote it.** The scanner reads the project FOLDER, and A08 is never in it - money lives in the Sensitive folder by policy. So the scanner under-reports by one on essentially every project that has done its economy work. On a real run it said 7 of 8 with A08 "missing" while the P&L existed and had been worked. Quoting the raw fraction tells a PM they are not ready when they are.

So: take the scanner's number, then verify the four inputs that actually matter by hand and restate the fraction:

- **Project Description** (A04) - what problem, what outcomes, what success looks like.
- **Roadmap, milestones, hours and period** (A07) - is there a plan with dates, and how many hours over what window.
- **Economy** (A08) - read the recorded outcome in `project-context.md`: the classification, who worked it, when. That record exists because `a07-a08` is told to bring it back for this gate. **If it is not there, the economy judgement has not come back and the gate is not ready** - that is a far more useful answer than a fraction. Never open the P&L to check figures.
- **Risks and open items** (A06) - what the decision-makers need to know before saying yes.

Be honest about a thin baseline. "A07 and A08 are not done, so there is nothing to approve yet" beats assembling a package around holes. If the PM wants to proceed anyway - and sometimes a project genuinely starts before the paperwork - say plainly which parts of the decision will be unsupported, and carry that as a caveat on the outcome rather than hiding it.

CHECKPOINT: "Corrected pre-gate readiness is X of 8 (the scanner said Y - it cannot see the P&L, which is in the Sensitive folder). Economy classification on record: [x] from [date]. Missing: [gaps]. Run the gate now, or close [gap] first?"

## Stage 1 - The leadership summary (this is the artifact)

**Write for how it is actually read.** Leadership will not work through nine areas of detail. They want a summary and clear flags so they can decide whether to open staffing, with a route into the detail if something looks wrong. A thorough package nobody reads is worse than a page that gets a decision.

One page. Hours are shareable, money is not. The shape:

- **What the project is and what we are delivering** - two lines. Not the vision statement, the thing.
- **Hours and period** - how much work, over what window. The headline number, straight in the summary.
- **Contract state** - signed / in signing / blanks outstanding, and what is open. Whether A03 was reviewed.
- **The PM's readiness call** - see below. The centre of the document.
- **Flags** - red and amber and green, scannable. This is the part that actually gets read, so put the honest ones in it.
- **Main risks** - three to five from A06, not the register. Include the owner.
- **Main strengths** - what is genuinely solid. A summary of only problems reads as a project in trouble when it may not be.
- **Value classification** - one line: how we are taking this project, and the named value owner. Rationale and hypothesis go in the annex (Stage 2).
- **Economy** - a flag plus "posted in the Economy chat". NEVER a link to the file, never a figure. See the rule below.
- **What has been prepared** - the inventory of documents and analysis done, with links. This is how leadership sees the work was real without reading it, and it is the route into detail for anyone who wants it. Take it from the output list in `project-context.md`.

### The PM's readiness call, and the copilot's job around it

An honest take from the PM: **ready to start / ready with constraints / not ready** - and why, in their own words. This is what leadership is actually buying, and the copilot does not own it.

What the copilot does own: drafting a candidate take from the evidence and then CHECKING the PM's version against it. If the PM says ready while A06 carries uncovered critical risks, the client baseline is unconfirmed, or the contract still has blanks, say so before the package goes out. Not to overrule - to make sure the take is an informed one and the PM is not about to be surprised in the room.

If the PM's call and the evidence disagree and the PM stands by their call, that is their prerogative. Record the call as theirs and note what it is going against, plainly, once.

### The economy rule, which is absolute

**Never link the P&L file. Never put a figure, rate, margin or cost in the summary.** The summary says the economy is posted in the Economy chat, and nothing more about where it lives.

Then ask the PM to CONFIRM it is actually posted there before that line ships. "It is in the Economy chat" is a claim leadership will rely on without checking, and an unposted economy discovered at the gate is an avoidable embarrassment.

On the flag itself: default to carrying the classification word from A08 - healthy, questionable, risky, negative, acceptable only with strategic justification - because leadership deciding whether to open staffing needs to know which of those it is, and the word carries no figure. Offer the PM the option to strip it to a bare "posted in the Economy chat" if they would rather it were not on the page. Their document, their leadership.

CHECKPOINT: show the one-pager. "This is what goes to leadership. Your readiness call reads [x] - [any evidence that argues with it]. Is the economy actually posted in the Economy chat? Anything you would frame differently?"

## Stage 2 - Value classification and who owns realising it

The judgement that makes this step worth doing, and the one most often skipped.

Classify the project as one or a combination of:
- **Profit-oriented** - it makes money and the economy supports that.
- **Marketing / reference / market-entry / client-development** - a logo, a case study, a foot in a market, a relationship worth having.
- **Technical or domain expertise acquisition** - we learn something we want.

**The A08 economy classification is what triggers this work, so read it first.** The two classifications interlock and it is easy to treat them as unrelated: A08 classifies the ECONOMY, A09 classifies how we are taking the PROJECT. An A08 verdict of "acceptable only with strategic justification" is precisely the case that mandates a non-profit classification with a documented rationale and a value extraction hypothesis. A "healthy" economy usually means profit-oriented and a short annex.

Then the conditional requirements the standard attaches:

- **If profitability is weak, it proceeds only on ONE of two documented things** - and the skill used to carry only the second. Either a **documented management decision** (a Head of PMO or Delivery decision to take it anyway, recorded, with who decided and when), OR a **non-financial value rationale**. Both are legitimate. The management-decision route is often the real one, so do not push a PM to manufacture a strategic story when the honest answer is "Delivery decided to take it, here is the record".
- **If the classification is anything other than profit-oriented, a value extraction hypothesis must be documented** - how the non-financial value actually gets realised, and **who owns realising it.** "It's good for marketing" with no owner is not a hypothesis, it is a hope. Name the person or say plainly that nobody owns it, which is itself a finding worth surfacing.

The summary carries one line of this. The rationale and the hypothesis go in the annex behind it, for whoever wants to argue with them.

The copilot's job here is to draft the classification and interrogate the rationale, not to decide it. If the economy is weak and the PM has neither a management decision nor a non-financial story, say so - that is a real input to the gate, not a gap to paper over.

CHECKPOINT: "Classified as [x] because [y]. The value extraction hypothesis is [z], owned by [who]. Does that hold up, or is it a story we are telling ourselves?"

## Stage 3 - Internal validation (the go/no-go)

**Point each area at the stakeholder who should actually review it**, rather than sending one document to everyone and hoping. The summary goes to whoever gives the go, but specific areas need specific people:

| Area | Usually reviewed by |
|---|---|
| The go/no-go itself | Head of PMO or Delivery |
| Client commitments, contract state | Account / Sales |
| Technical feasibility, architecture, the long pole | the technical owner (DM / Tech Lead) |
| Staffing feasibility, if the roles are contested | Resource Manager |
| Economy | Head of PMO / Delivery, via the Economy chat - not via this document |

Confirm the actual names against the A02 stakeholder register rather than assuming, and **fix this routing list BEFORE anything goes out.** It is the denominator for the coverage metric, and deciding which areas needed a reviewer after you know which ones got read is how a 100% gets manufactured.

Draft the ask: the summary, who you need to look at what, the recommendation, and the deadline. The PM sends it - never the copilot.

**Then write down that the ask is pending, before waiting.** Put it in `project-context.md` (who, what, when sent, deadline) and in `pm-tasks.md` as something waiting on someone else. A09 pauses on other people for days, so the answer almost always arrives in a different session - and without this the next session re-drafts an ask that is already sitting in a Head of Delivery's inbox.

Then RECORD what came back. The outcome vocabulary is fixed by the standard; use exactly one of these and do not invent a sixth:

- approved to continue
- approved with constraints
- requires rework
- paused
- rejected - not accepted

"Approved with constraints" needs the constraints written down, each with an owner. That is the most common real outcome and the one that silently becomes "approved" if nobody records the constraints.

If a decision has not come back yet, the outcome is not recorded yet. Do not fill it in optimistically, and never infer approval from silence.

CHECKPOINT: the drafted ask plus the routing list for the PM to send; then record it as pending. The outcome and its constraints get recorded in a later session, when they exist.

## Stage 4 - Client baseline validation

Separate from Stage 3, different audience, and **no internal money in it.** The client confirms the delivery baseline they are getting: scope, milestones, acceptance approach, their own obligations and inputs.

The standard accepts confirmation in the contract or SOW, an email, a meeting follow-up, or another agreed written channel. There is no template for this - the template register confirms it - so draft it and say plainly that the format is ours, not house standard.

Record one of: confirmed / requires clarification / requires rework. An unconfirmed client baseline blocks team appointment and setup just as an internal no does.

If the client raises material objections, those are not a footnote. Route them: scope changes to A05 and the CR process, timeline to A07, anything commercial to Account and Sales.

CHECKPOINT: the drafted confirmation request; later, the recorded client outcome.

## Stage 5 - Score, record, and say what this unblocks

**Control metric.** Stakeholder Validation Coverage = baseline areas reviewed with the required stakeholders / total relevant baseline areas x 100. Target 100% before team appointment and full setup.

Count it against the Stage 3 ROUTING LIST, not against how many areas appeared in the summary. The question is whether each area reached the person who should have looked at it - technical feasibility to the technical owner, client commitments to Account - not whether leadership read a page containing everything. Read the other way round the metric is trivially 100% and means nothing. Name both sides of the ratio, and an area nobody with the right role reviewed is not covered however confident anyone feels.

**The decision record** goes in the project folder, following `references/output-shapes.md`. It carries the internal outcome, the constraints, the value classification with its rationale and owner, the client outcome, the coverage number, and the date.

**The mandatory Baseline Validation and Project (Start) Approval artifacts** are the approval itself, and it lives in mail or Google Chat - the thread where the decision was actually given. Link it from the decision record rather than retyping it; the original message is the evidence.

Then say plainly what the outcome unblocks or blocks:
- **Approved to continue** - A10 staffing and A11 setup are open.
- **Approved with constraints** - open, but the constraints travel with the project. List them where the next steps will see them.
- **Requires rework / paused / rejected** - staffing and setup do NOT proceed. Name what would have to change.

Every open point touching critical scope, timeline, economy, client commitment or feasibility gets an owner and a next action.

CHECKPOINT: the decision record, the coverage number, and the one-line consequence.

## Outputs
- **The leadership summary** - one page: what the project is, hours and period, contract state, the PM's readiness call, flags, main risks, main strengths, the value classification line, the economy pointer, and the inventory of what was prepared with links.
- Reviewer routing list - which area goes to whom.
- Value classification annex - rationale, and the value extraction hypothesis with a named owner.
- Internal Stakeholder Validation Outcome (mandatory) - one of the five, with constraints if any.
- Client Baseline Validation Outcome (mandatory).
- Decision record in the project folder; the approval thread itself linked as the Project (Start) Approval artifact, and the client confirmation as Baseline Validation.
- Stakeholder Validation Coverage with its basis.

Never an output: a link to the P&L, or any figure from it.

## Close-out
A weak-but-taken economy is recorded with its justification and its value owner - that is the record someone will want in six months. A thin or skipped area is justified-and-recorded, never a silent pass.

If the copilot cannot tell whether a decision was actually given, it says so. An unrecorded gate is worse than an open one, because the project proceeds as though it passed.

Then write the residue down, and say in one line that you did:

- Anything that needs DOING goes in `<workspace>/pm-tasks.md`, tagged with the project - the PM's actions, what is waiting on someone else, what you routed elsewhere. Actions that only ever exist in this conversation are lost when it ends, and the PM re-derives them next week.
- Anything durable you learned about the project goes in `<project folder>/project-context.md` - decisions and who made them, people, links, and what is still open.
- **The project brain gets the DECISION - what was approved, by whom, when, and under what constraints.** Offer it via `project-brain` (feed mode). This is the single most queried fact on a project after the fact ("were we approved to start, and did anyone attach conditions"), and it is normally reconstructed from an email thread months later, badly. A decision recorded with its constraints is worth more in the brain than any document this skill assembles.
  - Carry the same discipline the rest of this skill holds: the economy is a CLASSIFICATION and a flag, never a figure. "Accepted with constraints, economy flagged, worked with the RM" goes in. Numbers do not, and the baseline package's economy section does not go in as an attachment. If the value classification came with money reasoning, record the classification and drop the reasoning.
- Anything the copilot got wrong, or asked for and could not do, goes in `<workspace>/copilot-feedback.md`.
