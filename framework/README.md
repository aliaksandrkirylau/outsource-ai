# framework — reusable pipeline assets

Stack-agnostic prompts and templates, generalized from the reference project
(ADAPT). Source templates, not active here: they are installed into a target
project.

## Contents and status

| Asset | Pipeline stage | Status |
|---|---|---|
| `commands/draft-ticket.md` | 2 — research & draft | proven on ADAPT, generalized |
| `commands/work-ticket.md` | 4 — implementation | proven on ADAPT, generalized |
| `commands/verify-epic-plan.md` | future BA/PM stage | proven on ADAPT, generalized |
| `skills/verification-before-completion` | all | proven on ADAPT, generalized |
| `skills/systematic-debugging` | 4, 5 | proven on ADAPT, generalized |
| `agents/researcher.md`, `agents/spec-reviewer.md` | 2, 3 | proven as roles (Opus reviewer agents + separate review session) |
| `agents/implementer-*.md` | 4 | proven as roles (Sonnet worker agents) |
| `agents/lookup.md` | any | proven (Haiku lookup agent) |
| `agents/project-analyst.md` | 0 — project onboarding | **proposed** |
| `agents/code-reviewer.md` | 5 — code review & cleanup (before testing) | **proposed** |
| `agents/tester.md` | 6 — testing the final, reviewed code | **proposed** |
| dispatcher | 1, 7, hand-offs | **not written** — decided: an Opus agent with a narrow mandate (`docs/decisions.md` D19) |
| `project-templates/*` | knowledge layer | generalized from ADAPT's documents |

Not yet written: commands for the proposed stages (onboard project, review
spec, test ticket, clean up, package PR) — their mandate currently lives in
the agent definitions.

## Installing into a target project

`<project>` is our private **workspace repository** for the client project: it
holds the knowledge layer, and the client's repositories are working copies
inside it, so none of these files land in client code. Install into a client
repository only if the profile says the client agreed.

| From | To |
|---|---|
| `agents/*.md` | `<project>/.claude/agents/` |
| `commands/*.md` | `<project>/.claude/commands/` |
| `skills/*/` | `<project>/.claude/skills/` |
| `project-templates/ticket-spec.md` | `<project>/tickets/_template.md` |
| other `project-templates/*.md` | `<project>/` root, filled in by the project analyst |

Commands and skills refer to project facts only through `PROJECT-PROFILE.md`
fields and the standard file names (`FINDINGS.md`, `BACKLOG.md`,
`SPEC-DISCREPANCIES.md`, `DECISIONS.md`, `ACCEPTED-BEHAVIOURS.md`,
`TRACKER.md`, `HANDOFF.md`, `tickets/`). Keep it that way: a project-specific
value in a framework file is a bug.
