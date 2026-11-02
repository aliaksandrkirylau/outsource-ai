---
name: verification-before-completion
description: Use when about to claim work is complete, fixed, verified, or passing — requires running the real verification command from the project profile and reading its output (and the actual data) before making any success claim. Evidence before assertions, always.
---

# Verification Before Completion

**Core principle:** evidence before claims, always.

The trap this guards against: systems that answer **"success" with empty or
wrong data** (a query against a misspelled table returns zero rows without an
error; a dropped filter returns everything), components with thin or no tests,
and old status notes ("fully done and tested") that turn out to be false. "It
should work" and "the code looks right" are worth nothing — only a fresh
command output or a real request/response counts.

## The Iron Law

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you have not run the verification in this session and read its output, you
cannot claim it works.

## The Gate

```
BEFORE claiming any status ("done", "fixed", "works", "passing"):

1. IDENTIFY: which command or request proves this claim?
2. RUN: execute it fully, fresh
3. READ: the full output — exit code, error count, AND the actual data
4. VERIFY: does the output confirm the claim?
   - NO  → state the actual status with the evidence
   - YES → state the claim WITH the evidence
5. ONLY THEN make the claim
```

## What counts, per layer

The commands live in `PROJECT-PROFILE.md` → "Verification matrix". The shape
of the rule does not change across stacks:

| Claim | Requires | Not sufficient |
|---|---|---|
| "Builds" | build command, exit 0 | lint passing |
| "Tests pass" | test run: N passed, 0 failed, delta vs. baseline | a previous run, "should pass" |
| "Endpoint / screen / command works" | a real request or run → correct data in the output | success status, "the route is wired" |
| "Returns rows / data" | the output contains the expected non-empty data | "the query looks right" |
| "Scoped / permission applied" | proof the restriction acts (two tenants, the filter visible) | a comment saying it "will be" applied |
| "Bug fixed" | rerun the ORIGINAL reproduction → now correct | code changed, assumed fixed |
| "Nothing else broke" | neighbouring scenarios and the regression set rerun clean | "my change was small" |

**A success status is never proof of correctness.** Read the data.

## Red flags — stop

- "should", "probably", "seems to", "looks correct"
- "Done!" before running anything
- a status claimed from the status code without reading the body
- trusting a prior note that says something is done or tested
- a partial check standing in for a full one (lint → "builds")
- any wording implying success without a run in this session

## When infrastructure is missing

If something genuinely cannot be verified (a service down, an environment
agents cannot reach), **say so explicitly** — "not verified because X is
unavailable" — and, for a tester, hand that part to human QA with a manual
test plan. Never imply success to fill the gap.

## When to apply

Always before any success claim (exact words, synonyms or implications),
before a report that moves a ticket forward, before marking a finding
resolved, before moving on to the next task.
