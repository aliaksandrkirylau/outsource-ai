---
name: a12-a14-kickoff
description: Run Standard A steps A12, A13 and A14 - align the team internally, prepare the client kick-off, run it, and send the follow-up. Use when the team is confirmed and the project is about to start - "prepare the kick-off", "kick-off deck", "internal kick-off", "align the team", "client kick-off", "kick-off agenda", "we have kick-off next week", "write the kick-off follow-up", "kick-off recap email", "what do I cover at kick-off", "A12", "A13", "A14". Builds the internal alignment agenda and team one-pager, fills the PMO kick-off deck, prepares the client-facing process topics (UAT, testing, release, environments, CR or budget control), drafts the invite and the 24-hour follow-up, and captures the agreements. The PM sends everything; the copilot drafts and checks.
---

# kickoff - A12 team alignment, A13 kick-off prep, A14 running it

Three steps, one arc: get the team aligned, prepare the client meeting, run it and capture what was agreed. They are one skill because the internal alignment feeds the client materials and the follow-up closes both.

Read the contract from `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`, sections A12, A13 and A14. Output shapes: `references/output-shapes.md`. The Kick-off Slide Deck is a mandatory starting artifact.

Two prerequisites the standard is firm about: the team must be confirmed (A10) and the PM system prepared (A11) before internal alignment, and internal alignment must be done before the client invite goes out. If A09 never passed, stop and say so - kicking off a project whose baseline was never approved is a governance problem, not a scheduling one.

## Rules that never relax

- **The PM sends everything.** The invite, the deck, the follow-up. The copilot drafts and checks.
- **Written approvals only.** A verbal yes on a call is not formal approval. Anything agreed verbally goes into the follow-up in writing, and that is what makes it real.
- **No internal money in client-facing material.** No margin, no rates, no internal cost, in the deck or the follow-up.
- **Two mandatory human gates before the client sees anything:** the M-Manager review of the deck, and the internal dry run. Neither is optional and neither is something the copilot can perform. Flag them; do not skip past them.

## Stage 0 - Which of the three are we doing, and what applies

Ask where the PM is: aligning the team, preparing the client meeting, or writing the follow-up after one. Run only that part - a PM two days from kick-off does not want to be walked through A12.

Then establish **what actually applies**, because the standard's "where applicable" doctrine matters here more than anywhere:

- **UAT** applies if the client must validate the result before acceptance. If not, still define how the result gets reviewed and accepted.
- **Release management** applies if there is a controlled release to staging, production, an app store, or a client environment.
- **Deployment** applies if it needs environments, access, infrastructure, approvals or client-side actions.
- **CR process** applies if scope can change and commercial impact must be controlled.
- **Budget threshold notifications** apply on T&M with a cap.

And the fork that changes the commercial half of the conversation:
- **Fixed price** - how scope changes, assumptions, out-of-scope requests and CR approval are handled.
- **T&M** - how budget usage, burn rate, remaining budget and threshold notifications get communicated.

A skipped topic is explainable, not invisible. Record why.

CHECKPOINT: "You are at [stage], the contract is [type], and these topics apply: [list]. These do not, because [reason]. Right?"

## Stage 1 - A12: internal team alignment

Goal: bring the confirmed team up to speed fast, and get their honest read on whether the plan is deliverable. The second half is the mandatory output and the one that gets skipped.

**The agenda.** The PMO internal kick-off checklist gives a nine-block structure - customer's company, project, team, communication plan, technologies, infrastructure, receivables, process, milestones - at roughly an hour. Draft it from the project's real material, not the generic list, and cut blocks that do not apply. Alchemy's version ran eight blocks with minute budgets and a short "open questions to settle in the room" list at the end; that shape works.

**The team one-pager.** Not in the standard, but it is what the team actually reads: what we are building, who is on it, key dates, how we work, what to watch, and where things live. Draft it alongside the agenda.

**Team Feasibility Confirmation (mandatory).** The point of the meeting. Ask the team directly whether scope, estimates, timeline, budget and delivery approach are deliverable, and record the answer - confirmation OR documented concerns. A meeting where nobody was asked has not produced this output.

If the team cannot confirm: a quick re-estimate from existing material is the PM's to run before the readiness review. Anything larger - team effort, client input, a technical spike, a separate discovery - needs effort, ownership, commercial impact and timing agreed with internal management first. If the project cannot be delivered within current fixed scope, budget or timeline assumptions, that escalates BEFORE client kick-off, and the fork is re-baselining vs discovery phase vs scope reduction vs CR vs moving to T&M.

**The team reviews the Communication Plan draft, and an updated draft is an A12 output.** A11 drafted it; this is where the people who have to live with the cadence get to say whether they can hold it. Put the draft in front of them and capture what changed - a meeting that should not exist, reporting that costs more than it returns, a demo rhythm nobody can sustain. Skipping this is how a communication plan survives to kick-off describing meetings the team never agreed to.

Also assign owners for the delivery-process documents that will be needed: Test Plan, Test Strategy, QA approach, deployment process, release management, code review rules, DoR and DoD, environment rules.

**And resolve or document the unclear basics.** The standard requires unclear roles, working rules, PM system or communication expectations to be resolved OR written down before the readiness review - not left to settle themselves. Ask directly whether everyone knows who owns what, how the team works, and where things live. "Probably fine" is not one of the two allowed outcomes.

**RACI Matrix (Team + Stakeholders) (mandatory since Sep 2026).** Built from the Stakeholder Register and A02's internal RACI, covering the team and the stakeholders. Every listed participant reviews and confirms their role - RACI Acknowledgement Coverage, target 100% before the readiness review. The confirmation is the hard part, so plan how each person confirms (a reply in the internal chat is enough) rather than presenting the matrix and assuming silence is agreement. No template exists yet: draft it and say it is our draft.

Control metric: Team Alignment Coverage = confirmed alignment areas / total required areas x 100. Target 100% before the readiness review. **Fix the area list before the meeting** - it is the agenda blocks that apply to this project - and count against it afterwards. Choosing the denominator once you know which blocks got covered produces a 100% that means nothing.

CHECKPOINT: agenda, one-pager, the Communication Plan changes, and the feasibility question the PM needs to ask in the room.

## Stage 2 - A13: the kick-off deck

**Ask first whether a template copy already exists.** This is the mistake worth avoiding: if the PM has already copied the PMO deck and named it for the project, that copy is the thing to fill. Building a parallel deck from scratch wastes the work and loses the branding. Only build fresh if there is genuinely no copy.

**The template, exactly:** "[PROJECT] Kick-off Slide deck - TEMPLATE", Google Slides `1L1ukfexCcqm2-fMnsKWicy4mP-c7oXoMDWKq62fEFKg`, `https://docs.google.com/presentation/d/1L1ukfexCcqm2-fMnsKWicy4mP-c7oXoMDWKq62fEFKg/edit` - 12 slides. Content guide Confluence 2891284612, best practice 4619206917, kick-off checklist 3035070505, internal kick-off checklist 3211985503.

**The slide-by-slide map is in `references/output-shapes.md`. Read it before filling anything** - it carries what belongs on each of the 12 slides, taken from the live template rather than from the guide. Two things in there worth knowing before you start:

- **The template's own agenda differs from the content guide's section list.** The template runs: Introduction, Team, Communication Plan, Project Approach & Tools, Project Overview, Project & Reviews Timeline, Q&A, Required Information, Open Points To Be Discussed. Follow the template, because that is the file being filled; use the guide for the reasoning behind each section.
- **Slide 8, Commercial Governance, is the one with consequences.** It carries both branches and you delete the one that does not apply. Fixed Price: changes follow the CR process, workflow Initiation -> Impact Analysis (Estimation) -> Approval by Decision Makers -> Implementation. T&M with Cap: budget fixed with **figures NOT disclosed on the slide**, scope managed by strict backlog prioritisation, and mandatory client notification at **70% and 85% of the cap**. Those percentages are the concrete form of "budget threshold notifications" - if nobody has agreed who sends them and through which channel, that is an open point for the meeting.

Adapt to the contract type - the guidance is explicit that content ranges from detailed plans to a lighter environmental presentation. The title and closing slides both instruct you to take the background from the PRE-SALE deck, so the client sees one continuous story.

**Strip the template's own instructions before anyone sees it.** The file is full of author guidance - "Background needs to be taken from the presale presentation... and this comment removed", "FOR REVIEW" markers, "Change timeline for the real one", a lorem ipsum block on Project Overview, a `PM EMAIL` placeholder, and a line of Russian on slide 8. `output-shapes.md` lists them all. Sweep for them explicitly. A deck that reaches a client still telling the PM what to write is the most avoidable bad impression available.

**If you are editing Google Slides through the connector, read `references/slides-gotchas.md` first.** Tables and grouped graphics report as type Unknown with no child IDs, `replaceAllText` with zero matches does not error, and deleting text collapses run styling. Every one of those has already cost a rebuild.

**Then the two human gates.** Submit the draft to the M-Manager for review before anything goes to the client - mandatory, and it covers team photos too if any were added. Then run the internal dry run with the core team: presentation flow, speaker transitions, technical details. Neither is something the copilot does. Say plainly that these are the PM's next actions.

CHECKPOINT: the filled deck, and the two gates flagged as outstanding.

## Stage 3 - A13: the client-facing process topics

The substance behind the deck, and the part that determines whether the first month goes smoothly. Prepare each applicable topic as discussion material - not final documents. The standard is explicit that A13 prepares draft assumptions and questions, it does not finalise process docs.

- **Communication and working model** - channels, cadence, participants, reporting and demo rhythm, how decisions get confirmed in writing, tracker usage, feedback flow.
- **UAT and acceptance** - who participates client-side, what gets accepted, how feedback and defects are submitted, what acceptance evidence is required, how final confirmation is recorded.
- **Testing** - levels, QA involvement, environments, test data, regression expectations, client participation, and whether a separate Test Plan is needed after kick-off.
- **Release, deployment, environments** - environments and who provides them, servers, accounts, access, deployment windows, third-party dependencies.
- **CR or budget control** - per the contract-type fork from Stage 0.
- **Client questions and required inputs** - contacts, access, environments, UAT participants, acceptance owners, reporting expectations, open delivery assumptions.

**Lead with access.** The single most reliable way to lose the first two weeks is waiting on accounts and environments. Prepare the access ask as a concrete per-person list - name, role, email, and exactly which systems each needs - rather than a general request. On Alchemy that list, sent the day after kick-off, was the thing that actually moved.

Anything here with commercial or contractual impact needs Account, Sales or Delivery involved before or during the client conversation. Do not let a PM agree an acceptance rule with commercial consequences on their own.

**The invite (mandatory output).** Meeting goal, agenda, required participants, key topics, pre-read links. Sent at least 24 hours ahead. If the agenda and materials are not ready enough to align expectations, the standard says postpone the invite - say that rather than helping ship something thin.

Control metric: Kick-off Materials Coverage = prepared required topics / total required topics x 100. Target 100% before the invite goes.

CHECKPOINT: the topic pack, the access list, and the drafted invite for the PM to send.

## Stage 4 - A14: run it, and the recording consent

During the governance part of the meeting the PM establishes recording as a standard quality procedure. The PMO gives the wording, and it is worth using close to verbatim because it frames recording as a quality practice rather than surveillance:

> "To ensure we don't miss any of your valuable feedback and to make our follow-ups as precise as possible, we record our status meetings and demos. This is our internal quality standard that helps us keep the whole team in sync without distracting you with repeated questions. Does this work for you?"

And at the start of every later session: *"As we agreed before, I am starting the recording now."*

Verbal consent must be documented in the follow-up. If consent is not given, that is a finding for the communication plan, not something to work around.

Prompt the PM on the things that get forgotten in the room: give the experts a moment to introduce themselves, leave time for Q&A, and capture decisions as they happen rather than reconstructing afterwards.

## Stage 5 - A14: the follow-up within 24 hours

The mandatory output, and the step that stops kick-off agreements from remaining verbal. Draft it; the PM sends it.

It carries: agreed points, open questions with owners and dates, access requests, team and roles on both sides, updated artifacts, next steps, and the recording confirmation if consent was given - *"Confirmed: all status meetings and demos will be recorded as per our agreed communication plan."*

Write it as the PM, in their voice. Access-led if access is the blocker, which it usually is. Concrete over comprehensive - a recap nobody reads has not captured anything.

This follow-up and the kick-off invite are both text the PM SENDS, so hand them to the PM's own voice skill if they have one, otherwise to `pm-voice`, rather than drafting inline. The length budgets live there, and a kick-off recap is where a missing budget shows worst. The required content list above is fixed; the voice applies inside it.

Then update what kick-off changed: the Communication Plan, the roadmap, risk and dependency records, the client inputs list, onboarding and working rules. And update the Strategy Chat with the outcome.

Two control metrics, both stated with their basis:
- Kick-off Agreement Capture Coverage = agreement topics documented / total agreed or discussed topics x 100. Target 100%.
- Open Action Ownership Coverage = open actions with an owner and a next step / total open actions x 100. Target 100%.

Any scope, timeline, budget, acceptance, environment or contractual mismatch that surfaced escalates to Account, Sales or Delivery BEFORE it gets absorbed into the delivery baseline. That is the one thing not to be relaxed about - a mismatch quietly absorbed at kick-off becomes an argument in month three.

CHECKPOINT: the drafted follow-up, the document updates, and anything needing escalation.

## A note on "the readiness review"

The standard gates several things on a readiness review - A11's and A12's control metrics both target 100% "before the readiness review", and three escalations require items resolved before it. **Our reference pack does not define what it is**, who runs it, or what it checks, and it is not one of A01 to A14.

So if a PM asks: say plainly that the standard references it as a gate and our copy does not describe it, and point them at PMO leadership or the live Confluence rather than inventing a description. Do not improvise a readiness-review agenda.

## Outputs
- A12: internal kick-off agenda, team one-pager, the Communication Plan draft updated with the team's input, Team Feasibility Confirmation or documented concerns (mandatory), RACI Matrix (Team + Stakeholders) with every role confirmed (mandatory), delivery-process document owners, the alignment outcome record (attendees, blocks covered, what was raised, what is open).
- A13: kick-off deck filled (a mandatory starting artifact), client-facing process topics, per-person access list, client kick-off invite sent (mandatory).
- A14: kick-off notes and follow-up sent (mandatory), updated Communication Plan, updated open actions and client inputs list, updated project documents.

## Close-out
Name what is still open with owners and dates. If UAT, release or CR topics were deferred to separate documents, say who owns each and by when. A thin or skipped topic is justified-and-recorded, never a silent pass.

Then write the residue down, and say in one line that you did:

- Anything that needs DOING goes in `<workspace>/pm-tasks.md`, tagged with the project - the PM's actions, what is waiting on someone else, what you routed elsewhere. Actions that only ever exist in this conversation are lost when it ends, and the PM re-derives them next week.
- Anything durable you learned about the project goes in `<project folder>/project-context.md` - decisions and who made them, people, links, and what is still open.
- **The project brain gets the deck, the meeting notes and the agreements made in the room.** Offer them via `project-brain` (feed mode). The agreements are the valuable part and the part that evaporates: what was promised about UAT, releases, environments, the CR process and budget control gets referred back to for the entire project, usually from someone's memory of a call. The deck is a native Google Slides file so it adds cleanly as a Drive source.
  - Format note from `${CLAUDE_PLUGIN_ROOT}/references/pmo-conventions.md`: combine transcripts and meeting notes into ONE source rather than adding each separately, or the source limit gets eaten by a single project's calls. This is the first step that generates recurring meeting material, so the habit starts here.
- Anything the copilot got wrong, or asked for and could not do, goes in `<workspace>/copilot-feedback.md`.
