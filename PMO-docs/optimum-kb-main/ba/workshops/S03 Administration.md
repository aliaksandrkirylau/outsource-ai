# S03 Administration

Session plan, topic 3, week 2. One hour. Part of [[00 discovery-BA-plan]]. Working material, not evidence.

## Elicitation goal

How users are managed, who approves corrections to saved entries, what the audit trail records, and
the permission matrix completed.

## Scope

- W2 users: WBS:Development Flutter!19
- W2 audit and edit approval: WBS:Development Flutter!21 (audit built in M6)
- [[REQ-006 Edit or backfill past entries with approval]], [[CAP-010 Audit trail and change approval]],
  [[CAP-001 Identity, roles and access]]

## Participants

Client: Mr. Lawal, a field supervisor, Ms. Zahra or Ms. Joud (IT). Ours: Anton, Leu.

## Preparation and inputs

- Prototype: users list and form (name, username, role, active), the approval queue (old and new
  value, the engineer's reason, approve or reject), the audit table (when, who, what, old and new,
  status).
- The permission matrix from S01, with the open rows marked.
- What S02 settled on assignment and on corrections.

## Agenda

| Min | Item | Fails without |
|---|---|---|
| 0-5 | Recap, goal | - |
| 5-15 | Users: who manages them, what a record holds | A1 |
| 15-35 | Corrections and approvals | B1, B2 |
| 35-45 | The audit trail | C1 |
| 45-55 | Walk the permission matrix; click through | Matrix rows agreed |
| 55-60 | Next steps | - |

## Questions register

Grouped by topic in agenda order; must-haves first. Blocks: the WBS line the answer is needed for, as its row in the WBS tab "Development Flutter" and a short name. When: Call, or Written after the session.

| ID | Question | Blocks | Must | When | Ahead | Source |
|---|---|---|---|---|---|---|
| | **A. Users** | | | | | |
| A1 | Who manages users, IT or operations? What does a user record need (name, username, role, active)? | 19 User accounts (web) | Yes | Call | Yes | Agent; Sheet W2 v0 |
| A2 | When an engineer leaves, is the account deactivated, never deleted? | - | - | Call | - | Agent |
| | **B. Corrections and approvals** | | | | | |
| B1 | Who approves corrections and backfills: the operations manager, an admin, or either? | 21 Audit and edit approval (web) | Yes | Call | Yes | Sheet W2 B1; [[REQ-006 Edit or backfill past entries with approval\|REQ-006]] |
| B2 | Does a correction wait for approval? What does an offline rig see meanwhile? (Behaviour to S08.) | 21 Audit and edit approval (web) | Yes | Call | Yes | Sheet W2 B1 |
| B3 | What happens to a report already sent when a correction is approved? (Detail in S06.) | - | - | Call | - | Sheet W5 B1 |
| | **C. Audit trail** | | | | | |
| C1 | Which actions must be logged, and who reads the log? (Estimated: up to 30 logged actions.) | 21 Audit and edit approval (web) | Yes | Call | Yes | Sheet W2 L |
| C2 | How long must the log be kept? Does ISO 9001 record control apply? | - | - | Call | Yes | Sheet W2 L; [[CON-008 Compliance with ISO 9001, ISO 14001 and API standards\|CON-008]] |
| C3 | Should anyone be able to export the log? | - | - | Written | - | Agent |
| | **D. For other topics** | | | | | |
| D1 | Where are low-stock levels set? (With S04.) | - | - | Written | - | Sheet W2 L |

Materials to request: the HQ user list (names and roles), who may approve corrections, the list of rigs (Sheet W2).

## Confirm with the client

| Ours | Plain wording |
|---|---|
| [[REQ-006 Edit or backfill past entries with approval]] | A saved check is locked; a correction goes to HQ for approval, with a reason. |
| [[REQ-004 Roles and what each role can do]] | The permission matrix as agreed here. |
| The limit | The audit trail records up to 30 kinds of action. |

## Outputs

- **Permission matrix completed** in [[REQ-004 Roles and what each role can do]]; sent with the written OK.
- KB: [[REQ-006 Edit or backfill past entries with approval]] updated; the audit limit written in.
