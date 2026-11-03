---
type: source
kind: rendering
date: 2025-10-28
original: https://docs.google.com/spreadsheets/d/1odTylYDFxGsCINxhYBQH9zhdQOXkClo_pw2e1opah-Y
removed:
  - nothing; the sheet carries no hours, amounts or personal data
---

# 2025-10-28 BA draft WBS - rendering

Google Sheet "[draft] OES WBS" by Kira Barshchevich (created 2025-10-28, last changed 2025-11-03),
the presale BA's feature vision. All three tabs, verbatim, typos kept. Rows are numbered as in the
sheet. The Workshops tab is an unfilled checklist; its empty rows are kept. Never edited after
storing.

## Tab "WBS"

| Row | Product Features | Comment | |
|---|---|---|---|
| 2 | **Administration Module** | | |
| 3 | Manage User Accounts | UI to CRUD user accounts. Includes assigning to one of the three required roles (Admin, Engineer, Supervisor/Manager). | |
| 4 | Role-Based Access Control | UI to manage system access permissions through assigning roles to the existing users. | |
| 5 | Parameter Threshold Definition | UI to define threshold limits (minimum/maximum acceptable values) for each of the fluid parameters tracked. | |
| 6 | Audit Logging & Modification Approval | UI to track all data entries edit/backfill actions (when, by whom and what was changed) and their approval status. | |
| 7 | Data Synchronization Management | UI for monitoring synchronization of mobile / site-stored data with the HQ centralized database: last sync date, current status, sync errors and data conflicts log. | |
| 8 | Location Management | UI to CRUD rig sites (locations) that are currently operable and available for selection within project. | Optional |
| 9 | Project Template Management | Template configuration form for project fields to pre-define and manage project structure and requirements (e.g., standard reports, required measurement frequency). | Optional |
| 10 | Historical Data Import Utility | Utility to import existing historical data into the centralized database. | Optional |
| 11 | **On-Site Engineer Desktop App** | | |
| 12 | In-App User Login | Login screen uitilizing unique credentials to ensure that on the shared computer individual user activity is recorded for Engineers on different shifts. | |
| 13 | Project Setup & Management | Ability to create a new (or select and update an existing) well/project entry and input the required details (location, client info, etc.) with project assigned active status and ID as a result. | |
| 14 | Measurement: Manual Fluid Input [+Mobile] | UI to manually input and pre-validate the measured fluid parameters (e.g., density, viscosity) linked to the current shift and project. | |
| 15 | Measurement: Derived Value Calculation | Backend logic to automatically calculate derived values (e.g., density corrections) upon the Engineer saving the raw input data. | |
| 16 | Threshold Violation Alerting | Visual highlight/notification of an inputted parameter value that surpasses a predefined threshold. The system should require to input a mandatory comment or reason before allowing the data to be saved with a 'flagged' status. | |
| 17 | Standard Engineering Calculator [+Mobile] | Module allowing to run quick, standard engineering calculations (e.g., "How many bags of barite do I need to increase mud weight?") using a set of input variables (e.g., desired weight, current volume). | |
| 18 | Simulation: Fluid Hydraulics | Fluid hydraulics simulation/modeling module. UI form inputs include technical details like well architecture, rheology data, and flow rates. Output includes "what if" scenarios (e.g., impact of changing flow rates) with chart visualizations and data tables showing predictive outcomes | |
| 19 | New User Onboarding | A step-by-step tutorial or wizard for new users on how to enter daily data. | |
| 20 | Contextual Input Guidance | Contextual hints for specific fields during data entry, providing rules or acceptable ranges to prevent incorrect input (e.g., "Hint: Density must be between X and Y"). | |
| 21 | Offline Data Store [+Mobile] | A local data persistence layer within the Desktop/Mobile App to input and save data when the internet connection is poor or absent. | Architecture Solution |
| 22 | Data Synchronization Module | Logic to manage the synchronization of locally stored data with the centralized database once connectivity is restored. | Architecture Solution |
| 23 | **Supervisor/Manager Module** | | |
| 24 | Personal Account Login | Standard user authentication flow for access to manage the superior's unique oversight permissions and adapt the accessed UIs. | |
| 25 | Measurement Data | Read-only view on the Mobile App to view the raw measurement entries inputted by the Engineers across their assigned rigs/sites. | |
| 26 | Dashboard View | Dashboard UI providing a high-level one-page snapshot of operational status, key KPIs, and progress against targets across multiple job sites. Includes filter and search for a particular project and visualization options (charts/graphs). | |
| 27 | Quality Control Data Review | UI focused on Quality Control (QC), allowing to easily see and review data streams from their assigned rigs with entries flagged for threshold violations highlighted. | |
| 28 | Reports Approval Flow | Function to formally 'Approve' or 'Lock' End-of-Section and End-of-Well reports generated by the Engineer. | |
| 29 | **Inventory Module** | | |
| 30 | Inventory Management | UI to CRUD products (chemicals, materials) used on the rig, including Brand Name, Material #, Unit Size, and Unit of Measure (UoM). | |
| 31 | Stock Movements Log | UI to record key inventory events: Initial Loadout, Inflow (Received), Returned, and Lost. | |
| 32 | Daily Consumption Log [+Mobile] | UI for the Engineer to manually log the daily use or consumption of materials for the shift/day. | |
| 33 | Material Cost Linkage | Logic to link consumption entries to a unit price from the provided Price List for internal (e.g., Daily Report) cost calculation. | |
| 34 | Product Concentration Tracking | UI field and backend logic to input and track the Ending Concentration (e.g., lb/bbl) of specific mud components. | |
| 35 | Low Stock Alerting [+Mobile] | Visual highlight/notification of remaining quantity of a material falling below a predefined low stock level. | |
| 36 | Expiration Date Alerting [+Mobile] | Visual highlight/notification of material approaching or passed its expiration date. | |
| 37 | **Reporting Capabilities** | | |
| 38 | End-of-Day Report Generation | Ability to generate a standard End-of-Day Report. The report must be filterable and exportable to the PDF and CSV/Excel formats. | |
| 39 | End-of-Section Report Generation | Ability to generate a comprehensive End-of-Section Report. The report must be filterable and exportable to the PDF and CSV/Excel formats. | |
| 40 | End-of-Well Report Generation | Ability to generate a comprehensive End-of-Well report, summarizing all data, inventory, and simulation results collected throughout the duration of the project. The report must be filterable and exportable to the PDF and CSV/Excel formats. | |
| 41 | Inventory Report Generation | Ability to generate Inventory targeted report in desired file format, such as a summary of the current quantity, use trend, and cost for all materials at a selected rig site. The report must be filterable and exportable to the PDF and CSV/Excel formats. | |
| 42 | [Mobile] Basic Reports Overview | A simplified, read-only view of the data entered for the selected reports (without file export option). | |

## Tab "Workshops"

| Row | Workshop                         | Points to cover                                                                                                 |
| --- | -------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 2   | Kick-off & Detailed Scope Review | ☑ Establish key stakeholders and their roles, outline workshops schedule.<br>☑<br>☑<br>☑                        |
| 3   |                                  | ☑<br>☑<br>☑                                                                                                     |
| 4   |                                  | ☑<br>☑<br>☑                                                                                                     |
| 5   |                                  | ☑<br>☑<br>☑                                                                                                     |
| 6   |                                  | ☑<br>☑<br>☑                                                                                                     |
| 7   |                                  | ☑<br>☑<br>☑                                                                                                     |
| 8   |                                  | ☑<br>☑<br>☑                                                                                                     |
| 9   | Validation Meeting               | ☑ Walkthrough of final deliverables.<br>☑ Plan for testing and validating.<br>☑ Final checklist and next steps. |

## Tab "Artifacts"

| Row | Artifact | Description |
|---|---|---|
| 2 | Business Requirements Document (BRD) | This document captures the overall business goals, objectives, and the high-level needs of the project. It ensures all stakeholders have a shared understanding of the project scope. |
| 3 | Implementation Roadmap | A timeline that outlines the key milestones, development sprints, and delivery timelines for the project. |
| 4 | Use Case (could be diagrams) | Will help outline (or visualize) the interactions between users and the system, especially for functionalities like user authentication and onboarding. |
| 5 | User Stories + Acceptance Criteria | Short, actionable user stories that describe the features from the user's perspective.<br>For each user story, define clear acceptance criteria to determine if the feature has been successfully implemented. |
| 6 | Data Flow Diagrams (DFD) | A visual representation of how data flows through the system, particularly useful for understanding the interactions between mobile applications and the server-side components. |
| 7 | System Architecture Diagrams | A high-level overview of the system architecture to show how the different components of the digital platform, mobile app, and backend systems will interact. |
| 8 | Wireframes + Mockups | Visual representations of the user interface and app screens, especially for the mobile app and onboarding tutorial. |
| 9 | [optional] Test Cases + Test Plans | Based on the user stories and acceptance criteria, test cases will ensure that each feature functions as expected under different conditions. |
| 10 | [optional] Security and Compliance Documentation | Detailed documentation on the security standards for user authentication, such as encryption methods, data protection laws (GDPR, CCPA), and secure coding practices. |
