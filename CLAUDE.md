# CLAUDE.md

Guidance for Claude Code sessions opened in this folder.

## What this project is

**outsource-ai** designs an AI-agent development workflow for outsourcing
projects: a ticket is picked up from the tracker (Jira), researched, specified,
reviewed, implemented, tested, cleaned up and turned into a pull request by
agents. **The only human step in the target flow is accepting the PR.**

It is **not** a codebase of a client project. It is a knowledge base plus a
reusable framework, distilled from a real project where this workflow was run
by hand — **ADAPT** (`/Users/user/prog/work/ADAPT`, a 4-service outsourcing
project; see `docs/06-adapt-case-study.md`). Everything here must be **stack-,
domain- and client-agnostic**: no ADAPT names, collections, endpoints or tools
in the framework. Project-specific facts belong to a per-project
`PROJECT-PROFILE.md` (template in `framework/project-templates/`), never to the
framework itself.

Read `HANDOFF.md` first — it is the map: current state, the owner's decisions,
what is next.

## Current goal

Phase 1 of `docs/07-roadmap.md`: a **high-level presentation / demo for
management** (head of DM/PM, possibly delivery director and CTO), in
**Russian**, showing visually — understandable to non-technical people — the
stages a ticket goes through in the agent workflow. No economics (hours,
tokens, money) at this stage, by owner decision.

## Layout

| Path | What | Language |
|---|---|---|
| `HANDOFF.md` | State, owner's answers, decisions, next steps | RU |
| `docs/01-vision.md` | Goal, audience, principles, boundaries | RU |
| `docs/02-target-workflow.md` | The target pipeline: stages, statuses, gates, branches | RU |
| `docs/03-agent-roster.md` | Agent roles: model, effort, inputs/outputs, limits | RU |
| `docs/04-knowledge-layer.md` | What every project must carry so agents can work on it | RU |
| `docs/05-lessons-learned.md` | Lessons from running the workflow by hand, as principles | RU |
| `docs/06-adapt-case-study.md` | How the workflow ran on ADAPT, as-is → to-be mapping | RU |
| `docs/07-roadmap.md` | Development stages of the system (no dates, no economics) | RU |
| `docs/08-open-questions.md` | Open design questions, grill-session backlog | RU |
| `docs/decisions.md` | Decision log (D1, D2, …) — append, never rewrite | RU |
| `framework/` | Reusable, stack-agnostic assets generalized from ADAPT; `framework/README.md` = index, proven/proposed status, install map | EN |
| `framework/agents/` | Agent definitions (model/effort frontmatter + prompt) | EN |
| `framework/commands/` | Slash-command prompts: draft, verify plan, implement | EN |
| `framework/skills/` | Skills: verification-before-completion, systematic-debugging | EN |
| `framework/project-templates/` | Files a target project carries (profile, handoff, journals) | EN |

`framework/` is deliberately **not** `.claude/`: these are source templates to
be installed into a target project, not commands active in this repository.
Do not move them into `.claude/` here.

## Rules

- **Language.** Human-facing documents (`HANDOFF.md`, `docs/`, the
  presentation) are in Russian — the owner and the audience are Russian
  speaking. Agent-facing prompts (`CLAUDE.md`, everything in `framework/`) are
  in English.
- **Stack-agnostic.** If a sentence in `framework/` only makes sense for one
  language, database, tracker or client, it belongs in a `PROJECT-PROFILE.md`
  field instead. Name the field, not the value.
- **Mark what is proven and what is proposed.** The ADAPT-derived parts
  (draft → review → implement, findings routing, verification discipline)
  were run for real. Stages that did not exist on ADAPT (automatic pickup,
  tracker transitions, tester agent, cleaner agent, PR creation, project
  onboarding) are proposals: say so in the docs.
- **Decisions are logged.** Every owner decision goes to `docs/decisions.md`
  with a date; `HANDOFF.md` only points to it.
- **Do not touch ADAPT** from sessions opened here, except to read it. Nothing
  for this project is written into the ADAPT folder.
- **No economics yet** — no hour, token or cost estimates in any document
  until the owner asks for them.
- **No git write commands** (commit, branch, push) unless the owner asks. Repo:
  private `github.com/aliaksandrkirylau/outsource-ai`, branch `main`.
