---
type: source
kind: presale
date: 2025-11-03
original: https://docs.google.com/document/d/1xZZ4DTDPOquMto5oD2izaRSBc6kISwpxzQs-zhtrGkM
received_from: Daniil Lynko and Aliaksei Tsitou (presale)
purpose: the presale solution proposal behind the client-facing slides
supersedes:
procedure_version: b4cb7da
---
# 2025-11-03 Solution proposal - overview

kind: presale. original: Google Doc "Proposal for Optimum Engineering Standards (without budget)", in
the presale shared drive. Rendering: [[2025-11-03 Solution proposal - rendering]].

## What it is

The internal proposal draft: the client's problems and objectives, functional and non-functional
requirements, an on-premises hybrid architecture, five phases, team composition, deliverables,
challenges, assumptions, and post-project support options. Budget and hours are placeholders.

## How far to trust it

Medium (`sources/presale/`), and historical: what presale planned in November 2025. The client saw
the slides ([[2025-11-05 Proposal slides - overview]]), not necessarily this document.

## Not for

Scope (the SOW and the WBS are the reference), hosting (it proposes on-premises; the slides and later
sources move to cloud), or support terms (the contract sets them).

## Removed at ingest

The percentage by which the on-demand support rate exceeds the team-allocation rate. The rate table is
empty in the original.

## Summary

On-premises hybrid: a MAUI desktop app with SQLite at each rig, a central PostgreSQL, aggregation
service, central service, identity provider and React web app at HQ. Objectives include 99.9% data
integrity, five report types including engineering calculation reports, guided wizards, 100+
locations. Challenges named: bi-directional sync, on-premises deployment without client staff,
calculation complexity, and the visualisation scope, since the client's "No" suggested complex
visuals. Assumptions: the client provisions hardware; deployment and maintenance outside the budget;
mobile a future phase; migration scoped separately; English only.

## Proposed changes

In the batch 2 table in [[2025-10-22 First call with OES - minutes 2]], rows 12, 13, 15, 18, 21, 22,
27, 28 and 29.
