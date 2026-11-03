---
name: standards-sync
description: Refresh the copilot's bundled copy of the PMO standard, the initiation artifacts checklist and the template register from live Confluence. Use when the reference pack is stale, when a PM says the standard changed / "Artem updated the standard" / "this page looks different now", when a skill reports a synced date more than a few weeks old, or on request - "sync the standards", "update the reference pack", "refresh the standard", "is our copy of the standard current", "check for standard changes". Also use when a step's control metric or output list disagrees with what a PM sees in Confluence.
---

# standards-sync - keep the bundled reference pack current

The copilot ships a CACHE of the PMO standard in `${CLAUDE_PLUGIN_ROOT}/references/`. Confluence is the source of truth. This skill re-reads the live pages and writes a refreshed copy into the PM's WORKSPACE, showing exactly what changed first.

Why a cache at all: reading fourteen Confluence pages every time a skill runs is slow and fails entirely for a PM without Atlassian connected. Why a sync skill: a cache that silently drifts is worse than no cache. The synced date is the honesty mechanism; this skill is what resets it.

## Where the refreshed copy goes - important

Write the refresh to `<workspace>/pm-copilot-references/`, NOT back into the plugin folder. The plugin directory is managed by the app: a write there may be refused outright, and if it succeeds it is wiped on the next plugin update, silently reverting both the content and the synced date. That is precisely the drift this skill exists to prevent.

So the resolution order every skill should use, and which this skill should state plainly when it finishes:

1. `<workspace>/pm-copilot-references/<file>` if it exists - the PM's refreshed copy wins.
2. `${CLAUDE_PLUGIN_ROOT}/references/<file>` - the shipped copy, whatever came with this version.
3. Live Confluence, if Atlassian is connected and both copies look stale.

If the shipped copy is NEWER than the workspace copy (the PM installed a plugin update), say so and offer to discard the local one rather than quietly preferring a stale override.

## How this skill behaves

Staged, and the write is gated. Show the diff, get a yes, then write. Never overwrite the reference pack silently - a PM should be able to see what moved in the standard, because a changed control metric or a new mandatory artifact is real news, not housekeeping.

## What it syncs

| File | Live source |
|---|---|
| `references/standard-a-contract.md` | Pages 4619206688, 4619206702, 5142544653, 4619206765, 4619206785, 4619206806, 4619207137, 4619206956, 4619206835, 4619206729, 4619207047, 4988764344, 4988633155, 5015830531, plus the overview 4619206674 |
| `references/initiation-artifacts-checklist.md` | Page 5166432427 |
| `references/template-register.md` | Follow-on pages named in the standard; see the register for the current ID list |
| `references/pmo-conventions.md` | Pages 5257166927 + 5257167110 + 5262049359 (Drive), 3006398548 (Chats), 3723624953 (PROREP), 4955406559 (Project Brain) |

**Never synced - no Confluence source exists.** Do not go looking for pages for these and do not report them as stale:

| File | What it is |
|---|---|
| `references/pl-structure.md` | house knowledge from real P&L runs. Update by hand when the file structure changes |
| `references/pm-profile-template.md` | ours entirely |
| `references/instructions-layers.md` | ours entirely |

**One more cache that lives outside `references/` and is easy to miss.** `skills/a01-presale-handover/scripts/score_handover.py` hardcodes the 28-item A01 rubric with its core and critical flags, derived from page 3285712947 - and the same list exists as `skills/a01-presale-handover/references/acceptance-checklist.md`. If that page changes, the scorer keeps producing metrics against the old rubric and nothing else notices. It is the only place in the bundle that generates a number a PM puts in front of Sales, so check it during a sync. Fixing the script is a BUILD change for the copilot owner, not a workspace write - report it, do not patch it.

## Stage 0 - check whether a sync is even needed
Read the `synced:` date from each reference file and report it. If Atlassian is not connected, say so plainly and stop - the cache stays as it is, and skills continue on the cached copy with the staleness stated.
CHECKPOINT: "Reference pack last synced [date]. I can re-read [N] Confluence pages and show you what changed. Run the check?"

## Stage 1 - fetch and diff
Fetch each page by ID (never by title - see the numbering caveat below). Compare against the cache and report changes in PM terms, not diff terms:
- New or removed mandatory outputs.
- Changed control metric names, formulas or targets.
- Changed verification criteria.
- New steps, renumbered steps, or new pages appearing under a step.
- Changes to the artifacts checklist (rows added, storage locations changed).
- Pages that returned nothing or moved.

Lead with what MATTERS to a PM running the standard. A reworded sentence is noise; a target moving from 70% to 80% is not.

**Sort every discrepancy into one of two kinds, because the consequences are completely different:**

- **The standard changed.** Propagate it forward: refresh the pack, flag the affected skills, add tasks where live projects are touched.
- **Our copy was WRONG.** Not a change - a transcription error or something invented when the file was written. This is real and has happened: the chat table once listed a "Project / delivery" chat that exists nowhere in Confluence, while the real eighth chat (Staffing) was missing entirely. When you find one of these, say so plainly as OUR error and say what may have been built on it. A wrong cache line does not just need correcting; anything downstream that relied on it needs a second look, and a PM may have been given a finding that was never true.

Do not fold the second kind into "here is what moved in the standard" - that attributes our mistake to PMO and hides the fact that something downstream may be wrong.

CHECKPOINT: show the change summary, separated into standard-changed and we-had-it-wrong. "Nothing has been written yet. Update the reference pack?"

## Stage 2 - write the refreshed copy (WRITE GATE)
On an explicit yes, write the affected files to `<workspace>/pm-copilot-references/` with a new `synced:` date. Create the folder if it does not exist. Never write into the plugin folder.

Preserve the copilot's own annotations - the numbering caveat, the known-template-gaps section, the counting rules and the copilot rules are OUR content layered on the standard, not extracts, and a sync must not wipe them. Carry them across from the shipped copy into the refreshed one.

**And preserve content OBSERVED from a live system, which is a third category and the easiest to destroy.** Some of the pack is fact read off Jira or a live file rather than off a Confluence page - the PROREP epic's structure, its child issue types and its Implementation tab field map, the kick-off template's actual 12-slide layout. None of that is on the pages listed as those files' sources, so a naive refresh from those pages deletes it. Carry it across, and where a sync makes you doubt it, go and re-read the live system rather than dropping it.
CHECKPOINT: confirm which files were written, where, and the new synced date. Tell the PM plainly that skills will now prefer this copy over the shipped one.

## Stage 3 - flag what the change breaks
If a control metric, an output list or a mandatory artifact changed, name which skills are now out of date and which produced artifacts on live projects may no longer satisfy the standard. This is the part that earns the skill its keep - a silent cache refresh helps nobody.
Report it, do not fix it. Updating a skill is a build decision for the copilot owner.

## The numbering caveat - always resolve by page ID

Until about 22 Sep 2026 the standard carried two numbering schemes that disagreed by one, because the contract review (page 5142544653) was a detail page missing from the overview table. The table now lists A01-A14 and the copilot follows it since 0.45.0. The rule outlives the fix.

So: never match a step by page title, and never match by the number in a title. Fetch by ID. If a fetch by ID returns a page whose title does not match what the register expects, report that as a finding - it may mean PMO restructured the space, which is exactly the kind of thing this skill exists to catch.

## Standing open items - check these on every sync

Four questions the pack cannot answer on its own. They are recorded here rather than in someone's notes so a sync answers them whether or not anybody remembers to ask.

1. **Does the overview table still list A01-A14, in the order the pack has?** It was renumbered once already (contract review added as A03, Sep 2026). If steps are added, removed or reordered again, every skill folder name and code needs the same renumber - flag it loudly rather than patching quietly.
2. **Has a real "Acceptance From Pre-sale v2" appeared?** A01 cites it; only a v1 draft exists (page 3285712947) and our scored rubric is derived from that draft. If a genuine v2 turns up, BOTH the checklist markdown and the scorer's hardcoded rubric need reconciling against it, and every maturity score computed before then was against a different yardstick.
3. **Is the A08 line about not assigning named people still on the live page?** Our cache says "do not assign named people in the calculation unless already confirmed and required by the calculation logic". The copilot owner reports that named people are fine in practice. So either the pack over-tightened when it was written, or the written standard and actual practice disagree - both worth knowing, and the second is worth raising with PMO.
4. **Does anything define "the readiness review"?** Five things in the standard gate on it - A11's and A12's control metrics both target 100% before it, plus three escalations - and no page in our pack describes what it is, who runs it or what it checks. It is not one of A01 to A14. If a sync finds a page defining it, that is a genuine gap closed.

## After a sync that changed something

A changed standard usually means work. If a step gained an output, a control metric moved, or an artifact changed its filing destination, put that in `<workspace>/pm-tasks.md` tagged per affected project rather than only reporting it - "the Risk Register now belongs in Confluence, ours is still a Sheet" is a task, not a news item. Note the sync date and what moved in each affected `project-context.md` too.

## Notes
- Requires Atlassian (Confluence) connected. Without it, this skill reports and stops; it does not guess.
- Safe to re-run. If nothing changed, say nothing changed and just bump the date.
- This skill only touches the plugin's reference pack. It never touches a project's documents.
