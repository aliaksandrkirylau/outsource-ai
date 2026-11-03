# Output shapes - A07 and A08 (skeletons only)

Structural skeletons. NOT the control contract - the authoritative Inputs / Outputs / Verification Criteria / Control Metrics live in the standard (A07 = Confluence 4619207137, A08 = 4619206956) or `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`.

Note what is NOT here: an economy calculation. The copilot does not compute margin, revenue or profitability - it has no validated rates or cost model on a new project. It fills the economy file with the planned hours, and the PM and the PMO Resource Manager form their judgement from what the FILLED file computes. Order matters: plan, fill, then judge. What the copilot produces is the plan, the assumptions behind it, and the record of what came back.

## A07 - Roadmap + role-by-month plan (shareable; hours OK, no money)

```
# <Project> - Phase <n> roadmap + role-by-month plan

## Planning basis
- Hour basis: MAX (default - the safe envelope for a T&M cap, not the expectation)
  or min / mid / risk-blend if the PM changed it, with the reason
- Capacity, ramp, front/back-load, cap discipline, dependency order (see planning-rules.md)
- Two calls the PM made: oversight billed or absorbed; QA as its own line or folded in

## Phases
| Phase | Window | Focus | Lead roles | CS-ids covered |

## Milestones and checkpoints
| Milestone / checkpoint | Target date or period | Type | Responsible side |
(include demo / review / UAT / acceptance / release validation, environment readiness
 points, and required client inputs, approvals, access and decisions. Every critical
 environment or client-input point needs a RESPONSIBLE SIDE and an EXPECTED DATE, or an
 explicit "unowned - routed to X". A box with nobody against it is not a dependency.)

## Role x month hours  (this IS the preliminary resource plan at this stage)
| Role | Seniority | <Mon1> | <Mon2> | <Mon3> | ... | Total |
(month and role totals stay consistent when a role is added / removed / rescaled.
 The formal Project Resource Plan 3.0 comes after staffing - not this document.)

## Critical path
- the long pole, named, and what slipping it costs

## Options log
| Variant | Basis | Role mix | Window | Result | Why not taken |
(every iteration, so nothing gets re-litigated and A08's assumptions write themselves)

## Notes / watch-items
- the peak month to protect; critical-path input slips; unlocked scope that could move hours
- Critical Scope Roadmap Coverage: k of n = 100%? - name the CS-ids
- Resource Timeline Coverage: k of n = X% (target >= 90%)
```

## A08 - Economy assumptions and concerns + hand-off record

Hours and assumptions, no figures - so this can live in the project folder. The calculation itself lives only in the economy file.

```
# <Project> - Economy assumptions, concerns and hand-off (A08)

## Hours check (no money)
- Plan total: <h> against WBS envelope <h> - within / over by <h>
- Against the cap, where the cap is expressed in hours: <read>
- Peak month and whether any role exceeds one realistic person-month

## What went into the economy file
- Tab and dated copy: <name>
- Months written, by column letter, confirmed from a live header read: <letters>
- Written: paid (billable) AND worked hours, plus role labels. Rates, salary, tax
  residency and grade untouched.
- Paid = worked for all roles EXCEPT: <role> absorbed, zero paid, because <reason>
- Billable total <n>h vs plan <n>h vs contract <n>h - tied? yes / no + attribution
- Worked total <n>h; absorbed gap <n>h (expected where a role is unbilled)
- Resource-to-Economy Coverage: k of n role-periods present - name any that did not make it

## Economy assumptions  (mandatory output where applicable)
- from the options log, and from A05's flagged estimate assumptions
- flag any place the plan relies on unrealistic staffing, seniority, allocation, or
  UNPAID work - the standard makes that a revise-before-validation trigger

## Concerns raised
- ...

## Hand-off to the PM + RM
- Handed over on <date>. Owner: <PM> with <RM>.
- Comparison the PM should make: how does this compare with what PRE-SALE assumed?
  (a distinct check from "does it fit the cap", and the one that catches quiet degradation)

## What came back  (fill in when it does - A09 cannot run without this)
- Classification: healthy / questionable / risky / negative / acceptable only with
  strategic justification
- If weak: the documented justification, and the NAMED owner of realising that value
- Escalated to Head of PMO / Delivery management? (required before baseline validation
  completes if the result is below target, negative, or materially worse than pre-sale)
- Date, and who worked it
```

Reminder: the A07 roadmap and role-by-month hours can be shared and synced to the brain. Anything with a currency figure, rate, salary or margin cannot - it lives only in the sensitive Drive, and the hours write is hard-gated (confirm columns from a live read, verify totals after).
