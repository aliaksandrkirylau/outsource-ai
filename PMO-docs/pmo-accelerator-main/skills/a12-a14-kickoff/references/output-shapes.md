# Output shapes - A12, A13, A14 (skeletons only)

Structural skeletons. NOT the control contract - the authoritative Inputs / Outputs / Verification Criteria / Control Metrics live in the standard (A12 = Confluence 4988764344, A13 = 4988633155, A14 = 5015830531) or `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`.

For the mechanics of editing the deck through the connector, read `slides-gotchas.md` in this folder first.

---

## The kick-off deck - what is actually in the template

**Template: "[PROJECT] Kick-off Slide deck - TEMPLATE"**, Google Slides `1L1ukfexCcqm2-fMnsKWicy4mP-c7oXoMDWKq62fEFKg`, 12 slides, canvas 9144000 x 5143500 EMU. Content guide: Confluence 2891284612. Best practice: 4619206917. Checklists: 3035070505 and 3211985503 (internal).

Verified against the live template 2026-07-28. **Fill the PM's own copy of this - never build a parallel deck.**

| # | Slide | What goes in it |
|---|---|---|
| 1 | Title | `[Project Name]`, "Project Kick-Off", date. Background taken from the PRE-SALE deck for visual continuity |
| 2 | Agenda | The template's own nine items - see below |
| 3 | Team | six Position / Full Name slots |
| 4 | Communication Plan | the meeting table, with client-facing meetings highlighted and their regularity confirmed |
| 5 | Project Approach | methodology, delivery cadence, tools and communication, reporting and meetings, tech stack |
| 6 | Project Overview | the core project narrative for the client. Ships with lorem ipsum - replace it |
| 7 | Project & Reviews Roadmap | the real timeline, with sprint / milestone / release durations spelled out, plus key priorities |
| 8 | Commercial Governance & Project Rules | the FP or T&M fork - see below. NO figures |
| 9 | Q&A | questions grouped by assignee, product part and technical part, each with a named owner |
| 10 | Required Information | the access and information ask |
| 11 | Open Points To Be Discussed | client questions, things they wanted to think about, and a DEADLINE for the answers |
| 12 | Closing | "Let's develop software together", innowise.com, the PM's email. Same pre-sale background |

The template's agenda (slide 2), which is the real running order: Introduction, Team, Communication Plan, Project Approach & Tools, Project Overview, Project & Reviews Timeline, Q&A, Required Information, Open Points To Be Discussed.

Note this differs from the eight sections in the content guide. **The template is what gets filled, so follow it**, and use the guide for the reasoning behind each section.

### Slide 8 in detail, because it is the one with commercial consequences

The template gives both branches. Use the one that matches the contract and delete the other.

- **Fixed Price** - any change to requirements or initial inputs must follow the Change Request process. The workflow, as the template states it: Initiation -> Impact Analysis (Estimation) -> Approval by Decision Makers -> Implementation.
- **T&M with Cap** - the budget is fixed and **the figures are NOT disclosed on the slide**. Scope is managed by strict backlog prioritisation. Mandatory client notification on reaching **70% and 85%** of the cap.

Those two percentages are the concrete form of "budget threshold notifications". If the PM has not agreed who sends them and through which channel, that is an open point for the kick-off, not an implementation detail.

The slide also carries an instruction to describe the process for this specific project so the client understands the scope boundary - so do not leave the generic wording in.

### Before it goes anywhere: strip the template's own instructions

The template is full of author guidance that must not reach a client. Every one of these is real text in the file:

- "Background needs to be taken from the presale presentation for consistency and this comment removed" (slides 1 and 12)
- "Highlight in the table meetings with the Client and confirm regularity" (4)
- "FOR REVIEW" markers and "Fill info about the approach, tools etc" (5)
- "Need to describe core information about the project to sync with client" and the lorem ipsum block (6)
- "Need to Clarify in Text Durations of Each object", "Change timeline for the real one" (7)
- the commercial-process instruction, including a line in Russian (8)
- "Prepare list of Questions by assignee and facilitate meeting accordingly" (9)
- "Request needed accesses and so on" (10)
- "DEADLINE for receiving this info" - keep the deadline, remove the instruction (11)
- `PM EMAIL` placeholder (12)

Sweep for these explicitly and screenshot-verify. A deck that reaches a client still telling the PM what to write is the most avoidable bad impression available.

---

## A12 - internal alignment

```
# <Project> - internal kick-off  <date>

## Agenda  (cut blocks that do not apply; ~1 hour)
| # | Block | Minutes | Who |
(customer's company, project, team, communication plan, technologies,
 infrastructure, receivables, process, milestones)

## Team one-pager
- What we are building, in three lines
- Who is on it and who owns what
- Key dates and the critical path
- How we work: cadence, DoR/DoD, review rules, where things live
- What to watch: the top risks that affect the team's work

## Communication Plan review  (A12 output 3)
The team reads the A11 draft and gives input - cadence they can actually hold,
meetings that should not exist, reporting that costs more than it returns.
| Item | Team input | Changed? |

## Team Feasibility Confirmation  (MANDATORY output)
Asked explicitly in the room, about scope, estimates, timeline, budget and
delivery approach.
Outcome: CONFIRMED / CONFIRMED WITH CONCERNS / NOT CONFIRMED
| Concern | Area | Owner | What it needs |
(a meeting where nobody was asked has not produced this output)

## Delivery-process document owners
| Document | Owner | By when |
(Test Plan, Test Strategy, QA approach, Deployment Process, Release Management,
 Code Review rules, DoR / DoD, environment rules)

## Roles, working rules, PM system, communication expectations
| Unclear item | Resolved now / documented for later | Owner |
(the standard requires each one resolved OR documented before the readiness review)

## Alignment outcome  (A12 output 1)
Date, attendees, blocks actually covered, what was raised, what is open.

## Team Alignment Coverage
k of n agenda blocks confirmed covered = X%  (target 100%)
- the denominator is the blocks that APPLY to this project, fixed before the meeting
```

---

## A14 - the follow-up (send within 24 hours)

Written as the PM, in their voice. Access-led if access is the blocker, which it usually is. Concrete over comprehensive.

```
Subject: <Project> kick-off - agreements, next steps and what we need from you

- Thanks + one line on what was agreed overall
- Agreed points (short, numbered)
- What we need from you, by when   <- lead here if access is the blocker
  | What | Who it is for | Needed by |
- Open questions
  | Question | Owner | By when |
- Team and roles, both sides
- Next steps and the next meeting
- Recording, if consent was given:
  "Confirmed: all status meetings and demos will be recorded as per our agreed
   communication plan."
```

Then update what kick-off changed: Communication Plan, roadmap, risk and dependency records, the client inputs list, onboarding and working rules. And post the outcome to the Strategy chat.

```
## Capture coverage
- Kick-off Agreement Capture: k of n topics documented = X%  (target 100%)
- Open Action Ownership: k of n actions with an owner AND a next step = X%  (target 100%)
```

Any scope, timeline, budget, acceptance, environment or contractual mismatch that surfaced goes to Account / Sales / Delivery BEFORE it is absorbed into the delivery baseline.
