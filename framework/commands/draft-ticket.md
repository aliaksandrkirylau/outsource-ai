---
description: Draft a full tickets/<KEY>.md (scope, acceptance criteria, boundaries) from a tracker ticket, grounded in the actual codebase. Produces a DRAFT that the spec reviewer must approve before /work-ticket will use it.
argument-hint: [TICKET-KEY]
---

# /draft-ticket — turn a tracker ticket into a real ticket spec

Argument received: `$ARGUMENTS` (a ticket key)

Tracker tickets range from a full specification to a one-line summary inside an
epic with a short paragraph. This command's job is to turn either into
something `/work-ticket` can safely execute: concrete scope, explicit
boundaries against sibling tickets, and a draft acceptance-criteria checklist —
grounded in what is actually in the repository, not guessed from the title.

The output is a **draft**, marked `Status: DRAFT`. `/work-ticket` refuses to
run against it until the spec reviewer (or a human) sets `Status: CONFIRMED`.
Do not skip that marking.

Project-specific facts — repositories, conventions, owner roles, tracker
access — come from `PROJECT-PROFILE.md`. Read it first.

## Step 0 — Gather the tracker context

Try, in order:

1. If the tracker is reachable (see the profile), fetch the ticket, its epic,
   and every sibling ticket in that epic (key, summary, status, area). The
   ticket's description is the fullest spec available.
2. Else, if `TRACKER.md` exists, **do not read it whole**: grep for the key to
   find its epic, then extract only that epic's heading, description, sibling
   table and this ticket's own paragraph.
3. Else, if the epic block is already present earlier in this conversation,
   use it.
4. Else stop and ask for the epic block. Do not draft from a bare key — there
   is not enough signal.

You need, at minimum: this ticket's summary and area, the epic's description,
and every sibling's key and summary. **Siblings define what NOT to build here.**

Then check the findings journal for debt already assigned to this ticket.
**Do not read `FINDINGS.md` whole**; grep for the owner-ticket label:

```bash
grep -n -E -B 5 -A 8 "Likely owner ticket(\*\*)?: .*$ARGUMENTS" FINDINGS.md
```

Any match with `Resolved: no` is a candidate for this ticket's scope — carry it
into "Known related findings" so a decision is made explicitly. Do not mark it
resolved here.

Also grep `DECISIONS.md` and `SPEC-DISCREPANCIES.md` for the ticket's key
terms: a decision already taken must not be reopened by the draft.

## Step 1 — Ground the draft in the actual codebase

- From the ticket's area and the epic, identify which part(s) of the system it
  touches, using the component map in the profile.
- Search the code for anything already related: existing modules, endpoints,
  similar prior work. Note what exists vs. what is genuinely missing.
- Read the conventions of the touched part (its `CLAUDE.md` / README) that the
  acceptance criteria must respect.
- If the area is ambiguous even after this, say so in Open questions rather
  than inventing an architecture.

## Step 2 — Draft the scope

- **In scope**: what this ticket, and only this ticket, delivers.
- **Out of scope, explicitly**: every sibling ticket by key with a one-line
  reason, plus anything epic-level the ticket summary does not itself claim.

## Step 3 — Draft acceptance criteria

- Concrete, verifiable criteria: an endpoint returns a given shape, a screen
  shows a given state, an input produces a given output.
- Where the ticket implements a client formula or rule, quote it verbatim and
  implement it literally — divergence from data goes to
  `SPEC-DISCREPANCIES.md`, not into a "corrected" criterion.
- Anything you are not confident about goes to Open questions, not into the
  criteria as a guess.

## Step 4 — Write `tickets/$ARGUMENTS.md`

If the file exists with `Status: CONFIRMED`, do not overwrite it; report that
and stop. Any other status may be regenerated.

Use `framework/project-templates/ticket-spec.md` (installed in the project as
`tickets/_template.md`).

## Step 5 — Report

To whoever launched you:

- the drafted scope and acceptance criteria in brief (the file is the source
  of truth);
- pre-existing findings that matched — they need a yes/no decision;
- the Open questions, each phrased so the role who owns the answer can reply
  in one line.

Do not run `/work-ticket`. Drafting and implementing are separate steps on
purpose.
