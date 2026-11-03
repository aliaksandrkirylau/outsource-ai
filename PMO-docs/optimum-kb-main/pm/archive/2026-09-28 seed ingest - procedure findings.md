# 2026-09-28 seed ingest - procedure findings

Final, after batches 1 to 7 and the two meetings of 2026-09-28 (claude-code/claude-opus-5-5, for Anton).
Where AGENTS.md, schema/types.md, the procedures, the templates, the lint or the environment were
unclear, wrong, missing or slow, with the case that showed it. "Fixed" means changed with Anton's
approval: in commit b4cb7da (the rules change before batch 1), 56ca5db (rule 6) or d6eb286 (images).
Findings 1 to 31 come from batches 1 to 3, 32 to 39 from batch 4 (the WBS), in a session started on the
main checkout without a worktree, as finding 1 advised; that worked. Findings 40 to 45 come from batch 5
(the presale chat), 46 to 54 from batch 6 (the contract and economy chats), 55 to 61 from batch 7 (the
client images), 62 to 66 from the two meetings of 2026-09-28 (the 11:00 call and a 1:1). The summary of
the seed itself: [[2026-09-28 seed ingest - summary]].

## What to change, in order

The open findings as changes, most important first. All are the curator's to make; changes under
`tools/` are made by hand (finding 2).

Applied 2026-09-28 with Anton's approval: 4, 9, 12 and 13 in the schema v2 commit (9b1b639; since
change 13, agents may edit `tools/` after asking); 1, 3, 5, 6, 7, 10 and 11 in the procedure-text
commit after it. Open: 2 (waits for the PMO Drive folder) and 8 (Anton's call). 14 needs no rule.

| # | Change | Where | Findings |
|---|---|---|---|
| 1 | Delete downloaded originals after rendering: the Drive tool leaves them in `~/.workspace-mcp/attachments`, contract PDFs with amounts and personal data among them | ingest.md step 2 | 6, 61 |
| 2 | A home for redaction maps, which hold the figures they remove: the PMO Drive folder, next to the P&L, once it exists | ingest.md step 2; AGENTS.md "Where the rest lives" | 47 |
| 3 | Check a new Decision against what the Commitments and the SOW deliver, whatever their status, not only against stable notes | ingest.md step 6 | 66 |
| 4 | A step that asks a PM to name the deciders, and a way to propose a Decision whose deciders are still to be named; six of the eleven Decisions have none | ingest.md step 7; schema, Decision; kb-lint | 24 |
| 5 | Say which parts of a source folder are ours and may be edited (overviews, minutes, result marks, link swaps), and that trust notes are schema | AGENTS.md rule 1; `sources/AGENTS.md` | 16, 17, 51 |
| 6 | Meetings: Bluedot first, and check the transcript's language before using a summary; from a 1:1, only the project parts; a remark about a person with no project content is redacted; a remark that could embarrass a colleague and adds little goes to the person | ingest.md steps 1, 2 | 43, 62, 64 |
| 7 | Redaction: normalise whitespace first, treat a redaction that matches nothing as an error, and when a header says money but the cells hold hours, check the formulas | ingest.md step 2 | 33, 48 |
| 8 | Say whether a source's own precedence clause settles a dispute; four Commitments are disputed over the contract's "the Agreement prevails over the SOW" | AGENTS.md rule 3 | 29 |
| 9 | Supersede in part (link, and the older Decision's Consequences say what no longer holds), and `valid_from` as the earliest day a source shows the decision agreed | schema, Decision; AGENTS.md rule 4 | 53, 54 |
| 10 | Batch order and handoffs: store the scope references (SOW, WBS) and the chats that explain documents first; a note naming a source not yet stored uses a placeholder; a handoff carries file IDs, and its counts are rechecked at ingest | ingest.md steps 3, 4 | 20, 34, 36, 37, 38 |
| 11 | Small rules: bot messages that relay a person's words; the date of a living document; estimates in the internal and presale trust notes; link-only for money chats; the formula convention; thumbnails listed, not rendered; check who is speaking and name people only from sources; the wording of a row's result; counts from the scripts, not by hand | ingest.md; the two trust notes | 21, 22, 35, 42, 44, 45, 50, 52, 56, 58, 65 |
| 12 | Schema and lint: `wbs` as a list; `party: both`; no `acceptance_measure` demanded of a disputed requirement; one default status in the Question template | schema/types.md; kb-lint; templates | 25, 26, 27, 28 |
| 13 | Environment: start KB sessions without a worktree and say so in the README; `ask` instead of `deny` for `tools/**`; allow read-only git in the forms agents use; point PowerShell users to `sync-kb.cmd`; strip the tab kb-money reads after a file name with spaces | `.claude/settings.json`; README; AGENTS.md; `tools/kb-money.pl` | 1, 2, 3, 4, 8, 32 |
| 14 | For agents, no rule change: scripts with regexes go in files; write LF; read chats in full, paging by `createTime`, and render them with `chat2md.mjs`; Bluedot through `bluedot-json2md.py`; absolute paths, never a bare `cd` | this note; the handoff | 5, 7, 40, 46, 60, 63 |

Fixed during the seed, keep: 8 (the money gate), 9, 10, 11, 12, 13, 39, 55, 57 and 59; 1 in part (the
AGENTS.md wording). Closed by a source: 30 and 31 (QUE-006).

## Environment and syncing

1. **Worktree sessions cannot write the KB.** The desktop app starts a session in a git worktree on a
   side branch; its hook then blocks Write/Edit on the main checkout, and moving the session is refused.
   kb-sync rightly refuses the side branch. Worked around by writing into a scratch copy and copying
   with `cp`, with Anton's OK. AGENTS.md said "from the repo root" - fixed to "the main checkout, on
   main, never a worktree". Still open: start KB sessions without a worktree, and say so in README.
2. **The curator's agent cannot edit tools.** `.claude/settings.json` denies Write/Edit on `tools/**`,
   while AGENTS.md "Changing the schema" tells the agent to update `tools/kb-lint.mjs`. Anton copied
   the tools change himself. Suggest `ask` instead of `deny`.
3. **`git -C` is denied**, which also blocks read-only checks written that way (AGENTS.md allows
   read-only git). Minor; use `cd` first.
4. **Commands handed to a person run in PowerShell 5.1** (no `&&`); a bash command failed in Anton's
   terminal. AGENTS.md tells people `bash tools/kb-sync.sh`; in PowerShell `bash` may be WSL or missing.
   `sync-kb.cmd` exists but AGENTS.md does not mention it.
5. **The shell tool eats backslashes** in inline commands (a regex written through a heredoc lost its
   `\b`). Scripts with regexes must be written as files, not inline.
6. **Downloads land outside the repo silently.** The Google tools save attachments to
   `~/.workspace-mcp/attachments`; the contract PDFs with amounts and personal data sat there until
   deleted. The ingest procedure should say: delete downloaded originals after rendering.
7. **Python on Windows writes CRLF** (the first-call transcript); git normalised it. Scripts should
   write with `newline="\n"`.
32. **The deny list also catches read-only commands.** `git branch --show-current` falls under
    `Bash(git branch *)`, as `git -C` does (finding 3): the first two checks of batch 4 were refused.
    `git status --short --branch` gives the branch instead. Allow `git branch --show-current`, or say
    in AGENTS.md which form to use.
40. **The chat search misses messages.** The Chat search tool found nothing in the presale chat for
    "DevOps", "spreadsheets" or "EST", though "DevOps done" and dozens of sheet links are there. Chats have
    to be read in full. The read tool has no page token; paging with `createTime > "<last message>"`
    works.
41. **No chat export.** Each of the 446 rendered messages of the presale chat was rewritten by hand from
    the tool's output; the one control was the count (304 + 142 rendered, 15 left out, 461 as the
    handoff said). An export (Takeout, or a script against the Chat API writing the rendering) would make
    chat renderings reproducible and cheaper; the contract chat (batch 6) is longer.
46. **A script renders chats now (finding 41).** Read with a page size of 1000, the Chat tool's result
    is too large for the conversation, so the agent app saves it as a file. `chat2md.mjs` (in
    `pm/seed-ingest-scripts/`) turns that file into renderings by period: it leaves out bot, system and
    empty messages and counts them, applies a redaction map by message key and warns "NOT FOUND" when a
    redaction does not match, masks e-mail addresses and Drive user IDs, and prints the counts per
    part. The contract chat's 665 messages were rendered this way in three parts. Checked against the
    batch 5 hand rendering of the presale chat: 438 of 446 messages identical, and one of the eight that
    differ is a real deviation (list dashes added by hand in the 2026-05-15 13:46 message). Rule 1 keeps
    the stored rendering as it is; the deviation is recorded here. Use the script for every chat
    rendering from now on.
47. **The redaction map has no home.** It holds the figures it removes, so it cannot be in the repo; it
    sits in the session's scratchpad and goes with it. Re-rendering the contract chat, or adding a part
    that quotes earlier messages, needs it. Suggest the PMO Drive folder once it exists, next to the
    P&L. For now (2026-09-28): a copy in Anton's My Drive, private. The map also held two Zoom links with
    their passwords, as the text to remove; those were left out of the Drive copy, so a map should name
    what it removes without keeping a credential, or keep credentials to a pattern the script masks.
60. **A `cd` inside a command moves the session.** Twice in batch 7 the app took the working directory
    from a `cd` in a shell command, so later relative paths would have resolved in `knowledge/` or a
    source folder. Use absolute paths, or end the command back at the repo root.
61. **Downloads again (finding 6).** The Drive tool saved the 20 PNGs of batch 7 to
    `~/.workspace-mcp/attachments`, next to earlier downloads. Nothing in them needed removing, but the
    step "delete downloaded originals after rendering" is still missing from ingest.md.

## The money rule

8. **Nothing ran the lint.** kb-sync's header promised "5 = lint refused the commit" but only checked
   conflict markers; the pre-commit hook the same. A figure would have reached GitHub if anyone skipped
   the lint. Fixed: `tools/kb-money.pl` runs in kb-sync (STOPPED, exit 5) and in the pre-commit hook;
   the self-test covers it. It then caught two examples in this very note and the handoff on the
   first sync. One bug found that way: for a file name with spaces git adds a tab after the name in
   the diff header, so kb-money.pl reports "name.md<TAB>:45"; the check still works. Fix: strip the
   trailing tab when reading `+++ b/` (curator).
9. **The old money pattern caught only currency codes and symbols.** It missed a rate written as a
   number with "/h", a "k" suffix, "тыс.", amounts in words ("Thirty-Two Thousand ... Dollars"), Arabic digits, and figures split from
   "USD" by a PDF line break. Fixed: one shared rule file, tested on samples, the contract and the KB.
10. **"Money amount" was undefined** - margin %, discount %, payment-split %, rates. Fixed in
    ingest.md step 2 (what is removed, what stays). Anton's line: facts without figures stay.
48. **Non-breaking spaces defeat redaction by text.** Three figures in the client's letter of 7 July
    2026 did not match their redactions, because the letter used non-breaking spaces inside the
    numbers. The warning caught it; the script now turns them into plain spaces before matching. Add to
    ingest step 2: normalise whitespace before removing text, and treat a redaction that matches
    nothing as an error.
49. **The screen's false positives are reviewed by hand.** In batch 6 it flagged "К 11" (read as
    thousands) and "100% выполнения" (a completion condition, not a payment share). Both kept, after
    reading them. The screen cannot tell those apart and should not try; the review step is the right
    place. One hard hit was real enough to stop a sync: a regex backreference `"$1"` in `chat2md.mjs`
    reads as a dollar amount. Rewritten as a function. Scripts in the repo should avoid a dollar sign
    before a digit, as formulas do (handoff, batch 7).

## Sources and the ingest procedure

11. **No path for a source that cannot be rendered** (a 480 MB call recording without a transcript,
    videos). Fixed: `kind: link-only` overviews.
12. **No rule for versions** (SOW drafts, contract rounds, question drafts). Fixed: render what someone
    relied on, list the rest in the latest overview, `supersedes` on the overview.
13. **No rule for long or ongoing chats** (461 and ~670 messages, the contract chat still active).
    Fixed: parts by period, a new part per ingest.
14. **The procedure is per source; a batch is not.** Six related sources fed the same notes; there is
    no place for one table. Put it in the main source's overview and pointed the others to row numbers.
15. **A recorded meeting with only someone's notes** is not covered (Bluedot, or "notes when
    unrecorded"). Stored as `meetings/` with `- notes.md` and minutes.
16. **Correcting our own minutes has no rule.** Batch 1's minutes said "no transcript exists"; batch 2
    found the transcript (the source register had called it a "call script PDF"). Rule 1 forbids
    editing a stored source, yet step 8 edits overviews and minutes (marking rows). Used a
    "- minutes 2" that says what it corrects. Say whether minutes and overviews are sources.
17. **Rule 1 literally covers the folders' trust notes** (`sources/*/AGENTS.md`); I edited
    `sources/contract/AGENTS.md` in the rules change. Say trust notes are schema.
18. **Naming.** "`<name>/`" for documents has no date; Drive names collide ("Questions"). Used
    "`<YYYY-MM-DD> <title>`" for every source folder.
19. **An overview written before approval cannot link the notes it proposes** (lint: broken link).
    Used plain text ("proposed note COM-012, row 12").
20. **Batch order against the scope check.** The scope check needs the WBS and the SOW, but they came
    in batches 3 and 4, so notes named them in plain text and were re-linked later (22 notes for the
    SOW; the WBS links are still pending). Store the scope references first.
21. **Speaker labels in transcripts are not checked.** Bluedot labelled nearly all client speech
    "Zahra Ahmed"; the speaker introduces himself as Lawal, the general manager. Add a step: check who
    is speaking before quoting a person.
22. **"Mark each row" (step 8) gives no wording**; used "applied <date>" and "recorded <date>, no
    note".
23. **Count from the original.** The Q&A register has 8 assumptions (items 2 to 9); the harvest said 9.
33. **A header can say money when the cells hold hours.** Two WBS columns headed "Rate, USD/hour" hold
    hours: the max plus 15% (a formula) and the max plus 10 hours taken from "Other" (typed in).
    Dropping them by the header loses data; keeping them by the values is a guess. The formulas and two
    chats settled it (Arseniy in [Core]: "обычные часы + стабилизация"; Marina Zaretskaya in the
    contract chat: "это не рейт"). Add to ingest step 2: when a header and its cells disagree, check
    the formulas, and say in the rendering which it is.
34. **A handoff named files without links.** The four link-only companions of the WBS (old estimate,
    DevOps estimate, resource plan, April hours plan) came with names only, and Drive search finds
    neither them nor the WBS sheets themselves, which are shared by link. Moved to batch 5. A handoff
    should carry file IDs.
35. **A living spreadsheet has no date.** The folder name needs one. The v1 WBS says "Created
    05.07.2025" (a template value, from before presale), its Flutter tabs came later, and Drive gave no
    metadata. Used the day it was named the current WBS, 2026-09-25 (Anton kept it). Say which date a
    living document takes: the day someone relied on it, or the day it was read.
36. **Linking a source the notes named without a placeholder.** 26 notes said "v1 WBS" with no
    "(stored in batch 4)" placeholder, so `link-source.mjs` did not fit; wrote `link-mention.mjs`
    (links the first plain mention, skips text inside a wikilink - the new link's own name contains
    "v1 WBS"). Batches 1 to 3 used the placeholder for the SOW but not for the WBS. Rule: a note that
    names a source not yet stored uses the placeholder.
37. **Batch order, again (finding 20).** Batch 4 needed three contract-chat messages (the WBS sent on 5
    November; "это не рейт"; the grand total is "сложить") that batch 6 stores. Cited in plain text,
    "(stored in batch 6)". Chats that explain documents should come in before the documents, or with
    them.
38. **A chat changes between sessions.** The handoff said the [Core] chat had one message; by batch 4 it
    had two (Mikhail's results of the 2026-09-28 call). That message belongs to the call's ingest. A
    handoff's counts are a snapshot; recount at ingest.
42. **Bot messages can carry a person's words.** The sales tool's feedback form came back as a bot
    message ("Proposal Review - не проводили ввиду нехватки времени между финализацией решения и митом с
    клиентом", 2025-11-17). The rule leaves bot messages out; the answer was quoted in the overview. Say:
    leave out bot messages unless they relay a person's input.
43. **No rule for a personal remark.** One message was a heated personal remark to a colleague. The rules
    remove money, personal data and credentials, not conduct. Redacted in place with its project content
    kept as a note; Anton kept the redaction. Add: a remark about a person that carries no project content
    is redacted and marked, and the overview says so.
44. **"Estimates" fits two folders.** The trust notes of `sources/internal/` and `sources/presale/` both
    list estimates. Filed the current WBS in internal (the scope reference) and the superseded presale
    estimates in presale. Say so in the two trust notes.
45. **Authors that cannot be named.** "Deleted User" and a bare user ID wrote real content: the May 2026
    review of the estimate and a consultant's reading of the client's formulas. Rendered as the chat
    shows them, not guessed. When it matters who said it, a PM has to ask. The contract chat has the
    same: PMO's finalisation of 28 November 2025 ("TM with Budget CAP") is by "Deleted User".
50. **Counts and names written by hand go wrong.** Re-reading my own overviews caught three errors: the
    contract chat's money was said to be in 28 messages (23), the economy chat to have 58 messages
    (55), and a presale remark was given to "Anton Snotov" where the chat does not say which Anton.
    Take counts from the script's output, and name a person only as the source names them.
51. **Placeholders sit in stored sources too.** Batch 4 wrote "(stored in batch 6)" in two overviews
    and a rendering, so linking them in batch 6 meant editing three files under `sources/`, which rule
    1 forbids; done as link swaps only, as the handoff said, and logged. Same question as findings 16
    and 17: say which parts of a source folder are ours (overviews, our annotations in a rendering) and
    may be edited.
52. **A chat that is mostly money.** The economy chat has almost nothing without a figure. Anton's call:
    link-only, with the non-money facts dated in the overview's summary. That worked; ingest.md could
    name it as the path for P&L and pricing chats.
55. **Images have no way into the KB.** Step 2 keeps "images" in Drive and step 3 stores the original
    "only if it is small text", so batch 7 carries ten formula pages and charts as text only. For a
    formula or a chart the image is the clearer reference, and Anton asked whether the images can come
    in. The tools already allow it: `.gitattributes` marks `*.png` binary, kb-lint resolves
    `[[file.png]]`, and kb-money skips binary diffs - which also means the money screen cannot read an
    image, so a person has to look at each one. Needs a rule: which images, how large, checked by whom.
    Fixed 2026-09-28 with Anton's approval: ingest.md step 2 lets an image under 1 MB come in with its
    rendering, looked at first by a person or their agent, named `<name> - image 01.png` and embedded;
    the ten batch 7 images came in that way (2.4 MB).
56. **No convention for typeset formulas.** Wrote each as one line of plain text with a key (`_`
    subscript, `^` power, `sqrt()`), in code blocks, and marked the readings that could go two ways
    (an exponent set above and after "Re"). No dollar signs, as the handoff advised; the screen still
    flagged "100 K_a" three times as thousands (finding 49). Put the convention in ingest.md.
57. **Drive file names are not titles.** The ten names look machine-made ("Dating luil-40.png",
    "100-108-918s-1214a-o-polval-34.png"), are numbered 24 to 43 as if cut from a longer document, and
    one has a character-set error ("ΓåÆ-Fieto-24.png", an arrow read in the wrong code page). The
    rendering names each image by its own heading and keeps the Drive name. Images stored in the repo
    need names of our own: unique, and plain ASCII.
58. **Thumbnails.** The folder has a "-small-" copy of each image. Compared by the PNG headers (same
    aspect ratio, 256 pixels on the long side) and one by eye: scaled copies, not rendered. ingest.md
    could say: a scaled copy is listed, not rendered.
59. **Third-party material from the client.** The pages look cut from a published manual and the
    screens from a commercial program; the client named neither. The procedure has no rule for the
    copyright of what the client sends. The images stayed in Drive and the rendering keeps to formulas
    and labels; the overview says so. If images come in (finding 55), the rule should say internal use
    only, never in an export. Fixed 2026-09-28 with Anton's approval: stored images are internal
    reference only (ingest.md step 2) and export.md step 3 strips them. Copyright itself is still not
    checked; Anton's call was to keep a reference copy.
62. **Gemini's notes are useless for a call in Russian.** The 11:00 call's Gemini transcript renders the
    Russian speech as English fragments ("Foreign speech. Foreign speech", "bread."), and its summary is
    built on them ("contract pricing", "mobile pre-sale timelines"); Bluedot had the call in Russian.
    The handoff pointed to the Gemini notes. Say in ingest step 1: for a recorded meeting, look in
    Bluedot first, and check the transcript's language before using any summary. The participant's own
    results (Mikhail's [Core] message) were quoted in the minutes, not stored as a chat source.
63. **Bluedot's result is too large for the conversation.** `get_meeting` returns word-level JSON
    (about 300,000 characters for 30 minutes); the app saves it as a file. `bluedot-json2md.py` (in
    `pm/seed-ingest-scripts/`) groups the words into speaker turns, as the PDF route
    (`bluedot2md.py`) did, and writes Bluedot's summary next to it for reading.
64. **A 1:1 is mostly not project knowledge.** Of 45 turns, 23 were about Optimum; the rest were an
    audit of another project, feedback, a career topic and another project's close, one with figures.
    The procedure has no rule for storing part of a meeting. Kept the project turns verbatim and marked
    every other turn in place. One project remark was sensitive rather than personal (starting before
    the formal staffing approvals): kept out by default and put to Anton. Say in step 2: from a 1:1,
    only the project parts; a remark that could embarrass a colleague and adds little, ask the person.
    Also: the recording started a few minutes late, so the first turn begins mid-sentence; the header
    says so.
65. **People by first name only.** The calls say "Леша", "Миша", "Ваня", "Леша Титов", "Паша Мальцюк";
    identified in the minutes as "most likely" from other sources (DEC-009 names Ivan Shatuho and
    Michael Labutin as approvers), "Ваня" at 00:04:37 left unidentified. Same as finding 21: a name in a
    note comes from a source, never from a guess.

## Types and fields

24. **`deciders` must be `human:<innowise id>`**, so a decision taken by the client (the desktop is the
    client's "first and foremost" requirement) cannot name its decider. DEC-005 and DEC-006 have none.
    Batch 5: DEC-007 (Flutter) has no named decider either, and the lint refuses a proposed Decision
    without deciders, so it stays draft although it is ready for the deciders to confirm. Allow
    `proposed` with the deciders to be named, or let a Decision record "decided by: not stated".
    Batch 6: the contract chat shows Arseniy's approval of Flutter (2026-05-25), and Anton named him as
    the decider, so DEC-007 is proposed. DEC-008 (fixed price, a call of 22 May 2026) and DEC-009
    (signing as is, "решение со стороны менеджмента", 4 September) name who attended or was copied, not
    who decided; both stay draft. Anton: "pretty much a go for project, but we will try to follow the
    procedure anyway". The procedure has no step that asks a PM to name the deciders; the handoff
    carries it.
25. **`wbs` is one line**, but most requirements span a web line, a desktop line and group rows. Used
    the main line and named the rest in the body.
26. **Commitment `party` is us or client only**; non-solicitation, written minutes and termination bind
    both. Wrote "both" in the body.
27. **Lint versus schema on disputed requirements.** The lint demands `acceptance_measure` for any
    status but draft, so a disputed requirement fails; the schema asks for it "once proposed". Gave
    REQ-004 a neutral measure. Treat disputed like draft here.
28. **The Question template defaults to `proposed`**; the first ingest wrote Questions as `draft`.
    Pick one.
29. **Rule 3 against a contract's own precedence clause.** The contract says the Agreement prevails
    over the SOW (1.3), yet rule 3 says keep both and mark disputed. Followed rule 3: four Commitments
    disputed. Say whether a source's own precedence rule settles a dispute.
30. **A person's statement in the session is not a source.** Anton confirmed SOW v10.4 as the working
    SOW "in chat"; recorded in QUE-006 as his statement, to be cited from the contract chat in batch 6.
    The procedure has no way to record "the PM told me" until the underlying source is stored.
    Batch 6 closed it: QUE-006 now cites Yauheni Krasner's message in the contract chat ("это должен
    быть по идее финальный SOW").
31. **`scope_status: contracted`** is "stated in the contract, SOW or WBS" without saying which SOW;
    it became QUE-006.
39. **Rule 6 and the initial estimate.** Rule 6 keeps estimates and hours in Jira and the P&L, so the
    batch 4 notes name WBS lines but carry no hours; the hours are only in the WBS rendering. Several
    points are clearer with them (the cloud DevOps tab against the on-premises one, the calculator
    estimated "per 1 algorithm"). Anton, 2026-09-28: initial estimates could go into the KB "if it makes
    sense". Fixed 2026-09-28 with Anton's approval: rule 6 and schema/types.md now let a note quote the
    initial estimate of a WBS line as history, citing the WBS version; current estimates and hours
    spent stay in Jira and the P&L. Hours added to CON-002, CON-003, REQ-007 and REQ-008. The lint does
    not check either way.
53. **No partial supersede.** DEC-009 (sign the client's final contract as it stands) overturns the
    second half of DEC-008 ("дорабатываем ее под свои условия"), not the fixed price. Rule 4 and the
    schema's "propose this as superseding it" have no case for a part. Both are draft; DEC-008's
    Consequences say so and leave it to the deciders. Say: supersede when the core of the choice
    changes; otherwise link, and the older Decision's Consequences record what no longer holds.
54. **Which day is `valid_from`?** DEC-002 (senior engineers first) has 2026-09-25, the sync where it
    was recorded; the contract chat shows the same line agreed on 7 September. The schema says "the
    day it was decided, never earlier", but a decision restated at a later meeting has two days. Left
    for the decider; say that `valid_from` is the earliest day a source shows it agreed.
66. **The contradiction check missed a deliverable.** DEC-010 (prototypes in code, no designer at the
    start) was proposed without noticing that Milestone 1 delivers a "UI Kit" and "Main UI/UX mockups",
    and every later milestone builds on the approved UI Kit (COM-020, the SOW v10.4). Anton caught it at
    approval. Step 6 checks contradictions against stable notes; the Commitments are draft, so nothing
    prompted the check. Say: a new Decision is checked against what the Commitments and the SOW say is
    delivered, whatever their status. The same check did catch the 7 September line in DEC-009, because
    it was a quoted sentence, not a deliverable in a table.

## What the rules got right (keep)

- The money screen now catches what matters, and the gate made the chat and contract batches safe to
  sync.
- "Invent nothing" caught a real error: the first ingest wrote that the desktop "was a requirement of
  the client's leadership" from a bare "Да"; the transcript shows the speaker then said he could only
  assume. Corrected in batch 1.
- Keeping both versions surfaced the three payment schedules, the SOW's references to another contract
  version, and the client's report and role definitions, instead of one silent pick.
- Reading the formulas, not only the values, showed what the WBS values could not: the roll-up counts
  MVP lines only, the "rate" columns are hours, and the "MLT" columns add up the wrong rows.
- Checking the notes against the stored source: every WBS row and assumption number cited from the
  harvest in batches 1 to 3 matched the sheet.
- Storing the version sent to the client next to the internal one surfaced what the client was shown
  and the current estimate dropped: mobile and the wizard in the MVP, "per 1 algorithm", an on-premises
  DevOps tab with a desktop update pipeline.
- Counting the chat against the handoff's number (461) caught nothing missing, and cross-reading the chat
  with the sync transcript dated the "40 минут" estimate to 5 November 2025, about ten months before the
  sync, not "больше года назад".
- Keeping the disputed Commitments disputed while adding the negotiation: fourteen Commitments now
  say how their clause came about, and the September risk list says which risks were accepted knowingly,
  without the agent settling any dispute.
- Waiting for the source instead of relying on a person's word (finding 30): the chat confirmed SOW v10.4
  as the final SOW in a teammate's words, with the caveat that there was no frame in Word.
- Reading the client's samples against the notes (batch 7): the "flow window" the client asked for on
  the first call is a chart in its own program, the daily report's hydraulic fields (n, k, ECD, critical
  velocities) are what the procedures compute, and the team's presale count (4 + 3 + 2 + 1) adds up to
  the ten images. It also showed what the samples lack: units, a named source, one rheological model.
- The page-creation gate: ten images of formulas produced two new notes (QUE-008, TRM-009) and seven
  updated ones, not a note per formula.
- Reading the transcript, not the summary: the 11:00 call was about staffing, discovery, prototypes and
  the decision-maker's language, none of which Gemini's summary shows.
- Keeping both versions (rule 3) with a decision still in the making: the two proposals of 28 September
  run against a line of the 7 September management call; the line is quoted in both Decisions and in
  DEC-009, and nobody but the deciders settles it.
