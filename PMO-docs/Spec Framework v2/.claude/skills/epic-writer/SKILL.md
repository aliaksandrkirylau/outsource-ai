---
name: epic-writer
description: Draft a complete Epic from raw client input, brief notes, or a description of an area. Structures it following the Epic Template with features as sections, including full Given/When/Then acceptance criteria. Use when starting a new Epic from scratch or when told to "write an epic", "draft Epic-XX", or "create the spec for [area]".
---

# Epic Writer Skill

Turn raw input into a structured, template-compliant Epic draft ready for review and refinement — including full acceptance criteria for every feature.

## When Triggered

User says: "write an epic for...", "draft Epic-XX", "create the spec for [area]", "start the [feature area] epic" — or when the 8-step loop reaches the Execute step for a new Epic.

## Before Starting

Read these files first:
1. `01_Context/Platform_Specification.md` — essential context: personas, business model, MVP scope, epic map
2. `00_Meta/Templates/Epic_Template.md` — the structure to follow
3. Any relevant raw inputs in `01_Context/RawInputs/` if mentioned
4. Existing Epics in `02_Epics/` to check for: scope overlaps, dependencies, numbering

If P0 open questions exist in `03_Discussions/Open_Questions.md` that affect this epic, flag them before proceeding — don't draft around P0 blockers.

## Step 1 — Assess Input Quality Before Drafting

Before writing anything, assess whether you have enough to draft well. Check:

- Is it clear what user problem this epic solves?
- Do you know which user roles are primarily involved?
- Is there a rough sense of what's in and out of scope?
- Are there relevant confirmed decisions in `03_Discussions/Decision_Log.md`?

**If input is thin, ask — don't invent.** Use a targeted clarification loop (max 2-3 questions per round, starting with the highest-impact gap):

Round 1 example:
> "Before I draft this Epic, I need a few things:
> 1. What's the core action this user needs to accomplish? (e.g., 'trainers create and publish training sessions')
> 2. Which user roles does this primarily involve — and are there secondary roles who see or interact with the output?
> 3. Is there anything you already know should NOT be in this epic?"

Wait for answers, then assess again. If you still have critical gaps after one round, ask one more targeted round. After two rounds, proceed with `[ASSUMPTION: ...]` tags for anything still unclear — don't keep the user in a clarification loop indefinitely.

**Ready to draft when you can answer:**
- What problem does this epic solve and for whom?
- What are the 3-5 main capabilities it includes?
- What is explicitly out of scope?

## Step 2 — Draft the Epic

Follow the Epic Template structure exactly. File name: `Epic-[NN]_[Name]_SPEC.md`

### Epic Overview Section
Write:
- **Description**: 2-3 paragraphs explaining what this Epic covers and its business value. Use plain language. Focus on the user need being served.
- **In Scope (MVP)**: Bullet checklist of capabilities included. Be specific — not "manage events" but "create, edit, cancel, and view training sessions"
- **Out of Scope**: ❌ list of explicitly excluded items with brief reason. At minimum 3-5 items. Think: what would someone naturally assume is in here but isn't?
- **Dependencies**: What must exist before this Epic can be built. What does this Epic block.
- **User Roles**: Table of roles, their primary actions in this epic, and their access level.

### Feature Sections
For each significant feature within the Epic, write a section:

```markdown
---
## Feature: [Feature Name]
```

Each feature section includes:
1. **User Story** — As a [role], I want [action], so that [benefit]. One sentence. Specific.
2. **Description** — 1-2 paragraphs. What it does, why it exists, key behavior.
3. **User Flow** — Numbered step-by-step happy path. Keep it to the key steps.
4. **Acceptance Criteria** — Given/When/Then scenarios (see AC rules below). Minimum: happy path + 1 edge case + 1 error state.
5. **Edge Cases** — Table: scenario | expected behavior
6. **Business Rules** — Numbered list of constraints and policies for this feature
7. **Data & State** — What data is involved (not how it's stored). State table if applicable.
8. **Out of Scope** — ❌ items specific to this feature
9. **Open Questions** — Any unknowns specific to this feature (P0/P1/P2)
10. **Decisions Made** — Key decisions already confirmed for this feature

### Acceptance Criteria Rules

Every AC must be **binary**: it either passes or fails. No grey area. Ask: could a developer write an automated test for this without asking any questions? If no, it needs to be more specific.

**Required scenarios per feature:**

**1. Happy Path (required)**
```
Given [user is in a specific state and context]
When [user performs the action]
Then [observable outcome 1]
And [observable outcome 2]
```

**2. Permission/Access (if roles are relevant)**
```
Given [user does NOT have the required role/permission]
When [user attempts the action]
Then [access is denied with a clear message]
```

**3. Edge Cases (at least 2)**
```
Given [edge condition — empty list, max length, deadline just passed]
When [user performs the action]
Then [specific defined behavior]
```

**4. Error/Failure States**
```
Given [user is in a valid state]
When [action fails — network error, service unavailable, concurrent edit]
Then [system handles gracefully — specific message, no data loss, retry option]
```

**AC format:**
```markdown
**Scenario 1: Successful [action]**
- **Given** [context]
- **When** [action]
- **Then** [outcome]
- **And** [outcome]

**Scenario 2: [Edge case]**
- **Given** [context]
- **When** [action]
- **Then** [outcome]
```

**What NOT to write in ACs:**
- ❌ "The system should load quickly" — not measurable
- ❌ "Users should find it easy to navigate" — not testable
- ❌ "The feature works correctly" — circular
- ❌ "Use Stripe API to process payment" — implementation detail
- ❌ "80% of users complete this in under 2 minutes" — vanity metric

If you had to assume something to write a criterion (session timeout, error message text), tag it: `[ASSUMPTION: session timeout is 30 minutes — confirm with client]`

## Step 3 — Apply Quality Standards

Before delivering the draft, check:

- [ ] No API schemas, database schemas, or specific technical architecture
- [ ] No story point estimates or time estimates
- [ ] No vanity success metrics ("X% of users should...")
- [ ] Every feature has an Out of Scope section
- [ ] Every assumption is tagged `[ASSUMPTION: ...]`
- [ ] ACs are binary and testable (no "should work correctly")
- [ ] ACs cover: happy path + at least one edge case + at least one error state
- [ ] Business language throughout — describe what users need, not how to build it

## Step 4 — Deliver and Flag

Deliver the draft Epic, then:

1. **List assumptions**: Everything tagged `[ASSUMPTION: ...]` that needs client confirmation
2. **List open questions**: Any unknowns surfaced during drafting → offer to log in `03_Discussions/Open_Questions.md`
3. **Note what's thin**: Any sections that need more client input before they're solid

End with: "This draft is ready for review. Once you've reviewed it, I'd recommend running `gap-analysis` to catch anything I missed."

## What to Avoid

- **Don't invent business rules** that weren't in the input. If a rule is needed but unknown, tag it as an assumption or log as an open question.
- **Don't over-specify features** that are simple. Not every feature needs all sections at equal depth.
- **Don't mirror the client's exact language** if it's ambiguous — translate into clear spec language, but flag any interpretation you made.
- **Don't skip ACs** because the feature "seems simple". Simple features still need at least a happy path scenario.
