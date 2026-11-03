---
name: correspondence-log
description: Collect a project's client email into one Google Doc so it is searchable by more than one person, then keep it collecting. THE TRIGGER MOST OFTEN MISSED - the PM is digging through their own inbox for something this log should already answer, or somebody is arguing about what was agreed and the answer is in a thread nobody else can reach. Also - "collect the project correspondence", "get the client emails into the brain", "set up email collection for this project", "where is the email where they agreed to X", "I cannot find the thread", "the client says we never agreed that", "correspondence log", "put the project mail into NotebookLM", "is my correspondence log current". Does the back-collection of history and the ongoing capture, both into the same Doc, holding out money, contract text and live credentials per message so the log stays safe to put in the project brain. It is a findability tool and NOT legal evidence - it does not preserve original headers and must never be offered as proof.
---

# correspondence-log - the project's mail, findable a year later

A project's real decision trail is in one person's inbox, searchable by that person only, in a
tool that ranks by recency and forgets structure. The question that gets asked a year later is
"when did they confirm this, and in what words" - and the honest answer today is usually "give me
twenty minutes and I will go and look".

This skill moves that trail into one Google Doc per project, which the team can read, the next PM
inherits, and the project brain can answer from.

## What this is not - say it once, early, and never blur it

The log holds a READABLE COPY: body text, sender, date, subject, and a pointer back to the
original. It is not the message. It carries no DKIM signature, no `Authentication-Results`
verdict and no `Received` chain, so it cannot show that a message is authentic or unmodified.

If the PM is heading into a dispute, a claim, an audit finding or anything with a lawyer near it,
the evidence is the original mail sitting in the mailbox plus whatever retention the org runs
centrally. This log is how you find WHICH message to go and get. That is a real job and it is
worth doing, but it is not the same job.

Say this plainly the moment a PM starts treating the log as proof. Nothing else in this skill
matters as much.

## The one rule that runs through everything: never report an unearned zero

A sweep that read nothing and a mailbox with nothing in it produce the same sentence - "no new
messages" - and only one of them is true. Every count in this skill is therefore reported in pairs:
what you READ beside what you FOUND. "Fetched 43, 2 new" is checkable. "0 new" is not.

This is not a style note. It is the failure this skill exists to prevent, arriving from the inside:
a log that quietly stops collecting looks exactly like a project that has gone quiet, and nobody
finds out until the missing message is the one that matters. Anything built to run unattended
(see `automate`) must be incapable of reporting a zero it did not earn - it fails loudly instead.

## Three modes

| Mode | The PM said something like | What you do |
|---|---|---|
| **collect** (write) | "collect the correspondence", a first build, or catching up since the last sweep | sweep the mailbox, classify, append new messages to the Doc |
| **automate** (change) | "set it up so it keeps happening", "I do not want to ask for this every week" | get an arrival-triggered flow running so the PM stops needing this skill |
| **review** (audit) | "is the log current", "did we capture everything", nobody has swept in weeks | coverage and staleness against the live mailbox, report the gap |

The middle mode is not the usual one. Nobody hand-edits a correspondence log the way they edit a
risk register, so the change mode here is about the machinery that keeps it filling rather than
about one entry.

Reading the log needs no mode. If the Doc is already a brain source, `project-brain` in `ask` mode
is the better route - it searches the whole project's knowledge rather than one document.

## Before anything: find the log

Read the project's `project-context.md` for the Doc ID. Otherwise search Drive for
`<Project> - Correspondence Log` using every alias in `pm-profile.md`, because a project's
documents are often named for the client while the PM calls it by the product.

Never start a second one. Two correspondence logs for one project means two different windows of
mail, both looking complete, and nobody can tell which one holds the message they need.

**Where it goes is a decision, not a default.** `${CLAUDE_PLUGIN_ROOT}/references/pmo-conventions.md`
puts A-block working documents in `<Project> - General`, and General is shared with the team AND
the client. A log of client mail is mostly mail the client already has - but the moment it carries
an internal thread, a partner's mail, or a message about the client rather than to them, General
is the wrong home. Sensitive is also wrong; that folder is money, legal and contracts.

So ask once, name the consideration in one line, and record the answer in `project-context.md`.
Do not quietly file it in General and hope. If the PM has no strong view, propose General/PM and
say what the log must then never contain.

## Build the query before you sweep - this is the part that goes wrong

The query decides whether the log is complete, and an incomplete log is worse than none: the gaps
get read as selection. The PM knows who is on the project, so SHOW THEM THE QUERY before running
it.

Hard rules, each of which has produced a silently empty sweep:

- **Never filter on `category:primary`.** External client threads land outside Primary, and sent
  mail carries no Primary label at all, so a Primary filter returns close to nothing and reports
  it as a quiet project.
- **Never filter on `to:me`.** A PM is frequently on a thread without being on the To: line.
- **Never scope by keyword, and on a product project this is actively harmful.** If the product
  emails anyone, its own notifications carry the project's names: verification codes to the team's
  `+alias` test accounts, cloud budget alerts, payment-provider webhooks, tracker automation. On one
  real project a keyword sweep came back roughly 90% product noise while the participant-scoped
  sweep was clean. Scope on WHO, not on what the mail is about.
- **Sweep BOTH directions.** The PM's own sent mail is half the record and it is where the
  commitments we made live. `from:me` is in scope, not excluded.
- **Scope by people and domains, then subtract noise.** Denylist the automated senders rather than
  allowlisting a Gmail category: `jira@`, `confluence@`, Drive share notifications, Docs comment
  notifications, Calendar and Meet notifications, `no-reply@`, internal automation addresses.
- **Several client domains is the normal case**, not the exception - an agency plus the end
  client, or a client whose staff use two domains. Get them from `project-context.md` stakeholders
  and include all of them.
- **A client on a personal address has no domain to scope on.** Small clients and founders often
  use a personal Gmail, so the participant LIST is the query and it decays as people join. Record
  every address in `project-context.md`, and whenever a sweep surfaces a new client-side person,
  add them there and say you did.

Query shape, filled from the project's own facts:

```
(from:@clientdomain.com OR to:@clientdomain.com OR cc:@clientdomain.com
 OR from:named.person@other.com OR to:named.person@other.com)
after:YYYY/MM/DD
-from:jira@ -from:confluence@ -from:no-reply@google.com
```

**A sweep that comes back near-empty on a live project is a broken query, not a quiet project.**
Before reporting nothing found, run a deliberately broad sanity query for the same window and
compare the counts. If the broad one is much larger, the scoping is wrong - fix it and say so.

In triage, drop calendar Accepted/Declined/Tentative replies and out-of-office auto-replies. Be
careful with verification codes: a provider's own OTP mail is noise, but a client FORWARDING one to
report a bug is project correspondence. Judge it by who sent it, not by the subject line.

## What never reaches the body - per message, never per thread

The Doc is destined for the project brain, so the hold-out list in
`${CLAUDE_PLUGIN_ROOT}/references/pmo-conventions.md` applies to every single message that goes in.
A held-out message still appears - date, sender, subject, pointer - with the body replaced by one
marked line. Three grounds:

**Money.** Rates, margin, invoices, deposits, budget caps, salary, client currency figures.

**Contract text.** SoW and NDA language, exhibits, amendments, liability and governing-law clauses.
Personal staffing data gets the same treatment.

**Live credentials - the tier the money rule misses, and on some projects the bigger exposure.**
Clients paste passwords, API keys and one-time codes into mail, and those would otherwise flow
straight into the project's knowledge container. Split this one two ways, because a single-tier rule
is wrong in both directions:

- a secret VALUE is present -> hold the body. `Password: ...`, "the code is 481920", an API key or
  access key, a private-key block, a bare six-digit line, an attachment named like a credential file.
- credentials are merely DISCUSSED -> keep the body, and mark the entry. "the account is protected
  by 2FA", "I will send the credentials separately", step-by-step instructions for generating an
  API key.

On one real project that split was 8 withheld against 36 kept-and-flagged. Holding out all 44 would
have gutted an entire access negotiation for no safety gain.

**When a sweep turns up live credentials, tell the PM as a finding in its own right.** It is
usually news, nobody has rotated them, and it matters more than the log does. Report it separately
rather than burying it in a hold-out count.

**Classify each message on its own.** One thread routinely carries a costing and then, two replies
later, a plain scope confirmation. The confirmation is exactly what this log exists for; the
costing must never reach the brain. A thread-level rule either loses the first or lets through the
second.

When unsure, hold it out. Report the held-out count and its grounds at the checkpoint, so the PM
can see the rule fired and can check it if the number looks wrong.

## What an entry looks like

NotebookLM answers from a stretch of text and cannot see the document's structure, so every entry
has to repeat its own metadata. An entry that relies on a heading four pages up is invisible to it.

```
--- 2026-09-07 14:28 | D. Whitfield (client) to me | Re: phase 1 task list
Participants: d.whitfield@northwind.example, pm@innowise.com
Message-ID: <AS8P190MB1589A1FF616B48398A6C1592B22@AS8P190MB1589.EURP190.PROD.OUTLOOK.COM>
Open: https://mail.google.com/mail/u/0/#search/rfc822msgid%3AAS8P190MB1589A1FF616B48398A6C1592B22%40AS8P190MB1589.EURP190.PROD.OUTLOOK.COM

Yes, that works for us. Send over the full task list and we will line it up
against the phase 1 scope on our side before Thursday.
```

The rules that make it usable:

- **Chronological, oldest first, newest appended at the end.** A reader and a model both want the
  story in order.
- **Trim the quoted history.** A twenty-message thread logged in full says the same things twenty
  times, and the repetition actively degrades what the brain retrieves. Cut at `On <date> ...
  wrote:`, at lines beginning `>`, at `-----Original Message-----`, and at a `From: ... Sent: ...`
  block. Also cut confidentiality footers, which are boilerplate the sender never wrote.
- **Trimming must not empty a message.** Two cases bite. A signature block at the very start means
  the body was only a signature, which is genuinely empty - but a bare forward, where the sender
  wrote nothing above `Begin forwarded message:`, is NOT empty and must not be dropped: record a
  one-line marker naming who forwarded what. And never let a signature cut consume an entire body;
  require content before it.
- **Strip the external-sender banner IF THE MAILBOX HAS ONE.** Some gateways tag inbound mail with
  something like `[External Email Communication]` that the sender never wrote; strip it, and say
  once that you did, so it is never read back as the client's own words. Check before asserting it
  - on one Innowise Gmail account the tag does not exist at all, and claiming to have stripped
  something you never saw is its own small lie.
- **Plain text, not HTML, and normalise PUNCTUATION only.** Smart quotes to straight, em dash to
  " - ", ellipsis to "...", emoji dropped. Say once that you do this: it is the only edit made to
  the sender's words, and the rule above promises not to touch them. **Do not ASCII-fold letters.**
  The tooling constraint is narrower than it looks - it is PowerShell that mangles non-ASCII, not
  the Doc, not Python, not the editor - so folding a client's name or a message written in another
  alphabet damages the record for no safety gain. On a project whose mail is not all English, write
  the local file as UTF-8 rather than ASCII and keep the letters intact.
- **Keep the Message-ID as text as well as in the link.** The link form depends on which Google
  account index the reader is signed into; the Message-ID does not, and it is what finds the
  message from any mailbox that holds it. Worth clicking one of them on the PM's own account the
  first time, to confirm the form resolves there.
- **A held-out message is one line** with no body, marked `[body withheld - commercial]`,
  `[body withheld - contract text]` or `[body withheld - live credential]`.
- **Attachments**: name them, and link a Drive copy if one exists. Never paste their content. Drop
  inline signature images (`image001.png`, `Outlook-*`) rather than listing them as attachments.

## Mode: collect

**Stage 1 - scope and window.** Read `project-context.md`. Build the query. Show it, with the
domains and names used and the denylist. Say the window: a first run goes back as far as there is
mail, and you report the earliest date FOUND rather than assuming a start date; a later run starts
from the cursor. STOP here - a wrong query wastes the whole sweep.

**Stage 2 - sweep and classify.** Fetch, dedup, classify each message on its own, trim the quotes.
Report: how many messages were FETCHED, how many are new, how many held out and on what grounds,
the date range, and the biggest threads by message count. Show ONE sample entry in full, so the PM
sees the format before it is multiplied by four hundred. STOP.

Two mechanical facts that have each cost a run:

- **Gmail's per-minute quota returns a 403 PER MESSAGE inside an otherwise successful batch.** It
  bites around 250 full fetches. A batch comes back half empty and reads as fine, so verify every
  id you asked for came back, and re-fetch the gap a minute later rather than trusting the first
  pass.
- **Dedup BEFORE fetching bodies where you can.** A weekly run typically re-reads several messages
  it already has, because the window overlaps the cursor on purpose. Fetching every body to find
  that most were already logged is the same quota the backfill runs out of. Pull metadata first,
  drop what the log already holds, then fetch full bodies only for the survivors.

**Stage 3 - write.** Gated, like any write to a shared store. Say exactly what is about to be
appended and what is held back, then append. Update the cursor line.

**Creating the Doc on a FIRST build.** A back-collection runs to hundreds of KB, which used to be a
dead end - every Workspace MCP tool taking a file path was unusable, and the workaround was to hand
the PM the file and have them drag it into Drive. **That is over, fixed in workspace-mcp 1.27.0 and
proven by live writes on 2026-09-18.** `import_to_google_doc` with a `file_path` creates a native
Google Doc from a local file in one call. Never retype the content in chunks through context, and
never ask the PM to do a job the tool now does.

Two things about it that are still true. The import tools only read from
`%USERPROFILE%\.workspace-mcp\attachments` unless `ALLOWED_FILE_DIRS` is set, so copy the file
there first rather than importing from the project folder. And Drive truncates the file name at
50 characters, so name it before the import, not after.

**Check which tab the content landed in.** A Doc created by dragging a file into Drive keeps its
content in tab `t.0`, and every later Docs API call must then pass `tab_id` or it reports an empty
document and an append silently lands nowhere. Whether an imported Doc behaves the same way is not
established - so read the structure back once, find where the content actually is, and record that
in `project-context.md` beside the Doc id. Verify the first append by reading the length back.

**Stage 4 - the brain.** Hand to `project-brain` in `feed` mode: first time, add the Doc as a Drive
source; every later run, re-sync it. A native Google Doc is the right format because it can be
re-read in place rather than re-added - but re-reading is a SYNC, not something that happens on its
own. Say that out loud, because "it is a Doc so the brain stays current" is the obvious wrong
inference and PMs make it. Record the source id, not just the Doc id; the sync call needs it.
Verify the source is listed afterwards rather than assuming the push worked.

**Stage 5 - residue.** Anything the sweep turned up that needs doing - a message never answered, a
commitment with no owner, a held-out message that should be filed in Sensitive, live credentials
that need rotating - goes to `pm-tasks.md` with the project tag. That is the main reason the sweep
is worth running rather than just reading.

**Stage 6 - offer to automate, every time, before you close.** A first `collect` has just done the
one thing that cannot be done later: the backfill. That makes this the only moment where switching
on ongoing capture leaves NO gap, so the offer belongs here and not in some future session the PM
may never start. Say it in one line - the history is in, ongoing capture is not, here are the
routes - and hand to `automate` on a yes. If the PM says no, write that decision and its date into
`project-context.md` so the next run does not re-ask, and put a re-sweep reminder in `pm-tasks.md`
instead, because a log nobody re-runs is stale the first time it matters.

Never end a `collect` run silently. A PM who has just watched a year of mail land in one document
reasonably assumes it now keeps itself up to date. It does not, and only this skill knows that.

**The cursor.** Keep one line at the top of the Doc: `Collected through: YYYY-MM-DD (last run
YYYY-MM-DD)`. Read it before sweeping and rewrite it after. Re-sweep the last few days every time
and **dedup on Message-ID, never on date** - a message can arrive carrying an older date than one
already logged, and a date cursor drops it silently.

## Mode: automate

A log that depends on the PM remembering to ask for a sweep will be six weeks stale the first time
it matters. The goal of this mode is that the PM never needs `collect` again except as a catch-up.

Usually reached from Stage 6 of `collect` rather than asked for by name, because a PM who has just
had the backfill done is rarely thinking about what happens next week.

Route on what this PM actually has, probed rather than assumed:

1. **Workspace Studio, arrival-triggered.** The default, and the only route that needs nothing
   from Claude and nothing installed on a machine. Studio has a genuine on-email-arrival trigger,
   the classification step is a prompt rather than code, and it works for every PM on the team.
   Hand them the setup guide. The weakness is that the hold-out judgement becomes a prompt, and
   the credential tier is the part you would least want to hand to one.
2. **A scheduled task in Claude**, if this PM has scheduling available - try it and see, do not
   assume from the fact that it exists on somebody else's machine. Better judgement about what is
   a confirmation versus chatter, which is the whole argument for it: the credential tier and the
   commercial call are exactly what a single prompt gets wrong. This is the route that has actually
   run, weekly, on a real project, and the six constraints below are what it cost to make it
   reliable. Its limit is ownership, not capability - it runs on one person's machine and stops
   when that machine does, so for the team it stays a prototype while for a PM who has Claude it is
   the working route.

   **A scheduled task is a PROMPT, not a script.** It is stored as a `SKILL.md` and each run starts
   with no memory of any other session, so everything it needs is in that text - which is also why
   a runbook it follows has to name its commands. Scripts belong inside it only where the output
   must be identical every week (trimming, dedup, rendering: a model re-deriving those from prose
   drifts, and in an append-only log drift is permanent) or where a rule has to be ENFORCED rather
   than requested. The judgement stays in the prompt. Do not turn the classification into code.
3. **Apps Script on a time trigger.** The most control, and the only route that does history and
   ongoing capture with one mechanism. Two things to say out loud: Gmail has NO arrival trigger
   for Apps Script, so this is polling with a few minutes of latency, and a trigger runs as
   whoever installed it, on their consent and their quota - which means it dies when they change
   team.

**Then say the coverage boundary, because this is where a hole gets built in.** An
arrival-triggered flow covers from switch-on forward and cannot reach backwards. So run `collect`
FIRST, once, over the full history, and only then turn the flow on. Do it the other way round and
there is a gap between the project's earliest mail and the switch-on date that nobody notices
until the missing message is the one that matters.

### Building an unattended run: six constraints, all learned the hard way

**Every command must be a constant string - and whatever the run follows must SUPPLY that string.**
A scheduled run that composes a command carrying a session path, a timestamp or the current cursor
date gets "allow once" as the only option, because there is no stable rule to persist, and the
permission it earns dies with that session. So it prompts again on every run, forever. Fixed script
path, no arguments that change between runs, a fixed input file.

The second half is the one that actually bit, on the second live run of this skill. The runbook
said "append to the master and move its cursor" without naming a command, so the session improvised
Bash carrying that week's date, and the PM got two "allow once" prompts on a job built specifically
to never prompt. **Writing "use a constant string" is not a control. Naming the command is.** Any
step that tells the run to do something without giving it the exact command is itself the defect -
say so rather than inventing one.

**Append, never rewrite, and keep the cursor OUT of the file being appended to.** A step that reads
the whole log, adds a few hundred bytes and writes it back makes every run capable of destroying
the archive - and the usual reason it does that is a "collected through" line sitting at the top of
the same file, which has to be edited in place. Put the cursor in its own small sidecar, open the
log in append mode, and the worst a bad run can do is add a wrong entry. Verify the file grew by at
least what was written.

**The write step must be safe to run twice**, because eventually it will be: a run that fails after
appending gets retried. Dedup the incoming entries against the log by Message-ID and refuse if any
are already there, rather than trusting that the caller only calls once.

**Reconcile the stores before the run reports success.** The log lives in a Doc, a local master and
the brain, and the run writes them in sequence, so any one of those writes can fail alone and
nothing will notice. The cheapest check is the cursor: the same date must appear in every store at
the end. If it does not, name which write did not land and stop - carrying on means next week
either duplicates an entry or silently misses one.

**Never read input from wherever the harness happened to put it.** Large tool results get persisted
to disk and small ones come back inline, so anything that globs a results folder works during the
big first build and silently finds nothing on every normal week afterwards. Write what you fetched
to a fixed path, then read that path.

**Make an unearned zero impossible, do not merely discourage it.** The automation should exit
non-zero - not report politely - when its input is missing, stale, or unparseable, and it should
print what it READ beside what it FOUND so a zero can be checked. Treat a stale input file as an
error too: last run's input dedups cleanly to "0 new" and looks exactly like a quiet week.

Record in `project-context.md` which route is live, when it was switched on, and the date the
backfill reached. Those three facts are what `review` compares against.

## Mode: review

- **Read the cursor.** Days since last collection is the staleness number, and it is the one to
  lead with.
- **Re-run the query for the window since the cursor** and count what has not been collected.
- **Check the brain actually re-synced.** A Doc added as a source once and never re-synced is the
  quiet failure here: NotebookLM keeps answering from the version it read, so the log looks current
  in Drive and is months behind in the brain.
- **Sanity-check coverage, not just recency.** Count what the log holds for a window against a
  deliberately broad query for the same window. A large gap means the scoping is too narrow, which
  is the normal fault and the one nobody notices.
- **Check the automation is still capable of failing.** If a scheduled flow is live, look at what
  its last runs actually reported. A run of identical "nothing new" weeks is the symptom to chase,
  not the reassurance it looks like - confirm the runs are reading something, and that its
  permissions have not been left pinned to a dead session.
- **Check the stores still agree.** Compare the cursor in every place it lives - the Doc, the local
  master or its sidecar, `project-context.md`. They diverge when one write in a run failed, and the
  divergence is silent until somebody needs a message that only one store has.
- **Check the participant list still matches reality.** People join a client project and a
  participant-scoped query does not notice.
- **Report concretely**: collected through X, N messages uncollected, N held out and on what
  grounds, brain last synced Y, automated capture live since Z or not live at all. Then offer to
  close it - a review that ends in a diagnosis and no proposed action just generates a question.

## The commitments table - the part that actually settles an argument

An archive of four thousand messages does not show that scope was confirmed. One row does: the
date, what was confirmed, who confirmed it, and the Message-ID that points at the proof. Keep it
at the top of the same Doc, above the entries.

While collecting, watch for approvals, sign-offs, scope changes, agreed dates and refusals. Note
that the mandatory Baseline Validation and Project (Start) Approval artifacts are themselves
filed as mail - so its evidence is exactly the kind of message this table indexes.

Two practical notes. Scan the CLIENT side only - our own "please confirm" is not a confirmation -
and expect roughly half the candidates to be meeting RSVPs that match on the word "accepted"; cut
those. Carry each row's verbatim quote next to the summary, so a reader can see the reading is
fair without opening the mailbox.

Offer the candidates at the checkpoint. Never write them silently: a misread confirmation sitting
in a table is worse than no table, because the next person quotes it. If the PM says no, drop it
and do not re-offer on every run.

## Checkpoints and what gets written

Every stage ends with one line naming what went into `project-context.md`.

`project-context.md` holds: the Doc ID, where it was filed and that decision, the query (domains,
named participants, denylist), the cursor date, the brain SOURCE id, and which automated route is
live since when. Money never goes in it, and nor does any message body.

`pm-tasks.md` holds the residue, tagged with the project.

## Notes

- **This is not one of the mandatory starting artifacts.** Nothing scores it and nobody audits it, which
  is exactly why it quietly does not exist on most projects. It earns its place on the day the
  client's memory and ours differ.
- **Never let it be called evidence.** Repeated because it is the one mistake here that cannot be
  walked back once somebody has relied on it.
- **One Doc per project.** If it grows unwieldy, split by year and keep the naming
  (`<Project> - Correspondence Log 2026`) so the brain can hold both as sources.
- **Chat and calls are the bigger hole.** Client decisions land in Google Chat and on calls at
  least as often as in mail, and this skill covers neither. Say so rather than letting a PM
  believe the mail log is the whole record.
