---
name: meeting-processor
description: Process a client meeting transcript or email chain after the fact. Produces a meeting summary, follow-up email draft, decisions to log, and a spec impact plan — what needs updating in the Platform Specification and which Epics are affected. Use immediately after any client meeting or when given an email chain to process.
---

# Meeting Processor Skill

Turn a raw meeting transcript or email chain into structured outputs: summary, follow-up email, decisions logged, and a clear plan for what specs need updating.

## When Triggered

User says: "process this meeting", "here's the transcript", "review this email chain", "what came out of this meeting", "help me write the follow-up" — or pastes a transcript/email thread directly.

## Step 0 — Get the Transcript

**If the user provided a transcript or email chain:** proceed to Step 1.

**If the user mentioned a meeting but didn't paste a transcript**, say:

> "I'll create a transcript file for you to paste into. Give me a moment."

Then create `03_Discussions/Meetings/[YYYY-MM-DD]_[Brief-Description]_RAW.md` with this starter content:

```
# Raw Transcript — [Meeting Title]
Date: [YYYY-MM-DD]
Participants: [to fill in]

---

[Paste raw transcript or notes here]
```

Then say:
> "[filename]_RAW.md is ready in 03_Discussions/Meetings/. Paste the transcript there and let me know — I'll process it right away."

Do not proceed to Step 1 until there is actual transcript content to work with.

## Step 1 — Read the Context

Before processing, read:
- `01_Context/Platform_Specification.md` — to understand current scope and detect changes
- `03_Discussions/Open_Questions.md` — to check if any open questions were resolved
- `03_Discussions/Decision_Log.md` — to avoid duplicate decision entries

Then read the input (transcript or email chain) fully before producing any output.

## Step 2 — Extract the Key Information

From the meeting/email, identify:

**Decisions made** — things that were agreed, confirmed, or chosen
- Business logic confirmed ("the cancellation window is 2 hours")
- Scope decisions ("camps are out of MVP")
- Technical decisions ("they use Stripe for payments")
- Process decisions ("client will send designs by Friday")

**Open questions resolved** — any questions from Open_Questions.md that were answered

**New information** — facts, context, or constraints shared that weren't known before

**New scope requests** — features or changes the client mentioned that aren't in current specs. Flag these separately — they are NOT automatically added to specs.

**Action items** — things someone committed to doing, with who and when

**Concerns or risks** — anything the client expressed concern about, or gaps you noticed during the meeting

## Step 3 — Produce the Outputs

### Output 1: Meeting Summary

```markdown
## Meeting Summary — [Date]
**Attendees**: [List]
**Purpose**: [1 sentence]

### Key Decisions
1. [Decision — state it clearly and concisely]
2. [Decision]

### Questions Resolved
- Q-XXX: [Question] → Answer: [Answer]

### New Information
- [Fact or constraint learned]

### Scope Requests (NOT yet in specs — needs review)
- [Item]: [What client requested, as they described it]

### Action Items
| Action | Owner | Due |
|:---|:---|:---|
| [Action] | [Who] | [When] |

### Open Items / Risks
- [Concern or risk noted]
```

### Output 2: Follow-Up Email Draft

A professional email to the client summarizing what was agreed and what's happening next.

Structure:
- Opening: thank them, reference the meeting
- What was confirmed (decisions, scope, etc.)
- Any clarifications or follow-ups still needed from them
- What you're doing next (what they can expect)
- Closing

Tone: professional, concise. Don't over-explain — the client was in the meeting.

### Output 3: Spec Impact Plan

What needs to change in the specs as a result of this meeting. Be specific.

```markdown
## Spec Impact Plan

### Platform Specification
- [ ] [What to update, which section] — [Why: decision/information that drives the change]

### Epics to Update
- [ ] Epic-XX [Name]: [What changes and why]
- [ ] Epic-XX [Name]: [What changes and why]

### New Epics Implied
- [If any]: [Area] — [Why a new Epic may be needed based on what was discussed]

### Decisions to Log (Decision_Log.md)
- D-XXX: [Decision summary] — [Context, options, rationale, stakeholders, impact]

### Open Questions to Close
- Q-XXX: Mark as resolved with answer: [answer]

### New Open Questions Surfaced
- [Question] — Priority: P0/P1/P2 — [Why it matters]

### Scope Requests Requiring Decision
- [Item]: Log as Open Question before adding to any spec. Suggested: P1.
```


## Step 4 -- Save the Files

Before asking the user to review, save both files to `03_Discussions/Meetings/`:

1. **`[YYYY-MM-DD]_[Brief-Description]_RAW.md`** -- the raw transcript as provided (skip if already saved from Step 0)
2. **`[YYYY-MM-DD]_[Brief-Description].md`** -- the processed output (all three outputs from Step 3)

Use the meeting date for the filename. If date isn't in the input, use today's date and note it as approximate.

## Step 5 -- Ask Before Acting

Deliver all three outputs, then ask:

"Ready to apply these changes? I can:
1. Update the Platform Specification with the confirmed decisions
2. Log the decisions i