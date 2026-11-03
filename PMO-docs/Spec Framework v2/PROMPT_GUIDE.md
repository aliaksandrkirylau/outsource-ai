# Prompt Guide -- How to Talk to Claude

**This is a cheat sheet for effective sessions.** How to phrase requests, which words trigger which skills, and patterns that work well.

---

## Starting a Session

Claude reads `CLAUDE.md` and `Project_Plan.md` automatically. You don't need to explain the framework every time. Just orient Claude to where you are:

> "Continue from where we left off. Check Project_Plan.md for current status."

> "New session. Let's pick up on Epic-03."

> "Starting fresh -- no prior context. Here's what we're building: [brief description]."

---

## Skill Triggers -- Exact Phrases That Work

### `initialize-project`
Use at the start of every new project.
```
"Let's initialize this project."
"I have a new client. Run initialize-project."
"Start Session 0."
```

### `epic-writer`
Use when starting a new Epic area from scratch.
```
"Write an Epic for [feature area]."
"Draft Epic-04 for [name]."
"I need a spec for [area]. Use the epic-writer skill."
```

### `gap-analysis`
Use after drafting or updating any spec file.
```
"Run a gap analysis on Epic-02."
"Check Platform_Specification.md for gaps."
"Analyze this Epic for missing edge cases and undefined terms."
```

### `acceptance-criteria`
Use when writing or reviewing user stories.
```
"Write acceptance criteria for [feature]."
"Check if these ACs are testable and binary."
"Generate Given/When/Then scenarios for [user story]."
```

### `scope-audit`
Use any time new scope is proposed.
```
"Run a scope audit on this new feature."
"Is [feature] still MVP?"
"We're about to add [X] -- check if this belongs in scope."
```

### `meeting-processor`
Use immediately after a client meeting.
```
"We just had a call. Here's the transcript: [paste]. Run meeting-processor."
"Process this email chain and tell me what changed."
"Here are my meeting notes: [paste]. What needs to update in the spec?"
```

### `workshop-prep`
Use before a client meeting.
```
"We have a client call tomorrow. Prepare me."
"Run workshop-prep for next week's session."
"What questions should I bring to the client? Use workshop-prep."
```

### `open-questions`
Use when reviewing any spec artifact for unknowns.
```
"Run open-questions on Epic-01."
"What are we still missing from the Platform Spec? Surface open questions."
"Log all unknowns from this Epic to Open_Questions.md."
```

### `client-summary`
Use when preparing a client-facing version of a spec.
```
"Write a client-friendly summary of Epic-02."
"Summarize the platform for a non-technical stakeholder."
"Create a plain-language overview of what we're building."
```

### `decision-logger`
Use when a decision has been confirmed.
```
"Log this decision: [description]."
"The client confirmed [X]. Add it to the Decision_Log."
"Run decision-logger -- we agreed that [decision]."
```

---

## Common Request Patterns

### Providing new client input
```
"The client just sent this email: [paste]. What changes?"
"New input from client. Here's the brief: [paste]. Process this and update the spec."
"Meeting notes from today: [paste]. Run meeting-processor."
```

### Reviewing existing work
```
"Review Epic-03 and tell me what's missing."
"Check Open_Questions.md -- are any P0 items still unresolved?"
"Compare Decision_Log with the current Platform Spec. Any conflicts?"
```

### Adding scope
```
"Client wants to add [feature]. Is this MVP or should it be deferred?"
"New requirement: [X]. Log it as an open question first, then we'll decide."
```

### Getting unstuck
```
"I'm not sure what to work on next. Check Project_Plan.md."
"What's the status of the spec? Summarize where we are."
"What P0 questions are blocking Epic work?"
```

### Preparing for client review
```
"We're presenting to the client Thursday. What do I need to prepare?"
"Create a summary of what's confirmed vs. still assumed."
"Which items need client sign-off before we can proceed?"
```

---

## Tips for Better Results

**Give Claude the raw material, not the interpretation.**
Paste the transcript or email directly. Let Claude extract the insights.
> [x] "Here's the transcript: [paste full text]"
> [no] "The client said they want a dashboard"

**Name the skill explicitly when you want it.**
Claude will often trigger the right skill automatically, but explicit invocations are more reliable for complex tasks.
> [x] "Run the gap-analysis skill on Epic-02"
> [no] "Check if Epic-02 is complete"

**Use [ASSUMPTION: ...] tagging actively.**
When you tell Claude something is assumed rather than confirmed:
> "Assume the platform is B2B for now -- we haven't confirmed this with the client."
Claude will tag it accordingly so it doesn't get treated as fact.

**Batch questions for client meetings.**
Don't send one-off emails for every unknown. Log them in Open_Questions.md and batch them for the next call.
> "Surface all P0 and P1 questions from Open_Questions.md. I'm preparing for a client call."

**Flag contradictions explicitly.**
If the client said something that conflicts with what's in the spec:
> "The client said [X] but the spec says [Y]. Log this as a contradiction and tell me how to resolve it."

---

## When Something Goes Wrong

See `00_Meta/Troubleshooting.md` for:
- Claude ignoring the 8-step loop
- Skills not triggering
- Spec drift and scope creep
- Session context issues
