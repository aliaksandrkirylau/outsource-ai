# SPEC-DISCREPANCIES — defects in the client's specification

Discrepancies in the **client's documents**, not in our code (code defects go
to `FINDINGS.md`). The audience is different: these entries go to the client
through the PM, not to internal triage.

**The rule this file encodes: conformance to the specification is in scope;
correctness of the specification is not.** A rule or formula is implemented
exactly as the client wrote it, even when the data says it is wrong. Silently
"fixing" it produces a number that disagrees with the client's own documents,
and nobody can tell why. Implement as specified, record here, the client
decides.

Classes:

- **SUSPECT** — implementable literally, but the data or another client
  document contradicts it. Implement literally, record, do not deviate.
- **FORCED DEVIATION** — cannot be implemented as written (a named field,
  entity or source does not exist). A substitution is unavoidable: record what
  was substituted and why, and say so in the ticket report.
- **ACCEPTED DEVIATION** — a known, owner-approved gap between what ships and
  what the spec asks, with an end date.

Append-only. On an existing entry only `Raised`, `Answer received` and
`Verified` may be edited; an answered entry stays, with its answer. Grep
before adding — a duplicate hides which entry is authoritative.

## Summary

| Class | What is wrong | Affects | Ticket | Raised |
|---|---|---|---|---|

---

# Register

<!--
## [SUSPECT | FORCED DEVIATION | ACCEPTED DEVIATION] <short title>
- Spec says: <verbatim, with source and version>
- Data / code says: <what is actually there, with numbers and how measured>
- What we implemented: <literal | substitution: X instead of Y>
- Ticket: <KEY>
- Raised: <date, to whom | to raise>
- Answer received: <date, answer | —>
- Verified: <YYYY-MM-DD — method, numbers>
-->
