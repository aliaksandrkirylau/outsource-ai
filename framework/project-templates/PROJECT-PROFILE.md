# PROJECT-PROFILE — <project name>

> Written by the project analyst (stage 0), refreshed when the project changes.
> Every field is filled from a named source or marked
> `UNKNOWN — asked <who>, <date>`. No plausible guesses.
> Every number carries a date: data gets reseeded, baselines drift.

**Last refreshed**: <YYYY-MM-DD> · **Sources**: <repos, docs, people asked>

## 1. Product

- What the product does, for whom, in two or three sentences.
- Client, domain, contract frame (fixed scope / T&M / phase), what is under
  acceptance and what is not.

## 2. Components

| Component | Repo / path | Stack | Role | Own rules file |
|---|---|---|---|---|
| | | | | |

How they talk to each other (one diagram or a call chain), and which layer
owns which concern (validation, envelope, persistence, auth).

## 3. Verification matrix

| Layer / component | Build | Tests | Lint / types | Live check | Baseline (date) |
|---|---|---|---|---|---|
| | | | | | <N passed, M known failures> |

- **Regression set**: <name, where it lives, how to run before/after, what a
  regression is>
- **Known red** (failing before any change, not ours): <test, since when>

## 4. Environments and test data

| Environment | Reachable by agents? | How | Data | Write allowed? |
|---|---|---|---|---|
| local | | | | |
| staging | | | | |
| client-only / closed | no | — | — | — |

- Test accounts and test entities (by reference, never secrets in this file).
- **Closed-environment checks** → handed to human QA with a manual test plan.

## 5. Sources of truth and their priority

| Priority | Source | What it decides |
|---|---|---|
| 1 | <client specification, version, date> | formulas / business rules, literally |
| 2 | `DECISIONS.md` | how ambiguous spec points are read |
| 3 | code | where a document disagrees, the code wins and the disagreement is recorded |

## 6. Conventions and hard rules

- Code style, naming, comment density, language of user-facing strings.
- Forbidden patterns (e.g. fabricated fallbacks, swallowed errors, hidden
  retries, renaming environment variables, ticket keys in comments).

## 7. Forbidden actions

Destructive or outward-facing actions agents never take, and who does them
instead (e.g. production data operations, deploys, writes to shared data).

## 8. Known, intentional breakage

What looks broken but is decided — "do not fix", with the decision's date.
Behaviours that are accepted and must not be reported as bugs:
`ACCEPTED-BEHAVIOURS.md`.

## 9. Known traps

Root causes that already bit this project and fail silently (misspelled names,
missing tenancy fields, derived values, envelope differences, time zones…).
The debugging skill checks these first.

## 10. People and roles

| Role | Person | Owns | Answers escalations about |
|---|---|---|---|
| Developer (ours) | | | |
| PM | | | |
| BA | | | |
| QA | | | |
| DevOps | | | |

This list is the owner vocabulary for `FINDINGS.md`.

## 11. Tracker

- Tracker, project key, how agents access it (API / snapshot `TRACKER.md`).
- Pipeline stage → tracker status mapping:

| Stage | Status |
|---|---|
| queued for AI | |
| research | |
| spec review | |
| needs info | |
| in development | |
| testing | |
| ready for QA (closed env) | |
| cleanup | |
| PR review | |
| done | |

## 12. Git

Branching model, PR target, merge method, who merges, what agents may do.
