---
name: gap-analysis
description: Analyze a spec artifact (Platform Specification, one Epic, or the full spec set) for completeness gaps — missing edge cases, undefined terms, logic inconsistencies, undocumented dependencies, implied features. Use after drafting or updating any spec artifact at any stage of the project.
---

# Gap Analysis Skill

Systematically analyze a spec artifact for gaps and issues that would cause problems in development or client review.

## When Triggered

User says: "run gap analysis", "check this epic for gaps", "analyze the spec", "what's missing", "review this for completeness" — or Claude determines a gap analysis is due after drafting or significantly updating a spec artifact.

## Step 1 — Identify the Target

Determine what to analyze:
- **Single Epic**: User specifies an Epic, or you just drafted one
- **Platform Specification**: User asks to check the foundation doc
- **Full spec set**: User wants a cross-epic review

Read the target file(s) before proceeding. Also read `01_Context/Platform_Specification.md` for project context regardless of target.

## Step 2 — Run the Analysis

Check for all of the following. Be specific — name the exact section, feature, or scenario that has the issue.

### Completeness Checks
- **Missing user roles**: Are all roles defined in the Platform Specification represented? Are there flows that only work for some roles but aren't labeled?
- **Missing edge cases**: Happy path is described but what happens when: the action fails, the user lacks permission, data is missing, the session times out, a third-party service is unavailable?
- **Missing error states**: Every user action that can fail needs a defined failure behavior
- **Implied features**: Does the spec assume a feature exists that isn't documented? (e.g., "users are notified" but no notification feature exists)
- **Out of Scope gaps**: Does every feature section have an explicit Out of Scope list? Are items that are clearly NOT being built actually listed there?

### Clarity Checks
- **Undefined terms**: Any domain term used that isn't in `01_Context/Glossary.md`? Flag it.
- **Vague acceptance criteria**: Any AC that says "works correctly", "user-friendly", "fast" — these are not testable. Flag each one.
- **Ambiguous business rules**: Rules with "usually", "generally", "in most cases" — these hide assumptions
- **[ASSUMPTION:] tags without resolution**: Any assumptions that were tagged but not yet confirmed with the client?

### Consistency Checks
- **Contradictions within the epic**: Does Feature A say X is allowed while Feature B says X is not allowed?
- **Contradictions with Platform Specification**: Does anything in this Epic conflict with the scope, personas, or business model defined in the Platform Specification?
- **Cross-epic conflicts** (full spec reviews only): Do any Epics define overlapping behavior differently?

### Dependency Checks
- **Undocumented dependencies**: Does any feature require another feature that isn't listed in the Dependencies section?
- **Circular dependencies**: Does Epic A depend on Epic B which depends on Epic A?
- **External dependencies not listed**: Third-party services referenced in ACs but not in the Dependencies section?

### Scope Checks
- **MVP creep**: Any feature that sounds like post-MVP scope that wasn't explicitly flagged?
- **Complexity signals**: Any single feature with 5+ edge cases or 3+ external dependencies — worth flagging for simplification review

## Step 3 — Format the Output

Group findings by severity:

**🔴 Blockers** — Must resolve before this spec is usable for development
List each with: what's missing, which section it's in, why it blocks

**🟡 Important** — Should resolve before client review
List each with: what's unclear, where it is, what to do about it

**🟢 Minor** — Nice to fix, low impact
List each with: brief description

Then end with:

**Summary**: X blockers, Y important, Z minor issues found.
**Recommended next step**: [what to do — e.g., "resolve the 2 blockers, then run workshop-prep skill before next client meeting"]

## Step 4 — Log Open Questions

For any blocker or important issue that requires client input, draft an entry for `03_Discussions/Open_Questions.md`:

```
| Q-XXX | [Question] | [Why it matters] | [Which Epic/section] | Client | P0/P1 | [Today's date] |
```

Ask the user if they want these logged now.

## Tone and Style

- Be specific, not generic. "Feature 2.3 has no error state for payment failure" is useful. "Some features are missing error states" is not.
- Don't pad the output. If something is fine, don't mention it.
- If the spec is g