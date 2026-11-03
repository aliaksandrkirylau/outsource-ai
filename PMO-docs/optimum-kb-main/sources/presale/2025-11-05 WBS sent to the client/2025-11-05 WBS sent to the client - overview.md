---
type: source
kind: presale
date: 2025-11-05
original: https://docs.google.com/spreadsheets/d/1KsP4-7CAzXqCQywxdLht56bbyUl38bqXEdQ9PsP_sfQ
received_from: Innowise presale; sent to the client on 5 November 2025 (Lizaveta Shauchenka, contract chat, 2025-12-01)
purpose: what the client was shown as the estimate before the SOW - the reference for "what did we tell them" questions
supersedes:
procedure_version: b4cb7da
---
# 2025-11-05 WBS sent to the client - overview

kind: presale. Rendering: [[2025-11-05 WBS sent to the client - rendering]]. Superseded as the estimate
by the v1 WBS, [[2026-09-25 v1 WBS - overview]].

## What it is

The Google Sheet "Optimum Engineering Standards - WBS", six tabs: Overview, Discovery Estimation,
Selected Development Estimation, Development, DevOps, Assumptions & Risks. Its Overview says "Created
05.11.2025". That it went to the client comes from the contract chat ([[2025-11-25 Contract chat - rendering 1]]), 2025-12-01:
asked "а мы клиенту WBS отправляли?", Lizaveta Shauchenka linked this sheet: "вот эта 5 ноября
отправлялась". The proposal slides of the same day carry the estimate as images
([[2025-11-05 Proposal slides - rendering]], slides 34 to 38).

## How far to trust it

Medium (`sources/presale/`): what the client was shown, not what they agreed. The binding texts are the
contract and, once confirmed as its annex, the SOW. Useful when the client refers back to it: mobile,
the onboarding wizard, location management and project templates were all in its MVP, and the
calculations were estimated "per 1 algorithm" (assumption 26).

## Not for

Scope checks (use the v1 WBS and the SOW v10.4), or rates and amounts (removed; in the original and the
P&L).

## Removed at ingest

Every rate and amount: the rate and amount columns of the Discovery and Selected Development tabs, the
forecasted cost row in the Overview, the "TOTAL USD" row. The company address and phone number.

## Summary

A MAUI estimate for "Web application and Cross Platform application": .NET back end, MAUI client,
ReactJS web, SQLite on site, PostgreSQL centrally. Every line in the MVP, mobile included. Discovery
by role, domain experts included. An on-premises DevOps tab: VMs provisioned with Ansible/Terraform,
CI with SAST, RBAC security tests, logging and monitoring with alarms for site synchronization lag,
backup and disaster recovery, and a desktop auto-update pipeline marked "CRITICAL". An optional data
engineer. 25 assumptions (numbered to 26, no 24) and 8 risks. 4 to 6 months.

## Proposed changes

In the batch 4 table in [[2026-09-25 v1 WBS - overview]], rows 4 to 11.
