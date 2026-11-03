---
name: project-brain
description: Work with a project's NotebookLM notebook - its "brain". Feed it, query it, or check whether it has gone stale. THE TRIGGER MOST OFTEN MISSED - an artifact, decision, transcript, register or document has just been produced or found and needs a home - offer it the notebook in the same breath, whether or not anyone mentioned the notebook. Also when a question about the project should already be answerable from what the project knows, or the notebook has not been touched in a while - "add this to the brain", "is the brain up to date", "what does the brain know about X", "sync the project brain", "what have we decided on this project", "catch me up on this project", "add the meeting notes", "did we ever decide X", "seed the brain for this project", "what is missing from the notebook". Called by the PM at any point, and by the initiation step skills when they produce something the brain should hold. The copilot proposes and shows the inventory; the PM approves every upload.
---

# project-brain - the project's working memory

One NotebookLM notebook per project. A mandatory starting artifact, created at A01 and updated at
A11, and then in practice abandoned - which is the problem this skill exists to fix.

A brain a month behind its own Drive folder stops being worth querying. Once a PM asks it
something and gets a stale answer, they stop asking, and the artifact is dead while still
formally existing. That failure is quiet and it is the normal one.

## Three modes - work out which before doing anything

Every artifact skill has a write mode, a change mode and an audit mode, named for its artifact. A brain is fed rather than created and its read is free and constant, so here they are `feed` / `ask` / `review` - where `risk-register` uses `create` / `update` / `review`.

| Mode | The PM said something like | What you do |
|---|---|---|
| **feed** (write) | "add this to the brain", or a step skill just produced an artifact | show the inventory, get a yes, upload |
| **ask** (read, free) | "what does the brain know about X", "did we ever decide Y", "catch me up" | query it. No permission needed, no gate |
| **review** (audit) | "is the brain current", "has this gone stale", or nobody has checked in a while | audit coverage against what the project actually has, report the gap |

If it is ambiguous, say which you are about to do in one line and carry on - do not open with a
menu. `ask` is free and reversible, so when torn between `ask` and the others, read first.

**Called from another skill?** The caller says which mode and what it is handing over. Do that
and hand back a one-line result - do not restage the whole flow inside someone else's checkpoint.

## Before anything: find the brain

Read the project's `project-context.md` for the notebook ID. If it is not there, list notebooks
and match on the project name and its aliases from `pm-profile.md` - the aliases matter, because
a project's notebook is often named for the client while the PM calls it by the product.

Three outcomes, and be precise about which:

- **Found.** Record the ID in `project-context.md` if it was missing, so the next session does not
  repeat this search.
- **Not found, and the project is real.** The mandatory artifact does not exist. Say so plainly -
  this is a real gap against the mandatory artifacts, not a technicality - and offer to create it (that is `feed`
  in its first-seed form, and `a11-project-setup` owns the container half if they are in setup).
- **Cannot tell.** NotebookLM not authorized, or several candidates. Do not guess between two
  notebooks - a wrong upload is hard to undo and pollutes another project. Ask.

Never write to a notebook you have not confirmed belongs to this project.

## Mode: feed

### What goes in

The default answer to "does this belong in the brain" is YES, and you propose it rather than
waiting to be asked. Anything that would help answer a question about this project in three
months: artifacts and registers, decisions and who made them, meeting notes and transcripts,
client-supplied specs, requirement pages, the source register, retros.

### What never goes in - check every item, every time

From `${CLAUDE_PLUGIN_ROOT}/references/pmo-conventions.md`, and none of these bend:

- **Money.** No rates, salaries, margins, P&L figures, client currency amounts. Worked and paid
  hours are fine. The P&L lives in the Sensitive folder and nowhere else.
- **Contract text.** Goes to the separate confidential contract notebook, never here.
- **Candidate CVs and staffing sheets carrying personal data.**
- **Large raw client data files.** Put a data dictionary note in the brain instead of the file.

A document that is mostly fine with one money table in it is NOT fine. Say which part is the
problem and offer the redacted version, or offer to point at it in Drive instead of uploading it.

### What will actually sync

Also from the conventions pack, and worth checking before promising an upload worked: native
Google Docs and Slides add cleanly as Drive sources; Office files and Sheets pushed via MCP do
not sync reliably. Combine many small documents into one source - all transcripts into one text
source, meeting notes into one compiled Doc - to stay under the source limit.

So for a Sheet, the honest options are a link plus a summary note, or an exported Doc. Do not
push a Sheet and report success.

### The gate - this one never relaxes

Show the upload inventory BEFORE uploading: every item going in, and separately every item held
back with the reason. This gate holds in express mode, on a re-run, and when the PM has already
said yes to something similar. The PM decides what their project's knowledge container holds.

CHECKPOINT: "Ready to add [N items] to the brain: [list]. Holding back: [item] because [reason].
OK?"

After the upload, verify rather than assume - list the notebook's sources and confirm the new
ones are there. A source that failed to sync looks exactly like one that worked, from the caller's
side.

## Mode: ask

Free. No gate, no permission, no checkpoint. Query the brain and answer.

Do this far more often than feels necessary: before answering any question about the project,
before drafting anything for it, and above all before telling a PM you do not know something. A
copilot with a project's brain that does not read it is guessing with the library in the room.

Two habits worth keeping:

- If the brain's answer looks thin or contradicts what you can see in Drive or Jira, say so and
  name the suspicion - that is a `review` finding surfacing on its own, and it is the most
  reliable way staleness gets caught.
- Say where an answer came from. "The brain says X, as of the source uploaded in June" is a
  different claim from "X", and the PM needs the difference.

## Mode: review

The mode nothing else in the copilot does, and probably the most valuable one. The question is
whether this brain can still be trusted, answered with evidence rather than a feeling.

Compare what the brain holds against what the project actually has:

1. **List the brain's sources**, with dates.
2. **Look at the project's real material** - the Drive folder, the Confluence space, the board,
   the artifacts checklist. What exists that the brain has never seen?
3. **Report the gap concretely.** Not "the brain looks a bit out of date" - name the newest
   source, name what is missing, and name what a PM would ask that it would now get wrong.

Two numbers worth reporting because they are cheap and they mean something:

- **Newest source date.** The single best staleness signal. Older than a month on a running
  project is a finding.
- **Artifact coverage** - of the 23 mandatory starting artifacts that exist for this project, how many are
  represented in the brain. Not the same as the PMO's own artifact score; this one asks whether
  the brain knows about them.

Then offer to close the gap, which is a hand-off to `feed` with a specific list. A review that
ends in a diagnosis and no proposed action generates a question instead of answering one.

CHECKPOINT: "Newest source is [date]. [N] things the brain has not seen: [list]. Want me to add
them?"

## Say the state out loud, always

Whatever the mode, end by saying where the brain now stands - what went in, what was held back,
what is still missing. This is the only way a PM builds a sense of whether the thing is current,
and that sense is what decides whether they ever query it again.

## Check the always-on rule is actually installed

The feed-by-default behaviour has to work when this skill is NOT running, because most of the
time a PM produces something without thinking about the brain at all. That lives in the always-on
layer, not here.

So while you are in this skill, check it: does `<workspace>/.claude/rules/pm-copilot-baseline.md`
exist, and does it carry the project brain section? If the file is missing, or predates it, the
disposition is not installed and this skill is the only thing that will ever feed the brain -
which is exactly the failure mode.

Say so, and say the fix in one line: re-run "set up my copilot", which replaces the baseline and
leaves everything of theirs alone. Do not rewrite the baseline from in here - it is ours,
copilot-setup owns it, and a hand-patched copy diverges silently from the shipped one.

## Notes

- Format and hold-out rules live in `${CLAUDE_PLUGIN_ROOT}/references/pmo-conventions.md`. Read it rather than working
  from memory; it is versioned and it is what `standards-sync` refreshes.
- Three containers, kept apart, and mixing them is the one unrecoverable mistake here: the org
  Superbrain (standards, shared with the whole PM team), the project brain (one per project), and
  the confidential contract notebook. An upload to the wrong one cannot be quietly undone.
- The brain is a mandatory starting artifact and the PMO checks for it. But it is scored on existing, and this
  skill is about it being worth something - those are different bars, and the second one is the
  one the PM actually feels.
