---
name: pmo-guide
description: Questions about PMO process and the standard - "how do we...", "what is the standard for", "what does B03 require", "who approves", "who do I escalate to", "is this mandatory", "is there a template for", "where is this filed", "what is the process for a running project", and the same in Russian. Any block of the standard, A to G, not only initiation. Answers from the live Confluence page with the page ID cited, using the reference pack as the index and the PMO Superbrain as background. Read-only, never writes to Confluence, Jira or a notebook. NOT for doing the work - "run A05", "build the risk register", "post the status" go to that skill; this one explains, cites and offers the skill.
---

# pmo-guide - how we do things here, with the source attached

A PM asking "how do we escalate a budget overrun" does not want a draft, a process or a skill run.
They want the rule, where it is written, and whether it is current. This skill gets that and stops.

The trap it exists to avoid is answering from memory or from the bundled pack alone. The pack is a
dated cache and it drifts: on 2026-09-23 it said the initiation checklist had 21 artifacts, the
live page had 20 that morning and 23 by the evening. A confident answer from a stale cache is worse
than "I do not know", because the PM acts on it.

## Sources, and what each is FOR

Three sources, and they are not interchangeable. Using one for another's job is the failure.

1. **The reference pack** - `<workspace>/pm-copilot-references/`, falling back to the shipped copy
   (resolution order is in `copilot-baseline.md`). Use it as the INDEX: which step, which artifact,
   which Confluence page ID. Fast, works offline, and never the final word.
2. **Confluence, read live by page ID** - the AUTHORITY. Whatever the page says today is the answer.
   If the pack gives no page ID, search the PMO space for the page, then fetch it by ID and cite the
   ID. Never trust a title or the step number in a title: the numbering changed in Sep 2026 (the
   caveat in `standards-sync`), and a PM's older notes may still use the old codes.
3. **The PMO Superbrain notebook** (`158e107b-0f3e-47b9-9566-f481595ab399`) - the NARRATIVE. Best
   for Standards B to G, the Knowledge Base (Risk Framework, Roles, DoR/DoD, Charter) and "how do we
   usually handle this" questions no page answers directly. It is fed from Confluence and lags it,
   so when Superbrain and a live page disagree, the page wins.

### Asking Superbrain without timing out

Measured 2026-09-23. A blocking notebook query is cut at about 60 seconds by the connector
("Request timed out"), whatever timeout the query itself asks for - one asking for 240s was cut
at 61s. That is the client's limit, not the notebook being slow. Broad questions run in the
background finished in about 100s, as 12-17k-character answers with 60-77 citations, and ignored
"keep it brief". A two-sentence question took 28s across all sources and 16s pinned to one.
Latency tracks how much the notebook has to WRITE, not how many sources it holds.

Querying and reading the sources are not equivalent. In a side-by-side on the same question, the
query was better at breadth (it covered blocks F and G) and worse on the details that matter: it
built its own "never skip" list instead of using the guideline page's, called a block optional and
then mandatory, and missed a step-order mismatch between two pages that reading the text caught.
Use the query to find where something lives; read the source or the live page for what it says.
So:

- **One topic per question.** One standard block, one step, one artifact. Never "everything".
- **Pin the question to its source** when you know which one holds it. Each standard block (B, C, D,
  E, F, G) is its own Superbrain source, one Confluence page per heading. Look source IDs up by
  title from the notebook's source list for each question, never reuse one from memory or an
  earlier session: the weekly sync deletes and re-adds every changed source, so its ID changes, and
  an old ID then fails with "Failed to get source content".
- **For exact wording or a page ID, read the source text instead of asking.** It returns in seconds,
  word for word, and every heading carries its Confluence link - so for B to G, where the pack has
  nothing, the source text IS the index that gives you the page IDs to fetch live.
- **Anything that may take over a minute runs in the background** (start it, poll for the result).
  A blocking query only for a narrow question pinned to one or two sources. If a blocking query
  returns "Request timed out" at about a minute, switch to the background form - do not retry it
  with a longer timeout, that parameter does not lift the connector's limit.
- Better still, answer a broad question as a map - see "Broad questions" below.

## The flow

### Stage 1 - locate
Work out what kind of question it is: a step (A01..A14, or a B-F cycle), an artifact, a role or
owner, a template, or general house practice. Look it up in the pack to get the step and page IDs.
If the pack has nothing - common outside initiation - go to Superbrain for the narrative and the
page it came from.

### Stage 2 - read the live page
Fetch the page by ID. Note its title and last-modified date. If the fetch fails, or Atlassian is not
connected, say so in one line and answer from the pack and Superbrain with the staleness stated:
"from our cached copy, synced [date] - I could not check the live page."

### Stage 3 - answer
Answer first, in as few lines as the question needs. Then the sources, one line each:

```
An EVM Baseline is mandatory on Fixed-Price projects only. It is built at step A09 together with
the economy calculation and used afterwards to track SV/CV/SPI/CPI.

Source: Starting Project Artifacts Checklist, page 5166432427, row 13, edited 2026-09-23
Note: our cached checklist has no EVM row - logged as pack drift
```

Quote the requirement when the exact wording matters (a control metric, a threshold, a "must").
Paraphrase everything else. Do not recite the whole page.

If a skill does the thing they asked about, end with one line offering it: "`risk-register` can
build it - want me to run it?" Do not run it unasked.

### Broad questions - give the map, then go one level down on request
"What is the standard for a running project" is not one question, it is fifteen steps across four
cycles. Do not answer it with every step's outputs in one reply. Give the map: which blocks apply,
the cadence of each, the page ID of each block, and the few things the standard says can never be
skipped. Then offer to open any one block. A PM asking the broad question is orienting, and a wall
of tables is the thing they will not read.

Anything stated as a specific requirement - a threshold, a "mandatory", an owner - is either
checked on the live page or labelled "from Superbrain, not checked live". Never let a Superbrain
paraphrase pass as the page. In the 2026-09-23 test run, a step swap (B02 capacity vs risks between
the overview and the step pages) and two edit dates were reported from Superbrain's copy only.

### Stage 4 - if the sources disagree
Say which is current and what the other one says. Two different kinds, kept apart as in
`standards-sync`:

- **The standard moved and our pack has not caught up.** Answer from the live page. Add one line
  to `pm-tasks.md`: `[PM Copilot] Pack drift: <file> says X, page <ID> says Y (seen <date>) - run
  standards-sync`. Tell the PM you added it.
- **Superbrain disagrees with the page.** Answer from the page, mention that Superbrain is behind.
  No task - Superbrain is refreshed by its own pipeline, not by the PM.

### When nothing covers it
Say so plainly: "I am not sure what we usually do here - no page in the standard covers it."
Name who would know, from the pack's owners (the standard itself is PMO's; contracts and presales
have their own owners). If the PM wants a draft anyway, give one and label it as a draft, not house
practice. Never present a guess as the PMO's rule, and never invent a process to fill the gap.

## What this skill does not do

- Write anything shared. It reads Confluence, Jira and notebooks; it never edits them. The one write
  is the drift line in the PM's local `pm-tasks.md`.
- Run a step. Explaining A05 is this skill; doing A05 is `a05-a06-scope-and-risks`.
- Refresh the pack. It reports drift; `standards-sync` fixes it, behind its own gate.
- Grade the PM's work against the standard. "Does my register meet the standard?" is answered by
  stating what the standard requires and letting the PM compare, or by offering the artifact's
  skill, which has a review mode.

## Notes
- Answer in the language the PM asked in. Page titles, step codes and artifact names stay English
  so they match Confluence.
- One live fetch per question is the norm, two or three for a question spanning steps. A question
  that needs ten pages is a research task - say so and ask before reading them all.
- Frontmatter note for whoever edits this file: the description must not contain a colon followed by
  a space. It breaks strict YAML parsing, and on 2026-09-23 this skill listed with no description at
  all when installed as a standalone account skill. Ship it inside the plugin.
- If the PM says the page reads differently from what you told them, they are probably right. Fetch
  it again by ID and check before defending the answer.
