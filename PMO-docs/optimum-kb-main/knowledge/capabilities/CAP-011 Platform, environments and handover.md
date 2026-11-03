---
type: capability
id: CAP-011
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: enabler
baseline:
  - "WBS:Development Flutter!6-11"
  - "WBS:DevOps!6-15"
  - "SOW:M1 Solution Architecture Design"
  - "SOW:M1 UI Kit"
  - "SOW:M2 Environment preparation"
  - "SOW:M2 Base front-end components"
  - "SOW:M6 Final Handover"
  - "[[COM-013 Source code, IP and third-party components]]"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - capability
  - platform
  - devops
---
# CAP-011 Platform, environments and handover

## What it must do

Everything the product runs on and ships through: the architecture, the environments and pipelines
for both clients, the shared component library, the route by which the desktop app reaches the rig
PCs, and the final handover - "publication in the Customer's source-code system" and "build
deployment to the Customer's servers" ([[2026-06-15 SOW v10.4 - rendering]] row 11, Milestone 6,
Final Handover). "Provisioning production and staging infrastructure stays with the DevOps line and
the Customer (who provides servers, hosting, and access)" (row 11, Milestone 2, Environment
preparation).

## Coverage criteria

Drafted from the SOW v10.4 wording (row 11); the TL owns these.

- C1 The Solution Architecture Design and the UI Kit are delivered (M1).
- C2 Development environments, source-control repositories, a branching strategy and an automated
  build and integration pipeline exist for both clients (M2).
- C3 A shared component library and theme built from the UI Kit serves the web and the desktop, with
  the English localization scaffolding (M2).
- C4 The desktop app can be installed and updated on the rig PCs. No WBS row or SOW item names this
  route.
- C5 The final software is handed over as source code in the client's source-code system and a build
  deployed to the client's servers (M6).

## Refined by

- [[CON-002 Deployment outside public cloud]]
- [[CON-004 Scale and data volume]]
- [[CON-005 Easy and responsive interface]]
- [[DEC-004 Backend stack]]
- [[DEC-005 Desktop at the rig, web app at HQ]]
- [[DEC-007 Flutter for the desktop app]]
- [[DEC-012 Host the central system on Google Cloud in the Kingdom]]
- [[DEC-010 Confirm the product with the client through prototypes in code]] (its designer part
  runs against the UI Kit due in M1)
- [[COM-013 Source code, IP and third-party components]]

## Plan

M1 (architecture, UI Kit), starts M2 (environments, pipeline, components), continues through every
milestone, completes M6 (handover).
