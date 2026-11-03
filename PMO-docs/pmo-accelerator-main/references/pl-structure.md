---
source: Innowise PMO project economy files (Economics [Staff] / Economics [Actual] tabs), plus real write runs on Alchemy, LotberG, IB Tutor, WindoTrader
written: 2026-07-28   # house knowledge from real P&L runs - NOT synced from Confluence
sensitivity: HIGH - everything in this file concerns money
---
# Project P&L - how our economy files are structured, and how to write to one safely

Purpose: so the copilot can read a P&L, explain it to a PM, build a plan against it, and help the PM write planned hours into it after A07/A08 without inventing a phantom month or leaking money into the wrong place.

## The three rules that come before anything else

1. Money never leaves the Sensitive folder. Not into the common project folder, not into the NotebookLM project brain, not into a shared Sheet, not as a link. Worked and paid HOURS are fine anywhere; currency amounts, rates, salaries, margins and profit are not. Contract documents get the same treatment.
2. The PM owns the write. The copilot reads, computes, proposes and can execute a write the PM has explicitly approved - it never writes first and asks after. Show the numbers, let the PM look at them, then write.
3. Work on a copy first. Duplicate the tab with a dated name before touching a live P&L. Promoting the copy to the live tab is a separate, explicit PM decision.

If the project has no P&L yet, the action is to REQUEST one from PMO RM, not to build one. There is deliberately no self-serve template (see A08 in the template register).

## File shape

A project economy file typically carries these tabs:

- `Economics [Staff]` - the PLAN. Roles and their planned hours and rates. This is what A07/A08 fills.
- `Economics [Actual]` - what actually happened. Fed from timesheets and invoices.
- An overhead tab (often labelled with a Cyrillic "nakl" style name) - the operational cost model. Read this before doing any net or margin maths.
- Sometimes a redistribution tab for fair-hours splits.

Months are columns, identified by a month CODE in a header row: `726` = July 2026, `826` = August 2026, `926` = September, `1026` = October, `126` = January. Read the code, not the position.

## The role block

Each role or person occupies an 11-row block. Offsets from the block start are stable across every file we have seen. Use the fixed offset, do not scan for a label - scanning adds Unicode surface area and obscures the data shape.

| Offset | Row |
|---|---|
| +2 | Rate |
| +3 | Paid hours |
| +4 | Worked hours |
| +6 | Level / grade |
| +7 | Tax residency |
| +8 | Salary (ZP + bonuses + vacation) |

If you want a safety net against template drift, read one anchor cell at the expected row at parse start and warn if it is blank. Do not rebuild a dynamic label search.

## Overhead

Never assume the coefficients. Read them from the sheet's own formula before computing anything net:

- OpRate - operational cost per worked hour.
- Busdev rate - a percentage of revenue.
- Per-desk exemptions - some desk types (for example Pre-prod) are exempt; some tax residencies have the Busdev and tax term folded into gross rather than charged separately.

That last point matters: because overhead is partly revenue-linked and charged differently by tax residency, a redistribution of billable hours across residencies shifts total overhead. So a "zero-sum" move is only approximately zero-sum. Flag the delta and attribute it; do not claim exact zero-sum.

## Writing planned hours after A07/A08

This is the sequence. Every one of these steps exists because skipping it caused a real bug.

**1. Confirm the columns from a live header read.** Read the month header row and the anchor metric row (Paid hours) and match each active month code to its actual column LETTER. Do NOT infer the column from a values-array index - `get_sheet_data` returns columns A, B and C as the first array elements, so index does not equal column. Getting this wrong writes one column to the left, fills an empty month and overwrites a real one. On LotberG this invented a phantom month and jumped revenue from 61,671 to 89,016 before it was caught.

**2. Read raw values, not displayed ones.** Use `include_grid_data` and read `effectiveValue`. A rate displayed as 49.1 may store 49.14, and building on the displayed value drifts every downstream number. Read one cell at a time for the cells that matter; a bulk grid read across many rows blows the token limit.

**3. Write BOTH hour rows and the role labels. Nothing else.** Paid (billable) is offset +3, Worked is +4 - fill both. Conventions at plan stage:
- **Paid = Worked by default**, for every role.
- Depart from that only where something explicitly says otherwise. The usual case is a role that is not billable - a DM carried as oversight but absorbed rather than billed gets worked hours and ZERO paid. Ask if it has not been settled; do not guess, because a wrongly billable oversight line changes the invoice total.
- **Total billable hours must equal what the plan and the contract say was sold.** That is the control check that catches a non-billable role written as billable, a month written to the wrong column, or a role missed entirely.
- Total worked may legitimately EXCEED total billable where a role is absorbed. That gap is expected; name it, because it is the visible cost of carrying oversight unbilled.
- **Rates, currency conversion, salary, tax residency and grade are NOT the copilot's to fill.** Do not derive a rate, do not convert between currencies, do not carry a conversion factor in an instruction (any rate baked into a document is wrong by the time someone reads it), and do not look one up. These are finance-owned.
- If the PM explicitly asks for a rate to be written, the PM supplies the figure and the currency. Echo it back, write exactly that, and say plainly that you are not validating it because you have nothing to validate it against. The standard requires rate, salary, location and exchange-rate data to be provided or confirmed by the responsible owner before any result is treated as reliable.
- A positive profit with a blank salary column is EXPECTED at plan stage. Explain that to the PM rather than presenting it as a result.
- Do not report a margin or a profitability figure at all at planning stage. The economy is worked by the PM with the PMO RM; the copilot places hours and checks that they tied.

**4. Verify control totals immediately after.** Re-read and compare: total BILLABLE hours against the plan and the contract (the one that matters), total worked, each role's own total, and the invoice pool. A total that is not roughly equal after a supposedly neutral write is a targeting bug, not rounding. Attribute the difference before moving on. On a zero-sum move, any drift should be explainable by rounding or by a known structural exemption - if it is not, something was written to the wrong cell.

**5. Report what you wrote.** Cells touched, totals before and after, and the delta. If anything is off, say so first.

## Fair-hours redistribution (the optimisation layer)

**Not for initial planning.** At A07/A08 paid equals worked by definition and a new project has no actuals, so there is nothing to redistribute. This applies at A10 with a confirmed team, or later against real worked hours. Do not reach for it while building a plan.

It is a zero-sum redistribution of BILLABLE hours - billable is the fairness lever, not a physical record.

Constraints that hold:
- The pool stays constant per month: each month's billable sum equals that month's invoice or sold total.
- Presence: a desk can only be billable in months it was actually present (worked hours greater than zero).
- Billable hours are whole numbers by default. A 0.1h option exists and cuts mixed-rate invoice drift substantially - it is a per-run choice.
- Billable is NOT capped by worked. A desk can be credited more billable than it worked; that is the point of the lever. The only hard constraints are the pool, presence, and billable at or above zero.
- A floor is a minimum, not a pin. If a floored role is the only desk present in a month, it absorbs that whole month rather than being capped at its period share.
- A line with zero worked hours AND zero billed is held out (a carried cost like a tool or licence line). A line that WORKED but was zero-paid is a PARTICIPANT - it gets credited other desks' billed hours, and its written rate emerges as the blended rate of what it receives.

Cards first, write last. Render the proposal as cards the PM can look at and nudge. The PM approves, then the split is written. Never write first.

Before writing a redistribution, cross-check the written invoice total against the true invoice total. A shortfall means hours went unplaced, not that rounding happened.

## What the copilot should refuse

- Putting any currency figure, margin, salary or rate into the project brain, a shared Sheet, a client-facing document or a chat outside the Economy chat.
- Filling salary or tax residency.
- Writing to a live P&L tab without an explicit approval on the specific numbers, in this conversation.
- Reporting a margin or profitability percentage outside an approved channel.
- Claiming a write tied out without actually re-reading the totals.
