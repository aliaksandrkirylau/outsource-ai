# Reports

**Purpose**: Output folder for structured validation reports generated during spec review.

---

## What Goes Here

Validation reports produced by the `gap-analysis` skill or manual validation sweeps. These are snapshot documents -- they capture the state of a spec at a point in time, with issues flagged and resolved.

**Typical files:**
- `Validation_Report_Epic-01_[date].md` -- gap analysis output for a specific Epic
- `Validation_Report_FullSpec_[date].md` -- full-spec consistency check before dev handoff
- `Validation_Report_PlatformSpec_[date].md` -- Platform Specification review

---

## When to Generate a Report

- After drafting or significantly updating an Epic -- run `gap-analysis`, save the output here
- Before presenting specs to the client -- full sweep to confirm no P0 gaps
- Before development handoff -- final validation that all Open Questions are resolved and no contradictions exist

---

## How to Save a Report

After running `gap-analysis` or a manual validation sweep, ask Claude:
> "Save this validation report to 00_Meta/Reports/ with today's date in the filename."

---

## Note

Reports are reference documents, not active spec files. They're useful for tracking what was flagged and resolved over the life of the project. They don't need to stay current -- each report is a snapshot.
