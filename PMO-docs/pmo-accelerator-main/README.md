# PM Copilot (Innowise PMO)

A copilot that helps a PM run the PMO Project Initiation standard with less manual work and more consistency. It drafts, checks, computes and automates; the PM judges, decides and sends. It never sends to a client or Sales on its own, and it gates every write to a shared or sensitive place.

**Alpha.** What changed in each build is in `CHANGELOG.txt` next to the zip. Every step of the standard has a skill, three artifact skills work outside the A-block, and five working skills answer to no step at all - the correspondence log, a guide to the standard itself, a voice pass for anything you send, a daily digest of your chats, and a wrap-up that closes a session into your files. This is deliberately not called 1.0 - a copilot that overstates what it can do is worse than one that does less.

If something behaves oddly, that is expected at this stage. The copilot keeps a `copilot-feedback.md` log for exactly this - tell it when it gets something wrong rather than working around it, and send the file back.

## Setting up

`SETUP.md` has the steps. Short version: install the plugin, install the three `.mcpb` extensions, add Atlassian in Claude's connector settings, quit Claude, reopen it, then say "set up my copilot" in the Code tab.

No scripts, no commands to paste, and nothing to install on your machine first. Each extension declares its own runtime and Claude supplies it, so there is no Python step and no client secret to chase - the OAuth credentials ride inside the extensions.

**Use the Code tab for setup, not Cowork.** One step needs it: NotebookLM has no public API, so it authenticates by driving a browser on your own machine, and Cowork's sandbox cannot reach your laptop. Everything else works on either surface.

If anything goes wrong, say "my copilot setup is broken" in Claude - copilot-setup diagnoses it and gives you the specific fix.

Two things to know before you hand this to anyone:

- Double-clicking a `.mcpb` does not work on Windows - the package declares no file associations, so Windows offers Notepad. The route that works is Settings, Extensions, Extension Developer, Install Extension, which sits behind a Developer Tools warning box.
- The NotebookLM sign-in expires every week or two. That is the only routine breakage in the whole setup and it is not a fault. A PM re-runs it from the Code tab in a few seconds, usually without typing anything. Tell them in advance, or they will read it as the copilot breaking.

## How a PM uses it

1. **`copilot-setup`**, once, in the Code tab. It runs steps 4 to 10 of the ten-step install in `SETUP.md`, and tells you which step you are on every time it stops. Probes your connectors and helps fix the ones that do not work, installs the copilot's rules and its copy of the PMO standard, drafts a profile of your portfolio, and starts your task list and the alpha feedback log. Getting the connectors green is step 7, not the end - if you stop there, stop deliberately, and say "continue my copilot setup" in a new chat when you come back.
2. Then, per project:
   - **`map-existing-project`** for any project that already exists in the real world but the copilot has never seen - whether you inherited it or have been running it yourself for months.
   - **`project-router`** for a brand new project, or one that has already been mapped. Scans what exists, scores readiness, routes you to the thinnest step.
3. From there, run the step skills it routes you to, reviewing at every checkpoint.

Real projects do not run A01 to A14 in order, and the standard says so explicitly. These are routers, not wizards.

**How the two routers fit together.** The split is about whether the project has been MAPPED, not about how you got it or how well you know it.

`map-existing-project` maps a project that already exists in the real world. Two kinds of PM land there and both belong: someone who inherited a project and does not know it, and someone who has run a project for months but has never used the copilot on it. The second is the more common case on day one, because every PM has a portfolio Claude knows nothing about. It sweeps every system, confirms gaps with you rather than assuming, offers to draft what is genuinely missing, and writes `source-register.md` and `takeover-brief.md` into the project folder.

`project-router` is for a brand new project, or one takeover has already mapped. It looks for those two files first and reads them rather than repeating the sweep.

The trap this avoids: if you point `project-router` at a project you have been running for six months, the folder is nearly empty (you never used Claude on it), the scan reports 2 of 13, and it would route you to A01 pre-sale handover on a project that has been delivering since spring. Both skills now guard against that - a near-empty scan on a live project means the material is elsewhere, not that the work was never done.

## The skills, in the order you would use them

Skills that produce a Standard A step's outputs carry the step code, so the list sorts into process
order and you can see at a glance which part of the standard a skill belongs to.

| Skill | What you get | Steps |
|---|---|---|
| `copilot-setup` | Connectors probed and repaired, always-on layer installed, your profile drafted, task list and feedback log started | - |
| `map-existing-project` | Source register, project-context, takeover brief, what needs attention now, artifact scorecard, drafts of what is missing | - |
| `project-router` | Where the project stands, and which skill to run next | - |
| `a01-presale-handover` | Handover brief, assumptions and commitments list, scored checklist as a Sheet others confirm line by line, source register, risk log, seeded project brain | A01 |
| `a02-a04-stakeholders-and-description` | Stakeholder Register with a decision-ownership table, the A03 contract checkpoint, Project Description | A02, A03 check, A04 |
| `a03-contract-commitments` | Commitments Register from the signed contract, four-bucket alignment check against the plan, and the operating parameters propagated to where you work | A03 part |
| `a05-a06-scope-and-risks` | Required Roles List, work-category sweep, Critical Scope with acceptance criteria, Risk Register with candidate traceability, Issue log, CR candidates | A05, A06 |
| `a07-a08-roadmap-and-economy` | Roadmap, milestones with owners and dates, role-by-month plan, options log, economy assumptions, gated write of planned HOURS into the economy file. Does not compute margin - that is yours with the RM | A07, A08 part |
| `a09-baseline-gate` | The go/no-go: a one-page leadership summary with the PM's readiness call and flags, reviewer routing, value classification, recorded decision | A09 |
| `a10-staffing` | Prerequisite and gate check, help with the position requirements the DM owns, the candidate acceptance checklist handed to you, then the confirmed data moved into your Resource Plan copy and the P&L | A10 |
| `a11-project-setup` | Containers early (Drive, sensitive storage, brain), then after staffing: PROREP filled in, Project Description updated, Communication Plan and Working Rules drafts, chat plan from the source page | A11 |
| `a12-a14-kickoff` | Internal alignment with the team feasibility call and Communication Plan review, the PMO kick-off deck filled slide by slide, client process topics, access list, invite, 24h follow-up | A12, A13, A14 |
| `standards-sync` | A refreshed copy of the standard, separating what changed from what we had wrong, plus four standing questions it answers each time | - |

Every step of the standard now has a skill, including **A03** - a real mandatory step that appears in
neither of the standard's own summary tables, which is why its name carries no clean number.

### Artifact skills - any time, not in the A-sequence

Three of the mandatory starting artifacts outlive initiation, so they get their own skills. These carry no
step code because they answer to no step: use them on a project in month seven as readily as in week
one, and the step skills call them rather than duplicating them.

| Skill | What you get | Artifact |
|---|---|---|
| `project-brain` | Feed the project notebook, query it, or check whether it has gone stale | 1 |
| `risk-register` | Add or close one risk or blocker without re-running initiation, plus a review of coverage and staleness | 8 |
| `prorep-card` | The weekly eight-field status and eight PMO indicators posted to the card together, plus a portfolio-wide review of which of your cards are behind | 17 |

`prorep-card` is the one with a cadence. Every other skill here runs when something happens; that one
is owed every week until the project closes, which is why its review mode reads across every card you
own rather than one at a time. It deliberately has no write mode - the card comes from Sales, and its
descriptive fields are filled at A11.

Both it and `a11-project-setup` read `references/prorep-fields.md`, a live field-by-field map of the
card built from a real read of all 519 of its fields. That file exists because the card is a minefield:
English and Russian near-duplicates of the same field, two different project-stage fields with
different option sets, one field that would accept a money figure, and three separate field sets that
all get called "metrics" of which only one is the PM's weekly job.

Two deterministic scripts back the judgement calls: `score_handover.py` (the A01 metrics, re-run four times on a live project) and `scan_initiation_state.py` (the state and artifact scanner). In Cowork they run in the sandbox, which has Python built in. In the Code tab they run on the PM's own machine, and there Python is not guaranteed. The three extensions keep their own runtime inside Claude, so nothing has to be installed for THEM to work. Setup does still put two things on the laptop, both at step 7 and both for the NotebookLM sign-in: Git, which the Code tab itself requires, and `uv`, which Claude Code installs from Astral. Neither is Python - `uv` brings its own. The skills try `uv` first, fall back to whatever Python is there, and if there is none they fall back to a hand read and say so rather than passing it off as the deterministic number.

### Working skills - no step, no artifact

Some of a PM's real work answers to nothing in the standard. Where that work is recurring, shaped the
same way every time, and has a house rule that decides whether it is safe, it is worth a skill. Where
it does not, it is ordinary help and needs no apparatus.

| Skill | What you get |
|---|---|
| `correspondence-log` | The project's client mail collected into one Doc the team can read and the project notebook can answer from, back over the history and forward from now on |
| `pmo-guide` | An answer to a process question - "who approves", "what does B03 require", "is this mandatory" - from the live Confluence page, with the page ID cited. Any block of the standard, A to G. Read-only |
| `pm-voice` | Anything you will send - a client reply, a weekly status, a kick-off follow-up, an escalation - at the length the channel expects and without the English and Russian AI tells |
| `daily-digest` | One digest a day of your Chat spaces, mail and meeting notes - what needs you, what was decided, new ideas and use cases, risks - on a schedule, delivered to one private place you choose |
| `wrap-up` | Before a chat closes, the session's new tasks on your list, what stays true in each project's `project-context.md`, and a short resume note in the project folder - so the next chat starts where this one stopped, not from you explaining it again |

`correspondence-log` is the first of these, and its boundary is the important part. It makes a
project's mail FINDABLE - one Doc per project instead of one person's inbox, with a money rule applied
per message so the Doc is safe to put in the project brain. It is **not evidence**: it holds a copy of
the text, not the message, so it carries no signature, no authentication verdict and no delivery
headers. It is how a PM finds which message to go and get, not proof that the message said what it
said. The skill says so itself, twice, for the same reason it is said here.

Its Track 2 counterpart is a Workspace Studio flow, so a PM without Claude gets the ongoing capture.
Studio has no way to search mail, though, so only the skill can collect what came before today.

`pmo-guide` exists because the question "how do we do X here" was being answered from memory or from the bundled pack, and the pack drifts - the initiation checklist went from 21 to 23 rows in a single day. So the pack is the index, the live page is the answer, and the Superbrain notebook is background. It explains and cites; it does not do the work, and it offers the skill that does.

`pm-voice` exists because copilot drafts fail on length before they fail on vocabulary. It sets the size by channel first - a chat reply is a sentence or two, a client email two to four short paragraphs - then scans for AI tells in English and Russian against how PMO chat spaces actually read. If you have a voice skill of your own, that one wins. If setup saved a few of your real messages, pm-voice follows your habits over its defaults. Other skills hand their outbound text to it.

`daily-digest` exists because a PM in a hundred Chat spaces skims them all and still misses the one decision that mattered. Setup agrees what to look for (a default list you reorder, drop from or add a focus to), where it lands (a private Chat space, email to yourself, or just the scheduled run), and which spaces to skip, then runs one digest live and asks what time to schedule it. It reads meeting notes from Bluedot if you have it, or asks where yours end up. The digest goes to that one place and nowhere else, and it only runs while Claude is open.

`wrap-up` exists because a new chat starts blank. What a session worked out - a task, a decision, who said what, where the work stopped - is gone when it closes unless it is in a file. It finds your task list (or asks where you keep one), updates `project-context.md`, writes `resume.md` next to the project, adds anything that went wrong to `copilot-feedback.md`, and offers the project brain what is new. One route, no modes. If you have a wrap-up routine of your own, that one wins. It writes only the copilot's local files - never Jira, PROREP, a notebook or a message.

A desktop-access connector is deliberately NOT bundled. Everything the copilot needs lives in Drive, Confluence, Jira, Chat, NotebookLM and Gmail, and a PM working in the Code tab already has their own machine. It stays available as an opt-in escape hatch on Windows for the occasional Cowork case where the sandbox cannot reach a local file - see the optional section in SETUP.md, which also explains why pairing a full shell with `map-existing-project` (a skill that reads a great deal of material in one pass) deserves a deliberate decision.

## The reference pack

`references/` is what makes this portable rather than one person's rig. It is a dated CACHE of the PMO standard; Confluence is the source of truth, and `standards-sync` refreshes it.

Setup copies the whole pack into `<workspace>/pm-copilot-references/`, and that copy is the one that gets used. It has to be there: the always-on rules file loads outside any plugin context, so a path into the plugin folder does not resolve from it. Without the workspace copy the copilot would fall back to reciting the standard from memory, which is the single failure the pack exists to prevent.

- `standard-a-contract.md` - every step's outputs, verification criteria, control metrics and page ID.
- `initiation-artifacts-checklist.md` - the 21 mandatory artifacts and where each is filed.
- `template-register.md` - which template serves which step, where it lives, and which mandatory artifacts have no template at all.
- `pmo-conventions.md` - Drive layout, chat taxonomy, the two brains, filing, editing gotchas.
`prorep-fields.md` - the PROREP card field by field, from a live read of all 519 of them: what is filled in practice, where each value comes from, the money boundary, and the three different field sets that all get called "metrics".
- `pl-structure.md` - how our economy files are built and how to write to one without breaking it.
- `pm-profile-template.md` - the shape of a PM's own profile, filled in during setup.
- `instructions-layers.md` - which of the four always-on files anything belongs in, and what a PM's own instructions commonly lack.

## Coverage against the standard

Every step A01 through A14 has a skill, plus A03. Standards B to G have no step skills, but they are not uncovered: `pmo-guide` answers from them with the live page cited, and the artifact skills work inside them.

**A03 (`a03-contract-commitments`) is scoped to the PM's actual job.** The contract preparation group drafts the contract and Legal signs it; the PM's part is working out what the signed document commits the project to and checking that against what the project has planned. So the skill produces a Commitments Register - delivery obligations, client obligations, acceptance rules, reporting duties, constraints - and sorts every item into aligned / in-the-contract-but-not-our-plan / in-our-plan-but-not-contracted / contradictory. It deliberately does NOT do the agreed-versus-signed version comparison the standard also describes; that needs contract access and PMO leadership. And it does not give legal advice - anything touching liability, IP or termination is named and routed to contracts, not answered.

Contract text goes in a separate confidential container, never the project brain. The Commitments Register can live with the project documents, because it is a summary in delivery terms rather than the document itself.

**A10 (`a10-staffing`) is deliberately a pair of bookends.** The staffing run itself is the Resource Manager's process, in the Staffing Master, not here. The skill checks the three prerequisites the instruction requires up front, drafts the request from the Required Roles List, points at the Confluence instruction for the run, and then does the part that actually slips: the candidate vetting record and reconciling the Resource Plan and P&L with confirmed people, reusing the same column-confirmation and control-total checks as A08. Candidate CVs and personal data never enter the project brain.

**A09 (`a09-baseline-gate`) never approves anything.** It assembles the package, sharpens the value classification, drafts the internal ask and the client confirmation, and records what real stakeholders decided - using the standard's fixed five-outcome vocabulary. A gate the copilot can pass on its own is not a gate. It also splits the two audiences properly: the internal package may discuss economy, the client-facing one carries no margin, rate or cost figure at all.

**A11 (`a11-project-setup`) is deliberately partial**, and the boundaries are worth knowing before you run it:

- **Creates**, with your approval: the Drive folder structure, and the NotebookLM project brain.
- **Advises only**: project chats (which ones, who belongs, what to pin - it never creates a chat or invites anyone) and the tracker. PROREP is different now: A11 fills the card's descriptive fields on approval, working from a field map, and ties its billable-hours figure back to your plan. It does not create the card - that comes from Sales at Closed-Won - and it does not touch the weekly metrics, which are `prorep-card`'s job.
- **Drafts**, gated: the Communication Plan and the Team Working Rules.
- **Optional**: a Confluence documentation space. Producing Google Docs into the brain satisfies the requirement for now, so its absence is not treated as a blocker.

It never renames, moves or deletes anything that already exists. On a project with a non-standard structure it maps the standard onto what is there and only creates what is genuinely missing - two competing structures being worse than one untidy one.

One real tooling limit: on shared drives the connector can create folders but cannot make shortcuts, and the Sensitive and Presale Final entries are normally shortcuts. The skill creates what it can and hands you an explicit list of shortcuts to add by hand, rather than quietly creating real folders where shortcuts belong.

## Two instruction files, and who owns which

Setup installs `.claude/rules/pm-copilot-baseline.md` - how the copilot behaves, the same for every PM, shipped with the plugin and replaced whenever the plugin updates. Nothing you wrote gets edited to make room for it.

Next to it goes `.claude/rules/pm-profile.md`, and that one is yours. Who you are, your portfolio with the aliases each project actually goes by, where things live, your lead and RM, and whether you want the copilot guided or express. Setup drafts it from your Drive and Jira rather than handing you a form, then you correct it. The copilot offers to add to it and never rewrites it, and a plugin update leaves it alone.

The aliases line earns its keep on its own. A sweep that knows a project by one of its three names finds about a third of the material.

Setup also offers a short pointer block for your global instructions - the layer that loads in every workspace and every project. It is a safety net: if you open a single project folder as its own space rather than your whole portfolio, the two rules files above do not load, and without the pointer the copilot has no idea any of this exists. If you always work from the portfolio root, you can skip it.

In the Code tab, setup writes that block for you. In Cowork it hands you the text to paste into your personal preferences instead, because Cowork's global instructions are managed by the app rather than kept in a file anything can write to.

One maintenance action to know about. A new plugin version brings new skills immediately, but the workspace copies of the baseline and the reference pack only move when you re-run "set up my copilot". It is safe to repeat and it takes a minute.

## What the copilot writes down

Four more plain markdown files, all local, none of them shared anywhere. The copilot reads them before it starts work so you are not answering the same questions, or re-deriving the same conclusions, every session.

`pm-tasks.md` is one task list across your whole portfolio, project-tagged. It exists mainly because every skill throws off actions - gaps to close with Sales, an artifact to file, a client to chase - and without somewhere to put them they vanish when the session ends. If you already keep a task file, the copilot adopts it rather than starting a rival.

`pm-copilot-setup.md` in your workspace records which connectors were confirmed working, so a skill can tell you up front that part of it will be blind instead of failing halfway through.

`project-context.md` in each project folder is what the copilot knows about that project - names and aliases, where things live, who the people are, what was decided and by whom, which step outputs exist, what is still open. Money and contract text stay out of it.

`copilot-feedback.md` in your workspace is the alpha log, and it is the point of the alpha. The copilot writes an entry whenever it could not do something, got a fact about Innowise wrong, or you had to correct it - and you can say "log this" at any point to force one. Once a session, after real work, it will ask you one question about how that went. Send the file to whoever gave you the copilot. The corrections are the most useful entries in it, so there is no need to be polite.

## Work the standard has no opinion about

Most of what this bundle contains is PMO process. Plenty of a PM's week is not - the client update, the chase email, the agenda, sanity-checking someone's estimate. For those the copilot just helps, without invoking the standard or apologising for having no skill. It keeps the parts that always apply: it will not send anything for you, money stays where it belongs, and it will say when it is guessing about how Innowise does something rather than posing.

It also logs the gap, so a request that keeps coming back can turn into a skill later.

## Design principles

**Steps are the contract; skills are clusters.** The standard's steps each define outputs, verification criteria and a control metric. One skill may produce several steps' outputs when they share source material. The scanner still tracks readiness per step.

**Two scores, two questions.** The A-step map says what work is left. The 21-artifact map says what the PMO will ask you for. On an inherited project the second is the useful one, because it does not assume the project started at A01.

**Governance.** Every skill works in stages and stops to show what it found. Every write to the brain, a shared Sheet, a P&L, Confluence or Jira is gated. Money and contract text never enter the project brain. The org Superbrain and the per-project brain stay separate.

These gates are behavioural - instructions the model follows, not code that enforces them. Hooks would make them structural and are on the roadmap. Until then the honest description is "the copilot is built to stop and ask", not "the copilot cannot write without permission".

## Known gaps

- The three artifact skills - `project-brain`, `risk-register`, `prorep-card` - are called by INSTRUCTION, not by any import mechanism. A step skill invokes them in prose, so the handoff is only as reliable as its wording. That is the part to watch when a step skill hands off. `correspondence-log` hands to `project-brain` the same way and inherits the same weakness.
- Only A01 has a deterministic scorer. Every other control metric is estimated in prose, with its basis shown.
- The three local files and the alpha feedback loop are new in this version and have not been exercised across sessions yet. If `project-context.md` turns out to be another file that goes stale, say so - the point of it is that you should never have to re-explain your own project.
- No SKILLS cover Standards B through F - monthly and milestone cycles, weekly and sprint management, daily management, closure. The standards themselves are in the PMO Superbrain notebook, so the copilot can read the requirements out and work through them with you; it just has no guided flow for them.
- No completeness-checker subagent and no enforcement hooks.
- `a07-a08-roadmap-and-economy` can write to a live P&L. Treat the write with suspicion, work on a copy tab, and check the control totals.
- The takeover sweep degrades badly without the Google connectors. It says so rather than failing quietly.
- The extension bundles have not been installed on a clean machine end to end, and not at all on a Mac. Everything about the first launch - Claude fetching its own runtime, the network egress that needs, and how it fails on a locked-down laptop - is reasoned from how the mechanism works rather than watched happening. The first PM through is the test; ask them to report anything odd rather than working around it.
- Setup now depends on the Code tab for one step, which puts a developer-facing surface on the critical path for a non-technical audience. The NotebookLM sign-in is the only thing that needs it, and only because NotebookLM has no API to authenticate against properly.
- Several mandatory PMO artifacts have no company template - Onboarding / Team Working Rules is mandatory with a `[Link TBD]` in the standard itself. `template-register.md` lists all ten known gaps.

## Distribution

Opt-in, never admin-forced. The alpha shares the bundle manually. The end state is an opt-in org catalog entry a PM can choose to install, updated from one source.
