# A09 output shapes

Skeletons only. The control contract - outputs, verification criteria, the metric - lives in
`${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`, section A09. These are shapes, not the contract.

There is no PMO template for any of this; the template register confirms it. Say that to the PM rather than
presenting these structures as house standard.

---

## 1. The leadership summary (the artifact)

ONE PAGE. Leadership scans this for flags and decides whether to open staffing; the detail is one
click away for anyone who wants it. Hours are shareable. Money is not - no figures, no P&L link.

```
# <Project> - baseline summary for start approval        <date>

## What this is
<two lines: what the project is, what we are delivering. Not the vision statement.>

## Size
Hours: <n> over <period>.  Contract: <signed / in signing / blanks outstanding: what>.
A03 contract review: <done / not done>.

## PM's readiness call
READY / READY WITH CONSTRAINTS / NOT READY
<why, in the PM's own words. This is the PM's judgement, not the copilot's.>

## Flags
RED    - <the things that could stop this>
AMBER  - <the things to watch>
GREEN  - <what is genuinely solid>

## Main risks (top 3-5, from A06)
| K-id | Risk | Severity | Owner |

## Main strengths
- <what is actually solid. A page of only problems misreads a healthy project.>

## How we are taking this project
<value classification in one line> - value owner: <named person>
(rationale and extraction hypothesis in the annex)

## Economy
<classification word from A08, no figures> - posted in the Economy chat.
(PM confirmed posted: yes/no. Never a link to the file.)

## What has been prepared
| Document / analysis | Step | Where |
(the route into detail - from the output list in project-context.md)
```

Do not pad this to look thorough. A page that gets a decision beats a package nobody opens.

---

## 2. Value classification

```
Classification:   profit-oriented | marketing / reference / market-entry / client-development |
                  technical or domain expertise acquisition        (one or a combination)

Economy read:     healthy | questionable | risky | negative | acceptable only with strategic justification

Rationale:        why this classification, in the PM's own words, specific to this project.
                  If the economy is weak, this is MANDATORY and must be attributable to whoever made the call.

Value extraction hypothesis:
                  Required whenever the classification is not purely profit-oriented.
                  How does the non-financial value actually get realised?
                  What has to happen, by when, for it to be real?

Value owner:      a NAMED person who owns realising it.
                  "Marketing" is not an owner. "Nobody currently owns this" is a valid and useful answer -
                  record it as such rather than leaving the field blank.
```

A classification with no owner and no hypothesis is the failure mode this section exists to prevent. Surface it; do not fill it in to look complete.

---

## 2b. Reviewer routing (fix this BEFORE the ask goes out)

It is the denominator for Stakeholder Validation Coverage. Deciding which areas needed a reviewer
after you know which ones were read is how a 100% gets manufactured.

| Area | Reviewer (name + role) | Sent | Reviewed |
|---|---|---|---|
(go/no-go -> Head of PMO or Delivery; client commitments and contract -> Account / Sales;
 technical feasibility -> DM or Tech Lead; contested staffing -> RM; economy -> via the
 Economy chat, never via this document)

---

## 3. Internal Stakeholder Validation Outcome (mandatory)

```
Date:             
Requested:        <date sent, deadline asked for>   <- record this at ask time, not after
Reviewed with:    name - role - which areas they reviewed
Outcome:          EXACTLY ONE of
                    approved to continue
                    approved with constraints
                    requires rework
                    paused
                    rejected - not accepted
Evidence:         link to the mail thread or chat message where the decision was actually given
```

If the outcome is **approved with constraints**, every constraint is listed:

| # | Constraint | Owner | By when | Where it is carried forward |
|---|---|---|---|---|

Constraints that are not written down become "approved" within a fortnight. That is the whole reason this table exists.

If no decision has come back, the outcome field stays empty and the record says "pending, requested [date]". Never infer approval from silence.

---

## 4. Client Baseline Validation Outcome (mandatory)

```
Date:             
Confirmed by:     name - role
Channel:          contract / SOW | email | meeting follow-up | other agreed written channel
Outcome:          confirmed | requires clarification | requires rework
Evidence:         link
```

Objections raised, and where each is routed:

| # | Objection | Impact area | Routed to |
|---|---|---|---|

No internal economy, margin, rate or cost figure appears anywhere in the client-facing package or in this record.

---

## 5. Decision record (the assembled artifact)

Lives in the project folder. Frontmatter carries `type: decision-record`, `step: A09` and the date.

```
# A09 baseline validation - <Project>

Decision date:
Pre-gate readiness at the time:        X of 7 (A01-A08)
Stakeholder Validation Coverage:       N of M areas (P%)

## Internal outcome
<one of the five, with constraints table if applicable>

## Value classification
<classification, economy read, rationale, extraction hypothesis, named owner>

## Client outcome
<confirmed / requires clarification / requires rework, with evidence link>

## What this unblocks
<A10 staffing and A11 setup open / blocked, and what would have to change>

## Open points carried forward
| # | Open point | Area | Owner | Next action |

## Caveats
<any baseline area that was thin or unreviewed at the time of the decision, stated plainly>
```

The Caveats section is not optional padding. A gate passed over a thin A08 is a different decision from one passed over a complete baseline, and in six months only this record will remember the difference.
