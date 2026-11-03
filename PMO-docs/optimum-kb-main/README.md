# Optimum KB

The team's knowledge base for Optimum Engineering Standards: what the client agreed, what we
decided and why, what we owe, what is still open. Internal to the team. Tasks and status live in
Jira; this holds what Jira cannot.

v0: local only. There is no shared server yet.

## Setting up, once

1. Install Git for Windows (on a Mac, Apple's command line tools), Obsidian, and your AI agent
   (Claude Code or Codex). Nothing else is needed.
2. Clone into a short folder, such as `C:\kb\optimum`. Deep folders hit Windows' path limit.
3. Double-click `check-kb.cmd` (Mac: `bash tools/kb-doctor.sh`). Fix what it lists and run it again
   until it says "all set". `bash tools/kb-doctor.sh --fix` applies the git settings for you.
4. Tell git your role, so a sync warns you when you edit outside it:

   | Role | Run once |
   |---|---|
   | PM | `git config kb.territory "pm/ knowledge/commitments/ knowledge/decisions/ knowledge/risks/ knowledge/capabilities/ knowledge/increments/"` |
   | BA | `git config kb.territory "ba/ knowledge/requirements/ knowledge/questions/ knowledge/terms/"` |
   | Tech lead | `git config kb.territory "tl/ knowledge/concerns/ knowledge/decisions/ knowledge/capabilities/ knowledge/increments/"` |
   | QA | `git config kb.territory "qa/"` |

5. Open the folder in Obsidian: vault switcher, "Open folder as vault". Check that Settings, Core
   plugins, Templates is on.
6. Open Claude Code in the folder once and accept the trust prompt; until you do, it ignores the
   team's rules. Codex users: `tools/codex.md`.
7. Start agent sessions on the KB folder itself, not in a git worktree. The Claude desktop app may
   start a session in a worktree on a side branch; turn that off for this folder. Sync refuses any
   branch but main, so work done in a worktree reaches nobody.

## Every day

- Say "sync" to your agent when you start, when you stop, and after processing a meeting. Without
  an agent, double-click `sync-kb.cmd`.
- After a meeting: "process this meeting", with the transcript. You get a list of proposed changes;
  nothing becomes knowledge until you approve it.
- A question about the project: ask your agent. It answers from here, with sources.
- Before a session: "prepare for the workshop on ...".
- Sync says DISPUTED: someone changed the same passage at the same time. Your agent shows both
  versions and you decide.
- Sync says STOPPED: nothing was shared and your work is safe. Tell Anton.

## What goes in, and what never does

In: every meeting (recorded), document and piece of client material, and anything that affects
decisions or delivery.

Never: money amounts (the fact goes in, the figure stays in the P&L), CVs or personal data beyond
names and roles, passwords or keys. Big files stay in Drive; the KB holds a rendering and the link.

## How it is organised

- `sources/`: what came in, never edited.
- `knowledge/`: nine kinds of note - capabilities, requirements, concerns, decisions, questions,
  terms, commitments, increments, risks. Each has a status; only a person can make a note `stable`.
  The PMO risk register, and later the roadmap and specs, are generated from these notes.
- `index.md`: the list of every note, plus what needs a decision. Generated, so do not edit it.
- `pm/`, `ba/`, `tl/`, `qa/`: each role's own working space.
- The rules the agents follow: `AGENTS.md`. The note types: `schema/types.md`.

Anton is the curator: anything STOPPED, renames, new types, and the rules themselves.
