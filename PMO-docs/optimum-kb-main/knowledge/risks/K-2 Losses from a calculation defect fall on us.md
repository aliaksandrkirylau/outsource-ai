---
type: risk
id: K-2
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
register: internal
capabilities:
  - "[[CAP-005 Mud engineering calculations and simulation]]"
sources:
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-10-20 Introductory call - transcript]]"
tags:
  - calculations
  - liability
  - contract
---
# K-2 Losses from a calculation defect fall on us

## Risk

Cause: Innowise is liable for "direct losses caused by its breach, negligence or unlawful conduct", its
aggregate liability "shall not be less than the total Contract price" and the text sets no cap
([[2026-09-07 Final contract - rendering]] 12.1, 12.3); the SOW's "The impact of the Services or the Deliverables on business of the Customer shall not be
within the scope of responsibility of the Contractor" ([[2026-06-15 SOW v10.4 - rendering]] row 37) is
not in the contract ([[COM-017 Liability, indemnity and force majeure]]).
Event: a defect in how a formula is implemented gives a wrong recommendation, and it is followed at a
rig. Effect: a damaged well and a claim for the losses against us. No figure here.

## Why we think so

Mikhail Andrushkevich, 1 October: "Словно говоря, у нас там баг, формула не та. Они рекомендациям
последовали, скважину поломали, убытки на [amount removed]. По текущим контрактам все эти убытки, за них
несем ответственность мы." ([[2026-10-01 Optimum Three Caballeros call - transcript]] 00:16:00). Anton
Oparienko, just before: "Фундаментальная формула не может поменяться, но то, как мы ее написали и
имплементировали, может." (00:15:35). The quality the architecture must hold:
[[CON-003 Correct calculations]]; fixing a defect after the fact depends on
[[QUE-010 Are past results recalculated when a formula or threshold changes]]. The legal reading is for
a PM.

Added 2026-10-30 (evaluated): the client expects us to catch its formula mistakes. Mr. Lawal, 20
October: "there needs to be a level of double-checking from your side in case if something is wrong or
there's a mistake", or "it will become, oh, but that is what you said"; Arseniy: "That's the only right
approach" ([[2026-10-20 Introductory call - transcript]] 00:12:59, 00:14:21). The SOW puts validating the
formulas on the client; both texts are in [[COM-008 Client cooperation and dependencies]]. This supports
the reading that the losses fall on us.

## Response and next action

Not set. A PM scores it and names the owner and the response.

## History

- 2026-10-02 written as a draft from the 1 October call; not scored.
- 2026-10-30 updated: the client expects us to double-check the formulas (the call of 20 October); not scored.
