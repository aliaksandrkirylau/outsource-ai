---
synced: 2026-07-28
---
# Where an instruction belongs

Four files load into a PM's session automatically. They have different owners and different lifecycles, and putting something in the wrong one means it either gets overwritten on the next plugin update or it never applies where the PM needed it.

| File | Owner | Overwritten when | What belongs in it |
|---|---|---|---|
| `<workspace>/.claude/rules/pm-copilot-baseline.md` | the copilot | copilot-setup is re-run | how the copilot behaves, the PMO process it follows, the gates |
| `<workspace>/.claude/rules/pm-profile.md` | the PM | never | who they are, portfolio and aliases, mode, their people, where things live |
| `<workspace>/CLAUDE.md` | the PM | never | their own general working preferences, anything that should outlive the plugin |
| the GLOBAL layer - see the caveat below | the PM | never | preferences that follow them into every workspace and project, plus the copilot pointer block |

A plugin update brings new skills straight away, but it does NOT refresh the workspace copies of the baseline or the reference pack. Those move only when the PM re-runs copilot-setup, which is the single maintenance action and is safe to repeat.

## The two files that are not instructions

`<workspace>/pm-copilot-references/` holds the standard, the artifact checklist, the templates and the conventions. It is a copy of the plugin's pack, made at setup, refreshed by standards-sync. It has to exist in the workspace because the always-on rules file is loaded OUTSIDE any plugin context, so `${CLAUDE_PLUGIN_ROOT}` does not expand there - a pack that only exists inside the plugin folder is unreachable from the always-on layer, and the copilot quietly falls back to reciting the standard from memory.

`<project folder>/project-context.md` holds per-project facts. Not an instruction file, read at the start of any work on that project.

`<workspace>/pm-tasks.md` is one task list across the portfolio, project-tagged, and the destination for anything a skill turns up that needs doing. Workspace level rather than per project on purpose: the PM's daily question spans projects. If they already keep a task file, adopt it instead of adding a second.

`<workspace>/copilot-feedback.md` is the alpha log.

None of these four are instructions and none of them belong in a rules file. Keep facts in them and behaviour in the baseline.

## Why a pointer block in the global CLAUDE.md

A Cowork project rooted at a subfolder does not load its parent's `.claude/rules/`. So a PM who opens a space at `projects/<Client>/` instead of at the portfolio root loses the baseline and their profile silently - no gates, no conventions, and no idea the reference pack exists.

The global layer loads in every workspace and every project, so a short block there naming the real paths is what makes the rest findable. It is a pointer, not a copy: never duplicate the baseline's content into it.

**Where that layer lives depends on the surface, and only one of the two is a file you can write.** Observed 2026-09-03.

- **Claude Code (the Code tab):** a real file at `~/.claude/CLAUDE.md`. Append to it.
- **Cowork:** app-managed. No file exists at `~/.claude/CLAUDE.md`. The content is materialised per session into `.../local_<uuid>/.claude/CLAUDE.md` and rewritten at session start - one machine held 541 such folders, each with an identical copy. A write into any of them survives only until the session ends, and looks successful the whole time. The only durable route is the app's own personal-preferences setting, which means handing the PM a paste block rather than writing for them.

So: probe for the real home-path file before writing. Never write into a `local_<uuid>` path, and never report the pointer block as installed from a write you cannot read back in a later session. The same trap in a different costume as `${CLAUDE_PLUGIN_ROOT}` not expanding outside a skill - a path that is real on one surface and silently absent on the other, failing quietly rather than loudly.

For a PM who genuinely wants per-project workspaces, the cheaper alternative to reinstalling everywhere is a one-line `CLAUDE.md` in each project folder that `@`-imports the portfolio baseline by relative path. Imports resolve relative to the importing file and go four hops deep.

Routing rule when something needs writing down:

- Copilot or PMO process behaviour goes in the baseline. Which also means it is not the PM's to edit - a request to change it is a feedback-log entry, not a file edit.
- A fact or preference about this PM or their portfolio goes in the profile.
- A general working preference that would still apply if the copilot were uninstalled, or that applies when the PM is doing something unrelated to PMO work, goes in their own CLAUDE.md.
- Per-project facts are not instructions at all. They go in `project-context.md` in the project folder.

## Reviewing a PM's existing instructions at setup

Read what they already have, check it against the list below, propose what is missing, route each suggestion to the right file above, and show every proposed edit as a before-and-after. Never apply one without a yes.

Worth having, and commonly absent:

- Plain ASCII only for files written to a Windows workspace. Without it, dashes, arrows and smart quotes get double-encoded by Windows tooling and land as garbage in the file. Belongs in their CLAUDE.md, because it applies to everything they do rather than only to copilot work.
- Their writing voice, even one line of it. Most PMs have never told Claude how they write, and the default reads as AI to the client on the other end.
- Which language they work in, if it is not English.
- A tools-and-access note: what is connected, and any notebook or space IDs they use often.
- How much they want explained, and whether they would rather be asked or have work done and shown.
- Somewhere for corrections to accumulate, so the same mistake is not made twice. A lessons-learned section is the highest-value habit in the file and almost nobody has one until it is suggested.

Do not turn this into an audit. Two or three concrete suggestions is help. A review of everything they have written is an imposition on a first run, and a PM who wanted their instructions reviewed would have asked.

## What not to duplicate

A PM who copies the copilot's own rules into their CLAUDE.md ends up maintaining a stale second copy of a file that gets replaced on every update. If they ask for that, say what the baseline already covers and point them at it instead.

Same for the portfolio. If they already keep a project list in their CLAUDE.md, point the profile at it rather than writing a second one that will drift.
