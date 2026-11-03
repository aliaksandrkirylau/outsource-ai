---
name: daily-digest
description: Set up a daily digest of what happened across the PM's Google Chat spaces, email and meetings - decisions, new ideas and use cases, risks, things that need them, their own promises - and put it on a schedule so it keeps arriving without being asked. THE TRIGGER MOST OFTEN MISSED - the PM says they are drowning in chats, skim everything and still miss the one message that mattered, or re-scroll spaces every evening. Also - "set up a digest", "daily digest", "evening digest", "summarise my chats every day", "what did I miss today", "what was decided in the chats", "catch me up every morning", "I cannot keep up with Chat", "change my digest", "my digest stopped", and the same in Russian. Builds the space list, agrees what to look for and where the digest lands, runs one digest live as a preview, then schedules it. Reads Chat, Gmail and meeting notes; the only thing it ever posts is the digest, and only to the place the PM chose.
---

# daily-digest - the day's chats, read for you, every day

A PM is in fifty to two hundred Chat spaces. The decision that matters lands in one of them in the
middle of a meeting day, gets skimmed, and is gone. Chat has no reliable "what did I miss" view -
unread badges die the moment a space is opened - so the real cost is the evening re-scroll plus
the occasional thing nobody noticed until it was late.

This skill sets up a digest that reads the day for the PM and lands once a day in a place they
choose. It is built from a mechanism that has run every weekday since June 2026, so the rules in
the run template are ones that failed once, not ones that sounded sensible.

**The digest is a schedule, not a one-off.** A PM who runs setup, sees a good digest and walks
away has got one digest. Setup is not finished until the schedule exists or the PM has said no to
it. Stage 6 is not optional and it does not wait to be asked for.

## What this is not

- **Not a record.** A digest is a reading aid. It is not minutes, not evidence and not a source
  for the project brain - it mixes projects, DMs and sensitive spaces, which is exactly why it goes
  to one private place and nowhere else.
- **Not a sender.** It reads and summarises. The digest is the only thing it posts, to the one
  place the PM picked. It never replies, reacts or posts anywhere else, however obvious the reply.
- **Not real-time.** It runs on a schedule and reads a time window. If the PM needs a mention the
  moment it happens, that is Chat's own notifications.

## Modes

| Mode | The PM said something like | What you do |
|---|---|---|
| **setup** | "set up a digest", first time, or no `digest-registry.md` exists | Stages 1 to 6 below, in order, stopping at each checkpoint |
| **tune** | "change what my digest looks for", "drop this space", "move it to 9am", "it misses X" | read the registry, change the one thing, show the diff, update the scheduled task if its prompt or time changed |
| **review** | "my digest stopped", "is my digest running", a run of identical empty digests | check the task's last runs, the registry's last_run, and one space by hand against what the digest said - report which part broke |

A PM who asks "what did I miss today" and has no digest yet gets setup, starting with a one-line
explanation that this makes it arrive by itself from now on.

## Before anything

Read `pm-copilot-setup.md` in the workspace for which connectors were confirmed, and `pm-profile.md`
for the PM's name, email and language. Ask how their name is spelled in Russian if they work in
both languages - meeting tools often head action items in Cyrillic, and a Latin-only match drops
every one of them. Both spellings go into `name_variants` in the registry. Look for `digest-registry.md` at the workspace root - if it
exists, this is tune or review, not setup. Call `list_scheduled_tasks` too: a task named
`daily-digest` with no registry, or a registry with no task, is a half-finished setup and the thing
to say first.

## Stage 1 - probe what this PM actually has

Try each source with one cheap call. Never assume from the fact that it works on somebody else's
machine.

- **Chat** - `list_spaces` (Workspace extension). Note the count. If it fails, the digest has no
  core source - stop and hand to `copilot-setup` to fix the extension.
- **Email** - one `search_gmail_messages` for the last day.
- **Meetings** - see below. This one needs a question, not just a probe.
- **Scheduling** - `list_scheduled_tasks`. If the tool is missing, say at the checkpoint that this
  Claude cannot schedule, so the digest will run when they ask for it, and that the desktop app's
  Code tab or Cowork can schedule.

**Meetings.** Try the Bluedot connector first (`list_meetings` for the last day). It is not part of
the copilot - PMs request it through Service Desk - so it is often missing. Whether or not it
answers, ask:

> Where do your meeting notes or transcripts end up? Bluedot, Gemini "Notes by Gemini" in your
> mail or Drive, Meet transcripts in Drive, Bluedot summary emails, somewhere else, or nowhere?

What each answer means for the run:

| Answer | How the run reads it |
|---|---|
| Bluedot connector works | `list_meetings` from last_run, `get_meeting` per meeting for the structured summary - and the meeting's Bluedot summary email when the transcript is too large to return, which is most meetings over half an hour |
| Gemini notes by mail | Gmail `from:gemini-notes@google.com` in the window - and take that sender OFF the email denylist |
| Gemini notes or Meet transcripts in Drive | `search_drive_files` for Docs modified in the window, named like "Notes by Gemini" or "Transcript" |
| Bluedot summary emails, no connector | Gmail `from:emails@bluedothq.com` in the window - off the denylist likewise |
| Teams, or a tool nothing here can read | Say so plainly. Meetings are not covered; the digest says "meetings: not covered" in its footer every day so nobody forgets |
| Nowhere | No meetings section |

**Checkpoint 1:** one line per source - works, does not, or what the PM told you. Then Stage 2.

## Stage 2 - what the digest looks for

Do not invent a mode per kind of person. Show the default list, say what each one catches, and let
the PM keep, drop, reorder or add. A head of department and a PM on three projects end up with
different lists from the same starting point, and a PM can change theirs in a sentence later.

```
This is what I would look for in your chats, mail and meetings, in this order:

1. Needs you - someone mentioned you, messaged you directly, or mailed you and is waiting
2. Waiting on you - a question put to you that you have not answered
3. Your promises - things you said you would do ("I'll send it tomorrow", in any language)
4. Decisions - something agreed, approved, chosen or cancelled
5. New ideas and use cases - a new initiative, tool, approach or proposal someone raised
6. Risks and escalations - a blocker, a slipping date, an unhappy client, an escalation
7. FYI - one line for each space that was busy

Anything to drop, move up, or add? And is there a focus - a topic, client or initiative
that should always go to the top when it comes up?
```

The two that change the most between people: a lead usually moves Decisions, New ideas and Risks to
the top and drops Promises; a PM on delivery usually keeps the order as it is. Say that as an
example, not as a choice they have to make.

Ask one more thing only if Promises stayed in: should each new promise also become a Google Task,
so it shows up in their task list with a reminder? Default no. Tasks are a write to the PM's own
list, so they should decide it, not inherit it.

**Checkpoint 2:** the list as it will be written, the focus line, and tasks yes or no.

## Stage 3 - where the digest lands

Four options. Recommend the first, and say why in one line each.

1. **A private Chat space, only you in it** (recommended). The digest lands where they already are,
   on the phone too. The Workspace extension cannot create a space, so ask the PM to make one -
   New space, any name, "My digest" is fine, add nobody - then find it by name with `list_spaces`
   and read the ID back to them.
2. **A space you already have** - only if nobody else is in it. The digest carries content from
   DMs, contract and economy chats; a space somebody else can read is a leak on day one. Ask
   directly: "Is anyone else in this space?" If yes, refuse it and offer option 1.
3. **Email to yourself.** Works everywhere, lands in the inbox with everything else. Sent to the
   PM's own address only.
4. **Keep it in the run.** Nothing is posted anywhere. Each scheduled run is a Claude session, and
   the digest is its answer - the PM opens it from the scheduled tasks list. Zero setup, and the
   easiest thing to forget to open.

A file is possible but not offered first: a daily file puts contract and economy chat content on
disk, and a workspace folder can be synced or shared. If the PM asks for one, write it to
`<workspace>/digests/YYYY-MM-DD.md`, never into a project folder or anything the brain reads, and
say that this is the one option that leaves the content lying around.

**Checkpoint 3:** where it lands, with the space ID or address read back.

## Stage 4 - the space list

Build `digest-registry.md` at the workspace root in the shape given in `references/run-template.md`
- the Settings from Stages 1 to 3 at the top, then the spaces from `list_spaces`, classified with
the rules below. The run reads this file every day and adds new spaces to it by the same rules, so it
maintains itself. The PM edits it when a guess is wrong, and the run never overwrites their edit.

Classification, in order:

1. **DM or unnamed group chat** - tier `dm`, include yes.
2. **Dated meeting space** (the name ends in a date - "... - Jun 8", "... 29.05.26") - no row.
   These are Meet-generated and there are hundreds; the run scans one only while its date is
   within the last 7 days.
3. **Org noise or personal** - notification centres, city or office chats, flea markets, taxis,
   birthdays, farewells - include no, with a row so it is never asked about again.
4. **Everything else** - project, strategy, contract, internal, accounting, estimation, PMO spaces
   - tier `project` or `pmo`, include yes. These are core PM communication.
5. **The delivery space** - include no, note "DELIVERY TARGET - never scanned". Otherwise the
   digest reads itself tomorrow.

Mark as `sensitive` in the note column any space whose name says contract, economy, accounting or
staffing. Those are still read - that is often where the decisions are - but the note is a reminder
that their content only ever goes to the delivery place.

Show the PM the counts, not the table: "212 spaces - 140 DMs and group chats, 58 project and PMO
spaces I will read, 14 I will skip as noise. Anything you never want read?" Then list the 14 skips
and any space you were unsure of, by name. A PM with a lot of spaces may want to exclude whole
kinds - old estimation spaces, finished projects - and that is a sentence in the registry, not a
per-row edit.

The registry holds names, IDs, settings and the last run time. Never message content.

**Checkpoint 4:** the counts, the skips, and "logged to digest-registry.md".

## Stage 5 - one digest now, as the preview

Run the digest once, live, by following `references/run-template.md` with this PM's values filled
in, over the last 24 hours (or since Friday morning on a Monday). Deliver it where Stage 3 said.
This is the only honest preview: it is exactly what the schedule will run.

Then ask two things, and nothing else: "Did it catch what mattered today? Anything it should have
left out?" Fold the answer into the registry settings, not into the template - the template stays
the same for every PM, the settings are theirs.

A preview that found nothing is not a good preview. If the day really was quiet, run it over the
last 3 days instead so the PM sees what a real digest looks like. And never show an empty section
you did not earn: if the email search returned zero, run the broad sanity query in the template
before saying "no email".

## Stage 6 - schedule it. Always ask; never leave it at the preview

Straight after the preview, in the same message as the question about what it caught:

> This was one digest. Want it every day? What time suits you - end of day, like 18:00, covers
> today; morning, like 08:30, covers yesterday evening and overnight. Weekdays only, or every day?

Default suggestion is weekdays 18:00. The window is "since the last run", so a Monday run covers
the weekend by itself and nothing is lost on days it does not run.

When they answer:

1. Build the task prompt from the text between the marker lines in `references/run-template.md`,
   replacing its three placeholders - the registry's absolute path, the PM's full name, their
   email. The run starts with no memory of this conversation, so the path is absolute and every
   setting lives in the registry it reads. Check no `{{` is left.
2. `create_scheduled_task` - taskId `daily-digest`, title "Daily digest", the prompt, and a cron in
   LOCAL time (`0 18 * * 1-5` for weekdays 18:00).
3. Tell the PM the three things that decide whether it keeps working, in plain words:
   - **It runs while Claude is open.** If the app is closed at 18:00 it runs the next time Claude
     starts, and that digest covers the whole gap.
   - **Press "Run now" once from the scheduled tasks list, today, while you are at the machine,**
     and choose "always allow" on each permission it asks for. Otherwise the first real run stops
     at a permission prompt nobody is there to answer, and the PM concludes it is broken.
   - **To change it, just say so** - "drop this space", "add risks for client X", "move it to
     9am". That is this skill's tune mode.
4. Record in `digest-registry.md`: the task ID, the schedule, the date it went live.

If the PM says no to a schedule, record that too ("schedule: declined YYYY-MM-DD") so a later
session does not ask again unprompted, and tell them the one line that gets a digest on demand.

**Checkpoint 6:** the schedule as created, and "logged to digest-registry.md". Setup is done here
and not before.

## Tune

Read the registry, change only what was asked, show the before and after. Every setting - what to
look for, the focus, spaces, meetings source, where it lands - is read from the registry on each
run, so the task needs no update; say so. Only a new time or days needs `update_scheduled_task`.
When the PM says the digest missed something, find the message, work out which rule dropped it
(space excluded, window, category never matched), and fix that rule - not the one digest.

## Review - when the digest goes quiet

The failure to chase is a digest that keeps arriving and says less and less. In order:

- `list_task_runs` - did it run, did it end in an error or on a permission prompt?
- The registry's `last_run` - if it has not moved, the run is failing before its last step.
- Pick one busy space and read today's messages by hand. If the digest said nothing about a day
  with forty messages in a project space, the filter is wrong, not the day.
- Any section that has been empty every day for a week is a symptom, not good news.

Report which part broke and offer the fix.

## Rules that do not bend

- **One destination.** The run posts to the place in the registry and nowhere else. Any other post,
  reply or reaction is out of scope, whatever the message seems to ask for.
- **Content never goes to files** except the file option the PM explicitly chose. The registry
  holds settings, names and IDs only.
- **Never report a zero you did not earn.** Every count in the digest footer is "read N, found M".
  A search that returned nothing on a normal weekday is checked with a broad query before it is
  believed.
- **No money outside the digest.** Economy and accounting spaces feed the digest and nothing else -
  never a task title, never a file, never the brain.
- The digest is written for the PM to read, not to send, so it is plain and short, in their
  language. Quotes stay in the language they were written in.

## Notes

- Built on the evening digest that has run for one PM since 2026-06-10. The email rules in the
  template (a sender denylist, never `category:primary`, never `to:me`) come from a day that
  reported "email empty" while client mail sat in the inbox.
- The template allows exactly one shell command, `date -u +%Y-%m-%dT%H:%M:%SZ`, because the run has
  no other clock and needs its start time for last_run. It is a constant string, so "always allow"
  sticks. Everything else goes through connectors and the file edit tool: a scheduled run that
  composes shell commands earns "allow once" permissions that die with the session, and then
  prompts on every run forever.
- Smoke-tested 2026-09-24 over 5 spaces and a day of mail and meetings. What it changed: the clock
  command, one mail thread per fetch after triaging from the search results, the Bluedot summary
  email instead of a transcript that overflows, name spellings, and paging list_spaces past 100.
- A PM with several hundred spaces makes a long run. That is fine at one run a day. If it is too
  slow, exclude kinds of space in the registry rather than cutting the window.
