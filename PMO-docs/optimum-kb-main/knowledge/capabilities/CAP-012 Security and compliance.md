---
type: capability
id: CAP-012
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: enabler
baseline:
  - "[[COM-015 Saudi cybersecurity and regulatory compliance]]"
  - "[[COM-014 Confidentiality and personal data]]"
sources:
  - "[[2026-07-14 Cybersecurity framework - rendering]]"
  - "[[2026-07-14 NCNICC-1 translation - overview]]"
tags:
  - capability
  - compliance
  - security
---
# CAP-012 Security and compliance

## What it must do

The system, and the way it is built, meet the Saudi controls that apply to it
([[CON-007 Saudi cybersecurity and data protection rules]]), and data about the client's own
customers is stored and shared only as the client allows
([[CON-006 Confidentiality of the client's customers' data]]). It constrains every other capability.

Its baseline is unsettled: [[COM-015 Saudi cybersecurity and regulatory compliance]] is disputed,
because the contract and the SOW v10.4 place the burden differently.

## Coverage criteria

Drafted from the Concerns and Commitments; the TL owns these.

- C1 Which controls apply is settled, including the client's NCA category
  ([[QUE-005 Is the client an NCA Category A or B entity]]).
- C2 A compliance gap analysis against those controls is done in Discovery
  ([[2026-07-14 NCNICC-1 translation - overview]]).
- C3 The secure-development controls that apply are in the pipeline and checked before go-live
  ([[CON-007 Saudi cybersecurity and data protection rules]] lists them per framework).
- C4 Data about the client's customers is stored and shared only as the client allows (CON-006).
- C5 Where our team members may work from is settled
  ([[QUE-009 Where may our team members be located]]).

## Refined by

- [[CON-006 Confidentiality of the client's customers' data]]
- [[CON-007 Saudi cybersecurity and data protection rules]]
- [[COM-014 Confidentiality and personal data]]
- [[COM-015 Saudi cybersecurity and regulatory compliance]] (disputed)
- [[QUE-005 Is the client an NCA Category A or B entity]]
- [[QUE-009 Where may our team members be located]]

## Plan

M1 (which controls apply, the gap analysis), then through every milestone, checked before handover
in M6.
