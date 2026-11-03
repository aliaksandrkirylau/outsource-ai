---
name: workshop-prep
description: Prepare for an upcoming client meeting or workshop. Given the current spec state and open questions, produces what needs confirming, a prioritized question list, and a suggested meeting agenda. Use before any client meeting.
---

# Workshop Prep Skill

Prepare for a client meeting so you walk in knowing exactly what you need to get out of it.

## When Triggered

User says: "prepare for the meeting", "help me prep for the workshop", "I have a call with the client", "what should I ask tomorrow", "meeting prep" — or before a scheduled client review or discovery session.

## Step 1 — Read the Current State

Before preparing anything, read:
1. `03_Discussions/Open_Questions.md` — all open questions, especially P0 and P1
2. `01_Context/Platform_Specification.md` — current foundation doc state
3. `03_Discussions/Decision_Log.md` — what's already been decided (don't re-ask these)
4. Any recently updated Epics in `02_Epics/` if the meeting is about reviewing spec work

Ask the user: "What is the goal of this meeting?" if not already clear. Options:
- Discovery/kickoff — understanding the project for the first time
- Foundation review — confirming the Platform Specification before Epic work
- Epic review — walking through completed specs with the client
- Issue resolution — resolving specific open questions or blockers
- Progress update — general sync

## Step 2 — Identify What Needs Confirming

From the open questions and current spec state, extract:

**Must confirm (P0)** — blockers that prevent further spec work. These MUST be answered in this meeting.

**Should confirm (P1)** — important decisions that affect design and scope. Prioritize these.

**Assumptions to validate** — any `[ASSUMPTION: ...]` tags in specs that the client hasn't confirmed yet. Group by Epic.

**Scope items to lock** — anything in the MVP In/Out lists that hasn't been explicitly confirmed. Especially items that seem borderline.

## Step 3 — Produce the Outputs

### Output 1: Pre-Meeting Status Brief

A one-paragraph summary of where the project stands — what's been done, what's confirmed, what's open. This is useful to send to the client before the meeting as context.

### Output 2: Prioritized Question List

Group questions by topic (not by priority level — topic grouping works better in a meeting):

```markdown
## Questions for [Meeting Date]

### [Topic Area 1 — e.g., "Payments & Pricing"]
1. **[P0]** [Question — specific, one thing at a time]
   *Context: [1 sentence on why this matters / what depends on it]*

2. **[P1]** [Question]
   *Context: [Why this matters]*

### [Topic Area 2 — e.g., "User Roles & Permissions"]
...
```

**Rules for good questions:**
- One question per item — don't bundle two questions into one
- Provide context so the client understands why you're asking
- Offer options where the answer is likely one of a few choices: "Option A: [X] / Option B: [Y]"
- Don't re-ask questions already answered in Decision_Log.md

### Output 3: Suggested Meeting Agenda

A time-boxed agenda based on the goal of the meeting and the questions list.

```markdown
## Meeting Agenda — [Date]

**Goal**: [One sentence on what a successful meeting achieves]
**Duration**: [Suggested time based on number of topics]

1. [5 min] — Quick context: where we are, what we're deciding today
2. [X min] — [Topic 1]: [Questions to cover]
3. [X min] — [Topic 2]: [Questions to cover]
4. [X min] — [Topic 3 if applicable]
5. [5 min] — Confirm decisions, next steps, action items

**Must-have outcomes** (meeting fails if we don't get these):
- [P0 question answered]
- [P0 question answered]

**Nice-to-have outcomes**:
- [P1 items if time allows]
```

### Output 4: Spec Areas to Walk Through (if Epic review)

If the meeting involves reviewing spec work, list:
- Which Epics or sections to walk through
- Key decisions or assumptions in each that need client sign-off
- Any areas where the spec made a judgment call that the client should be aware of

## Step 4 — After the Meeting

Remind the user: once the meeting is done, use the `meeting-processor` skill to process the transcript or notes and produce decisions, follow-up email, and spec impact plan.

## Tips

- Don't send a 20-question list to the client — it's overwhelming. Send the top 5-7 most important ones in advance if you share questions ahead of time.
- Group questions by topic in the meeting — it makes conversations more natural 