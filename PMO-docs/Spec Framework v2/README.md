# AI-First Requirements Framework

> **Version**: 2.0
> **Purpose**: Claude/Cowork-first framework for taking any project from raw client brief to development-ready specifications

---

## What This Is

A structured spec framework designed for a PM/BA working with Claude. You copy this folder to a project, give Claude your context, and it guides you -- through workflows, templates, and skills -- to produce specifications that are clear, client-confirmed, and ready for a developer to feed into their own AI.

**Built on real project experience.** The patterns here come from producing 590+ pages of specs on a real client project (Practice Perfect, you can contact Anton Oparienko).

**How it works:**
- The framework lives in this folder. Copy it to each project -- one copy per project.
- Claude (via Cowork) acts as your BA partner: analyzing input, drafting specs, surfacing questions, running validation.
- Skills handle specific tasks: writing epics, gap analysis, processing meetings, workshop prep.
- You stay in control via the 8-step loop (Analyze -> Plan -> Approve -> Execute -> Report -> Question Check -> Review -> Next Steps).

---

## Setup

### 1. Copy this folder to your project

Name the copy after the client (e.g., `ClientName Spec`). Every project gets its own copy -- it tracks that project's decisions, questions, and history.

### 2. Open the folder in Cowork

In the Cowork desktop app, select this project folder as your workspace.

### 3. Verify skills are active

Skills must be loaded via the Cowork Skills panel before use. Check that these are active:

| Skill                | What it does                                                                    |
| :------------------- | :------------------------------------------------------------------------------ |
| `initialize-project` | Session 0: assesses input, drafts Platform Spec, initializes project plan       |
| `epic-writer`        | Drafts a complete Epic from raw input, including Given/When/Then ACs            |
| `gap-analysis`       | Reviews any spec artifact for completeness and logic gaps                       |
| `scope-audit`        | "Is this actually MVP?" -- run proactively the moment any new scope is proposed |
| `open-questions`     | Surfaces unknowns from spec files, formats for Open_Questions.md                |
| `meeting-processor`  | Transcript/email -> summary, follow-up draft, spec impact plan                  |
| `workshop-prep`      | Prepares prioritized question list and agenda for client meetings               |
| `client-summary`     | Plain-language Epic or platform overview for client review                      |
| `decision-logger`    | Formats and logs decisions to Decision_Log.md with contradiction check          |

To add a missing skill: open the Skills panel in Cowork -> upload `.claude/skills/[skill-name]/SKILL.md`.

---

## Session 0: Your First Session

Before any Epic work, you need a confirmed foundation. **Session 0 builds that foundation.**

**1. Dump everything you have**
- Paste client emails, brief, meeting notes verbatim into `01_Context/Client_Brief.md`
- Drop any files (transcripts, documents) into `01_Context/RawInputs/`

**2. Open a Cowork session and say:**
> "Let's initialize this project. I've put everything I have into Client_Brief.md and RawInputs/. Run the initialize-project skill."

The skill will assess what you know vs. what's missing, ask targeted clarifying questions, draft `Platform_Specification.md`, and surface open questions for the client.

**3. Get client confirmation**
Before Epic work starts, the Platform Specification needs client sign-off. Minimum: walk through it on a call and log the confirmation in Decision_Log.md. Use the `workshop-prep` skill to prepare.

**4. Start Epic work**
Once Platform Spec is confirmed: use `epic-writer` for each Epic area. The 8-step loop governs all Epic work.

---

## Typical Project Flow

```
Client contact
     ?
Session 0 (initialize-project skill)
  -> Dump raw inputs -> Platform Specification draft -> Client sign-off
     ?
Epic work: Workflow_Main.md (8-step loop)
  -> Epic-01 -> gap-analysis -> acceptance-criteria -> client review
  -> Epic-02 -> ... repeat
     ?
Validation: Workflow_Validation.md
  -> All P0 questions resolved -> scope confirmed -> dev handoff
     ?
Development handoff
  -> Dev receives: Platform_Specification.md + all Epic files
```

---

## When to Use What

| Situation | Action |
|:---|:---|
| Starting a new project | `initialize-project` skill |
| Meeting with client coming up | `workshop-prep` skill |
| Just had a client meeting | `meeting-processor` skill |
| Starting a new Epic | `epic-writer` skill |
| Just drafted an Epic | `gap-analysis` skill |
| Writing user stories | `acceptance-criteria` skill |
| Adding new scope or features | `scope-audit` skill |
| Found an unknown | Log in `Open_Questions.md` |
| Client makes a decision | Log in `Decision_Log.md` |

---

## Folder Structure

```
|-- CLAUDE.md                    <- AI instructions -- read by Claude automatically
|-- README.md                    <- You are here
|-- PROMPT_GUIDE.md              <- How to talk to Claude; skill trigger phrases
|-- BEST_PRACTICES.md            <- Goldilocks Principle, scope discipline, lessons learned
|
|-- 00_Meta/                     <- Workflows, templates, question banks, validation
|   |-- Project_Plan.md          <- Active task tracking for your project
|   |-- Workflow_Main.md         <- The 8-step loop (core process for Epic work)
|   |-- Workflow_ProjectInitialization.md  <- Session 0 full workflow
|   |-- Workflow_Validation.md   <- Quality assurance process
|   |-- Troubleshooting.md       <- When things go wrong with Claude sessions
|   |
|   |-- Templates/
|   |   |-- Epic_Template.md     <- Template for all spec work
|   |   +-- Meeting_Templates/  <- Templates for meeting-processor output
|   |
|   |-- QuestionBanks/           <- Discovery questions by project type
|   |   |-- Web_App_Questions.md
|   |   |-- Mobile_App_Questions.md
|   |   |-- SaaS_Questions.md
|   |   +-- Integration_Questions.md
|   |
|   +-- Reports/                 <- Validation report outputs
|
|-- 01_Context/                  <- Project context and raw inputs
|   |-- Platform_Specification.md  <- Foundation doc: what/who/in-out/epic map
|   |-- Client_Brief.md            <- Raw client inputs (verbatim)
|   |-- Glossary.md
|   +-- RawInputs/               <- Transcripts, emails, attachments
|
|-- 02_Epics/                    <- All specifications live here
|   +-- Epic-XX_Name_SPEC.md     <- One file per epic; features are sections within
|
|-- 03_Discussions/              <- Decisions, questions, meetings
|   |-- Open_Questions.md        <- All unknowns, prioritized P0/P1/P2
|   |-- Decision_Log.md          <- All confirmed decisions with rationale
|   |-- Developer_Questions.md   <- Dev clarifications during implementation
|   +-- Meetings/                <- meeting-processor output lands here
|
+-- 04_Designs/                  <- UI/UX artifacts (optional)
```

---

## Core Philosophy

**Epics are the primary artifact.** Each Epic file contains the full spec for that area -- overview, all feature sections, acceptance criteria, edge cases, business rules, open questions. One file = complete context. No separate feature files.

**Platform Specification is the foundation.** Before any Epic work, you need a confirmed overview: what you're building, for whom, what's in MVP, what's out. Get client sign-off on this first.

**Specs describe WHAT and WHY. Never HOW.** No API schemas, no database structures, no specific libraries. The developer's AI handles technical architect