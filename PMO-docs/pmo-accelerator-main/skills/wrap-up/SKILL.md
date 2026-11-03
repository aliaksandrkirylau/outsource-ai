---
name: wrap-up
description: End-of-session wrap-up for a PM - before the chat closes, move what the session produced into the files the next session reads, so nothing has to be explained twice. Use when the PM is stopping - "wrap up", "let's close", "that's it for today", "I'll pick this up tomorrow", "I'll continue in a new chat", "give me a summary to continue", and the same in Russian. Syncs the task list, writes durable facts into each touched project's project-context.md, leaves a resume note in the project folder, logs what went wrong in copilot-feedback.md, and offers the project brain anything new. One route, no modes. If the PM has a wrap-up skill of their own, that one wins and this skill steps aside. Writes only the copilot's local files - never Jira, PROREP, a notebook or a message.
---

# wrap-up - close a session without losing it

A new chat starts blank. Whatever this session worked out - a task, a decision, who said what, where
the work stopped - is gone when it closes unless it is in a file the next session reads. This skill
puts it there. It takes a minute or two and it runs the same way every time.

## Who wins

Check first, and stop at the first that applies.

1. **The PM's own wrap-up skill.** Look at the skills available in this session. If one that is not
   part of the copilot is an end-of-session wrap-up - its name or description says so - or the PM's
   `pm-profile.md` names one, hand over to it and stop here. A routine the PM built for their own
   setup beats this one.
2. **This skill.** Everything below.

## Read first

- `pm-copilot-setup.md` in the workspace - the workspace shape, the projects folder, and the task
  list's name if setup recorded one.
- `pm-profile.md` - project aliases, and any line about where the PM keeps tasks.
- `project-context.md` for each project the session touched.

## 1. Find the task list

In this order, first hit wins:

1. The list named in `pm-copilot-setup.md` or `pm-profile.md`.
2. A `pm-tasks.md` or `TASKS.md` at the workspace root (any capitalisation). If there are two, ask
   which one is real - never write to both.
3. Nothing found - ask: "Do you keep a task list somewhere, or shall I start `pm-tasks.md` here?"

If the PM names a list you did not know about, use it, then offer ONE line for `pm-profile.md` so the
next run finds it straight away: "Tasks live in <where>." The profile is theirs - offer, do not
write it unasked. If the list is somewhere you cannot write, put the new lines in chat, ready to
paste, and say so.

## 2. Sync the list

Go through the session for anything with a next action: what the PM said they would do, what a skill
turned up, a promise made in a drafted message, a question that needs the client, something waiting
on another person.

- Use the sections the list already has. Do not impose new ones.
- New work goes in with a project tag and where it came from.
- Finished work moves to Done with today's date and one line on what happened. Mark it done, do not
  delete it - a PM wants to see what moved.
- Blocked on a person goes to Waiting on someone, with the person's name.
- Check what is already there first. Update a line rather than adding a second one.

An unknown about the project is not a task - it goes to `project-context.md`. Something that could
hurt the project belongs in the Risk Register - offer `risk-register` rather than burying it here.

## 3. Update project-context.md

For each project the session touched, write the facts that stay true: a decision and who made it, a
contact and their role, where something was filed, which step output now exists, an open question.
Date each entry. If the session contradicted something already in the file, correct that entry in
place. If a project has no `project-context.md` yet, create it from what the session established.

No money and no contract text - the file can end up shared.

## 4. Write the resume note

The resume is where the work STOPPED. `project-context.md` is what stays true. Keep them apart.

Where it goes:

| Session was about | Resume |
|---|---|
| One project | `resume.md` in that project's folder. With a one-project workspace, the workspace root |
| Several projects | The main one gets the file, the others one line each in chat |
| No project - setup, a general question, ordinary PM work | No file. The resume goes in chat |

One file per project, overwritten at every wrap-up - it is the current state, not a history. When a
project closes, delete its `resume.md` in that wrap-up. Plain markdown, no frontmatter.

If the PM said what the next session is for, write the resume for THAT and leave out what it does
not need. If they did not, name the main thread yourself on the first line, marked "inferred", so a
wrong guess is easy to spot. Do not ask.

```
# Resume - <project> - <date>

Next session: <what the PM said, or "inferred: ...">

Where it stands: <1-3 sentences>

Decided:
- <choice + why, if the why is not obvious>

Open:
- <item + state or blocker - point at the task list line, do not copy it>

Open questions:
- <came up, not settled>

Files:
- <path or link> - <its state in one line>

Use next:
- <copilot skill> - <why the next session needs it>
```

Leave out any section with nothing in it. Link documents, tickets and Drive files, never paste them.
Before writing, redact: no amounts, rates, salaries, margins or P&L figures, no contract text, no
candidate or staffing personal data, no passwords, keys or tokens. Hours are fine.

## 5. The feedback log and one question

Read back over the session for entries `copilot-feedback.md` should have: something asked for with
no skill or template behind it, a draft the PM rejected or redid, a fact about Innowise practice the
copilot got wrong, a connector that blocked a step, a skill abandoned part-way. Write any that are
missing - four lines each, projects by name only, no client material.

Then, if real work happened this session, ask ONE question: "Anything about how the copilot ran
today you would change?" An answer becomes an entry. Do not push if they skip it.

If a preference of the PM's has shown up twice now - a format, a length, a person they always copy
in - offer a line for `pm-profile.md`. Offer, never write it unasked.

Leave Claude's own memory alone. The copilot remembers through these files.

## 6. Offer the project brain

If the session produced or found an artifact, register, decision, transcript or document that the
project's NotebookLM notebook does not hold yet, list them and offer `project-brain` to add them. The
upload is gated there - this skill never pushes anything itself. Nothing new - skip this silently.

## 7. Close

In chat, short:

- one line per file written, saying what went in
- the line to start the next session from: "Next time, start with: read <path>/resume.md"

A new chat does not read the resume by itself. It reads it when pointed at it, which is why that
last line matters.

## What this skill never does

Post a PROREP status, move a Jira issue, send a message, or upload to a notebook. Those have their
own skills and their own gates. The only writes here are the copilot's local files: the task list,
`project-context.md`, `resume.md` and `copilot-feedback.md`. Mention each write in one line, as the
baseline asks.

## When to offer it

Offer once, at a natural stop - the PM says they are done for the day or will continue in a new
chat, or a long multi-step session has just landed a deliverable: "Want a quick wrap-up before you
close?" Never interrupt work in progress to offer it, and do not offer it twice in one session.
