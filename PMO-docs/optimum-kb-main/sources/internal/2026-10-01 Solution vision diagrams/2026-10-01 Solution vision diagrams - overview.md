---
type: source
kind: document
date: 2026-10-01
original: https://chat.google.com/room/AAQAkfyHFwA/G7m2a378xfA/G7m2a378xfA
received_from: Arseniy Klimenko in the [Core] Optimum engineering chat (images 01 and 02); Mikhail Andrushkevich in the chat of the 1 October call (diagram 3)
purpose: the team's first solution vision diagrams, read to check whether they record decisions and which version stands (Anton's ask, 2026-10-02)
supersedes:
procedure_version: 5d00575
---
# 2026-10-01 Solution vision diagrams - overview

kind: document (`sources/internal/`). Rendering: [[2026-10-01 Solution vision diagrams - rendering]].
Images 01 and 02 are stored next to it as "2026-10-01 Solution vision diagrams - image 01.png" (390 KB)
and "image 02.png" (259 KB) and embedded in the rendering. Diagram 3 is rendered as text only. Discussed
in the call of the same morning: [[2026-10-01 Optimum Three Caballeros call - minutes]].

## What it is

Three diagrams of the solution, all posted on 2026-10-01:

| # | Diagram | Posted | Where it comes from |
|---|---|---|---|
| 01 | Optium_Engineering_Architecture.png: containers of a self-hosted Supabase back end with Flutter web and desktop clients | Arseniy, [Core], 12:56 UTC | "Вот диаграммы от технарей. Как вариант видения солюшена"; "Здесь варант с бэком на супабейз" |
| 02 | Optium_Engineering_frontend.png: the layers of the Flutter app (presentation, features, domain, data, APIs) | the same message | the same |
| 3 | C4 L2 - Containers: a C4 container diagram | Mikhail, the call's chat, 09:06 UTC, again at 09:51 and in high resolution at 09:54 | "Это не финальный source of truth, а сгенерена Клодом по имеющимся материалам. У Арсения ребята сейчас работают над диаграммами." (09:52) |

Arseniy asked the day before what to prepare - "пару диаграм (контейнеры,контекст) и общее тех видение"
- and Anton answered "для начала точно достаточно ... обсудим с Лешей" ([Core], 2026-09-30 12:38, 14:38).
Who "технари" are is not said; Mikhail calls them "У Арсения ребята". Diagram 3 was built from this
knowledge base: its labels cite DEC-004, REQ-012, the v1 WBS and "the July 2026 chat; decision not
recorded".

How the diagrams compare (our reading, evaluated):

| Point | Images 01-02 (Arseniy) | Diagram 3 (Mikhail, from the KB) |
|---|---|---|
| Web app | Flutter Web | "ReactJS or Flutter Web - open" |
| Desktop app | Flutter Windows, offline-first, local DB "SQLite/Isar", calculations and hydraulics simulation, offline auth, sync engine | Flutter Windows, SQLite with a sync outbox, calculations "formulas fixed in code", offline sign-in |
| Back end | self-hosted Supabase: Kong or Nginx gateway, GoTrue auth, PostgREST and GraphQL, Storage, Edge Functions, PgBouncer, Redis, Realtime; a Redis queue and worker for sync conflict resolution, audit aggregation and heavy exports | a Central API Service and a Sync / Aggregation Service, "backend - open, DEC-004" |
| Identity | Supabase Auth (GoTrue) | "Keycloak / ASP.NET Identity / Supabase Auth - open" |
| Database | PostgreSQL with row-level security | PostgreSQL with materialized views |
| Documents and reports | Supabase Storage, "S3-Compatible for Reports" | object storage for HQ documents (REQ-012, a CR candidate) |
| Hosting | not drawn | "GCP Dammam (KSA) per the July 2026 chat; decision not recorded" |
| Desktop updates | not drawn | a "Desktop update channel", "No line in the v1 WBS" |
| Operations | SMTP, Sentry, Prometheus, Grafana, S3 backups | not drawn |

They agree on Flutter Windows at the rig, offline work, calculations on the desktop and PostgreSQL
centrally. Images 01 and 02 fill in [[DEC-004 Backend stack]] option 2 (self-hosted Supabase) and put the
web app on Flutter, which [[DEC-007 Flutter for the desktop app]] leaves open. Diagram 3 restates what
the KB already held and marks the same points open.

Who drew 01 and 02 (added 2026-10-13): most likely the mobile department's people, possibly Sergei
Gubkin, whom Arseniy planned on 30 September to ask to draw them
([[2026-09-30 Optimum Three Caballeros call - minutes]]). Not confirmed.

## How far to trust it

Vision, not decisions. Arseniy offers images 01 and 02 "Как вариант видения солюшена" and as "вариант с
бэком на супабейз", so other variants are expected; in the call he said "мы сейчас рисуем архитектуры,
накидываем, вот еще не готово" ([[2026-10-01 Optimum Three Caballeros call - transcript]] 00:18:02).
Diagram 3 is, by Mikhail's own words, "не финальный source of truth", and he points to Arseniy's team
for the diagrams. So images 01 and 02 are the ones to follow, as a proposal: Arseniy is the named
decider of DEC-004 and DEC-007, and neither is decided. The reactions on the Supabase message (one ✅,
one 👀, by people the chat does not show) are not acceptance.

## Not for

A decided architecture, a stack the client has agreed, the hosting choice, or a design to code from.

## Removed at ingest

Nothing from the diagrams. The two stored images were looked at by claude-code/claude-opus-5-5 for
Anton Oparienko before they were stored: no money, personal data or credentials (the money screen
cannot read an image).

Not stored:

- Diagram 3's image. It is derived from this KB, and its readable version, "C4 L2 - Containers
  (high-res).png", is 1,079,152 bytes, over the 1 MB limit; it stays in the chat
  (https://chat.google.com/room/AAQAlS0lPMM/XI-K8PdnyuA/XI-K8PdnyuA). The 09:06 and 09:51 versions
  (188,883 bytes each, "размыто" for Alexey) and Anton's Gemini upscale of 09:53
  (Gemini_Generated_Image_5zgj305zgj305zgj.jpg) are scaled copies, listed here and not rendered.
- From the call's chat (spaces/AAQAlS0lPMM, 9 messages): the Gemini recap of 09:37 UTC, a bot message.
  The other 8 are in the rendering.
- From [Core]: only the four messages about the diagrams are quoted. The chat is not stored as a
  source; its other messages since 2026-09-28 are not ingested here.

## Summary

Arseniy's team drew the self-hosted Supabase option of the backend in two diagrams, the containers
and the Flutter app's layers, and offered them as one variant of the solution vision. Mikhail's
container diagram, generated by Claude from the KB for the call, is not a source of truth and adds
nothing new. Nothing in either is decided.

## Proposed changes

In the call's table: [[2026-10-01 Optimum Three Caballeros call - minutes]], rows 1 and 2 (key D).
