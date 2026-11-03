# Workflow: Main Spec Process (8-Step Loop)

This is your core operating process. Every substantial task -- drafting an Epic, processing new client input, running validation -- follows this loop.

---

## The 8-Step Loop

### 1. Analyze
**Claude reads relevant context files and current state before doing anything.**

Files to read:
- `01_Context/Platform_Specification.md` -- scope, personas, business model
- `00_Meta/Project_Plan.md` -- current tasks and decisions
- `03_Discussions/Open_Questions.md` -- active blockers
- Relevant Epic files in `02_Epics/`

**Prompt pattern:**
> "Analyze the current state. What's the highest-priority task based on Project_Plan.md and Open_Questions.md?"

---

### 2. Plan
**Claude writes a specific plan as a checklist in `00_Meta/Project_Plan.md`.**

Format:
```markdown
## Current Session: [Session Name] -- [Date]
- [ ] Task 1: [specific action]
- [ ] Task 2: [specific action]
- [ ] Task 3: [specific action]
```

**Prompt pattern:**
> "Update Project_Plan.md with a checklist of specific tasks for this session."

---

### 3. Approve
**You review and approve (or adjust) the plan before execution.**

Options:
- [x] "Approved, proceed"
- ? "Adjust: [what to change]"
- [no] "Let's do [different thing] instead"

**Never skip this step.** The loop exists to keep you in control.

---

### 4. Execute
**Claude creates or edits files based on the approved plan.**

Outputs go to:
- `02_Epics/` -- Epic spec files (`Epic-XX_Name_SPEC.md`)
- `01_Context/` -- Platform Specification, Glossary, Client Brief
- `03_Discussions/` -- Open Questions, Decision Log, meeting notes

**Note:** Features are documented as sections WITHIN Epic files. There are no separate feature files.

---

### 5. Report
**Claude gives a brief summary of what was done.**

Format:
```
Changes made:
- Created Epic-02_EventManagement_SPEC.md with 4 feature sections
- Updated Platform_Specification.md MVP scope (Camps moved to Out of Scope)
- Added 2 terms to Glossary.md

Files modified: [list]
```

---

### 6. Question Check
**Claude logs any new unknowns surfaced during the work.**

Output: Updates to `03_Discussions/Open_Questions.md`

Priorities:
- **P0** -- Cannot proceed without this answer
- **P1** -- Significantly affects scope or design
- **P2** -- Clarification that would help

---

### 7. Review
**You verify the work for accuracy and alignment.**

Checks to run:
- Does this match what the client actually said?
- Are there contradictions with Platform_Specification.md or other Epics?
- Are [ASSUMPTION: ...] tags used where appropriate?
- Run `gap-analysis` skill on any newly drafted Epic

---

### 8. Next Steps
**Claude updates the project roadmap.**

- Mark completed tasks `[x]` in Project_Plan.md
- Archive completed items in Session History (don't delete)
- Add the next 3-5 logical tasks to the active list

---

## Work Modes

### Mode 1: New Client Input

**Trigger:** Client sends email, meeting notes, or transcript arrives.

1. Paste into `03_Discussions/Meetings/` or directly in chat
2. Run `meeting-processor` skill
3. Review: summary + follow-up draft + spec impact plan
4. Decide what to apply -- then follow the 8-step loop

---

### Mode 2: Epic Drafting

**Trigger:** A new Epic area needs to be specced.

1. Run `epic-writer` skill
2. Skill reads Platform Specification for context, asks clarifying questions if needed
3. Follow 8-step loop to review and finalize
4. Run `gap-analysis` after draft is complete

---

### Mode 3: Scope Change

**Trigger:** Client requests new feature, or scope shifts.

1. Run `scope-audit` skill immediately -- before adding anything
2. Scope-audit evaluates MVP fit: include, simplify, or defer
3. Log outcome in `03_Discussions/Decision_Log.md`
4. Apply changes if approved, update Out of Scope sections if deferred

---

### Mode 4: Validation Sweep

**Trigger:** End of a spec phase, before client review, or when something feels off.

1. Run `gap-analysis` on the relevant artifact (Platform Spec, Epic, or full spec set)
2. Address ? critical issues immediately
3. Log ? medium issues as open questions
4. Log all findings in validation report

---

## Staying on Track

### Every session should:
- Start by reading `00_Meta/Project_Plan.md`
- End with `00_Meta/Project_Plan.md` updated and current

### Never:
- Add unplanned scope without running `scope-audit` first
- Leave "TBD" in a spec -- log it as an open question
- Skip the Approve step (Step 3)

### Signs of trouble:
- **10+ epics** -- consolidate or scope creep is happening
- **50+ open questions** -- not enough discovery, schedule a client intensive
- **Epic changes daily** -- lock down, validate, don't keep building on sand

---

## Related Files

- **Session 0 workflow**: `00_Meta/Process_