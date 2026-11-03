---
type: source
kind: presale
date: 2026-07-14
original: https://docs.google.com/document/d/1SEBpkHih_4OCkGzdXrED-UwKy_sJa3bpt2YfU-7e9Fg
received_from: Aliaksei Tsitou (presale), shared in the contract chat's space
purpose: the Saudi cybersecurity and data protection baseline presale set for the project
supersedes:
procedure_version: b4cb7da
---
# 2026-07-14 Cybersecurity framework - overview

kind: presale. original: Google Doc "Optimum cybersec framework". Rendering:
[[2026-07-14 Cybersecurity framework - rendering]].

## What it is

A checklist of controls from four Saudi frameworks, written as instructions to the development team:
NCNICC-1:2025 (private sector baseline, "your primary mandatory framework"), DCC-1:2022 (data
cybersecurity), PDPL (personal data protection) and CCC-2:2024 (cloud). It was written during the
contract talks of July 2026, when the client raised Saudi compliance.

Link-only, listed here: an English machine translation of NCNICC-1:2025, posted in the contract chat
(attachment of spaces/AAQAXooObiI/messages/JK6tANhCUWA.dfeYYHEhElk). Not rendered: a third-party
regulation, long, and a machine translation. What would make it usable: the official NCA text, read
against the controls the project agrees to in discovery.

## How far to trust it

Medium (`sources/presale/`): Innowise's reading of the regulations, not the regulations and not an
agreement with the client. The contract's cybersecurity article (batch 3) and the July 2026 contract
chat (batch 6) say which of these the project owes; the chat already shows that "all" of them cannot
be met in this budget (Gamanovich, 2026-07-10).

## Not for

Legal interpretation - ask a PM.

## Removed at ingest

Nothing.

## Summary

Secure development (secure SDLC, OWASP and CWE, SAST, vulnerability scans, penetration tests if the
client is Category A), identity (MFA for admin and remote access, least privilege), SBOM; data
controls (classification, TLS 1.2 or higher, encryption at rest, key management, immutable audit logs,
secure disposal); PDPL (privacy by design, consent, data subject rights, personal data stored inside
Saudi Arabia, records of processing); cloud (zero trust, DevSecOps scanning, cloud IAM and KMS, audit
logs kept per the client's retention policy, a provider in the Saudi region).

## Proposed changes

In the batch 2 table in [[2025-10-22 First call with OES - minutes 2]], rows 21, 24 and 25.
