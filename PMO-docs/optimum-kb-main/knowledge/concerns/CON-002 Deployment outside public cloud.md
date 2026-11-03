---
type: concern
id: CON-002
status: draft
origin: evaluated
author: claude-code/claude-opus-5-5
kind: operations
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-11-03 Solution proposal - rendering]]"
  - "[[2025-11-05 Proposal slides - rendering]]"
  - "[[2026-07-14 Cybersecurity framework - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-11-05 WBS sent to the client - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 1]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
  - "[[2025-11-25 Contract chat - rendering 1]]"
  - "[[2025-11-25 Contract chat - rendering 3]]"
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
capabilities:
  - "[[CAP-011 Platform, environments and handover]]"
tags:
  - deployment
  - hosting
---
# CON-002 Deployment outside public cloud

## What must hold

The system can be deployed and updated where the client's servers are, which may not be a public
cloud, and updates reach about 70 rig desktops that are often offline.

## Why

Anton: the Flutter team's experience is mostly web projects on AWS, Azure or Google Cloud, while this
looks like an on-premise deployment, harder to connect to and to deliver updates to
([[2026-09-25 Optimum Eng sync - transcript]] 00:17:49, 00:18:10). Arseniy: discussed with the team;
the plan carries a lot of DevOps hours for deploying the system (00:18:22). Where the server is
hosted is not settled in this source.

What the client said in October 2025 (added 2026-09-28, batch 1 of the seed ingest). Both answers
are kept; they pull in different directions and come from the same document:

- Where the central server should live: "Central server on-premises; remote sites use local caches
  with sync when connectivity allows." ([[2025-10-29 Client answers to the Q&A register - rendering]]
  C.5)
- Whether they can run it: "Do you have the technical capability (staff and infrastructure) to deploy
  and maintain centralized services on-premises?" - "No" (C.6).
- First call: "the client doesn't want to depend on the cloud only, they think about on-premises
  storage as well", and "The Client expects advice from our side"
  ([[2025-10-22 First call with OES - notes]] key point 6).

The first call's transcript (added 2026-09-28, batch 2): storage was undecided - "is this going to be
cloud based or is this going to be localized on each computer and migrated to its physical server in
our office or is it going to be a hybrid arrangement? I think that is something that we need to
deliberate on" ([[2025-10-22 First call with OES - transcript]] 0:43:55). What the client did want:
"definitely we need to have local access to data, you know, natively on the individual computers on the
job site ... There should be a smart way, you know, to migrate those data onto into a physical server in
the office. We do not want. While we see some of the merits of having some form of cloud based, we
don't want to be totally dependent 100% on cloud based solutions because these ... Confidential customer
data and we have confidentiality to protect. And at the same time we don't want to be subjected to
outages ... like we're having recently with AWS" (0:44:41).

Presale history (added 2026-09-28, batch 2):

- November 2025, the proposal: an on-premises hybrid, "a central On-Premise Server deployed at your
  headquarters"; the client provisions hardware, network and licences; "initial server setup,
  deployment, and ongoing on-premise maintenance is not included in the core development budget"
  ([[2025-11-03 Solution proposal - rendering]]).
- The slides: "centralized cloud control", with a central database "AWS PostgreSQL Database" described
  as "Deployed at OES HQ" - a contradiction within one slide
  ([[2025-11-05 Proposal slides - rendering]] slide 14); then iteration 2: "Infrastructure would be
  implemented using cloud provider instead of hybrid or on-premise approach" (slide 24).
- July 2026, the cybersecurity framework: "All personal data must be stored inside Saudi Arabia", and a
  cloud provider operating "within the Saudi Arabia Central Region"
  ([[2026-07-14 Cybersecurity framework - rendering]]; [[CON-007 Saudi cybersecurity and data protection rules]]).

From the presale chat, November and December 2025 (added 2026-09-28, batch 5):

- After the proposal was presented on 5 November: "он прем им и не нужен скорее всего, вроде как мысль
  до него донёс что лучше на gcp всё сделать и железки не мучать самим" (Aliaksei Tsitou,
  [[2025-10-20 Presale chat - rendering 1]] 2025-11-05 15:03).
- The plan of 12 November: "Заменяем он прем хранение на клауд GCP, девопсы пересматривают оценку с
  учетом этого изменения" (Marina Zaretskaya, [[2025-10-20 Presale chat - rendering 2]] 2025-11-12
  10:12).
- The draft reply to the client, 24 November: "Regarding the cloud provider, we suggest AWS. While Azure
  and GCP are also excellent options, AWS offers comparable pricing and provides additional discounts
  through our partnership program" (2025-11-24 12:44).
- The re-estimate of 25 November: "клиент уходит от онпрем и выбирает клауд ( ассампшн AWS)"
  (2025-11-25 09:37).
- 24 December: "6 месяцев бесплатной инфры от старта разработки дадим" (Nikita Prygodich, answering
  "AWS", 2025-12-24 11:25).

From the contract chat, 2026 (added 2026-09-28, batch 6; [[2025-11-25 Contract chat - rendering 1]],
[[2025-11-25 Contract chat - rendering 3]]):

- To the client, 5 January 2026: "During the development process, all AWS infrastructure including all
  environments will be owned and managed by Innowise via the Innowise AWS account. The arrangement for
  the production environment will continue for three months after the go-live date. After this period,
  we will hand over all infrastructure to your account for full ownership" (2026-01-05 12:47).
- July 2026, AWS dropped: "с точки зрения инфраструктуры (AWS) регион в целом в зоне риска. Т.е.
  сегодня часть сервисов недоступно и не факт что завтра там что то появится в рабочем режиме" (Alexey
  Gamanovich, 2026-07-10 18:06); and the region cannot be left: "Там очень строгие правила и выйти за
  пределы MENA никак нельзя" (Uladzislau Murashka, 2026-07-13 15:50).
- GCP in Dammam instead: "почти все сервисы доступны, из основных доступны все" (Nikita Verbovikov,
  2026-07-14 10:38), and billing works from outside the Kingdom with monthly invoicing (12:04); "нужно
  идти с GCP, клиент делает аккаунт (нужно чтобы аккаунт сделал кто-то именнто из KSA ) и дает
  возможность работать под этим аккаунтом" (Gamanovich, 12:05).
- Innowise's letter of 14 July put the hosting region and data residency outside the current SOW; the
  client's final contract binds them (10.2; [[COM-015 Saudi cybersecurity and regulatory compliance]]).

From the SOW and the contract (added 2026-09-28, batch 3): the client provides "all required
infrastructure (servers, hosting, licenses, VPN access, etc.)" and the final handover is "build
deployment to the Customer's servers" ([[2026-06-15 SOW v10.4 - rendering]]); Innowise must meet the
Saudi rules on "hosting, cloud services, data residency and cross-border transfers"
([[2026-09-07 Final contract - rendering]] 10.2; [[COM-015 Saudi cybersecurity and regulatory compliance]]).
The SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) makes the client provide "all required infrastructure (servers,
hosting, licenses, VPN access, etc.)".

From the two WBS versions (added 2026-09-28, batch 4). The v1 WBS ([[2026-09-25 v1 WBS - rendering]]) DevOps tab is written for a cloud -
"ready-made Terraform modules for two to three environments", "CloudWatch metrics/alarms", load
balancers - and has no line for getting updates to the rig desktops (DevOps rows 6 to 16). The WBS sent to the client on 5 November 2025
was built for the client's own servers ("I. Environment & VM Automation (On-Premises)") and had a line
for it: "CRITICAL: Design, build, and rigorous testing of a robust auto-update/forced-update mechanism
for 70+ remote Windows clients over sketchy connectivity"
([[2025-11-05 WBS sent to the client - rendering]], DevOps rows 6 to 14). So the current estimate may
not cover delivering updates to the rigs, which this Concern needs (our reading, not checked against the
P&L or the resource plan).

The initial estimates, as history (AGENTS.md rule 6), in hours, min to max as the sheets have them:

| DevOps | v1 WBS | WBS sent to the client, 5 Nov 2025 |
|---|---|---|
| All DevOps | 168 to 232 (DevOps row 16; roll-up row 25) | 448 to 600 (DevOps row 26); its roll-up says 449 to 600 (Selected Development Estimation row 25) |
| Delivering updates to the rig desktops | no line | 56 to 72 ("Desktop App (MAUI) Update Pipeline", DevOps row 14) |

From the call of 1 October (added 2026-10-02; [[2026-10-01 Optimum Three Caballeros call - transcript]]): how builds reach the
rigs is "вот это первый вопрос. Организационный, как будет доставка работать" (Alexey, 00:08:15). The
routes named: a download "из какого-то шаритфолдера" with a pop-up when a new version is out (Alexey,
00:06:54); "просто с флешкой инженер приезжает и ставит" (Mikhail, 00:07:34); the builds kept in the
cloud, "через Cloud Storage раздавать все новые релизы, новые билды, вот эти экзешники", or in an
artifact registry (Alexey, 00:26:17, 00:27:57). It is to be shown to the client at the start, so they can
say "у нас нету таких логистических цепей, чтобы такую доставку так организовывать" (Alexey, 00:09:32).

## Affected requirements

- [[REQ-001 Record and calculate a shift without internet]]
- [[REQ-003 Sign in on a shared rig computer]]

## Treatment

Partly [[DEC-004 Backend stack]] (self-hosted Supabase or a classic backend). The hosting decision
itself is not recorded yet.

Hosting, since 2026-10-02: proposed, not decided, in [[DEC-012 Host the central system on Google Cloud in the Kingdom]].
