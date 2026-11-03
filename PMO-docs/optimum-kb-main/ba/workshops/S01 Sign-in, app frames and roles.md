# S01 Sign-in, app frames and roles

Session plan, topic 1, week 1. One hour. Part of [[00 discovery-BA-plan]]. Working material, not evidence. Milestone 2 builds these areas first, so
their written OK comes first.

## Elicitation goal

How people sign in at the rig and at HQ, what each role sees, and the first full draft of the role
and permission matrix.

## Scope

- D1 desktop sign-in and app frame: WBS:Development Flutter!47, !12 ([[REQ-003 Sign in on a shared rig computer]])
- W1 web sign-in and app frame: WBS:Development Flutter!17, !12 ([[REQ-004 Roles and what each role can do]])
- [[CAP-001 Identity, roles and access]]

## Participants

Client: Mr. Lawal, Ms. Zahra, Ms. Joud (IT, for accounts and passwords). Ours: Anton, Leu.

## Preparation and inputs

- Prototype: D1 and W1 in the chosen UI kit; three roles, four only behind a switch; sign-in as a
  plain form.
- A permission matrix draft: three roles × the SOW modules, from S00.
- What S00 said about users and the day.

## Agenda

| Min | Item | Fails without |
|---|---|---|
| 0-5 | Recap of S00, goal | - |
| 5-25 | Sign-in at the rig: accounts, offline, shift change | A1, A2, A3 |
| 25-45 | Roles: who sees what, walking the frames per role and the matrix draft | B1, B2, B3 |
| 45-55 | Click through D1 and W1 | Corrections noted |
| 55-60 | Next steps | - |

## Questions register

Grouped by topic in agenda order; must-haves first. Blocks: the WBS line the answer is needed for, as its row in the WBS tab "Development Flutter" and a short name. When: Call, or Written after the session.

| ID | Question | Blocks | Must | When | Ahead | Source |
|---|---|---|---|---|---|---|
| | **A. Sign-in at the rig** | | | | | |
| A1 | A personal account for each engineer, or one login per rig computer? (You said you prefer personal.) | 47 Sign-in (desktop) | Yes | Call | Yes | Sheet D1 B1; [[REQ-003 Sign in on a shared rig computer\|REQ-003]] |
| A2 | Can an engineer sign in offline on a computer he has never used? How do new accounts reach an offline rig? | 47 Sign-in (desktop) | Yes | Call | - | Sheet D1 B2 |
| A3 | At shift change, does the next engineer continue the same shift record or open a new one? Does signing out close the shift? | - | Yes | Call | - | Sheet D1 B3; [[TRM-002 Shift\|TRM-002]] |
| A4 | What screen size and resolution do the rig computers have? | - | - | Call | Yes | Sheet D1 B4 |
| A5 | May an engineer edit a colleague's entries? | - | - | Written | - | Sheet D1 L |
| A6 | Should a shared computer lock itself when idle? | - | - | Written | - | Sheet D1 L |
| A7 | Who resets a password at an offline rig? | - | - | Written | Yes | Sheet D1 L |
| A8 | Should the engineer see whether data has synced? | - | - | Written | - | Sheet D1 L |
| | **B. Roles and access** | | | | | |
| B1 | Are Supervisor and Manager one role or two? (Our baseline: three roles; a fourth is extra scope.) | 12 Role model; 19 User accounts (web) | Yes | Call | Yes | Sheet W1 B1; [[REQ-004 Roles and what each role can do\|REQ-004]] |
| B2 | Where do Field Supervisors, Project Engineers, Operations Support and the Operations Manager fit? Which of them will use the system? | - | Yes | Call | - | Sheet W1 B1 |
| B3 | Which roles see all rigs, and which only their assigned rigs? | 29 Quality control (web) | Yes | Call | - | Sheet W1 B2 |
| B4 | Does anyone at HQ enter data, or is the web only for viewing and managing? | - | - | Call | - | Agent |
| B5 | How many HQ users per role? | - | - | Written | - | Sheet W1 L |
| B6 | Do admins need two-factor sign-in? (Excluded in the SOW; the NCA rules may require it; for S08.) | - | - | Written | - | Sheet W1 L; [[CON-007 Saudi cybersecurity and data protection rules\|CON-007]] |
| B7 | Confirm that customers do not get access. | - | - | Written | - | Sheet W1 L |

Materials to request: the rig PC standard (OS, screen, domain, shared Windows account), a crew rotation for one rig, the IT password policy, the HQ org chart with roles and headcounts, the supervisor-to-rig mapping (sent ahead) (Sheet D1, W1).

## Confirm with the client

| Ours | Plain wording |
|---|---|
| [[REQ-003 Sign in on a shared rig computer]] | Every engineer has a personal account and signs in on the rig computer, also without internet once he has signed in there before. |
| [[REQ-004 Roles and what each role can do]], Version B | Three roles: Mud Engineer at the rig; Supervisor/Manager and Admin on the web. |

## Outputs

- **Permission matrix**, full draft (roles × screens and actions) into REQ-004; completed in S03.
- KB: [[REQ-003 Sign in on a shared rig computer]], [[REQ-004 Roles and what each role can do]]
  (the dispute settled or narrowed), [[TRM-002 Shift]].
