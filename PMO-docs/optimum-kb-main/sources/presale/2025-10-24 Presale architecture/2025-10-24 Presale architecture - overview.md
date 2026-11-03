---
type: source
kind: presale
date: 2025-10-24
original: https://docs.google.com/document/d/1Iw685h0d8EJ2NCetSxWNEXei46ggl20hZ8KSpiVv_RM
received_from: Aliaksei Sauta (presale solution architect)
purpose: the presale architecture - what the architect took from the first call and proposed
supersedes:
procedure_version: b4cb7da
---
# 2025-10-24 Presale architecture - overview

kind: presale. original: Google Doc named like the presale chat, created 2025-10-24, changed
2025-11-04; linked in the presale chat on 2025-11-03 as "architecture from Architect". Rendering:
[[2025-10-24 Presale architecture - rendering]].

## What it is

One page: the architecturally significant requirements and NFRs as the architect heard them on the
first call, and the proposed components - a MAUI desktop app, an aggregation service for sync, a
central service, an identity provider, a web app - with a tentative stack.

## How far to trust it

Medium, and historical (`sources/presale/`): a presale recommendation that needs refinement. The stack
is superseded (Flutter; the backend is open in DEC-004).

## Not for

Technical decisions for delivery.

## Removed at ingest

Nothing. The diagram is only in the original.

## Summary

Manual input from lab equipment at about 70 simultaneous sites, central storage, calculations and
hydraulics simulation, reports with PDF, CSV and Excel, inventory including lab tools. A Windows
desktop app is required for offline work. At least three user groups: engineers, project supervisors,
management. The aggregation service owns sync.

## Proposed changes

In the batch 2 table in [[2025-10-22 First call with OES - minutes 2]], rows 7, 11, 15, 18, 22 and 27.
