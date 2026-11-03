# 02 Discovery change requests

Every client ask in Discovery that may go beyond the agreed scope, until it is a signed change request or a decision not to raise one. Part of [[00 discovery-BA-plan]]. Working material, not evidence.
The contract's rules: [[COM-005 Change requests]]; the small-change threshold is open
([[DEC-003 Handling small change requests]]).

## Change assessment

1. **Logged** (Leu): heard in a session or by e-mail, added the same day.
2. **Raised** (Leu): sent to Anton and Mikhail with the WBS line and our minimal version.
3. **Decided** (Anton, Mikhail), one of:
   - *Absorbed*: inside the scope or below the threshold; goes into the area's backlog.
   - *Not a CR*: clarification, refinement or "implicit in the SOW" (contract 4.4); reason recorded.
   - *Revisit*: kept for the scope revisit after Discovery.
   - *CR candidate*: the Requirement gets `scope_status: proposed-change`.
1. **Requested** (client): our impact assessment is due within five business days (4.2).
2. **Assessed** (Anton sends; Leu writes scope, dependencies, risks).
3. **Approved or rejected**: effective only when the client signs it (4.3).

## Change register

| ID | Date | From | What the client asked, in their words | WBS line | Our minimal version | Status | Assessment due | Decision, who, date | Note |
|---|---|---|---|---|---|---|---|---|---|
| CR-01 | before Discovery | Q&A E.23 | "Document upload required from HQ but accessible on the job site." | none | Not drawn | CR candidate | - | - | [[REQ-012 Documents uploaded at HQ available at the rig]] |
| CR-02 | before Discovery | Q&A | Inventory of lab equipment and reagents | none | Not drawn | CR candidate | - | - | [[REQ-016 Inventory of lab equipment and reagents]] |
| CR-03 | before Discovery | Q&A Part 1, 3 | An engineering calculation/simulation report | none | Not drawn | CR candidate | - | - | [[REQ-017 Report on a single calculation or simulation]] |
| CR-04 | | | | | | | | | |

Gaps found before Discovery that may come up as asks: [[2026-10-01 SOW v10.4 to v1 WBS scope mapping]].

## Impact assessment template

One per entry that reaches "Requested", copied below the register.

```
### CR-nn <short title>

- Requested by, date received, assessment due:
- What is asked (client's words, link to the e-mail or minutes):
- Why it is outside the agreed SOW (not a 4.4 item):
- Scope impact: areas, WBS lines, prototypes, Requirements affected:
- Time impact: milestone affected, delay if any:
- Price impact: yes / no (figures stay with the PMs, never here)
- Dependencies:
- Risks:
- Options: absorb / defer to the scope revisit / change request
- Recommendation:
- Client decision: approved / rejected, signed by, date (contract 4.3):
```
