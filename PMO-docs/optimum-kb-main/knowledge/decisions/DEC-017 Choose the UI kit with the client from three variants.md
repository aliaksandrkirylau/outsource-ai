---
type: decision
id: DEC-017
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: delivery
deciders:
  - tbd
sources:
  - "[[2026-10-28 Optimum sync - transcript]]"
  - "[[2026-10-20 Introductory call - transcript]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
valid_from: 2026-10-28
capabilities:
  - "[[CAP-011 Platform, environments and handover]]"
tags:
  - design
  - discovery
---
# DEC-017 Choose the UI kit with the client from three variants

## Context

The UI kit is a Milestone 1 deliverable, and the screens of the later milestones are built on the
approved UI kit ([[COM-020 Milestone plan and deliverables]]; [[2026-06-15 SOW v10.4 - rendering]]).
The client has no brand book - "in terms of a standard company brand book, no" - will provide logos,
and leaves the design to us: "How that is going to exactly play out in your design and the base of your
design, I'm going to leave all that to you", as long as it is "very fresh, need to be very, very modern"
([[2026-10-20 Introductory call - transcript]] 00:39:44, 00:40:42;
[[CON-005 Easy and responsive interface]]). A designer joins only on demand
([[DEC-014 Staff on demand, seniors who work with Claude, fewer developers]]).

## Options considered

1. One kit, Mikhail's, generated from the client's site: "Один у меня есть сгенеренный по их сайту"
   ([[2026-10-28 Optimum sync - transcript]] 00:00:00). Not taken alone: it becomes one of the three.
2. About three kits that differ, shown at the first working session, the client choosing one. Chosen.

## Decision

"Обсудили, что к первой рабочей сессии было бы неплохо UI-китов накидать клиенту, там штуки три
показать разных и попросить определиться. Один у меня есть сгенеренный по их сайту, еще парочку,
которые отличаются там совсем в одном направлении, сделает лев." (Mikhail, 00:00:00; "лев" is Leu.)
Arseniy checks Mikhail's kit with the developers and asks which libraries they want, "чтобы
стандартизировать контроллы", and passes it to Leu, "чтобы Лев генерил уже новые киты с учетом этого"
(00:00:00).

Said as discussed, "Обсудили", without naming who decided; deciders tbd (Anton Oparienko, ingest
session 2026-10-30).

## Rationale

Not stated on the call. Our reading (evaluated): with no brand book and the design left to us, a choice
among concrete kits gets the client's direction before the prototypes are built on one.

## Consequences

- Downside: three kits to build before the first working session, after the developers' library
  choice.
- New obligation: the client's choice confirmed in writing
  ([[COM-018 Written minutes, notices and amendments]]), since the Milestone 1 UI kit and the later
  screens build on it.
- New obligation: the kits use component libraries the developers accept, so the app can be built as
  designed.
- Easy to reverse before the client chooses; harder after, once the prototypes use the kit.
- Related: [[DEC-010 Confirm the product with the client through prototypes in code]].
