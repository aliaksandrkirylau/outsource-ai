# FINDINGS — found and deliberately not fixed

Append-only. Add entries at the bottom with a CLI append; never rewrite or
delete earlier entries. The only allowed edit to an existing entry is its
`Resolved` field. Never read this file whole — grep it (by ticket key, by
symptom). Keep the labels below **character-exact and not bold**: commands
grep for them.

Entry template:

```markdown
## [<CURRENT-KEY>] <short title>
- Found while working on: <CURRENT-KEY> — <ticket summary>
- Where: <component>/<path> — <function/line if useful>
- What: <2–4 factual sentences. No speculation about why.>
- Likely owner ticket: <KEY> | none — see Owner | unclear
- Owner: <role from PROJECT-PROFILE §10> — <name if known>
- Tracked in: BACKLOG.md #<N>   <!-- only when ours and no ticket covers it -->
- Priority: high | medium | low
- Downstream impact: <which tickets this blocks or reshapes — omit if none>
- Blocking?: no (left untouched) | yes (fixed inline — see the ticket report)
- Resolved: no
- Date: <YYYY-MM-DD>
```

---
