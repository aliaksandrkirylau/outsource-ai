---
name: copilot-setup
description: First-run setup and health check for a PM starting with the PM Copilot. Use when a PM has just installed the copilot, or says "set up my copilot", "get me started", "first run", "onboard me", "initialize my workspace", "install the baseline", "what do I do first", "is my copilot working", "my connectors are broken", "Claude cannot see my Drive", "fix my setup", "check my setup", "fix my NotebookLM", "NotebookLM stopped working", "the project brain says authentication expired". Probes which connectors actually work and guides repair of the copilot's three extensions, decides the workspace shape, installs the always-on layer (baseline rules, the reference pack copied into the workspace, a pointer block in the PM's global instructions), drafts their portfolio profile, starts the task list and the alpha feedback log, and records the setup state so other skills know what is available. Run once per PM before project-router, and again whenever something stops working.
---

# copilot-setup - set the copilot up, and fix it when it breaks

Two jobs in one skill: first-run setup, and the thing a PM runs when something stopped working. Both start the same way - find out what is actually connected - so they are one flow with a different ending.

Goal: after this runs the PM has working connectors, or a clear list of what to do about the ones that are not, the always-on layer installed and pointing at real paths, a profile of their own portfolio, somewhere for tasks and feedback to land, and an understanding of what just happened.

## How this skill behaves - read first

Guided and staged. One stage at a time, STOP at each checkpoint, show what you found or are about to do, get a yes. A PM running this for the first time should never be surprised by a change to their machine.

### One step counter, and it is not yours

There is ONE numbered list for the whole install, it lives in `SETUP.md`, it has TEN steps, and this skill is steps 4 to 10 of it. Do not invent a second count, do not say "seven stages", and do not number anything from 1 - the PM has already done steps 1 to 3 before they got here, and a fresh counter starting at 1 is why nobody could tell how far along they were.

| Step | What it is | Stage below |
|---|---|---|
| 1-3 | Plugin, extensions, restart - done before this skill runs | - |
| 4 | Start setup: prerequisites, folder, project check, workspace shape | Stage 0 |
| 5 | The Google sign-ins | Stage 1 + 1b |
| 6 | Atlassian | Stage 1 + 1b |
| 7 | NotebookLM | Stage 1b |
| 8 | The rules file and the PMO reference pack | Stage 3 |
| 9 | The PM's profile | Stage 4 |
| 10 | Task list, feedback log, health check, hand-off | Stages 5 and 7 |

Every checkpoint opens with the position, in those numbers, in plain words:

> **Step 6 of 10.** Atlassian is connected. Next is step 7, the NotebookLM sign-in - the longest one. Ready?

Two optional extras sit OUTSIDE the count and are never numbered: the voice sample (Stage 6) and the suggestions about the PM's own instructions (Stage 8). Offering them must not read as more steps to survive.

### Do not let it look finished before step 10

The single most common failure this skill has: every PM in both install sessions stopped when the connectors went green, which is step 7. They thought they were done. They were not, and the half they skipped is the half that makes the copilot pick the right skill.

So:

- The word **"complete"**, "finished", "done" or "all set" appears in exactly ONE place in this whole flow - the Stage 7 hand-off at step 10. Nowhere else, for any reason.
- After the connectors, say what is LEFT before saying anything positive about what works. "Connectors are green. That is step 7 of 10 - three left, and they are the ones that make the copilot useful."
- Never offer an exit that sounds like an ending. "Want to stop here?" is fine; "that is everything working" is not, because it is not true at step 7.

### Run this in the Code tab

Ask the PM to run setup from the **Code tab**, not a Cowork window. Say why in one line: it is the only surface with a real shell on their own machine, and the NotebookLM sign-in needs one.

That is not a formality. Cowork's shell is a sandboxed Linux VM - it cannot launch the browser on their laptop or write to their user profile, so the NotebookLM step simply cannot complete there. Everything else in this skill works on either surface; that one step does not.

If a PM is already mid-setup in Cowork, do not restart them. Carry on and move only the NotebookLM sign-in to the Code tab at the point it comes up.

Three rules that never relax:
- Never authorize a connector on the PM's behalf and never touch their credentials. You detect and report; the PM signs in. The one exception is in the NotebookLM repair in Stage 1b: with an explicit yes, you may move a stale NotebookLM login folder aside so the next sign-in cannot reuse it. Move it, never read, copy or delete what is inside.
- Writing into the workspace or into their instructions is a real change. Show the exact content and the exact target file, and get an explicit yes.
- Never run `uv tool install`, `uv tool upgrade` (or `pip install`) for the PM from inside Claude. Claude's own shell is redirected into the app's MSIX container on Windows, so a tool installed that way lands somewhere only Claude can see: every check you run passes and the PM's own terminal fails. Use the ephemeral `uv tool run` form given in Stage 1b, which installs nothing. The tell that someone got this wrong is `error: uv trampoline failed to canonicalize script path`.

The NotebookLM server gives two hints of its own that are WRONG on a PM's machine, and Claude follows them unless told not to. Its instructions say "run `nlm login`" - but `nlm` is deliberately not on a PM's PATH, so that fails with not-found and reads as "NotebookLM is installed but missing". Its `server_info` offers `uv tool upgrade notebooklm-mcp-cli` - but the extension pins its own version, so that upgrade changes nothing the extension runs and leaves an `nlm` only Claude can see. Ignore both. The sign-in is the pinned `uv tool run` form in Stage 1b, and the server version moves only when the PM reinstalls the extension.

### Fast path - only NotebookLM is broken

Most repair runs are this one: the copilot worked, and now the project brain fails with "Authentication expired", "not signed in" or a NotebookLM tool that is not there. When NotebookLM is the only complaint, do NOT start the ten-step flow. Skip the resume check, the folder check and the step counter, and go straight to "NotebookLM - check and repair" in Stage 1b. Say so in one line: "Only NotebookLM is broken, so I will fix just that - about five minutes, and the Google sign-in in the browser is yours to do."

It still needs the Code tab. If they are in Cowork, say that one step has to move there and why, then stop.

Plain language throughout. Do not expose file paths or schema details unless the PM asks or is about to run something.

## Stage 0 - Step 4: work out where they are, then frame it

Four things happen here before any question gets asked. Three of them are checks you run yourself.

### 0a. Is this a resume?

Check this FIRST, before anything else, and check it by LOOKING rather than by asking. A PM who stopped at step 7 last week and came back is the most likely person to be running this, and asking them "is this a first setup?" puts the burden of knowing on the one person who does not.

Read, in the workspace:

- `pm-copilot-setup.md` - if it exists it names the date, the highest step reached, the connector results and what was left unresolved. That file IS the resume point.

  **Create it at the END OF STEP 4, before the connectors, and update it as each step lands.** This is not optional bookkeeping and getting it wrong breaks the whole resume path: the most common place to stop is step 7, and if this file is only written at step 10 then the single most likely returning PM has no file, no baseline, no profile and no task list - so their resume looks identical to a first run and they get marched through everything again. Stage 5 formalises the file's full contents; what matters here is that it EXISTS early and carries `Reached step N of 10`. A two-line stub at step 4 is worth more than a complete file at step 10.
- `.claude/rules/pm-copilot-baseline.md` - present means step 8 was done.
- `pm-copilot-references/` - present and populated means step 8 was done.
- `.claude/rules/pm-profile.md` - present means step 9 was done.
- A task list (`pm-tasks.md`, or the `TASKS.md` the PM already kept) and `copilot-feedback.md` - present means step 10 was at least started.
- The pointer block, if they accepted one. Only checkable in the Code tab, at `~/.claude/CLAUDE.md`. In Cowork the global layer is app-managed and NOT readable as a file, so its state cannot be detected - ask, rather than reporting it as missing. See step 8.

Then say where they are and offer to carry on from there:

> **Picking up where you stopped.** You got to step 7 of 10 on 12 August - connectors are in, and NotebookLM was still outstanding. Steps 8, 9 and 10 have not run. Want me to re-check the connectors quickly and then carry on from step 8?

If nothing is there, it is a first run and you say so. Do not make a PM assert which one they are.

### 0b. Are they inside a project?

A chat outside the project loads none of the project's context, so setup writes files the PM's later sessions will not read. It happened in a live install and cost real time.

Check the working folder against the folder they name. If the window is offering to "make a project so Claude can use the same context", they are outside it.

If they are outside, STOP and say so plainly - this is one of the few hard stops in the skill:

> Before anything else: this chat is not inside a project, so what I install now will not load in your later sessions. Create a project pointed at [folder] and start setup from a chat inside it. Everything from here works properly once you do.

### 0c. Are the prerequisites actually in place?

The "Before you start" section of `SETUP.md` lists five. Check what you can and stop clearly on what is missing, rather than failing four steps later with a confusing error. Keep this table matched to that section, because a PM who worked through it expects the same list. Git is the fifth and has its own paragraph below the table, because whether it blocks depends on the surface:

| Prerequisite | How you know | If it is missing |
|---|---|---|
| Claude access accepted | You are talking to them, so this one is self-evident | - |
| Desktop app, not the browser | Only the desktop app has the Code tab and extensions | Installing the app itself may need admin rights on a work laptop - it blocked a PM in a live session. If they cannot run the installer even as administrator, that is an IT request, not something to work around |
| A working folder with a project pointed at it | List the folder; the project half is checked at 0b above. Claude refuses protected locations - a Mac home folder is the one that bit | Ask for a specific subfolder, not `~` |
| The zip unpacked | They needed it for install steps 1 and 2, so this is usually self-evident by now | If they never unpacked it they are not past step 2 - go back there |

The three extensions are install step 2, not a "Before you start" item, so do not gate on them here - Stage 1 is about to probe them properly and Stage 1b fixes what is missing.

**Git depends on which surface they are on, so check the surface before deciding whether it blocks.** Git is a prerequisite of the CODE TAB, not of NotebookLM - the Code tab needs it to open a session in a folder. NotebookLM only comes into it because the sign-in is the reason a PM goes to the Code tab at all.

- **Running the whole setup in the Code tab** (what this skill asks for): Git is needed HERE, at step 4, or the tab will not open a session and nothing else runs. Check it now.
- **Running in Cowork and switching to the Code tab only for step 7:** Git is not needed yet. Do not block them at step 4 over something three steps away - raise it at step 7.

Either way, the Code tab's own prompt comes first: on a fresh install Claude sees Git is missing and walks the PM through installing it, on both systems. Only if it does not offer, use the manual route in SETUP.md's "Before you start": on Windows the installer from git-scm.com with the defaults; on Mac `xcode-select --install` in Terminal (tell them how to open Terminal - Cmd and Space, type Terminal) and click Install in the window that appears. Not Homebrew: it is a pasted curl command and a password prompt, too much for a first-time PM. Then quit Claude fully and reopen - it does not notice Git until it restarts.

### 0d. Then frame it

Say where they are, what the shape is, and that most of the time is theirs not yours.

The workspace shape is DECIDED here, not asked, and not revisited later. Default is one portfolio workspace - state it, record it, move on. Stage 2 carries the reasoning if you need it, and the one case that overrides the default: if the folder they named is a single project rather than a portfolio root, say what you see and offer both.

If they told you this is a repair rather than a first run, Stage 1 is the diagnosis either way - go from there straight to the fix and skip the install, profile and voice stages.

CHECKPOINT: "**Step 4 of 10.** Setting up your copilot - seven steps from here, around 40 minutes, and most of that is you clicking through Google sign-ins rather than waiting on me. Steps 5 to 7 are the connectors, 8 to 10 are the copilot's rules, your profile and your task list. Getting the connectors green is step 7, not the end - the last three are what make it reach for the right skill. No project of yours gets touched. Two things: do this in the Code tab rather than a Cowork window, because the NotebookLM sign-in needs a shell on your own machine and Cowork does not have one. And I am assuming one portfolio workspace - all your projects as subfolders of [folder] - which is what most PMs want; say so if you would rather have one workspace per project. Folder is [folder] - right? OK to start?"

## Stage 1 - Probe the connectors for real

Do NOT ask the PM what is connected, and do not infer it from the tool list. PROBE each one with a cheap read and see what happens. A tool that exists but is not authorized fails at call time, not at list time - that distinction is the entire point of this stage.

| Connector | Probe with | Needed for |
|---|---|---|
| Google Drive | list a few Drive items | Every skill. Project folders, all documents |
| Gmail | list recent message IDs | The takeover sweep, client thread history |
| Google Calendar | list calendars | Meeting cadence, the de-facto communication plan |
| Google Chat | list spaces | A01 harvest, A02 channels, the takeover sweep |
| Google Sheets | list spreadsheets | WBS, resource plan, checklists, P&L |
| NotebookLM | list notebooks | The project brain (a mandatory starting artifact) |
| Atlassian Jira | list visible projects | PROREP, tracker, risk register |
| Atlassian Confluence | list spaces | The live standard, filing mandatory artifacts |

Do NOT probe for or recommend a desktop-access connector as part of setup. In the Code tab you already have a shell, and nothing here needs one beyond that. See the note at the end of this skill for when it legitimately comes up.

Report each as working / not authorized / not installed, with a one-line why-you-need-it. A short table, not an essay.

For anything not working, name the fix. Note which kind of thing each one is, because the fix differs:
- Atlassian is an ordinary connector the PM adds in Claude's own settings. Point them at it; they do it themselves.
- Google Drive / Gmail / Calendar / Chat / Sheets / NotebookLM come from the copilot's three EXTENSIONS - `pmc-gws`, `pmc-sheets`, `pmc-nlm`. Installed but unauthorized means one call and a sign-in - except NotebookLM, which authenticates differently and is covered on its own in Stage 1b.

**A tool missing from your list does NOT mean the extension is not installed.** In the Code tab, extensions often attach to a session late, and a copilot that reported "no NotebookLM access" from a missing tool cost a PM an hour on 9 Oct. Before you call one missing: if your session can search for tools that are not loaded yet, search for it by name (`notebooklm`, `drive`, `sheets`) - that search waits for servers still connecting. Still absent, ask whether the extension shows in Claude's settings under Extensions. Listed there means it has not attached to this chat: a new chat first, then a full quit and reopen. Not listed means it is not installed (Stage 1b).

One extension can serve several rows in that table: Drive, Gmail, Calendar and Chat all come from `pmc-gws`, so they usually fail or pass together. If they do not, it is an authorization problem rather than a missing extension.

### Claude's own connector suggestions are noise here

While this is happening Claude will probably suggest connectors of its own - Asana, Gmail, Google Calendar, others. Every PM in both install sessions stopped to ask about them. Get ahead of it in one short paragraph rather than letting it derail the step.

Say: those are Claude's own suggestions, not part of this install, and the copilot does not need any of them. Atlassian is the single exception and it is on the list above.

If they ask what the overlap is, the honest answer is that ours cover more:

| Claude's own connector | Covered by | What ours adds |
|---|---|---|
| Gmail | `pmc-gws` | drafts, threads, labels, filters, attachments |
| Google Calendar | `pmc-gws` | free/busy, focus time, out of office, calendar management |
| Google Drive | `pmc-gws` | permissions, sharing links, folder creation, Docs and Slides editing |
| (none exists) | `pmc-gws` | **Google Chat** - spaces and messages, which Claude has no connector for |
| (none exists) | `pmc-sheets` | reading and writing cells, formulas, charts |

Leave them on or turn them off - nothing in the copilot reads them either way. Do not advise turning them off; it is not our business and it is not a step.

CHECKPOINT: show the table. Position first, and do NOT offer an off-ramp that sounds like an ending - the honest framing is that skipping a connector costs specific capability later.

"**Step 5 of 10.** These work, these need attention. [table] Want me to walk you through the ones that do not? If you would rather come back to them, that is fine - I will note what is blind and carry on through the rest of the connectors, but [name the skills that degrade] will not work properly until it is fixed."

Steps 6 and 7 are Atlassian and NotebookLM, so they come next whether or not step 5 fully succeeded. Never tell a PM the step after 5 is 8 - deferring a broken connector skips a FIX, not a step, and the count has to stay honest or it stops being worth stating.

## Stage 1b - Guided repair (only if something is broken)

Do not hand the PM a document and walk away. Work out which case they are in and give them the one thing that fixes it.

**Case: an extension is not installed at all.** The three servers ship as extensions - `pmc-gws` (Drive, Gmail, Calendar, Chat, Docs, Slides, Tasks, Contacts), `pmc-sheets` (Sheets) and `pmc-nlm` (NotebookLM). Installing one is something the PM does in Claude's own settings; you cannot do it for them.

There is nothing to download, fetch or configure first. Each extension declares its own runtime, and Claude supplies what it needs - it finds or downloads `uv`, and `uv` brings its own Python. So there is no python.org step, no version to check, and no "externally-managed-environment" to explain.

Point them at the install path and let them do it. Do not attempt to write a launcher, copy a secret, or edit the Claude config - none of that applies any more, and the OAuth credentials ride inside the extensions.

The one thing worth warning about: the first launch of an extension on a clean machine reaches out to the network to fetch its runtime, so it can take a minute and it needs egress. A PM behind a strict proxy may see the extension install fine and then fail to start, which reads like a broken bundle but is not.

After they install, say plainly that extensions load at startup - so a fresh install usually needs Claude restarted before the tools appear, and a re-probe after that is the only way to know it worked.

**Case: installed but not authorized (the two Google ones).** No script needed. Ask them to make one request that uses it ("show me my recent Drive files") and complete the Google sign-in. Warn them there are two separate Google extensions and therefore two separate consents - that surprises people.

**Case: the consent never appears. Treat this as EXPECTED, not as a fault.** It hit three of four PMs in one install session. The browser tab simply does not open, every connector comes back "not authorized" or "not found", and nothing is misconfigured. A PM who is not told this is normal concludes the bundle is broken and stops.

Work it in this order, and say which step you are on so it does not feel like flailing:

1. **Distinguish a refused consent from one that was never answered** - they look identical from inside a conversation and the fix differs. Ask: did a Google tab open at all? If it opened and they closed it, or it timed out unanswered, the request is simply outstanding - say "retry" and make the call again. That alone fixed one machine, and an unanswered consent is what leaves a connector looking dead rather than declined.
2. **If no tab ever opened: quit Claude completely and reopen**, then re-probe. This is what fixed it both times it happened - new tabs open, they approve, everything goes green. Completely means the tray on Windows and Cmd-Q on Mac, not just the window.
3. **Still failing: the extension started badly rather than being unauthorized.** An extension that cannot launch its runtime vanishes from the tool list entirely instead of erroring, so "missing tool" and "broken tool" are indistinguishable from here. Check whether the tools are absent or present-but-failing, and say which.

One variant seen in session 2 with no established cause: extensions installed, Claude restarted, and still invisible to a Code-tab session specifically. It resolved on its own. If it happens, say honestly that it is a known intermittent rather than inventing a reason, and try a new chat before anything more drastic.

Do not conclude "consent refused" unless they actually saw a Google screen and declined on it. Everything else is an unanswered request, and the fix for that is a retry.

**Case: NotebookLM - check and repair.** This one is different from every other row and needs its own handling. The fast path at the top of this skill lands here.

NotebookLM has no public API, so the extension cannot do an ordinary OAuth consent. It authenticates by driving a browser once and keeping the resulting session. That sign-in has to happen in a real shell on the PM's own machine, which is why this skill asks for the Code tab.

Say the plain fact before anything else: **the Google sign-in is theirs to do.** You start it and wait. A Chrome window opens on their screen, and you cannot see it, type in it or pick the account. If they step away, it times out.

**Start with the cheap check, because it often fixes an expiry on its own.** Call `refresh_auth`, then `notebook_list`. Recent server versions try to recover an expired login from the saved browser session when asked to refresh, so this alone may be the whole repair. A list that comes back is the proof - say it works and stop.

**What counts as proof.** Only a real call, and only after `refresh_auth`. A running server holds its session in memory, so without the refresh a passing call can hide a login that is gone from disk, and a failing one can hide a fresh login it has not read yet. These three have all said "fine" while every real call failed, so never report success on them alone:

- `server_info` reporting auth as `configured`. It is mostly a cached check of the Google homepage, not of NotebookLM. `unverified` proves nothing either way.
- `refresh_auth` reporting success on its own.
- `nlm login --check` printing "Authentication valid" with "Notebook count unavailable" under it. That second line IS the failure.

**A first sign-in on this machine: walk the chain.** This is step 7, it is the longest step, and it is the one nobody finished unaided in either install session. Budget ten minutes and walk the chain link by link, stopping at each. Do not hand over the whole sequence at once - it reads as a wall and people stall on link two. On a repair where NotebookLM has worked on this machine before, links 1 to 4 are done - start at link 5.

1. **The Code tab asks to select a folder for the local session.** Same folder they have been using. Say so before it asks, because it looks like a new decision and is not.
2. **Git.** Needed by the Code tab itself, not by NotebookLM - see Stage 0c. If it is missing, the route is the one in Stage 0c: Claude's own prompt first, then git-scm.com on Windows or `xcode-select --install` on Mac.
3. **Refresh the Code tab.** After installing Git the tab does NOT notice on its own. Reload it, or use the relaunch prompt if one appears. This link is invisible and it is where a PM concludes Git did not work.
4. **uv.** Install it from Astral if it is missing. A few permission prompts; `Allow once` is fine and applies only to the command being asked about. This is fine to do from here - it lands in their user profile, not in Claude's container. Then call it by its FULL path for the rest of the chat: Claude's shell does not see a newly installed program on its PATH until Claude restarts, which is how "uv is installed but not found" happens. The installer puts it in `~/.local/bin/`; the sign-in command below already falls back to that path.
5. **The sign-in itself**, below.
6. **Restart Claude or start a new chat.** NotebookLM commonly still shows as MISSING right after a successful sign-in. That is a stale connector list, not a failed login. Say this BEFORE they see it, or they will re-run a sign-in that already worked.

Then run the sign-in for them, from the Code tab, in the background - it waits up to 300 seconds, so a short timeout will kill it before they finish:

```bash
# AIM: open the NotebookLM sign-in in Chrome - the PM signs in, and the login is saved where the copilot's NotebookLM extension reads it
UV_PYTHON_INSTALL_DIR="$HOME/.uv/python" UV_CACHE_DIR="$HOME/.uv/cache" "$(command -v uv || echo "$HOME/.local/bin/uv")" tool run --from notebooklm-mcp-cli==0.15.4 nlm login
```

Keep the version pinned to whatever `pmc-nlm` pins, so the sign-in and the server are always the same build. Never a bare `nlm login`: `nlm` is not on a PM's PATH.

The two folder settings keep uv's Python and its download cache in the home folder. On Windows, whatever Claude's shell writes under AppData lands inside the app's own container, where long paths and leftover copies from earlier runs break the sign-in - one PM's only worked once these were moved. The home folder is not redirected, and the Python folder is the one the extension already uses, so the sign-in does not download a second Python. On a Mac they are harmless.

That form installs nothing and leaves nothing on their PATH - it is deliberately not `uv tool install`, for the reason in the rules at the top of this skill. If `uv` is not on the machine at all, it fails with a not-found error rather than anything informative - go back to link 4.

Tell them what to expect before you run it: a Chrome window opens, they sign in with their Innowise account, and it closes itself once NotebookLM has really signed them in. If they have signed in on this machine before, it often completes on its own without them touching anything. NotebookLM does NOT need to be open in a browser; it reads the Google cookies, so "should I open NotebookLM first" is a no.

When it finishes, `refresh_auth` then `notebook_list` - the proof above. If the list fails, if the sign-in finished without a browser ever opening, or if it used the wrong Google account, go to the clean sign-in.

**Clean sign-in - when a sign-in "worked" but NotebookLM still fails, or used the wrong account.** The usual cause is an old saved login that every new sign-in quietly reuses. Move it aside so it cannot, then sign in fresh. This is the one place this skill touches credentials, so show the command, say it can be undone, and get an explicit yes:

```bash
# AIM: move the old NotebookLM login aside (not delete) so the next sign-in starts fresh - it can be moved back
B="$HOME/.notebooklm-mcp-cli/stale-login-$(date +%Y%m%d-%H%M)" && mkdir -p "$B" && mv "$HOME/.notebooklm-mcp-cli/profiles/default" "$B/"
```

Wrong Google account ("I need a different email"): move the saved browser session as well, in the same command, or Chrome signs straight back into the same account. They then sign in from scratch, password and second factor included - say so:

```bash
# AIM: move the old NotebookLM login AND its saved browser session aside, so Chrome asks which Google account to use
B="$HOME/.notebooklm-mcp-cli/stale-login-$(date +%Y%m%d-%H%M)" && mkdir -p "$B" && mv "$HOME/.notebooklm-mcp-cli/profiles/default" "$B/" && mv "$HOME/.notebooklm-mcp-cli/chrome-profiles/default" "$B/chrome-default"
```

If a move fails because a file is in use, a Chrome window from the last sign-in is still open - ask them to close it and run it again. Then the sign-in above, then the proof. Tell them where the old login went; once NotebookLM works it can be deleted, and that is theirs to do.

**Case: it worked before and stopped.** Three usual causes, in this order.

One, NotebookLM specifically: the session expires roughly every week or two, and this is the most common breakage a PM will ever see here. It is not a fault and nothing is misconfigured. Run the cheap check first, `refresh_auth` then `notebook_list`. If that does not bring it back, the sign-in above; if the sign-in does not take, the clean sign-in.

Two, a stale cached Google token - the Workspace server caches by email address and silently reuses an old one, so a call can succeed against the wrong client and look fine.

Three, an extension that failed to start rather than one that is unauthorized. Extensions that cannot launch their runtime disappear from the tool list entirely rather than erroring, so "the tool is missing" and "the tool is broken" look identical from inside a conversation. A restart and a re-probe separates them.

**Case: the machine blocks it.** Locked-down laptops happen. Do not push. Options in order: ask IT to allow the extension runtime to reach the network; ask the copilot admin to sit with them; or carry on without the Google extensions. If they carry on, be honest about the cost - the takeover sweep and most document work degrade badly, though Atlassian and NotebookLM alone still cover a useful slice.

CHECKPOINT: re-probe whatever they fixed and show the updated table. Do not claim something works because a script finished - prove it with a call.

Say the position and what remains, in that order, and note that the sentence below deliberately avoids the words this skill bans: "**You are at step 7 of 10.** Connectors are green. Three steps left and they are the ones that decide whether the copilot picks the right skill - the rules and the PMO standard, your profile, then your task list. About fifteen minutes. Carry on?"

## Two things worth explaining here, once the connectors work

Both landed well with PMs in the install sessions, both reduce anxiety rather than adding a step, and this is the right moment - they have just watched Claude ask for a lot of access, and they are about to watch it write files.

Keep each to a few lines. This is reassurance, not training.

**What it can and cannot do without asking.** Read-only actions - searching Drive, reading a sheet, listing Jira issues - can be set to allow-always, and it is worth doing because otherwise they approve the same read fifty times. Anything that writes, creates or deletes cannot be automated: the always-allow option refuses those, by design. So every write comes back to them for a yes. A PM in the install session called this excellent protection against your own mistakes, and he was right - that is exactly what it is. It also means the copilot cannot quietly change a client document.

**The usage panel.** Watching a token counter climb was a real source of worry in the room. Two figures: the top one is a five-hour session window, the bottom one is the week. Normal PM work does not come close. The one thing that does eat it is reading a lot of material in one pass - a takeover sweep across Drive, Chat and mail - and that is worth knowing before running one, not worth avoiding.

## Stage 2 - The workspace shape - REFERENCE ONLY, decided back at step 4

This is not a step and it has no checkpoint. It sits here for the reasoning; the decision was stated at Stage 0d and recorded there. Do NOT stop the PM at this point to ask about their workspace shape - they are between the connectors and the install, and re-opening a settled question here is exactly the kind of stall that loses people.

There is a trap behind it worth understanding. A Cowork project rooted at a subfolder does NOT load instructions from its parent folder. So if the copilot's rules go in the portfolio root and the PM later opens a per-project space, every gate and convention silently disappears. Stage 3 installs a pointer in their global instructions as a safety net, but the shape still has to be a decision rather than an accident.

**The default is one portfolio workspace, and it is stated at Stage 0 rather than asked here.** All projects as subfolders of one folder, Claude always pointed at that folder, installed once, and the scanner and router work across every project. It is what almost every PM wants, and a question with an obvious right answer is a question that should not have been asked - it costs a round trip and invites a worse choice.

The alternative stays available and the PM only hears about it if they raise it, or if what you found at Stage 0 contradicts the default:

- **A workspace per project.** Cleaner separation, but the install repeats per project, this skill gets re-run per project, and the trap above bites harder.

Override the default WITHOUT asking in one case, and do it at Stage 0 rather than here: if the folder listing shows the PM pointed you at a single project folder rather than a portfolio root, say what you see and offer both, because the default is wrong for them.

Record the shape at Stage 0 - step 8 and every later re-run depends on it.

## Stage 3 - Step 8: install the always-on layer (WRITE GATE)

Three writes, one gate. They go together because each is useless without the others. The copilot ships its rules as content because a plugin has no always-on slot - a CLAUDE.md at a plugin root is not loaded as context.

Two of the three are ordinary file writes into the workspace. **The third is not a file write on every surface** - read its section before promising it.

### First, read what the PM already has

Do not write anything until you have looked. Any PM who has used Claude for a while already has instructions, and the copilot is arriving in someone else's house. Read these and report them as a short list:

- `<workspace>/CLAUDE.md` - their project instructions.
- `<workspace>/.claude/rules/*.md` - project rules files, which may belong to another plugin.
- Their global instructions, which apply in every project they open. In the Code tab that is `~/.claude/CLAUDE.md` and `~/.claude/rules/*.md`. In Cowork it is app-managed and not readable as a file at that path - the copy that loads into THIS session is visible in your own context, so read it from there and say so, rather than reporting they have no global instructions. "I could not find a file" and "they have nothing" are different answers.

Every one of those loads automatically and they are ADDITIVE. Nothing you install replaces any of them, so say what you found rather than writing over it blind. The collisions that actually happen:

- Voice or formatting rules of their own. Every PM gets `pm-voice`; if they already have voice rules of their own, theirs win and you should say so.
- Their own autonomy preferences. A PM who has told Claude to act without asking will find the copilot's gates like friction - explain what the gates are for and let them decide, do not quietly override either instruction.
- File path and output-location conventions.
- Another PMO, productivity or note-taking plugin whose rules do a similar job.

Where there is a real conflict, show both sides, say plainly that the baseline defers to the PM's own version, and offer to record the exception in their file so the next session does not relitigate it.

Do NOT start proposing improvements to their instructions here. That is Stage 8, deliberately after the copilot works - an optional negotiation in the middle of an install is how a setup stalls.

### Then install the three pieces

When you show this to the PM, call out ONE thing in it by name rather than describing the file generally: the project brain rule. It is the behaviour they will notice most and the one that decays fastest if the file is missing - every time the copilot produces an artifact it offers to put it in the project's notebook, and without this file that offer never comes. Worth a sentence, because a PM who knows the behaviour exists will notice when it stops.

**1. The rules file.** `<workspace>/.claude/rules/pm-copilot-baseline.md`. Every markdown file in that folder loads automatically alongside CLAUDE.md, so this works without touching a line the PM wrote, and deleting one file removes the behaviour cleanly - which a merged CLAUDE.md section does not. Put it inside their CLAUDE.md only if they ask, and if they do, wrap it in marked start and end lines.

**2. The reference pack, copied into the workspace.** Copy every file from `${CLAUDE_PLUGIN_ROOT}/references/` to `<workspace>/pm-copilot-references/`. Do not skip this and do not treat it as optional.

Why it is mandatory: the baseline is loaded as workspace rules, which is NOT a plugin context, so `${CLAUDE_PLUGIN_ROOT}` does not expand there. Without a workspace copy, every reference-pack pointer in the always-on layer is a dead path, and the copilot falls back to reciting the standard from memory - the exact failure the pack exists to prevent. `standards-sync` later refreshes this same folder in place.

**3. A pointer block in the PM's GLOBAL instructions.** The safety net for the Stage 2 trap: the global layer loads in every workspace and every project, so this is what keeps the rest findable when they open a single project folder on its own.

**This write is not a file write on every surface. Establish which surface you are on before touching anything.** Found on Anton's own install, 2026-09-03.

- **Claude Code (the Code tab).** The global layer is a real file at `~/.claude/CLAUDE.md`. Append the block, gated like any other write.
- **Cowork.** There is NO file at `~/.claude/CLAUDE.md`. Cowork's global instructions are app-managed and materialised PER SESSION into `.../local_<uuid>/.claude/CLAUDE.md`, rewritten at session start. On a working machine there were 541 such folders each holding an identical copy. **Writing into one of those evaporates when the session ends** - and it will look like it worked, because the write succeeds and the file is there for the rest of the session. Hand the PM the block to paste into the app's own personal-preferences setting instead, and say why.

How to tell, without guessing: check whether `~/.claude/CLAUDE.md` exists as a real file at the home path. If it does, write it. If the only copies you can find live under a `local_<uuid>` session folder, that is Cowork and the layer is app-managed - hand over a paste block. **Never write into a `local_<uuid>` path**, whatever the surface, and never report a pointer block as installed on the strength of a write to one.

This is the same class of problem as `CLAUDE_PLUGIN_ROOT` not expanding outside a skill: a path that is real on one surface and silently absent on the other, where the failure is invisible rather than loud. When a write target is app-managed rather than a plain file, probing costs one call and saves a false green.

Keep the block short, name real resolved paths rather than placeholders, and mark it so it can be found and removed:

```
<!-- PM Copilot pointer - added by copilot-setup, safe to delete -->
## PM Copilot

PM and PMO work runs on the PM Copilot plugin. Its skills show up as `pm-copilot:*` - reach for
one rather than working a PMO step by hand.

- <workspace>/<the task list they actually use> - MY TASK LIST. Read it when I ask what is on my
  plate, and add to it whenever something turns up that needs doing. Project tag per line.
  Never start a second one - this is the list.
- <workspace>/.claude/rules/pm-copilot-baseline.md - how the copilot works, and the process it follows
- <workspace>/.claude/rules/pm-profile.md - my portfolio, aliases and preferences
- <workspace>/pm-copilot-references/ - the PMO standard, the 23 mandatory starting artifacts, templates, conventions
- <workspace>/copilot-feedback.md - alpha log, add an entry when something goes wrong
- PMO Superbrain notebook 158e107b-0f3e-47b9-9566-f481595ab399 - the standard beyond initiation

Before working on any project, read that project's project-context.md and keep it current.
Do not finish a piece of work leaving actions only in the chat - they go in <that same file>.
If the two rules files above are not already loaded this session, read them before PM work.
```

The task list goes FIRST in that block deliberately. It is the file a PM touches every day, and the one whose value collapses if the copilot forgets it exists. Put it where it cannot be skimmed past.

**Name the list the PM actually keeps, not `pm-tasks.md` by default.** Step 10 adopts an existing `TASKS.md` or equivalent rather than starting a rival, so by the time this block is written the real filename is known - use it, and say plainly in the block that it is the only list. A pointer naming a file that does not exist, beside a real list it does not mention, is worse than no pointer: it invites the copilot to create the second tracker the whole rule exists to prevent.

Trim anything already covered by the PM's own instructions. If they have their own voice or formatting rules, the block should not restate them - theirs win, and a duplicate goes stale on the next update.

If the PM chose per-project workspaces at Stage 2, say plainly that writes 1 and 2 repeat per project, and offer to do the ones that already exist. A cheaper alternative worth mentioning: a one-line `CLAUDE.md` in each project folder containing `@` followed by the relative path to the portfolio baseline, which imports it rather than duplicating it.

Before writing anything: show the exact content and the exact target for all three. On a re-run, show what CHANGES rather than the whole file, and never duplicate an existing block.

CHECKPOINT (mandatory): "**Step 8 of 10.** Here is what you already have loaded: [list]. [Any conflicts, and that the baseline defers to yours.] Two things I can install for you: the copilot's rules at [path], and its copy of the PMO standard at [path] so those rules point at something real. Plus a third that is yours to paste: a short pointer block for your global instructions, so this still works if you ever open a single project folder rather than your whole portfolio. Nothing you wrote gets edited or replaced. Here is each one [show them]. Confirm and I will install the two."

Adjust that wording to the surface: in the Code tab all three are writes and it is "three things to install"; in Cowork the third is a paste block and saying otherwise promises something you cannot do. Only act on an explicit yes.

Take a no on the pointer without arguing - say which parts stop working and move on. It only matters if they open a project folder as its own space, so for a PM working from the portfolio root it is genuinely optional, and saying so is more honest than selling it.

## Stage 4 - Step 9: draft the PM's own profile (WRITE GATE)

The baseline is org-wide and identical for every PM. This is the other half: who THIS PM is, what is in their portfolio, and how they want to be worked with. Without it the copilot re-asks the same things every session, and searches for a project under one of the three names it actually goes by.

DRAFT IT, do not interview. By now you have probed their connectors and you know their projects folder, so go and look before asking: list the projects folder, search Drive for project folders, list visible Jira projects, list their Chat spaces. Fill in what you find, then show it and have them correct it. A filled draft with three wrong rows gets fixed in one message; a blank form gets abandoned.

Use `${CLAUDE_PLUGIN_ROOT}/references/pm-profile-template.md` as the shape. Keep its headings even where you could not fill them - an empty section the PM can see is an invitation, a missing one is invisible.

Ask directly only for what no amount of looking can tell you:

- The aliases and codenames each project goes by. Highest-value line in the file and no sweep can infer it. Ask for it explicitly rather than hoping.
- Guided or express mode.
- Which language they want to work in.
- Their lead and their resource manager.

If Stage 3 found portfolio-ish content already sitting in their own CLAUDE.md, do not copy it across - point at it and keep the profile to what is genuinely new.

Write to `<workspace>/.claude/rules/pm-profile.md`, alongside the baseline. Say plainly that this file is THEIRS: the copilot will offer to add to it but never rewrites it, and re-running setup replaces the baseline while leaving this one alone. Tell them to edit it whenever they want.

Nothing client-confidential goes in it. Project and client names, folder links and Jira keys are fine; contract terms and money are not.

CHECKPOINT (mandatory): "**Step 9 of 10.** Here is a profile drafted from what I could find - [show it]. The portfolio rows are my guess from your Drive and Jira, so correct anything wrong, and tell me what else each project gets called. This file is yours, and updates will not overwrite it. OK to write it to [path]?"

## Stage 5 - Step 10: the three working files (WRITE GATE)

Show them, get a yes, write them.

**`pm-copilot-setup.md`** - so later skills and later runs know what happened. **This file was already created back at step 4 as a stub (see Stage 0a) and updated as each step landed - here you are completing it, not starting it.** If it does not exist by now, something skipped the step-4 write and the resume path has been broken for this whole run; create it and say so. Nothing sensitive - no tokens, no client secrets. Just:

- Setup date and plugin version.
- **The highest step number completed, and the date.** Write it as `Reached step N of 10 on [date]`. This is what Stage 0a reads to resume, and it is the difference between "carry on from step 8" and making the PM reconstruct their own history. Update it as each step lands, not only at the end.
- Workspace shape and the projects folder.
- Connector probe results and their date.
- Where the baseline and the reference pack were installed.
- Whether a voice profile exists.
- Anything left unresolved, and what would fix it.

This is what makes re-runs behave, what lets Stage 0a resume cleanly, and what lets `project-router` say "the takeover sweep needs Chat and you do not have it yet" instead of failing halfway through.

**`pm-tasks.md`** - one task list across the portfolio, with Now / Soon / Waiting on someone / Done sections and a project tag on every line.

Look for an existing tracker FIRST. If the PM already keeps a `TASKS.md` or equivalent, adopt it rather than starting a rival - ask which they want to use and then use that one. Two task lists is worse than none.

Explain what it is for, because the value is not obvious: every skill throws off actions - gaps to close with Sales, an artifact to file, a client to chase, a staffing request to raise - and without a list those evaporate when the session ends. This is where they land.

**Seed it with the first three tasks.** A PM who finishes setup has a working copilot and no idea what to do with it, which is where the last two rollouts stalled. So the list does not start empty - it starts with the three pieces of real work that turn setup into competence. Write them as ordinary tagged lines, with the pass condition ON the line, because a task with no pass condition is a suggestion:

```
## Now
- [ ] [Copilot] Map a project I already run - say "get this project into Claude". Pass: name one thing it found that I'd forgotten, AND one thing it got wrong
- [ ] [Copilot] Run this week's PROREP status - say "do my weekly status for <project>". Pass: name what I changed in the draft before posting
- [ ] [Copilot] Build my own voice skill from 8-10 things I actually sent. Pass: a draft reads as mine, and I can say what I'd change in the skill
```

Say two things about them out loud when you write them:

- **The first one is worth doing with whoever gave them the copilot**, not alone. It is the heaviest sweep in the plugin and the most likely to hit a missing connector.
- **"Name one thing it got wrong" is a real pass condition, not modesty.** Most of these skills have never run on a real project. A PM who reports no problems has told us they were not reading, and the corrections are the most valuable thing they can send back.

Then leave them alone. Do not chase them, do not re-offer them every session. They are on the list; the list is where the PM looks.

**`copilot-feedback.md`** - the alpha log, started empty with a short header: what it is for, the plugin version, and the fact that the PM can send it to whoever gave them the copilot.

Explain it in plain terms, because it only works if they know it is there: the copilot is in alpha, and this is where it writes down anything it could not do, anything it got wrong about how Innowise works, and anything they had to correct. They can also just say "log this" at any point. It is their channel back to whoever built it, and the corrections are the most useful part - tell them not to be polite about it.

Nothing about a client goes in that file - no client material, no money, no personal data. Projects by name only.

CHECKPOINT: "**Step 10 of 10**, the last one." Show all three, get a yes, write them.

## Stage 6 - Voice sample (optional, and OUTSIDE the ten steps)

Say plainly that this is an extra rather than a step, and that it is skippable with nothing lost. Do NOT say or imply that the ten steps are over here - step 10 also covers the health check in Stage 7, which has not run yet. "This one is optional and sits outside the ten" is the right framing; anything stronger conflicts with the only place setup is allowed to be called finished.

Offer to capture a short writing sample so drafts sound like the PM rather than like AI. A few real messages or a sent email is enough - a mix of a chat reply, a client message and a status is ideal. Save them as `voice-samples.md` next to `pm-copilot-setup.md`, with a one-line label on each saying the channel and audience. Redact amounts and rates. `pm-voice` reads that file and lets the PM's own habits win over its defaults.

Either way, update the voice line in their `pm-profile.md` so later sessions know whether samples or a personal voice skill exist and where.

Every PM gets `pm-voice` regardless - length by channel, and the English and Russian AI tells. The samples only make it closer to them.

CHECKPOINT: "Voice profile set / skipped. Last thing - the health check, so you can see what actually works. Run it?"

## Stage 7 - The health check and the ONE place setup is finished

Report pass or fail per line, in plain language:

- Baseline rules loaded and visible in this session.
- The reference pack present IN THE WORKSPACE - count the files and name one fact you just read out of the workspace copy. Read it from `<workspace>/pm-copilot-references/`, not from the plugin folder: the workspace copy is the one the always-on layer will actually use, so that is the path worth proving.
- The pack's `synced` date, from that same workspace copy. If it is stale and Atlassian is connected, offer `standards-sync`.
- The pointer block, if they accepted it - verified in the Code tab, PM-confirmed in Cowork. Do not claim it is installed on the strength of a write you could not read back, and never on the strength of a write to a session folder.
- Their profile written, and how many portfolio rows it has. Say that adding the rest of their projects later is a one-line request, not a re-run of setup.
- Copilot skills discoverable - list what you can actually see, not a hardcoded list.
- Connectors, from the Stage 1 probe, with anything still outstanding.
- Scheduled tasks available - `daily-digest` needs them, and so would a morning brief or a risk watch.

### Hand the files over properly

Do not just list them. A PM who does not know what was installed cannot maintain it, and a profile going stale is the most likely way this whole setup quietly stops earning its keep. Walk it once, plainly:

- `.claude/rules/pm-copilot-baseline.md` - how the copilot works, the PMO process it follows, the gates it holds. Ours, not theirs to edit: it gets overwritten whenever they re-run setup after a plugin update, so an edit here is work they will lose. If something in it is wrong, say so and it becomes a feedback-log entry instead.
- `.claude/rules/pm-profile.md` - theirs. Edit it whenever. Add a project, switch from guided to express, correct an alias, add a person. Nothing overwrites it.
- `pm-copilot-references/` - the PMO standard, the 23 starting artifacts, the templates and conventions. Also ours, also refreshed rather than edited. `standards-sync` updates it when the standard changes.
- `pm-tasks.md` - one task list for the whole portfolio, project-tagged. Whenever a skill turns up something that needs doing, it lands here rather than evaporating with the session.
- `<project folder>/project-context.md` - one per project, created the first time they work on it. The copilot keeps it current and says at every checkpoint what it wrote.
- `copilot-feedback.md` - the alpha log. Say "log this" any time, and send the file back.
- A pointer block in their global instructions, so all of the above is still findable when they open a single project folder rather than the whole workspace.

Be straight about the update story rather than implying it is automatic: a new plugin version brings new skills immediately, but the workspace copies of the baseline and the pack only move when they re-run "set up my copilot". Tell them that is one of two maintenance actions, and it is safe to repeat.

The other one, and the only routine breakage in the whole setup: **the NotebookLM sign-in expires every week or two.** Say this out loud at hand-off rather than letting them discover it as a fault. Give them the symptom and the fix in one line - when the project brain starts erroring, say "fix my NotebookLM" in the Code tab; it often recovers without a sign-in, and when it needs one, the browser part is theirs. A PM who has not been told this reads a routine expiry as the copilot breaking.

Then the two habits that keep it working, said out loud: tell the copilot when the profile is wrong, and expect the context line at every checkpoint. If either stops happening, something has broken and it is worth flagging rather than living with.

Then name the next move, and pick the right one:
- A brand new or handed-over project -> run `project-router` on it.
- A project already running that they inherited -> run `map-existing-project`; it sweeps Drive, Chat, mail, Jira and Confluence and works out what they have.
- Not sure -> `project-router` routes them either way.

And one offer that fits every PM whatever their projects, made once: `daily-digest`, a daily digest of their Chat spaces, mail and meeting notes, set up in a few minutes and then arriving by itself. If they say not now, drop it.

And one habit, said once: before closing a chat, say "wrap up". `wrap-up` puts the session's tasks, project facts and a resume note where the next chat will find them, because a new chat starts knowing nothing.

### This is the only place setup gets called finished

Everywhere else in this flow says the position and what is left. Here, and only here, say it is done - and say it unambiguously, because a PM who is not told will assume there is more and stop trusting the count.

Also record it: write the completion into `pm-copilot-setup.md` so a later run of this skill reads "all ten steps done on [date]" rather than re-deriving it from which files exist.

CHECKPOINT: "**All ten steps done - your copilot is set up.** [Health check results.] [Next move.] Want me to walk through it now on a real project, or shall I first suggest a couple of additions to your own instructions?"

## Stage 8 - Suggest additions to their own instructions (optional, OUTSIDE the ten steps, offer once)

Deliberately last. By this point the copilot works and the PM has seen what it does, which is when advice about their own setup is worth taking rather than an obstacle to getting started. Offer it once; if they decline, drop it and do not raise it again.

Most useful for a PM whose instructions are thin or empty. Read `${CLAUDE_PLUGIN_ROOT}/references/instructions-layers.md` - it carries the four-file routing rule and the list of what a PM's own instructions commonly lack.

Check what Stage 3 found against that list, then propose the gaps. ROUTE each suggestion to the right file rather than dumping everything in one place:

- Copilot or PMO process behaviour is already in the baseline. Do not propose adding it to their file - a second copy goes stale on the next update. Say it is covered and where.
- A fact or preference about them or their portfolio goes in their profile, not their CLAUDE.md.
- A general working preference that would still apply with the copilot uninstalled goes in their CLAUDE.md. The usual candidates: plain ASCII for a Windows workspace, one line about how they write, their working language, a tools-and-access note, how much they want explained, and somewhere for corrections to accumulate.

Show every proposed edit as a before-and-after they can read in a few seconds. Never apply one without a yes, and take a no without arguing.

Keep it to two or three concrete suggestions. This is not a CLAUDE.md audit, and a PM who wanted their instructions reviewed would have asked.

## When a desktop-access connector legitimately comes up

Only raise this if the PM is actually blocked, and only on Windows.

If they followed this skill and are in the Code tab, they already have a real shell on their own machine and do not need a desktop connector for anything here. Check which surface they are on before suggesting one.

Where it legitimately comes up is a PM working in Cowork who hits something the sandbox cannot reach. Cowork's shell is a Linux VM, so it has two blind spots on a Windows laptop: it can see a stale snapshot of files in a synced folder, and it cannot touch anything on the Windows side - including the NotebookLM sign-in. The cheap fix for the sign-in is to move that one step to the Code tab rather than installing anything. If they are genuinely stuck on the file-visibility problem, `Windows-MCP` is already in the Innowise connector list and they can add it themselves.

If you suggest it, say the trade-off in the same breath - do not present it as a neutral convenience:
- It gives a real shell on their laptop: PowerShell, file system, processes, and UI control. Much broader than any other connector here.
- `map-existing-project` reads a lot of material in one pass, and although nearly all of it is internal, some originated outside Innowise (client mail, client-authored specs). A broad read of other people's text alongside a full shell is a combination worth a deliberate choice.
- Recommend turning it off again once the specific blockage is cleared, rather than leaving it on as a convenience.

There is no equivalent in the Innowise list for macOS. A Mac PM who is blocked does that step by hand; say so rather than sending them to install something unvetted.

## Notes

- Safe to re-run, and Stage 0a means a re-run resumes rather than restarts. Detect what is already there and offer to update; never duplicate a block.
- The minimum that leaves a working copilot is steps 5 to 8 plus 10: connectors, the always-on layer, and the setup note that other skills read. Skipping the profile (step 9) costs re-asked questions; skipping the setup note means `project-router` cannot tell the PM in advance which parts of a sweep will be blind, and Stage 0a loses its resume point. If the PM is in a hurry, say which steps you are skipping and that the count is now shorter - do not silently drop one and keep saying "of 10".
- Connector auth, scheduled tasks, the voice profile and the projects folder are per-PM and per-machine. They do not travel inside the plugin - that is expected, not a limitation to apologise for.
