# Workflow: Validation & Quality Assurance

> **"Find problems in specs, not in code."**
> Fixing a contradiction in requirements takes 10 minutes. Fixing it in development takes 10 hours.

---

## When to Validate

- After drafting any Epic or Feature section
- After processing new client input
- Before any client review or milestone
- When something "feels off" -- trust the instinct, run gap-analysis

---

## Primary Tool: gap-analysis Skill

The `gap-analysis` skill is your main validation tool. Run it on:
- Individual Epics (most common)
- The Platform Specification (after Session 0 and after scope changes)
- The full spec set (before client review or development handoff)

**How to trigger:**
> "Run gap-analysis on Epic-03."
> "Run gap-analysis on the Platform Specification."
> "Run a full spec gap-analysis across all Epics."

Gap-analysis checks:
- Completeness (missing sections, undefined terms, empty Out of Scope)
- Logic (contradictions, missing edge cases, undefined states)
- Consistency (terminology drift between Epics, rules not applied)
- Dependencies (things required but not specced elsewhere)
- Scope (things implied but not explicitly included)

Output uses ?/?/? groupings. Address ? immediately before proceeding.

---

## Manual Validation Checks

Some checks are best done manually or via direct prompt:

### Logic Gap Analysis
```
Analyze [Epic-XX / Feature section name] for:
1. What happens if the user has insufficient permissions?
2. What happens if a required dependency doesn't exist yet?
3. What happens if the user repeats an action they've already done?
4. What are the boundary conditions (0 items, max items, etc.)?
5. What happens on network failure or system error?
List any gaps.
```

### Consistency Check Across Epics
```
Compare all Epics in 02_Epics/.
Check for:
- Same concept, different terms (e.g., "User" vs "Player" vs "Member")
- Contradicting business rules across Epics
- Assumptions in one Epic that conflict with confirmed decisions in Decision_Log.md
Report inconsistencies.
```

### Simplification Sweep
```
Review Epic-XX.
For each feature section, ask:
1. Can we achieve 80% of the value with 50% of the complexity?
2. Is this truly MVP or a nice-to-have?
3. Can this start as a manual process before being automated?
4. Can we defer this to Post-MVP without blocking the core value?
Recommend what to cut or defer. Don't modify the file -- list recommendations only.
```

---

## Validation Gates

### Before Epic Work Begins
- [ ] Platform_Specification.md has no P0 open questions
- [ ] MVP scope (In Scope and Out of Scope) is explicitly listed
- [ ] All major user roles are defined
- [ ] Client has confirmed the Platform Specification

### Before Client Review (per Epic)
- [ ] Every feature section has a User Story, Description, User Flow, ACs, Edge Cases, Business Rules
- [ ] Every feature section has an Out of Scope list (minimum 3 items)
- [ ] No TBD or TODO anywhere in the file
- [ ] All [ASSUMPTION: ...] tags flagged for client confirmation
- [ ] gap-analysis run with no ? findings

### Before Development Handoff (full spec)
- [ ] All P0 open questions resolved
- [ ] All major [ASSUMPTION: ...] tags either confirmed or escalated to open questions
- [ ] Platform Specification reflects confirmed scope
- [ ] Decision Log has all key decisions captured with rationale
- [ ] Client has confirmed the spec in writing or documented in Decision_Log.md

---

## Validation Types in Detail

### 1. Completeness Check

**Purpose:** Every feature section has what developers need.

Minimum required per feature:
- User Story (As a / I want / So that)
- Description
- User Flow (numbered steps)
- Acceptance Criteria (at least 1 happy path + 1 edge case + 1 error state in Given/When/Then)
- Edge Cases table
- Business Rules
- Data & State
- Out of Scope section

Run: `acceptance-criteria` skill if ACs are thin.
Run: `open-questions` skill to surface gaps systematically.

---

### 2. Scope Discipline Check

**Purpose:** Every feature section is actually MVP.

Run `scope-audit` when:
- Adding any new feature or capability
- Changing the Platform Specification scope
- Any "while we're at it" moment
- An Epic is growing beyond 5-6 feature sections

The question is always: **Is this still MVP, or have we drifted?**

Items that don't pass scope-audit go to the Out of Scope section of the relevant Epic, not a separate file.

---

### 3. Terminology Consistency

**Purpose:** Same concept = same term everywhere.

Check: `01_Context/Glossary.md` is up to date.

Run:
```
Extract all capitalized nouns, role names, and domain-specific terms from 02_Epics/.
Cross-reference against 01_Context/Glossary.md.
Report any terms used in specs but not defined in the Glossary.
```

---

### 4. Decision Consistency

**Purpose:** Specs reflect confirmed decisions, not outdated assumptions.

Run:
```
Compare all [ASSUMPTION: ...] tags in 02_Epics/ and 01_Context/Platform_Specification.md
against confirmed decisions in 03_Discussions/Decision_Log.md.
Which assumptions have been resolved but not yet updated in the spec?
Which assumptions contradict a logged decision?
```

---

## Client Sign-Off Process

### 1. Prepare the review package
- Use `client-summary` skill to generate plain-language Epic summaries
- Identify which [ASSUMPTION: ...] tags need client confirmation
- Prepare open question list from `03_Discussions/Open_Questions.md` (P0 and P1 only)

### 2. Walk through in a meeting
- Use `workshop-prep` skill to prepare the meeting agenda
- Focus on: does this match their vision? Are MVP priorities right?

### 3. Process the meeting output
- Run `meeting-processor` on the transcript or notes
- Log confirmed decisions with `decision-logger`
- Update specs based on confirmed information

### 4. Log the confirmation
Sign-off can be formal (written approval) or lightweight (confirmed in meeting, logged in Decision_Log.md).

---

## When Validation Fails

**Critical issues (?):** Stop. Fix before proceeding. A broken foundation makes every Epic built on top of it wrong.

**Medium issues (?):** Log as open questions with P1 priority. Schedule resolution before next milestone.

**Scope creep found:** Run `scope-audit`. Document what was found and the decision to defer or include.

**Client misalignment found:** Return to Platform Specification. The foundation was wrong -- fix it before conti