---
type: decision
id: DEC-007
status: proposed
origin: extracted
author: claude-code/claude-opus-5-5
kind: architecture
deciders:
  - human:arseniy.klimenko
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2026-09-25 v1 WBS - overview]]"
  - "[[2025-11-05 WBS sent to the client - rendering]]"
  - "[[2025-11-25 Project description - rendering]]"
  - "[[2025-11-25 Contract chat - rendering 2]]"
  - "[[2025-11-25 Economy chat - overview]]"
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
  - "[[2026-10-01 Solution vision diagrams - rendering]]"
valid_from: 2026-05-25
capabilities:
  - "[[CAP-011 Platform, environments and handover]]"
tags:
  - stack
  - desktop
---
# DEC-007 Flutter for the desktop app

## Context

Presale planned the rig app in .NET MAUI, one codebase for desktop and mobile, with a ReactJS web app:
"Local client application - MAUI", "Central office web application - ReactJS"
([[2025-11-25 Project description - rendering]]); the estimate sent to the client on 5 November 2025 was
built on that ([[2025-11-05 WBS sent to the client - rendering]], Overview row 8). By September 2026 the
plan is Flutter: "в итоге решили идти с платром, потому что myui-щиков у нас почти нихрена нет. У нас в
дотнете он один был ... Флаттер тут безопаснее, просто по наличию экспертизы. Но суть так же" (Arseniy
Klimenko, [[2026-09-25 Optimum Eng sync - transcript]] 00:22:01; "платром" is a recognition slip for
Flutter). The desktop client is Flutter (00:12:21).

How it came about, May 2026 (added 2026-09-28, batch 6). On 15 May Arseniy Klimenko read the scope as
"В скоупе есть React, .NET и MAUI": MAUI was the risk, one person had the expertise and had moved to
mobile, and the team advised adding about 20% to the MAUI part ([[2025-11-25 Economy chat - overview]]).
PMO on 20 May: "там есть привязка к технологии кот в компании есть у 1 девелопера и нет понимания
насколько хорошо владеет = bus factor -> предложение обсудить с клиентом альтернативу кот. есть в
компании в виде большего кол-ва сотрудников" (Alexey Gamanovich,
[[2025-11-25 Contract chat - rendering 2]] 2026-05-20 15:51). The call of 22 May: "Переходим с MAUI на
Flutter (или другую кроссплатформу), чтобы снизить риски и упростить подбор команды. Проверяем,
подходит ли Flutter под требования проекта." (Yauheni Krasner's summary, 2026-05-22 13:07). Treats
[[CON-001 Offline operation and sync between rigs and HQ]] and
[[CON-002 Deployment outside public cloud]]; the backend is [[DEC-004 Backend stack]], the platform
split [[DEC-005 Desktop at the rig, web app at HQ]].

## Options considered

1. .NET MAUI for the desktop (and a later mobile app from the same code), ReactJS for the web: the
   presale plan and what the client was shown. Lost on staffing: too few MAUI developers (00:22:01).
2. Flutter for the desktop. Chosen as the plan: the Flutter estimate of 22 May 2026, "оценка готова по
   стеку все релевантно, проблем с реализацией под требования не будет" (Sergei Gubkin,
   [[2025-10-20 Presale chat - rendering 2]] 2026-05-22 15:33); "актуальная оценка из чата с флатером"
   (Arseniy, 2026-05-25 14:14); the current estimate is the Flutter roll-up
   ([[2026-09-25 v1 WBS - overview]]; [[2026-09-25 v1 WBS - rendering]], Total Estimation Development
   Flutter).

## Decision

Flutter for the desktop app. Arseniy Klimenko, 25 May 2026: "Со своей стороны по флатеру даю апрув, у
нас гораздо больше гибкости с флатеорм. Ребята даже чуть меньше насчитали. в районе 100 часов меньше. Я
бы эти часы оставил все равно и не снижал бы цифру." ([[2025-11-25 Contract chat - rendering 2]]
2026-05-25 13:53). Anton Oparienko, 2026-09-28, in the seed-ingest session: "as I understand now - we go
with flutter for the build", and "for now the aim is flutter from our calls"; he named Arseniy as the
decider the same day.

Not decided here: whether the web app is Flutter too. Arseniy on 25 May: "ребята пересчитали и фронт на
вебе в флатер, там тоже экономия получается, но это как опция" (13:53). The v1 WBS Overview still says
"Central office web application - ReactJS" (Overview row 8), while [[DEC-004 Backend stack]] option 2 has
two Flutter full-stack developers covering the work.

On 1 October (added 2026-10-02): Arseniy's team's variant has the web app in Flutter Web, one Flutter
app's layers serving the desktop and the web ([[2026-10-01 Solution vision diagrams - rendering]]
images 01 and 02) - a variant, not a decision; Mikhail's KB-generated diagram has "ReactJS or Flutter
Web - open" (diagram 3). Windows is the only desktop platform: "Да, Винда была указана как
единственная" (Anton), "Платформы в целом. Если что, мы так и так можем. Но да, Винда." (Arseniy,
[[2026-10-01 Optimum Three Caballeros call - transcript]] 00:06:40, 00:06:44).

## Rationale

Available expertise: "Флаттер тут безопаснее, просто по наличию экспертизы" (00:22:01), and the Flutter
estimate found the stack fits the requirements (2026-05-22 15:33). The aim in May was to lower the bus
factor and make the team easier to staff ("снизить риски и упростить подбор команды", 2026-05-22 13:07).

## Consequences

- Downside: the Flutter team's experience is mostly web on public clouds - "у нас 98% это web-based
  проекты, разворачивающиеся на AWS, Azure, Google Cloud" (Anton Oparienko, 00:17:49) - while this is an
  offline Windows desktop on about 70 rigs that must be updated remotely
  ([[CON-002 Deployment outside public cloud]]).
- Downside: the WBS still carries MAUI text in places - the Overview's stack, "the same NET MAUI both for
  desktop and mobile" (Development Flutter row 75), "ASP.NET or Keylock" (rows 17, 47, 77) - and the
  Flutter roll-up's design hours come from the MAUI tab ([[2026-09-25 v1 WBS - rendering]]).
- New obligation: check what Flutter offers on the Windows desktop for this app. Anton Oparienko checks
  it separately (2026-09-28).
- Hard to reverse once the desktop is built; before that, cheap.
