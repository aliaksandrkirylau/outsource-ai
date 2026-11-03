---
name: a01-presale-handover
description: Run Standard A step A01 - receive the pre-sale handover and onboard to project context. Use when a PM is handed a new or transferred project and needs to harvest the handed-over chats and the pre-sale Drive folder, structure the context (problem, sold scope, commitments, assumptions, constraints, risks, source register), build the handover checklist against the PMO Acceptance-From-Pre-sale v2 checklist, compute the A01 control metrics (Handover Maturity Index, Critical Uncertainty Ratio), and seed the project brain. Triggers - "I got a handover", "presale handover", "run A01", "harvest the presale", "what did we get from sales", "what did pre-sale hand over", "score the handover". For a general "onboard this project" or "start initiation", prefer project-router, which scans first and then routes here.
---

# A01 - Pre-sale handover and onboarding

Runs A01 of the PMO Project Initiation standard (Confluence page 4619206688): harvest -> structure -> risks -> checklist + metrics -> project brain. The copilot drafts and computes; the PM reviews and owns every decision.

The control contract lives in the standard, not in this file. Read it from `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`, section A01. If that file's `synced` date is old and Confluence is available, re-read page 4619206688 directly. The scoring rubric is bundled at `references/acceptance-checklist.md`.

Two things to know before you cite anything to the PM:
- Never resolve a step by page title or number - by page ID. Notes from copilot releases before 0.45.0 use the old codes (one lower from A03 on); see the numbering note at the top of `standard-a-contract.md`.
- A01 in the standard cites "Checklist: Acceptance From Pre-sale v2". Only a v1 draft page exists (3285712947). Our rubric is derived from it. If a PM or Sales asks, say that plainly - do not present it as an official v2.

Templates and where things are filed: `${CLAUDE_PLUGIN_ROOT}/references/template-register.md` (A01 section) and `${CLAUDE_PLUGIN_ROOT}/references/pmo-conventions.md`.

## How this skill behaves - read first

This is a GUIDED, staged skill. It does NOT run end to end and hand over a finished result. It works one stage at a time, and at the end of each stage it STOPS, shows what it has so far, and asks the PM to confirm before moving on. Frame every checkpoint like this:

> Stage N done. Here is what I found / built: [the result]. Does this look right? Reply to continue and I will move to Stage N+1: [name of next stage].

Why: a PM running this for the first time should never be surprised by what the copilot did or uploaded. Surface findings before acting on them. (Default mode is guided. If the PM explicitly says "just run it" / "express", you may collapse the review stops - but the brain push at Stage 4 is ALWAYS an explicit gate, no exceptions.)

Two hard rules that never relax:
- Never write to or share a persistent store - the NotebookLM project brain, a shared Google Sheet, a P&L, Jira - without showing exactly what will be written and getting an explicit yes.
- Never send anything to Sales or the client. The copilot drafts; the PM sends and shares.

Every checkpoint below also ends with one line naming what went into `project-context.md`. A01 establishes more durable facts than any other step - the client, the aliases, the problem statement, who owns what - and if they are not written down the next session starts from nothing.

## Output set (what A01 produces)

The standard's own A01 outputs come first, then the three this copilot adds. Everything here is a real file - nothing stays as prose in the chat.

From the standard:

1. **A01 Handover Brief** - the assembled Initial Project / Opportunity Context Summary, including the Client Problem Statement. Markdown in the project folder.
2. **Assumptions & Commitments List** - its OWN document, `assumptions-and-commitments.md`, not a section buried in the brief. It is a mandatory output of the step and it gets referred to for months: what we assumed, what we committed to, who committed it, and where each came from. Split it into assumptions, commitments we made, commitments the client made, and constraints.
3. **Source / Links Register** - `source-register.md`, kept ACTIVE through the whole project.
4. **Pre-sale Handover Questions / Gaps List** + the Sales-sync agenda.
5. **Project NotebookLM knowledge container**, seeded - only after the Stage 4 gate.

Added by the copilot, and say so rather than implying the standard asks for them:

6. **Handover checklist as a Google Sheet** - the evidence artifact the PM shares for confirmation.
7. **Risk & Problems Log** - structured records, severity plus a route to A05/A06.
8. **The scored statuses file** - `a01-handover-statuses.yaml` in the project folder. Fixed name, because the re-score pass and the Sheet both read it.

### Early drafts count as outputs too

A01 always throws off first drafts of things later steps own - a stakeholder matrix, scope boundaries, a rough role list, an early risk view. Do NOT drop them because "that belongs to A02" and do not leave them in the conversation.

Write each one out, mark it clearly as an early draft built from handover context rather than the output of its own step, and name which step will take it over. The Alchemy run is the model: its checklist cites a draft stakeholder matrix with client-side email gaps flagged inline, produced at A01 and handed to A02. That draft was worth more than a blank.

List every draft you produced at the Stage 5 checkpoint so the PM knows what exists.

## Inputs

Read `<project folder>/project-context.md` first. If it exists, `project-router` or an earlier session has already recorded the project and client names, the aliases, the Drive folder and the chats - use them and do not ask again. Ask only for what is genuinely missing.

Where to look: since Aug 2026 the presale material is COPIED into the project's `01_Presale` folder (PMO Private > Projects <YYYY> > <Client> - <Project>) at setup, so check there first; the original presale folder is the fallback. See `pmo-conventions.md`.

If it does not exist, ask the PM for these in ONE question: the handed-over chat(s) name/link, the pre-sale Drive folder link, the project + client name. Then create the file from the answers before starting the harvest, so nothing gathered below is lost if the session ends early.

If the connectors are unavailable or the sources are empty, STOP and say so. Do not run the harvest on nothing and do not fall back to the bundled `references/example-input.yaml` - that file is canned demo content and scoring a real project against it would produce a fabricated maturity index with a real project's name on it. Either the PM points you at material you can actually read, or they paste it in, or A01 does not run yet.

## The staged procedure

### Stage 0 - Frame and confirm inputs
Confirm the chat(s), Drive folder and project name. Read only the file LIST of the Drive folder + the chat exists - not the deep content yet. Show the PM the source inventory (how many files, what types, the chat date range) and confirm this is the right material before reading deeply.
CHECKPOINT: "Found N sources [list]. Is this the right handover material? Reply to start the harvest (Stage 1)."

### Stage 1 - Harvest and show findings
Now read deeply: full chat history (not just recent - this is not the daily digest), every Drive file INCLUDING the contents of Sheets (budgets, WBS, estimates). Structure: sold scope, key commitments, client expectations, milestones/timeline/budget, contract type and delivery model, assumptions, constraints, dependencies, and the document/links inventory. Build the Source / Links Register (markdown) as you go.

CLIENT PROBLEM / PAIN - the most important thing in A01, never skip it lightly. Artem (PMO workshop) is emphatic: at A01 the PM must find out the client's REAL pain - what problem we solve, why they actually came to us, what the project is FOR. A deliverable description ("build a mobile app / robot / platform") is NOT the goal; it is the solution to some underlying pain. Capture the problem in pain/outcome terms, not deliverable terms. If the harvest does not make the real pain clear, say so explicitly, mark it UNCLEAR, and make it the first question for the Sales sync - do not paper over it with a feature description. This is an A01 verification criterion ("the client's problem/pain point is captured at a high level or marked as unclear") and the seed of A04.

CHECKPOINT: present the structured findings + the register, and LEAD with the Client Problem Statement so the PM confirms it specifically. Nothing has been written to the brain or shared. "Here is the client problem as I read it, and what I found. Is the problem right, and anything wrong or missing, before I look at risks (Stage 2)?"

### Stage 2 - Risk and problems deep-dive
Spend real attention here - this is the part a PM most needs. Do a focused pass for: candidate risks, sold-vs-deliverable mismatches, under-estimations, missing scope, dependencies and the practical problems the PM will have to deal with in later stages. Record each as a structured row: problem | why it matters | severity (high/med/low) | route to (A05 validate / A06 risk / staffing / other). Do not resolve them here - A01 surfaces and routes; A05/A06 own them.
CHECKPOINT: present the Risk & Problems Log. "These are the problems I see in what was sold. Agree with the read and severities before I build the checklist (Stage 3)?"

### Stage 3 - Checklist, score, and the confirmation Sheet

Where the rubric comes from, in this order: `references/acceptance-checklist.md` bundled with this skill is the working copy and what you score against. `scripts/score_handover.py` carries the same 28 items with their core/critical flags and is authoritative if the two ever disagree - it is the thing that computes the number. Confluence page 3285712947 is the backup, for when the bundled copy looks stale or someone disputes an item. Do not rebuild the rubric from memory and do not add items to it mid-run.

- For each item in the rubric, mark a status from the harvest (`gathered` / `partial` / `missing` / `na`).
- `na` is not free. It REMOVES the item from the denominator and therefore RAISES the maturity score, so every `na` needs a real reason in the statuses file and the PM's agreement. The scorer prints what the score would have been without the exclusions - show the PM that line, do not quietly report the flattering number.
- EVIDENCE MUST BE A REAL LINK, not a description. For every `gathered` / `partial` item, cite the actual URL of the exact artifact (Drive file, Google Doc/Sheet/Slides, or a Google Chat message permalink) plus a short locator (slide/section/cell/date). A line like "proposal Key Assumptions 01-04" is not enough - link the proposal and name the slide. The point: when the PM shares this with Sales, presales can click straight to the document and confirm "yes, that is the correct and current artifact" with zero ambiguity. Each evidence link should correspond to a row in the Source / Links Register.
- Write the statuses to `<project folder>/a01-handover-statuses.yaml` - that exact name, shaped like `references/example-input.yaml`, with the reason as a trailing comment on every `partial`, `missing` and `na`. Fixed name and location because the re-score pass reads the same file back and the Sheet is built from it. Then run the scorer - DO NOT compute the metrics by hand:
  ```
  python3 "<PLUGIN_ROOT>/skills/a01-presale-handover/scripts/score_handover.py" "<project folder>/a01-handover-statuses.yaml"
  ```
  `python3` in the Cowork sandbox; `python` if you are running on a Windows machine
  directly. Substitute the real plugin folder for `<PLUGIN_ROOT>`. If the scorer cannot run, say so - do NOT compute
  the two indices by hand and present them as the deterministic number.
  It returns the Pre-sale Handover Maturity Index (target >= 70%) and the Critical Uncertainty Ratio (target <= 30%) deterministically. One thing to be straight about if asked: the standard defines confirmed-over-relevant but says nothing about partial credit, so counting `partial` as 0.5 is OUR convention. It moves the headline number and it is ours, not the standard's.
- Build the confirmation Sheet in the project Drive folder, GENERATED FROM the statuses file rather than typed fresh - on the real Alchemy run the hand-built Sheet and the scored file had already drifted apart by the time it was published, with one item shown as gathered that had been scored `na`. Same source, no drift.

  Layout, which follows the Alchemy sheet because that one worked:
  - Row 1: `<Project> | A01 Handover Checklist`.
  - Row 2, on one line: both metrics with their PASS / BELOW flags, `Updated <date> by PM (draft)`, and the instruction to the recipient - "click each Evidence link, confirm it is the correct and current artifact, mark Y/N". The numbers travel WITH the artifact; a Sheet whose score lives only in a chat window cannot be checked by the person confirming it.
  - Row 3, headers: `Item | Status | Evidence (click) | Locator | Gap / Note | Owner | Owner confirms (Y/N)`.
  - Then the 18 CORE items only, in rubric order. The ten nice-to-haves are tracked in the statuses file and stay out of this Sheet - nobody should be asked to formally confirm the customer's time zone alongside the contract.
  - `Owner confirms`, not "Sales confirms". The Owner column on a real run reads BA / DM, DM / Client IT, Delivery, PM as often as Sales, and asking the wrong person to sign off is how a checklist gets ignored.
  - Evidence is a clickable hyperlink with a short label; the precise position goes in Locator (`Development tab`, `FE-MVP-1..18`, `BO-1..10`).
  - Gap / Note carries real substance, not a one-liner. What is open, what changed, what is contractual versus indicative, who owes what. Multi-line where it needs to be - the Alchemy stakeholder row holds the whole client-side list with `EMAIL MISSING` flags inline, and that is the right level of detail.

  Build it; do NOT share it - the PM shares it.
- From every `missing` / `partial` item draft the Gaps List + a short handover-sync agenda (owner per gap: Sales / Account / Pre-sale / BA / SA / Tech Lead / client-side; flag material vs capture-later).
CHECKPOINT: show the metrics, the gap list, and the Sheet link. "Maturity X%, Uncertainty Y%. Here is the checklist Sheet to send to Sales, and the gaps. Review it - OK to seed the project brain (Stage 4)?"

### Stage 4 - Seed the project brain (HARD WRITE GATE)
If no project brain exists yet, it is a mandatory starting artifact and gets created here. Follow the brain-seeding rules in `${CLAUDE_PLUGIN_ROOT}/references/pmo-conventions.md`: native Docs and Slides sync cleanly, Office files and MCP-pushed Sheets do not; combine many small documents into one source.

Hand the upload itself to `project-brain` (feed mode) - it holds the inventory, hold-out and verification mechanics in one place. The gate below stays here and stays hard; what moves is the doing, not the decision.

**Say one thing to the PM at this checkpoint that nothing else will tell them:** this seeding is the START of the brain, not the whole job. The normal failure is a brain seeded once at handover and never touched again, which scores as a present artifact and answers nothing useful by month three. The copilot will offer to add things as they are produced, and they can ask "is the brain current" at any point. Thirty seconds here is what stops the brain becoming a formality.

Before pushing anything: show the PM the exact upload inventory - which documents and notes go into the brain - and what is being HELD BACK. SENSITIVITY RULE: no money in the brain (no client currency, salaries, rates, margins, P&L); worked and paid hours are fine. CONTRACT TEXT IS ALSO HELD BACK - contract version review happens in a separate confidential notebook, never the shared project brain (standard A03, page 5142544653). Money lives only in sensitive Drive storage (A11). List the redactions explicitly.
CHECKPOINT (mandatory, even in express mode): "I will push these [N items] to the project brain and hold back these [financial items]. Confirm and I will create/seed the NotebookLM container." Only on an explicit yes, create or confirm the per-project NotebookLM and push. This is the per-project brain, distinct from the org-wide Superbrain (PMO standards) - keep them separate.

### Stage 5 - Assemble and hand off

Assemble the A01 Handover Brief from the approved pieces: Client Problem Statement, Context Summary, the scored checklist with both metrics and their flags, Risk & Problems Log, Gaps List, links to the Assumptions & Commitments List and the Source / Links Register, and a one-line "ready / not ready to advance" call for the PM to confirm.

Write the Assumptions & Commitments List as its own file at this point if you have not already - `assumptions-and-commitments.md`. It is a mandatory output in its own right, not a heading inside the brief, and it is the document people come back to when someone asks six months later what we actually promised. Each line carries where it came from and who said it.

Then list the early drafts you produced, each marked as a draft and pointing at the step that owns it. Do not skip them because they are not this step's formal outputs.

Surface, do not silently pass: a material sold-versus-deliverable mismatch, a maturity below 70%, OR an uncertainty above 30%. Both metrics carry a threshold and both deserve naming - a project can pass on maturity and still be carrying too many unresolved critical gaps. If the PM proceeds anyway (a project that "started yesterday"), record the justification - a thin step is justified-and-recorded, never invisible.

Put the actions in `pm-tasks.md`, tagged with the project: every gap that needs Sales, the sync itself, anything the PM has to chase. Those are the whole point of the gaps list and they evaporate if they only ever exist in this conversation.

Then bring `project-context.md` up to date and say in one line what went in. At minimum: the confirmed client problem statement, the people named in the harvest and what each owns, where the brief and the checklist Sheet were filed, the brain's name or ID, the two metric values with today's date, the open gaps, and any justification recorded above. A02 and A04 read this file first, so anything left out here gets asked again.

The brain was seeded at Stage 4, but the pieces produced SINCE then were not in that inventory - the Handover Brief itself, the Assumptions and Commitments List, the Risk and Problems Log, the Source Register. Offer them now via `project-brain` (feed mode). The Assumptions and Commitments List especially: it is the document people come back to when someone asks six months later what we actually promised, which is exactly the question the brain gets asked.

And anything the copilot got wrong, or asked for and could not do, goes in `<workspace>/copilot-feedback.md`.

## Re-score after the handover sync (second pass, later)
After the PM runs the recorded Sales sync, recap the call, update `<project folder>/a01-handover-statuses.yaml` with what was clarified, re-run the scorer, and show the DELTA (maturity before -> after, gaps closed, remaining). The before-values come from `project-context.md`, where Stage 5 recorded them with a date - read them from there rather than asking the PM what the old number was. Then regenerate the Sheet from the updated file so the shared artifact and the score cannot drift apart, and update the `Updated <date>` line in row 2. The aim is to clear >= 70% / <= 30% before A01 hands off. This re-estimates the INDEXES only. Re-estimating the project itself (realistic hours, scope realism) is A05, and the economy is A08 - both after the A09 baseline gate. A01 routes mismatches forward; it does not re-price.
