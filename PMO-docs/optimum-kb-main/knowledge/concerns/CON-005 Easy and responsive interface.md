---
type: concern
id: CON-005
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: quality
sources:
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-23 OES company research - rendering]]"
  - "[[2026-10-20 Introductory call - transcript]]"
capabilities:
  - "[[CAP-011 Platform, environments and handover]]"
tags:
  - usability
  - performance
---
# CON-005 Easy and responsive interface

## What must hold

The client's third outcome for the first release: "User friendly interface with low latency and
minimal bugs." ([[2025-10-29 Client answers to the Q&A register - rendering]] A.1) No measure yet:
the client gave none, and "low latency" has no number. The discovery phase would have to set one.

## Why

- The first request asked for "an intuitive user interface"
  ([[2025-10-23 OES company research - rendering]], Initial Request).
- The product is expected to be "better designed, intuitive and detailed" than the client's current
  Excel report (F.29).
- The client wants guided help for new users "very much" (E.26), and the in-app wizard is out of scope
  ([[REQ-014 Onboarding wizard for new users]]), so the interface itself carries more of that weight.

The client's design vision (added 2026-10-30; [[2026-10-20 Introductory call - transcript]]). Mr. Lawal:
"My vision for this project is to have a customized in-house-built reporting software for our
operation, you know, and also an engineering tool for our field personnel"; "whatever we're doing
needs to be very fresh, need to be very, very modern. I don't want to build something that is
mimicking what Schlumberger has done 15 years ago"; "it has to be a solution that is easy for the
engineer on the field, that makes his job a lot easier, a lot more professional, and that
differentiates us from our competitors"; "How that is going to exactly play out in your design and the
base of your design, I'm going to leave all that to you"; "I want to be free from the constraints of
the old ways and to the constraints of the incumbent solutions" (00:40:42). They used "Mod4" before,
most likely MUDPRO ([[2026-10-21 MUDPRO research]], `ba/`), and "whatever we're going to do should be
able to better any of those. I don't want, I don't want a copy of what someone has done 20, 15, 10
years ago" (00:40:42). No brand book: "in terms of a standard company brand book, no"; the logos they
will provide (00:39:44). Anton: "It should not probably be something like flashy in the face of the mud
engineers working on the field, but still looking good, like fresh and very clear on how to use it."
(00:44:36) Still no measure. How the UI kit is chosen:
[[DEC-017 Choose the UI kit with the client from three variants]].

## Affected requirements

- [[REQ-005 Parameter thresholds and entry alerts]]
- [[REQ-010 Reports]]
- [[REQ-011 Dashboards and KPIs]]

## Treatment

Not decided.
