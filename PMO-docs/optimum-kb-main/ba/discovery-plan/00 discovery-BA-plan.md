# 00 Discovery BA plan

Leu Dorakhau's plan for the business analysis in Discovery (Milestone 1). Written by Leu's agent
(claude-code/claude-opus-5-5) on 2 November 2026. Working material, not evidence (`ba/AGENTS.md`).

## 1. Purpose

- Follows the kick-off deck ([[2026-10-18 Kick-off deck|kick-off deck]], "Discovery: How It Runs") and
  [[2026-10-13 Discovery plan - draft|Anton's Discovery plan]]; people and materials are in the [[2026-10-29 PM handover|PM handover]].
- This file is the plan and changes rarely. Working artefacts: [[01 discovery-tracker]] (sessions,
  readiness, weekly log), [[02 discovery-change-requests]] (register, impact assessments, no money), and the session plans S00-S08 in `ba/workshops/` (section 3), whose questions come from the
  [[2026-10-13 Discovery question sheets - draft|question sheets]] (handover record).

## 2. Business analysis approach

- **Prototype-led, per topic** ([[DEC-010 Confirm the product with the client through prototypes in code|DEC-010]], [[DEC-015 Discovery - our own picture of the system, questions as if from scratch|DEC-015]]): bring our picture as a prototype, ask as if from scratch.
- **As simple as possible** (fixed price): the smallest version that meets each WBS line; where a screen must pick an option, the estimated one; structure, not answers to open questions. Anything bigger is not drawn ([[K-5 Scope grows through the prototypes|K-5]]).
- **One hour, one topic per session**, as the deck told the client; a second session only if the e-mail round fails.
- **Questions from the client's own material**, not generic banks.

## 3. Elicitation and collaboration

| Wk  | Session                                                                                                                                           | Areas                           |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| 1   | Kick-off (Anton)                                                                                                                                  | -                               |
| 1   | [[S00 Vision and UI kit]]                                                                                                                         | Users, the day; UI kit          |
| 1   | [[S01 Sign-in, app frames and roles]]                                                                                                             | D1, W1                          |
| 2   | [[S02 Well job, mud checks and QC]]                                                                                                               | D2, W3, W2 thresholds and units |
| 2   | [[S03 Administration]]                                                                                                                            | W2 users, approvals, audit      |
| 3   | [[S04 Inventory]]                                                                                                                                 | D4, W4                          |
| 3   | [[S05 Calculations and hydraulics]]                                                                                                               | D3                              |
| 3   | [[S08 Technical session]] (Tech Lead or Arseniy)                                                                                                  | X1-X3                           |
| 4   | [[S06 Reports and approval]]                                                                                                                      | D5, W5                          |
| 4   | [[S07 Dashboards]]                                                                                                                                | D6, W6                          |
| 5   | Buffer: topics without an OK carry on beside the build ([[DEC-011 Move scope between milestones and start building in the first month\|DEC-011]]) | -                               |

Fallback: no formula set by the end of week 2, S05 swaps with S06.

Each session:

1. **Prepare for workshop**, 2-3 days before: refresh the session plan from the KB (`procedures/workshop-prep.md`); my prototype v0; prepare the questions in advance: the open questions already on the topic (the session plan's register, open Questions in `index.md`) and my own that came up while preparing, added to the register; send the top five ahead; chase the inputs.
2. **Conduct workshop**, 60 minutes: log asks beyond scope; never agree, price or refuse in the room.
3. **Confirm results**, same day: ingest (`procedures/ingest.md`); open questions in writing (`procedures/export.md`), due in three business days ([[COM-007 Client answers clarifications within three business days|COM-007]]); new change request entries raised with Anton and Mikhail.
4. **Communicate**: the revised prototype goes to the client to click through.
5. **Approve**: written OK by e-mail, then the area's backlog.

## 4. Requirements and designs: deliverables and approval

My share of the Milestone 1 deliverables in the SOW ([[COM-020 Milestone plan and deliverables|COM-020]]), plus the two models acceptance depends on. I own the requirements; Anton is accountable (RACI row 8).

| Deliverable | Holds | When | Lives in | Approved by |
| --- | --- | --- | --- | --- |
| Vision & Scope (M1) | Vision, goals, success criteria ("99.9% data integrity", "complete and accurate reports" made checkable); scope in and out; assumptions, constraints, limits; key risks ([[K-5 Scope grows through the prototypes\|K-5]], [[K-10 Fixed price with vague acceptance criteria\|K-10]]); high-level requirements | Outline wk 2, draft wk 4, final wk 5 | Draft: [[vision-and-scope]] in `ba/artefacts/`. Final: open, the KB or the client-facing space ([[2026-10-14 Generated documents as sources - options\|decision 5]]) | The client, in writing ([[COM-002 Written acceptance of each deliverable\|COM-002]]) |
| Validated backlog (M1, in the V&S) | User stories with high-level acceptance criteria per agreed area | After each written OK | With the V&S | With the V&S |
| Main UI/UX mockups (M1) | One prototype per area, D1-D6, W1-W6 | 2-3 days after each session | `ba/prototypes/`; one master; inputs: Anton's v0 ([[2026-10-30 Prototype canvas export\|canvas export]]) and Mikhail's [[OE prototype - read me\|OE prototype]]; fictional data | Before the client sees it: me (I own the prototypes), Anton reviews. Each area: Mr. Lawal or a named stand-in, written OK by e-mail ([[COM-018 Written minutes, notices and amendments\|COM-018]]) |
| UI Kit (M1) | Three options | Confirmed wk 1 | `ba/prototypes/ui-kit/` | Mr. Lawal chooses one ([[DEC-017 Choose the UI kit with the client from three variants\|DEC-017]]), confirmed in writing |
| Role and permission matrix | Roles × screens and actions; REQ-004's acceptance measure | Draft wk 1, agreed wk 2 | [[REQ-004 Roles and what each role can do\|REQ-004]] | With the S01 and S03 written OKs |
| Calculation specification | Numbered list, inputs, outputs, units, source, worked examples, tolerance, sign-off ([[CON-003 Correct calculations\|CON-003]], [[K-2 Losses from a calculation defect fall on us\|K-2]]) | Wk 3 | [[REQ-007 Derived values and standard calculations\|REQ-007]], [[REQ-008 Fluid hydraulics simulation\|REQ-008]] | How far we check: Mikhail and Kavalchuk, a Decision before S05. Test cases: the client's named signer |
| Input to the revised WBS (PMs own it) | Our minimal version against each client ask | Wk 4 | [[02 discovery-change-requests]] | Absorb, change request or scope revisit: Anton and Mikhail ([[COM-005 Change requests\|COM-005]]) |
| Input to the architecture (Tech Lead owns it) | Agreed flows, roles, data, limits; S08 answers | Wk 3-4 | To the Tech Lead | - |
| Non-functional requirements (Tech Lead owns them) | The business side: the client's top three as measures (S00), integrity, report and dashboard speed (S02, S06, S07); the technical side is the Tech Lead's questionnaire in S08 | Wk 1-3 | [[nfrs]] in `ba/artefacts/`; agreed measures in the Concern notes and the V&S | The Tech Lead (Concerns); the client with the V&S |
| Requirements, Questions, Terms | Updated after every session | Continuous | `knowledge/`, per `schema/types.md` | Per `schema/types.md` |
| Diagrams | Process flows, data model, lifecycles, system context | When a session shows something the prototype and notes cannot carry | `ba/artefacts/` ([[diagrams\|index]]) | With the area they belong to |


Prioritisation: the MVP is the WBS lines marked TRUE, ordered by the milestone that builds them; S01 first because Milestone 2 builds it.

## 5. Stakeholder engagement

Who is who: the PM handover and [[COM-008 Client cooperation and dependencies|COM-008]].

| Who | Influence / interest | How I engage them |
|---|---|---|
| Mr. Lawal, sponsor and subject expert | High / high | Short, visual sessions when available; decisions put plainly; a modern tool ([[CON-005 Easy and responsive interface\|CON-005]]); his ISO and API expectations heard ([[CON-008 Compliance with ISO 9001, ISO 14001 and API standards\|CON-008]]) |
| Ms. Zahra, Ms. Joud, day-to-day | Medium / high | One inputs list per session, with dates; written questions; IT for S08 |
| A mud engineer, a field supervisor (to be named) | Low / high | S02, S04, S05, S06; questions about their real day |
| Anton, PM | High / high | Daily; weekly review; sends everything to the client |
| Mikhail, Lead PM | High / high | Scope questions, before the client hears about them |
| Arseniy, DM; the Tech Lead when staffed | High / high | UI kit libraries; S08; architecture input |
