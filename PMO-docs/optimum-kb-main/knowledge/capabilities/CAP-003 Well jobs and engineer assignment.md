---
type: capability
id: CAP-003
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: business
baseline:
  - "WBS:Development Flutter!26"
  - "WBS:Development Flutter!27"
  - "WBS:Development Flutter!50"
  - "SOW:M3 Project management (create, edit, assign)"
  - "SOW:M3 Project management feature"
depends_on:
  - "[[CAP-001 Identity, roles and access]]"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
tags:
  - capability
  - projects
---
# CAP-003 Well jobs and engineer assignment

## What it must do

HQ creates and edits well jobs ([[TRM-005 Project (well job)]]) and assigns and reassigns engineers
on the web. On the desktop, the engineer creates a project entry or selects and updates an existing
one, and the project gets an active status and an ID. "Assigning engineers is done on the web, not
desktop" ([[2026-06-15 SOW v10.4 - rendering]] row 11, Milestone 3, desktop Project management
feature).

## Coverage criteria

Drafted from the SOW v10.4 wording (row 11); the TL owns these.

- C1 On the web, a user creates and edits a project, assigns and reassigns engineers, and sees the
  project list with basic filter and search (M3).
- C2 On the desktop, an engineer creates a new project entry or selects and updates an existing one,
  enters the required details, and the project gets an active status and an ID (M3).
- C3 Engineers are assigned on the web only (M3).

Not included, per the SOW: project templates, bulk assignment. Location Management and Project
Template Management are outside the v1 estimate (Development Flutter rows 23, 24).

## Refined by

- [[REQ-020 Create and manage well jobs and assign engineers]]
- [[QUE-011 Who wins when a project is edited on the web and on an offline desktop]]
- [[QUE-012 Are engineers assigned to rigs or to wells]]
- [[TRM-004 Rig]]
- [[TRM-005 Project (well job)]]
- [[TRM-006 Well section]]

## Plan

M3.
