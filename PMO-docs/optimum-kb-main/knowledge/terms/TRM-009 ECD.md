---
type: term
id: TRM-009
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
aliases:
  - equivalent circulating density
sources:
  - "[[2025-11-20 Client formula and chart samples - rendering]]"
  - "[[2025-10-29 Client sample daily report - rendering]]"
tags:
  - domain
  - hydraulics
---
# TRM-009 ECD

## Definition

The density the drilling fluid acts with at a depth while it circulates: its own density plus the
pressure lost to friction in the annulus above that depth, expressed as a density. The sources write
only "ECD"; "equivalent circulating density" is the industry's expansion, not written in them.

## Context and units

- The client's procedure: "ECD = P_aT / ((0.052)(TVD)) + ρ", where P_aT is the sum of the annular
  pressure drops (Figure 2-1, step 11;
  [[2025-11-20 Client formula and chart samples - rendering]] image 3). The units are not stated.
- The client's daily report: "ECD @ Bit Depth" and "ECD @ Casing Shoe", in ppg
  ([[2025-10-29 Client sample daily report - rendering]] rows 43, 44).
- The client's program screens: ECD with and without cuttings ("ECD w/ Cut- CSG Shoe", "ECD w/ Cut -
  BH", "ECD /wo Cuttings", "ECD w/ Cuttings"), at the casing shoe and at the bottom, in lb/ft^3
  (images 8, 10); the operating window plots it against flow rate (image 10).
- Units: [[REQ-018 Units of measure and conversion]]. Where it is computed:
  [[REQ-008 Fluid hydraulics simulation]].

## Not to be confused with

- ESD, on the same screen ("ESD /wo Cuttings initial", "ESD w/ Cuttings initial", image 10): the static
  counterpart, with no circulation (evaluated: without cuttings it equals the mud density there, 78.00).
- EMW, in the swab and surge procedure ("Surge Pressure EMW", "Swab Pressure EMW", Figure 2-4, image 6)
  and the tripping table (image 9): the pressure while the pipe moves, as a density, not while the fluid
  circulates.
- The mud weight or density itself: ρ in the formula.
