---
name: initialize-project
description: Initialize a new project using the framework. Takes raw client brief or context, assesses what is known vs unknown, guides the PM through setting up the foundation before Epic work begins. Use at the start of every new project — pairs with Workflow_ProjectInitialization.md.
---

# Initialize Project Skill

Guide a PM through Session 0: from raw client inputs to a confirmed Platform Specification ready for Epic work.

## When Triggered

User says: "start a new project", "initialize the project", "let's set up the project", "I have a new client" — or at the start of a fresh framework session with no Platform Specification filled in yet.

## Step 1 — Check Skills Availability

Before anything else, verify the framework skills are available in this session. Check whether the following skills are listed as available:

- gap-analysis
- epic-writer
- scope-audit
- open-questions
- meeting-processor
- workshop-prep

If any are missing, inform the user:

> "Some framework skills are not yet active in this session. To get the full workflow, you'll need to add them via the Cowork UI:
> 1. Go to Settings → Skills (or the Skills panel in Cowork)
> 2. Upload the SKILL.md file for each missing skill from `.claude/skills/[skill-name]/SKILL.md`
>
> Missing: [list them]
>
> You can continue without them, but [skill-name] and [skill-name] will be needed for [specific workflow steps]."

Proceed regardless — don't block the user just because skills are missing.

## Step 2 — Assess What Exists and Initialize Project Plan

Check what's already in the project:
- Is `01_Context/Client_Brief.md` filled in with real content, or still a template?
- Is `01_Context/Platform_Specification.md` filled in, or still a template?
- Are there any files in `01_Context/RawInputs/`?
- Does `03_Discussions/Open_Questions.md` have any real questions logged?
- Is `00_Meta/Project_Plan.md` initialized for this project?

**Initialize Project_Plan.md now** (don't wait until Step 6):
- Set the project name and client if known (use `[TBD]` if not)
- Set Phase 1 (Foundation / Session 0) as In Progress
- Log this session in Session History

If there's no client input at all, ask the user to share the client brief or context before proceeding. You need at minimum: what the client wants to build, who it's for, and any constraints mentioned.

## Step 3 — Rapid Assessment

Once you have some input (from Client_Brief.md, RawInputs, or directly from the user), assess completeness across nine dimensions. Be direct about what you know vs. what's missing:

**1. Platform understanding**
- Can you describe what the platform does in 2 sentences?
- Is it clear who the primary paying customer is?
- Is the revenue or value model clear?

**2. Users & roles**
- Are the main user types defined?
- Is it clear what each user type needs to accomplish?
- Are there admin or internal users implied?

**3. Scope**
- Is there a clear list of what's in MVP?
- Is there any indication of what's explicitly out?
- Are there "nice to haves" that should be deferred?

**4. Constraints**
- Are there hard technical constraints (must use X, can't use Y)?
- Are there budget or timeline limits?
- Are there compliance or regulatory requirements?

**5. Business model**
- How does the client make money from this?
- Is pricing clear? Are there tiers, plans, or usage limits?

**6. Integrations**
- Are there third-party systems or APIs the platform must connect to?
- Are there existing systems it must not break or replace?

**7. Success criteria**
- What does "done" look like for the client?
- Are there launch criteria or key metrics mentioned?

**8. Risks and unknowns**
- What's the most critical unknown that would block writing the Platform Specification?
- Are there contradictions in the input (e.g., client says X in one place and Y in another)?

**9. Project context**
- Is there prior work, an existing system, or a version 1 that informs this?
- Are there known stakeholders or approvers mentioned?

## Step 4 — Fill the Gaps (Targeted Questions)

If there are significant unknowns, ask targeted questions — maximum 3 at a time, starting with what blocks progress most.

- Ask about the highest-impact unknown first
- Frame questions with context: "You mentioned [X] — does that mean [interpretation A] or [interpretation B]?"
- Offer options where the answer is likely one of a few: "Is this B2C, B2B, or a marketplace?"
- Wait for answers before asking the next round

Don't ask for information that can be assumed and tagged. If something is reasonably guessable, draft with an `[ASSUMPTION: ...]` tag and move forward.

**Ready to draft when:**
- You can describe the platform in 2 sentences
- You know who the primary user/customer is
- You have a rough sense of what's in MVP (even if incomplete)
- You know at least 2-3 user roles

If you're missing critical information after 2 rounds of questions, flag it as P0 and recommend the user schedule a discovery call before continuing.

## Step 5 — Draft the Platform Specification

Using `01_Context/Platform_Specification.md` template, fill in what you know. Write clearly and concisely. For unknowns:
- Use `[ASSUMPTION: ...]` for reasonable inferences
- Leave sections with `[TO CONFIRM WITH CLIENT]` where client input is genuinely needed

Sections to fill in order of priority:
1. Executive Summary
2. Key Facts
3. User Personas
4. MVP Scope (In and Out lists)
5. Business Model
6. Epic Map (rough — even 4-5 epic titles is fine)
7. Key Integrations (if known)

## Step 6 — Add Epics to the Project Plan

The Project Plan was initialized in Step 2. Now that the Platform Specification is drafted and the Epic Map is in place, add the epics:
- Add each epic from the Epic Map as a pending item in the Phase 2 checklist
- Mark Phase 1 (Foundation) as complete or in-progress based on what was done
- Note any items that still need client confirmation before Epic work can begin

## Step 7 — Surface Open Questions

After drafting, identify what must be confirmed before Epic work can begin. Use the `open-questions` skill (if available) or manually create entries for:
- P0: anything that would block the first Epic from being written
- P1: anything that affects MVP scope or business model

Offer to log them in `03_Discussions/Open_Questions.md`.

## Step 8 — Handoff

Summarize what was done:
- What's now in the Platform Specification (what's confirmed vs. assumed)
- What P0 questions need client confirmation before proceeding
- Recommended next step: schedule foundation workshop with client to confirm the overview, then start