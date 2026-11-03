---
type: requirement
id: REQ-009
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-10-29 Client sample daily report - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2026-11-02 Client sample daily mud reports - rendering]]"
  - "[[2026-11-02 Client sample end-of-well recap - rendering]]"
scope_status: contracted
baseline:
  - "WBS:Development Flutter!38-41"
  - "WBS:Development Flutter!61-66"
capabilities:
  - "[[CAP-006 Inventory]]"
tags:
  - inventory
---
# REQ-009 Inventory tracking

## Need

The engineer records what materials and chemicals the rig has, receives and uses; HQ sees stock and
consumption across rigs and is warned about low stock and expiry. The client's expectation: "Tracks
initial loadout, inflow, daily consumption, cumulative consumption per section and well, daily
balance, product details (brand name, generic description, density, material #), products use
concentration (in pounds/barrel & %) in the drilling fluid, expiration dates, product unit size, unit
cost and total cost" ([[2025-10-29 Client answers to the Q&A register - rendering]] E.24).

Scope: contracted. v1 WBS ([[2026-09-25 v1 WBS - rendering]]) Development Flutter rows 61-66 (desktop inventory: daily consumption, stock
movements, concentration, low-stock and expiry alerts) and 38-41 (web inventory: products, stock
movements, cost linkage), all estimated.

From the first call's transcript (added 2026-09-28, batch 2): "the inventory control and management
will be for the drilling fluid itself, for the long list of chemicals and materials that they use in
conditioning and treating and maintaining the properties of the drilling fluid"
([[2025-10-22 First call with OES - transcript]] 0:12:27); a report of what the rig had "at the
beginning of the job against what you presently have and what you have used ... with a click of a
button" (0:37:48). The third part the client named, "The inventory of their own tools and reagents and
equipment that they use in the lab", is not in the v1 WBS lines and is split out as
[[REQ-016 Inventory of lab equipment and reagents]].

## Acceptance criteria

To be written by the BA.

## Edge cases

| Scenario | Expected behaviour |
|---|---|
| Stock is recorded offline on the rig and changed at HQ | Not defined in these sources |

## Business rules

- Stock events: "Initial Loadout, Inflow (Received), Returned, and Lost"
  ([[2025-10-28 BA draft WBS - rendering]] row 31); the client's sample has the same columns plus
  daily use, final quantity and ending concentration
  ([[2025-10-29 Client sample daily report - rendering]] row 95).
- Alerts: "Alerts to identify critical materials below minimum stock level" (E.20, type 3); "QHSE
  alerts: alerts on upcoming expirations of products, reagents, stock- outs, or equipment calibration"
  (F.27).
- Cost: consumption is linked "to a unit price from the provided Price List for internal (e.g., Daily
  Report) cost calculation" (BA draft row 33); the client's sample has a products price list and daily
  and cumulative cost fields (sample, "Products Price", rows 62 and 86-92). No figures are held in the
  KB.
- Low-stock levels are set at HQ (BA draft row 35; the SOW v10.4([[2026-06-15 SOW v10.4 - rendering]]) says in the web
  admin panel, not on the desktop).
- The first call: "account for the quantity or volume of drilling fluid that has been utilized for
  that day and what is remaining, chemicals, materials, etc." ([[2025-10-22 First call with OES - notes]]
  key point 5).
- Stock as the client keeps it in its samples (added 2026-11-02;
  [[2026-11-02 Client sample daily mud reports - rendering]]): "Start, Transferred In, Received,
  Returned, Lost, Daily Use, Final" with the ending concentration in the active and reserve system
  ([[2026-11-02 Client sample daily mud reports - DMR Sample 1.pdf#page=4|DMR Sample 1 p4]]); "Initial, Received, Used, Interval, Cumulative, Final, Expire Date" with the
  concentration at start and end in ppb ([[2026-11-02 Client sample daily mud reports - DMR Sample 2.pdf#page=2|DMR Sample 2 p2]]).
- Whole mud moves as stock too: "OBM Transferred In / Out (LMP/Other Well/Other Section)" with
  volumes, and volume in "From LMP / Other rigs"
  ([[2026-11-02 Client sample end-of-well recap - rendering]] pp [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=25|25]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=28|28]]) - mud from the liquid mud
  plant and from other wells and sections.
- Costs are in every sample, per day, section and well, with an engineering service cost besides the
  products; the end-of-well report sets "Planned Units" and "Planned Cost" against actual, with "Not
  Planned Costs" and a cost analysis (the recap, pp [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=6|6]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=10|10]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=15|15]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=20|20]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=25|25]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=30|30]]). The figures stay in the
  renderings (AGENTS.md rule 7). Their arithmetic holds as printed: unit price by units is the line
  cost, lines sum to the section cost and sections to the well (the recap), daily costs sum to the
  daily product cost and final stock by price to the inventory value ([[2026-11-02 Client sample daily mud reports - DMR Sample 1.pdf#page=4|DMR Sample 1 p4]]). The cost per
  bbl does not: its divisor changes between pages - volume used, volume in (the recap, [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=23|p23]]), initial
  plus make-up volume (pp [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=3|3]], [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=15|15]]) - and [[2026-11-02 Client sample end-of-well recap - EOWR Sample.pdf#page=3|p3]]'s "Fluids Cost / bbl of fluid" row holds the per-ft
  values.
- Evaluated: v1 WBS row 41 links consumption to a price list ("Material Cost Linkage"); planned
  against actual cost, the engineering cost and which volume a cost per bbl uses are not in its
  wording. For the BA.

## Out of scope
