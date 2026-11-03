# Output shapes - A02 and A04 (skeletons only)

These are structural skeletons so the two outputs come out consistent. They are NOT the control contract - the authoritative Inputs / Outputs / Verification Criteria / Control Metrics live in the standard (A02 = Confluence 4619206702, A04 = 4619206765) or `${CLAUDE_PLUGIN_ROOT}/references/standard-a-contract.md`. Read those for what "done" means; use these for the layout.

## A02 - Stakeholder register + internal communication

```
# <Project> - Stakeholder Register + internal communication (A02)

## Client-side stakeholders
| Person | Role | Area / ownership | Status (+ EMAIL MISSING flag) |

## Internal stakeholders (Innowise)
| Person | Role | Ownership | Status |

## Decision ownership map
| Decision area | Client-side owner | Internal owner | Client status | Internal status |
(scope/CR, acceptance, budget/cap, commercial rule values, technical direction,
 technical-delivery supervision)
(status = confirmed / gap / N-A. This table IS the denominator for both A02 indices,
 so every relevant area gets a row and every row gets a status. An explicit N-A counts
 as ready for the internal index, not as a gap.)

## Internal communication channels
| Channel | Purpose | ID / link | PM added |
(note the chat lifecycle: pre-sale -> common on signing; strategy/others on Closed Won;
 internal is PM-created)

## Actor / ownership / comms gaps (A02 actions)
1. ... (each gap with an owner: Sales / Account / client-side)

## A02 control metrics
- Client Decision Clarity Index: X of N = XX% (target 70-80% before kick-off)
- Internal Ownership Readiness Index: Y of N = YY% (target 100% before client kick-off)
(both counted off the decision-ownership table above - name the rows, do not assert a
 percentage. Decision support for the PM, not a grade.)
```

## A04 - Project description + context

The numbered sections ARE the eight areas the Project Definition Maturity Index counts, in
the standard's own order. Keep the numbering and keep an empty section rather than deleting
it - "5. Success criteria - not yet defined, owner Jake" is a countable gap, a missing
heading is invisible. This is how the index becomes readable off the document.

```
# <Project> - Project description (A04)

## 1. Client problem / pain
(reuse the A01 client problem statement VERBATIM - pain and outcome, not the deliverable)

## 2. Project goals and expected outcomes

## 3. High-level scope context

## 4. Success criteria
- MVP observable success criteria (what we can demonstrate, and how)
- Business north-star targets (client's aspiration) - marked DIRECTIONAL / NON-COMMITTAL,
  matching the SOW. Never let these read as delivery commitments or acceptance gates.

## 5. Key assumptions

## 6. Key constraints

## 7. Business / strategic value (where applicable)
(money / marketing / domain-or-technical growth; if economics weak, value must be
 marketing or technical AND someone owns realizing it - feeds A08/A09)

## A04 control metrics
- Project Definition Maturity Index: k of 8 = XX% (target >= 80%)
  (only 0/12.5/25/37.5/50/62.5/75/87.5/100 are possible against a fixed 8 - or /7 if
   value is genuinely N-A. A number like 90% means it was estimated, not counted.)
- Observable Success Criteria Ratio: j of m = YY% (target >= 70% before kick-off)
  (list which criteria counted as observable and which did not)

## Feeds forward
- to A05 (validation), A09 (baseline package). Note any A03 contract findings this
  description is built on, or state that it is built on the proposal because the
  contract was not yet reviewed.
```
