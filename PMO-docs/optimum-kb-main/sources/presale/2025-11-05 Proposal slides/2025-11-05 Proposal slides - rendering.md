---
type: source
kind: rendering
date: 2025-11-05
original: https://docs.google.com/presentation/d/10-oqb8y1x7Eq-4Ami6uAZCGwxC5gJuXlbdg-M2T9ges
removed:
  - the discount amount and the advance payment amount (slide 28)
  - the monthly support budget (slide 32)
  - the timeline and budget slides (21, 22, 25, 26, 29, 30) and the estimate slides (34 to 38) - images in the original, and the budget ones carry prices
  - the account manager's e-mail address (slide 40)
---

# 2025-11-05 Proposal slides - rendering

Google Slides "Proposal from Innowise - Optimum Engineering Standards", 40 slides, owned by Aliaksei
Tsitou, created 2025-11-05, last changed 2026-05-15. The client-facing proposal, with three
iterations in one deck. The text of each slide, verbatim; slides that are pictures are described, not
rendered. Slides 1 to 9 and 39 are Innowise's company presentation and are listed by title only.
Never edited after storing.

## Company slides (1-9)

1 cover; 2 countries, entities, key facts; 3 "Сertified provider and acknowledged leader"; 4 "Reliable
tech partner"; 5 and 6 "We've built software for"; 7 "Resource Map"; 8 "Tech domains we cover"; 9
"Services".

## Slide 10 - Proposal overview

## Slide 11 - Overview

We are developing a custom, scalable software solution to replace its current Excel-based and manual
data management processes for drilling fluid operations.

The system must serve as a centralized, in-house application for ~70 rig sites, many of which have
poor or non-existent internet connectivity.

The solution must provide full offline functionality for engineers, ensuring data integrity upon
synchronization, and deliver robust modules for measurements, inventory , complex engineering
calculations, and fleet-wide reporting.

## Slide 12 - Project Objectives and Success Criteria

The solution aims to address operational disruption and data fragmentation caused by current tools

1. Ensure 99.9% Data Integrity & Availability by implementing a robust offline-first system with
   efficient, automated synchronization
2. Generate Complete and Accurate Reports, including End-of-Day, End-of-Section, End-of-Well, and
   Inventory reports
3. Establish a Scalable & Secure Platform that is centralized and on-premise, supporting up to 100+
   locations and role-based access control (RBAC)

## Slide 13 - Key Functional Requirements

The core functionality spans several modules crucial for field engineers and HQ staff:

- Measurements & Data Quality: Ability to manually input and pre-validate measured fluid parameters
  (less than 50 parameters, approximately 4 times per day). Threshold Violation Alerting must visually
  highlight out-of-range values and require a mandatory comment before saving 'flagged' data. Derived
  values (e.g., density corrections) will be calculated automatically upon saving raw input.
- Calculations & Simulation: Includes a Standard Engineering Calculator module (e.g., calculating
  required chemical bags) and a complex Fluid Hydraulics Simulation/Modeling module.
- Inventory Management: Tracks initial loadout, inflow, daily consumption, cumulative consumption,
  product concentration, material costs, and includes Low Stock Alerting and Expiration Date Alerting
- Reporting: Ability to generate comprehensive End-of-Day, End-of-Section, End-of-Well, and Inventory
  reports, filterable and exportable to PDF, CSV, and XLXS formats. Reports Approval Flow is required
  for End-of-Section and End-of-Well reports.
- Admin Panel: Ability to Manage User Accounts (CRUD) and define Parameter Thresholds. Audit Logging is
  required to track all data entries edit/backfill actions and their approval status

## Slide 14 - Proposed Architecture

We propose a robust Architecture combining native rig-site applications with centralized cloud
control

| Component | Proposed Approach | Comment |
|---|---|---|
| Rig-Site Application | Cross platform App (.NET MAUI) | Designed for 100% offline operation for data entry, calculations, and reporting. |
| Local Database | Embedded Local Database (SQLite) | The core of the offline solution, saving all data locally with no internet required. |
| Central Database | AWS PostgreSQL Database | Deployed at OES HQ, acting as the single source of truth for all sites. |
| Data Synchronization | Cloud Aggregation Service | A dedicated service that reliably handles and validates all incoming data transmissions from remote desktop apps. |
| HQ Management Portal | Central Web Application (ReactJS) | Browser-based access for Supervisors and Managers to view fleet-wide dashboards and QC workflows. |
| Security/IAM | Identity Provider (e.g., ASP.NET Identity or Keylock) | Manages in-app user accounts and RBAC for roles like Mud Engineer, Supervisor, Manager, and Admin. |

(Read from the slide image; the slide also has a diagram.)

## Slide 15 - Team structure and responsibilities

- Developers (5): The developers are responsible for analysis and task implementation of user stories
  and reported issues related to backend, admin panel, mobile application and web app
- QA specialist (1): The QA Specialist is responsible for test documentation creation, running manual
  functional and auto tests, monitoring software quality, and reporting on discovered issues.
- Business Analyst (1): The Business Analyst is responsible for requirements elicitation and
  documentation, product roadmap development.
- Project Manager (1): The Project Manager is the person in overall charge of the planning, budget, and
  execution of the project based on the agreed scope.
- DevOps Engineer (1): The DevOps Engineer is responsible for configuration and environments
  management, as well as the continuous integration/deployment process including automated builds,
  deployment, and test runs.
- UI/UX Designer (1): The UI/UX Designer is responsible for conducting user research, mapping out the
  desired user experience in the form of wireframes, and ensuring that the application meets the user
  needs.

## Slide 16 - Deliverables

- Source code: Original set of instructions behind a software application that allows Client to have
  transparency, full control over the software, and intellectual property rights over the solution.
- Testing documentation: Comprehensive set of documents (such as Test Cases, Test Results) that outline
  the testing processes, procedures, and results associated with a software project.
- Software solution: Working software solution with the features defined by the team
- Software requirements specification: Detailed description of the system's functional and
  non-functional requirements, outlining what the software should do and how it should perform.

## Slide 17 - Communication and escalation procedures

There are three main types of issues that require escalation during the project, listed below. Any one
of them can cause significant delays and unexpected costs if left unresolved:

- Scope issues and delays in work;
- Resource bottlenecks or changes to the team.
- Major decisions or change that needs to be made;

Communication process will be set up within the Communication Plan (will be drafted at the beginning
of the project), which needs to be approved by customer team.

\* Communication plan can be adjusted depending on client's needs.

Supposed frequency of communication – at least 2 times a day. Innowise working time: 9.00-18.00
(GMT+2) client's stakeholders will be invited to demos at the end of each sprint.

On the Innowise side, the Project Manager will be the contact person for all project related issues.
The Account Manager will be responsible for all other issues (contracts, feedback, etc.).

We can schedule biweekly management meetings to align with priorities, scope and changes.

## Slide 18 - Delivery management approach

This responsibility area includes the following items:

- Documentation creation and project tracking (Jira, Confluence).
- Scope and delivery management focuses on creating the release plan, generating the release scope,
  and monitoring the development lifecycle to achieve the planned release timelines.
- Release management activity based on the Agile approach.
- Resource management focuses on organizational planning, resource allocation, and workload
  monitoring.
- Development management focuses on development practices designed to achieve the code quality and
  build stability goals.
- Risk management covers activities related to risk discovery and analysis, as well as risk
  mitigation. The main goal of this activity is to prevent possible project problems such as budget
  overruns and project schedule shift.
- Quality management focuses on quality planning, assurance, and control to constantly monitor the
  quality of project deliverables.

## Slide 19 - Software development collaboration tools

Our software engineering teams use the following software development tools to plan, design, build,
deploy, test, and maintain great software: Video conferencing tools (Google Meet/Slack/MS
Teams/Skype/Zoom/GMail); Design and diagramming (Figma, Diagrams.net); Documentation (Confluence);
CI/CD (UrbanCode Deploy); Testing (BrowserStack, Xray, TestRail); Source code management
(GitHub/GitLab/ Bitbucket); Project management (JIRA).

## Slides 20-22 - Initial Timeline and Budget Proposal

Slide 21 "Timeline": an image, with the note "Timeline is build based on most likely estimation and
should be adjusted after Discovery phase is completed." Slide 22 "Initial Project Budget": prices, not
rendered; its notes: "Additional Infrastructure costs would be determined on during Discovery Phase."
"All services are planned to be provided remotely, onsite engagement is possible based on separate
agreement."

## Slides 23-26 - Iteration 2 - Timeline and Budget Proposal

Slide 24 "Key optimization areas":

1. Mobile application was considered as out of scope. Desktop application will be limited to include
   only input functionalities. All functionalities would be available in web application.
2. Infrastructure would be implemented using cloud provider instead of hybrid or on-premise approach.
3. Calculations and Simulations were considered as out of scope.

Slide 25 "Iteration 2 Timeline": an image, same note as slide 21. Slide 26 "Iteration 2 Budget:
Delivery Phase": prices, not rendered; same notes as slide 22.

## Slides 27-30 - Iteration 3 - Timeline and Budget Proposal

Slide 28 "Key optimization areas":

1. Calculations and Simulations samples were provided. These functionalities were added back to the
   scope of the project. Additionally unit management system was added to the scope.
2. Innowise agreed to provide discount for Optimum Engineering Standards in amount of [amount removed]
   due to interest in the project and develop oil and gas portfolio in the region.
3. Specific collaboration requirements are provided to Optimum Engineering Standards to maintain
   special pricing conditions as follows:
   - Project shall start within the first week of January 2026
   - Innowise will be granted with possibility to freely use the project as success story in marketing
     materials and references after Project official Go Live.
   - Advanced payment in amount of [amount removed] before start of Project execution.

Slide 29 "Iteration 3: Timeline": an image, same note as slide 21. Slide 30 "Iteration 3 Budget":
prices, not rendered; same notes as slide 22.

## Slides 31-32 - Support and Project scope

Slide 32 "Post Go Live Support":

We offer 3 weeks warranty period after project release date. Once warranty period is over - several
support options are available:

- Allocation of a team for a certain number of hours per month, with a possible increase by agreement
  of the parties
- Change requests

The option with an allocated team might be the following:

Team: Software Engineer, QA Engineer, Project Coordinator

Allocation: to be determined before project completion. Current assumption that monthly 80h package
would be enough for this project with estimated budget [amount removed]

Note: Innowise may involve you in a strategic decision-making process with subsequent reporting

Support development team can be responsible for handling support issues and developing new features
from the backlog of the product.

## Slide 33 - Prototype video recording

A video; the prototype and its recordings are listed in the overview.

## Slides 34-38 - Web - HQ Application (three), Desktop Application, General activities

Images, not rendered (the estimate by feature).

## Slides 39-40 - Closing

39 "Develop your business with Innowise". Slide 40 "Why opt for us" says, verbatim: "Working with us,
Xalq bank will get personalized service from the outset" and "Xalq bank can employ our
industry-specific expertise and broad technology stack. With 16 years of experience" - text left over
from another proposal. Contact: Anton Snotau, Head of Business Development Middle East.
