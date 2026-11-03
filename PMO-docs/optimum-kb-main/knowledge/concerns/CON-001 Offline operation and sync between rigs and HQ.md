---
type: concern
id: CON-001
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: quality
sources:
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2025-10-28 BA draft WBS - rendering]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-10-24 Presale architecture - rendering]]"
  - "[[2025-11-03 Solution proposal - rendering]]"
  - "[[2025-12-30 Answers to the client's questions - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2025-11-05 WBS sent to the client - rendering]]"
  - "[[2026-09-25 v1 WBS - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
  - "[[2026-10-12 Optimum Three Caballeros call - transcript]]"
capabilities:
  - "[[CAP-002 Offline data and sync between rigs and HQ]]"
tags:
  - offline
  - sync
---
# CON-001 Offline operation and sync between rigs and HQ

## What must hold

The desktop works with no internet: a shift is opened, filled and closed, and calculations run
locally. When a connection appears, the data syncs to the central database; while there is none, it
does not ([[2026-09-25 Optimum Eng sync - transcript]] 00:08:12). Nothing recorded offline is lost or
changed by the sync.

The client's words: "Rigs should have local databases with automatic sync when internet is
available." ([[2025-10-29 Client answers to the Q&A register - rendering]] C.7); "Centralized dbase at
the HQ not at each work location. Each work location should have local access to their own data."
(Part 1, 8). The measure the client gave, as their second outcome for the first release: "99.9% data
integrity and efficient synchrony between job sites and HQ server" (A.1). What "99.9% data integrity"
means and how it is measured is not defined.

## Why

About 70 rigs, where connectivity cannot be assumed (00:08:12). The client: "internet connectivity on
rig sites may be unreliable. The application should ideally support offline access and functionality
when there's no internet connection available" (A.2).

## Affected requirements

- [[REQ-001 Record and calculate a shift without internet]]
- [[REQ-002 Managers see engineers' reports in the web app]]
- [[REQ-005 Parameter thresholds and entry alerts]]
- [[REQ-012 Documents uploaded at HQ available at the rig]]

## Treatment

Not decided. Which sync patterns, and whether sync is one-way or two-way, is to be fixed in a
whiteboard session between Alexey and Arseniy ("через какие паттерны идет синхронизация. Она
односторонняя, она двухсторонняя", 00:05:03). Depends on [[QUE-002 Do managers send anything back to the rigs]].

Since 2026-09-28 (batch 1 of the seed ingest): data does go from HQ to the rigs - thresholds set in the
web admin are checked on the desktop, and documents uploaded at HQ must be readable at the rig - so sync
is two-way in at least those cases (QUE-002's answer). The BA draft planned a screen to monitor sync
("last sync date, current status, sync errors and data conflicts log",
[[2025-10-28 BA draft WBS - rendering]] row 7) and marked the offline store and the sync module as
"Architecture Solution" (rows 21, 22); the v1 WBS ([[2026-09-25 v1 WBS - rendering]]) has no line for sync. The SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) puts project and measurement sync in Milestone 3 and each later module's sync in its own milestone.

Added 2026-09-28 (batch 2):

- The client on the first call: "all the drilling rigs, 1 to 50 whatever data they're generating and
  all that while they have local access to those data and do things with those data, we want the 50
  rigs data to be regularly centrally stored" ([[2025-10-22 First call with OES - transcript]] 0:28:04).
- The presale design: an "Aggregation service ... It manages the synchronization logic, ensuring data
  is received reliably, validated, and inserted/updated correctly into the central database"
  ([[2025-10-24 Presale architecture - rendering]]).
- The presale proposal named the risk: "Designing and building a truly robust, bi-directional
  synchronization and conflict-resolution engine that guarantees 99.9% data integrity over highly
  unreliable networks is the primary technical challenge"; an internal comment on the 99.9%: "The
  question is how we define / promise this 99.9% of integrity or accuracy."
  ([[2025-11-03 Solution proposal - rendering]])
- What the client was told in December 2025: web reports are "based on the last synchronized data. The
  data will only be updated once the connection is restored"
  ([[2025-12-30 Answers to the client's questions - rendering]], Page 2); Tsitou's internal comment: "и
  наоборот" (and the other way round).
- Calculations stay on the desktop so they work offline:
  [[DEC-006 Calculations run in the desktop app, formulas fixed in the code]].

Checked against both WBS versions (added 2026-09-28, batch 4): neither has a development line for sync.
The v1 WBS puts architecture at zero, "accounted in discovery"
([[2026-09-25 v1 WBS - rendering]], Total Estimation Development Flutter row 27). The WBS sent to the
client had sync only in monitoring: "Configuring specific alarms for performance, resource utilization,
and crucially, Site Synchronization Lag (70+ unique alarms)"
([[2025-11-05 WBS sent to the client - rendering]], DevOps row 17).

From the presale chat (added 2026-09-28, batch 5):

- What the client was told on 24 November 2025, when they asked for reports and dashboards on the
  desktop: "the main question here is if you want it to be availavle without internet connection.
  Features like reporting and dashboards heavily rely on server-side resources and data" (draft reply,
  [[2025-10-20 Presale chat - rendering 2]] 2025-11-24 12:44).
- The fresh review of the estimate in May 2026 lists, among what the estimate "вероятно, не учтены либо
  существенно недооценены": "разработка механизма синхронизации локальных данных с удаленным сервером"
  and "обработка конфликтов синхронизации и поддержка offline-first сценариев" (2026-05-15 13:46).

From the call of 1 October (added 2026-10-02; [[2026-10-01 Optimum Three Caballeros call - transcript]]): the patterns the
session above was to settle, discussed by Alexey and Arseniy. Not decided.

- Rig to HQ: "в Desktop, скорее всего, у нас будет какая-то внутренняя, как отдельный сервис, очередь,
  которая будет скапливать данных, которые нужно дать на API" (Arseniy, 00:18:02); a table with sync
  metadata, "какие рекорды синхронизировались, какие не синхронизировались, когда они
  синхронизировались" (Alexey, 00:19:55), a transactional outbox (00:28:03).
- HQ to rig: the web service "вообще не знает о существовании отдельных дестопов"; each desktop pulls
  when connected, "как Kafka работает", acknowledges, and the server sees which instance took the data
  (Alexey, 00:19:55); a job tries the server by heartbeat or circuit breaker (00:28:03). Arseniy:
  "Реал-тайм какой-то нам не нужен" (00:19:01); "мы можем и видеть конкретный десктоп, оттуда идёт ли
  он, засинкан ли он там" (00:21:40).
- What flows: "С веба мы тянем на десктоп какие-то новые данные, по формулам, коэффициенты, если они
  хотят задавать ... А на веб отдаем отчеты, всю там мета-данные интересующие" (Arseniy, 00:19:01).
- How hard: "Это типовые задачи" (Arseniy, 00:21:40); "Их просто надо под присмотром грамотного
  инженера сделать" (Alexey, 00:22:01).
- Consistency: "здесь нельзя рассчитывать на 100% консистенции среди всех десктопов ... Но можно это
  минимализировать как-то" (Arseniy, 00:11:38).
- Still to come: "в деталях именно синхронизации я чуть позже отвечу, мы сейчас рисуем архитектуры"
  (Arseniy, 00:18:02).
- A new open point, never raised with the client: a rig with no internet at all, "надо будет как-то
  организовывать передачу данных с десктоп-приложения на сервер тоже флешками, глубиной почты, как-то
  так" (Mikhail, 00:07:34).

Without a queue for now (added 2026-10-13; [[2026-10-12 Optimum Three Caballeros call - transcript]]): the Redis queue the mobile team drew to absorb
bursts when rigs come back online is taken out after Alexey's objection; desktops write straight to the
API ([[DEC-004 Backend stack]]). Arseniy: Redis was there for the case when "интернет появился, и резко
вот это устройство или несколько устройств там со всех сайтов, они как бы пачки, батчи просто запросов
начинают фигачить на API" (00:00:56); "Если синхронно альпишку долбить, ничего не случится" (00:08:14).
Mikhail: the data "будут прилетать не в то время, когда с других вышек. Сам-то сервер у нас будет
всегда в интернете." (00:04:01). If load grows, a load balancer and horizontal scaling (Arseniy,
00:08:48). Anton proposed a test with about 30 rigs sending at once (00:06:58); Mikhail: "нам этим надо
будет заниматься, если делать нечего будет" (00:07:23). Volumes: [[CON-004 Scale and data volume]].
