# PM Copilot - install, use, update

The PM Copilot is a set of Claude skills for running Innowise PMO delivery work: the initiation
standard step by step, the weekly PROREP status, the risk register, the project notebook, and
answers to "how do we do this here" from the live standard. It drafts, checks and computes. You
judge, decide and send.

This guide is everything you need to install it on your own, on Mac or Windows. Where the two
differ, the step says Mac or Windows. Plan about an hour the first time, most of it clicking
through sign-ins.

**Stuck at any point? Message Anton Oparienko in Google Chat.** Say which step you are on and what
you see.

The same guide is on Confluence and in the Drive folder as "PM Copilot - START HERE", and both are
updated with every release.

## Words you will meet

- **Claude Desktop** is the Claude app on your laptop. Everything here happens in it, not in the
  browser.
- **The Code tab** is where setup runs. Open it with the **</>** button at the top right of the
  Claude window; the speech-bubble button next to it takes you back to chat.
- **Customize** is in the left sidebar of the Claude window. Plugins, extensions and connectors
  are all installed from there.
- **The plugin** is the copilot itself: its skills and the PMO standard. One file,
  `pm-copilot.plugin`. A **skill** is one thing the copilot knows how to do, like a weekly status
  or a risk register - you never call them by name, you describe what you need.
- **Extensions and connectors** give the copilot access to your tools. The three extensions
  (Google Workspace, Google Sheets, NotebookLM) come in the zip. Atlassian (Jira and Confluence) is
  a connector you add from Claude's own list.

## What is in the Drive folder

The folder: https://drive.google.com/drive/folders/1A3aIWCtIzj-JbVrxMqzbhD4vIY61q1nV

| | What it is |
|---|---|
| PM Copilot - START HERE | This guide |
| `PM-Copilot-latest.zip` | The copilot. Always the newest version, under the same link |
| `PM-Copilot-Field-Guide.pdf` | What each skill gives you and what to type. Read it once you are set up |
| `CHANGELOG.txt` | What changed in each version, newest first |
| `versions/` | Older builds. Ignore it unless you were told to use one |

If the folder says "Request access", you are not in the PM group yet - message Anton.

## Before you start

**1. Get a Claude license.** Request it through Service Desk. The PMO "AI Toolset" page has the
Service Desk link and a request template to copy:
https://innowise-group.atlassian.net/wiki/spaces/PMO/pages/5288362280/AI+Toolset

- Use the Claude template. You can request BlueDot in the same ticket.
- As approver, name Alexey Gamanovich, head of PMO. Service Desk sorts out the rest of the routing.
- Read the conditions on that page too - it lists the Anthropic courses to complete and a note
  about VPN.

A ticket sent on a Friday is usually handled on Monday, so request it before you plan to install.
The invite arrives by email; open it and accept. If you see two Innowise organisations when you
sign in, message Anton before picking one.

**2. Install Claude Desktop.** Download it from https://claude.ai/downloads - choose the desktop
app for your system, not the browser version. Sign in with your @innowise.com account. If the
installer refuses to run, run it as administrator.

**3. Open the Code tab once, and let it install Git.** Click **</>** at the top right of the Claude
window. The Code tab needs Git before it can start.
On a fresh install, Claude sees Git is missing and walks you through installing it - follow what
it says. If it does not offer:

- Windows: download Git from https://git-scm.com/downloads and click through with the default
  options.
- Mac: open Terminal (press Cmd and Space, type Terminal, press Enter), type
  `xcode-select --install` and press Enter. A window asks to install the command line developer
  tools - click Install and wait for it to finish.

Then quit Claude completely and reopen it (how to quit: step 3 of the install below). Claude does
not notice Git until it restarts.

**4. Make one folder for Claude, and create a Claude project on it.** A Claude project is Claude's
way of remembering a folder and its settings - not one of your client projects. One folder for
everything: the copilot creates a subfolder for each of your client projects inside it.

- Windows: a folder under your user folder, or on another drive. Not a drive root, and not your
  whole Documents folder.
- Mac: avoid Documents if it syncs to iCloud. A folder on the Desktop is fine.

Claude refuses your home folder itself with "protected locations, invalid path, choose a more
specific folder". Expected - pick a folder one level deeper.

Then in Claude: Home, Projects, create a new project, choose that folder, and click Always allow.
The warning that Claude can read and change files in there is the normal one; accept it.

This folder stays on your laptop and is not shared with your team. Sharing still happens through
Drive, NotebookLM and Confluence.

**5. Download the zip and unpack it.** From the Drive folder at
https://drive.google.com/drive/folders/1A3aIWCtIzj-JbVrxMqzbhD4vIY61q1nV download
`PM-Copilot-latest.zip` and unpack it somewhere you can find it. You will pick single files out of
it in the next steps. Never upload the zip itself anywhere - it is rejected with a confusing
error.

## Installing - ten steps

| | Step | Where |
|---|---|---|
| 1 | Install the plugin | Customize |
| 2 | Install the three extensions | Customize, or double-click on Mac |
| 3 | Quit Claude and reopen | - |
| 4 | Say "set up my copilot" | Code tab, in your project |
| 5 | The Google sign-ins | Code tab + browser |
| 6 | Add Atlassian | Customize + browser |
| 7 | NotebookLM | Code tab + browser |
| 8 | The copilot's rules and its copy of the PMO standard | Code tab |
| 9 | Your profile | Code tab |
| 10 | Task list, feedback log, health check | Code tab |

Steps 4 to 10 happen in one chat - the setup chat - and the copilot tells you which step you are on
every time it stops. Getting the connectors working is step 7, not the end: steps 8 to 10 are what
make the copilot pick the right skill, so do not stop at 7.

### 1. Install the plugin

In Claude: Customize, then Plugins, then Add, then Upload. Choose `pm-copilot.plugin` from the
unpacked zip.

You should now see PM Copilot in your plugins list.

If the Plugins screen shows a directory of organisation and partner plugins with no upload option,
you are on the browse view - the upload is behind the Add button. If you get "zip must contain a
.claude-plugin/plugin.json file", you picked the zip instead of the `.plugin` file.

### 2. Install the three extensions

Three files from the same unpacked zip. In Claude they show under these names:

| File | Shows in Claude as | Gives the copilot |
|---|---|---|
| `pmc-gws.mcpb` | PM Copilot - Google Workspace | Gmail, Drive, Calendar, Chat, Docs, Slides, Tasks, Contacts |
| `pmc-sheets.mcpb` | PM Copilot - Google Sheets | Spreadsheets |
| `pmc-nlm.mcpb` | PM Copilot - NotebookLM | NotebookLM, the project notebook |

**Mac:** double-click each file, and click Install when Claude asks.

**Windows:** double-clicking opens Notepad instead, so install them from Claude: Customize,
Extensions, Advanced settings, Install extension, and pick the files one at a time. Some versions
label the same screen Settings, Extensions, Advanced settings, Extension Developer, Install
Extension. It sits behind a developer-tools warning; that is expected for internal Innowise
extensions.

You should now see all three under Extensions. Claude may say it cannot reach an MCP server - that
is expected until the next step.

### 3. Quit Claude completely and reopen it

Closing the window is not enough.

- **Windows:** click the ^ arrow at the right of the taskbar, right-click the Claude icon, choose
  Quit.
- **Mac:** Cmd-Q.

Extensions only load when Claude starts.

### 4. Say "set up my copilot"

Open your project (Home, Projects, the one you made) and switch to the Code tab. The Code tab asks
which folder to work in - pick your Claude folder, the same one the project uses. Type "set up my
copilot".

**Check you are in the project.** If Claude offers to "make a project so Claude can use the same
context", you are outside it - go back to Home, Projects, open your project and start the session
from there. What setup installs only loads in chats inside the project. The copilot also checks this at the
start and tells you if you are outside it - if it does, fix that before going on.

The copilot checks the "Before you start" items, asks whether this is a first setup, and then
checks each connector with a real call. From here on it tells you which step you are on.

If you close this chat, find it again in your recent chats, or open a new one in the project and
say "continue my copilot setup" - it picks up where you stopped.

### 5. The Google sign-ins

Google asks twice - once for the Workspace extension, once for Sheets. Both want your
@innowise.com account. Approve everything it asks for.

**This is the step that stalls.** On several machines the browser tabs never opened and every
connector came back "not authorized" or "not found". Nothing was wrong. In order:

1. If a Google tab opened and you closed it, or it timed out, tell the copilot "retry".
2. Quit Claude completely (install step 3), reopen it, open the setup chat and ask the copilot to re-check
   your access. New Google tabs open; approve them.
3. If it still fails, see "An extension installed but will not start" under "If something goes
   wrong".

Claude may also suggest its own connectors here - Gmail, Google Calendar, Asana and others. You do
not need them; the copilot's extensions cover the same ground. Atlassian is the one exception, and
it is the next step.

### 6. Add Atlassian

In Claude: Customize, Connectors, then browse or add a connector, find Atlassian and click Connect.
A web page opens: sign in with your Innowise account and choose the site
`innowise-group.atlassian.net`. Finish that page and come back to Claude - it does not complete on
its own.

You should now see Atlassian listed as connected. It gives the copilot Jira, Confluence and the
live PMO standard.

### 7. NotebookLM

The longest step, about ten minutes the first time. It installs one small helper on your machine.

In the setup chat, say "fix my NotebookLM setup and login". The copilot walks you through it and
stops at each point:

1. **Git.** If it is still missing, the copilot points you at the install from "Before you start".
2. **uv**, a small helper. The copilot installs it itself. You will get a few permission prompts;
   `Allow once` is fine.
3. **Sign in.** A browser window opens. This part is yours - the copilot cannot see the window or
   type into it, so stay at the keyboard. Use your @innowise.com account. If it picked the wrong
   Google account, say "I need a different email" and it redoes the sign-in.
4. **Restart.** NotebookLM often still shows as missing right after a successful sign-in. Quit
   Claude completely and reopen it, then open the setup chat and tell it NotebookLM is done.

If the browser sign-in will not open or keeps failing, sign in from a terminal instead: open
PowerShell (Windows: Start, type PowerShell) or Terminal (Mac: Cmd and Space, type Terminal), type
this and press Enter:

```
uv tool run --from notebooklm-mcp-cli==0.15.4 nlm login
```

A browser window opens for your @innowise.com account. If the terminal first asks whether to keep
the login "Protected" or as a "plain file", choose plain file - it is what the copilot's own sign-in
makes. Then restart Claude as in point 4. (If the terminal says `uv` is not found, close it and open
a new one - `uv` is installed during this step. Type the line exactly as above: a plain `nlm login`
does not exist on your machine, whatever an error message suggests.)

If you run out of time here, the rest keeps working - only the project notebook is missing, and
setup offers to skip it and carry on.

### 8. The copilot's rules and its copy of the PMO standard

The copilot writes two things into your Claude folder: the rules it works by, and a copy of the
PMO standard and its mandatory artifacts, so it works from the standard rather than from memory.
It shows you each file before writing it, and changes nothing you wrote.

### 9. Your profile

It drafts your profile from your Drive and Jira: your projects, what each one is also called, your
lead, your resource manager, and whether you want it to check in at every step. You correct the
rows rather than fill in a form. The other names matter: without them the copilot searches for a
project under one name when your team calls it another.

It also offers to save a few messages you actually sent, so its drafts sound like you. The profile
is yours - edit it whenever, and nothing overwrites it.

### 10. Task list, feedback log, health check

A task list for your whole portfolio, a feedback log, and a final check that reports what works and
what is still missing. The last thing it says is what to do first on a real project - when you see
that, setup is finished.

## Updating to a new version

`CHANGELOG.txt` in the Drive folder says what changed, newest first. The zip under the same link is
always the newest version.

1. Download `PM-Copilot-latest.zip` again and unpack it.
2. Upload the new `pm-copilot.plugin` as in step 1. It replaces the old version; there is nothing
   to remove first.
3. Reinstall the three extensions only when the changelog line says "Reinstall the extensions".
   Most versions do not. When one does, install them as in step 2, then quit and reopen Claude.
4. Start a new chat in your project. A chat that was already open keeps the old version.
5. Say "set up my copilot". It refreshes the rules and the copy of the PMO standard in your folder,
   which the plugin update does not touch. It takes a minute and leaves your profile alone.

## How to use it

Work from your project in Claude, in the Code tab - it is what setup used and it covers everything
the copilot does.

**You do not launch skills.** Write to Claude in normal words and describe your situation - "I got
a handover for a new project", "time for my weekly statuses", "the client just told me something
that worries me" - and it picks the right skill.

Read `PM-Copilot-Field-Guide.pdf` from the Drive folder once. It lists every skill by the situation
you are in, with what you get and what to type. When you are not sure whether there is a skill for
something, the answer is usually yes. (The same guide is in the zip as an HTML file.)

Two habits worth starting early:

- Name the project. The copilot knows your portfolio and the other names each project goes by.
- Say "log this" when it gets something wrong. It keeps a feedback log for exactly that.

## What you just installed

| | What it gives the copilot |
|---|---|
| The plugin | The skills, the PMO standard, the rules it works by |
| PM Copilot - Google Workspace | Gmail, Calendar, Drive, Docs, Slides, Chat, Tasks, Contacts |
| PM Copilot - Google Sheets | Spreadsheets - WBS, resource plan, checklists, P&L |
| PM Copilot - NotebookLM | The project notebook, which is a mandatory PMO artifact |
| Atlassian | Jira, Confluence and the live standard |

The copilot works partly without some of these and tells you what it cannot do rather than
pretending.

You do not need Claude's own Gmail, Calendar or Drive connectors. The Workspace extension covers
them and adds Google Chat, sharing and permissions, and editing Docs and Slides. The Sheets
extension covers spreadsheets, which Claude has no connector for. If you already have Claude's own
ones on, you can leave them or turn them off.

The extensions need no admin rights. The first time each one starts, it downloads its own runtime,
so it needs internet access then.

## What it asks before doing

Reading is safe. Writing - anything that creates, changes or deletes something in Drive, Jira,
Confluence, Sheets or mail - comes to you first, with what it intends to do, unless you have set
that action to always allow. You can say no or tell it to wait.

In Customize, Connectors, click a PM Copilot connector to see every action it can take. Each can be
set to always allow or to ask each time. Setting the read actions you see constantly to always
allow saves a lot of clicking. **Keep the write actions on ask for your first weeks**, while you get
used to how Claude works; switch individual ones to always allow once you are confident with them.

In the Code tab, prompts say `Allow once` or `Allow always`. Always applies to that one command,
not to everything.

## Which model

Leave it on the default, Sonnet. It is enough for almost everything the copilot does.

Opus is the strongest model and uses your allowance much faster. Worth it for a heavy pass across a
whole project, wasteful for daily work. Settings, Usage shows how much you have left.

## The one thing that will break later

**The NotebookLM sign-in expires every week or two.** That is normal. You notice it as the project
notebook starting to error while everything else works. Open the Code tab and say "fix my
NotebookLM". It often recovers without a sign-in; when it needs one, a browser window opens and you
sign in. Or run the terminal sign-in from install step 7.

## If something goes wrong

**First try:** say "my copilot setup is broken". The copilot tests each connector, works out which
problem you have, and tells you the fix. If that does not help, message Anton Oparienko in Google
Chat.

### Connectors show as not authorized and no Google tab ever opened

The most common one. Quit Claude completely, reopen it, and ask the copilot to re-check access. See
step 5.

### You installed an extension but the copilot cannot see it

Quit Claude completely and reopen it - extensions load only at startup. If it is still missing, it
installed but did not start: see the next one.

### An extension installed but will not start

On its first start it downloads its own runtime, which can take a couple of minutes and looks like
nothing is happening. On a locked-down network the download fails silently. Try another network,
or ask IT to allow `astral.sh` and `github.com/astral-sh`.

### Google rejects your sign-in

Check you are using your @innowise.com account. Personal Google accounts are rejected by design.

### Spreadsheets work but Drive does not, or the other way round

They are two extensions with two sign-ins. Ask Claude for the missing one directly ("list my recent
emails") and complete the browser step.

### The copilot uses Claude's own Gmail or Drive connector instead

Tell it "use the PM Copilot connectors". If it keeps doing it, turn Claude's own ones off in
Customize, Connectors.

### NotebookLM is the only thing failing

Either the regular expiry above, or setup never finished. Both are fixed from the Code tab, not
from Cowork.

### NotebookLM signed in but still shows as missing

Quit Claude completely and reopen it, or start a new chat.

### NotebookLM says you are signed in, but the notebook still fails

Usually the sign-in is reusing an old saved login. Say "fix my NotebookLM" in the Code tab. The
copilot checks with a real notebook call, and if that fails it sets the old login aside (it does not
delete it) and opens a fresh sign-in for you. A message saying "Authentication valid" next to "Notebook
count unavailable" means the same thing - the sign-in did not work.

### You signed in to NotebookLM with the wrong Google account

Say "I need a different email". It sets the old sign-in aside and opens a fresh one, where you
sign in from scratch with the right account.

### After an update, the copilot does not know a new skill

Your chat started before the update. Start a new one.

### Everything is erroring and none of this fits

Claude itself has bad days. If errors are broad and strange rather than specific, wait a while
before debugging your own setup.

### Nothing will install at all

Some laptops block downloads. Ask IT to allow `astral.sh` and `github.com/astral-sh`, or message
Anton to go through it with you. Without the Google extensions, Atlassian alone still covers part
of the work, and the copilot says which skills are affected.

## Feedback

Setup starts a `copilot-feedback.md` file in your Claude folder. When the copilot cannot do
something, gets a fact about Innowise wrong, or you have to redo its work, it writes that down, and
you can say "log this" any time. Send the file to Anton Oparienko. The blunt entries are the most
useful.

## What stays with you

The plugin carries the skills and the knowledge. Your sign-ins, your profile, your saved writing
samples and your Claude folder are yours, per person and per laptop.
