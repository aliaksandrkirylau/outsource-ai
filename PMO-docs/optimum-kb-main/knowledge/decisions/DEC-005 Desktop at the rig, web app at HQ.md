---
type: decision
id: DEC-005
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: architecture
sources:
  - "[[2025-11-25 Project description - rendering]]"
  - "[[2025-10-22 First call with OES - notes]]"
  - "[[2025-10-29 Client answers to the Q&A register - rendering]]"
  - "[[2026-09-25 Optimum Eng sync - transcript]]"
  - "[[2025-10-22 First call with OES - transcript]]"
  - "[[2025-10-24 Presale architecture - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2025-10-20 Presale chat - rendering 1]]"
  - "[[2025-10-20 Presale chat - rendering 2]]"
capabilities:
  - "[[CAP-001 Identity, roles and access]]"
  - "[[CAP-002 Offline data and sync between rigs and HQ]]"
  - "[[CAP-011 Platform, environments and handover]]"
tags:
  - platform
  - desktop
  - web
---
# DEC-005 Desktop at the rig, web app at HQ

## Context

Engineers work on about 70 rigs where the connection is unreliable, on a computer that belongs to the
rig, not to a person ([[2025-10-22 First call with OES - notes]] key points 4 and 8). Managers and
supervisors work at HQ across many rigs. The client asked Innowise for advice: "Clients is asking on
our opinion - desktop or web - pros and cons based on the collected requirements" (key point 4).
Treats [[CON-001 Offline operation and sync between rigs and HQ]].

The desktop is the client's requirement (added 2026-09-28, batch 2): "It needs to be a desktop
application. That is first and foremost" ([[2025-10-22 First call with OES - transcript]] 1:02:23). The
presale architecture took it as an NFR: "A desktop application (Windows OS) is required for the field
engineer on the job site" ([[2025-10-24 Presale architecture - rendering]]).

Where the web app came from, and the client's answer to the proposal (added 2026-09-28, batch 5). The
client did not ask for a web app; it followed from the manager role: "на звонке он говорил про десктоп и
мобилку, нигде не просил веб ... роли Manager нужно видеть данные с нескольких подконтрольных локаций; с
учетом того, что он четко проговаривал, что у десктопа (Engineer) будет доступ только к данным своей
локации, вот отсюда может выплывать веб именно для менеджмент-юзеров" (Kira Barshchevich,
[[2025-10-20 Presale chat - rendering 1]] 2025-11-03 16:09). The proposal kept calculations, reporting,
dashboards and inventory off the desktop, and the client answered: "We noticed that calculations &
modeling, reporting, dashboard, and inventory management are not included in the desktop application
under project scope. These items remain essential requirements for the desktop application."
([[2025-10-20 Presale chat - rendering 2]] 2025-11-24 12:10). Our draft reply: "The initial decision to
limit the desktop application's scope was a key factor in aligning with the project's budget ...
Features like reporting and dashboards heavily rely on server-side resources and data ... we can fully
duplicate functionalities from web to desktop app" (12:44). The WBS was then re-estimated "исходя из фул
скоупа десктопного приложения и отсутствия мобильного" (15:35).

## Options considered

1. One web application for everyone. We asked whether anything ruled it out; the client: "There are
   no strict limitations requiring the use of desktop or mobile applications. However, we need to
   consider that internet connectivity on rig sites may be unreliable"
   ([[2025-10-29 Client answers to the Q&A register - rendering]] A.2). Lost on offline work at the rig,
   and on the client's own requirement. On the first call Marina Zaretskaya leaned this way: "For
   scalability? I probably would recommend web application" (transcript 1:04:02).
2. A desktop app plus a mobile app, the client's first ask: "preferably desktop (OS windows)", with a
   "mobile app future that will be in demand within supervisors" (notes, key point 4). The mobile part
   was dropped later; see [[REQ-013 Mobile app]].
3. A native Windows desktop app at the rig and a web app at HQ. Chosen in presale
   ([[2025-11-25 Project description - rendering]]).

## Decision

Two components: "a native Windows desktop application used on-site to enter measured data, manage
inventory, perform calculations and modeling, and generate reports; and a web application used to
monitor project statuses across multiple rigs, manage users, oversee inventory, work with reports, and
track key metrics through dashboards" ([[2025-11-25 Project description - rendering]]).

Who decided, and when, is not in these sources, so no deciders are named. On 25 Sep Anton Oparienko
asked whether the desktop was the client leadership's requirement; Arseniy Klimenko answered "Да"
and then "Честно, я не знаю истины, я могу только предполагать"
([[2026-09-25 Optimum Eng sync - transcript]] 00:11:29, 00:12:12, 00:12:21). The SOW v10.4 ([[2026-06-15 SOW v10.4 - rendering]]) has the same two components.

## Rationale

"It gives rig engineers the reliable, high-performance offline tool they need, while simultaneously
giving managers the centralized data and reporting they require"
([[2025-11-25 Project description - rendering]]).

## Consequences

- Downside: two clients to build and test, and a desktop to install and update on about 70 rig
  computers that are often offline ([[CON-002 Deployment outside public cloud]]).
- Downside: no mobile app, which the client asked for ([[REQ-013 Mobile app]]).
- New obligation: sync between the desktop and HQ in both directions
  ([[CON-001 Offline operation and sync between rigs and HQ]]).
- Open: whether engineers want the desktop or a tablet ([[QUE-001 Why a desktop at the rig, and tablets later]]).
- Hard to reverse once the desktop UI is built: a tablet UI is designed differently (Mikhail
  Andrushkevich, 25 Sep, 00:14:04).
