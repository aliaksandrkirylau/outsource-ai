---
type: concern
id: CON-008
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: compliance
sources:
  - "[[2026-10-20 Introductory call - transcript]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-07 Final contract - rendering]]"
capabilities:
  - "[[CAP-005 Mud engineering calculations and simulation]]"
  - "[[CAP-008 Reports and report approval]]"
  - "[[CAP-012 Security and compliance]]"
tags:
  - compliance
  - standards
---
# CON-008 Compliance with ISO 9001, ISO 14001 and API standards

## What must hold

The tool, and the records it generates, align with ISO 9001 and ISO 14001 and with the API standards
that govern the client technically. Mr. Lawal, the client's sponsor: "whatever we're also doing, okay,
should be compliant, you know, to the industry standard, the standard for quality and the standard, you
know, for safety"; "when ISO 9001 and 14001 certified organization, So whatever tool we're using and,
and the records we generate from those tools should very much align and comply, you know, to those
international standards"; "we're being governed technically by API standards, you know, so technical
compliance to the American Petroleum Institute requirement, you know, an alignment in the way we design
our tool is also paramount" ([[2026-10-20 Introductory call - transcript]] 00:45:35).

No measure yet. Not stated: which records, which clauses of the two ISO standards, which API
documents. To settle in Discovery.

## Why

The client is certified to ISO 9001 and ISO 14001 and works in oil and gas under API standards:
"there's no point in designing a tool, however user-friendly it is and stuff, that is out of compliance
to the international standards" (00:45:35). Anton: "that is something we definitely have in the back of
our hands and will be one of the kind of cornerstones and staples for the technical design" (00:46:59).

Against the baseline (evaluated, 2026-10-30): the contract's compliance articles are about Saudi
cybersecurity, data protection and hosting ([[2026-09-07 Final contract - rendering]] 10.1, 10.2;
version A of [[COM-015 Saudi cybersecurity and regulatory compliance]]). The SOW v10.4 names none of
the three standards and puts such requirements on the client: "Security, data protection,
certification, and compliance requirements (GDPR, ISO, local regulations) must be provided by the
Customer before the project start." ([[2026-06-15 SOW v10.4 - rendering]], assumptions; version B of
COM-015). So what the standards add beyond the WBS lines may be a change request candidate; a
Requirement that comes from it gets its scope check.

Left out of the 20 October follow-up on purpose, for Mikhail and Kavalchuk to look at first
([[2026-10-20 Introductory call follow-up]], `pm/exports/`). The BA's reading of the API 13 series and
RP 13D: [[2026-10-22 API standards research]] (`ba/`, not evidence).

## Affected requirements

- [[REQ-007 Derived values and standard calculations]]
- [[REQ-008 Fluid hydraulics simulation]]
- [[REQ-010 Reports]]

## Treatment

None yet. The acceptance risk: [[K-10 Fixed price with vague acceptance criteria]].
