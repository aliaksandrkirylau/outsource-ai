# Planning rules + P&L-write mechanics (reusable)

Grounded in real project runs (Alchemy roadmap; LotberG / IB Tutor / Alchemy P&L writes). These are house patterns, not the control contract - the standard defines what A07/A08 must produce and verify. Confirm against the PM if a project deviates.

## Roadmap / resource planning rules

- Capacity: 1 FTE is ~168-176 usable hours per full month. No single role exceeds one person's realistic month unless the PM adds a head.
- Basis: the WBS MAX hours is the safe envelope for a T&M cap - the ceiling, not the expectation. Real burn should land under it. min / mid / max / risk-blend is the PM's fork (Stage 0).
- Ramp: a partial start month gets partial hours (e.g. devs starting mid-month). Don't book a full month on a part-month start.
- Front/back-load per role: tech / AI lead front-loaded (KT + architecture early, taper as hands-on dev takes over); QA at the tail (stabilization / UAT); DM a light oversight line (~4h/week), additive on top of the WBS build envelope if it is billed (a commercial call, flag it).
- Cap discipline: when hours run out against the cap, pull UAT / acceptance EARLIER rather than exceed the cap - land the project inside the window rather than trailing into an extra month.
- Hold the WBS total constant when shifting hours between months: extra early hours come out of the tail, they are not new hours.
- Dependency order: environment + access + architecture/integration first -> data access + mapping -> core engine + AI layer -> explainability / audit / dashboard -> test / UAT / acceptance. Put the long pole (often the AI/LLM layer) on the critical path explicitly.
- Single-source shared numbers: a value that lives in several artifacts (e.g. the PM's monthly split across P&L / roadmap / resource plan) WILL drift. Keep one source and flag divergence; never silently propagate one version.

## P&L structure, write mechanics and fair-hours

Moved to `${CLAUDE_PLUGIN_ROOT}/references/pl-structure.md`, because the takeover skill and the staffing work need the same knowledge. It covers the file and tab layout, month codes, the 11-row role block offsets, the overhead model, the full write sequence with its control-total check, and the fair-hours redistribution rules.

Read it before touching any economy sheet. The short version: money stays in the Sensitive folder, work on a copy, confirm month columns from a live header read, leave salary blank, verify control totals after every write, cards before writes.
