---
type: decision
id: DEC-004
status: proposed
origin: extracted
author: claude-code/claude-opus-5-5
kind: architecture
deciders:
  - human:arseniy.klimenko
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-11-25 Project description - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 1]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
  - "[[2025-11-25 Economy chat - overview]]"
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
  - "[[2026-10-01 Solution vision diagrams - rendering]]"
  - "[[2026-10-01 Solution vision diagrams - overview]]"
  - "[[2026-10-12 Optimum Three Caballeros call - transcript]]"
capabilities:
  - "[[CAP-011 Platform, environments and handover]]"
tags:
  - stack
  - staffing
---
# DEC-004 Backend stack

## Context

The desktop client is Flutter ([[2026-09-25 Optimum Eng sync - transcript]] 00:12:21;
[[DEC-007 Flutter for the desktop app]]). The backend is
open, and the staffing positions depend on it (00:30:57). Treats [[CON-002 Deployment outside public cloud]].

History: in presale the stack was "TBC after the discovery stage": "Backend service - .NET or Java",
"Local client application - MAUI", "Central office web application - ReactJS", "Identity provider -
ASP.NET Identity or Keylock", SQLite on site and PostgreSQL centrally
([[2025-11-25 Project description - rendering]]). The two options below came later. The platform
split itself is [[DEC-005 Desktop at the rig, web app at HQ]].

The v1 WBS ([[2026-09-25 v1 WBS - rendering]]), added 2026-09-28, batch 4. Its Overview still names
the presale stack - "Backend service - .NET or Java", "Local client application - MAUI", "Central
office web application - ReactJS" - and a team of 2 front-end and 2 back-end developers (Overview rows
8, 10 and 11). Its Flutter roll-up names no backend and splits development into four lines: web and desktop,
back end and front end (Total Estimation Development Flutter rows 11 to 14). Arseniy describes the
original estimate's backend differently: "у нас изначальная оценка без супербейса это какой-то там нода
питон, что в принципе не суть дела" ([[2026-09-25 Optimum Eng sync - transcript]] 00:16:40). The two
disagree on the original backend; the choice below is open either way. How the estimate was made:
for MAUI, "уже больше года назад", in "40 минут", and "все цифры, когда были даны тогда, они актуальны"
(00:22:01).

The estimate's dates, from the presale chat (added 2026-09-28, batch 5):

- 5 November 2025: the MAUI desktop and mobile front end was estimated the morning the proposal was
  presented. Arseniy asked "Сколько у нас времени?", Marina Zaretskaya answered "минут 40", and Vitaly
  Ponteley posted "Десктоп и мобилка готовы" about an hour later
  ([[2025-10-20 Presale chat - rendering 1]] 2025-11-05 08:12, 08:21, 09:27). This is the "40 минут" of
  the 25 September sync, about ten months before it rather than over a year.
- 25 November 2025: re-estimated in the v1 sheet for the full desktop, with no mobile
  ([[2025-10-20 Presale chat - rendering 2]] 2025-11-25).
- 22 May 2026: the Flutter estimate, "оценка готова по стеку все релевантно, проблем с реализацией под
  требования не будет" (Sergei Gubkin, 2026-05-22 15:33); Arseniy: "актуальная оценка из чата с
  флатером" (2026-05-25 14:14). That chat is not stored.
- 15 May 2026, before the Flutter move: "В скоупе есть React, .NET и MAUI" (Arseniy, in the economy chat;
  [[2025-11-25 Economy chat - overview]], added 2026-09-28, batch 6). So the back end then counted was
  .NET, a third reading beside the Overview's ".NET or Java" and Arseniy's "нода питон" of 25 September.

One back end for web and desktop, as the presale back-end estimator put it: "back end не разделяется на
десктоп и веб, технически на деле это будет одно решение, которое будет использовать и front end на
web'е и front end на desktop'е, там функционал общий" (Artsiom Bulakh, 2025-11-25 13:24).

## Options considered

1. Flutter with a classic backend (Node or Python), as in the original estimate: 4 developers, each
   part-time because the technologies and pieces of work differ (Arseniy, 00:16:40).
2. Flutter with self-hosted Supabase: 2 full-stack developers full-time for the same timeline; the
   Flutter lead says it is realistic and takes responsibility (Arseniy, 00:16:40). Arseniy worked
   on an energy-company project that adopted it (the transcript reads "UPB", from context Supabase)
   and does not see platform maturity as a risk (00:18:22).

Against option 2 as a cloud service: Anton believes Supabase's cloud is not deployed in the Arab
region ("по-моему", 00:16:27, unverified); the self-hosted variant can run anywhere (00:16:40).

Option 2 drawn (added 2026-10-02, from the 1 October call and the diagrams): Arseniy's team drew the
self-hosted Supabase variant as containers and as the Flutter app's layers - a Kong API Gateway or
Nginx, Supabase Auth (GoTrue), PostgREST and GraphQL, Supabase Storage, Edge Functions (Deno),
PgBouncer, Redis, Realtime, PostgreSQL with row-level security, and a "Redis Queue & Worker Service
(Data Sync Conflict Resolution, Audit Aggregation, Heavy Exports)"
([[2026-10-01 Solution vision diagrams - rendering]] images 01 and 02). Offered as one variant: "Вот
диаграммы от технарей. Как вариант видения солюшена", "Здесь варант с бэком на супабейз" (Arseniy,
[Core], 2026-10-01 12:56 UTC). Option 1 has no diagram. Mikhail's container diagram for the call,
generated by Claude from this KB, marks the back end "open, DEC-004" and is "не финальный source of
truth" ([[2026-10-01 Solution vision diagrams - overview]], diagram 3). Alexey in the call: "Superbase
где-то там звучало, да, это же гугловый как-то сервис, да?"
([[2026-10-01 Optimum Three Caballeros call - transcript]] 00:22:52) - not checked; option 2 is
self-hosted either way.

Redis out for now (added 2026-10-13; [[2026-10-12 Optimum Three Caballeros call - transcript]]): Alexey Gamanovich objected to Redis in the mobile
team's architecture; Arseniy held a session with the mobile team, and "Решили, типа, идти без него" -
direct writes to the API and, if a need appears, "может, не RADIUS, а кавку" (Redis, Kafka; Arseniy,
00:00:56). Alexey's objection as Arseniy relays it: "сингл-поинт фейлер такой. Он плохо скейлится"
(00:00:56). The decision itself stays open; option 2 loses its Redis queue and worker. Sync:
[[CON-001 Offline operation and sync between rigs and HQ]].

## Decision

Open. Arseniy: "У меня две опции. Супербейсинг. Надо подумать. И тогда примем решение" (00:30:57).
Staffing cards are prepared for both options.

Still open on 1 October: the diagrams are a variant, not a decision, and in the call Arseniy said "мы
сейчас рисуем архитектуры, накидываем, вот еще не готово"
([[2026-10-01 Optimum Three Caballeros call - transcript]] 00:18:02).

## Rationale

To be written when decided.

## Consequences

To be written when decided. The choice sets the backend and DevOps positions.

Known already (added 2026-10-02): every component of the chosen stack has to pass contract 8.4 on
copyleft and recurring licence fees ([[COM-013 Source code, IP and third-party components]]).
