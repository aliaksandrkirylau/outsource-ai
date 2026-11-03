---
type: reference
tags: [pm-copilot, plugin, design-log, pmo]
moved_from: auto-memory project_pm_copilot_plugin
moved_on: 2026-09-17
---

# PM Copilot plugin - design and build log

> Moved out of auto-memory on 2026-09-17. This is a document, not a single fact, so it lives with
> the work rather than in the memory index. The memory file is now a pointer.

The PM Copilot moved from "one A01 skill" to a plugin-shaped bundle covering the front door of Standard A (Project Initiation). Built 2026-07-22 as the "beyond A01" work ahead of the PM intro workshop (workshop = 2026-07-22 afternoon; deck is a separate session). Bundle lives at `pm-copilot/source/` and is packaged as `pm-copilot/dist/pm-copilot.plugin`. Design doc: `pm-copilot/design/a-initiation-final-setup.md`.

KEY ARCHITECTURE DECISION (Anton 2026-07-22): **steps = contract, skills = clusters.** The 13 A-steps (A01-A13) stay the CONTRACT - each defines outputs + verification criteria + a control metric, tracked per step by the state scanner and the checkers. But a single SKILL may produce one OR several steps' outputs when they share source material. This supersedes the "~13 atomic step-skills" strawman in [[copilot-contents-map]]. Grounded in how Alchemy actually ran - several steps produced in one distillation pass, out of order, because the harvested material supported it. Anton raised the doubt ("is each A step actually a skill?"); the Alchemy evidence confirmed his instinct.

**Front door = router, not wizard.** project-init detects what already exists, scores readiness, and routes to the thinnest step; every step is also directly invokable (menu fallback). Router chosen because real projects run steps out of order (the standard says order is flexible; Alchemy did A04-A07 before A02-A03).

Built this session (verified): workspace-init (first-run setup, installs `rules/copilot-baseline.md` into the workspace, connector + health check); project-init (router SKILL + `scripts/scan_initiation_state.py` - deterministic A01-A13 output detector by filename/keyword, scores coverage + pre-A08-gate readiness); context-pack (A02 stakeholders/comms + A03 description worked example, grounded in the real Alchemy registers); validation-pack (A04 advisor-first scope/estimate/economy realism + A05 risk register + issue/blocker log, grounded in the Alchemy A04/A05); a01-presale-handover included from the existing built skill; plugin.json manifest + README. Bundle v0.2.0, 5 skills, 27 files. Scanner verified on Alchemy (85.7% pre-gate; correctly flags A07/economy "missing locally" since money lives in the sensitive Sheet), fresh project (routes A01), A01-only (routes A02/context-pack).

Clustered skill list (the build unit): front door = workspace-init, project-init; then A01 handover (standalone), context-pack (A02+A03), validation-pack (A04+A05), plan-and-economy (A06+A07, reuse fair-hours + pl tooling), baseline-gate (A08), staffing (A09, reuse Staffing Master + fair-hours), system-setup (A10, reuse jira-import/confluence), kickoff-pack (A11+A12+A13). ~7 skills over 13 steps + 2 front-door. BUILT clusters so far: context-pack (A02+A03) + validation-pack (A04+A05) + plan-and-economy (A06+A07, advisor-first forks + hard P&L write gate, reuses fair-hours + pl tooling, encodes the LotberG/Alchemy P&L-write lessons). Bundle v0.3.0, 6 skills, 32 files. ROADMAP (designed, not built): baseline-gate (A08), staffing (A09), system-setup (A10), kickoff-pack (A11-A13); completeness-checker subagent; P&L write-gate + brain-sensitivity hooks; full org-catalog plugin install (currently a manual-share bundle).

Distribution: opt-in, never admin-forced - manual-share for the pilot, opt-in org catalog as the end state.

Governance baked in (from [[feedback_copilot_checkpoints_no_autowrite]]): every skill staged with checkpoints; every write to brain/Sheet/P&L/Jira gated; no money in the project brain; Superbrain (org standards) vs project brain kept separate. Shipped in `rules/copilot-baseline.md`.

Workshop demo plan (tested 2026-07-22 by Anton, works well): show the START of A01 in action (handover kicking off + gathering data), kept short + safe, then focus on the Alchemy results for outcomes. Bundle installed + skills trigger correctly (they appear as pm-copilot:* skills). Deck = narrative + slide-by-slide brief BUILT 2026-07-27 at [[pm-copilot-workshop-deck-brief]] (pm-copilot/decks/), REPOSITIONED copilot-first: the deck is about the Copilot ITSELF (regular PMs do not yet know what it is); initiation is the near-ready proof-point at the end, not the subject. ~13 slides, RU narration/headlines + EN tech terms (locked rules), reuses 5 built slides from pm-copilot/decks/built/ + the claude-101 primer, slide 7 = "shippable plugin that briefs the genius-intern". Ready for Claude Design. OPEN before the workshop: pick + prep the sanitized sample project for the live A01 demo.

## ALPHA HARDENING, 2026-07-27 - bundle now v0.4.0 (8 skills, 47 files)

Deep review found v0.3.0 was a skeleton with one working muscle: 1 of 6 skills ever run, three skills reading Anton's vault paths (`automations/confluence/superbrain/...`, `automations/fair-hours-redistribution`), no `.mcp.json`, no setup path, every "HARD GATE" prose-only. Review doc: `pm-copilot/design/pm-copilot-alpha-readiness-review.md`. Lesson recorded as [[feedback_portability_before_breadth]].

Anton's forks: bundled reference pack + sync skill (not live Confluence, not Superbrain); build portability + takeover first; KEEP the P&L write but document the file structure so Claude can help the PM write after planning; self-service install script with workspace-init as the guided fallback.

Built: `references/` pack - standard-a-contract.md (all steps: outputs, verification criteria, control metrics, page IDs, numbering caveat), initiation-artifacts-checklist.md (the 21), template-register.md (~35 templates mapped to steps + 10 real PMO template gaps such as Onboarding/Working Rules being mandatory with a `[Link TBD]`), pmo-conventions.md, pl-structure.md (role-block offsets, month codes, overhead model, the full write sequence). New skills `standards-sync` and `project-takeover`. Scanner v2 with content sniffing + 21-artifact scoring + a money-in-the-common-folder policy flag (Tensi+ went 0 to detecting its xlsx registers; InamuH A01 evidence 1 to 4 files). Setup layer: `.mcp.json`, `scripts/setup/install-mcp-servers.ps1` with every known gotcha baked in, `SETUP.md`, workspace-init v2 that probes connectors for real and guides repair. Corrected the A07 control metric (was "margin vs target", is Resource-to-Economy Coverage 100%) and added the missing A03 metrics.

Two discoveries that outlive this build, see [[reference_standard_a_numbering_trap]]: a hidden 14th step (contract review, page 5142544653, comparison must happen in a SEPARATE confidential notebook) causing an off-by-one in every detail page title, and the new 21-artifact Project Initiation Artifacts Checklist (page 5166432427) which is now the copilot's definition of done and the spine of the takeover flow.

## COVERAGE COMPLETE, 2026-07-27 end of session - v0.11.0, 13 skills, 61 files

Every Standard A step A01-A13 now has a skill, plus A02.5. Built this session: `a08-baseline-gate`, `a09-staffing`, `a10-project-setup`, `a11-a13-kickoff`, `a02b-contract-commitments`, `map-existing-project`, `standards-sync`. Plus a macOS installer, and `skills-to-upload/validate-plugin.py` which enforces the plugin's length limits pre-package.

SKILLS RENAMED for PM readability (Anton: "what is context-pack?"). Step-producing skills carry their A-code so the list sorts into PROCESS order: a01-presale-handover, a02-a03-stakeholders-and-description, a02b-contract-commitments, a04-a05-scope-and-risks, a06-a07-roadmap-and-economy, a08-baseline-gate, a09-staffing, a10-project-setup, a11-a13-kickoff. Non-step skills: copilot-setup, map-existing-project, project-router, standards-sync.

Deliberately partial, and each says so rather than overselling: `a09-staffing` does not run the staffing process (RM's, in the Staffing Master) - it checks prerequisites, drafts the request, then reconciles the Resource Plan and P&L after. `a10-project-setup` creates Drive folders and the brain but only ADVISES on chats and PROREP, and never renames/moves/deletes anything existing. `a02b-contract-commitments` does not do the agreed-vs-signed version comparison and gives no legal advice. `a08-baseline-gate` never approves anything - it records what real stakeholders decided.

VERSION HELD AT 0.11.0, NOT 1.0 - full coverage is not maturity. **12 of 13 skills have never been run on a real project.** That is the dominant remaining risk and the README leads with the number.

## RULES PASS, 2026-07-28 - v0.12.0

Items 1 and 3 of Anton's list, done together. `rules/copilot-baseline.md` rewritten after being read whole for the first time. Four decisions:

**Per-project context file.** New `project-context.md`, fixed name, one per project folder. Aliases, where things live, people, decisions and who made them, which step outputs exist, open questions, skip-with-justification. Read at the start of any project work, appended at the end of a stage that establishes a fact, and NOT gated (it is the copilot's own local note - gating it would kill it). The gap it fixes: the only persistent state was `pm-copilot-setup.md` plus takeover's `source-register.md`/`takeover-brief.md`, so on a NEW project session 2 re-asked the project name, client, folder and aliases that A01 had already established.

**No-instruction behaviour = three cases, not two.** (1) PMO step or mandatory artifact with a skill -> run it. (2) PMO step or artifact with no skill -> read the step contract from the reference pack and work it by hand. (3) Ordinary PM work with nothing in the standard behind it -> just help, silently: no mention of the standard, no apology for having no skill. Distinguish 2 from 3 by EVIDENCE (does the 21-artifact checklist or a step contract name the thing?), which is the same principle as [[feedback_route_on_evidence_not_provenance]]. The single old rule misfired: "draft my weekly update" got "here is what the standard requires", which reads as a paperwork robot.

**Alpha feedback log - Anton's addition, and the important one.** `copilot-feedback.md` in the workspace, created by copilot-setup and explained to the PM up front. The copilot logs no-skill/no-template gaps, the PM correcting it substantively (flagged as the most valuable type, "do not soften it and do not leave it out because it is unflattering"), Innowise facts it got wrong, blocked steps, abandoned skills. "log this" from the PM forces an entry. Once per session after real work it asks one question about how that ran. Plugin version in the header so a report ties to a build; projects by name only, no client material/money/PII. This is the mechanism that substitutes for Anton being in the room during alpha - PMs send the file back.

**Language:** answer in whatever language the PM writes in; step codes, artifact names and filenames stay English.

Also fixed: missing opening frame (what it is / is not, plus precedence - the PM's own workspace instructions WIN over the baseline, and the copilot should name the conflict); the setup-state paragraph was misfiled under "where to read the reference pack from"; A02.5 was defined two ways in one bundle (baseline said version comparison, `a02b` says commitments-and-alignment - baseline now matches the skill); README carried two self-contradicting stale claims ("six of thirteen steps have no skill", "there is no skill for A02.5"); `map-existing-project` still told PMs the copilot only covered A01-A07.

Propagated into `copilot-setup` (Stage 4 now writes both workspace files), `project-router` (its vague "local conventions note" is now `project-context.md` by name) and `map-existing-project`. **The ten step skills were NOT touched - none of them yet reads or appends `project-context.md`.** Do that during the one-by-one skill review.

## PM PROFILE LAYER, 2026-07-28 - v0.13.0

Anton spotted the missing layer: the bundle had org-wide behaviour and per-project state but nothing per-PERSON. Now three layers, and the axis that matters is WHAT SURVIVES A PLUGIN UPDATE:

1. `.claude/rules/pm-copilot-baseline.md` - shipped, org-wide, REPLACED on update. Copilot owns it.
2. `.claude/rules/pm-profile.md` - the PM's own. Never rewritten by the copilot, untouched by an update.
3. `<project>/project-context.md` - per project, copilot-maintained.

VERIFIED PLATFORM FACT that drove the design (checked against Claude Code docs, I had initially doubted it): **every `.md` in `.claude/rules/` IS auto-loaded, at both project and `~/.claude/` level, alongside CLAUDE.md.** And a CLAUDE.md at a PLUGIN root is explicitly NOT loaded as context - so "a plugin has no always-on slot" is correct. Consequence: install the baseline as a separate rules file, never merged into the PM's CLAUDE.md. Additive, nothing of theirs edited, and deleting one file uninstalls cleanly (a merged section does not). Docs also say CLAUDE.md discovery walks UP to repo root, which RECONCILES with the City-planner finding in [[reference_cowork_context_inheritance]]: in Cowork the mounted folder IS the root, so there is nothing above it to walk to. The workspace-shape question at setup Stage 2 therefore still has to be answered, not assumed.

Built: `references/pm-profile-template.md` + copilot-setup Stage 3b. Minimal by choice - me / how I want the copilot to work (guided vs express, language, voice pointer) / portfolio table with ALIASES, Drive folder, Jira key, chats, brain / where things live / my people / "what the copilot has learned about working with me" which grows. Lessons and escalation map deliberately left to grow from real use.

DESIGN CALL worth reusing: **draft, do not interview.** Stage 3b lists the projects folder, searches Drive, lists Jira projects and Chat spaces, fills what it finds, then has the PM correct it. "A filled draft with three wrong rows gets fixed in one message; a blank form gets abandoned." Only aliases, mode, language and lead/RM are asked outright, because no sweep can infer them. Aliases are the payoff and are wired into `project-router` and `map-existing-project` Stage 0 - a sweep knowing 1 of a project's 3 names finds a third of the material.

Setup Stage 3 also now PROPOSES improvements to the PM's existing CLAUDE.md (Anton: "essential to propose to PM to update and add our specific instructions") - shown as before-and-after, never applied, capped at 2-3: missing plain-ASCII rule on a Windows workspace, stale connected-tools list, a rule that fights the write gates, a rule broad enough to fire on every message. "Setup is not a CLAUDE.md audit."

`project-context.md` enforcement also upgraded from "offer to append" to READ FIRST / WRITE AT EVERY CHECKPOINT / CORRECT IN PLACE. The enforcement mechanism is that the checkpoint line SHOWS what was logged - a PM who has been seeing it will notice when it stops. Behavioural like every other gate, but visible.

## OPERATING DOCTRINE, 2026-07-28 - v0.15.0

Anton's read: the baseline was all governance (gates, staging, sensitivity, posture) and said nothing about how to OPERATE - that a process exists and should be steered toward, that the copilot itself should be heavily used, that the brain is working memory. Three sections added AHEAD of the governance:

- **What we are working with** - Standard A named as the frame (13 steps + contract step, 21 artifacts = definition of done, the PM accountable for the artifacts whether or not steps ran in order), then the three process sources in authority order: bundled pack (contract, exact, versioned) -> Confluence (live, by page ID) -> Superbrain (narrative, "how do we usually").
- **Reach for a skill, do not freehand** - name the skill and run it, because a hand-rolled step output silently drops the verification criteria, the control metric, the template AND the gates. Steer to the house guideline where one exists; slowing a PM for one message beats helping them build a parallel process.
- **The project brain is working memory, not a filing cabinet** - READ constantly, no permission, especially before saying "I do not know". FEED BY DEFAULT: propose unprompted whenever anything new is produced or found, because a brain a month behind its Drive folder stops being worth querying, which is how the artifact quietly dies. The GATE IS UNCHANGED (inventory + hold-out + explicit yes, even express) - what flipped is the disposition, who initiates, not who decides.

**Superbrain ID confirmed and hardcoded** - see [[reference_pmo_superbrain]]. It carries Standards A-F, which corrected a real bundle claim: "no skills for the B, C, D blocks" read as "we have nothing on delivery/closure". Now: **"there is no skill for this" is never the same thing as "we have nothing on this."**

**`references/instructions-layers.md`** - new, and the answer to Anton's "should we suggest editing CLAUDE.md". Four always-on files, each with owner + survives-update + what-belongs, plus a ROUTING RULE: copilot/PMO behaviour -> baseline (not the PM's to edit; a change request is a feedback-log entry); facts about the PM -> profile; general preferences that would outlive an uninstall -> their own CLAUDE.md; per-project facts -> project-context.md, not an instruction file at all. Setup Stage 3 analyses their existing instructions against it and proposes the gaps, ROUTED, as before-and-after, never applied without a yes, capped at 2-3 ("setup is not a CLAUDE.md audit"). Explicit anti-pattern: never propose copying the baseline into their CLAUDE.md - a second copy goes stale on the next update.

Setup Stage 6 now HANDS THE FILES OVER rather than listing them: which is ours vs theirs, that editing the baseline is pointless because updates replace it, and the two habits that keep it alive (tell the copilot when the profile is wrong; expect the context line at every checkpoint).

Baseline is 169 lines always-on - treat that as the ceiling; anything further goes in the pack and is read on demand.

## ALL 13 SKILLS REVIEWED, 2026-07-28 - v0.33.0

Anton's format, and it worked: "you review the skill, tell me what it does and how it works, what it points to, and if you have anything to suggest. I review and give feedback - we make changes based on that." One skill per pass. Twelve of thirteen changed.

Three skills were RESCOPED on his calls, not just fixed - each time because the skill claimed capability it did not have:
- **a06-a07** was pretending to calculate the economy. Anton: "How stage 2 would actually calculate the economy? it does not have information about that." On a new project there are no rates, no salaries, no overhead model. Now: build the plan, fill the staffing tab, hand the economy to the PM + RM, make sure the classification comes BACK for A08. Order matters and I had it backwards - the economy cannot be judged outside the P&L file, so filling it is the PREREQUISITE, not a hand-off courtesy. Also: fill BOTH paid and worked rows, paid=worked by DEFAULT with the absorbed-DM exception, billable total ties to plan+contract.
- **a08** was the wrong artifact for its audience - nine areas with per-area decision asks. Anton: "Leadership will not go through everything, they need a summary and red\green flags." Now a one-pager whose centre is **the PM's own honest readiness call**, which did not exist before. P&L never linked, only "posted in the Economy chat", and the copilot asks the PM to confirm it actually is.
- **a09** guides the PM OUT of the copilot. Requirements are the DM's content (PM asks the DM), so the copilot's default mode is CHECKING them against the plan and P&L grades. The vetting checklist is HANDED OVER, not applied - the copilot never sees a CV. Data move only on request, asking for the P&L tab and the link to the Resource Plan copy the PM made.

**Ships-a-lie findings, i.e. the pack was wrong not just thin:** a fabricated chat type ("Project / delivery") that exists nowhere in Confluence while the real 8th chat (Staffing) was missing; a11-a13 referencing an `output-shapes.md` that did not exist; a10 omitting "Project Description created/updated" which is a MANDATORY A10 output; A08 quoting a readiness fraction the scanner systematically under-reports because A07 is never in the project folder.

**Verified against live sources rather than the cache, which is where the value was:** the chat page (3006398548) gave the private-by-default rule, the pre-sale-to-Common RENAME convention, bot-created Strategy/Accounting, and the real pin lists. PROREP gave the Epic + child-issue-type structure. The kick-off template gave 12 real slides, an agenda differing from the content guide, and two concrete rules we only had abstractly - **70%/85% cap notification** and the FP CR workflow.

Cross-cutting rules added to the baseline this session: reuse-before-create (check project-context output list -> folder -> Drive/Confluence before drafting anything new); pm-tasks.md as the destination for skill output; three-case no-instruction behaviour; answer in the PM's language.

NEXT: **Alpha test 2026-07-29** - a PM installs the package himself and runs the copilot on his NEW project, so the path is `project-router` -> `a01-presale-handover`, not the takeover sweep. Also outstanding: the BASELINE TRIM (200+ lines always-on, deferred every version this session), and the four standing questions now encoded in standards-sync (14-step renumber / real v2 checklist / the A07 named-people line / what "the readiness review" is).

Lessons recorded separately: [[feedback_route_on_evidence_not_provenance]], [[feedback_verify_limits_dont_assert]], [[feedback_portability_before_breadth]], [[reference_standard_a_numbering_trap]].

## INSTALL FLOW REBUILT, 2026-07-28 - v0.34.0, 40 files

The alpha test found the real blocker before any skill got a chance to run: the test PM could not get through onboarding. Anton: "it's explaining too hard for pm... regular PM cant pass the onboarding flow now with all the closing and scripts." A 20-minute flow with a Python install, a tray-quit, an execution-policy line, a zip rename and six pasted PowerShell lines is not a flow a non-technical PM completes.

Anton's four calls: embed the secret; full auto where possible (though "we can still ask to install python or make a clear instruction for it"); try the double-click file "but have a backup"; cover both platforms, "though we were testing on Mac" - which makes the never-run-on-hardware Mac script the LIVE path.

**Two prerequisites deleted rather than documented better.**

1. The zip dance existed to work around an asserted limit that was false - see [[reference_plugin_root_dead_path]]. An installed plugin IS fully unpacked on disk, `scripts/` included, and the skill can just resolve the path. The false claim had been written into the skill as an instruction NOT to look, which is what made it survive.
2. The Python prerequisite dissolves into `uv`: the standalone installer needs no Python and no admin, and `uv tool install --python 3.12` makes uv fetch its own CPython. Bonus - this fixes a latent failure nobody had hit: `notebooklm-mcp-cli` requires >=3.11, so on a 3.10 machine the resolution was flatly unsatisfiable (reproduced in the sandbox). pip is gone from both scripts.

**The delivery pattern worth reusing elsewhere:** Claude resolves the bundled installer, copies four files into `<workspace>/pm-copilot-setup/` (both installers, `client-secret.txt`, the platform launcher), and the PM double-clicks `Set up PM Copilot.cmd` / `.command`. Launchers find the installer next to themselves via `%~dp0` / `dirname $0`, so nothing is substituted and no path can be wrong. Two non-obvious wins: a locally-GENERATED executable has no Mark-of-the-Web, so no SmartScreen prompt where a downloaded `.cmd` would get one; and self-contained copies survive a plugin update that moves the plugin folder.

**Automation added:** the installer closes Claude itself (graceful `CloseMainWindow` / `osascript quit`, then force) and reopens it - on Windows via the `Get-StartApps` AppID captured BEFORE the kill, because the Store build has no launchable .exe. It also runs `nlm login` inline. The close moved from the start of the run to just before the config write, so Claude is shut for seconds rather than the whole install.

**Secret handling:** ships as `scripts/setup/client-secret.txt`, read by both installers, prompt as fallback. Deliberately a file rather than hardcoded - keeps it out of chat transcripts and script diffs, and a bundle can be built without it for anyone outside Innowise. The security argument for shipping it at all: it is a Desktop/"installed app" OAuth client, which per Google's own spec cannot keep a secret confidential (PKCE + localhost redirect are the actual protection), and the consent screen is Innowise-restricted. STILL A PLACEHOLDER as of this session - one line for Anton to fill, then repack. Residual exposure handled: the setup folder sits in a possibly-Drive-synced projects folder, so the skill offers to delete it once connectors probe clean and checks for leftovers at the start of every run.

Verified: full real run of the sh script under a fake HOME (correct merge, unrelated connector preserved, cred file 600, corrupt-JSON refused after backup); PowerShell `Parser::ParseFile` clean + ASCII-only; `-WhatIf` end to end on the real machine (Store config path, existing connectors preserved); `.cmd` forced to CRLF while `.command` stays LF; validator PASS; nothing lost vs the previous bundle bar two stale `.pyc` files. Untested and flagged: uv's managed-Python download (the sandbox cannot reach GitHub releases) and every macOS-specific behaviour - `pgrep -x Claude`, `osascript` quit, and whether the `.command` exec bit survives the mount.

Lesson: [[feedback_verify_limits_dont_assert]], extended with the fifth and most expensive instance, plus a new ranked rule in the project CLAUDE.md - delete the step > have the tool do it > have Claude generate a thing they click > give them a line to paste > explain it well.

## v0.35.0 / v0.36.0, and the .mcpb question, 2026-07-30

Two more installer fixes, both from real evidence rather than review:

**v0.35.0 - the dependency break Yauheni hit.** `mcp-google-sheets` 0.6.3 does not constrain its
SDK, so it pulled `mcp` 2.0.0, which removed `mcp.server.fastmcp`; the server died with
ModuleNotFoundError at every launch while the install reported success. Reproduced exactly. Two
corrections to his report: `workspace-mcp` is NOT exposed (it pins itself to mcp 1.29.0), and a
launch-based smoke test false-alarms because a healthy sheets server also exits non-zero without
credentials. Both installers now IMPORT-check every tool after install (entry-point modules, run
from a temp FILE rather than `python -c`, because a multi-line `-c` mangles on some hosts and the
resulting SyntaxError reads as a broken tool) and apply `mcp<2.0.0` ONLY if the check fails - so
the upstream fix is picked up automatically with no re-release.

**v0.36.0 - config detection made deterministic.** It globbed `Claude_*` and took the first
match without validating it, falling back to `%APPDATA%\Claude` which the Store build never
reads. My first fix ranked candidates by config mtime and immediately chose "standard install" on
a Store machine, because under package redirection both paths are the SAME FILE (identical NTFS
file id) and `Sort-Object` is not stable on ties. Now structural: if a `Claude_*` package exists
the Store location wins, full stop. It prints its reasoning, lists rejected candidates, and warns
when it creates a fresh config while another location already has one.

**Clean-machine test harness** at `skills-to-upload/Test-CleanInstall.ps1` (dev tool, not
shipped). Extracts the real `.plugin` into a throwaway profile, redirects USERPROFILE / APPDATA /
LOCALAPPDATA / UV_*, replaces PATH with the Windows minimum, forces
`UV_PYTHON_PREFERENCE=only-managed`, and fingerprints the real profile before and after. Verified
the from-nothing path in 78s: uv bootstrapped, fetched cpython-3.12.13, all three installed and
imported, the sheets pin fired. See [[feedback_instrument_contaminates_measurement]] for the two
ways its first version lied.

**The strategic finding: `.mcpb` distribution works and can replace the installer.** Prompted by
Ilya Isayenia's `google-workspace-mcp.mcpb` and its Cloud Run token broker (secret genuinely
absent, verified end to end). Built `skills-to-upload/mcpb-probe/` and got a SELF-CONTAINED
verdict inside Claude: a bundle shipping `bin/uv.exe` bootstraps its own CPython and dependencies
with nothing on the machine. Target shape becomes `.plugin` for skills + one `.mcpb` per server,
no script. Mechanics, constraints and the MAX_PATH trap are in
[[reference_claude_desktop_extensions]]. Feedback for Ilya written up at
`meta/ilya-mcpb-feedback-2026-07-30.md`; the decisive open question is whether his bundle works
on a machine without uv, which neither of us can test.

Also proven and worth carrying: both his extension and our installer key tokens on
`~/.google_workspace_mcp/credentials/<email>.json`, so on a machine that ran our installer his
extension reads OUR client id and OUR secret from that cache and bypasses the broker entirely.
A PM must have one or the other, not both.

## ATOMIC ARTIFACT SKILLS + SETUP REBUILD, 2026-09-02/03 - v0.39.0, 15 skills, 38 files, PACKED

**THE SECOND AXIS, and the biggest design change since "steps = clusters".** Anton: initiation skills are fine but artifacts are worked all project long and "how to work with them is buried inside the initiation". Evidence: `a04-a05` Stage 2 held 34 lines of risk-register know-how - ID conventions, traceability, the Risk Library pass, both control metrics with the denominator-honesty rule - reachable ONLY by re-running an initiation step. **The know-how was not missing, it was unreachable.** Design note: `pm-copilot/design/atomic-artifact-skills.md`.

All 21 artifacts walked; 11 live past initiation; reduced to `project-brain` (1), `risk-register` (8), `monthly-plan-update` (11+12, not built), `prorep-update` (17, Anton's item 5), `scope-change` (6+7, low confidence). **Anton corrected two of four cuts:** Resource Plan and P&L ARE a monthly PM job - the surrounding automations serve Michael, the RMs and Anton, never the PM's own month-end pass (lesson in project CLAUDE.md); and the roadmap moves without scope moving, so 13 leaves `scope-change` and feeds a NEW open question he raised - "a skill/structure on how to check progress reliably", which is not roadmap maintenance and probably subsumes artifact 13.

**RUN PHASE DECIDED: no phase construct.** "Atomic skills that PM runs when he needs them... they sit near A skills for now." Scheduled tasks deferred. Four consequences: discovery is now the BINDING constraint (A-skills have an implied order and a router; atomic skills have neither, so nothing upstream suggests one); the `description` trigger phrases are the only discovery mechanism; no numeric prefixes; `project-router` must learn they exist. Mechanism confirmed by Anton: **a skill calls another by INSTRUCTION, not import** - so the handoff is prose and only as reliable as its wording (name the skill, name the mode, say what to hand back).

Built: `project-brain` (feed/ask/review) and `risk-register` (create/update/review) - shared shape is write/change/audit, named per artifact. `review` is the mode nothing else had and probably the most valuable: "can this still be trusted", answered with evidence. `a04-a05` Stage 2 thinned to step framing only.

**BRAIN STALENESS - the rule existed and did not fire.** The baseline already said "FEED IT BY DEFAULT". Diagnosis: it was a DISPOSITION WITH NO TRIGGER, unlike the money rule which is a prohibition checked at a specific action. Countable second cause - brain mentions per skill: a01 19, a10 15 (both SEED it), then a02-a03 8, a04-a05 5, a06-a07 2, a09 1, a11-a13 1. Seeded at A01, set up at A10, ignored by the eight steps producing most artifacts. Fix: the rule now names a moment - "any checkpoint where an artifact, register, decision, transcript or document was produced, filed or found ends with the brain question", whether or not a skill is running. Propagated per-skill and NOT as a paste: `a02b` gets an absolute nothing-goes-in override, `a06-a07` roadmap-yes/P&L-never with the same-breath trap named, `a09` roster-yes/CVs-never ("the FACT of the team is shareable, the HR record behind it is not").

**SETUP: one counter of TEN steps, owned by SETUP.md, skill runs 4-10.** Root cause of PMs stopping at connectors was two competing counters (doc said 8, skill announced "seven stages" mid-install). "Complete/finished/done" now allowed in exactly one place. Resume detection reads state rather than asking. Also landed: outside-the-project hard stop, prerequisite gate, One Portfolio defaulted not asked, OAuth stall as an expected branch (refused vs never-answered distinguished FIRST - they look identical and an unanswered consent is what leaves a connector looking dead), six-link NotebookLM chain. **Git corrected: it is a CODE TAB prerequisite, not a NotebookLM one** - so it blocks step 4 if the whole run is in the Code tab, step 7 if they switch over only for NLM.

**FOUR-AGENT PRE-REPACK REVIEW (setup docs / instruction layers / all skills / packaging) - worth repeating before any release.** Found four defects I had introduced hours earlier, including one that mattered: the resume fix did not work for its own primary scenario, because `pm-copilot-setup.md` was written only at step 10 while the common stop is step 7. Also found the thinning had ALREADY drifted - `a04-a05/references/output-shapes.md` held a full second register definition and the two copies already disagreed on a metric name. **Lesson: when thinning a skill, check its `references/` folder** - the worst place for a duplicate, because nobody re-reads it while editing the SKILL.md.

**SECURITY FINDING I OVERSTATED, Anton pushed back correctly.** Reported the OAuth secret in `scripts/setup/client-secret.txt` as a BLOCKER needing rotation. It is an INSTALLED-APP secret (Google does not treat these as confidential; PKCE is the protection) and the SAME secret already ships in `pmc-gws.mcpb` manifest and `pmc-sheets.mcpb` client_secret.json, which every PM must install. No rotation. Only real point: `.mcpb` installs from local disk and never leaves the machine, `.plugin` is uploaded to install, so the plugin's copy rested outside for no benefit. Error pattern = the same proximity-reads-as-severity mistake as "already served". Resolution: `scripts/setup/` MOVED to `_archive/pm-copilot-scripts-setup-2026-09-03/` - the folder was already retired by the docs, so this removes the dead installer AND makes the exclusion structural rather than dependent on remembering a `-x` flag.

**PACKING, second working method (bash was denied this session, so `zip -r` was unavailable):** build the archive with `ZipArchive` + `CreateEntryFromFile` and construct each entry name yourself as `.Replace('\','/')`. Do NOT use `Compress-Archive` or `ZipFile::CreateFromDirectory` - both can emit backslash separators, which the ZIP spec forbids and the installer rejects after a long apparent upload. Verify `entries with backslash paths: 0` before shipping.

Shipped: `pm-copilot/dist/pm-copilot.plugin` (38 files, 211 KB) + `pm-copilot/dist/PM-Copilot-alpha-2026-09-03.zip` (plugin + the three UNCHANGED `.mcpb` + SETUP/BEFORE-YOU-START). Extensions byte-identical to July, so a PM who has them does not reinstall. **Installing the plugin does NOT update the workspace baseline** - the always-on brain trigger only lands on a re-run of copilot-setup, so half of the brain fix ships and half does not. Applies to Anton too.

Still true: 13 of 15 skills never run on a real project, and the untested part of the new pattern is specifically the prose handoff. Anton closed "test the skills" as a tracked task - he uses it himself and collects PM feedback.

## v0.40.0, 2026-09-03 - prorep-card, the description audit, and the enablement chain

**Third atomic artifact skill: `prorep-card`** (artifact 17), the weekly eight-field status + eight PMO indicators. Generalized from Anton's personal `prorep-metrics-update` and the already-good `automations/prorep-status/prorep-weekly-prompt-shareable.md`. **Two modes, not three, and the reason is worth keeping: there is no write mode because nothing about this card is ever created by the PM** - the card comes from Sales at Closed-Won and its descriptive fields are A10's. What recurs is the weekly status.

**Anton's correction, and it produced the session's most reusable artifact.** I had merged three different field sets under "metrics" and edited the reference pack to say so. He: "don't confuse metrics with pmo metrics, double check with atlassian on my project for example." A live read of one card found THREE sets - the eight `Indicator_*` (22759-66, weekly, PM's), four older lozenge fields (12006-09 + a `Metrics update` date, abandoned, nine months stale while Set A was current), and Health Check/audit/PMO Rating (owned elsewhere, all empty). Neither "METRICS" nor "PMO Operational Metrics" exists as a field NAME - both are UI tab labels and no Atlassian tool exposes tab grouping, so which covers which is recorded as UNRESOLVED. New reference `references/prorep-fields.md`, marked OBSERVED vs INFERENCE line by line. Full lesson in project CLAUDE.md.

**DESCRIPTION AUDIT, all 16 - and it found a real bug, not just weak wording.** `project-router`'s description advertised "in-flight" projects, the exact case its own body spends 30 lines forbidding under a heading called "The failure this prevents". Structural finding worth more than the fix: **every deferral in the plugin was stated by the skill that RECEIVES the work, never by the one that should step aside** - `map-existing-project` said "use project-router only for a brand new project" while router said nothing, and `risk-register` disclaimed the first build while `a04-a05` listed "build the risk register" as its own trigger. A deferral in a body cannot influence which skill fires. Nine descriptions rewritten; the weak pattern was positional triggers ("after A01", "after scope is validated") which are not situations a PM recognises AND are the one kind of trigger the standard says cannot be relied on.

**DISCOVERY RESEARCH - the page is not the instrument.** Notes: `pm-copilot/design/discovery-research-2026-09-03.md` and `pm-copilot-competitive-scan-2026-09-03.md`. Vercel's eval: skill installed with default discovery = 53%, identical to no docs; + one "use this skill" line in the always-loaded file = 79%; compressed index in it = 100%; "in 56% of eval cases, the skill was never invoked". **Anton's caveat is the important one and I had framed it wrong**: their 53% row is a DOCS skill with a generic description, ours carry explicit trigger phrases, so we start nearer their 79% row. Implication is narrower than "change instrument" - a skill whose description does not say WHEN is the one at risk, checkable per skill. Also: no study anywhere measures a cheat-sheet driving adoption; Ontario mandated Gawande's checklist across 200,000+ procedures for no significant effect because it was not really used; Carroll's paradox of the active user explains the abandoned onboarding (production bias - PMs will not get established up front even when it saves them time). Decision: **strengthen the baseline, no 17th skill** - a skill that fixes discovery is itself subject to discovery and would have to fire on the vaguest input.

**Competitive scan of PM skill packages.** Closest existing artifact is `lpm-skills` (legal PM, 16 skills, ex-Baker McKenzie), whose published principles are partly the OPPOSITE of ours - draft correspondence produced immediately without gates, "produce don't ask", "skills that require behaviour change don't get adopted". `phuryn/pm-skills` (25,932 stars, product not project) has the cleanest skill-vs-command articulation and **suggests the next commands after any completes**. Anthropic has NO project-management plugin and has published nothing on doing PM internally; `product-management`'s description formula (one capability clause + exactly four SITUATIONS) is the closest thing to a house style. **Biggest scope gap found: scope change control as a lifecycle skill** - ours is front-loaded at A02b/A04, nothing covers "the client emailed something that is a CR and nobody has named it as one". Fires weekly. Then meeting-notes-to-artifact (7/8 sources, we have zero), a quality tier that audits artifact CONTENT not existence, a scheduled portfolio sweep, closure. Convergent grouping across 3 sources: partition by whether the USER invokes it. At 8-9 skills nobody groups; at 68 and 77 everyone builds a second index - **we are at 16, on the boundary.**

**BASELINE REGRESSION, flagged not hidden: 246 lines, was 203, ceiling 169.** The index table made "Reach for a skill" the largest section at 45 lines. The index is the evidenced intervention so it earns its place, which means something else in that file has to go - the trim is now more urgent, not less. Also caught live and worth remembering: loaded rules arrive wrapped in "this context may or may not be relevant to your tasks", so the index is framed as ADVISORY - hence imperative phrasing, which is a mitigation and not a fix. Only real test is a cold "what can you help me with?" on an installed machine.

**Enablement chain, all new files in `pm-team/`:** `pm-copilot-field-guide.html` + a 3-page A4 PDF + a published artifact (three bands - start here / the arc with A08 as a physical gate / all project long; when-to-reach and what-to-type as SEPARATE columns, per the BA sheet); `how-claude-actually-works.md` v2 (2,651 words vs 6,864 original, model-level truth only, no products or versions since that is exactly what went stale); `claude-101-assessment-2026-09-03.md`; `pm-enablement-structure-proposal.md`; `pm-copilot-first-three-tasks.md`.

**The BA cheat sheet EXISTS and my agent's confident negative was wrong** - it searched vault/Drive/Confluence/Chat/Gmail and surfaced Ilya Razuvaev's outstaff engineer framework instead. Anton produced the real one. Its transferable ideas: a one-sentence "you don't launch skills" callout top-right, a workflow-ordered pipeline strip, separate когда/пример columns, and **a partition of nine invoked skills from four the reader is told to ignore** ("думать о них не нужно"). Note the disagreement worth sitting with: the BA sheet says the model picks the right skill; Ilya's framework says "скиллы сами не срабатывают" from ~100 sessions and injects a charter to force it - same conclusion as Vercel, reached in-house.

**FIRST THREE TASKS, and Anton settled all four opens.** Map a project (LIVE with a facilitator), this week's PROREP (solo), build your own voice skill (solo). Voice skill is PERSONAL, not bundled - nobody collects it, which is why they can use real messages. NO scaffold: "just the direction and what it should do and achieve", we want to see what they build. **A thin Task 1 sweep is OUR bug not the PM's** - there is a lot of material on a real project, so an empty result means we are looking in the wrong places. All three run AFTER setup completes. **`copilot-setup` step 10 now SEEDS them into `pm-tasks.md` with pass conditions on the line** (Anton: "good idea"), then leaves them alone. Pass conditions are inverted throughout - not "did it work" but "name one thing it got wrong", because 14 of 16 skills have never run for real and a PM reporting no problems was not reading. Task 3's condition is "you can say what you'd change in the skill", which is the can-continue-alone test: **writing a skill's "use when" line is the same problem the audit found in seven of ours, so making one skill teaches how all sixteen work.**

Also: `pm-tasks.md` brought to parity in the baseline (it had a descriptive paragraph while `project-context.md` had three named MANDATORY rules).

Related: [[project_a01_handover_skill]], [[project_lesha_strategic_session]], [[project_alchemy_a01]], [[feedback_copilot_checkpoints_no_autowrite]], [[feedback_portability_before_breadth]], [[reference_standard_a_numbering_trap]], [[project_copilot_strategy_deck]], [[reference_plugin_root_dead_path]].


## daily-digest, 2026-09-24 - v0.44.0 / v0.44.1, 20 skills

Alexey asked at AI PMO 2026-09-24 for a daily digest of key management decisions and new use cases
from chats. Built as `daily-digest` (IPMO-313) from the evening-chat-digest that has run for Anton
since 2026-06-10. Decisions (Anton): no per-role lens mode, because a lead sets it up once and there
are many PMs - one default look-for list the PM reorders, drops from or adds a focus to. Four delivery
options (private space, own space only if nobody else is in it, email to self, keep it in the run);
a daily file only on request, because it leaves contract and economy chat content on disk. Meetings:
Bluedot if connected, otherwise ask where the PM's notes end up. Setup always ends by asking for the
schedule time, so it never reads as a one-off.

Design: everything tunable lives in `<workspace>/digest-registry.md`; the scheduled prompt carries
only the registry path, name and email, so it is rewritten only for a new time. The run template is
in `skills/daily-digest/references/run-template.md` and the Stage 5 preview runs the same text.

Smoke test (fresh subagent, 5 spaces, delivery=run) gave a good digest and six fixes, all in 0.44.0:
no clock without a shell (one constant `date -u` command allowed), oversized Gmail batches and
get_meeting transcripts (triage from search results, one thread per fetch, Bluedot summary email
instead of the transcript), Cyrillic name spellings (`name_variants`), list_spaces capped at 100
(page size + token), Invitation mails, and one-item-one-section losing a mention. 0.44.1 routes to it
from the baseline table and the copilot-setup hand-off.


## wrap-up, 2026-09-30 - v0.46.0, 21 skills

Anton asked to bring his own `session-wrap-up` into the copilot (IPMO-334), with the caveat that his
setup is not a PM's. Decided with Anton: ONE route for PMs, no Quick/Full. The task list is found from
the setup state, then `pm-profile.md`, then `pm-tasks.md` / `TASKS.md` at the root; none found, ask;
a list the PM names gets offered back as a `pm-profile.md` line so the next run finds it.

What did not port, and what replaced it: the work log (a PM has none - the dated Done section is
theirs), vault frontmatter (no Obsidian, IPMO-328 still open), the memory step (corrections go to
`copilot-feedback.md`, a twice-seen preference becomes a `pm-profile.md` offer, Claude's own memory is
left alone - Cowork and the Code tab keep separate stores), the skill log (it IS the feedback log),
and the IPMO step (becomes a `project-brain` offer, gated there). The alpha log gains most: one fixed
moment per session to be written, instead of depending on the copilot noticing mid-session.

Step-aside: a personal wrap-up skill wins, checked from the session's own skill list and the profile.
Plugin skills ignore `skillOverrides` (docs, checked 2026-09-30), so there is no per-skill off switch;
Anton adds `Skill(pm-copilot:wrap-up)` to his vault's deny rules once this ships. Named `wrap-up`, not
`session-wrap-up`, so the two are not read as one skill. Russian: "and the same in Russian" in the
description, as pmo-guide, pm-voice and daily-digest do. Cyrillic trigger phrases would need the
validator allowlist widened - not done unless a Russian test on a PM install misses.

Wired in the same change: README row, paragraph and working-skill count; field guide card, chip and
count; baseline index row plus one paragraph; one hand-off line in copilot-setup ("say wrap up before
closing a chat"); plugin.json description 486/500.

## NotebookLM login, 2026-10-09 - for v0.46.1, pmc-nlm 1.2.0

A PM's alpha report (plugin 0.46.0, Windows, Code tab) lost an hour to a dead NotebookLM. Every check
said valid while every call failed. Root cause on our side: 0.46.0 shipped `pmc-nlm` 1.1.0 pinned to
0.9.4, and the 0.15.2 bump from 5 Oct never shipped. 0.15.2 would not have been enough: upstream
0.15.3 is the release where login waits for real signed-in cookies plus CSRF before saving, and where
an API rejection stops hiding behind "Notebook count unavailable (network slow)". 0.15.4 makes
`--clear` work on Windows. Pinned 0.15.4, the build the PM proved.

What changed in copilot-setup, and why each one:
- Proof is `refresh_auth` then `notebook_list`. The old text trusted `server_info` and distrusted the
  list; `server_info` auth_status is a 30s-cached homepage probe and was the one that lied. The refresh
  first answers the old worry (a running server serving a session gone from disk).
- Fast path for "fix my NotebookLM": most repair runs are this, and the ten-step flow is wrong for it.
- Clean sign-in moves the profile aside into `stale-login-<stamp>/` (outside `profiles/`, so it is
  never listed as a profile), with the Chrome profile too for a wrong account. Moved, not `--clear`:
  reversible. The one sanctioned touch of credentials, behind an explicit yes.
- uv by full path after install (Claude's PATH is fixed at app launch), and the sign-in runs with
  `UV_CACHE_DIR` / `UV_PYTHON_INSTALL_DIR` under `$HOME/.uv` - the default cache is under AppData,
  which the MSIX container redirects. The Python dir matches the manifest's, so no second download.
  Checked from Git Bash that uv resolves both to `C:/Users/<user>/.uv/...`. The PM's failure without
  them was not reproduced here.
- The server's own hints (`nlm login`, `uv tool upgrade`) are named as wrong on a PM machine, in the
  skill and in a new baseline section, because they are what produced "installed but not in my
  terminal".
- A missing tool is not a missing extension: search first (it waits for servers still connecting).

SETUP.md: terminal fallback says to pick "plain file" if 0.15 asks - that is what the Code-tab sign-in
makes, and it is the only mode an older extension still reads. Not tested: whether 0.15.x
`refresh_auth` headless recovery holds for Innowise Workspace accounts (upstream #330 risk). The skill
tries it as a cheap first step and promises nothing.
