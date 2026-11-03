# S04 Inventory

Session plan, topic 4, week 3. One hour. Part of [[00 discovery-BA-plan]]. Working material, not evidence.

## Elicitation goal

What the rig records about products, what HQ manages, and where stock levels and expiry live.

## Scope

- D4 desktop inventory: WBS:Development Flutter!62 to !66
- W4 web inventory: WBS:Development Flutter!39 to !41
- [[REQ-009 Inventory tracking]], [[CAP-006 Inventory]]

## Participants

Client: a mud engineer, someone who handles products at HQ, Mr. Lawal. Ours: Anton, Leu.

## Preparation and inputs

- **The product catalogue** (brand, generic name, material number, unit size, unit, density) and one
  real day's products table. The price list's structure only; figures stay in Drive.
- Prototype: the rig's products table as in their daily report (Start, Received, Returned, Lost, Daily
  Use, Final, concentration); the HQ catalogue and per-rig stock; basic validation and the consumption
  view on the web (promised in the SOW, no WBS line). No costs on the rig screens.

## Agenda

| Min | Item | Fails without |
|---|---|---|
| 0-5 | Recap, goal | - |
| 5-25 | Products at the rig: what is recorded, in what units | A1, A2, A3 |
| 25-40 | HQ: catalogue, receiving, stock per rig | B1, B2, B3 |
| 40-48 | Low stock and expiry | C1 |
| 48-55 | Click through both apps | Corrections noted |
| 55-60 | Next steps | - |

## Questions register

Grouped by topic in agenda order; must-haves first. Blocks: the WBS line the answer is needed for, as its row in the WBS tab "Development Flutter" and a short name. When: Call, or Written after the session.

| ID | Question | Blocks | Must | When | Ahead | Source |
|---|---|---|---|---|---|---|
| | **A. At the rig** | | | | | |
| A1 | Is stock kept per rig or per well? Does it carry over to the next well? | 62 Daily consumption (desktop); 63 Stock movements (desktop) | Yes | Call | Yes | Sheet D4 B2; [[REQ-009 Inventory tracking\|REQ-009]] |
| A2 | Is use recorded in sacks and drums, or by weight? | 62 Daily consumption (desktop) | Yes | Call | Yes | Sheet D4 B3 |
| A3 | Should the app track mud volumes (pits, active and reserve, losses)? (No WBS line names it.) | - | Yes | Call | - | Sheet D4 B6 |
| A4 | Is concentration entered, or calculated from use and volume? | - | - | Call | - | Sheet D4 B4 |
| | **B. Catalogue and receiving at HQ** | | | | | |
| B1 | Who owns the product catalogue? Can an engineer add a product at the rig? | 39 Product catalogue (web) | Yes | Call | Yes | Sheet D4 B1 |
| B2 | One company catalogue, or lists and prices per customer? Who provides the price list, and how often does it change? | 39 Product catalogue (web); 41 Material cost linkage (web) | Yes | Call | - | Sheet W4 B1 |
| B3 | Who records products received, the HQ warehouse or the rig? | 40 Stock movements (web); 63 Stock movements (desktop) | Yes | Call | Yes | Sheet W4 B2 |
| B4 | How is the first catalogue loaded? (Import is out of scope.) Is warehouse stock needed? | - | - | Written | - | Sheet W4 L |
| B5 | Does an ERP hold the catalogue and prices? | - | - | Written | - | Sheet X5 |
| | **C. Low stock and expiry** | | | | | |
| C1 | Where are low-stock levels and expiry dates set? Is expiry recorded per lot on receipt? | 65 Low stock alerts (desktop); 66 Expiry alerts (desktop) | Yes | Call | Yes | Sheet D4 B5, W4 B3 |
| | **D. Costs and out of scope** | | | | | |
| D1 | Who may see costs? Should the engineer? | - | - | Written | - | Sheet D4 L, W4 L |
| D2 | Lab equipment, reagents and calibration: needed, or out of scope? | - | - | Written | - | Sheet D4 L; [[REQ-016 Inventory of lab equipment and reagents\|REQ-016]] |

Materials to request: the catalogue export, a typical loadout, one real day's products table, low-stock and expiry rules, how products are dispatched to rigs today (Sheet D4, W4).

## Confirm with the client

| Ours | Plain wording |
|---|---|
| [[REQ-009 Inventory tracking]] | The rig records products received, used, returned and lost each day; HQ keeps the catalogue and sees stock per rig. |

## Outputs

- KB: [[REQ-009 Inventory tracking]] updated; where low-stock and expiry are set settled or a Question.
- The catalogue and the low-stock answer asked in writing.
