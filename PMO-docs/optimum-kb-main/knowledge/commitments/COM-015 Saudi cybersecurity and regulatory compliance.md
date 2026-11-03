---
type: commitment
id: COM-015
status: disputed
origin: extracted
author: claude-code/claude-opus-5-5
party: us
due: throughout; incidents promptly
clause: "6.4, 10.1-10.4; SOW v10.4 Compliance"
sources:
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 3]]"
tags:
  - compliance
  - security
---
# COM-015 Saudi cybersecurity and regulatory compliance

## What is owed

Disputed: the contract and the SOW v10.4 place the compliance burden differently. Both kept.

### Version A - the contract

- "The Second Party warrants that the architecture, software, development process and Deliverables
  shall comply with all cybersecurity controls, requirements, frameworks and directives issued by the
  competent authorities in the Kingdom of Saudi Arabia that are applicable to the Project, including
  applicable requirements of the National Cybersecurity Authority (NCA)." (10.1)
- "The Second Party shall comply with applicable Saudi requirements relating to personal data,
  information security, hosting, cloud services, data residency and cross-border transfers to the
  extent such requirements apply to the Project. No category of applicable Saudi requirement is
  excluded from this Agreement." (10.2)
- A regulatory change during implementation: notify and implement; "Where the change was publicly
  issued before the Effective Date or reasonably foreseeable by a professional provider, it shall not
  constitute a Change Request." (10.3)
- Security incidents: notify promptly, cooperate in containment, investigation, remediation and
  notifications (10.4); comply with all laws for the deployment and operation of the deliverables in
  the Kingdom (6.4).

([[2026-09-07 Final contract - rendering]])

### Version B - the SOW v10.4

"Security, data protection, certification, and compliance requirements (GDPR, ISO, local regulations)
must be provided by the Customer before the project start." ([[2026-06-15 SOW v10.4 - rendering]],
assumptions)

### How the contract wording came about

From the contract chat (added 2026-09-28, batch 6). The dispute stays for Anton; this is the record of
what the team knew.

- The client, 7 July 2026: "the Agreement should expressly require that the software, system
  architecture, databases, and all project deliverables fully comply with all applicable Saudi
  cybersecurity regulations, data protection requirements, and other relevant regulatory standards in
  force within the Kingdom" ([[2025-11-25 Contract chat - rendering 3]] 2026-07-07 13:13).
- Inside, two views. Lizaveta Shauchenka: "отвечаем тогда клиенту в письме, что полностью соблюдаем все
  применимые требования Саудовской Аравии в области кибербезопасности, защиты данных и других
  регуляторных требований" (2026-07-10 15:50). Alexey Gamanovich: "мы \"все\" регуляции поддержать не
  можем ... уж точно не в тот бюджет кот здесь определен" (2026-07-10 18:20).
- Innowise's letter of 14 July proposed NCNICC-1:2025 and the PDPL "as applicable to the scope of the
  Services", with "any requirements relating to the physical location of infrastructure, cloud hosting
  region, or data residency within the Kingdom of Saudi Arabia" outside the current SOW (2026-07-14
  15:18).
- The client's final version widened it to "all applicable Saudi cybersecurity controls, requirements,
  frameworks and directives" plus hosting, cloud services, data residency and cross-border transfers
  (Yauheni Krasner's review, 2026-08-13 09:26); Innowise's objection of 25 August was not taken up
  (2026-09-02 15:55).
- Accepted as a known risk on 2026-09-07: "широкая формулировка compliance со всеми применимыми
  требованиями Saudi Arabia" (2026-09-07 10:32; [[DEC-009 Sign the client's final contract as it stands]]).

## By when

Throughout; the SOW's version before the start.

## How it is accepted

Not stated.

## Drives

- [[CON-007 Saudi cybersecurity and data protection rules]]
- [[QUE-005 Is the client an NCA Category A or B entity]]
- [[CON-002 Deployment outside public cloud]] (hosting and data residency)
