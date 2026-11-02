---
name: systematic-debugging
description: Use when encountering any bug, wrong data, empty result, or unexpected behaviour, before proposing fixes. Especially for silent failures — a success response with wrong or empty data.
---

# Systematic Debugging

**Core principle:** always find the root cause before attempting a fix.
Symptom fixes are failures.

Multi-component systems hide their worst bugs at boundaries, and the most
dangerous are *silent*: a success response with empty or wrong data instead of
an error. Reading code is not enough to catch these — reproduce against the
running system and inspect the actual data.

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

## Check the project's known traps first

`PROJECT-PROFILE.md` → "Known traps" lists the root causes that already bit
this project (misspelled names that fail silently, missing tenancy fields,
derived values that must not be recomputed by hand, which layer adds which
envelope). Rule them out before deep investigation.

## Phase 1 — Root cause investigation

1. **Read the actual response and errors completely.** Not the code — the real
   output, the full stack trace, the exact line and name.
2. **Reproduce consistently** against the running system, with the test data
   named in the profile. Capture the exact input and the exact output. Not
   reproducible → gather more data, do not guess.
3. **Check the data layer directly** when the result is empty or wrong: does
   the thing the code names exist? does the field it filters on exist? count
   with and without the filter to localize the drop.
4. **Gather evidence at each boundary** (client → service → service → store):
   what goes in and what comes out at each hop. Find WHERE it goes wrong, then
   investigate only that layer.
5. **Trace the bad value to its source** — every place it comes from, not just
   the first one you find.

## Phase 2 — Pattern analysis

Find a working example of the same kind in the codebase, read it end to end,
and list every difference, however small.

## Phase 3 — Hypothesis and testing

One hypothesis, stated: "X is the root cause because Y". Test it with the
smallest possible change, preferably outside the code (a direct query, a single
request). Worked → Phase 4. Did not → a new hypothesis; never stack fixes.
When you do not know, say so.

## Phase 4 — Implementation

1. **A rerunnable reproduction first** — a failing test, or the exact request
   and its current wrong output.
2. **One fix, at the root cause.** No bundled improvements — those are
   findings to log. No fix that makes an empty result *look* populated:
   fabricated fallbacks are a worse bug.
3. **Verify** with `verification-before-completion`: rerun the reproduction,
   then the neighbouring scenarios.
4. **Fix did not work?** Fewer than 3 attempts → back to Phase 1 with what you
   learned. **3 or more → stop and question the architecture**; raise it
   instead of trying fix number four. If it is outside the ticket's scope, it
   is a finding, not an inline fix.

## Red flags — return to Phase 1

- "Quick fix now, investigate later"
- "Just change the name and see" — confirm in the data first
- several changes, one run
- "it returns success, so it works"
- proposing fixes before reproducing
- "one more attempt" after two failures

## Scope note

Root-cause work surfaces adjacent issues. Investigate fully, fix only the
in-scope root cause, log the rest to `FINDINGS.md` (see `/work-ticket` Steps
4–5).
