---
type: source
kind: rendering
date: 2025-10-29
original: "Questions.docx, sent by the client and posted in the presale chat on 2025-10-29 (spaces/AAQAMdfmWl4/messages/HpWQqfEXnEw.HpWQqfEXnEw)"
removed:
  - nothing; the document carries no amounts, personal data or credentials
---

# 2025-10-29 Client answers to the Q&A register - rendering

The client's answers, typed by the client into Innowise's question document and sent back on
2025-10-29. Verbatim from the returned Questions.docx, including its typos and the repeated phrase
in A1. Its two embedded images (the Innowise letterhead) are left out. Question 1 of Part 1 does
not exist in the original; the numbering starts at 2. Never edited after storing.

**Questions from Innowise to Optimum Engineering Standards**

| DOCUMENT INFORMATION | |
|---|---|
| DOCUMENT TITLE: | Q&A register |
| DATE: | October 24, 2025 |
| SECURITY: | Confidential |

This list of questions is designed to eliminate ambiguities, confirm the project boundaries, and
gather the specific details necessary to design the solution architecture and create an accurate
effort estimate.

The questions are separated into the two requested sections: Confirming Assumptions (validating
current scope understanding) and Open Questions (seeking new, missing, or detailed information).

## Part 1: Confirming Assumptions (Scope Validation)

These questions seek confirmation of information already stated or strongly implied in the initial
discussions and documents. Confirming these assumptions validates the foundational scope required
for the Minimum Viable Product (MVP).

| # | Assumption to Confirm | Answers |
|---|---|---|
| **I. Core Functionality** | | |
| 2. | Are the measurement parameters limited to less than 50, and are they manually inputted approximately 4 times per day? | Yes |
| 3. | Are the primary reports required for the MVP confirmed to be End-of-Day, End-of-Well, Engineering calculation/simulation, and Inventory reports? | Yes, including end-of-section reports. |
| 4. | Is it confirmed that Modeling/Calculation features do not require 3D models or complicated visualizations? | No |
| **II. Out-of-Scope Items (MVP)** | | |
| 5. | Is it confirmed that the following are out of scope for the MVP: Data collection from sensors, Integrations with other systems, API designing, Simulation for predicting equipment maintenance, and AI? | Yes. Unsure about API design. |
| 6. | Is the initial required application language confirmed to be English only? | Yes |
| 7. | Is the target user base approximately 70 locations (rigs/sites) with around two engineers working at each location? | Yes. But can potentially reach 100 based on market activity. Solution should be scalable. |
| **III. Architecture and Security** | | |
| 8. | Is the understanding correct that the system requires a centralized database for all locations? | Centralized dbase at the HQ not at each work location. Each work location should have local access to their own data. |
| 9. | Is it confirmed that the computers where the software will be deployed are shared among multiple engineers (1 to 4 people), as the computer is assigned to the rig site, not the individual? | Yes |

## Part 2: Open Questions (Gaps for Architecture and Estimation)

These questions address known gaps or require detailed specifications needed to make technology
choices, finalize the system design, and accurately estimate development complexity.

### A. Project Success & Platform Decision

| # | Open Question | Domain / Rationale | Answers |
|---|---|---|---|
| 1. | What are the top 3 outcomes or results you want in the first app release (e.g., better and faster operations, quick and available reporting, fewer data errors)? | Defines MVP success criteria. | 1. Must generate complete and accurate reports.<br>2. 99.9% data integrity and efficient synchrony between job sites and HQ server. between job sites and HQ server.<br>3. User friendly interface with low latency and minimal bugs. |
| 2. | Do you have any strict limitations that insist on using desktop and mobile applications instead of using web based universal solution? | Critical architectural decision point. | There are no strict limitations requiring the use of desktop or mobile applications. However, we need to consider that internet connectivity on rig sites may be unreliable. The application should ideally support offline access and functionality when there's no internet connection available. |

### B. Mobile Application Scope

| # | Open Question | Domain / Rationale | Answers |
|---|---|---|---|
| 3. | If a mobile application needed, should it duplicate all desktop functionalities or be limited to more narrowed list of features (like only data input). | Defines the scope of works | No, it should focus on the most essential tasks for users in the field, such as quick data entry, status checks, or basic reporting. |
| 4. | What devices should be supported for mobile applications? Are they limited to smartphones or tablets as well? | Defines technical support matrix. | iPhone and Android devices |

### C. Data Architecture, Availability, and Storage

| # | Open Question | Domain / Rationale | Answers |
|---|---|---|---|
| 5. | Given the need for a centralized DB but reluctance to depend solely on the cloud, where should the central server live, and how should remote sites connect? | Defines the hybrid deployment model and networking complexity. | Central server on-premises; remote sites use local caches with sync when connectivity allows. |
| 6. | Do you have the technical capability (staff and infrastructure) to deploy and maintain centralized services on-premises? | Determines viability of on-premises/hybrid solution. | No |
| 7. | Given that internet connection loss is an issue at some remote locations, what are the specific requirements for offline functionality and data synchronization? | Essential for designing the data persistence and replication layers. | Rigs should have local databases with automatic sync when internet is available. |
| 8. | What is the specific Data Retention policy for raw measurements, logs, and attachments (how many months/years should the data be stored)? | Impacts database sizing and archival strategy. | Between 1-2 years |
| 9. | If you plan to import historical Excel data, how big is this data pull expected to be (how many rows, GBs)? | Defines data migration effort. | Import data will not be Excel. Actual data format and size estimate to be confirmed later. |
| 10. | Could you please explain the master hierarchy that governs how data is organized (e.g., Company → Client → Field → Rig → Well/Project → Shift)? | Defines data modeling structure. | Data generation: On Job Site by field engineer.<br>Access to Report and System: Field Supervisors, Project Engineers, Operations Support, and Operations Manager.<br>Report Distribution: Client personnel, field supervisors and management. |

### D. User Management, Security, and Workflows

| # | Open Question | Domain / Rationale | Answers |
|---|---|---|---|
| 11. | For login, do you prefer device-level login (Windows) only, or lightweight in-app accounts per user/shift (recommended for information security)? | Defines security module complexity and architecture. | Prefer In-app accounts per user/shift but device level login is also acceptable. |
| 12. | Can we reuse an existing Identity Provider for managing authentication and Role-Based Access Management? | Determines integration complexity for user authentication. | Need further clarifications but probably not. |
| 13. | For each user role (site engineer, admin, supervisor, manager), could you please list example usage scenarios of what each role can do or see? | Defines precise permissions and access controls. | Mud Engineer: Enter measurements, perform calculations and simulations, generate reports and email reports to the supervisors<br>Supervisor: Review and generate reports<br>Manager: Access dashboards, oversee multiple sites<br>Admin: Manage users, roles, and system settings |
| 14. | Do supervisors or managers ever need to approve or lock entries (e.g., sign off end-of-shift or daily reports)? | Defines workflow needs and data immutability requirements. | No. Sign-off or approval only required for end-of-section or end-of-well reports. |
| 15. | Does the application need to support any other internal workflows (e.g., sending the report for a manager's or supervisor's review)? If yes, please clarify what workflows. | Defines workflow engine requirements. | Not at the moment. |
| 16. | Who will be responsible for administering users/roles and who will manage thresholds/templates within the application? | Defines administrative requirements and role responsibilities. | Authorized IT personnel. |
| 17. | Do client or customer details require masking or redaction in reports that are shared internally or externally? | Defines security and reporting sensitivity requirements. | Data masking/redaction feature not required. However, filtering of data for specific reports should be possible. |
| 18. | Given that English is the primary language, do you expect to extend support to other languages (e.g., Arabic) in further iterations? | Determines if internationalization must be built into the core architecture. | No |

### E. Detailed Feature Specification (Measurement, Inventory, Calculations)

| # | Open Question | Domain / Rationale | Answers |
|---|---|---|---|
| 19. | How do you currently set thresholds? Are thresholds global, per mud system, or per well/project? | Critical for designing the configuration module. | Kindly explain what you meant by "threshold". |
| 20. | When values surpass a threshold, what specific actions should happen (e.g., in-app highlight, require comment, block save, escalate to a supervisor)? Should supervisors receive notifications (email/SMS/mobile push)? | Defines alerting system requirements and complexity. | There should be different types of data control alerts. Examples:<br>1. Alerts to users to prevent wrong data entry.<br>2. Alerts to users to highlight critical parameters that are out of threshold.<br>3. Alerts to identify critical materials below minimum stock level |
| 21. | Should the app calculate derived values (e.g., density corrections) automatically on save? | Defines calculation engine needs. | Yes |
| 22. | Do Engineers backfill or edit past entries? If yes, who should be allowed to edit, and should they require a reason for that action? | Defines audit logging and data modification rules. | Backfill or edit feature required but subject to approval by operations manager and/or system admin. |
| 23. | Would you need to attach photos, files, or any important attachments to a measurement (e.g., lab sheets, calibration certificates)? | Defines file storage and attachment handling requirements. | Document upload required from HQ but accessible on the job site. |
| 24. | Describe your expectations from the inventory management part and what the current process looks like. | Defines the inventory module scope. | Tracks initial loadout, inflow, daily consumption, cumulative consumption per section and well, daily balance, product details (brand name, generic description, density, material #), products use concentration (in pounds/barrel & %) in the drilling fluid, expiration dates, product unit size, unit cost and total cost. |
| 25. | What inputs are specifically required in the Hydraulics/Simulation module (e.g., trajectory, BHA, bit type, pump rates, rheology)? | Defines the data required for the complex modeling features. | The well architecture/configuration (including casing size/depth, open hole size/depth, well survey data), drill string/BHA details, drilling fluids parameters (density, rheology etc), mud pump parameters, bit parameters, formation parameters (fracture pressure, pore pressure, bottom hole static/dynamic temperature etc). |
| 26. | Do you want guided wizards, sets of rules and hints, or checklists for new engineers and new app users? | Defines UI complexity for user onboarding/support features. | Yes (very much)! |

### F. Reporting and Dashboards

| # | Open Question | Domain / Rationale | Answers |
|---|---|---|---|
| 27. | Which KPIs are most important to monitor (e.g., barite sacks required, oil/water ratio changes)? | Defines dashboard and reporting focus. | 1. Tracking of critical mud parameter by depth & compared to offset wells.<br>2. Top 5 product consumption and general products use pie chart for current well section & cumulative for the well.<br>3. Fluids volume trend, cumulative mud loss and volume-out alert.<br>4. QHSE alerts: alerts on upcoming expirations of products, reagents, stock-outs, or equipment calibration.<br>5. Drilling progress status |
| 28. | What timeframe do you prefer to monitor data (per shift, daily, per well, fleet-wide across ~70 locations)? | Defines data aggregation and dashboard performance requirements. | Per 12-hour shift every operating day on all active locations (rigs). |
| 29. | Are you able to share any existing roadmap, high-level drafts, sketches, preferences, or examples of the desired outcome for the standard report types? | Provides critical visual requirements for reporting development. | See attached high level sample report for visual appreciation. Envisioned product is expected to be better designed, intuitive and detailed. |

## Innowise comments on the Google Doc copy (not the client's)

Kira Barshchevich copied the answers into the Innowise Google Doc on 2025-10-30 and left three
comments there. They are ours, not the client's.

- On A. 23 ("Document upload required from HQ but accessible on the job site."): "Need a list of the
  features requiring file upload."
- On A. 22 ("manager and/or system admin"): "Need to determine exact role of the approver."
- On A. 20 (alert types 1 and 2): "Need more details/examples to understand the difference (if there
  is any)."
