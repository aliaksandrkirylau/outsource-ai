# S07 Dashboards

Session plan, topic 7, week 4. One hour. Part of [[00 discovery-BA-plan]]. Working material, not evidence. Last on purpose: KPIs depend on what checks,
inventory and reports hold.

## Elicitation goal

The KPIs on each dashboard, how each is defined, and where targets come from.

## Scope

- D6 desktop dashboard: WBS:Development Flutter!56 (built in M6)
- W6 web dashboard: WBS:Development Flutter!31 (built in M5)
- [[REQ-011 Dashboards and KPIs]], [[CAP-009 Dashboards and KPIs]]

## Participants

Client: Mr. Lawal, a field supervisor, a mud engineer. Ours: Anton, Leu.

## Preparation and inputs

- KPI definitions and any management dashboards or Excel they use today; a mud program with target
  ranges and planned depths, if they have one.
- Prototype: both dashboards drawn from the agreed areas only; simple charts (bar, pie, x-y).
- Their five KPIs (Q&A F.27) listed against what the agreed areas can supply.

## Agenda

| Min | Item | Fails without |
|---|---|---|
| 0-5 | Recap, goal | - |
| 5-25 | HQ dashboard: KPIs and definitions | A1, C1 |
| 25-40 | Rig dashboard | B1 |
| 40-48 | Targets, and what is out | C2, C3 |
| 48-55 | Click through both | - |
| 55-60 | Next steps | - |

## Questions register

Grouped by topic in agenda order; must-haves first. Blocks: the WBS line the answer is needed for, as its row in the WBS tab "Development Flutter" and a short name. When: Call, or Written after the session.

| ID | Question | Blocks | Must | When | Ahead | Source |
|---|---|---|---|---|---|---|
| | **A. HQ dashboard** | | | | | |
| A1 | Which KPIs go on the fleet view, and which on the drill-down? | 31 Dashboard (web) | Yes | Call | - | Sheet W6 B1; [[REQ-011 Dashboards and KPIs\|REQ-011]] |
| A2 | Should rigs that have not synced for some hours be flagged? | - | - | Written | - | Sheet W6 L |
| A3 | How should 70 to 100 rigs be laid out? | - | - | Written | - | Sheet W6 L |
| A4 | How quickly must the dashboard open for all rigs? | - | - | Written | - | Client Q&A A.1 (NFR); [[CON-004 Scale and data volume\|CON-004]] |
| | **B. Rig dashboard** | | | | | |
| B1 | Which KPIs does an engineer need for his rig, compared with HQ? | 56 Dashboard (desktop) | Yes | Call | Yes | Sheet D6 B1 |
| B2 | What should the engineer see at the start of a shift: the dashboard, a well summary or today's mud checks? (Moved from S00.) | - | - | Call | - | Sheet D6 L |
| | **C. KPI definitions and targets** | | | | | |
| C1 | How do you define "critical mud parameter", "volume-out alert" and "drilling progress status"? (A KPI without data from an agreed area is extra scope.) | - | Yes | Call | Yes | Sheet W6 B1 |
| C2 | Where do targets come from: the mud program, planned depth or days? If the mud program, is it entered in the app? | - | Yes | Call | Yes | Sheet D6 B2 |
| C3 | Can we leave out offset-well comparison, since past wells are not imported? | - | Yes | Call | - | Sheet W6 B2; [[REQ-015 Import of historical data\|REQ-015]] |

Materials to request: KPI definitions, formulas and targets, a mud program with target ranges and planned depths, the charts they use today, current management dashboards or Excel, the list of critical parameters (sent ahead) (Sheet D6, W6).

## Confirm with the client

| Ours | Plain wording |
|---|---|
| [[REQ-011 Dashboards and KPIs]] | The KPIs on each dashboard are the numbered list agreed here, with simple charts. |
| The limit | No offset-well comparison in the first release. |

## Outputs

- KB: [[REQ-011 Dashboards and KPIs]] updated with the KPI list and definitions; sent for written OK.
