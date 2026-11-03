---
type: source
kind: rendering
date: 2026-09-25
original: https://docs.google.com/spreadsheets/d/10H7vDQCbev_-jC6y0J5zeCw1Os2n-6MfJiAVb0k2hbg
removed:
  - the company address and phone number in the tab headers
  - the "Estimate, USD" columns and the "Forecasted Cost (USD)" row, which hold only zeros or nothing
  - tabs not rendered - Total Estimation Development and Development MAUI (the MAUI estimate, link-only), Infrastructure Costs (money), Sheet11 (empty)
---

# 2026-09-25 v1 WBS - rendering

Google Sheet "v1 EST - Optimum Engineering Standards - ASnot - SA - Big data - 023690", read on
2026-09-28 as displayed values, with formulas checked where they explain a figure. Six of its ten tabs,
verbatim, typos kept. Rows are numbered as in the sheet; a column letter is the sheet's. "-" is in the
sheet; an empty cell is empty there. Line breaks inside a cell are shown as `<br>`. Never edited after
storing.

## Tab "Overview"

| Row | Cells |
|---|---|
| 5 | B5 Project Optimum Engineering Standards \| Estimate |
| 6 | B6 Project: · D6 Project_Name |
| 7 | B7 Platforms: · D7 Web application, Desktop application |
| 8 | B8 Programming Stack: · D8 Backend service - .NET or Java<br>Local client application - MAUI<br>Central office web application - ReactJS<br>Identity provider - ASP.NET Identity or Keylock<br>DataBases: <br>Local storage for site clients SQLite - to keep data ready for server sync<br>Central database PostgreSQL - supports materialized view for efficient reports building |
| 10 | B10 Development Team composition (FTE): · D10 Frontend Developer · E10 2 |
| 11 | D11 Backend Developer · E11 2 |
| 12 | D12 Business Analyst · E12 1 |
| 13 | D13 UI/UX Designer · E13 1 |
| 14 | D14 QA Engineer · E14 1 |
| 15 | D15 Project Manager · E15 0.5 |
| 16 | D16 DevOps · E16 0.5 |
| 17 | D17 Data engineer · E17 On demand |
| 19 | B19 Forecasted Timeline (months): · D19 Min · E19 Max |
| 20 | D20 4 months · E20 6 months |
| 22 to 23 | The forecasted cost row, left out: its two cells show zero placeholders |
| 25 | B25 The provided estimation displays possible, most likely hours and timelines of product development, and should not be considered as a commitment from the implementation team to meet these hours and timelines, as the software development lifecycle is a complex process and cannot be predicted with high accuracy. |
| 26 | B26 Created 05.07.2025 |

## Tab "Total Estimation Discovery"

Labels are in column A on this tab. Column D is headed "Rate, USD/hour" in the sheet, but its cells
are hours: each is the role's max plus 10 hours moved from "Other" for the P&L (the note under the
table). The "Estimate, USD" columns E and F are empty and left out.

| Row | A | B min | C max | D (hours, see above) | G Comments |
|---|---|---|---|---|---|
| 5 | | Estimate, hours | | | Comments |
| 6 | Total Estimation | min | max | | |
| 7 | Design UI/UX | | | | See breakdown on separate tab |
| 8 | PM | 30 | 40 | 50 | |
| 9 | BA | 120 | 120 | 130 | |
| 10 | UI/UX | 40 | 60 | 70 | |
| 11 | SA | 60 | 80 | 90 | |
| 12 | Other (on demand) | 20 | 40 | | |
| 13 | TOTAL | 270 | 340 | | |
| 22 | | | | 4,901 | |

- B13 and C13 sum rows 8 to 12. D8 to D11 are typed in, not calculated. D22 is the sum of D8 to D11
  plus the MAUI roll-up's TOTAL max (tab "Total Estimation Development", D28), so it is hours.
- Column D, from the contract chat ([[2025-11-25 Contract chat - rendering 1]]), 2025-11-28: Lizaveta Shauchenka asked about
  "странный" rate; Marina Zaretskaya: "это не рейт, это Яна для P&L раскинуа по 10 часов от other
  каждому", "у ПМ было 40 стало 50. у БА было 120 стало 130", and "под other мы предполашаем солянку
  из разрабов, которые буут оценивтаь новую вбс и модет придется кого-то на консалтинг в процессе
  дтскавери привлечь". The same thread: SA is "Solution Architect".

Notes beside the table, columns L to P:

| Row | L | N | O | P |
|---|---|---|---|---|
| 6 | SAD | 1 | 2 | 3 |
| 7 | vision and scope | onbording | confoirm draft | conform US for 2 sprints |
| 8 | detailed US for first 2 sprints | qa  | elaborate VS  | congorm vs |
| 9 | low fidelity designs | draft SAD | draft design | confriom designs |
| 10 | resource/budget/timeline plan  | draft VS | conf SAD | confrom project arts |
| 11 | detailed WBS | | | |
| 12 | | ui kit | | |

## Tab "Total Estimation Development Flutter"

The current estimate. Column E is headed "Rate, USD/hour" in the sheet, but its formula is the max
plus 15% (`=D11+D11*0.15`), so its cells are hours; the [Core] chat, 2026-09-25: "Тут есть еще один
столбец, в девелопменте. Это просто обычные часы + стабилизация". Column F, "VS React/MAUI", is the
MAUI roll-up's hours minus this tab's. The "Estimate, USD" columns G and H hold only zeros or nothing
and are left out.

| Row | B | C min | D max | E (hours, max + 15%) | F VS React/MAUI | I Comments |
|---|---|---|---|---|---|---|
| 6 | | Estimate, hours | | | VS React/MAUI | Comments |
| 7 | Total Estimation | min | max | | | |
| 8 | Design UI/UX | | | | | See breakdown on separate tab |
| 9 | Total design | 144 | 210 | | | The UI/UX Designer is responsible for mapping out the desired user experience in the form of wireframes and ensuring that the application meets the user needs. |
| 10 | Development | | | | | See breakdown on separate tabs |
| 11 | Back-end Development (web) | 479 | 595 | 684 | 0 | |
| 12 | Front-end Development (web) | 310 | 438 | 504 | 168 | |
| 13 | Back-end Development (desktop) | 252 | 325 | 374 | 0 | |
| 14 | Front-end Development (desktop) | 488 | 640 | 736 | 134 | 28 |
| 15 | Total Development | 1,529 | 1,998 | | 302 | |
| 16 | Quality Assurance | | | | | |
| 17 | Quality Assurance | 459 | 599 | | 91 | |
| 18 | Stabilization | 229 | 300 | | 45 | |
| 19 | Total Quality Assurance | 688 | 899 | | 136 | |
| 20 | Project management & Business Analysis | | | | | |
| 21 | PM Activities | 320 | 400 | | 0 | Budgeting, Planning of scope of work, Building Roadmap, JIRA setup and Tasks management, Project Processes Setup, Support internal and external communication, Risk Management, Delivery support, Scrum implementation, Monitoring Automation. |
| 22 | BA Activities | 382 | 499 | | -115 | Business analyst is in charge of understanding business needs, gathering requirements. Responsibilities include analyzing processes and fostering communication between stakeholders. |
| 23 | Total PM & BA | 702.25 | 899.45 | | | |
| 24 | DevOps | | | | | See breakdown on separate tab |
| 25 | DevOps | 168 | 232 | | | The DevOps Engineer is responsible for configuration and environments management, as well as the continuous integration/deployment process including automated builds, deployment, and test runs. |
| 26 | Architecture | | | | | See breakdown on separate tab |
| 27 | | 0 | 0 | | | accounted in discovery |
| 28 | TOTAL | 3,231 | 4,238 | | 323 | |
| 30 | timeline | 4 | 6 | | | |
| 32 | | 279 | 384 | | | |
| 33 | | 0.27 | 0.23 | | | |

How the figures are built (from the formulas):

- Total design (row 9): the MAUI tab's UI/UX MVP total minus 60 (`='Development MAUI'!M98-60`).
- Rows 11 to 14: the "Total MVP" row (98) of tab "Development Flutter": web back end from G and H,
  web front end from E and F, desktop back end from K and L, desktop front end from I and J.
- Quality Assurance: 30% of Total Development, rounded; Stabilization: 15%, rounded.
- PM Activities: 4 × 80 and 5 × 80. BA Activities: 25% of Total Development.
- DevOps: the DevOps tab's total (row 16).
- TOTAL: design + development + QA + PM and BA + DevOps.
- Rows 32 and 33 have no label: 279 and 384 are typed in (the BA columns of "Development Flutter"
  row 98), and row 33 is 1 minus each of them divided by the BA Activities figure.
- I14 holds the number 28 with no label.

## Tab "Development Flutter"

Columns: B Work Breakdown Item · C MLT for MVP · D MLT per feature · E, F Web FE Hours min, max · G, H
Web Back end Hours · I, J Desktop FE Hours · K, L Desktop Back end Hours · M, N UI\UX Hours · O, P BA
Hours · Q Stage (MVP) · R Comments.

| Row | Work Breakdown Item | C MLT for MVP | D MLT per feature | E Web FE min | F max | G Web BE min | H max | I Desktop FE min | J max | K Desktop BE min | L max | M UI/UX min | N max | O BA min | P max | Q MVP | R Comments |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | Base project setup | 95 | 95 | | | | | | | | | | | | | | |
| 6 | UI Kit | | | - | - | - | - | - | - | - | - | 10 | 12 | | | TRUE | |
| 7 | Project setup | | | 1 | 2 | 8 | 10 | 6 | 8 | - | - | - | - | 4 | 4 | TRUE | |
| 8 | Architecture | | | 2 | 4 | 12 | 14 | 6 | 8 | - | - | - | - | 0 | 0 | TRUE | |
| 9 | Base components and UI theme | | | 10 | 12 | - | 0 | 16 | 24 | - | - | - | - | 0 | 0 | TRUE | |
| 10 | DB structure setup | | | 4 | 6 | 10 | 12 | 6 | 8 | - | - | - | - | 0 | 0 | TRUE | |
| 11 | Localization | | | 1 | 2 | 6 | 8 | 4 | 6 | - | - | - | - | 0 | 0 | TRUE | |
| 12 | Role model | | | 12 | 14 | 8 | 10 | 20 | 24 | - | - | - | - | 6 | 8 | TRUE | Ability to manage system access permissions through assigning roles to the existing users. |
| 14 | **Project features** | | | | | | | | | | | | | | | | |
| 15 | **Web-Based Application** | | | | | | | | | | | | | | | | |
| 16 | Login/Logout | | | | | | | | | | | | | | | | |
| 17 | Authorization/Authentication | | | 6 | 8 | 24 | 32 | - | - | - | - | 6 | 8 | 8 | 12 | TRUE | Utilizing Identity provider (analogue - ASP.NET or Keylock). Supporting authentication flow for access to manage the superuser's unique oversight permissions and adapt the accessed UIs. |
| 18 | Admin panel | 0 | 68 | | | | 0 | | | | | | | | | | |
| 19 | Manage User Accounts | | | 20 | 24 | 6 | 8 | - | - | - | - | 12 | 14 | 18 | 24 | TRUE | Ability to CRUD user accounts. Includes assigning to one of the three required roles (Admin, Engineer, Supervisor/Manager). |
| 20 | Parameter Threshold Definition | | | 8 | 14 | 6 | 8 | - | - | - | - | 4 | 6 | 6 | 8 | TRUE | Ability to define threshold limits (minimum/maximum acceptable values) for each of the fluid parameters tracked. |
| 21 | Audit Logging & Modification Approval | | | 16 | 32 | 14 | 16 | - | - | - | - | 6 | 8 | 8 | 16 | TRUE | Ability to track all data entries edit/backfill actions (when, by whom and what was changed) and their approval status.<br>Up to 30 logged actions |
| 22 | Metric system customizing | | | 4 | 8 | 12 | 14 | - | - | - | - | 6 | 8 | 12 | 20 | TRUE | Choosing metric units used for measurements and the conversion of one unit of measurement into another, including validation rules. Assumption - 3 data sets. |
| 23 | Location Management (Optional) | | | 12 | 28 | 6 | 8 | - | - | - | - | 6 | 8 | 0 | 0 | FALSE | Ability to CRUD rig sites (locations) that are currently operable and available for selection within project. |
| 24 | Project Template Management (Optional) | | | 12 | 16 | 12 | 14 | - | - | - | - | 6 | 8 | 4 | 6 | FALSE | Template configuration form for project fields to pre-define and manage project structure and requirements (e.g., standard reports, required measurement frequency). |
| 25 | Project management | 41 | 41 | | | | | | | | | | | | | | |
| 26 | Manage projects | | | 24 | 28 | 10 | 12 | - | - | - | - | 10 | 12 | 12 | 16 | TRUE | CRUD project, assign/reassign engineers |
| 27 | Project details | | | 10 | 16 | 5 | 6 | - | - | - | - | 4 | 6 | 8 | 12 | TRUE | View list of projects, filter projects |
| 28 | Measurements | | | 8 | 12 | 14 | 16 | - | - | - | - | 4 | 6 | 6 | 8 | TRUE | View the raw measurement entries inputted by the Engineers (up to 50 parameters) |
| 29 | Quality Control  | | | 4 | 6 | 12 | 14 | - | - | - | - | 2 | 4 | 8 | 12 | TRUE | Feature focused on Quality Control (QC), allowing to easily see and review data streams from their assigned rigs with entries flagged for threshold violations highlighted. |
| 30 | Dashboard | 22 | 22 | | | | | | | | | | | | | | |
| 31 | Dashboard View | | | 14 | 16 | 36 | 48 | - | - | - | - | 8 | 10 | 8 | 12 | TRUE | Dashboard providing a high-level one-page snapshot of operational status, key KPIs, and progress against targets across multiple job sites. Includes filter and search for a particular project and visualization options (simple charts/graphs -  bar charts, pie charts, etc.). |
| 32 | Reporting  | 0 | 0 | | | | | | | | | | | | | | |
| 33 | Reports Approval Flow | | | 4 | 6 | 5 | 6 | - | - | - | - | 2 | 4 | 6 | 8 | TRUE | Function to formally 'Approve' or 'Lock' End-of-Section and End-of-Well reports generated by the Engineer. |
| 34 | End-of-Day Report Generation | | | 10 | 12 | 24 | 32 | - | - | - | - | 4 | 6 | 4 | 6 | TRUE | Ability to generate a standard End-of-Day Report. The report must be filterable and exportable to the PDF, CSV, XLXS  formats. |
| 35 | End-of-Section Report Generation | | | 4 | 6 | 24 | 32 | - | - | - | - | 4 | 6 | 4 | 6 | TRUE | Ability to generate a comprehensive End-of-Section Report. The report must be filterable and exportable to the PDF, CSV, XLXS  formats. |
| 36 | End-of-Well Report Generation | | | 4 | 6 | 32 | 40 | - | - | - | - | 4 | 6 | 4 | 6 | TRUE | Ability to generate a comprehensive End-of-Well report, summarizing all data, inventory, and simulation results collected throughout the duration of the project. The report must be filterable and exportable to the PDF, CSV, XLXS  formats. |
| 37 | Inventory Report Generation | | | 8 | 10 | 28 | 36 | - | - | - | - | 4 | 6 | 8 | 12 | TRUE | Ability to generate Inventory targeted report in desired file format, such as a summary of the current quantity, use trend, and cost for all materials at a selected rig site. The report must be filterable and exportable to the PDF, CSV, XLXS  formats. |
| 38 | Inventory Module | 170.9 | 1579.8 | | | | | | | | | | | | | | |
| 39 | Inventory Management | | | 24 | 28 | 12 | 14 | - | - | - | - | 12 | 14 | 8 | 12 | TRUE | Ability to CRUD products (chemicals, materials) used on the rig, including Brand Name, Material #, Unit Size, and Unit of Measure (UoM). |
| 40 | Stock Movements Log | | | 8 | 12 | 8 | 10 | - | - | - | - | 4 | 6 | 6 | 8 | TRUE | Ability to record key inventory events: Initial Loadout, Inflow (Received), Returned, and Lost. |
| 41 | Material Cost Linkage | | | | | 12 | 14 | - | - | - | - | - | - | 4 | 6 | TRUE | Logic to link consumption entries to a unit price from the provided Price List for internal (e.g., Daily Report) cost calculation. |
| 42 | Other | 17 | 17 | | | | | | | | | | | | | | |
| 45 | **Desktop Application** | | | | | | | | | | | | | | | | |
| 46 | Login/Logout | | | | | | | | | | | | | | | | |
| 47 | Authorization/Authentication | | | - | - | - | - | 12 | 16 | 12 | 16 | - | - | 1 | 2 | TRUE | Utilizing Identity provider (analogue - ASP.NET or Keylock). Supporting authentication flow for access to manage the superuser's unique oversight permissions and adapt the accessed UIs. |
| 48 | New User Onboarding | | | - | - | - | - | 16 | 24 | 4 | 5 | 8 | 10 | 4 | 6 | FALSE | A step-by-step tutorial or wizard for new users on how to enter daily data  (up to 10 promopts) |
| 49 | Project management | | | | | | | | | | | | | | | | |
| 50 | Project Setup & Management | | | - | - | - | - | 12 | 16 | - | - | - | - | 4 | 4 | TRUE | Ability to create a new (or select and update an existing) well/project entry and input the required details (location, client info, etc.) with project assigned active status and ID as a result. |
| 51 | Measurements input | | | - | - | - | - | 6 | 8 | 8 | 10 | 6 | 8 | 8 | 12 | TRUE | Ability to manually input and pre-validate the measured fluid parameters (e.g., density, viscosity) linked to the current shift and project. |
| 52 | Threshold Violation Alerting | | | - | - | - | - | 6 | 8 | 5 | 6 | 6 | 8 | 8 | 12 | TRUE | Visual highlight/notification of an inputted parameter value that surpasses a predefined threshold. The system should require to input a mandatory comment or reason before allowing the data to be saved with a 'flagged' status. |
| 53 | Contextual Input Guidance | | | - | - | - | - | 6 | 8 | 5 | 6 | 4 | 6 | 6 | 8 | TRUE | Contextual hints for specific fields during data entry, providing rules or acceptable ranges to prevent incorrect input (e.g., "Hint: Density must be between X and Y"). |
| 54 | Metric system customizing | | | - | - | - | - | 8 | 12 | 24 | 32 | 4 | 4 | 0 | 0 | TRUE | Choosing metric units used for measurements and the conversion of one unit of measurement into another, including validation rules. Assumption - 3 sets. |
| 55 | Dashboard | 0 | 6 | | | | | | | | | | | | | | |
| 56 | Dashboard View | | | - | - | - | - | 24 | 32 | 24 | 32 | 8 | 10 | 6 | 8 | TRUE | Dashboard providing a high-level operational status, key KPIs, and progress. Different form web app dashboard (simple charts/graphs -  bar charts, pie charts, etc.). |
| 57 | Calculations&Modelling | | | | | | | | | | | | | | | | |
| 58 | Derived Value Calculation | | | - | - | - | - | 12 | 16 | 12 | 14 | - | - | 4 | 6 | TRUE | Backend logic to automatically calculate derived values (e.g., density corrections) upon the Engineer saving the raw input data. |
| 59 | Standard Engineering Calculator | | | - | - | - | - | 48 | 56 | 48 | 64 | 8 | 10 | 4 | 6 | TRUE | Module allowing to run quick, standard engineering calculations (e.g., "How many bags of barite do I need to increase mud weight?") using a set of input variables (e.g., desired weight, current volume)  view formulas shared by the client |
| 60 | Simulation: Fluid Hydraulics | | | - | - | - | - | 80 | 88 | 56 | 72 | 12 | 14 | 4 | 6 | TRUE | Fluid hydraulics simulation/modeling module. UI form inputs include technical details like well architecture, rheology data, and flow rates. Output includes "what if" scenarios (e.g., impact of changing flow rates) with chart visualizations and data tables showing predictive outcomes. Charts are not complex (bar charts, curves x-y, etc.) - view materials shared by the client |
| 61 | Inventory  | 0 | 0 | | | | | | | | | | | | | | |
| 62 | Daily Consumption Log | | | - | - | - | - | 8 | 10 | - | - | 8 | 10 | 6 | 8 | TRUE | Ability for the Engineer to manually log the daily use or consumption of materials for the shift/day. |
| 63 | Stock Movements Log | | | - | - | - | - | 8 | 10 | - | - | - | - | 6 | 8 | TRUE | Ability to record key inventory events: Initial Loadout, Inflow (Received), Returned, and Lost. |
| 64 | Product Concentration Tracking | | | - | - | - | - | 8 | 10 | 5 | 6 | 6 | 8 | 6 | 8 | TRUE | Ability to input and track the Ending Concentration (e.g., lb/bbl) of specific mud components. |
| 65 | Low Stock Alerting | | | - | - | - | - | 10 | 16 | 5 | 6 | 4 | 6 | 4 | 6 | TRUE | Visual highlight/notification of remaining quantity of a material falling below a predefined low stock level. |
| 66 | Expiration Date Alerting | | | - | - | - | - | 10 | 16 | 5 | 6 | 4 | 6 | 4 | 6 | TRUE | Visual highlight/notification of material approaching or passed its expiration date. |
| 67 | Reporting | 0 | 9 | | | | | | | | | | | | | | |
| 68 | End-of-Day Report Generation | | | - | - | - | - | 16 | 20 | - | - | - | - | 1 | 1 | TRUE | Ability to generate a standard End-of-Day Report. The report must be filterable and exportable to the PDF/CSV/xlxs formats. |
| 69 | End-of-Section Report Generation | | | - | - | - | - | 14 | 18 | - | - | - | - | 1 | 1 | TRUE | Ability to generate a comprehensive End-of-Section Report. The report must be filterable and exportable to the PDF/CSV/xlxs formats. |
| 70 | End-of-Well Report Generation | | | - | - | - | - | 14 | 18 | - | - | - | - | 1 | 1 | TRUE | Ability to generate a comprehensive End-of-Well report, summarizing all data, inventory, and simulation results collected throughout the duration of the project. The report must be filterable and exportable to the PDF/CSV/xlxs formats. |
| 71 | Inventory Report Generation | | | - | - | - | - | 14 | 18 | - | - | - | - | 1 | 1 | TRUE | Ability to generate Inventory targeted report in desired file format, such as a summary of the current quantity, use trend, and cost for all materials at a selected rig site. The report must be filterable and exportable to the PDF/CSV/xlxs formats. |
| 72 | Other | 170.9 | 170.9 | | | | | | | | | | | | | | |
| 75 | **Mobile Application <br>[ note for developers - Desktop Features Adaption]<br>The app is using the same NET MAUI both for desktop and mobile - thats not development from scratch! Assume the most fucntions are implemented in desktop part not to estimate the efforts twice!!!!** | | | | | | | | | | | | | | | | |
| 76 | Login/Logout | | | | | | | | | | | | | | | | |
| 77 | Authorization/Authentication | | | - | - | - | - | 4 | 8 | - | - | 2 | 4 | 2 | 4 | FALSE | Utilizing Identity provider (analogue - ASP.NET or Keylock). Supporting authentication flow for access to manage the superuser's unique oversight permissions and adapt the accessed UIs. |
| 78 | Project | | | | | | | | | | | | | | | | |
| 79 | View project details  | | | - | - | - | - | 12 | 16 | - | - | 2 | 4 | 2 | 2 | FALSE | View main project details <br>Note: the feature mostly accounted in the desktop part! |
| 80 | Measurements input | | | - | - | - | - | 2 | 4 | - | - | 2 | 4 | 2 | 2 | FALSE | Ability to manually input and pre-validate the measured fluid parameters (e.g., density, viscosity) linked to the current shift and project.<br>Note: the feature mostly accounted in the desktop part! |
| 81 | Derived Value Calculation | | | - | - | - | - | 2 | 4 | - | - | | | 2 | 2 | FALSE | Backend logic to automatically calculate derived values (e.g., density corrections) upon the Engineer saving the raw input data. |
| 82 | Standard Engineering Calculator | | | - | - | - | - | 2 | 4 | - | - | 4 | 6 | 2 | 2 | FALSE | Module allowing to run quick, standard engineering calculations (e.g., "How many bags of barite do I need to increase mud weight?") using a set of input variables (e.g., desired weight, current volume)<br>Note: the feature mostly accounted in the desktop part! |
| 83 |  Inventory | | | | | | | | | | | | | | | | |
| 84 | Daily Consumption Log | | | - | - | - | - | 1 | 2 | - | - | 2 | 4 | 2 | 2 | FALSE | Ability for the Engineer to manually log the daily use or consumption of materials for the shift/day<br>Note: the feature mostly accounted in the desktop part! |
| 85 | Low Stock Alerting | | | - | - | - | - | 10 | 16 | - | - | 2 | 4 | 2 | 2 | FALSE | Visual highlight/notification of remaining quantity of a material falling below a predefined low stock level.<br>Note: the feature mostly accounted in the desktop part! |
| 86 | Expiration Date Alerting | | | - | - | - | - | 10 | 16 | - | - | 2 | 4 | 2 | 2 | FALSE | Visual highlight/notification of material approaching or passed its expiration date<br>Note: the feature mostly accounted in the desktop part! |
| 87 | Reporting | | | | | | | | | | | | | | | | |
| 88 | Basic Reports Overview | | | - | - | - | - | 32 | 40 | - | - | 2 | 4 | 2 | 4 | FALSE | A simplified, read-only view of the data entered for the selected reports (without file export option). |
| 90 | **General activities** | | | | | | | | | | | | | | | | |
| 91 | Unit Tests | 79.5 | 122.9 | 30 | 60 | 69 | 86.8 | 30 | 60 | 43 | 55 | - | - | | | TRUE | |
| 92 | Error States and loaders | 16 | 16 | 6 | 8 | 8 | 10 | 16 | 20 | - | - | 4 | 6 | | | TRUE | |
| 93 | Project Technical Documentation | 19 | 27 | 8 | 16 | 14 | 16 | 8 | 16 | - | - | - | - | | | TRUE | |
| 94 | Communication: Scrum (planning, daily, demo, retro), requirements clarifications | | | 60 | 70 | 60 | 70 | 60 | 70 | - | - | 24 | 32 | 56 | 64 | TRUE | The implementation effort presented also includes communication, as communication is inevitable, as individuals make up the team. Communication is the key to project success and the team members need to be involved in certain discussions, both planned and unplanned, among which are:<br>- Daily Meetigs<br>- Sprint Planning<br>- Sprint Review<br>- Retrospective<br>- Interteam communications (discussions on the matter of technical implementation, architectural choices, PR reviews, merge requests, as well as any meetings aimed at improving the processes, technical & project documentation, acquiring the understanding of the business part of the project)<br>- Agendas preparation and requirements collection |
| 97 | **Total Development** | | 2174.6 | 334 | 482 | 497 | 617 | 579 | 774 | 256 | 330 | 242 | 330 | 305 | 418 | | 2,213 |
| 98 | **Total MVP** | 631.3 | | 310 | 438 | 479 | 595 | 488 | 640 | 252 | 325 | 204 | 270 | 279 | 384 | | |
| 99 | | | | | | | | | | | | Total sum | | 3,295 | 4,319 | | |

Rows 1 to 4, 13, 43, 44, 73, 74, 89, 95 and 96 are empty or the header. How the totals are built
(from the formulas):

- Row 97 sums every line of each column (rows 6 to 94); row 98 sums only the lines with TRUE in column
  Q. The Flutter roll-up reads row 98, so FALSE lines are outside the estimate.
- R97 is the sum of the min columns of row 97.
- Row 99, "Total sum" (O99, P99): row 98's min and max columns plus four cells of the MAUI roll-up (tab
  "Total Estimation Development", rows 19, 21, 25 and 27: total QA, PM, DevOps, architecture).
- Unit Tests, web back end and desktop back end: 20% of the column's lines above.
- Columns C and D, "MLT" (not expanded in the sheet): at a group row, the average of the min and max
  sums of web FE, web BE and UI/UX over a range of rows. "Base project setup" and the general
  activities (rows 91 to 93) point at their own rows, "Admin panel" at its two optional lines only (23,
  24); the other groups point at other groups' rows or past the end of the tab (Project management at 51
  to 59, Inventory Module at 89 to 97, desktop Inventory at 105 to 113). Row 32 holds typed zeros.
  Nothing else in the sheet reads columns C and D.

## Tab "DevOps"

| Row | B Milestones | C Work Breakdown Item | D Short Description | E min | F max | G Comments |
|---|---|---|---|---|---|---|
| 3 | Milestones | Work Breakdown Item | Short Description | Hours | | Comments |
| 5 | | Development | | | | |
| 6 | Infrastructure as Code (IaC) Implementation | Infrastructure Code development/implementation | Write scripts to automate the provisioning of servers, databases, and other infrastructure components.<br>Ensure the infrastructure is easily reproducible and version-controlled.<br>Implement configuration management to maintain consistency across environments (e.g., development, production).<br>Ensure security best practices are followed during infrastructure setup, including access control, network security, and encryption. | 50 | 88 | It will take a minimum of 16–24 hours if we use ready-made Terraform modules for two to three environments.<br><br>OR<br>Optional. If we're creating a more flexible infrastructure as code (IaC) solution with advanced settings (security, networking and encryption), it will take 68–88 hours. |
| 8 | Setting Up the Development and Production Environments | Environment Configuration | Set up development and production environments on the chosen infrastructure. | 12 | 14 | |
| 9 | | Continuous Integration (CI) Setup | Implement CI pipelines using tools like Jenkins, GitLab CI, or similar for automated builds and testing.<br>Integrate with the version control system (e.g., Git) for code repository management. | 24 | 28 | |
| 10 | | Continuous Deployment (CD) Configuration | Establish CD pipelines for automated deployment of applications to staging and production environments. | 16 | 24 | |
| 11 | | Monitoring and Logging | Set up monitoring (e.g., CloudWatch metrics/alarms) for performance, health checks and to capture application and infrastructure logs.  | 10 | 16 | |
| 12 | Performance Optimization and Scaling Strategies | Load Balancing and Scalability | Implement load balancers to distribute traffic efficiently across multiple instances. | 10 | 14 | |
| 13 | | Backup and Disaster Recovery | Set up automated backup solutions for databases and critical data. | 10 | 12 | |
| 14 | Documentation, Training and ongoing support | Documentation of Processes | Create comprehensive documentation for deployment processes, CI/CD configurations, and infrastructure setups.<br><br>Ensure all configurations and scripts are well-documented for future reference.<br><br>Ensure knowledge transfer and support for the ongoing maintenance of the DevOps environment. | 16 | 16 | Optional. The team can work without documentation, but maintenance and development will be more challenging. If comprehensive documentation and instructions for future changes are required, an additional 16 hours will be needed. |
| 15 | Pre-release and Post Release (Stabilization Period Activitieis) | Provide the ongoing support, issues resolution and incident responses | Quickly resolve post-release issues and defects based on deployment logs, reports and metrics monitoring. | 20 | 20 | Optional. Adding post-launch support and troubleshooting (log monitoring and incident analysis) increases the time to 20 hours. Otherwise, the development team remains responsible for the first weeks after release. |
| 16 | | Total Development | | 168 | 232 | |

## Tab "Assumptions & Risks"

B6: "Project Optimum Engineering Standards  | Assumptions". The numbering skips 24.

| Row | No. | Assumption |
|---|---|---|
| 9 | 1 | This document provides a baseline estimate for the basic planning of the timeline and budget. To implement the project, Innowise provides the Client with a dedicated team |
| 10 | 2 | Changes in the composition and / or content of functional requirements, as well as the sequence of their implementation, can lead to a change in the timing and budget of the project. Any features that were not described in the documentation provided by the Client at the time of the evaluation, or that were changed during the project, shall be considered as Change Requests and are to be discussed, evaluated and agreed with the client separately. |
| 11 | 3 | At the time of preparing the estimate, the full requirements were not provided |
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

B34: "| Risks".

| Row | No. | Risk |
|---|---|---|
| 37 | 1 | Not clear requirements, especially related to the mobile app - medium |
| 38 | 2 | Absence of clear understanding the complexity of calculations and modelling modules - high |
| 39 | 3 | Scope creep duting the project implementation - medium |
| 40 | 4 | Uncertainty regarding the need for API design and development - medium |
| 41 | 5 | Absence of support from the client side (calculations and modelling) - high |
| 42 | 6 | Limited clients involment, delays with feedback - low |
| 43 | 7 | Potential gaps in user experience (UX) expectations - medium |
| 44 | 8 | Client infrastructure readiness - medium |
