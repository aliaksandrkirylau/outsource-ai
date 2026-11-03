---
type: source
kind: rendering
date: 2025-11-05
original: https://docs.google.com/spreadsheets/d/1KsP4-7CAzXqCQywxdLht56bbyUl38bqXEdQ9PsP_sfQ
removed:
  - every rate and every amount - the "Rate, USD/hour" and "Estimate, USD" columns, the "Forecasted Cost (USD)" row and the "TOTAL USD" row
  - the company address and phone number in the tab headers
---

# 2025-11-05 WBS sent to the client - rendering

Google Sheet "Optimum Engineering Standards - WBS", read on 2026-09-28 as displayed values. All six
tabs, verbatim, typos kept, hours only. Rows are numbered as in the sheet; a column letter is the
sheet's. "-" is in the sheet; an empty cell is empty there. Line breaks inside a cell are shown as
`<br>`. The formulas were not checked. Never edited after storing.

## Tab "Overview"

| Row | Cells |
|---|---|
| 5 | B5 Optimum Engineering Standards \| Estimate |
| 6 | B6 Project: · D6 Project Optimum Engineering Standards |
| 7 | B7 Platforms: · D7 Web application and Cross Platform application |
| 8 | B8 Programming Stack: · D8 Backend service - .NET <br>Local client application - MAUI<br>Central office web application - ReactJS<br>Identity provider - ASP.NET Identity or Keylock<br>DataBases: <br>Local storage for site clients SQLite - to keep data ready for server sync<br>Central database PostgreSQL - supports materialized view for efficient reports building |
| 10 | B10 Development Team composition (FTE): · D10 Frontend Developer · E10 2 |
| 11 | D11 Backend Developer · E11 2 |
| 12 | D12 Business Analyst · E12 1 |
| 13 | D13 UI/UX Designer · E13 1 |
| 14 | D14 QA Engineer · E14 1 |
| 15 | D15 Project Manager · E15 0.5 |
| 16 | D16 DevOps · E16 0.5 |
| 17 | D17 Data engineer · E17 0.25 |
| 19 | B19 Forecasted Timeline (months): · D19 Min · E19 Max |
| 20 | D20 4 months · E20 6 months |
| 22 to 23 | The forecasted cost row, min and max [amounts removed] |
| 25 | B25 The provided estimation displays possible, most likely hours and timelines of product development, and should not be considered as a commitment from the implementation team to meet these hours and timelines, as the software development lifecycle is a complex process and cannot be predicted with high accuracy. |
| 26 | B26 Created 05.11.2025 |

## Tab "Discovery Estimation"

The rate and amount columns (D, E) are removed, with the TOTAL row's amount.

| Row | B | C Estimate, hours |
|---|---|---|
| 7 | Total Estimation | |
| 8 | UI/UX designer | 60 |
| 9 | Solution Architect | 80 |
| 10 | Business Analyst | 120 |
| 11 | Project manager | 40 |
| 12 | Domain experts | 70 |
| 13 | TOTAL | 370 |

## Tab "Selected Development Estimation"

The rate and amount columns (E, F, G) are removed, and row 29, "TOTAL USD", entirely.

| Row | B | C min | D max | H Comments |
|---|---|---|---|---|
| 6 | | Estimate, hours | | Comments |
| 7 | Total Estimation | min | max | |
| 8 | Design | | | See breakdown on separate tab |
| 9 | Total design | 323 | 364 | The UI/UX Designer is responsible for mapping out the desired user experience in the form of wireframes and ensuring that the application meets the user needs. |
| 10 | Development | | | See breakdown on separate tabs |
| 11 | Back-end Development (web) | 555 | 646 | |
| 12 | Front-end Development (web) | 534 | 712 | |
| 13 | Back-end Development (desktop+mobile) | 146 | 201 | |
| 14 | Front-end Development (desktop+mobile) | 545 | 784 | |
| 15 | Total Development | 1780 | 2343 | |
| 16 | Quality Assurance | | | |
| 17 | Quality Assurance | 532 | 703 | |
| 18 | Stabilization | 268 | 351 | |
| 19 | Total Quality Assurance | 800 | 1054 | |
| 20 | Project management & Business Analysis | | | |
| 21 | PM Activities | 332 | 480 | Budgeting, Planning of scope of work, Building Roadmap, JIRA setup and Tasks management, Project Processes Setup, Support internal and external communication, Risk Management, Delivery support, Scrum implementation, Monitoring Automation. |
| 22 | BA Activities | 338 | 466 | Business analyst is in charge of understanding business needs, gathering requirements. Responsibilities include analyzing processes and fostering communication between stakeholders. |
| 23 | Total PM & BA | 670 | 946 | |
| 24 | DevOps | | | See breakdown on separate tab |
| 25 | DevOps | 449 | 600 | The DevOps Engineer is responsible for configuration and environments management, as well as the continuous integration/deployment process including automated builds, deployment, and test runs. |
| 26 | Data engineer (optional) | | | See breakdown on separate tab |
| 27 | Total Data Engineering | 201 | 310 | |
| 28 | TOTAL HOURS | 4,223 | 5,617 | |

The sheet has no data engineering tab. The development rows here are not the Development tab's totals
(web front end: 534 to 712 here, 468 to 652 in Development row 91).

## Tab "Development"

Columns: B Work Breakdown Item · C, D Web FE Hours min, max · E, F Web BE Hours · G, H Application FE
Hours · I, J Application BE Hours · K, L UI\UX Hours · M, N BA Hours · O Stage (MVP) · P Comments.

| Row | Work Breakdown Item | C Web FE min | D max | E Web BE min | F max | G App FE min | H max | I App BE min | J max | K UI/UX min | L max | M BA min | N max | O MVP | P Comments |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | Base project setup | | | | | | | | | | | | | | |
| 6 | UI Kit | - | - | - | - | - | - | - | - | 10 | 12 | | | TRUE | |
| 7 | Project setup | 8 | 16 | 8 | 10 | 8 | 16 | 8 | 10 | - | - | 4 | 4 | TRUE | |
| 8 | Architecture | 16 | 20 | 12 | 14 | 16 | 20 | 12 | 14 | - | - | 0 | 0 | TRUE | |
| 9 | Base components and UI theme | 40 | 40 | - | - | 40 | 40 | - | - | - | - | 0 | 0 | TRUE | |
| 10 | DB structure setup | 10 | 12 | 10 | 12 | 10 | 12 | 10 | 12 | - | - | 0 | 0 | TRUE | |
| 11 | Localization | 12 | 16 | 6 | 8 | 12 | 16 | 6 | 8 | - | - | 0 | 0 | TRUE | |
| 12 | Role model | 24 | 32 | 8 | 10 | 24 | 32 | 8 | 10 | - | - | 6 | 8 | TRUE | Ability to manage system access permissions through assigning roles to the existing users. |
| 14 | **Project features** | | | | | | | | | | | | | | |
| 15 | **Web-Based Application** | | | | | | | | | | | | | | |
| 16 | Login/Logout | | | | | | | | | | | | | | |
| 17 | Authorization/Authentication | 16 | 18 | 24 | 32 | - | - | - | - | 6 | 8 | 8 | 12 | TRUE | Utilizing Identity provider (analogue - ASP.NET or Keylock). Supporting authentication flow for access to manage the superuser's unique oversight permissions and adapt the accessed UIs. |
| 18 | Admin panel | | | | | | | | | | | | | | |
| 19 | Manage User Accounts | 28 | 32 | 6 | 8 | - | - | - | - | 12 | 14 | 18 | 24 | TRUE | Ability to CRUD user accounts. Includes assigning to one of the three required roles (Admin, Engineer, Supervisor/Manager). |
| 20 | Parameter Threshold Definition | 10 | 24 | 6 | 8 | - | - | - | - | 4 | 6 | 6 | 8 | TRUE | Ability to define threshold limits (minimum/maximum acceptable values) for each of the fluid parameters tracked. |
| 21 | Audit Logging & Modification Approval | 16 | 32 | 14 | 16 | - | - | - | - | 6 | 8 | 8 | 16 | TRUE | Ability to track all data entries edit/backfill actions (when, by whom and what was changed) and their approval status.<br>Up to 30 logged actions |
| 22 | Location Management (Optional) | 12 | 28 | 6 | 8 | - | - | - | - | 6 | 8 | 0 | 0 | TRUE | Ability to CRUD rig sites (locations) that are currently operable and available for selection within project. |
| 23 | Project Template Management (Optional) | 12 | 16 | 12 | 14 | - | - | - | - | 6 | 8 | 4 | 6 | TRUE | Template configuration form for project fields to pre-define and manage project structure and requirements (e.g., standard reports, required measurement frequency). |
| 24 | Project management | | | | | | | | | | | | | | |
| 25 | Manage projects | 24 | 32 | 10 | 12 | - | - | - | - | 10 | 12 | 12 | 16 | TRUE | CRUD project, assign/reassign engineers |
| 26 | Project details | 10 | 16 | 5 | 6 | - | - | - | - | 4 | 6 | 8 | 12 | TRUE | View list of projects, filter projects |
| 27 | Measurements | 8 | 12 | 14 | 16 | - | - | - | - | 4 | 6 | 6 | 8 | TRUE | View the raw measurement entries inputted by the Engineers (up to 50 parameters) |
| 28 | Quality Control  | 4 | 6 | 12 | 14 | - | - | - | - | 2 | 4 | 8 | 12 | TRUE | Feature focused on Quality Control (QC), allowing to easily see and review data streams from their assigned rigs with entries flagged for threshold violations highlighted. |
| 29 | Dashboard | | | | | | | | | | | | | | |
| 30 | Dashboard View | 16 | 18 | 36 | 48 | - | - | - | - | 8 | 10 | 8 | 12 | TRUE | Dashboard providing a high-level one-page snapshot of operational status, key KPIs, and progress against targets across multiple job sites. Includes filter and search for a particular project and visualization options (simple charts/graphs -  bar charts, pie charts, etc.). |
| 31 | Reporting  | | | | | | | | | | | | | | |
| 32 | Reports Approval Flow | 4 | 6 | 5 | 6 | - | - | - | - | 2 | 4 | 6 | 8 | TRUE | Function to formally 'Approve' or 'Lock' End-of-Section and End-of-Well reports generated by the Engineer. |
| 33 | End-of-Day Report Generation | 10 | 12 | 24 | 32 | - | - | - | - | 4 | 6 | 4 | 6 | TRUE | Ability to generate a standard End-of-Day Report. The report must be filterable and exportable to the PDF, CSV, XLXS  formats. |
| 34 | End-of-Section Report Generation | 10 | 12 | 24 | 32 | - | - | - | - | 4 | 6 | 4 | 6 | TRUE | Ability to generate a comprehensive End-of-Section Report. The report must be filterable and exportable to the PDF, CSV, XLXS  formats. |
| 35 | End-of-Well Report Generation | 10 | 12 | 32 | 40 | - | - | - | - | 4 | 6 | 4 | 6 | TRUE | Ability to generate a comprehensive End-of-Well report, summarizing all data, inventory, and simulation results collected throughout the duration of the project. The report must be filterable and exportable to the PDF, CSV, XLXS  formats. |
| 36 | Inventory Report Generation | 10 | 12 | 28 | 36 | - | - | - | - | 4 | 6 | 8 | 12 | TRUE | Ability to generate Inventory targeted report in desired file format, such as a summary of the current quantity, use trend, and cost for all materials at a selected rig site. The report must be filterable and exportable to the PDF, CSV, XLXS  formats. |
| 37 | Inventory Module | | | | | | | | | | | | | | |
| 38 | Inventory Management | 28 | 32 | 12 | 14 | - | - | - | - | 12 | 14 | 8 | 12 | TRUE | Ability to CRUD products (chemicals, materials) used on the rig, including Brand Name, Material #, Unit Size, and Unit of Measure (UoM). |
| 39 | Stock Movements Log | 12 | 20 | 8 | 10 | - | - | - | - | 4 | 6 | 6 | 8 | TRUE | Ability to record key inventory events: Initial Loadout, Inflow (Received), Returned, and Lost. |
| 40 | Material Cost Linkage | | | 12 | 14 | - | - | - | - | - | - | 4 | 6 | TRUE | Logic to link consumption entries to a unit price from the provided Price List for internal (e.g., Daily Report) cost calculation. |
| 41 | Other | | | | | | | | | | | | | | |
| 44 | **Desktop Application** | | | | | | | | | | | | | | |
| 45 | Login/Logout | | | | | | | | | | | | | | |
| 46 | Authorization/Authentication | - | - | - | - | 16 | 24 | - | - | - | - | 1 | 2 | TRUE | Utilizing Identity provider (analogue - ASP.NET or Keylock). Supporting authentication flow for access to manage the superuser's unique oversight permissions and adapt the accessed UIs. |
| 47 | New User Onboarding | - | - | - | - | 16 | 24 | 4 | 5 | 8 | 10 | 4 | 6 | TRUE | A step-by-step tutorial or wizard for new users on how to enter daily data  (up to 10 promopts) |
| 48 | Project management | | | | | | | | | | | | | | |
| 49 | Project Setup & Management | - | - | - | - | 12 | 16 | - | - | - | - | 4 | 4 | TRUE | Ability to create a new (or select and update an existing) well/project entry and input the required details (location, client info, etc.) with project assigned active status and ID as a result. |
| 50 | Measurements input | - | - | - | - | 8 | 10 | - | - | 6 | 8 | 8 | 12 | TRUE | Ability to manually input and pre-validate the measured fluid parameters (e.g., density, viscosity) linked to the current shift and project. |
| 51 | Threshold Violation Alerting | - | - | - | - | 6 | 8 | 5 | 6 | 6 | 8 | 8 | 12 | TRUE | Visual highlight/notification of an inputted parameter value that surpasses a predefined threshold. The system should require to input a mandatory comment or reason before allowing the data to be saved with a 'flagged' status. |
| 52 | Contextual Input Guidance | - | - | - | - | 6 | 8 | 5 | 6 | 4 | 6 | 6 | 8 | TRUE | Contextual hints for specific fields during data entry, providing rules or acceptable ranges to prevent incorrect input (e.g., "Hint: Density must be between X and Y"). |
| 53 | Calculations&Modelling | | | | | | | | | | | | | | |
| 54 | Derived Value Calculation | - | - | - | - | 6 | 8 | 6 | 8 | - | - | 4 | 6 | TRUE | Backend logic to automatically calculate derived values (e.g., density corrections) upon the Engineer saving the raw input data. |
| 55 | Standard Engineering Calculator | - | - | - | - | 12 | 16 | - | - | 8 | 10 | 4 | 6 | TRUE | Module allowing to run quick, standard engineering calculations (e.g., "How many bags of barite do I need to increase mud weight?") using a set of input variables (e.g., desired weight, current volume). |
| 56 | Simulation: Fluid Hydraulics | - | - | - | - | 24 | 32 | - | - | 12 | 14 | 4 | 6 | TRUE | Fluid hydraulics simulation/modeling module. UI form inputs include technical details like well architecture, rheology data, and flow rates. Output includes "what if" scenarios (e.g., impact of changing flow rates) with chart visualizations and data tables showing predictive outcomes. Charts are not complex (bar charts, curves x-y, etc.) |
| 57 | Inventory  | | | | | | | | | | | | | | |
| 58 | Daily Consumption Log | - | - | - | - | 8 | 10 | - | - | 8 | 10 | 6 | 8 | TRUE | Ability for the Engineer to manually log the daily use or consumption of materials for the shift/day. |
| 59 | Stock Movements Log | - | - | - | - | 8 | 10 | - | - | - | - | 6 | 8 | TRUE | Ability to record key inventory events: Initial Loadout, Inflow (Received), Returned, and Lost. |
| 60 | Product Concentration Tracking | - | - | - | - | 8 | 10 | 5 | 6 | 6 | 8 | 6 | 8 | TRUE | Ability to input and track the Ending Concentration (e.g., lb/bbl) of specific mud components. |
| 61 | Low Stock Alerting | - | - | - | - | 10 | 16 | 5 | 6 | 4 | 6 | 4 | 6 | TRUE | Visual highlight/notification of remaining quantity of a material falling below a predefined low stock level. |
| 62 | Expiration Date Alerting | - | - | - | - | 10 | 16 | 5 | 6 | 4 | 6 | 4 | 6 | TRUE | Visual highlight/notification of material approaching or passed its expiration date. |
| 63 | Reporting | | | | | | | | | | | | | | |
| 64 | End-of-Day Report Generation | - | - | - | - | 24 | 32 | - | - | - | - | 1 | 1 | TRUE | Ability to generate a standard End-of-Day Report. The report must be filterable and exportable to the PDF/CSV/xlxs formats. |
| 65 | End-of-Section Report Generation | - | - | - | - | 24 | 32 | - | - | - | - | 1 | 1 | TRUE | Ability to generate a comprehensive End-of-Section Report. The report must be filterable and exportable to the PDF/CSV/xlxs formats. |
| 66 | End-of-Well Report Generation | - | - | - | - | 24 | 32 | - | - | - | - | 1 | 1 | TRUE | Ability to generate a comprehensive End-of-Well report, summarizing all data, inventory, and simulation results collected throughout the duration of the project. The report must be filterable and exportable to the PDF/CSV/xlxs formats. |
| 67 | Inventory Report Generation | - | - | - | - | 24 | 32 | - | - | - | - | 1 | 1 | TRUE | Ability to generate Inventory targeted report in desired file format, such as a summary of the current quantity, use trend, and cost for all materials at a selected rig site. The report must be filterable and exportable to the PDF/CSV/xlxs formats. |
| 68 | Other | | | | | | | | | | | | | | |
| 71 | **Mobile Application <br>Desktop Features Adaption** | | | | | | | | | | | | | | The app is using the same NET MAUI both for desktop and mobile - thats not development from scratch. Assume the most fucntions are implemented in desktop part not to estimate the efforts twice. |
| 72 | Login/Logout | | | | | | | | | | | | | | |
| 73 | Authorization/Authentication | - | - | - | - | 4 | 8 | - | - | 2 | 4 | 2 | 4 | TRUE | Utilizing Identity provider (analogue - ASP.NET or Keylock). Supporting authentication flow for access to manage the superuser's unique oversight permissions and adapt the accessed UIs. |
| 74 | Project | | | | | | | | | | | | | | |
| 75 | View project details  | - | - | - | - | 12 | 16 | - | - | 2 | 4 | 2 | 2 | TRUE | View main project details <br>Note: the feature mostly accounted in the desktop part! |
| 76 | Measurements input | - | - | - | - | 2 | 4 | - | - | 2 | 4 | 2 | 2 | TRUE | Ability to manually input and pre-validate the measured fluid parameters (e.g., density, viscosity) linked to the current shift and project.<br>Note: the feature mostly accounted in the desktop part! |
| 77 | Derived Value Calculation | - | - | - | - | 2 | 4 | - | - | | | 2 | 2 | TRUE | Backend logic to automatically calculate derived values (e.g., density corrections) upon the Engineer saving the raw input data. |
| 78 | Standard Engineering Calculator | - | - | - | - | 2 | 4 | - | - | 4 | 6 | 2 | 2 | TRUE | Module allowing to run quick, standard engineering calculations (e.g., "How many bags of barite do I need to increase mud weight?") using a set of input variables (e.g., desired weight, current volume)<br>Note: the feature mostly accounted in the desktop part! |
| 79 |  Inventory | | | | | | | | | | | | | | |
| 80 | Daily Consumption Log | - | - | - | - | 1 | 2 | - | - | 2 | 4 | 2 | 2 | TRUE | Ability for the Engineer to manually log the daily use or consumption of materials for the shift/day<br>Note: the feature mostly accounted in the desktop part! |
| 81 | Low Stock Alerting | - | - | - | - | 10 | 16 | - | - | 2 | 4 | 2 | 2 | TRUE | Visual highlight/notification of remaining quantity of a material falling below a predefined low stock level.<br>Note: the feature mostly accounted in the desktop part! |
| 82 | Expiration Date Alerting | - | - | - | - | 10 | 16 | - | - | 2 | 4 | 2 | 2 | TRUE | Visual highlight/notification of material approaching or passed its expiration date<br>Note: the feature mostly accounted in the desktop part! |
| 83 | Reporting | | | | | | | | | | | | | | |
| 84 | Basic Reports Overview | - | - | - | - | 32 | 40 | - | - | 2 | 4 | 2 | 4 | TRUE | A simplified, read-only view of the data entered for the selected reports (without file export option). |
| 86 | **General activities** | | | | | | | | | | | | | | |
| 87 | Unit Tests | 30 | 60 | 67 | 84 | 30 | 60 | 16 | 19 | - | - | | | TRUE | |
| 88 | Error States and loaders | 16 | 20 | 6 | 8 | 16 | 20 | 6 | 8 | 4 | 6 | | | TRUE | |
| 89 | Project Technical Documentation | 8 | 16 | 12 | 14 | 8 | 16 | 12 | 14 | - | - | | | TRUE | |
| 90 | Communication: Scrum (planning, daily, demo, retro), requirements clarifications | 64 | 80 | 64 | 80 | 64 | 80 | 20 | 28 | 24 | 32 | 56 | 64 | TRUE | The implementation effort presented also includes communication, as communication is inevitable, as individuals make up the team. Communication is the key to project success and the team members need to be involved in certain discussions, both planned and unplanned, among which are:<br>- Daily Meetigs<br>- Sprint Planning<br>- Sprint Review<br>- Retrospective<br>- Interteam communications (discussions on the matter of technical implementation, architectural choices, PR reviews, merge requests, as well as any meetings aimed at improving the processes, technical & project documentation, acquiring the understanding of the business part of the project)<br>- Agendas preparation and requirements collection |
| 91 | **Total Development** | 468 | 652 | 483 | 606 | 549 | 758 | 133 | 166 | 224 | 308 | 287 | 390 | | |
| 92 | **Total MVP** | 468 | 652 | 483 | 606 | 549 | 758 | 133 | 166 | 224 | 308 | 287 | 390 | | |

Rows 1 to 4, 13, 42, 43, 69, 70 and 85 are empty or the header. Every line is TRUE in column O.

## Tab "DevOps"

| Row | B Work Breakdown Item | C min | D max | E Comments |
|---|---|---|---|---|
| 3 | Work Breakdown Item | Hours | | Comments |
| 5 | Environment setup | | | |
| 6 | I. Environment & VM Automation (On-Premises) | | | |
| 7 | Docker Compose for Local Dev (Backend) | 24 | 32 | Creating a stable Docker environment for local development and testing of Aggregation/Central services. |
| 8 | Container Image Optimization & Hardening | 24 | 32 | Reviewing and securing Dockerfiles for all 5-6 server components (Identity, Aggregation, Central). |
| 9 | Ansible/Terraform Infrastructure Setup | 40 | 56 | Developing Infrastructure-as-Code (IaC) to automatically provision/configure the on-premises VMs/servers (OS, networking, Docker install). |
| 10 | Deployment Scripting (CI/CD to VM) | 32 | 40 | Creating automated CI/CD scripts (e.g., using Ansible Playbooks or CI/CD agents) to pull images and deploy/update containers on the target VMs. |
| 11 | II. CI/CD & Client Update | | | |
| 12 | CI Pipeline Setup (Build, Test, Security) | 32 | 40 | Setting up the pipeline for building Docker images, running Unit/Integration tests, and executing security scanning (SAST). |
| 13 | DB Migration & Schema-as-Code | 32 | 40 | Integrating database migration tools (e.g., Flyway/EF Core Migrations) into the CD process for PostgreSQL. |
| 14 | Desktop App (MAUI) Update Pipeline | 56 | 72 | CRITICAL: Design, build, and rigorous testing of a robust auto-update/forced-update mechanism for 70+ remote Windows clients over sketchy connectivity. |
| 15 | III. Operations & Observability | | | |
| 16 | Logging Stack Setup | 32 | 40 | Deploying a centralized logging system (e.g., ELK Stack or Loki/Grafana) and configuring all services to stream logs to it. |
| 17 | Monitoring Setup & Custom Alarms | 32 | 40 | Setting up a monitoring system (Prometheus/Grafana). Configuring specific alarms for performance, resource utilization, and crucially, Site Synchronization Lag (70+ unique alarms). |
| 18 | Central Backup & DR Setup | 40 | 56 | Implementing automated daily full and incremental backups , including a documented and tested Disaster Recovery (DR) restoration procedure. |
| 19 | IV. Security & Documentation | | | |
| 20 | Configuration & Secret Management | 32 | 40 | Establishing a secure method for managing environment variables and secrets (e.g., self-hosted Vault or secured files). |
| 21 | RBAC Security Testing Integration | 16 | 24 | Integrating automated tests to verify Role-Based Access Control (RBAC) integrity across all services (Engineers, Supervisors, Management). |
| 22 | Release Readiness and Stabilization Support | | | |
| 23 | Incident Response and Management | 16 | 24 | A process for rapid incident response and management of emerging post-release issues, including monitoring, root cause analysis and implementation of solutions to improve system stability.  |
| 24 | Documentation & Runbooks (Operational) | 24 | 40 | Create comprehensive documentation for deployment processes, CI/CD configurations, and infrastructure setups.<br>Ensure all configurations and scripts are well-documented for future reference. |
| 25 | Issue Resolution | 16 | 24 | Quickly resolve post-release issues and defects based on reports and monitoring. |
| 26 | Total Development | 448 | 600 | |

## Tab "Assumptions & Risks"

B6: "| Assumptions". The numbering skips 24.

| Row | No. | Assumption |
|---|---|---|
| 9 | 1 | This document provides a baseline estimate for the basic planning of the timeline and budget. To implement the project, Innowise provides the Client with a dedicated team |
| 10 | 2 | Changes in the composition and / or content of functional requirements, as well as the sequence of their implementation, can lead to a change in the timing and budget of the project. Any features that were not described in the documentation provided by the Client at the time of the evaluation, or that were changed during the project, shall be considered as Change Requests and are to be discussed, evaluated and agreed with the client separately. |
| 11 | 3 | At the time of preparing the estimate, the full requirements were not provided. |
| 12 | 4 | Innowise is solely responsible for the development of the applications and is not responsible for possible restrictions on the application by third parties. |
| 13 | 5 | Pace of Development will also depend on availability for communication and speed of answering from the Client during Development Process. Timeline is created on the basis that communication process with the customer will comply with Communication Plan. |
| 14 | 6 | Innowise doesn’t take any responsibility for purchase of servers, the performance of server provided by the Client or third parties. |
| 15 | 7 | Innowise doesn’t take any responsibility for changes in the code made by not-Innowise software developers. |
| 16 | 8 | All accounts/credentials/certificates required for development, integration and deployment should be provided on time. Delay may affect Timeline provisions. |
| 17 | 9 | We assume that modeling (simulations) does not require access to a central service for calculations. However, if access to a central server becomes necessary, it will lead to limitations in offline mode |
| 18 | 10 | The modules required for each user Role are assumed by Innowise team and are subject to further review from Client's side, possibly resulting in estimations update. |
| 19 | 11 | The vizualization capabilities for reports/dashboards are estimated for simple chart types (e.g., pie chart, bar chart) and would require additional efforts allocated if more complex charts are needed. |
| 20 | 12 | Efforts for calculationg and modelling features are assessed by assuming the Client provides Innowisewith clear formulars to be used |
| 21 | 13 | 3D visualisations, comlpex charts designing, animations are not in the scope |
| 22 | 14 | Desktop application is used by engineers only, Mobile by managers and engineers, Web - by Admin, managers and supervisors |
| 23 | 15 | API design is out of scope |
| 24 | 16 | External integrations are out of scope (apart from identity management provider). If integration with third-party services is required, the additional scope of work will be evaluated and implementation plan will be revised. |
| 25 | 17 | Complex modelling is not required |
| 26 | 18 | Reports sending to Client is out of the solution scope. Users can generate reports, but their sending is made via other solutions. |
| 27 | 19 | The only language to be supported is English |
| 28 | 20 | A step-by-step tutorial or wizard for new users includes up to 10 hints explaining how to use the desktop app, what modules are where and what their purposes are, but not guidance how to calculate the paramenters and model results. Tech Guide is not in the scope as well. |
| 29 | 21 | Reports generation is not in the scope of mobile app |
| 30 | 22 | Adaptive markup implementation is not accounted |
| 31 | 23 | Existing data migration is out of scope |
| 32 | 25 | Post-deployment support efforts are not included |
| 33 | 26 | Due to uncertainty regarding the complexity of calculations/simulation and the number of algorithms required, the efforts were accounter per 1 algorithm (rows 54-56 of Development tab) |

B35: "| Risks".

| Row | No. | Risk |
|---|---|---|
| 38 | 1 | Not clear requirements, especially related to the mobile app - medium |
| 39 | 2 | Absence of clear understanding the complexity of calculations and modelling modules - high |
| 40 | 3 | Scope creep duting the project implementation - medium |
| 41 | 4 | Uncertainty regarding the need for API design and development - medium |
| 42 | 5 | Absence of support from the client side (calculations and modelling) - high |
| 43 | 6 | Limited clients involment, delays with feedback - low |
| 44 | 7 | Potential gaps in user experience (UX) expectations - medium |
| 45 | 8 | Client infrastructure readiness - medium |
