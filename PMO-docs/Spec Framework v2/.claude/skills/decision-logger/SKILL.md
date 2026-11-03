---
name: decision-logger
description: Format and log a decision into Decision_Log.md. Use when a client confirms something, a team makes an architectural choice, or scope is formally changed. Keeps the decision log consistent and ensures rationale is captured.
---

# Decision Logger Skill

Capture decisions properly so they're traceable and don't get lost or re-litigated.

## When Triggered

User says: "log this decision", "add this to the decision log", "we decided X", "the client confirmed Y" — or after a meeting where decisions were made and the meeting-processor skill has already produced the list of decisions to log.

## Why This Matters

A decision without rationale is nearly useless. Six weeks later, when someone asks "why did we do it this way?", you need to know:
- What options were considered
- Why the chosen option was picked
- Who was involved
- What it affects

Without that, you end up re-opening decisions already made.

## Step 1 — Gather the Information

For each decision to log, collect:

1. **What was decided** — one clear sentence
2. **Why it came up** — what triggered this decision
3. **Options that were considered** — at minimum 2 (even if one was obvious)
4. **What was chosen** — the selected option
5. **Why it was chosen** — the rationale
6. **Who was involved** — client, team, or both
7. **What it affects** — which Epics, features, or the Platform Specification

If any of these are missing, ask the user before logging. A decision entry without rationale is worth almost nothing.

## Step 2 — Assign an ID

Check `03_Discussions/Decision_Log.md` for the last entry number per category:

- **D-T###** — Technical/Architecture decision
- **D-B###** — Business/Monetization decision
- **D-UX###** — User Experience decision
- **D-S###** — Scope decision (feature in/out, MVP boundaries)
- **D-C###** — Compliance/Legal decision

Pick the next available number in the right category.

## Step 3 — Format the Entry

```markdown
| [D-X###] | [Today's date] | [1-line decision summary] | [Why this came up] | [Option A / Option B / Option C] | [Chosen option] | [Why chosen] | [Client / Team / Both] | [Impact level] - [Affected areas] | Active |
```

**Impact levels**: High (multiple epics or architecture), Medium (single epic significantly), Low (single feature or UI detail)

**Example:**
```markdown
| D-S003 | 2026-03-30 | Camps deferred to Post-MVP | Client asked about camp registration; scope would add 40%+ complexity | A: Include in MVP / B: Defer to Post-MVP | B: Defer | Complexity too high for first version; core platform value works without it | Client + Team | High - Epic-03 Out of Scope | Active |
```

## Step 4 — Check for Contradictions

Before logging, scan the existing Active Decisions in `Decision_Log.md`. Does this new decision contradict anything already logged?

If yes, flag it:
> "This new decision conflicts with D-XXX ([summary]). Do you want to supersede that decision? If so, I'll mark D-XXX as Superseded and create a new entry."

If superseding: mark the old entry status as "Superseded by D-XXX" and log the new entry normally.

## Step 5 — Update Affected Specs

After logging, identify what needs updating in the specs:

- Does the Platform Specification MVP scope need updating?
- Does any Epic's In Scope / Out of Scope section need updating?
- Are any `[ASSUMPTION: ...]` tags now resolved?

List the updates needed and ask: "Want me to apply these changes to the spec files now?"

## Step 6 — Log It

Append the formatted entry to the correct category table in `03_Discussions/Decision_