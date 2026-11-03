---
type: decision
id: DEC-012
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: architecture
deciders:
  - tbd
sources:
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
  - "[[2025-11-25 Contract chat - rendering 3]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
capabilities:
  - "[[CAP-011 Platform, environments and handover]]"
tags:
  - hosting
  - deployment
  - compliance
---
# DEC-012 Host the central system on Google Cloud in the Kingdom

## Context

The web app, the API and the central database need a home, and the hosting decision was not recorded
([[CON-002 Deployment outside public cloud]], Treatment). The Saudi rules bind it: Innowise must comply
with the requirements on "hosting, cloud services, data residency and cross-border transfers", and "No
category of applicable Saudi requirement is excluded" ([[2026-09-07 Final contract - rendering]] 10.2;
[[CON-007 Saudi cybersecurity and data protection rules]]). The SOW v10.4 has the client provide "all
required infrastructure (servers, hosting, licenses, VPN access, etc.)" and the final build deployed "to
the Customer's servers" ([[2026-06-15 SOW v10.4 - rendering]]). Treats
[[CON-002 Deployment outside public cloud]] and [[CON-007 Saudi cybersecurity and data protection rules]].

July 2026, in the contract chat ([[2025-11-25 Contract chat - rendering 3]]): AWS "регион в целом в зоне
риска" (Alexey Gamanovich, 2026-07-10 18:06); GCP in Dammam: "почти все сервисы доступны, из основных
доступны все" (Nikita Verbovikov, 2026-07-14 10:38); "нужно идти с GCP, клиент делает аккаунт (нужно
чтобы аккаунт сделал кто-то именнто из KSA ) и дает возможность работать под этим аккаунтом" (Alexey
Gamanovich, 12:05); "пока целимся на "NCNICC-1:2025 + PDPL" , делаем на GCP" (12:28).

The call of 1 October ([[2026-10-01 Optimum Three Caballeros call - transcript]]): where the web service
is deployed "еще вот это до конца не проработали" (Arseniy, 00:22:30). In the negotiations cloud or
on-premise "открытый вопрос оставался ... по-моему, премисс вариант как-то превалировал" (Mikhail,
00:24:16).

## Options considered

1. Google Cloud in the Kingdom (the Dammam region). Proposed (below).
2. Azure: "Там всего четыре клауд-провайдера, там еще Azure и Oracle ... Еще остается только Azure"
   (Alexey, 00:22:52). Named as the one left; not assessed.
3. Oracle Cloud. Lost: "Oracle нас не интересует, потому что специфичный, так сказать, опыт нужен"
   (00:22:52).
4. AWS, the presale assumption ([[CON-002 Deployment outside public cloud]]). Lost: "на текущий момент
   AWS там нет" (Alexey, 00:22:52); "AWS точно нет" (Arseniy, 00:24:02); services unavailable in the
   region in July (2026-07-10 18:06).
5. The client's own servers or data centre. Lost, in Alexey's view: "on-premise или в дата-центре они,
   скорее всего, не обеспечат", since the data centre would have to be certified for the Saudi
   cybersecurity controls, "вот этот ECC cybersecurity документу. Я склонен думать, что это, скорее
   всего, они хрен могут обеспечить" (00:24:31). The client answered "No" when asked if they can deploy
   and maintain centralized services on-premises
   ([[2025-10-29 Client answers to the Q&A register - rendering]] C.6), while preferring "Central server
   on-premises" (C.5). The team's July reading was that the ECC applies to government and critical
   infrastructure, not this client ([[CON-007 Saudi cybersecurity and data protection rules]]); both
   readings are kept.

## Decision

A proposal, not decided: "Соответственно, остается только Google Cloud. Поэтому пичить solution будем
просто через Google Cloud, если они скажут, не, ребят, мы говорим, окей, ну тогда дайте нам дата-центр,
где, в как, это что, кто со стороны дата-центра нам предоставит все доступы и все остальное, и на каких в
инструментах он как бы работает, да, вот orchestration слой, как он у них работает. И третье, ну, чтобы
они тогда предоставили сертификаты о том, что они compliant. В противном случае мы просто вычеркиваем из
контракта вот эти пункты." (Alexey, 00:24:31). Arseniy is to work the hosting out: "тебе нужно, чтобы
провентилировали хостинг" (00:26:17). Deciders not named (Anton, 2026-10-02: tbd), so draft.

## Rationale

AWS is not available in the region, the data must stay in the Kingdom, and the client is unlikely to
run a certified data centre; GCP covers part of the security controls: "Киберсекьюрити— там же
обеспечивается Google Cloud, все вот эти элементы, firewall и прочие какие-то механизмы" (Alexey,
00:28:03); "для PDPL нужно будет GCP в KSA, поэтому часть закроет сам GCP для Cybersecurity"
([[2025-11-25 Contract chat - rendering 3]] 2026-07-14 16:43).

## Consequences

- New obligation: the client opens the GCP account from the Kingdom and lets us work under it (July,
  12:05); the SOW's "Customer provides all required infrastructure" and the handover to "the Customer's
  servers" then mean that account.
- Downside: who pays for the cloud is open. Mikhail: "они могут попытаться на нас стоимость костов за
  облачного провайдера переложить" (00:25:49); [[COM-008 Client cooperation and dependencies]],
  [[K-1 Cloud hosting costs put on us]].
- The fallback "мы просто вычеркиваем из контракта вот эти пункты" runs against
  [[DEC-009 Sign the client's final contract as it stands]]: the client refused further changes to the
  contract. Not settled here; for the deciders.
- It goes against the client's stated preference for a server on their premises (C.5), so it has to be
  pitched and agreed: "первые шаги они будут не девелоперские, первые шаги они будут запитчить" (Alexey,
  00:26:17).
- Builds for the rigs can be served from the same cloud: "через Cloud Storage раздавать все новые
  релизы, новые билды, вот эти экзешники" (00:26:17).
- Hard to reverse once the environments and the data are in place.
