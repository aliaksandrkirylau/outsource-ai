---
type: concern
id: CON-007
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: compliance
sources:
  - "[[2026-07-14 Cybersecurity framework - rendering]]"
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 3]]"
  - "[[2026-07-14 NCNICC-1 translation - overview]]"
capabilities:
  - "[[CAP-001 Identity, roles and access]]"
  - "[[CAP-012 Security and compliance]]"
tags:
  - security
  - compliance
  - pdpl
---
# CON-007 Saudi cybersecurity and data protection rules

## What must hold

The system and the way it is built meet the Saudi controls that apply to it. Presale set them out in
July 2026 as four frameworks ([[2026-07-14 Cybersecurity framework - rendering]]):

- NCNICC-1:2025, "your primary mandatory framework": secure SDLC; secure coding (OWASP Top 10, CWE Top
  25) with SAST in CI/CD; vulnerability scans on all environments before go-live; "If the client is
  Category A, you are required to perform regular penetration testing ... For Category B, it is
  recommended"; patched OS, middleware and libraries; MFA "for all administrative access and remote
  access to the system"; least privilege in RBAC; an SBOM.
- DCC-1:2022: data classification labels in the architecture; TLS 1.2 or higher; encryption at rest,
  column-level for sensitive fields; a key management system; audit logs of every access to sensitive
  data (who, when, what, action), immutable; secure disposal.
- PDPL: privacy by design; a consent module (capture, record, withdraw); data subject rights (access,
  rectification, erasure); "Critical: All personal data must be stored inside Saudi Arabia", backups
  and logs included; records of processing activities.
- CCC-2:2024: zero trust and micro-segmentation; container and IaC scanning, SAST, DAST and dependency
  scanning in the pipeline; cloud IAM without root credentials, MFA for developers; the provider's KMS;
  cloud audit logs kept "according to the client's data retention policy"; a provider in the Saudi
  region aligned with NCA CCC.

Which of these the project owes is not settled in this source. Since batch 3: the contract makes all
applicable Saudi requirements ours, "No category of applicable Saudi requirement is excluded"
([[2026-09-07 Final contract - rendering]] 10.2), while the SOW v10.4 has the client provide the
requirements before the start - see [[COM-015 Saudi cybersecurity and regulatory compliance]] and
[[COM-014 Confidentiality and personal data]].

How the team read the frameworks in July 2026 (added 2026-09-28, batch 6;
[[2025-11-25 Contract chat - rendering 3]]):

- ECC-2:2024 does not apply: "ecc-2:2024 это госы и критическая инфра страны, не применимо к данному
  проекту" (Aliaksei Tsitou, 2026-07-14 08:46). DCC is part of ECC and drops out with it; CCC is for
  cloud-hosted components (09:29).
- The baseline proposed to the client: "NCNICC-1:2025 + PDPL" (09:30); "пока целимся на
  \"NCNICC-1:2025 + PDPL\" , делаем на GCP, уточняем через дискавери (детализируемся + gap analys)"
  (Alexey Gamanovich, 12:28). The PDPL applies: "мы храним данные инженеров/пользователей платформы, эт
  персонал дата = попадает по ПДПЛ" (Tsitou, 09:29).
- The NCNICC-1 controls "сверх естественный условий не диктует для Category B (наш кейс)", but the
  organisational ones sit with the client: "cybersecurity в оргаганизации должна быть описана и
  поддерживаться в актуальном состоянии ... со стороны клиента соот. должен быть кто-то кто будет это
  делать на своей стороне, Исполнительно может только помогать" (Gamanovich, 12:05; controls such as 2-1-1
  and 2-13, 16:43). "для PDPL нужно будет GCP в KSA" (16:43).
- If data were kept outside the region: an explicit privacy policy and time-stamped consent logs
  (Uladzislau Murashka, 12:08).
- The English working text of NCNICC-1: [[2026-07-14 NCNICC-1 translation - overview]] (machine
  translation, unchecked).

The client's category: [[QUE-005 Is the client an NCA Category A or B entity]] (our reading: B).

## Why

The client is a Saudi company serving Saudi Aramco; the data includes its customers' confidential
data ([[CON-006 Confidentiality of the client's customers' data]]) and the personal data of its users.

## Affected requirements

- [[REQ-003 Sign in on a shared rig computer]] (MFA for admin and remote access)
- [[REQ-004 Roles and what each role can do]] (least privilege)
- [[REQ-006 Edit or backfill past entries with approval]] (audit logs)
- [[REQ-015 Import of historical data]] and [[CON-004 Scale and data volume]] (retention, disposal)

## Treatment

Not decided. Several items are not in the v1 WBS ([[2026-09-25 v1 WBS - rendering]]): penetration testing, a consent module, data subject
rights. Whether penetration testing is required depends on
[[QUE-005 Is the client an NCA Category A or B entity]]. Where the data may be hosted is
[[CON-002 Deployment outside public cloud]].

Hosting, since 2026-10-02: proposed, not decided, in [[DEC-012 Host the central system on Google Cloud in the Kingdom]].
