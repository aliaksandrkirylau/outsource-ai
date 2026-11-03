# What Codex needs for the same sync (docs only - nothing installed or tested here)

Sources: research/alternatives-and-hosts.md (OpenAI docs as of 2026-09-25).

1. Instructions: nothing extra. Codex reads `AGENTS.md` natively, from the git root down to the
   working folder, closer files winning; the same `AGENTS.md` Claude imports through CLAUDE.md.
2. The sandbox is the difference. In the default workspace-write mode `.git` is read-only and
   network is off, so `bash tools/kb-sync.sh` (which commits, fetches and pushes) needs the
   person's approval to run outside the sandbox every time. [DOC + INFERENCE]
3. To make that one command routine and everything else impossible, a project rules file
   (experimental, loaded only when the person marks the project as trusted):

   `.codex/rules/kb.rules`
   ```
   prefix_rule(pattern=["bash", "tools/kb-sync.sh"], decision="allow")
   prefix_rule(pattern=["git", "push"], decision="forbidden")
   prefix_rule(pattern=["git", "commit"], decision="forbidden")
   prefix_rule(pattern=["git", "reset"], decision="forbidden")
   prefix_rule(pattern=["git", "rebase"], decision="forbidden")
   ```
   Check it with `codex execpolicy check` before relying on it. Same caveat as Claude's deny
   rules: prefix matching, so `git -C . push` is a different prefix. The server-side guard
   (no force push, no branch deletion) is the backstop for both agents.
4. Skills are optional. If wanted, Codex looks in `.agents/skills/<name>/SKILL.md`, Claude in
   `.claude/skills/<name>/SKILL.md`; the same file can be committed in both places. For sync the
   procedure is five lines in `AGENTS.md`, so no skill is needed on day one.
5. First person with a Codex seat: run it once in the repo, say "sync", and check which
   approvals it asks for. That is the missing test.
