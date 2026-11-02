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

Knowledge layer location: our workspace repository (default) / the client's
repository (only with the client's consent — name who agreed and when).

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

Documentation sources (tracker, wikis, drives, …): agents may read all of
them. They write only to their own pages and technical notes, listed here;
business and PM documentation (specifications, requirements, plans, client
documents) is read-only for agents.

| Source | Access | Agents' own pages / notes location |
|---|---|---|
| | read | |

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

This list is the owner vocabulary for `FINDINGS.md` and the escalation
routing table: an open question goes to the role whose "Answers escalations
about" covers it (requirements, technical/architecture, environments and
access, …), as a tracker comment mentioning that person. If no row matches, it
goes to the PM.

## 11. Tracker

- Tracker, project key, how agents access it (API / snapshot `TRACKER.md`).
- Pipeline stage → tracker status mapping:

| Stage | Status |
|---|---|
| research | |
| spec review | |
| needs info | |
| in development | |
| code review | |
| testing | |
| ready for QA (closed env) | |
| PR review | |
| waiting for stage QA (if any) | |
| done | |

- After merge: `done` (default) or `waiting for stage QA` if the project has
  QA on a stage environment — then QA sets `done`. A defect found after merge
  is a new bug linked to the ticket; a merged ticket is never reopened.
- Agent identity: agents act in the tracker and git under the account of
  developer <name>. What they may and may not do there is set by the
  framework rules and section 7, not by account permissions. Agent actions
  carry no AI marker: no prefixes in comments, no labels on PRs, no AI
  attribution in commits.
- Ticket pool: tickets of the current sprint in status <"to do" status>,
  assigned to that developer. The dispatcher picks from this pool only; it is
  started by a human and runs until the pool is empty or every remaining
  ticket is waiting for an answer.

## 12. Pipeline limits

- Returns per loop before escalation (spec review → draft, code review →
  implementation, testing → implementation): **2** by default. The third
  return in the same loop escalates to a human.
- Parallel tickets: at most **2** at a time (pilot default). Within this
  ceiling the dispatcher decides what can run in parallel.
- Escalation reminder: if an escalation has no answer after **2** working days
  (default), the dispatcher posts one reminder mentioning the PM; after that
  the ticket just waits. A waiting ticket keeps its branch and frees its queue
  slot.
- Shortened paths: every stage is mandatory unless a row here says otherwise.
  The dispatcher never skips a stage on its own judgement.

| Ticket type (how it is recognised) | Stages skipped | Why |
|---|---|---|
| | | |

## 13. Git

Default: one branch and one pull request per ticket. If the client's process
differs (shared branch, several tickets per PR, …), describe it here — it
overrides the default.

Branching model, branch naming, PR target, merge method, who merges, what
agents may do.
