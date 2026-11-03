---
type: commitment
id: COM-013
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
party: us
due: with each accepted milestone, fully at final acceptance, and immediately on termination
clause: "6.6, 8.1-8.5, 11.7"
sources:
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 2]]"
tags:
  - ip
  - source-code
---
# COM-013 Source code, IP and third-party components

## What is owed

From the contract ([[2026-09-07 Final contract - rendering]]):

- "Upon each accepted milestone and upon any expiry or termination, the Second Party shall deliver all
  work-in-progress, source code, repositories, documentation, credentials, configurations and related
  materials corresponding to amounts paid by the First Party, without withholding or technical
  lock-in." (6.6); on termination also "reasonable transition assistance" (11.7).
- Bespoke deliverables "shall be exclusively owned by the First Party upon payment of the corresponding
  accepted milestone"; Innowise assigns the IP and gets equivalent assignments from employees and
  subcontractors (8.1, 8.2).
- "Source code and related repositories shall be delivered progressively with each accepted milestone
  and fully at final acceptance." (8.3)
- No open-source or third-party components "that impose copyleft, disclosure, recurring licence fees,
  usage restrictions or other material obligations" without prior written approval; approved ones
  disclosed with licence terms (8.4).
- Pre-existing generic tools stay Innowise's only if "separately identified in the SOW", with "a
  perpetual, irrevocable, worldwide, royalty-free licence" for the client (8.5).

From the SOW v10.4: "The transfer of software source code shall occur through publication in the
Customer's source code storage and management system. The transfer of software builds shall be
executed by posting on the Customer's servers." ([[2026-06-15 SOW v10.4 - rendering]], assumptions)

## By when

Progressively, milestone by milestone.

## How it is accepted

Tied to milestone acceptance and payment ([[COM-002 Written acceptance of each deliverable]],
[[COM-012 Payment schedule]]).

History (added 2026-09-28, batch 6): PMO's reading of the client's May 2026 version listed "may not use
any open-source code (пункт 8.3)" (Alexey Gamanovich, [[2025-11-25 Contract chat - rendering 2]]
2026-05-07 17:33). The final contract's 8.4 limits only components with copyleft, disclosure, recurring
fees or similar obligations, and allows approved ones. Legal reading: ask a PM.

## Drives

- [[DEC-004 Backend stack]] (a self-hosted platform's licence must pass 8.4)
- [[DEC-007 Flutter for the desktop app]] (the framework's licence, the same test)
