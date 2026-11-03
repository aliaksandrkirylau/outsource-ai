---
type: source
kind: rendering
date: 2025-10-24
original: https://docs.google.com/document/d/1Iw685h0d8EJ2NCetSxWNEXei46ggl20hZ8KSpiVv_RM
removed:
  - nothing; the architecture diagram image stays in the original
---

# 2025-10-24 Presale architecture - rendering

Google Doc "T1 - EST - Optimum Engineering Standards - ASnot - SA - Big data - 023690" by the presale
solution architect, Aliaksei Sauta (created 2025-10-24, last changed 2025-11-04). Verbatim; the
"Proposed solution" diagram is an image and is only in the original. Never edited after storing.

## Architecturally Significant Requirements (ASRs)

**Functional Requirements:**

- **Manual Data Input:** The system must provide a user interface for **manual input** of measurement
  and chemical analysis data taken from laboratory equipment on the rig site
- **Data Centralization:** The system must be able to centrally store and manage data generated from
  approximately **70 simultaneous job sites** (drilling rigs). Local data must be regularly
  stored/migrated to a **central database**
- **Complex Calculations & Simulations:** The software must include modules for basic engineering
  calculations (e.g., mud weight change, chemical additions) and more complex fluid hydraulics
  simulations for scenario analysis.
- **Comprehensive Reporting:** The system must generate Daily Reports and End of Job Reports , as well
  as specific reports (e.g., inventory, lab tools) with export options for PDF (standard) , CSV, and
  Excel.
- **Inventory Management:** The system must track and manage the inventory of drilling fluid, long list
  of chemicals/materials, and lab tools/equipment on the rig site.

### Non-Functional Requirements (NFRs):

- **Deployment / Connectivity:** A **desktop application** (Windows OS) is required for the field
  engineer on the job site. This is critical because many job sites are in **remote locations** with
  sketchy or no Internet access.
- **Data Integrity & Quality Control:** The software must be smart enough to include rule-based
  alerting/alarms and internal control mechanisms to prevent wrong data input and flag when parameters
  go outside the customer-defined range/specification.
- **Security & Confidentiality:** The data is considered confidential customer data. The client wants
  to avoid being totally dependent on 100% cloud-based solutions due to this concern.
- **User Access / Roles:** The system requires Role-Based Access Control for at least three user
  groups: Job Site Engineers (primary data input, similar rights) , Project Supervisors (QC/higher level
  things, responsible for multiple rigs) , and Management

**Proposed solution:**

[diagram in the original]

Components:

- **Local Windows DesktopApp MAUI** - A **cross-platform desktop application** (specifically targeting
  **Windows** as required) developed using **.NET MAUI** (Multi-platform App UI). This application
  provides the UI for data entry, complex engineering calculations, and report generation, designed to
  operate fully even without an internet connection.
- **Aggregation service** - A dedicated service responsible for handling and processing data
  transmissions from all the remote **Local Windows DesktopApp MAUI** instances. It manages the
  **synchronization** logic, ensuring data is received reliably, validated, and inserted/updated
  correctly into the central database. This addresses the challenge of moving data from many disparate
  local data stores to one central system.
- **Central-service** - The core business logic layer accessed by the Web application. It handles
  operations like complex report generation, rule-based alarming, advanced data analytics, and all
  necessary server-side data processing and business logic execution.
- **Identity provider** - A component that manages user authentication and authorization
  (login/access) for both the Web Application and the Aggregation Service. It enforces the
  **Role-Based Access Control (RBAC)** required for Engineers, Supervisors, and Management, ensuring
  users only access features and data appropriate for their role. Identity server or existing provider
  already hosted on premise
- **Web application** - The browser-based interface accessed by **Central office users** (Supervisors
  and Management). It allows for "real-time" viewing of aggregated site data, dashboards, QC, and
  overall project oversight.

Proposed stack:

- Backend service - .NET or Java
- Local client application - MAUI
- Central office web application - ReactJS
- Identity provider - ASP.NET Identity or Keylock

DataBases:

- Local storage for site clients SQLite - to keep data ready for server sync
- Central database PostgreSQL - supports materialized view for efficient reports building

## Comment in the original

On "Proposed solution:" - Marina Zaretskaya: "а мобильное приложение учиывали при проектировании
системы?" Aliaksei Sauta: "MAUI - кроссплатформенная платформа, приложения можно развренуть на
Android и IOS операционных системах".
