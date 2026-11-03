---
type: source
kind: rendering
date: 2025-11-03
original: https://docs.google.com/document/d/1xZZ4DTDPOquMto5oD2izaRSBc6kISwpxzQs-zhtrGkM
removed:
  - the uplift of the on-demand support rate over the team-allocation rate (a percentage of a rate)
  - the architecture diagram image stays in the original
---

# 2025-11-03 Solution proposal - rendering

Google Doc "Proposal for Optimum Engineering Standards (without budget)", issued by Daniil Lynko, Big
Data Engineer, reviewed by Aliaksei Tsitou, Presale Manager, dated Nov 3, 2025 (last changed
2025-11-04). The internal draft behind the client-facing slides. Verbatim; checkbox markers and
emphasis dropped, the budget placeholders and the empty rate table kept as they are. Never edited
after storing.

| ISSUED BY: | Daniil Lynko, Big Data Engineer |
|---|---|
| REVIEWED BY: | Aliaksei Tsitou, Presale Manager at Innowise |
| DATE: | Nov 3, 2025 |
| SECURITY: | Confidential |

# SOLUTION PROPOSAL

## Description

Optimum Engineering Standards Co. Ltd. (OES), a Saudi company specializing in mud engineering and
chemical supply. OES is one of the growing business houses established in 2006 and located at
Al-Khobar in the Kingdom of Saudi Arabia.

## Initial request

OES requires a custom, scalable software solution to replace its current Excel-based and manual data
management processes for drilling fluid operations. The system must serve as a centralized, in-house
application for ~70 rig sites, many of which have poor or non-existent internet connectivity. The
solution must provide full offline functionality for engineers , ensuring data integrity upon
synchronization , and deliver robust modules for measurements , inventory , complex engineering
calculations , and fleet-wide reporting.

## Problems

- Operational Disruption & Data Loss: Unreliable internet at remote rig sites (per Meeting Notes)
  halts productivity. Current tools lack offline capabilities, leading to data loss, delays, and
  reliance on manual workarounds.
- Data Integrity and Fragmentation: The current use of Excel and disparate tools leads to data silos,
  manual entry errors, and an inability to perform centralized analysis or ensure data quality across
  operations.
- Lack of Scalability: Current solutions cannot scale to support the client's ~70 locations or provide
  the complex, role-based features required for engineers, supervisors, and managers.
- Inefficient Reporting & Analysis: Generating critical reports (End-of-Day, End-of-Well, Inventory) is
  a time-consuming, manual process. There is no capability for real-time dashboards or advanced
  hydraulic calculations.
- Data Security & Sovereignty: The client's confidential data and customer details require a solution
  that avoids full dependency on public Cloud infrastructure, necessitating an on-premise solution.

## Objectives

- Ensure 99.9% Data Integrity & Availability: Implement a robust offline-first system with efficient,
  automated data synchronization between remote job sites and the central on-premise HQ server.
- Generate Complete and Accurate Reports: Deliver a comprehensive reporting module to generate
  End-of-Day, End-of-Section, End-of-Well, Inventory, and Engineering Calculation reports, with export
  to PDF, CSV, and XLS.
- Improve Operational Efficiency: Provide a user-friendly, low-latency interface with guided wizards to
  streamline data entry, inventory tracking, and complex fluid calculations.
- Establish a Scalable & Secure Platform: Build a centralized on-premise solution with role-based
  access for Mud Engineers, Supervisors, Managers, and Admins that can scale to 100+ locations.

## Functional Requirements

- Manual Data Input: The system must provide a user interface for manual input of measurement and
  chemical analysis data taken from laboratory equipment on the rig site
- Data Centralization: The system must be able to centrally store and manage data generated from
  approximately 70 simultaneous job sites (drilling rigs). Local data must be regularly stored/migrated
  to a central database
- Complex Calculations & Simulations: The software should include modules for basic engineering
  calculations (e.g., mud weight change, chemical additions) and more complex fluid hydraulics
  simulations for scenario analysis.
- Comprehensive Reporting: The system must generate Daily Reports and End of Job Reports , as well as
  specific reports (e.g., inventory, lab tools) with export options for PDF (standard), CSV, and Excel.
- Inventory Management: The system must track and manage initial loadout, inflow, daily consumption,
  cumulative consumption per section and well, daily balance, product details (brand name, generic
  description, density, material #), products use concentration (in pounds/barrel & %) in the drilling
  fluid, expiration dates, product unit size, unit cost and total cost.

## Non-Functional Requirements

- Deployment / Connectivity: A desktop application (Windows OS) is required for the field engineer on
  the job site. This is critical because many job sites are in remote locations with sketchy or no
  Internet access.
- Data Integrity & Quality Control: The software must be smart enough to include rule-based
  alerting/alarms and internal control mechanisms to prevent wrong data input and flag when parameters
  go outside the customer-defined range/specification.
- Important KPIs to monitor in reporting:
  - Tracking of critical mud parameters by depth & compared to offset wells.
  - Top 5 product consumption and general products use pie charts for current well section &
    cumulative for the well.
  - Fluids volume trend, cumulative mud loss and volume-out alert.
  - QHSE alerts: alerts on upcoming expirations of products, reagents, stock-outs, or equipment
    calibration.
  - Drilling progress status
- Security & Confidentiality: The data is considered confidential customer data. The client wants to
  avoid being totally dependent on 100% cloud-based solutions due to this concern.
- User Access / Roles: The system requires Role-Based Access Control (RBAC) for the following user
  groups:
  - Mud Engineer: Enter measurements, perform calculations and simulations, generate reports and email
    reports to the supervisors
  - Supervisor: Review and generate reports
  - Manager: Access dashboards, oversee multiple sites
  - Admin: Manage users, roles, and system settings

# Proposed solution

Innowise wants to provide a robust and sustainable solution for building a strong, long-term
relationship in the future.

## Overview

Our proposal directly addresses your requirements for a true offline-first desktop application and a
secure on-premise deployment.

We recommend a robust Hybrid Architecture that combines a native Desktop application for rig sites
with the centralized control of an on-premise server at OES's HQ. This solution is composed of 2 main
parts:

- Offline access for rig sites: A Native Windows Desktop Application built with .NET MAUI. This
  application is installed on the shared rig computers and is designed to work 100% offline. All data
  (measurements, inventory, calculations) is saved to a local SQLite database. Engineers can perform
  their entire job without an internet connection.
- Online for HQ: A central On-Premise Server deployed at your headquarters. This server hosts the
  central PostgreSQL database, an Aggregation Service to receive data from rigs, and a Web Application
  for Supervisors and Managers to view fleet-wide dashboards and reports.

This approach provides the best of both worlds: it gives rig engineers the reliable, high-performance
offline tool they need, while simultaneously giving HQ managers the centralized data and reporting
they require, all within your secure, on-premise network.

## Solution

Based on OES feedback, answers and additional information on the crucial data architectural
questions, Innowise proposes a comprehensive phased approach below:

| Phase | Key Activities | Key Deliverable(s) |
|---|---|---|
| 1. Discovery & Architecture | Step 1.1 (Workshops): Facilitate workshops with OES Subject Matter Experts (SMEs) to map all business processes. Step 1.2 (Data Modeling): Define the detailed data model, including the master data hierarchy (Company, Client, Rig, Well, etc.). Step 1.3 (Logic Definition): Document the complex business rules for the Engineering Calculation & Hydraulics Simulation module and the Inventory Management module. Step 1.4 (Sync Strategy): Design the robust data synchronization and conflict-resolution logic, a critical component for ensuring 99.9% data integrity. Step 1.5 (Infrastructure): Define the specific hardware and network requirements for your on-premise HQ server. Step 1.6 (UX/UI Design): Create detailed wireframes and UI mockups for both the MAUI Desktop App and the HQ Web App. | 1. A Solution Architecture Document (SAD), 2. Detailed Project Plan. |
| 2. Core Platform & On-Premise Setup | Step 2.1 (Infrastructure Support): Assist OES authorized IT personnel in provisioning and configuring the on-premise server environment (VMs, physical servers, networking). Step 2.2 (Database): Deploy and configure the central PostgreSQL database, including schema, tables, and materialized views for reporting. Step 2.3 (Security & IAM): Develop and deploy the Identity Provider service to manage in-app user accounts and Role-Based Access Control (RBAC). Step 2.4 (Core API): Develop the Central-service (.NET or Java), which will serve as the main API for all business logic. Step 2.5 (Sync Service): Develop and deploy the Aggregation Service, the dedicated endpoint responsible for receiving, validating, and processing data from all 70 remote desktop apps. | 1. A functional, secure, and ready-to-connect on-premise backend platform. |
| 3: Rig Site Desktop Application (MAUI) | Step 3.1 (App Shell): Develop the foundational .NET MAUI Desktop Application for Windows OS. Step 3.2 (Local Database): Integrate the local SQLite database for 100% offline data persistence. Step 3.3 (Core Modules): Build the primary user modules: Project Setup & Management Manual Measurement Input (<50 parameters) Alerting (threshold violations, low stock) Step 3.4 (Offline Engines): Implement the Inventory Management module and the Engineering Calculation, Simulation module to run fully offline. Step 3.5 (Sync Client): Build the client-side synchronization logic that automatically detects connectivity and pushes/pulls data to/from the HQ Aggregation Service. Bonus*: Implement the sets of rules and hints for new engineers and new app users. | 1. An installable Windows application package (e.g., .msi) capable of full offline operation. |
| 4: HQ Web Application & Integration | Step 4.1 (App Shell): Develop the browser-based Web Application (ReactJS). Step 4.2 (Admin Modules): Build the administrative UIs for: User & Role Management Parameter Threshold Definition Data Modification Approval Workflow Step 4.3 (Manager Modules): Build the management UIs for: Fleet-wide Dashboards (KPIs, charts) Quality Control (QC) Data Review Report Approval Flow (End-of-Section/Well) Step 4.4 (Reporting Layer): Build the comprehensive Reporting Module to generate all required reports (End-of-Day, End-of-Well, etc.) with CSV / Excel export capabilities. | 1. A functional, secure web portal for HQ staff. |
| 5: Integration, Testing & Handover | Step 5.1 (Integration Testing): Perform end-to-end testing, focusing heavily on the offline-to-online synchronization and data conflict resolution. Step 5.2 (Deployment): Assist OES IT team in rolling out the MAUI application to rig site computers. Step 5.3 (Training): Conduct knowledge transfer and training sessions for the OES admin team. Step 5.4 (Documentation): Deliver all technical and user documentation. Step 5.5 (Go-Live): Provide hyper-care support during the initial go-live period. | 1. A fully deployed, tested, and operational system, 2. Technical & User Documentation. |

## Solution components

| Component | Proposed Approach | Comment |
|---|---|---|
| Rig-Site Application | Local Windows Desktop App (.NET MAUI) | A native Windows application, as requested, that provides the full UI for data entry, calculations, and reporting. It is designed to operate 100% offline. |
| Local (Rig) Database | Embedded Local Database (SQLite) | An embedded, file-based database within the MAUI app. This is the core of the offline solution, allowing engineers to input and save all data with no internet. |
| Central Database | On-Premise PostgreSQL Database | Deployed on your on-premise server at HQ. Acts as the single source of truth for all data from all 70-100+ sites. PostgreSQL supports materialized views for efficient reporting. |
| Data Synchronization | On-Premise Aggregation Service | A dedicated service that reliably handles, validates, and processes all incoming data transmissions from the remote desktop apps. It manages all sync logic and data integrity. |
| HQ Management Portal | Central Web Application (ReactJS) | A browser-based application for Supervisors and Managers at the central office. Provides dashboards, fleet-wide KPIs, QC/review workflows, and aggregated reports. |
| Business Logic | On-Premise Central Service (.NET or Java) | The core server-side API that powers the HQ Web Application, handles complex centralized business logic, advanced reporting, and serves as the backend for the Aggregation Service. |
| Security | On-Premise Identity Provider | Manages in-app user accounts and Role-Based Access Control (RBAC) for Engineers, Supervisors, etc., across both the desktop and web applications. |

## Architecture Diagram

[diagram in the original]

## Technical Stack

- Backend Service: .NET or Java
- Local Client Application: MAUI
- Central office Web application: ReactJS
- Identity Provider: ASP.NET Identity or Keylock
- Databases
  - Local storage for site clients to keep data ready for server sync: SQLite
  - Central Database for supporting materialized view & efficient reports building: PostgreSQL

## Total hours

X – Y hrs.

## Total budget

For the upcoming project, we estimate the total cost to range between $____ and $_____.

## Team composition

| Role | Employment | Description |
|---|---|---|
| Solution Architect (Data) | PTE | Designs the end-to-end hybrid on-premise data architecture, synchronization strategy, and ensures the solution is scalable and secure. |
| Senior Data Engineer (SME) | FTE | Implements and maintains the central PostgreSQL database, data marts, ETLs, and the core Aggregation Service. Calculation modeling. |
| Backend Engineer | FTE | Builds the server-side Central Service, the complex calculation/simulation engine logic, and user authentication services. Develops the offline-first Windows Desktop Application (.NET MAUI), local SQLite integration, and the user-friendly interface. |
| DevOps | FTE | Infrastracture |
| Frontend Engineer (Web) | FTE | Develops the central Web Application (ReactJS) for HQ users, including dashboards and reporting UIs. |
| Business Analyst | FTE | Leads the discovery, documenting the complex business rules for calculations, inventory, and reporting. |
| Project Manager | PTE | Oversight across all phases, serves as the main point of contact, manages timelines, and ensures the project remains on track. |

## Deliverables

- A comprehensive Solution Architecture Document (SAD) detailing the on-premise architecture, data
  model, sync logic, and application design.
- A secure, centralized On-Premise Database (PostgreSQL) and a robust Data Aggregation Service.
- An Offline-First Windows Desktop Application (.NET MAUI), deployable to all rig site computers.
- A central Web Application for HQ-based managers and supervisors to access fleet-wide dashboards,
  perform QC, and manage users.
- Reporting & Dashboard Module featuring KPIs and standard reports (End-of-Day, End-of-Section,
  End-of-Well, Inventory) with PDF, CSV, and XLS export.

## Challenges

- Data Synchronization: Designing and building a truly robust, bi-directional synchronization and
  conflict-resolution engine that guarantees 99.9% data integrity over highly unreliable networks is
  the primary technical challenge.
- On-Premise Deployment & Maintenance: The client has specified an on-premise solution but also
  indicated a lack of internal technical staff to deploy and maintain centralized services. A key
  challenge will be defining the infrastructure requirements and establishing a clear plan for
  deployment and ongoing support, which will require close collaboration with your authorized IT
  personnel.
- Calculation Complexity: Accurately modeling and implementing the complex fluid hydraulics/mechanics
  simulations will require deep, sustained collaboration with your Subject Matter Experts (SMEs).
- Visualization Scope: The client's response to confirming simple models indicates a potential desire
  for complex visualizations. This scope must be strictly defined during the Discovery phase to avoid
  significant scope creep.

## Assumptions

This proposal and its timeline are based on the following assumptions. Delays in meeting these
dependencies may impact the project schedule.

- Budget and Timeline: The project timeline and budget may change once Step 1 is completed due to the
  high-level nature of the current requirements.
- Client Stakeholder Availability: The project requires timely access to your engineering and
  operations SMEs for workshops, especially for defining the calculation and inventory logic.
- Platform: The solution will be a hybrid architecture: 1) A Windows Desktop (.NET MAUI) application
  for offline use at rig sites, and 2) A central Web Application for online use at HQ.
- Infrastructure: This proposal assumes the client will provision the necessary on-premise server
  hardware (physical or virtual), network infrastructure (e.g., VPNs), and OS/DB licenses for hosting
  the central database, web application, and services.
- Deployment & Maintenance: The effort for initial server setup, deployment, and ongoing on-premise
  maintenance is not included in the core development budget and will be handled either by the
  client's authorized IT personnel or under a separate Post-Project Support agreement.
- Mobile Application: A separate mobile-native app for supervisors (iPhone/Android) is considered as a
  future phase and is not included in this MVP proposal.
- Data Migration: Migration of historical data (format to be defined) is not part of the MVP and will
  be scoped separately.
- Language: The application will be English-only for the MVP.
- Out of Scope: As agreed, the MVP excludes direct sensor integration, 3rd-party system integrations ,
  and predictive maintenance AI.

# Post-project support

The client is welcome to request optional support and improvements once the project is completed.

## Support options

We offer several support options after the development is completed:

1. Allocation of a team for a certain number of hours per month, with a possible increase by agreement
   of the parties. E.g. 50 hours per month combined for all specialists. Response time is according to
   the signed SLA.
2. On-demand change requests. The client can request support or improvements at any point. In such a
   scenario Innowise will do its best to provide assistance as soon as possible, however, the response
   time period is not guaranteed (usually within 2-3 business days).

The option with an allocated team might be the following:

Team: Data Engineer (part-time), Project Manager (part-time).

Exact allocation to be determined after the project completion upon the client's request.

## Efficient Response Time and Incident Request Priority

Effective collaboration isn't just about communication; it's also about a swift and cost-effective
response. Our approach to determining the priority of Customer's Incident Requests and associated
response times ensures that you get the most value out of our support. Please find sample response
time schedule below:

| Category | Reaction time, business hours | Priority | Working Hours |
|---|---|---|---|
| Customer's request for an incident | 2 | High | Mon-Fri, 10:00 a.m. - 6:00 p.m. GMT+2 (9:00 a.m. - 5:00 p.m. UK time)* |
| Customer's request for an incident | 8 | Regular | |
| Request for information | 24 | Regular | |
| Urgent work | 2 | High | |

## Support pricing

If the client chooses the team allocation option, support fee is charged monthly based on the amount
of hours included in the support package.

On-demand support is billed on a per request basis, based on the amount of hours spent on fulfillment
of each particular request, at an hourly rate [a percentage removed] higher than with team allocation
option.

| Position | Rate, GBP/hour |
|---|---|
| Data Engineer (Senior) | [empty in the original] |
| Business Analyst | [empty in the original] |
| Data/BI Analyst | [empty in the original] |
| Project Manager | [empty in the original] |

## Comments in the original (internal)

- On the Desktop Engineer (.NET MAUI) role: Andrey Lapikov asked whether it is proposed separately
  from front and back end; a deleted account answered "Я бы получил здесь уточнение, так как сам не
  силен в бекенде".
- On "Step 3.6 (UX/UI): Implement the 'contextual hints'": Kira Barshchevich: the client answered
  "Yes (very much)!" to wizards, rules and hints; Andrey Lapikov: "Да, согласен. Добавим тогда как
  *Bonus*". In another thread on the same step, Lapikov: "я бы сказал, что это out of scope?"; the
  deleted account: "Пока да, думаю так, out of scope".
- On "HQ Management Portal": Lapikov: "То есть тут 100% Management portal будет web-based"; Aliaksei
  Sauta: "да, менджмент портал и UI для центрального офиса".
- On "Provide hyper-care support during the initial go-live period": Lapikov: "уточнить у PM,
  предполагается ли support после деплоя итд".
- On "PDF/CSV/Excel export capabilities": Lapikov asked where it came from; the answer quotes the call
  notes: "with the opportunity to export them in pdf, csv and xls formats".
- On "browser-based Web Application (ReactJS)": Lapikov wondered whether to make it optional; the
  deleted account: "Можно optional"; Lapikov: "мне кажется, что мы не можем это унести в совсем
  optional, так как это важные модули управления приложением".
- On "Offline Engines" and "Step 3.3 (Core Modules)": Lapikov and Barshchevich on which modules are
  core; no conclusion.
- On the platform deliverable: Sauta: "думаю да" (enough as the deliverable).
- On "ensuring 99.9% data integrity": Lapikov: "The question is how we define / promise this 99.9% of
  integrity or accuracy."
- On "Post-project support" and "Support pricing": "TBD by PrM/SM".
