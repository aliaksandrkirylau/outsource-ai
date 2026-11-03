---
type: source
kind: rendering
date: 2026-10-01
original: https://chat.google.com/room/AAQAkfyHFwA/G7m2a378xfA/G7m2a378xfA
removed:
  - nothing from the diagrams; the images carry no money, personal data or credentials
  - not rendered - the Gemini recap in the call's chat (a bot message), and the scaled copies of diagram 3 (see the overview)
---
# 2026-10-01 Solution vision diagrams - rendering

Three diagrams posted on 2026-10-01, with the chat messages that asked for them and carried them. Text
as the diagrams have it, box by box, then the arrows. Arrow ends are read from the picture; where
lines cross, an end may be off. Times are UTC. Our notes are in square brackets.

## The messages

[Core] Optimum engineering (spaces/AAQAkfyHFwA), the messages about the diagrams only:

- 2026-09-30 12:38 **Arseniy Klimenko**: Хочу к завтра подготовить наше тех видение. Что вообще думаете
  будет полезно увидеть, пару диаграм (контейнеры,контекст) и общее тех видение достаточно?
  (https://chat.google.com/room/AAQAkfyHFwA/3klEsB2mdks/3klEsB2mdks)
- 2026-09-30 14:38 **Anton Oparienko** (↳ 12:38): @Arseniy Klimenko Думаю для начала точно достаточно,
  давай с чего-то начнем и от этого будем плясать дальше и обсудим с Лешей. И жду еще твой юзернейм
  [reactions: 🤝x1]
- 2026-10-01 12:56 **Arseniy Klimenko**: Вот диаграммы от технарей. Как вариант видения солюшена
  [attachment: Optium_Engineering_Architecture.png, image 01 below] [attachment:
  Optium_Engineering_frontend.png, image 02 below]
  (https://chat.google.com/room/AAQAkfyHFwA/G7m2a378xfA/G7m2a378xfA)
- 2026-10-01 12:56 **Arseniy Klimenko**: Здесь варант с бэком на супабейз [reactions: ✅x1, 👀x1]
  (https://chat.google.com/room/AAQAkfyHFwA/zzJulnkulW4/zzJulnkulW4)

The call's own chat, "Optimum E.: Three Caballeros call - 1 Oct" (spaces/AAQAlS0lPMM), every message
but the Gemini recap (see the overview):

- 2026-10-01 09:01 **Anton Oparienko**: @Arseniy Klimenko зайдешь?
- 2026-10-01 09:06 **Mikhail Andrushkevich**: [attachment: C4 L2 - Containers.png, diagram 3 below]
  (https://chat.google.com/room/AAQAlS0lPMM/z2Xax9wd4f8/z2Xax9wd4f8)
- 2026-10-01 09:48 **Alexey Gamanovich**: @Mikhail Andrushkevich , перезакинь пож картинку в хорошем
  качестве. Когда открываешь там все размыто
- 2026-10-01 09:50 **Anton Oparienko**: у меня вроде норм открывается 🤔
- 2026-10-01 09:51 **Mikhail Andrushkevich**: У меня тоже, но на всякий случай вот. [attachment: C4 L2 -
  Containers.png]
- 2026-10-01 09:52 **Mikhail Andrushkevich**: Это не финальный source of truth, а сгенерена Клодом по
  имеющимся материалам. У Арсения ребята сейчас работают над диаграммами.
  (https://chat.google.com/room/AAQAlS0lPMM/Bzn-gcw79CU/Bzn-gcw79CU)
- 2026-10-01 09:53 **Anton Oparienko**: апскейл от джеминайки можешь еще попробовать) [attachment:
  Gemini_Generated_Image_5zgj305zgj305zgj.jpg]
- 2026-10-01 09:54 **Mikhail Andrushkevich**: Сгенерил в более высоком разрешении [attachment: C4 L2 -
  Containers (high-res).png] (https://chat.google.com/room/AAQAlS0lPMM/XI-K8PdnyuA/XI-K8PdnyuA)
- 2026-10-01 09:54 **Anton Oparienko**: засыпали картинками)

## Image 01 - Optium_Engineering_Architecture.png (Arseniy, from the tech team)

![[2026-10-01 Solution vision diagrams - image 01.png]]

Layer "CLIENT LAYER (Flutter)":

- «Client» Web Application (Flutter Web) [Managers, Supervisors, Admins] -- Dashboard & KPIs; Project &
  Inventory Mgmt; Reporting (PDF/CSV/XLSX); Admin Panel & Audit Logs
- «Client» Desktop Application (Flutter Windows) [Mud Engineers] <<Offline-First>> -- Local DB
  (SQLite/Isar) & Cache; Offline Auth & Input Validation; Calculations & Hydraulics Simulation;
  Offline-to-Online Sync Engine

Layer "ASYNC PROCESSING & QUEUES":

- «Async» Redis Queue & Worker Service (Data Sync Conflict Resolution, Audit Aggregation, Heavy Exports)

Layer "GATEWAY & SECURITY LAYER":

- «Gateway» Kong API Gateway / Nginx (SSL/TLS, Rate Limiting, WAF, CORS, Routing)

Layer "SELF-HOSTED SUPABASE INFRASTRUCTURE":

- «Supabase» Supabase Auth (GoTrue) (Identity Provider, JWT, Roles)
- «Supabase» PostgREST & GraphQL (Auto-generated API)
- «Supabase» Supabase Storage (S3-Compatible for Reports)
- «Supabase» Edge Functions (Deno) (Audit Triggers, Custom Alerts)
- «Supabase» Infrastructure Services -- PgBouncer (Connection Pooling); Redis (Cache, Rate Limits);
  Realtime (Websockets)
- PostgreSQL Database (RLS), holding: Users / Roles; Projects; Measurements; Inventory & Thresholds;
  Audit Logs

Layer "EXTERNAL INTEGRATIONS & ENVIRONMENT":

- «External» SMTP / Email Provider (Auth Emails, System Alerts)
- «External» [box title hidden under the arrow label "Scheduled Dumps"] (Sentry, Prometheus, Grafana)
  *Crucial for Self-Hosted*
- «External» Backup Storage (S3 DB/Storage Backups)

Arrows:

- Web Application to the gateway: "HTTPS / WSS"
- Desktop Application to the gateway: "HTTPS (Sync/Online Ops)"
- The gateway to Supabase Auth, to PostgREST & GraphQL, to Supabase Storage and to Edge Functions:
  "REST" each
- Supabase Auth, PostgREST & GraphQL and Supabase Storage to the database; Edge Functions to the
  database: "Manage / Sync"
- Redis Queue & Worker Service to the database: "Reads/Writes"; to the SMTP provider: "Triggers Alerts"
- Supabase Auth to the SMTP provider: "Sends Emails"
- Infrastructure Services to the Sentry, Prometheus, Grafana box: "Telemetry"
- The database to Backup Storage: "Scheduled Dumps"

No hosting provider and no desktop update route are drawn.

## Image 02 - Optium_Engineering_frontend.png (Arseniy, from the tech team)

![[2026-10-01 Solution vision diagrams - image 02.png]]

Left to right:

- USER to DESKTOP APP; ADMIN to WEB APP. DESKTOP APP and WEB APP to PRESENTATION (UI, Presenter).
- UI KIT (Themes, Colors, Fonts, Base UI components) to PRESENTATION.
- FEATURES, each linked both ways to PRESENTATION and to DI: Authorization / Authentication; User
  Management; Project Management; Calculations & Modeling; "...".
- DOMAIN: Services (SyncDomainService, CalculationService, SimulationService, AlertingService);
  Repositories (AuthRepository, UserRepository, ProjectRepository, ...); AccessController; UseCases. DI
  to UseCases; UseCases to AccessController.
- DATA: DI; Repositories (AuthRepository, UserRepository, ProjectRepository ...); Services
  (SyncDomainService, AlertingService); DATA LAYER COMMUNICATION; SYNC MANAGER; Providers (API
  Provider, Local DB Provider, Identity Provider Client, Network/Connectivity Provider).
- API's: API (SUPABASE Identity Service API), dashed to SYNC MANAGER; LOCAL DATA BASE (LOCAL DATABASE),
  to Providers.
- Along the bottom: MODELS - MAPPERS - ENTITIES - MAPPERS - API Models; APP EXCEPTION - ERRORS HANDLERS -
  ERROR SERVICE.

## Diagram 3 - C4 L2 - Containers (Mikhail, generated by Claude)

Not stored as an image (see the overview). Rendered from "C4 L2 - Containers (high-res).png", the
09:54 version.

People:

- Mud engineer [Person] - "Uses" - Rig Desktop App
- Supervisor / Management / Admin [Persons, HQ] - "Uses [HTTPS]" - HQ Web App

Boundary "Rig PC - Windows, shared, often offline (x ~70, up to 100)":

- Rig Desktop App [Container: Flutter, Windows] Shift data entry, threshold alerts, calculations and
  hydraulics simulation (formulas fixed in code), inventory, reports (PDF / CSV / Excel). Offline
  sign-in with cached credentials.
- Local database [Container: SQLite] This rig's data, the sync outbox, cached users, thresholds,
  low-stock levels, documents.

Boundary "Central hosting - GCP Dammam (KSA) per the July 2026 chat; decision not recorded":

- HQ Web App [Container: ReactJS or Flutter Web - open] Dashboards and KPIs, reports across rigs, well
  jobs, users and roles, thresholds, inventory oversight, document upload.
- Central API Service [Container: backend - open, DEC-004] Business logic for the web app: reports,
  rule-based alarms, dashboards and analytics, administration.
- Desktop update channel [Container: installer + update feed - open] Gets new builds to ~70 mostly
  offline rig PCs. No line in the v1 WBS. [dashed]
- Sync / Aggregation Service [Container: backend - open, DEC-004] Receives rig data, validates,
  resolves conflicts, writes to the central DB; sends HQ-set data back to the rigs.
- Identity Service [Container: Keycloak / ASP.NET Identity / Supabase Auth - open] Sign-in, tokens, RBAC
  for web and desktop.
- Central database [Container: PostgreSQL] All rigs' data; materialized views for reporting.
- Document storage [Container: object storage - open] Documents uploaded at HQ for the rigs (REQ-012,
  CR candidate). [dashed]

Arrows:

- Rig Desktop App to Local database: "Reads / writes"
- Rig Desktop App to Sync / Aggregation Service: "Pushes rig data, pulls HQ-set data when a connection
  exists [HTTPS]"
- Rig Desktop App to Desktop update channel: "Checks for and downloads new versions [HTTPS]" [dotted]
- Rig Desktop App to Identity Service: "Signs in online; caches credentials for offline [HTTPS]"
- HQ Web App to Central API Service: "Calls [HTTPS / JSON]"; to Identity Service: "Signs users in [OIDC]"
- Central API Service and Sync / Aggregation Service to Identity Service: "Validates tokens" each
- Central API Service and Sync / Aggregation Service to Central database: "Reads / writes [SQL]" each
- To Document storage: "Stores documents" and "Serves documents to rigs" [dotted]
