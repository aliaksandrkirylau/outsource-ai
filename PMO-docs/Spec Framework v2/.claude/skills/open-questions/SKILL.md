---
name: open-questions
description: Systematically surface open questions and unknowns from any spec artifact — Platform Specification, a single Epic, or a set of Epics. Formats findings for Open_Questions.md with correct priority levels. Use when reviewing a draft spec artifact.
---

# Open Questions Skill

Surface unknowns before they become surprises in development or client reviews.

## When Triggered

User says: "what questions do we still have", "find open questions in this epic", "what do we need to confirm with the client", "surface the unknowns" — or after drafting/reviewing a spec artifact.

## Step 1 — Read the Target

Read the specified Epic(s) or Platform Specification. Also read existing `03_Discussions/Open_Questions.md` to avoid duplicating questions already logged.

## Step 2 — Surface Unknowns

Look for these categories of unknowns:

**Business Logic Unknowns**
- Business rules that are implied but not confirmed ("users can cancel up to X hours before" — what is X?)
- Conditional behavior where the condition isn't defined ("premium users get extra features" — what features?)
- Missing pricing, limits, or thresholds ("tokens expire after..." — after how long?)

**Scope Unknowns**
- Features referenced but not specced ("users will be notified" — how? email, SMS, in-app?)
- Integrations mentioned but not confirmed ("connects to their existing system" — which system?)
- User permissions that are inconsistent or unclear across features

**Client Decision Unknowns**
- Anything marked `[ASSUMPTION: ...]` that hasn't been confirmed
- Anything that represents a business decision only the client can make
- Edge cases where the desired behavior isn't obvious and has real product implications

**Technical Feasibility Unknowns**
- Integrations where feasibility hasn't been confirmed (worth flagging for a quick dev check)
- Performance expectations that may need validation ("real-time updates" — what latency is acceptable?)

## Step 3 — Assign Priorities

For each question, assign:

- **P0** — Blocker. Cannot write or finalize a spec section without this answer. Development cannot start on this area until resolved.
- **P1** — Important. Significantly affects design or scope. Should be resolved before client sign-off.
- **P2** — Clarification. Low impact. Good to know, can proceed with a documented assumption.

**Default to P1 if unsure.** It's better to surface a P1 that turns out to be minor than to miss a real blocker.

## Step 4 — Format for Open_Questions.md

Format each question as a table row ready to paste:

```markdown
| Q-XXX | [Clear, specific question] | [Why this matters — what it blocks or affects] | [Epic-XX / Platform Spec section] | Client | P0/P1/P2 | [Today's date] |
```

**Write good questions:**
- Specific: "Can trainers edit attendance after the session ends? If yes, how long after?" ✅
- Provides context: "The payment flow assumes USD only. Do trainers need to accept other currencies?" ✅
- Offers options where helpful: "Should cancelled bookings be soft-deleted (recoverable) or permanently removed?" ✅

**Not this:**
- Vague: "How should payments work?" ❌
- Assumed: "We're using email for notifications, correct?" ❌

## Step 5 — Deliver the Output

Group questions by:
1. P0 — Blockers (list first)
2. P1 — Important
3. P2 — Clarifications

Then ask the user: "Want me to log these to `03_Discussions/Open_Questions.md` now?"

If yes, append each question to the appropriate priority section in the file.

## After Logging

Remind the user: P0 questions should be resolved before continuing spec work in the