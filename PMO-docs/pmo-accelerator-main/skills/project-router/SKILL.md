---
name: project-router
description: Works out where a project stands against the PMO initiation standard and which step to do next, then hands over to the skill that does it. Use on a project that is genuinely NEW - just sold, just handed over - or one that `map-existing-project` has already mapped - "I got a new project", "onboard this project", "what's left before we can start", "what should I do next on X", "which step am I on", "start initiation on X", "is this project ready to start", "what's the next step here". NOT for a project that has been running for months and that Claude has never seen - that goes to `map-existing-project` first. Scanning a live project's folder finds almost nothing, and this skill would read that emptiness as a project that never started and send a six-month-old delivery back to pre-sale handover. Checks which Standard A (A01-A14) outputs already exist, scores readiness for the A09 go/no-go gate, and points at the project's NotebookLM notebook. Run `copilot-setup` once before using this.
---

# project-router - onboard a project and route to the next step

This is the router, not a wizard. Real projects do not run A01 to A14 in order - on live projects the PM often has several steps done already, out of sequence, because the material supported it. So this skill first finds out what ALREADY exists, then routes to what is thinnest, and lets the PM pick any step directly. The standard itself says the order is flexible and steps run in parallel; this skill honors that.

It handles a BRAND NEW project (nothing has happened yet) and a project that `map-existing-project` has already mapped. For a project that already exists in the real world but has never been mapped into the copilot, see the next section - that is takeover's job, not this one.

## How this skill relates to map-existing-project

They are a pair, and the split is about EVIDENCE, not about how the PM got the project:

- `map-existing-project` establishes ground truth on a project nobody has mapped. It sweeps Drive, Chat, mail, Jira, Confluence, Calendar and NotebookLM, and produces a source register plus a takeover brief.
- `project-router` (this skill) routes the WORK once that ground truth exists, or once the PM already knows the material.

Two questions people get wrong here, so be precise:

- It is NOT "did you inherit it". A PM who just finished a takeover inherited it too.
- It is NOT "do you know the project". A PM can know a project intimately while the copilot knows nothing about it - that is the normal state of every project in their portfolio on day one.

The actual question is: **has this project been mapped into somewhere the copilot can work from?**

Before deciding, LOOK for the evidence in the project folder:
- `takeover-brief.md` - a takeover has already run. Do NOT send them back. Read it, use its artifact scorecard and stage call, and go straight to routing (Stage 3). Skip Stage 1's scan unless the brief is more than a few weeks old or the PM asks for a fresh one.
- `source-register.md` - the places-we-look list already exists and is better than anything this skill would build. Do not offer to recreate it.

If neither exists, the deciding question is whether the project is BRAND NEW or already exists in the real world:
- **Brand new** - nothing has happened yet beyond a handover or a signature. Carry on here; A01 is the right on-ramp.
- **Already running, or already part-way through initiation** - route to `map-existing-project`, even if the PM knows it perfectly well. A folder scan cannot see Drive, Chat, Jira, mail or Confluence, which is where an existing project actually lives.

### The failure this prevents

A PM has run a project for six months and opens the copilot on it for the first time. The project folder is nearly empty, because they never used Claude on it. If this skill scans that folder it will report 2 of 13 steps and route them to A01 pre-sale handover - on a project that has been delivering since spring. That is nonsense, and it is the most likely first experience for an alpha PM.

So: if the scanner returns a near-empty result and the PM has told you the project is live, do not believe the scan. Stop and route to `map-existing-project`. An almost-empty folder on a running project means the material is elsewhere, not that the work was never done.

Before Stage 0, check `<workspace>/pm-copilot-setup.md`. It records which connectors were confirmed working. If a connector this run needs is listed as not working, say so UP FRONT rather than failing at the tool call. If the file is absent, copilot-setup has not run - offer it, but do not force it.

The contract for every step is in `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`. The 23 mandatory starting artifacts are in `${CLAUDE_PLUGIN_ROOT}/references/initiation-artifacts-checklist.md`. Templates are in `${CLAUDE_PLUGIN_ROOT}/references/template-register.md`. Read from those rather than reciting from memory.

## How this skill behaves - read first

Guided and staged. One stage at a time, STOP at each checkpoint, show what you found, get a yes. The router RECOMMENDS a next step; the PM decides. Never march the PM through all 13 steps; surface state and route.

Two hard rules that never relax:
- Never write to or share a persistent store - the project brain (NotebookLM), a shared Sheet, a P&L, Jira - without showing exactly what goes in and getting an explicit yes.
- Never send anything to Sales or the client. The copilot drafts and routes; the PM sends.

## What this skill produces (the output set)

1. Initiation state map - which A01-A14 outputs exist / are thin / are missing, with a readiness score and "what's needed before the A09 gate" (from the scanner).
2. A recommended next step + the reasoning, plus the full menu (any step is directly invokable).
3. The per-project folder and its `project-context.md`, if not already there.
4. The project brain located or created and pointed at (seeding is gated, and runs inside the step skills, not here).
5. The "places we look" list (chats, Drive folder, Jira, contract state) - the seed of the A02 comms artifact. If `source-register.md` already exists from a takeover, point at it instead of producing a thinner duplicate.

## The staged procedure

### Stage 0 - Frame the project, and check you are the right skill
First check the project folder for `takeover-brief.md` and `source-register.md` (see the section above). That decides which of three ways this goes, and you should say which one you are in:

- **A takeover brief exists.** Say so, summarise its stage call and artifact score in two lines, and jump to Stage 3 to route. Do not re-run the sweep and do not ask whether they inherited the project - that is already answered.
- **No brief, and the project is brand new.** Normal path, continue below.
- **No brief, and the project already exists in the real world** - running, or part-way through initiation. Route to `map-existing-project` and stop, regardless of how well the PM knows it.

Read the PM's `pm-profile.md` before asking anything. If the project is already a row in their portfolio table, the client, aliases, Drive folder, Jira key and chats are recorded there.

Then ask, in one message, only for what is genuinely missing: the project and client name, the project folder, the handed-over chat(s), the Drive folder, and - the one that decides the branch above - whether anything has actually happened on this project yet, or whether it is genuinely at the starting line. If this is a project the profile does not know about, offer to add it as a row once the names are settled.
CHECKPOINT: "Onboarding [project]. It looks [fresh / partly done / already mapped by a takeover on DATE]. I will scan what already exists and tell you where you are - nothing gets written. OK to scan (Stage 1)?"

### Stage 1 - Scan the initiation state (the deterministic beat)
Run the state scanner on the project folder - do NOT eyeball it:

```
python3 "<PLUGIN_ROOT>/skills/project-router/scripts/scan_initiation_state.py" "<project folder>"
```

Substitute the real plugin folder for `<PLUGIN_ROOT>`, and quote both paths - plugin folders
often sit under a user name containing a space.

Which Python: in Cowork the sandbox is Linux, so `python3`. If you are running commands
directly on the PM's own machine instead - the Code tab - Windows has `python` (a stock
python.org install provides no `python3`, and that name opens the Microsoft Store) while
macOS has `python3`.

Do not assume either one exists. The copilot's servers ship as extensions that bring their
own runtime inside Claude, so nothing in setup puts Python or `uv` on the PM's machine any
more - a PM can have a fully working copilot and no system Python at all. If `uv` happens to
be there, `uv run --no-project python <script>` works on either platform and is the best
option; if it is not, fall back to whichever Python the machine has, and if it has none, say
so rather than guessing.

If the scanner cannot run at all, say so plainly and read the folder listing yourself. A hand
read is worth less than the scanner but far more than a silent failure - and never present a
hand read as the deterministic number.

It gives you three things:

1. **The A-step map** plus overall coverage and readiness for the A09 gate. This answers "what work is left". Four statuses, and the difference between two of them matters:
   - `present` - a file names the step (`A04-project-description.md`) or names the artifact (`risk-register.md`). Counted.
   - `thin` - named right but tiny, so possibly a stub.
   - `possible` - the ONLY evidence is a bare keyword or a generic phrase. NOT counted, and you should not route on it without asking. On real projects this is as often an unrelated file as a deliverable: `onboard` matched two client onboarding-flow feature specs and claimed the pre-sale handover was done; `kickoff` matched a delivery tracker and claimed the client kick-off was prepared. Read the possible list out and let the PM settle each one in a word.
   - `missing` - nothing at all.

   The report prints the match reason next to each step. Use it. "A01 present because the file is called A01-handover-brief.md" and "A01 possible because something had onboard in the name" deserve very different amounts of trust, and the PM cannot tell them apart unless you say so.

   Coverage counts material ON DISK, not work finished - a draft agenda counts as present. Say that when you quote the number, because a PM will repeat it to their lead.
2. **The mandatory-artifact map** against the 23-item Starting Project Artifacts Checklist. This answers "what will someone ask me for". Note the three states carefully: found locally, needs a system check, and not found locally. Most of the 23 live in Drive, Jira, Confluence, Chat or NotebookLM, so the scanner reports them as UNVERIFIED, not missing. Do not turn an unverified artifact into a missing one when you summarise - go and check it, or say it is unchecked.
3. **Unplaced files and policy flags.** Anything the scanner could not classify is listed rather than dropped - show that list, the PM usually knows what those are in one line. And if it flags a money-bearing file inside the common project folder, raise that immediately; the P&L belongs in the Sensitive folder only.

Three more sections worth reading out when they appear:

- **Probably noise.** One phrase matching five or more files, which is the signature of a bulk export where every document happens to share a phrase. On a real project 28 feature specs all matched "acceptance criteria" and inflated A05. Say it is noise rather than treating it as corroboration.
- **The two maps disagree.** The step map and the artifact map run off separate keyword tables, so an artifact can be found locally for a step the step map did not count. Usually the artifact is real and the step should count. Resolve it with the PM instead of printing a contradiction and moving on.
- **Copilot's own files.** `project-context.md`, `source-register.md`, the feedback log and anything named `copilot-*` are listed but never scored as deliverables - a notes file discussing the project description is not the project description. If the report says there is no `project-context.md`, the copilot has no memory of this project yet and Stage 2 should create one.

Detection uses step codes, filenames and content signals, so it can still misclassify. Present the map and CONFIRM it before routing on it.

If the scan comes back nearly empty on a project the PM has told you is live, stop and re-read the section at the top of this skill. That is the signature of a running project whose material lives in Drive, Chat and Jira rather than on disk - route to `map-existing-project` rather than concluding no work has been done.

If the connectors are available, spend a minute confirming the artifacts marked needs-a-system-check rather than leaving them unknown - the project brain, the Drive folders, the chats, PROREP and the board are quick lookups and they move the number a lot.

CHECKPOINT: show both maps. "Here is where the project stands: [step map]. Coverage X%, ready-for-gate Y%, [N] of 23 mandatory artifacts confirmed. Does this match reality - anything mislabelled, or anything that lives somewhere I did not look?"

### Stage 2 - Locate the brain + the places-we-look list
Check whether a project brain (NotebookLM) already exists for this project; if not, note that one is mandatory (A01/A11) and will be created inside the handover step, not here. Assemble the "places we look" list from Stage 0 (chats, Drive, Jira, contract state) - this is the seed of the A02 communication artifact and belongs in the project folder.
If the per-project folder does not exist, offer to create it. Then write or top up `project-context.md` in it - the project and client names, every alias, the Drive folder, the chats, the board, the brain, and the people you have identified so far. That file is what stops the next session re-asking all of this; it is the copilot's own local note, so write it and say you did rather than gating it. Keep A-block docs in General/PM per the PMO Drive layout; money never in the project folder.
CHECKPOINT: "Brain: [found / to be created at handover]. Places-we-look: [list]. I have put this in `project-context.md` so we do not go over it again. Anything wrong or missing?" Creating a Drive folder is still a gated write; the local context note is not.

### Stage 3 - Route
Recommend the next step from the state map, with the reasoning, and give the menu so the PM can pick anything.

Skills that exist and are ready to run:
- Fresh handover, or A01 missing or thin -> `a01-presale-handover` (harvest, brain, score). The usual on-ramp.
- A01 done, A02 or A04 thin -> `a02-a04-stakeholders-and-description` (stakeholders and description from the harvest).
- A05 or A06 thin -> `a05-a06-scope-and-risks` (scope and estimate realism, then risks).
- A07 or A08 thin -> `a07-a08-roadmap-and-economy` (roadmap and resource plan, then the economy check).
- A01-A08 all present -> `a09-baseline-gate` (A09). This is the hinge: until it passes, staffing and setup should not start. If the scanner says pre-gate readiness is 7 of 7 and A09 is missing, that is the recommendation - do not let a project drift past a complete baseline without a decision.
- A09 passed and the team is not staffed -> `a10-staffing`. It checks the prerequisites and drafts the request, points at the RM's process for the run itself, then reconciles the Resource Plan and P&L afterwards. Say plainly that the middle is not ours.
- A11 thin, or the project has no Drive folders / no brain -> `a11-project-setup`. Do not wait for its turn in the sequence: A11 builds the containers every earlier step needs somewhere to put things. If A01 has nowhere to file a brief, or A08 has no Sensitive folder for the P&L, run this first regardless of what the numbering suggests.

- A contract is signed and nobody has worked out what it commits us to -> `a03-contract-commitments`. Raise it unprompted when a signed contract or SOW turns up: it produces the Commitments Register and checks it against the scope, roadmap and economy. Its rule is absolute - contract text goes in a separate confidential container, never the project brain.
- Kick-off is coming, or has just happened -> `a12-a14-kickoff` (internal alignment, the deck, the follow-up).

### Artifact skills - not steps, and not in the A-sequence

These work at ANY point in a project's life, including long after initiation. They have no predecessor, so nothing arrives at them on its own - which means this router is one of the few places a PM will ever hear they exist. Offer them by name when the situation fits, not only when asked:

- `project-brain` - the project's NotebookLM notebook. Feed it, query it, or check whether it has gone stale. Raise it unprompted when the project has a brain that looks untouched, or when a PM asks a project question the brain should already answer. The common failure is a brain seeded once at A01 and abandoned, so "is your brain current" is a genuinely useful thing to offer on any running project.
- `risk-register` - the risk register and issue/blocker log. Raise it whenever a risk or blocker comes up outside initiation, which is most of the time: a PM should never have to re-run an initiation step to add one risk. It also has a review mode for "are my criticals still owned, has this gone stale".
- `prorep-card` - the weekly PROREP status: the eight-field comment and the eight PMO indicators, posted together, plus whether the card still tells the truth. This is the one with a CADENCE - it is owed every week until the project closes, so on any running project it is worth asking when the last status went in. Its review mode runs across every card the PM owns, which turns "which of mine are behind" into a one-question answer. The card's descriptive fields are A11's job, not this skill's.
- `correspondence-log` - the project's client email collected into one Doc the team can read and the brain can answer from, back over the history and forward from now on. The odd one out here: it answers to no step and no artifact, so nothing scores it and nobody will ever ask for it by name. Raise it when a PM is hunting their own inbox for what a client agreed, when the project's mail exists nowhere but one mailbox, or when a handover means somebody else now needs that trail. Be exact about what it is - it makes mail FINDABLE and it is not evidence of anything, because it holds a copy of the text and not the message.

On a project already in delivery, one of these three is more often the honest answer to "what should I do next" than any A-step is. Do not march a month-seven PM through A-block triage when what they actually need is a register update or this week's status.

Every A-step now has a skill. Three are deliberately partial and you should say so rather than overselling them: `a03-contract-commitments` does not do the agreed-versus-signed version comparison (that needs contracts and PMO leadership), `a10-staffing` does not run the staffing process, and `a11-project-setup` advises on chats and the tracker rather than acting (it does fill in the PROREP card's descriptive fields). Say so plainly when one of these is the right next move, then read that step's contract out of `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md` and work through its outputs and verification criteria with the PM by hand. Point at the relevant templates from the register. Do not invent a process and present it as ours.

Two things that are easy to miss and worth raising when they apply:
- A03, the contract review (page 5142544653). If a contract is signed and nobody compared the agreed version against the signed one, that is an open mandatory step. It sits between A02 and A04, is not in the overview table, and its comparison happens in a SEPARATE confidential notebook, never the project brain.
- A11 creates the containers - the Drive folders, the project brain, PROREP, the chats, the documentation space - that the earlier steps assume already exist. On a project where those are missing, doing A11 early is often the right call even though its number is high. Order is flexible; say so.

If several steps are thin, prefer an unfinished pre-gate step (A01-A08), because A09 is the one hard sequencing rule in the standard - after it the baseline is approved and setup begins. Otherwise ask the PM's preference.

One thing worth raising unprompted: if A10 or A11 work has already happened but A09 has not, the project is staffing and setting up without an approved baseline. The standard is explicit that no internal go means no team appointment and no setup. Say so plainly - it is not a filing gap, it is a governance one.

Respect skip-with-justification: if the PM wants to skip a step, capture the reason as a note. A thin step is justified-and-recorded, never a silent pass.

CHECKPOINT: "Suggested next: [step] because [reason]. Or pick any step from the map. What do you want to run?" Then hand off to the chosen skill.

Before handing off, put the loose ends in `<workspace>/pm-tasks.md` tagged with the project: the `possible` steps that need a human check, any unplaced file the PM could not identify, a money-bearing file sitting in the wrong folder, and any artifact the scan could not verify because a connector was missing. Those are exactly the things that get forgotten between sessions, and the router is the only place that sees them.

## Notes
- The scanner is a hint engine, not a judge. It tells the PM where to look; the PM confirms and decides.
- This skill does not itself produce A-step deliverables or push to the brain - it routes to the skills that do, each of which has its own gates.
- Re-run anytime ("where am I on X") to get a fresh state map as the project fills in - the readiness number climbing over time is the signal, same spirit as the A01 re-score loop.
