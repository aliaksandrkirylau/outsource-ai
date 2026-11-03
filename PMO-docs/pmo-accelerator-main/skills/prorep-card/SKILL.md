---
name: prorep-card
description: Owns the weekly PROREP status - the eight-field comment and the eight PMO indicators, posted to the leadership card together - and checks whether a card still tells the truth. Use when it is the weekly reporting slot and statuses are due, when a card has not been touched in weeks while the project moved on, or when the PM wants to know which of their cards are behind - "PROREP update", "update PMO metrics", "weekly status", "do my weekly statuses", "post the status to PROREP", "time for the weekly statuses", "is my card current", "which of my cards are stale", "what indicators should this project have", "the card says Red, is that still right". Also when the PM names a PROREP issue key and asks for a status, or asks what changed on a project this week for reporting. NOT for the card's descriptive fields - description, client, dates, technologies - which is `a11-project-setup`. Leadership-visible, so nothing is written without an explicit go.
---

# prorep-card - the card, every week, for the whole project

A mandatory starting artifact. Set up once at A11 and then owed a status EVERY WEEK until the project
closes - which makes it the one artifact whose maintenance burden dwarfs its creation. This skill is
the single definition of how the card works, so a PM never has to re-run a setup step to file one
week's status.

Weekly presentations were cancelled in Aug 2026. The card is the single point of truth, and the same
status text goes into the card comment AND the project's strategy chat. If something moves in the
chat afterwards, it goes into NEXT week's status rather than being edited in.

**Read `${CLAUDE_PLUGIN_ROOT}/references/prorep-fields.md` before touching any field on the card.**
It is a live field-by-field map: which fields exist by ID, which are filled in practice, where each
value comes from, and - the part that actually bites - the fact that THREE different field sets on
this card get called "metrics" and only one of them is the PM's weekly job. The card carries 519
fields including near-duplicate English and Russian pairs and two different project-stage fields.
Guessing at a field name here writes real data to the wrong place on a leadership-visible record.

Everything below is the part that lives nowhere else: the weekly cycle, the eight indicators, and
the transition mechanics.

## Which "metrics" this skill owns

Only **Set A**, the eight `Indicator_*` fields, customfield_22759 to customfield_22766. Those are
the weekly job.

Not **Set B** - the older lozenge fields `Legal and finance`, `Focus on Client`, `Committed to
Delivery`, `Team Dynamics` and the `Metrics update` date (12006-12009, 12004). These were a PM job
that the eight indicators superseded and they are not maintained; a real card was observed carrying
Set A current and Set B nine months stale. Do not write to them, do not propose reviving them, and
do not report them as a gap. If a PM asks why their card shows two sets of colours, that is the
answer.

Not **Set C** - Health Check, PMO Rating, Compliance and Audit fields. Owned elsewhere entirely.

Which of the on-screen tab labels sits over Set A and which over Set B is unresolved, and no
Atlassian tool exposes tab grouping. Work by field ID and the ambiguity never arises.

## Two card shapes - post to the right one

Project PROREP holds project-level Epics named for the project, and ALSO monthly cards named
`<Project> - <PM name> - <Month>, <Year>`. **The weekly status and the eight indicators belong to
the project-level card only.** The monthly cards are a separate mechanism.

Filter by name shape and confirm the card before posting. A weekly status on a monthly card is
visible to leadership and awkward to unpick.

## Two modes, and why there is no write mode

| Mode | The PM said something like | What you do |
|---|---|---|
| **update** (change) | "PROREP update", "weekly status", "update PMO metrics" | the eight-field status plus the eight indicators, posted together |
| **review** (audit) | "is the card current", "which of mine are stale", nobody has looked in weeks | staleness, unjustified colours, contradictions - one card or the whole portfolio |

Reading the card needs no mode and no permission - read it and answer.

The other artifact skills have a write mode. This one does not, and the reason is worth stating so
nobody adds one: **nothing about this card is ever created from scratch by the PM.** The card itself
comes from Sales at Closed-Won. Its descriptive panels - description, client, dates, cooperation
model, technologies, links, roles - are filled at A11 and belong to `a11-project-setup`, which reads
the same field map this skill does. What is left for this skill is the thing that recurs: the weekly
status and the eight indicators.

So if a PM asks for help filling in the descriptive side of the card, hand to `a11-project-setup`
rather than doing it here, and say why - that step ties the card's billable-hours fields back to the
A07/A08 plan, which is a check this skill has no business making.

**update is the mode that matters.** It runs weekly for years, and it is the whole reason this skill
exists as its own thing rather than living inside A11.

**Called from another skill?** Do the named mode, hand back a one-line result, and let the caller
run its own checkpoint. Do not restage this flow inside someone else's.

## Non-negotiables

**Never write to Jira without an explicit go.** Show the draft and the proposed indicator values,
then wait for a yes. This is a leadership-visible record and heads read it.

**Never post to the strategy chat.** The PM posts that themselves, every time. This skill produces
the text and names the space. Do not send it and do not offer to.

**Never put specific money in the comment or the chat text.** No figures, no margin, no revenue, no
budget cap, no deposit amounts. Budget Status carries the DIRECTION and the MECHANISM instead:
"still red, not positive yet, but the trend is going the right way, we are moving the client to a
fixed monthly budget and will bring details to the next meeting". The money signal already lives in
the indicator fields - Actual Budget and Budget vs Handover Baseline - and that is the structural
reason it stays out of the prose.

Hours ARE allowed where they are the commercial fact the reader needs: an estimate sent to a client
goes in with its number ("354-444 hours, sent, not confirmed"). The ban is on rates, revenue,
margin, caps and deposits, not on scope size.

**Never hard-wrap the status text.** One field = one unwrapped line, blank line between fields. Jira
and Google Chat both treat a newline as a real break, so a wrapped draft renders ragged mid-sentence
in a narrow column.

## Before anything: find the card

Read `project-context.md` for the card link. Otherwise ask for it - the project is `PROREP`, board
1500 at `https://innowise-group.atlassian.net/jira/software/c/projects/PROREP/boards/1500`, and each
project's card is an EPIC there, so ask for their epic rather than searching blind. If the PM says
"all mine", find them with JQL: `project = PROREP AND assignee = currentUser() ORDER BY updated
DESC`.

A running project with no card is a real finding, not a formality - the card should exist from
Closed-Won. Say so plainly and route it to the Sales Manager; the copilot does not create the card.

Confirm the Atlassian site is reachable before promising anything, with
getAccessibleAtlassianResources. PROREP lives on **innowise-group.atlassian.net**, cloudId
`55e57752-8ec0-4fb0-9676-2c4287bc89e5`. If the grant list comes back with a different site only,
retry once - the list has been observed to rotate within a session. If it still is not there, say so
and stop. Do not fall back to browser automation on a live PMO card unless asked.

Record the card link in `project-context.md` so nothing later has to hunt for it.

## Mode: update - the weekly run

### Step 0 - scope and mode

Ask in one go: which projects, what period (default the last 7 days), and how the evidence arrives.

- **Express** - the PM gives the week's facts in a few lines and this skill shapes them into the
  eight fields. Fast, and the right default for a PM doing four cards in a sitting.
- **Full sweep** - this skill gathers the evidence itself. Slower, but the PM reviews a draft
  instead of writing one.

### Step 1 - gather (full sweep only)

One READ-ONLY subagent per project, launched in parallel, each returning raw material rather than a
finished status. Give each one: the project name, client and aliases from `project-context.md`; the
period as explicit dates; the Google Chat space IDs to sweep - Internal, Strategy, Accounting,
Contract, team and dev spaces, plus any dated standup or meeting spaces in the period, which is
where the Bluedot and Gemini meeting recaps land; an instruction to check Gmail and Calendar; and
the eight field names below plus "what happened this week" and "open questions for the PM" as its
output headings.

Look the space IDs up with list_spaces first. Do not make the subagent hunt.

Two traps to pass on to every subagent:

- **Gmail filters.** Do NOT use `category:primary` or `to:me`. External client threads land outside
  Primary, the PM is often on a thread without being on the To: line, and sent mail carries no
  Primary label at all - so those filters silently return nothing and the whole bucket reads as
  empty. Use `after:EPOCH` with `-from:me` and drop known automation senders (jira@, confluence@,
  drive-shares-dm-noreply@, comments-noreply@docs.google.com, gemini-notes@google.com, no-reply@,
  notify@automation.innowise.com), calendar RSVPs and OTP codes. Check `from:me` with no category
  filter separately for commitments the PM made.
- **search_messages is unreliable** - it returns zero hits for strings that demonstrably exist in
  swept spaces. Treat a zero result as no information, not as absence. Rely on direct get_messages
  per space.

Every non-obvious claim comes back with a source: space plus date, or email subject plus date. A
field with nothing behind it comes back as "no evidence in period", never smoothed over.

### Step 2 - read the card before drafting

getJiraIssue on each card, requesting: status, resolution, updated, and customfield_22759 through
customfield_22766. Do not re-derive a value you can read.

Read the last two or three status comments too, so the new one reads as a delta and matches the tone
already on the card. Requesting the comment field on a long-lived card can exceed the response cap.
When it spills to a file, that file arrives as one enormous single line which Read and Grep both
refuse - delegate it to a subagent asking only about the newest two or three comments rather than
fighting the file. On Windows, `[System.IO.File]::ReadAllText` with the long-path prefix is what
actually reads it if a subagent is not an option.

### Step 3 - draft

Eight fields, this order, each on one unwrapped line:

```
Status:
Budget Status:
Timeline & Delivery Health:
Resources:
Blockers:
Risks:
Escalations with Client:
In-house Escalations:
```

Target roughly 8-14 lines across all eight. This is a leadership scan, not a digest.

- **Status** - the phase, in a clause. "Support / SLA, second month. No release this week."
- **Budget Status** - direction and mechanism, no figures. What is being done about it and when the
  client hears it.
- **Timeline & Delivery Health** - what shipped, what is next, what changed in scope or approach.
  Name the thing that is still winnable where there is one.
- **Resources** - "Green, team is stable" beats a roster. Name a person only when the person IS the
  news: a replacement, an offboarding, a departure. No per-person hours.
- **Blockers** - what is actually stopping work, and who owns it. Nothing blocked means "None". Do
  not pad with stale items.
- **Risks** - a few lines, no ticket counts, no board breakdowns. "Far fewer unresolved issues than
  before, but the client keeps reporting new ones" is the right altitude. A risk that is real but
  small gets one clause, not three sentences. If the risk block runs longer than the delivery block,
  it is too long.
- **Escalations with Client** - what is open in either direction. "None" is common and fine.
- **In-house Escalations** - only if something is genuinely STUCK and needs a head to unblock it. A
  colleague owning a normal next step is NOT an escalation, it is an assignment; put it in whichever
  field describes the work. Most weeks this is "None".

Cut anything that is an internal-process artifact rather than project state: who chased whom, an
email answered late, a wording ambiguity nobody has raised, a thread with no reply. If a head would
not decide or fund anything on the basis of it, it is not in the status.

Do not write a scope as "unclear" when the work to clear it is already done and priced. State what
is settled, then name the single real unknown.

Voice: the field labels above are the required format rather than the bold-term pattern the baseline
bans. Write it so it could be pasted into the same channel where colleagues chase the PM for it,
because that is exactly where the copy goes.

**Hand the comment text to the PM's own voice skill if they have one, otherwise to `pm-voice`**,
rather than drafting it inline. A weekly status is the single most reliable place for a copilot
draft to come out two or three times longer than the PM would have typed, and the length budgets
live in the voice skill, not here. The field set above is fixed; the voice applies inside it. Say
nothing that the labels already say.

### Step 4 - propose the indicators

Show the current value of all eight beside the proposal, and flag only what should change and why.
Carrying a value forward unchanged is the normal case, not laziness.

| Field | ID | Options |
|---|---|---|
| Contract Quality | customfield_22759 | BLACK Predatory Terms / RED Financial Risks, Vague Scope / YELLOW Contractual Risks Present / GREEN Secure Framework |
| Handover Status | customfield_22760 | BLACK Total Uncertainty / RED Project Not Ready to Start / YELLOW Minor Scope Ambiguities / GREEN WBS Completed |
| Actual Budget | customfield_22761 | BLACK Margin at or below 0% / RED Low Margin under 20% / YELLOW Margin Dropped but Managed / GREEN High Margin |
| Budget vs Handover Baseline | customfield_22762 | BLACK Deficit Budget / RED Serious Underestimation / YELLOW Acceptable Buffer / GREEN Solid Estimation |
| Staffing Status | customfield_22763 | BLACK Unknown State / RED High Risk, Delivery Delays / YELLOW Performance Bottlenecks / GREEN Fully Staffed |
| Delivery Health Current | customfield_22764 | BLACK Blind Spot / RED Critical Impediments / YELLOW Minor Bottlenecks / GREEN Flawless Execution |
| Upsell Opportunities | customfield_22765 | BLACK Strictly No Growth / RED High Hesitation / YELLOW Budget Available / GREEN Highly Interested Client |
| Project Stage | customfield_22766 | Presale (SM) / Discovery (Team) / Development (Team) / UAT (Team) / Project Closure and Payment (SM) / SLA / Pause (Hold) |

SLA and Pause (Hold) are real options that the on-screen help text under the field does not list.

**Option IDs differ per field.** Resolve them from getTransitionsForJiraIssue with
`expand: "transitions.fields"`, which returns allowedValues carrying the id for each. Never assume
an ID from another field.

**All eight are optional, so a field you omit silently keeps last week's value.** Send all eight
every time, including the unchanged ones, so the card never depends on what a previous run happened
to set.

Put these to the PM rather than deciding alone: Contract Quality and Upsell are not derivable from
chat traffic; Project Stage is the field most often stale; and where an indicator is literally still
true but the trend has turned, ask whether to keep it or move it - that is a reporting choice, not a
fact.

CHECKPOINT, and this is the gate that matters most in the whole skill: show the eight-field draft
and the eight indicator values side by side with what is on the card now, then stop. "Here is the
status and the indicators - two of the eight would change, [which] and why. Post it?" Nothing goes
to a leadership-visible card on an implied yes.

### Step 5 - post

One call per card. The transition carries the indicators AND the comment together: transitionJiraIssue
with the cloudId, the issue key, `transition` set to id `"2"`, `fields` carrying all eight
customfields as `{"id": "OPTION_ID"}`, and `update` carrying
`{"comment": [{"add": {"body": ADF}}]}`.

The comment body must be ADF: a doc node, version 1, whose content is one paragraph node per field,
each with a single text child. No hardBreak nodes and no literal newlines inside the text - that is
what produces ragged rendering.

**What the transition actually does.** Transition 2 "Update PMO Metrics" moves the card to a holding
status of the same name (id 32784), and the response comes back showing that holding status. This is
expected, not a failure. A hidden automation then returns the card to its previous colour within
seconds - verified live on a real card, not inferred. The rules are conditional transitions
invisible to a normal getTransitionsForJiraIssue call (Yellow auto 3, Red auto 4, Closed auto 5).
There is no Green auto, so a card sitting on Green got there by a manual click.

So **read the status back.** Returned to the expected colour, done. Still in the holding status, run
the colour transition: **Green 41, Yellow 51, Red 61** (Green has no screen; Yellow and Red do).
Manual Closed is 21.

Before running the metrics transition on a card in an unusual status - Closed, or new - check with
`includeUnavailableTransitions: true` that a route back exists. Stranding a leadership-visible card
in the holding state is worse than skipping the week.

**Verify the write.** Success from transitionJiraIssue is not proof the comment rendered correctly.
Read the newest comment back and check for eight paragraph nodes, each starting with its field
label, no hardBreak, no literal newlines. Re-read the eight custom fields and diff them against what
was sent. If the comment history is too large to pull inline, delegate the check to a subagent
asking only about the newest comment - do not skip the verification because the read is awkward.

### Step 6 - hand over the strategy chat text

The PM posts this. Do not send it and do not offer to.

Per project, give them the exact text - identical to what went into the card, unwrapped, blank line
between fields, ready to paste with no editing - inside a code block so copying it picks up no
surrounding formatting. Plus the name of the target space, which follows the pattern
`(strategy) Client_Project`; look it up with list_spaces so the name is exact rather than guessed.

**The Jira comment goes out in English.** The strategy-chat post goes out in the language that
project chat actually runs in, which is frequently not English. Translate the same content, field
labels included, and hold the same length discipline. The baseline's notes on drafting in another
language apply.

### Step 7 - record it

Say which cards were posted and when, which indicators changed, which strategy-chat posts are still
outstanding on the PM, and anything else they still owe - an unanswered client question, a missing
number, a card in a status that contradicts reality. State explicitly what could not be established,
so next week starts from a known gap rather than re-discovering it.

Outstanding chat posts and anything owed go to `pm-tasks.md`. The card link, indicator changes and
any decision go to `project-context.md`. The status text is ordinary project knowledge - the money
ban has already kept figures out of it - so offer it to `project-brain` (feed mode) along with
anything else the session produced. The indicator VALUES are a different matter: Actual Budget and
Budget vs Handover Baseline are a margin signal in four words, so they stay out of the brain and out
of `project-context.md`. Read the hold-out list in `pmo-conventions.md` rather than deciding it here.

## Mode: review

Nothing else checks this, and an unreviewed card decays while looking maintained.

1. **Staleness.** When was the last status comment, and does the gap match the weekly cadence.
2. **Colour justification.** Is there anything written anywhere that justifies the current colour.
3. **Contradiction with reality.** A card in Closed while its last comment describes live work; an
   indicator that plainly no longer matches the project; a Project Stage from two stages ago.
4. **Coverage across the portfolio.** Run over every card the PM owns and report which are behind,
   because the question is usually "which of mine need doing" rather than "is this one fine".

Report what a head would get wrong by trusting the card as it stands, then offer to fix the specific
cards. A review that ends in a diagnosis with no proposed action generates a question instead of
answering one.

CHECKPOINT: "Last status [date] on [n] of your [m] cards. [Card] says Red with no written
justification since January. [Card] is in Closed with live work in its last comment. Want me to run
the update on these?"

## Traps worth remembering

**A repeated transition in the changelog is not evidence of a decision.** The weekly Red -> Update
PMO Metrics -> Red pattern is the automation restoring the colour, not the PM re-affirming it. A
card can look reviewed every week while its colour has not actually been revisited for months. When
a colour has no written justification anywhere, say so and make the PM choose - justify it in this
week's comment, or change it.

**A card's status can contradict its own last comment.** One card sat in Closed with a null
resolution while its most recent comment described live work. Read both, name the contradiction, and
let the PM decide which is right before posting on top of it.

**Only propose changes to indicators you have evidence for.** Reading the current values and
carrying them forward is the correct default - re-deriving eight judgement calls from a week of chat
produces drift, not accuracy.

**The status is not the PM's digest.** The failure mode on every first draft is a research brief:
per-person hours, ticket counts, board breakdowns, who chased whom. Eight fields, 8-14 lines, and
nothing a head would not act on.
