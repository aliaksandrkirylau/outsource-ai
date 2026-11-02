# HANDOFF — <project name>

Updated **<YYYY-MM-DD>** by the dispatcher. The map every agent reads on
entry. Rules and architecture: `CLAUDE.md` and `PROJECT-PROFILE.md`. Here:
**what is happening now, where things are, how to run the work.**

## 1. Now

- Current phase and goal.
- Tickets in flight: key, stage, status, branch / PR, waiting on whom.
- Last accepted work (key, commit / PR, date).

## 2. Delivered

What has been accepted, by phase, with commit / PR references and the state
of the regression set.

## 3. How to triage a bug report

1. Accepted behaviour? → `ACCEPTED-BEHAVIOURS.md`, `DECISIONS.md`.
2. Literal client spec? → `SPEC-DISCREPANCIES.md`.
3. Already known? → grep `FINDINGS.md`, `BACKLOG.md`.
4. Which environment reproduces it, and does local match it (data, code)?
5. A defect → a tracker ticket (opened by the PM), then the normal pipeline.

## 4. Pipeline notes for this project

Anything project-specific about running the stages: which implementer for
which kind of ticket, what the tester must hand to QA, parallelism limits.

## 5. Document map

| File | What | Who updates |
|---|---|---|
| `PROJECT-PROFILE.md` | stack, verification, environments, roles | project analyst |
| `DECISIONS.md` | decisions in force | dispatcher |
| `FINDINGS.md` | found and not fixed | all agents, append-only |
| `SPEC-DISCREPANCIES.md` | client spec defects | researcher, implementer |
| `BACKLOG.md` | our work without a ticket | implementer |
| `ACCEPTED-BEHAVIOURS.md` | not-a-bug list | dispatcher |
| `tickets/` | spec of the ticket(s) in flight | researcher, reviewers |
| `docs/archive/tickets/` | specs and reports of done tickets | dispatcher |

## 6. Verified-claim rule

Every claim handed over between agents is written so it can be re-checked:
with a date, a file and a line, or a command and its output. The receiving
agent re-checks, it does not build on the description.
