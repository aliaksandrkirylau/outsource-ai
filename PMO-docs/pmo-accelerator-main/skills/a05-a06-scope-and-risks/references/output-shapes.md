# Output shapes - A05 and A06 (skeletons only)

Structural skeletons for consistent output. NOT the control contract - the authoritative Inputs / Outputs / Verification Criteria / Control Metrics live in the standard (A05 = Confluence 4619206785, A06 = 4619206806) or `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`. Use those for "done"; these for layout.

## A05 - Validation summary (+ roles + critical scope)

```
# <Project> - Pre-sale scope / estimate / economy validation (A05)

## Required Project Roles List
| Role | Seniority | Why needed (critical scope) |

## Work-category completeness
| Category | In the WBS? (yes / N-A + reason / MISSING) | Note |
(analysis-BA, architecture, UI-UX, implementation per component, integrations, data and
 migration, QA and test design, automation, DevOps and environments, security,
 documentation, deployment and release, UAT support, handover and training, PM.
 A named role is not the same as estimated work.)

## High-Level Critical Scope with Acceptance Criteria (MVP)
| CS-id | Critical scope area | Acceptance criteria (observable) | Ours / client-side |
(CS-1, CS-2, ... - stable ids, cited by A05's own metric caveat and later by the roadmap)

## Pre-Sale P&L (reference only)
(pointer to the sensitive P&L; economy detail is A08; NO money in this file)

## Validation summary
- Sold scope vs context: ...
- Critical scope: CS-1..CS-n identified; each linked to the MVP goal + has an estimate
- Roles / capability: validated with the tech lead ...
- Estimates: <range>; CAVEAT - which big lines rest on unvalidated assumptions
- Economy: <model> - acceptable pending ...
- Assumptions: client owns X; client provides Y; ...
- Delivery approach: iterative / cadence / duration - fit for the context?
- Estimates reviewed by: <name, role, date> - or NOT YET REVIEWED, owner <name>
  (a verification criterion; the copilot's own read does not satisfy it)

## Re-estimation / clarification needs (route to owner)
1. ... (-> client / Sales / tech lead / kickoff)
   (mark any that could change SOLD commitments as a CR candidate - never absorbed)

## Control metric (A05)
- Critical Scope Estimate Coverage: k of n = X% (target >= 80%) - list the CS-ids counted
  (flag any "covered" area whose estimate rests on an unvalidated assumption)
```

## A06 - Risk register + issue/blocker log

**The register and blocker-log shapes are NOT here. They live in the `risk-register` skill, which owns them.** Row shapes, the fixed ID conventions, the dispositions table, the risk-versus-issue split and both control metrics are defined there and nowhere else.

This file used to carry a full second copy. It was removed on 2026-09-03 because the two copies had already drifted - one said "Critical Dependency Readiness", the other "Critical Dependency Readiness Ratio" - which is precisely the failure the single-definition rule exists to prevent. A reference file is the worst place for a duplicate, because nobody re-reads it when editing the skill.

If you need the shapes, call `risk-register`. Do not paste them back in here.

What A06 still owns, and what belongs in this file:

```
## Assumptions / constraints updated
- ... (what the validation changed, and which A05 assumption it came from)

## Clarification items / CR candidates
| Item | Could change sold commitments? | Owner | Status |
(anything that might change what was sold - NEVER absorbed into baseline scope)

## Control metrics (A06) - REPORTED here, DEFINED in risk-register
- Critical Control Coverage: k of n = X% (target 100%) - name the rows counted
- Critical Dependency Readiness Ratio: k of n = X% (target >= 90%) - name the deps, and for
  each short one say whether it lacks a responsible side, an action, or a date/trigger
```
