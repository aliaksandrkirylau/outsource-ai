# Types and the note header

Nine types. Read this before creating or changing a typed note. A new type or field needs the
curator's yes (AGENTS.md, "Changing the schema"). Lint (`tools/kb-lint.mjs`) checks what is marked
"lint" below.

Capability is the centre: the Scope Baseline (the WBS, the SOW, the Commitments) justifies a
Capability; Requirements, Concerns and Decisions refine it; Increments implement parts of it; Risks
threaten it. Artifacts the standard requires (the risk register, the roadmap, specs) are generated
from these notes, never kept as a second copy.

## The header

Every typed note starts with this. Leave out fields that are empty.

```yaml
---
type: requirement          # requirement | concern | decision | question | term | commitment | capability | increment | risk
id: REQ-012                # the prefix for the type, three digits (risks: K-n); the file name starts with it
status: draft              # draft | proposed | stable | disputed | deprecated
origin: extracted          # extracted | evaluated | envisioned
author: claude-code/claude-opus-5-5    # who wrote it: human:<id>, or <agent>/<model>
verified_by: human:anton.oparienko   # set only by that person; required for stable
verified_on: 2026-10-08
sources:
  - "[[2026-10-06 Sync workshop - transcript]]"
supersedes: "[[REQ-004 Nightly sync]]"
superseded_by:
valid_from:
valid_to:
tags:
  - sync
---
```

- Lists go one item per line. Obsidian rewrites inline lists that way whenever anyone edits a
  property, and in a shared repo that causes conflicts on lines nobody touched.
- No `created` or `updated` fields. Git has both, and a field every edit changes conflicts on every
  concurrent edit.
- `author` is who wrote the text. `verified_by` is who confirmed it. They are often different, and
  that difference is the point: it replaces a confidence score nobody can check.
- A person's id is their Innowise email name: `human:anton.oparienko`, `human:anton.snotau`. First
  names are ambiguous - this project has two Antons.

`status`:

| Status | Meaning | Who sets it |
|---|---|---|
| draft | written, not reviewed | anyone, including agents |
| proposed | ready for the owner or the deciders to confirm | anyone, including agents |
| stable | confirmed by the person in `verified_by` | that person only (lint: needs `human:`) |
| disputed | two versions disagree; both are kept in the note | kb-sync, ingest, anyone |
| deprecated | superseded or dropped, kept for history | the owner or the curator |

`origin`:

- extracted - a source says it. Cite it with a short quote (lint: needs `sources`).
- evaluated - we concluded it from sources. Say from which.
- envisioned - we propose it. Nobody has agreed it yet.

Body: one H1, `# <ID> <title>`, then the type's sections. Cite inline, with the source link plus a
timestamp or section, and a short quote for anything extracted:

```text
([[2026-10-06 Sync workshop - transcript]] 00:14:32, "we cannot lose a report if the rig loses power")
```

Supersession: the new note carries `supersedes`, the old one `superseded_by` and
`status: deprecated`. Both directions, or the chain lies from one side (lint). Supersede when the
core of the note changes. When only a part changes, do not supersede: the new note links the old one,
and the old one gets a line saying what no longer holds and which note replaced that part.

No state fields on any note (lint): no `sprint`, `iteration`, `assignee`, `progress`, `estimate`,
`hours`, `state` or `jira_status`. Those live in Jira and reach the KB only as a generated snapshot.

The baseline is referenced the same way everywhere, one entry per line:

- `WBS:<tab>!<row>`, or a range `WBS:<tab>!<first>-<last>`: `WBS:Development Flutter!61-66`
- `SOW:M<n> <item>`: `SOW:M3 Synchronization with backend logic`
- a Commitment link: `"[[COM-020 Milestone plan and deliverables]]"`
- `CR:<id>` for an approved change request

## Requirement (REQ)

`knowledge/requirements/`. Owner: the BA.

A testable need the product must meet: what and why, never how.

Distinctions:

- Not a Concern. A Requirement is an outcome a user or the client needs; a Concern is a quality or
  constraint the architecture must treat (integrity, offline, latency, compliance).
- Not a Commitment. A Requirement is what the product must do; a Commitment is what we owe the
  client (a deliverable, a date, an acceptance step). One Commitment can drive many Requirements.
- Not a Question. If the need is unclear, it is a Question until answered.

Fields:

- `scope_status` (lint): contracted (stated in the contract, SOW or WBS), clarified (makes a
  contracted item concrete, no new scope), derived (follows necessarily from contracted items),
  proposed-change (new scope, a change request candidate), out-of-scope (recorded so nobody
  re-asks).
- `acceptance_measure` (lint, required for proposed and stable; not for draft or disputed): one
  measurable line.
- `baseline` (lint): a list, many-to-many, in the format above. For contracted, clarified and
  derived, the items that justify it (at least one). For proposed-change and out-of-scope, the
  nearest items it falls outside, or empty. Replaces `wbs`, which held one line.
- `capabilities`: the Capabilities it refines, one link per line.

Body: Need (who, what, why), Acceptance criteria, Edge cases, Business rules, Out of scope.

Acceptance criteria are binary: could a developer write an automated test without asking? At least
the happy path, a permission case where roles apply, two edge cases and an error case. For this
product the error case is usually offline: the connection drops mid-action, or two rigs edit the
same record. Given/When/Then or a checklist, either is fine. Never "works correctly", "fast",
"user-friendly", or an implementation detail. An assumption needed to write a criterion is tagged
`[ASSUMPTION: ...]` and becomes a proposed Decision or a Question.

Depth: just enough to transfer the knowledge without prescribing the implementation. No schemas,
APIs, libraries or current estimates; the initial estimate of the WBS line may be quoted as history,
citing the WBS version (AGENTS.md rule 6).

Lifecycle: draft, proposed, then stable when the BA confirms it against something the client stands
behind (the contract, the SOW, a client meeting). A proposed-change is always a new note; it never
edits a stable Requirement.

## Concern (CON)

`knowledge/concerns/`. Owner: the TL.

A quality attribute or constraint the architecture must treat explicitly.

Distinctions:

- Not a Requirement (above).
- Not a Risk. A Concern needs treatment whatever the odds; a Risk is an uncertain event.
- Not a Decision. The Concern is the problem; the Decision is the chosen treatment.

Fields: `kind`: quality, constraint, compliance, integration or operations. `capabilities`: the
Capabilities it constrains.

Body: What must hold (measurable where possible, "99.9% of reports reach HQ intact"), Why, Affected
requirements, Treatment (links to Decisions; empty until decided).

Lifecycle: stable when the TL confirms it. Treated when a stable Decision links it.

## Decision (DEC)

`knowledge/decisions/`. Owner: the named deciders.

An authoritative choice about business, scope, architecture or delivery, with its context, options,
rationale and consequences.

Distinctions:

- Not a Commitment. A Decision is our choice; it may create a Commitment.
- Not a Question. A Decision concludes; a Question asks.
- Not a Concern (above).

Fields: `kind` (business, scope, architecture or delivery), `deciders`, `valid_from`, `valid_to`,
`capabilities`.

`deciders` (lint), one per line:

- `human:<id>` for an Innowise person.
- `client:<name or role>` for a choice the client made, named as the source names them
  (`client:general-manager`).
- `tbd` while nobody has named them. A PM names them (ingest step 7). A Decision may be proposed
  with `tbd`; it cannot become stable with it.

Body, every section required (lint warns):

- `## Context`
- `## Options considered`: at least two, including the ones that lost and why. A decision with no
  rejected options is a press release, not a record.
- `## Decision`
- `## Rationale`
- `## Consequences`: at least one real downside and one new obligation. Say if it is hard to
  reverse.

Lifecycle: proposed until one of the `deciders` sets `verified_by` (lint). When every decider is
`client:`, a PM verifies it against the source instead. Before proposing, search the existing
Decisions for anything this one contradicts, and check it against what the Commitments and the SOW
say is delivered, whatever their status. If it overturns the core of an older Decision, propose it as
superseding that one; if only a part, link it (supersession, above). `valid_from` is the earliest day
a source shows it agreed; a decision restated at a later meeting keeps the first day.

A decision taken while refining an Increment is a Decision note linked to the Capability it affects,
never only text in the Increment. Otherwise the next Increment on that Capability does not find it.

Architecture: a Decision links the Concerns it treats. The full evaluation (option analysis, spikes,
comparisons across models) lives in `tl/`, marked `authoritative: false`; the Decision carries the
summary and links there.

## Question (QUE)

`knowledge/questions/`. Owner: the BA; the TL for technical questions.

Something unresolved that blocks a named WBS line or needs the client. If we can decide it
ourselves, propose a Decision instead.

Distinctions: not a Requirement (a need), not a Decision (a conclusion).

Fields: `asks` (client or team), `answered_by` (the Decision or Requirement that records the answer).

Body: Question (one thing), What it blocks (a WBS line or a note), Options (if the answer is likely
one of a few), Answer (with its source).

Lifecycle: open while `answered_by` is empty; `index.md` lists the open ones. When answered, the
answer goes into the Decision or Requirement it links, and the Question becomes stable once
verified. Dropped: deprecated, with one line saying why.

## Term (TRM)

`knowledge/terms/`. Owner: the BA.

A word, abbreviation or concept with one meaning in this project: mud-engineering vocabulary, the
client's names for things, our own labels.

Distinctions: not a Requirement (it defines language and needs nothing); not a Concern.

Fields: `aliases`, one per line: synonyms, abbreviations, spellings.

Body: Definition (plain language), Context and units (the formula, the unit, where it applies), Not
to be confused with.

Lifecycle: stable when the BA confirms it, or the client's subject expert does through a source. A
renamed term keeps the old name in `aliases`.

## Commitment (COM)

`knowledge/commitments/`. Owner: the PMs.

What we owe the client, or the client owes us, by contract or explicit agreement: a deliverable, a
date, an acceptance step, a warranty, a reporting duty, a client dependency.

Distinctions: not a Requirement (product behaviour); not a Decision (our choice, which may create a
Commitment).

Fields: `party` (lint: us, client or both), `due` (a date or milestone, verbatim from the source),
`clause` (contract clause or annex, if any), `valid_from`, `valid_to`.

Body: What is owed, By when, How it is accepted, Drives (links to Requirements and Decisions).

Money: never the amount (lint). "Payment 3 on verified completion of month 3" is a fact; the figure
stays in the P&L.

Lifecycle: stable when a PM verifies it against the contract or the agreement. Changed by a change
request or an amendment: superseded, never edited.

## Capability (CAP)

`knowledge/capabilities/`. Owner: the PM and the TL together.

A lasting thing the product or platform must be able to do. It is the container the rest hangs on:
it has a basis in the Scope Baseline, the knowledge about it collects around it, and work is
planned against it. It may live across several milestones.

Distinctions:

- Not a Requirement. A Requirement is one testable need; a Capability groups the needs, constraints
  and decisions about one thing the system can do. One WBS line can feed several Capabilities, and
  one Capability can span several WBS lines.
- Not an Increment. A Capability lasts; an Increment is one result delivered against parts of one or
  more Capabilities in one iteration.
- Not a WBS line or an epic. The WBS is how presale priced the work; a Capability is how delivery
  understands it. Jira epics may mirror Capabilities, but the meaning lives here.

Fields:

- `kind` (lint): business, enabler or hybrid.
- `baseline` (lint, at least one entry once proposed): what justifies it, in the format above. A
  Capability with no basis is a change request candidate.
- `depends_on`: other Capabilities it needs, one link per line. Only the dependencies that matter
  for planning.

No delivery status, no progress field. How far a Capability is done is read from its coverage
criteria against the Increments done in Jira.

Body: What it must do, Coverage criteria (`C1`, `C2`... each a checkable line, the TL owns them),
Refined by (links to Requirements, Concerns, Decisions, Questions, Terms), Plan (which milestones it
starts, continues and completes in).

Lifecycle: stable when the PM and the TL confirm it. Split or merged by the curator: the old one is
deprecated with a pointer, never deleted.

## Increment (INC)

`knowledge/increments/`. Owner: the TL, with the PM.

One concrete result the team takes into an iteration and can demonstrate as a whole. It usually cuts
across backend, desktop, web and QA, and implements parts of several Capabilities.

Distinctions:

- Not a Capability (above).
- Not a Requirement. An Increment delivers parts of several Requirements; it does not state a need.
- Not a Jira story. The story carries status, sprint and assignee; the note carries what the result
  is, what it covers and why, and the story's key.

Fields:

- `capabilities` (lint, at least one once proposed): the Capabilities it implements parts of.
- `covers`: the coverage criteria it satisfies, as `CAP-002 C1`, one per line.
- `milestone`: the SOW milestone it targets, `M3`.
- `jira`: the issue key, once there is one.

No `status` beyond the note header's (lint refuses the state fields). Whether it is planned, in
progress or done is Jira's, and shows in the generated snapshot.

Body: Outcome, Demo, Acceptance criteria, Out of scope, Depends on.

Lifecycle: proposed when the TL has cut it; stable when the TL and the PM confirm the scope. Decisions
taken while refining it go to Decision notes (Decision, above).

## Risk (K)

`knowledge/risks/`. Owner: the PMs.

An uncertain event that would hurt delivery, scope, acceptance, the economy or the client
relationship. The PMO risk register is generated from these notes and filed as a Confluence page; it
is never edited there. Comments on the filed page come back through ingest.

Distinctions:

- Not a Concern (above).
- Not a Question. A Question asks; a Risk says what goes wrong if the answer is late or wrong. An
  open Question can be a Risk's cause.
- Not an issue. Something already happening is a blocker, `B-n`, in the PMO issue log.

ID: `K-n` (`K-1`, `K-2`), as the PMO register numbers them. Never renumbered, never reused. A
candidate from A01 keeps its own ID in `from`.

Fields:

- `register` (lint): client, or internal for the Opportunity and Internal Risk Register. An internal
  risk never appears in anything the client sees.
- `severity` (lint): high, med or low (probability x impact).
- `owner` (lint, required once proposed): `human:<id>`.
- `response` (lint): the standard's words - accept, mitigate, clarify, escalate, transfer, defer,
  monitor, re-estimate, re-align.
- `critical` (lint): yes or no, by the standard's list (project start, critical scope, roadmap,
  resources, budget, acceptance, client expectations, formal acceptance). Mark it before counting.
- `from`: the A01 candidate or problem ID it came from, if any.
- `capabilities`: the Capabilities it threatens.

No money amounts, as everywhere: the fact that the warranty is unpriced, not a figure.

Body: Risk (cause, event, effect), Why we think so (with sources), Response and next action, History.

Lifecycle: proposed when a PM has scored it; stable when the owner accepts it. Closed: deprecated with
the reason and the date. Materialised: deprecated with a pointer to its `B-n` in the issue log.

## Not types, on purpose

- Sprints, tasks, status, assignee, current estimates and hours spent: Jira and the P&L. They reach
  the KB only as a generated snapshot, never written by hand. Notes carry the issue key; an initial
  WBS estimate may be quoted as history (AGENTS.md rule 6).
- Blockers and issues: the PMO issue log. Notes link the `B-n`.
- Stakeholders: the A02 register.
- Tests: when QA joins, starting from the QA pipeline, each test item pointing at a Requirement.
