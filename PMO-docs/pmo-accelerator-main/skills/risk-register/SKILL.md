---
name: risk-register
description: Own the project's risk register and its issue/blocker log on a project that is ALREADY RUNNING - add to it, close things out, or check whether it has gone stale. Use whenever a risk or blocker comes up outside initiation - "add a risk", "log this as a risk", "what are the risks on X", "the client just told us something that worries me", "is this a risk or an issue", "we are blocked on Y", "close this risk", "review my risk register", "is my register up to date", "the risk register has not been touched in months", "who owns this risk", "which risks are critical", "add this to the register". A PM should never re-run an initiation step to log one risk. NOT the first build during initiation - if the project is in initiation and the register does not exist yet, `a05-a06-scope-and-risks` runs the scope interrogation first and then calls this skill. One of the PMO's mandatory project artifacts; the filed version lives in Jira or Confluence, never loose markdown.
---

# risk-register - the register, for the whole life of the project

A mandatory starting artifact. Built at A06 and then, in practice, never opened again - which is the
gap this skill exists to close. A register nobody has revisited is worse than none, because it
looks like the work was done.

One neighbour to keep apart: the **Opportunity & Internal Risk Register** (mandatory since Sep 2026) holds opportunities and Innowise-only risks and is never shared with the client. Same ID discipline, separate register - never move an internal-only item into this one, because this one can be client-visible.

This skill is the single definition of how the register works. `a05-a06` calls it to build the
first one and keeps only its own step framing; everything about IDs, structure, scoring and
maintenance lives here.

## Three modes

Every artifact skill has the same three: one that WRITES from scratch, one that CHANGES what is there, and one that AUDITS. The names are per artifact - `project-brain` calls its write mode `feed` and has a free `ask` read mode, because you do not "create" a notebook's contents. For this skill they are:

| Mode | The PM said something like | What you do |
|---|---|---|
| **create** (write) | a05-a06 is building it, or "we need a register for this project" | distil candidates into the live control set |
| **update** (change) | "add a risk", "we are blocked", "close K3", "this one got worse" | one item in or out, holding every convention |
| **review** (audit) | "is it current", "which risks are critical", nobody has looked in weeks | audit coverage and staleness, report, propose |

Reading the register needs no mode and no permission - just read it and answer.

`update` is the mode that does not exist anywhere else in the copilot, and it is the one a running
project needs weekly. Do not make a PM re-run initiation to add one risk.

**Called from another skill?** Do the named mode, hand back a one-line result plus the metrics,
and let the caller run its own checkpoint. Do not restage this whole flow inside someone else's.

## Before anything: find the register

Read `project-context.md` for its location. Otherwise look in Jira and Confluence - the filed
artifact lives in one of them. If none exists on a running project, say so plainly: that is a real
gap against the mandatory artifacts, not a formality, and it is worth naming rather than quietly creating one.

Never start a second register. If you find two, stop and ask which is live - a duplicate register
is how owners and severities silently diverge.

## The conventions - these are the part that breaks when people improvise

**Fixed ID prefixes, because other documents cite them.** A01 candidates are `R-n`. Register risks
are `K-n`. Blockers and issues are `B-n`. Critical scope is `CS-n` from A05. Do not renumber and
do not invent your own letters. The project description, the validation summary and the roadmap
all cross-reference these, so one PM using different prefixes breaks every reference in the
project. When adding to an existing register, read the last ID and continue the sequence - never
restart, never reuse a retired number.

**Row shape.** `K-n | risk | from (R-id) | impact area | severity (probability x impact:
high/med/low) | owner | response | critical? (Y/N)`.

**Risks and issues are different things and live in different places.** A risk is still potential.
An issue or blocker is already real and active. A blocked access or an undelivered dependency is
an issue, not a risk, and filing it as a risk means nobody chases it. There IS a real template for
the issue log: Issue Log Master File, Confluence 5057020108 + Sheet
`16Dl5Y1Tda6Rp8TIp5Ai8S2YHzQG8skPAskmsvQb_ZAg`, three tabs, stored in the Sensitive folder.

**Response vocabulary the standard uses:** accept, mitigate, clarify, escalate, transfer, defer,
monitor, re-estimate, re-align. Use these words rather than inventing a description.

**Traceability, and this is the one that gets skipped.** Every register row names the candidate it
came from. Every candidate that did NOT make the register gets a one-line disposition - merged
into K3, closed because X, judged not a risk, moved to the blocker log. Keep those in a
dispositions table under the register.

Why it matters, from the real Alchemy run: 31 candidates became 12 risks and 4 blockers, and
nothing anywhere records what happened to the other 15. Distilling is correct. Distilling without
a trail means nobody can show the 15 were considered rather than lost, and that question gets
asked in an audit, where "I remember thinking about it" is not an answer.

**There is no blank Risk Register template in PMO.** Say that rather than implying a house format
exists.

## Scoring - mark critical FIRST, then count

Two control metrics. Both are decision support for the PM, not a grade, and both are only as good
as their denominator - which is why the `critical?` column gets marked before anything is counted.

**What counts as critical, so the denominator is not a matter of mood.** An item is critical if it
can affect project start, critical scope, the roadmap, resources, budget, acceptance, client
expectations or formal acceptance - the standard's own list.

Apply it honestly. On the real Alchemy run only K1, K2 and K3 were counted, giving a tidy 100%,
while K10 ("contract not signed, blanks in the SOW") carries impact area "Commercial, start" and
plainly qualifies. Including it would not even have changed the score, because it had an owner and
a response - but choosing a small denominator is how a 100% gets manufactured, and the number is
worthless the moment anyone notices. Mark every row, then count.

- **Critical Control Coverage** = critical items with owner AND next action / total critical items
  x 100. Target 100% before formal project acceptance.
- **Critical Dependency Readiness Ratio** = critical dependencies with a responsible side AND an
  expected action / total critical dependencies x 100. Target >= 90% before the roadmap and
  resource plan are finalised. Count only dependencies that can materially affect start or
  feasibility.

An "expected action" needs a named side and a concrete next step. A DATE is not required for the
item to count, but a dependency with neither a date nor a defined trigger is not ready - say which
of the two it has. Report as `2 of 4 = 50%, two awaiting dates`, never as a word like "partial",
so the next PM scores the same register the same way.

No scorer script - the marked table IS the audit trail. Report both as `k of n` beside the
percentage.

## Mode: create

Distil into the LIVE, still-open control set - A01 candidates, A05 findings, and any existing risk
log. Keep closed and superseded risks in history, not in the register.

**Run the PMO Risk Library pass. Actually do it rather than treating it as optional.** Its whole
job is surfacing risks the PM has not thought of - domain, integration, client-side. It is in the
PMO Superbrain notebook `158e107b-0f3e-47b9-9566-f481595ab399`, source
`Knowledge-Base__Risk-Library-will-be-updated`; `Knowledge-Base__Project-Management-Risk-Framework`
in the same notebook carries the framework the register is meant to fit. Query the notebook rather
than searching Confluence blind.

Do not paste the library in. Use it as a prompt list and bring back only what applies, with a note
on why. If the notebook genuinely is not reachable, say so plainly and run the pass from first
principles instead of implying you consulted a catalogue.

CHECKPOINT: present the register, the dispositions table, the blocker log and both metrics.
"Here are the live risks, the active blockers, and the coverage - [k of n] critical items owned,
[k of n] dependencies ready. Anything wrong before I file it?"

## Mode: update

The everyday mode. Someone says something worrying in a call, a dependency slips, a risk becomes
real, a mitigation lands.

- **New item** - risk or issue first, then the next ID in sequence, then severity, owner,
  response, and the critical mark. An item with no owner is not finished; say so rather than
  filing it half-done.
- **A risk that has materialised** - it stops being a risk and becomes an issue. Move it to the
  blocker log with a pointer from its `K-n`, do not delete it. The history is the useful part.
- **Closing one** - record why and when, and keep it in history rather than deleting the row.
- **Severity changed** - say what changed and what that does to the two metrics. A severity move
  that flips something into critical without an owner is worth flagging in the same breath.

CHECKPOINT: "Adding [K-n / B-n]: [the row]. That makes it [k of n] critical items owned. Filing
it to [Jira / Confluence] - OK?" Then re-report both metrics, because a single addition can move
them, and hand the change to `project-brain` (feed mode) along with anything else the session
produced.

## Mode: review

Nothing else in the copilot does this, and it is what stops the register decaying quietly.

1. **Every critical item has an owner and a next action.** That is Critical Control Coverage, and
   the gaps are the finding.
2. **Staleness.** When was it last touched, and are there risks whose review date or trigger has
   passed with nothing recorded.
3. **Contradiction with reality.** Risks still open that plainly resolved, and issues on the board
   or in recent chat that never made the register. This is where a register is usually wrong -
   not corrupt, just behind.
4. **Convention drift.** Renumbered IDs, missing dispositions, a second register.

Report what a PM would get wrong by trusting it as it stands, then offer to fix the specific rows.
A review that ends in a diagnosis and no proposed action generates a question instead of answering
one.

CHECKPOINT: "Last touched [date]. [k of n] critical items have an owner and a next action -
[the gaps]. [N] things on the board or in chat never made the register. Want me to fix these
rows?"

## Where it lives, and where it lands

The filed artifact goes to Jira or Confluence - a mandatory starting artifact - not loose markdown. Markdown in
the project folder is a working draft; say which one you are producing.

Every write to the filed register is gated: show the rows going in or changing, get an explicit
yes. Then record the register's location and any decision in `project-context.md`, put anything
needing action in `pm-tasks.md`, and offer the register to `project-brain` (feed mode). Risks are
ordinary project knowledge - no money, no contract text, so there is no hold-out argument here.
