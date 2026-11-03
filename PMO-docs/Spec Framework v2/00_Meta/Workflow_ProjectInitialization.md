?# Workflow: Project Initialization (Session 0)

**When to use**: First session on any new project -- before any Epic work begins.

**Goal**: Establish the foundation. Understand what we know, identify what we need to find out, and produce a client-confirmed Platform Specification that everyone (client, dev, AI) can work from.

**Output**: A signed-off `01_Context/Platform_Specification.md` and a populated `00_Meta/Project_Plan.md`.

---

## Why This Workflow Exists

Starting Epic work without a confirmed foundation is the most expensive mistake in spec work. If the scope, personas, or business model are misunderstood at the start, every Epic built on top of them needs rework. This workflow ensures the foundation is solid before any detailed spec work begins.

---

## Step 0 -- Verify Skills Are Available

This framework uses Cowork skills for key tasks. Skills are not always automatically available -- they must be explicitly added in Cowork.

**Check that the following skills are active before starting:**

| Skill | Used for |
|:---|:---|
| `initialize-project` | Session 0 guided setup |
| `gap-analysis` | Reviewing Platform Spec and Epics |
| `epic-writer` | Drafting new Epics |
| `acceptance-criteria` | Writing testable AC for features |
| `scope-audit` | Checking MVP discipline |
| `open-questions` | Surfacing unknowns from specs |
| `meeting-processor` | Processing meeting transcripts and emails |
| `workshop-prep` | Preparing for client meetings |
| `client-summary` | Creating client-facing summaries |
| `decision-logger` | Logging decisions to Decision_Log.md |

**If any are missing:**
1. Go to the Skills panel in Cowork
2. Upload the `SKILL.md` file for each missing skill from `.claude/skills/[skill-name]/SKILL.md` in this folder
3. The skill will then be available by name in your session

You can proceed without all skills -- but `gap-analysis`, `epic-writer`, and `meeting-processor` are the most critical for daily spec work.

---

## Step 1 -- Dump Everything

Put all client-provided material into `01_Context/`:

- `Client_Brief.md` -- paste the original brief, emails, problem statement verbatim. Do not edit client's words.
- `RawInputs/` -- drop in any attachments: transcripts, documents, wireframes, screenshots, competitor references.

**Rule**: Don't organize yet. Just get everything in one place.

---

## Step 2 -- Run a Discovery Assessment

Read all inputs and answer these questions honestly:

| Question                                                 | What it tells you                      |
| :------------------------------------------------------- | :------------------------------------- |
| Can you describe the platform in 2 sentences?            | If no -> foundation is not clear enough |
| Do you know who the primary paying customer is?          | If no -> business model is unclear      |
| Can you list what is definitely IN the MVP?              | If no -> scope is undefined             |
| Can you list 3+ things that are definitely OUT?          | If no -> scope boundaries don't exist   |
| Do you know the top 3 user roles?                        | If no -> personas need discovery        |
| Are there any hard constraints (budget, timeline, tech)? | If yes -> document them now             |

Log everything you can't answer as Open Questions in `03_Discussions/Open_Questions.md` with priority:
- **P0** = can't proceed without this answer
- **P1** = significantly affects scope or design
- **P2** = clarification that would help

---

## Step 3 -- Draft the Platform Specification

Using `01_Context/Platform_Specification.md`, fill in what you know. For anything uncertain, use `[ASSUMPTION: ...]` tags and/or log as an Open Question.

**Do not delay this step waiting for perfect information.** A draft with assumptions is far more useful than a blank file. The draft surfaces what you don't know.

Fill sections in this order of priority:
1. Executive Summary -- what is it, who is it for
2. Key Facts -- owner, customers, revenue model
3. MVP Scope -- what's IN (checklist), what's OUT (checklist with reason)
4. User Personas -- roles, actions, access level
5. Epic Map -- rough list of epics you expect (can be 2-3 words each at this stage)
6. Business Model -- how money flows
7. Key Integrations -- external services needed

Leave Performance, Security, and Compliance sections until you have more information.

---

## Step 4 -- Identify the Critical Gaps

Before going to the client, run gap analysis on the Platform Specification draft:

> "Review this Platform Specification draft. Identify: (1) sections with assumptions that need client confirmation, (2) missing information that would block Epic work, (3) scope items that seem implied but aren't explicitly stated."

Group gaps into:
- **Must resolve before Epic work** -- P0 blockers
- **Must resolve in first client meeting** -- P1 important
- **Can proceed with assumption, flag for later** -- P2 clarifications

---

## Step 5 -- Prepare for the Foundation Workshop

Use the `workshop-prep` skill (or manually) to prepare:

1. **Confirm list** -- assumptions in the Platform Spec that need client sign-off
2. **Question list** -- P0 and P1 open questions, grouped by topic
3. **Scope validation** -- walk the client through the MVP IN/OUT lists and get explicit confirmation

The goal of this workshop is not to gather new requirements -- it's to **confirm what you've drafted** and resolve the blockers. Keep it focused.

---

## Step 6 -- Process the Workshop Output

After the client meeting:

1. Use `meeting-processor` skill: paste transcript or notes -> get summary, decisions, and spec impact list
2. Update `Platform_Specification.md` with confirmed information
3. Move resolved questions to the Resolved section in `Open_Questions.md`
4. Log decisions in `03_Discussions/Decision_Log.md`
5. Replace `[ASSUMPTION: ...]` tags with confirmed facts, or escalate to P0 questions

---

## Step 7 -- Get Sign-Off

Before starting Epic work, the Platform Specification needs sign-off. This can be:

- **Formal**: Client reviews the document and confirms in writing
- **Lightweight**: Walk through the document in a call, confirm key points, log confirmation in Decision_Log.md

**Do not start Epic work until the Platform Specification is confirmed.** Changes to the foundation after Epics are started multiply rework.

---

## Step 8 -- Initialize the Project Plan

Update `00_Meta/Project_Plan.md`:

- Fill in project name, client, phase status
- List the confirmed Epics from the Epic Map
- Mark Phase 1 (Foundation) as Complete
- Set Phase 2 (Epic Definition) as In Progress
- Log the session in Session History with what was done

---

## Signs You're Ready to Start Epic Work

- [ ] Platform Specification has no P0 open questions
- [ ] MVP scope (IN and OUT) is explicitly listed and confirmed
- [ ] All major user roles are defined
- [ ] Epic Map has at least a rough list of expected epics
- [ ] Client has confirmed the overview (formally or in a meeting)
- [ ] Decision Log has the foundation decisions captured

---

## Common Mistakes

**Starting Epics too early** -- you think you understand the scope but haven't confirmed it. First Epic will need major rework after the foundation workshop.

**Waiting for perfect information** -- you won't get it before starting. Draft with assumptions, surface the gaps, confirm the critical ones. Move forward.

**Scope bloat in the foundation doc** -- the Platform Specification is an overview, not a detailed spec. If you're writing feature-level detail in it, you're doing Epic work. Keep it at the "what and why" level.

**Skipping the Epic Map** -- even a rough list of 5-8 epics gives everyone orientation. Don't skip it.

-