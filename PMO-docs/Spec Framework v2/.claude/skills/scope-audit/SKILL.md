---
name: scope-audit
description: Immediately run when ANY new feature, change, or addition is proposed — before it gets added to a spec. Ask "is this actually MVP?" at the moment of proposal, not after. Triggers on: "we could also add...", "the client wants...", "while we're at it...", "can we include...", adding anything to an Epic that wasn't in the confirmed Platform Specification, any scope that wasn't in the original brief. Do not wait to be asked — fire proactively.
---

# Scope Audit Skill

Ask the hard question: does this belong in MVP, or are we building a full product when we committed to a first version?

## When Triggered

- User adds a new feature or capability to an existing Epic
- User proposes a change to the MVP scope in Platform Specification
- User says "while we're at it we could also...", "it would be nice to add...", "the client asked for..."
- Before a client review session
- Any time scope feels like it's growing

## Core Question

**Would the product fail to deliver its primary value without this feature?**

If yes → it belongs in MVP.
If no → it's a candidate for Post-MVP. That doesn't mean it's bad. It means it's not now.

## Step 1 — Understand What's Being Added

Read the relevant Epic file and the Platform Specification (`01_Context/Platform_Specification.md`). Identify:
- What exactly is being proposed (be specific)
- What Epic it belongs to
- Whether it's a new feature, an extension of an existing feature, or a change to an existing one

## Step 2 — Run the MVP Test

Ask these questions about the proposed addition. Be direct — a yes/no answer for each:

**Value test**
- Does the product fail to deliver its core promise without this feature?
- Would the primary user (as defined in Platform Specification) be blocked from completing their main task without it?

**Complexity test**
- Does adding this require new integrations, new user roles, or significant new data requirements?
- Does it introduce edge cases that require substantial additional spec work?
- Does it add dependencies to other Epics that weren't there before?

**Scope signal test**
- Was this feature discussed and confirmed with the client, or is it an assumption?
- Was this in the original brief, or did it emerge during spec work?
- Is this the 2nd or 3rd extension to a feature that already has a clear MVP version?

## Step 3 — Make a Recommendation

Based on the test, produce one of three recommendations:

**✅ Include in MVP**
The feature is core to the product's value. Briefly state why: which primary user flow depends on it, or what would fail without it.

**⚠ï¸ Simplify for MVP**
The feature is needed but the proposed version is too complex. Describe a simplified version that delivers the core value with less scope. "Build the simple version now, add [extensions] in v1.1."

**❌ Defer to Post-MVP**
The product works without this. The feature adds complexity without being essential to the first version's value proposition. List it as an ❌ item in the relevant Epic's Out of Scope section.

## Step 4 — If Deferring, Document It

If the recommendation is to defer:
1. Add it to the relevant Epic's **Out of Scope** section with reason: `❌ [Feature] — Deferred: not required for MVP value delivery`
2. Optionally note it in `00_Meta/Project_Plan.md` under a "Post-MVP backlog" note so it's not lost

Do NOT create separate files, separate folders, or feature files for deferred items. The Out of Scope section is the record.

## Step 5 — If It's a Client Request

If the new scope came from a client conversation or meeting:

1. Do not add it to specs immediately, even if it sounds reasonable
2. Log it as an Open Question in `03_Discussions/Open_Questions.md`:
   ```
   | Q-XXX | Should [feature] be included in MVP? | Client requested during [meeting/date]. Not in original scope. | Platform Spec / Epic-XX | Client | P1 | [date] |
   ```
3. Flag that it needs a formal scope decision before spec work begins on it

## Tone

Be direct. Scope discipline is a service to the project, not a blocker. The goal is to ship something, get feedback, and build the right thing — not to build everything at once.

If