---
description: Implement exactly one ticket, end-to-end, strictly within its scope. Log everything else instead of fixing it, routed to the right owner.
argument-hint: [TICKET-KEY | path/to/TICKET-KEY.md]
---

# /work-ticket — implement one ticket, nothing else

Argument received: `$ARGUMENTS`

You are working on exactly **one** ticket. Follow the steps in order. Do not
touch code outside the scope defined in Step 1, except for the "blocking" case
in Step 4. Project-specific facts — components, verification commands,
environments, owner roles, forbidden actions — come from `PROJECT-PROFILE.md`.

## Step 0 — Resolve the ticket

Stop at the first that works:

1. `$ARGUMENTS` is a path to an existing `.md` file → read it.
2. `tickets/$ARGUMENTS.md` exists → read it.
3. The ticket's key, summary and acceptance criteria are present earlier in
   this conversation → use that.

If none gives a key, a summary **and** acceptance criteria, stop and ask. Do
not invent scope from a bare key; suggest `/draft-ticket <KEY>` instead.

**Status gate.** If the ticket came from a file, check `Status:`.
`CONFIRMED` → proceed. `DRAFT` or missing → stop: the spec has not been
reviewed. Summarize it and its Open questions and wait.

## Step 1 — Restate the scope (before touching any file)

- Ticket key, epic, one-line summary.
- Which component(s) this touches, inferred from the ticket's area and the
  profile's component map.
- **In scope**: the files/modules you expect to touch.
- **Out of scope, explicitly**: adjacent things that are tempting to fix too —
  named, so it is clear you are leaving them deliberately.
- **Related pre-existing findings**: grep, never read the journal whole:
  `grep -n -E -B 5 -A 8 "Likely owner ticket(\*\*)?: .*<KEY>" FINDINGS.md`.
  If the spec came from `/draft-ticket` they were already decided there.
  Otherwise list unresolved matches and ask whether to fold them in.

This is a plan you state and then act on, not a request for permission.

## Step 2 — Load context

- Read the `CLAUDE.md` / README of every component identified in Step 1.
- Load any project skill that matches the work.
- Re-read the profile's "Forbidden actions" and "Known, intentional breakage"
  for anything near the files you are about to touch.
- Measure the baseline of the checks you will run (tests, lint, build) before
  the first edit; documents' baselines are not trusted.

## Step 3 — Implement, strictly inside scope

- Touch only what the acceptance criteria need.
- Match the conventions of the files you edit; introduce no new patterns.
- No refactors, renames or cleanup of adjacent code.
- No functionality belonging to another ticket, however cheap — log it.
- Implement client formulas and rules literally. If the data contradicts the
  spec, implement the spec and log the discrepancy (Step 5C).
- Respect the hard rules: no fabricated fallbacks to mask missing data, no
  silent excepts, no hidden retries, fail fast, never rename existing
  environment variables, no ticket keys in code comments.

## Step 4 — Classify anything outside scope

If something is *broken* — yours or not — do not patch it by guessing. Use the
`systematic-debugging` skill to find the root cause first, then classify:

**A. Blocking** — you cannot implement or verify this ticket without touching
it → fix the minimum, say so in the report, and log it.

**B. Non-blocking** — a real issue, but this ticket works without it → do not
fix; log only.

Default to non-blocking. The bar is "I literally cannot finish or verify this
ticket otherwise", not "this seems related".

## Step 5 — Log every finding, routed to its owner

Nothing is dropped. **Who owns it decides where it goes.**

| Situation | Where it goes |
|---|---|
| Ours, and one of our tickets covers it | `FINDINGS.md`, `Likely owner ticket: <KEY>` |
| Another role owns it | `FINDINGS.md`, `Owner:` = that role (+ their ticket if known) |
| Ours, but no ticket covers it | `FINDINGS.md` **and** a new row in `BACKLOG.md` |
| The client's spec is wrong or impossible | `SPEC-DISCREPANCIES.md` |

Owner vocabulary: the role list in the profile. If you cannot tell, write
`Owner: unclear — needs triage` and say so in the report.

### A. Append to `FINDINGS.md` — always, for every finding

Append only, with a CLI append (`cat << 'EOF' >> FINDINGS.md`). Never load the
file to rewrite it; never edit or delete earlier entries. Use the entry
template at the top of the file; keep its labels character-exact — other
commands grep for them.

### B. Ours, no ticket → also a row in `BACKLOG.md`

Add rows only, with the next free number; never edit, merge or delete existing
rows. Propose a priority; the decision to open a tracker ticket is not yours —
say in the report which existing ticket the item wants to be attached to, or
that it needs a new one.

### C. Spec discrepancy → `SPEC-DISCREPANCIES.md`

Grep first — a duplicate entry hides which one is authoritative. Classes:
`SUSPECT` (implementable literally, data contradicts it — implement literally),
`FORCED DEVIATION` (cannot be implemented as written — record the substitution
and name it in the report).

## Step 6 — Verify before declaring done (lean)

Apply the `verification-before-completion` skill: no "done / fixed / works"
claim without a fresh command output read in this session.

- Add or update unit tests for the code you changed, in the project's
  existing test style.
- Run the profile's verification-matrix row for every component you touched.
- If the ticket changes behaviour or data, exercise it for real (request,
  screen, CLI run) and read the actual output, not the status code.
- If the fix came from a bug, rerun the reproduction that showed it broken.
- If the project has a regression set and you touched what it guards, run it
  before and after and report the delta.
- If something cannot be verified because infrastructure is missing, say so.

Keep it lean: touched tests while working, the full set once at the end.
Exhaustive testing is the tester's job — when your checks pass, stop.

## Step 7 — Final report

1. What was implemented, file by file, mapped to each acceptance criterion.
2. What you verified and how — exact commands, exact results.
3. Findings recorded, grouped by owner (ours with a ticket / another role's /
   ours without a ticket + the `BACKLOG.md` row / spec discrepancies).
4. Any blocking fix outside the nominal scope, and why it was unavoidable.
5. If this ticket resolved a pre-existing finding, set that entry's `Resolved`
   field in place to `yes — <KEY>, <YYYY-MM-DD>` — the one allowed edit to an
   existing entry.

Git and tracker writes belong to the dispatcher, not to this command.
