---
description: Adjudicate a proposed epic plan against the actual codebase and running system. Every claimed dependency is a hypothesis to falsify. Produces a VERIFIED plan with a re-derived ticket order and updates the spec-discrepancy register with evidence.
argument-hint: [EPIC-KEY | path/to/<EPIC-KEY>-plan.md]
---

# /verify-epic-plan — turn a proposed epic plan into a verified one

> Scope note: epic decomposition belongs to the future BA/PM stage of the
> pipeline. This command is kept because it ran on the reference project and
> its method (claims as falsifiable hypotheses, scope line) carries over.

Argument received: `$ARGUMENTS` (an epic key)

The plan was written **outside the repository**, from business documents, by
someone who could not run a single command. Every dependency it asserts is a
**hypothesis**, and some of the documents it was derived from are likely wrong
about the code. Your job is to arbitrate between the documents and the code.
**The code wins, always.** A refuted claim is the product of this step, not a
failure.

You implement nothing and fix nothing here. You read, run read-only checks,
adjudicate, and write.

## The scope line

> **Fidelity to the client's specification is in scope. Correctness of the
> specification is not.**

Every claim carries a `Scope`:

| `Scope` | A verdict may… | A verdict may **not**… |
|---|---|---|
| `mine` | move tickets, add or remove dependencies, change the order | — |
| `spec` | update the entry in `SPEC-DISCREPANCIES.md` | become a blocker, reorder tickets, land in `FINDINGS.md` |
| `external` | push a ticket later, or gate the epic's acceptance | block the start of implementation |

A confirmed `spec` defect is not a reason to delay a ticket or to correct a
client formula. The exception: a spec that is **impossible** to implement (a
named field or entity does not exist) forces a substitution — flag it for the
ticket's report as well as the register.

## Step 0 — Resolve and gate the plan

Read `$ARGUMENTS` if it is a file, else `plans/$ARGUMENTS-plan.md`, else a plan
pasted earlier. Without an epic key, a ticket list and a set of claims, stop
and ask.

Status gate: `PROPOSED` → proceed. `VERIFIED-DRAFT` → ask whether to re-run.
`CONFIRMED` → do not overwrite.

## Step 1 — Validate the plan's shape

Each claim must carry `Scope`, `Type` (`hard-dependency` | `soft-dependency` |
`external-blocker` | `fact`), `Asserts`, `Source`, `Verify` (a concrete grep,
path, query, request or test), and `If refuted` / `Action`. A claim without
`Verify` cannot be adjudicated; if more than a couple lack one, stop and report
the plan is not in a verifiable shape. Do not invent verification methods.

## Step 2 — Establish what you can actually check

State plainly which components are present, which files are dirty, whether
the system and its data store are reachable (per the profile), and which
checks therefore cannot run. An unavailable check never silently becomes a
pass.

## Step 3 — Adjudicate every claim

Run its `Verify`, read the output, assign one verdict: `CONFIRMED`, `REFUTED`
(record what is true), `PARTIAL` (say which part fails), `UNVERIFIABLE` (say why).

- Evidence is a file path with a line, or a command with its output. Not a
  recollection, not "the docs say so".
- A claim about behaviour needs a request, not a read: a success status often
  accompanies empty or wrong data.
- A claim about data needs a query against the real store, not a schema file.
- For "nothing implements X", one empty grep is weak — try synonyms, other
  spellings and neighbouring modules.
- Something broken → `systematic-debugging` for the root cause; record, do not
  patch.

## Step 4 — Re-derive the order

Rebuild the order from surviving `mine` and `external` claims, then diff it
against the proposal. Principles, in priority order:

1. Hard dependencies first.
2. Unknown mechanisms early, repetitive work late.
3. One thin vertical slice before the wide ones.
4. Externally blocked tickets late, unless the block can be lifted by asking today.
5. Optional, lowest-value tickets last.

Every moved position gets one line naming the verdict that moved it.

## Step 5 — Preconditions

Three buckets, never conflated: **blocks implementation** (expect it empty),
**blocks acceptance**, **blocks other people** — each with owner and whether it
must be requested now. Also list unresolved `FINDINGS.md` entries whose owner
ticket falls inside this epic (grep, do not read whole).

## Step 6 — Update `SPEC-DISCREPANCIES.md` in place

For each `spec` claim: grep for its entry, update only its `Verified` field
with date, method and the actual numbers. No entry → append one, grep first.
A refuted entry is not deleted; `Verified` says it was refuted.

## Step 7 — Log new code findings

Code defects only, to `FINDINGS.md`, using its template, after a dedup grep.
Facts, not speculation about why.

## Step 8 — Write `plans/<EPIC-KEY>-plan.verified.md`

A new file — keep the proposal beside it. Sections: verdict summary for
`mine`/`external` claims (claim, scope, type, verdict, evidence); verdict
summary for `spec` claims; final order with "changed from proposal?"; open
decision points; preconditions in three buckets; pre-existing findings owned
by the epic; forced deviations needing a note in a ticket report; what could
not be verified. Status `VERIFIED-DRAFT`.

## Step 9 — Report

Lead with what changed: refuted and partial `mine` claims, the final order and
every move with its cause, `spec` verdicts with numbers, preconditions to
request today, new findings, what could not be verified.

No git operations; no source changes.
