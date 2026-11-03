---
type: commitment
id: COM-020
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
party: us
due: six sequential milestones of 1 Month each
clause: "SOW v10.4, Project implementation phases and Project Phases"
sources:
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-28 Optimum discuss next steps - transcript]]"
  - "[[2026-10-14 Project email thread - rendering 1]]"
  - "[[2025-11-25 Contract chat - rendering 5]]"
  - "[[2026-10-13 OE Big4 chat - rendering 1]]"
tags:
  - milestones
  - discovery
---
# COM-020 Milestone plan and deliverables

## What is owed

The SOW v10.4's plan ([[2026-06-15 SOW v10.4 - rendering]] rows 9, 11, 16). Binding as far as the SOW
v10.4 is the contract's Annex 1: Anton Oparienko confirmed on 2026-09-28 that it is the latest SOW the
parties work with, per the contract chat ([[QUE-006 Which SOW and which plan are Annex 1 and Annex 2]]).

"The Project is executed in two main phases: Discovery Phase followed by Development Phase. For
delivery and project management purposes, these two phases are further divided into six (6) sequential
Milestones." (row 9)

| Milestone | Scope, as the SOW states it |
|---|---|
| 1 | "discovery activities (analysis, requirements clarification and specification, scope definition, risks evaluation, architecture design, UI/UX design)". Deliverables: V&S Document (vision and goals, scope in and out, assumptions and constraints, key risks, success criteria, high-level requirements, a validated backlog with user stories and high-level acceptance criteria); Solution Architecture Design (system overview, components, integrations, data flow, technology stack); UI Kit; "Main UI/UX mockups mandatory and enough to start the project implementation"; Communication plan; Revised WBS; Project plan (timeline, milestones, phases, dependencies, delivery schedule) |
| 2 | "Basic project setup, implementation of Authorization/Authentication feature, User creation feature, Users List View and quality assurance" |
| 3 | "requirements documentation development, implementation of users management, project management, and quality assurance" (with desktop project and measurement input and sync) |
| 4 | "implementation of inventory management, admin panel (parameter threshold definition) and quality assurance" (with desktop inventory and alerts) |
| 5 | "implementation of calculation feature, dashboard (web app), and quality assurance" (derived values, calculator, hydraulics simulation) |
| 6 | "implementation of dashboard (desktop app), reporting, audit logs, quality assurance and final stabilisation", then "Final Handover": "The stabilized final software solution, delivered through the agreed source-code handover (publication in the Customer's source-code system) and build deployment to the Customer's servers." |

Each milestone after the first has its own documentation, clarification, feature and QA deliverables in
the SOW.

The team's reading, not the contract (added 2026-09-28, the call of that day;
[[2026-09-28 Optimum discuss next steps - transcript]]): Anton asked whether the monthly milestones are
agreed at the start of each month or fixed (00:26:55). Mikhail: "В контракте прописан скоп на каждый
milestone, он довольно краткий, но high-level он есть" (00:27:37). Arseniy: "там расписывалось, какие
блоки входят в сови. Но под вопросом, насколько строго этому следовать ... я думаю, наверное, он открыт
будет, если мы предложим свой вид распределения по мейлстоунам" (00:27:48). Mikhail on Milestone 1:
"первый он там описывает чистый discovery" (00:28:25). A proposal to move scope between milestones:
[[DEC-011 Move scope between milestones and start building in the first month]].

Told to the client (added 2026-10-14): "as agreed between our teams, the Project begins with the
Discovery Phase (Milestone 1)", and the discovery plan will cover "the Milestone 1 deliverables (Vision
& Scope document, solution architecture design, UI kit and main mockups, revised WBS and project plan)"
([[2026-10-14 Project email thread - rendering 1]]). Our reading: that list leaves out the communication plan, which the SOW names among Milestone
1's deliverables. Internally, the record of 13 October: "По SOW мы уже взяли на себя обязательства по
результатам Discovery в большем объёме, чем запланировали внутри. Подход к их выполнению определяют PM и
DM." ([[2025-11-25 Contract chat - rendering 5]] 2026-10-13 09:55); Mikhail's minimum for the month: "акцептанс на деливераблс для следующей
фазы (1 месяц)" ([[2026-10-13 OE Big4 chat - rendering 1]] 2026-10-13 09:18);
[[DEC-015 Discovery - our own picture of the system, questions as if from scratch]].

## By when

"1 Month" each. Start: "agreed upon by the Parties via email" (row 11);
[[QUE-007 What is the Effective Date]].

## How it is accepted

Per milestone, in writing ([[COM-002 Written acceptance of each deliverable]]); payment:
[[COM-012 Payment schedule]].

## Drives

- The Requirements, by milestone; [[COM-001 Delivery within six months]].
