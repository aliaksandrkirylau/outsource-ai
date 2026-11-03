---
source: Innowise PMO Confluence, space PMO, "Minimal Required Project Management Framework > A. Project Initiation"
root_page: 4619206674
synced: 2026-09-24   # A02, A06, A07, A08, A10, A12 re-read live on 2026-09-24; the rest unchanged since 2026-07-17
maintainer: PM Copilot (refresh with the standards-sync skill)
---
# Standard A - Project Initiation: the step contract

This is the copilot's working copy of the control contract for each initiation step: what the step must produce, how it is verified, and the number it is measured by. It is a CACHE. The live Confluence pages are the source of truth. If a skill is about to produce a mandatory artifact or run a gate, and this file's `synced` date is more than a few weeks old, re-read the live page by ID before trusting it.

`[M]` marks an output the standard flags Mandatory.

## Read this before citing a step number to a PM

The overview table (page 4619206674) numbers the block A01-A14, and since about 22 Sep 2026 the detail-page titles agree with it: the contract review is A03 in the table itself. This copilot uses the same numbering. Still resolve a step by PAGE ID, never by title or number alone - the numbering has changed twice in three months.

Copilot releases before 0.45.0 used the old overview numbering: the contract review was "A02.5" and every code from A03 on was one lower than today (old A08 gate = A09 now, old A13 kick-off = A14). A PM's project-context.md, task list or older skill output may still carry the old codes - translate them by step NAME, never by number.

| Step | Live page title | Page ID |
|---|---|---|
| A01 Receive pre-sale handover and onboard | "A01. Receive pre-sale handover..." | 4619206688 |
| A02 Key actors, ownership, internal comms | "A02. Define External/Internal Stakeholders..." | 4619206702 |
| A03 Review final contract (see below) | "A03. Review final contract..." | 5142544653 |
| A04 Describe the project and define context | "A04. Describe the project..." | 4619206765 |
| A05 Validate scope, WBS estimates, approach | "A05. Validate pre-sale scope..." | 4619206785 |
| A06 Initial risks, dependencies, blockers | "A06. Identify initial risks..." | 4619206806 |
| A07 Roadmap, milestone schedule, resource plan | "A07. Create initial project roadmap..." | 4619207137 |
| A08 Calculate and validate initial economy | "A08. Calculate and validate..." | 4619206956 |
| A09 Validate baseline with stakeholders (GATE) | "A09. Validate project baseline..." | 4619206835 |
| A10 Staffing and team composition | "A10. Run staffing process..." | 4619206729 |
| A11 Set up the minimal PM system | "A11. Set up the minimal required..." | 4619207047 |
| A12 Align project team on start | "A12. Align project team..." | 4988764344 |
| A13 Prepare for client kick-off | "A13. Prepare for client kick-off..." | 4988633155 |
| A14 Kick off project | "A14. Kick off project" | 5015830531 |

In-text cross-references inside older pages may still use the previous numbering. Resolve any in-text step reference by its title, never by the number.

---

## A01. Receive pre-sale handover and onboard to the project context
Page 4619206688. Accountable: PM. When: at the start of initiation, once the PM is assigned.

Inputs: sales / pre-sale materials and the offer; client problem or pain point; contract / SOW / proposal where available; initial WBS / backlog / scope description; pre-sale estimates and assumptions; technical solution or architecture notes; client communication history and expectations; initial stakeholder contacts; known constraints, dependencies, commitments; an existing pre-sale knowledge container if one was made.

Outputs:
1. Collected Pre-sale Handover Package `[M]`
2. Pre-sale Handover Questions / Gaps List (where applicable)
3. Initial Project / Opportunity Context Summary WITH Client Problem Statement `[M]`
4. Source Materials / Links Register
5. Project NotebookLM / Knowledge Container created or updated `[M]`
6. Initial Assumptions and Commitments List `[M]`

Verification criteria:
- Client problem / pain point captured at a high level, or explicitly marked unclear.
- Handover materials collected, or the missing ones documented.
- Knowledge container created or confirmed, holding the available pre-sale material.
- Sold scope, key commitments, assumptions and constraints identified at a high level.
- Initial opportunity value captured where applicable.
- Initial estimates and source materials available for later validation.
- Open handover questions / gaps documented where applicable.
- The PM has enough context to move on to stakeholder, scope, estimate, risk and setup validation.

Control metrics:
- Pre-sale Handover Maturity Index = confirmed core handover areas / total relevant core areas x 100. Target >= 70% before deep scope and estimate validation.
- Critical Handover Uncertainty Ratio = material unresolved gaps / total relevant core areas x 100. Target <= 30% before formal project acceptance.

Escalation: request missing critical pre-sale material from Sales / Account / Pre-sale before detailed validation starts. Assign a clarification owner for unclear scope, timeline, budget or delivery commitments. A material sold-versus-deliverable mismatch is documented for A05 validation and A06 risk review. If the project is expected to start before critical gaps close, escalate per the governance model.

---

## A02. Identify key project actors, ownership roles, and internal communication channels
Page 4619206702. Accountable: PM. When: after initial context is received, before setup, communication planning and kick-off are finalised.

Inputs: pre-sale handover materials; internal Sales / Account / Delivery ownership info; expected involved departments; known client-side decision makers, Product Owners, approvers, operational contacts.

Outputs:
1. Stakeholder Register with key actors, ownership roles and gaps `[M]`
2. Internal Communication Channels
3. Stakeholder Power-Interest Grid (where useful for engagement planning)
4. Internal RACI Matrix (Sales / DM / Competency Center) `[M]` - internal only, never shared with the client. Feeds the RACI Matrix (Team + Stakeholders) at A12.

Verification criteria:
- Client-side key stakeholders identified.
- Client Sponsor / Business Owner defined or marked unknown.
- Product Owner / requirements owner defined or marked unknown.
- Final decision owners for scope, priorities, changes, acceptance, timeline, budget identified where applicable.
- Internal departments expected to supply people or expertise identified.
- Required internal communication channels identified, created, or confirmed as existing.
- PM added to the relevant internal chats.
- Required internal stakeholders added to chats, or missing participants documented.
- Internal management ownership defined or marked as a gap.
- Technical delivery ownership defined or marked as a gap.
- Actor / ownership gaps documented where applicable.
- Internal RACI Matrix (Sales / DM / Competency Center) prepared and shared in the accounting chat.

Control metrics:
- Client Decision Clarity Index = confirmed client-side decision areas / total relevant client-side decision areas x 100. Target 70-80% before kick-off. Unknowns are acceptable only if documented as clarification gaps.
- Internal Ownership Readiness Index = (confirmed internal ownership areas + explicitly not-applicable areas) / total relevant areas x 100. Required 100% before client kick-off.

Escalation: an unclear Product Owner / requirements owner / scope-priority decision owner must be clarified before scope is treated as stable. If the delivery department is unclear, clarify technical delivery ownership first, then with that owner decide which departments supply expertise, before resource planning and team appointment. Unresolved technical delivery ownership (DM / Tech Lead / Architect / Head of Department) blocks delivery start.

Chat set: Pre-sale, Contract, Common, Strategy, Accounting, Economy, Internal (where applicable).

---

## A03 Review final contract and confirm contractual baseline
Page 5142544653. Accountable: PM. When: after actors and channels are identified, before the project description, scope and estimate validation, roadmap, economy, staffing and kick-off.

It carries mandatory outputs and a hard confidentiality rule. Do not skip it silently.

Inputs: Contract Chat; the contract version agreed by the contract preparation group; the signed version received from Legal; pre-sale handover materials; proposal / commercial offer / SOW.

Outputs:
1. Contract Version Comparison Result `[M]`
2. Contractual Baseline Review Confirmation
3. Contract Discrepancy / Clarification Items `[M]` (where applicable)

Verification criteria:
- Contract review responsibility and the PM's access status are defined.
- The version agreed by the contract preparation group has been received.
- The agreed and signed versions have been compared.
- The comparison was done in a SEPARATE CONFIDENTIAL notebook or another approved assistant, NOT in the shared project NotebookLM.
- Project-related contractual commitments are understood at the level the PM needs.
- The review outcome is recorded in Contract Chat.
- Every discrepancy has an owner, a next action, and an escalation path.

Control metrics: TBD in the standard - none defined yet. Do not invent one; report it as not yet defined.

Escalation: contract versions must NEVER be uploaded to the shared project NotebookLM or any space the broader team can reach. A missing agreed-preparation version escalates to the contract preparation group plus Head PMO / Deputy Head PMO. Any signed-versus-agreed difference is an escalation case - never silently accept the signed version as the baseline. The signed version is requested through Head PMO / Deputy Head PMO, who requests it from Legal, separately from the preparation-group version. If the PM has no contract access (probation or other restriction), the assigned buddy / PM Lead / manager performs and confirms the review. Contractual obligations found here must flow into the project description, scope and estimate validation, risks, roadmap, economy, baseline validation and kick-off preparation.

COPILOT RULE: if this step is in play, the contract goes into a separate confidential container, never the project brain. Treat contract text with the same sensitivity as money.

---

## A04. Describe the project and define the project context
Page 4619206765. Accountable: PM. When: after initial context and key actors are identified.

Inputs: Initial Context Summary; Stakeholder Register; pre-sale handover materials; contract / SOW / proposal; client problem / pain point / opportunity trigger; sold scope and expected solution; client expectations and business goals; known assumptions, constraints, dependencies, commitments; strategic opportunity context.

Outputs:
1. Created / Updated Project Description with problem statement, goals, success criteria, constraints, assumptions and value context `[M]` (the only output for this step)

Verification criteria:
- Client problem / pain point documented, or marked unclear.
- Project goals and expected outcomes documented.
- Success criteria defined to a level sufficient for initiation.
- Key assumptions and constraints documented.
- Business / strategic value captured where applicable.
- The description can be used for scope, estimate, risk, roadmap, resource and economy validation.

Control metrics:
- Project Definition Maturity Index = confirmed core definition areas / total relevant core areas x 100. Target >= 80% before validation and roadmap planning. The standard fixes the denominator at these 8 areas: client problem / pain point, project goals, expected outcomes, high-level scope context, success criteria, key assumptions, key constraints, business / strategic value where applicable.
- Observable Success Criteria Ratio = success criteria with an observable outcome / total defined success criteria x 100. Target >= 70% before kick-off.

Escalation: unclear success criteria must be clarified before the roadmap, the acceptance approach and kick-off are finalised. Constraints that materially affect feasibility, budget, timeline, acceptance or value are documented for validation in the following steps. If business or strategic value is being used to justify a low-margin or risky project, that value must be documented explicitly before formal acceptance.

---

## A05. Validate pre-sale scope, WBS estimates, assumptions, and delivery approach
Page 4619206785. Accountable: PM. When: after the project description and context are prepared, before risks, roadmap, resources and economy are finalised.

Inputs: Initial Context Summary; Project Description; Stakeholder Register; pre-sale handover materials; contract / SOW / proposal; pre-sale WBS / backlog / scope description; pre-sale estimates and assumptions; technical solution / architecture notes; known constraints, commitments, dependencies, client expectations.

Outputs:
1. Required Project Roles List `[M]`
2. Validated WBS / Scope Baseline with high-level Acceptance Criteria and estimations `[M]`

Verification criteria:
- WBS reviewed against the expected project result AND the contractual delivery commitments.
- Required delivery work categories included, or documented as not applicable / missing.
- Critical scope has usable estimates, or the estimate gaps are documented.
- Estimates reviewed by relevant team members or technical experts.
- Delivery approach defined well enough for roadmap and resource planning.
- Material assumptions and unknown areas documented.
- Clarification, discovery, investigation or re-estimation needs have owners and next actions.

Control metrics:
- Critical Scope Estimate Coverage = critical scope areas with a usable estimate / total critical scope areas x 100. Target >= 80% before roadmap and resource planning. Count only project-level critical scope areas / workstreams identified in this step.

Explicit non-scope: this step does NOT validate profitability. Financial validation happens at A08, after the roadmap, timeline and preliminary resource plan exist.

Escalation: if the WBS does not cover what is needed to deliver the expected result, the missing work is added or documented before further baseline planning. Unreliable critical estimates trigger clarification, discovery, technical investigation or re-estimation. If the team concludes the sold scope cannot be delivered with the proposed approach, escalate to Delivery, Account, Sales and other relevant stakeholders. Significant estimate assumptions must stay visible into roadmap, resource, risk and economy planning. Any contractual delivery mismatch connects back to the contract review outcome (A03) and moves into risk / clarification management.

---

## A06. Identify initial risks, dependencies, blockers, and change gaps
Page 4619206806. Accountable: PM. When: after scope, estimates, assumptions and delivery approach are validated, before the roadmap, acceptance approach, resource plan and economy are finalised.

Inputs: Project Description; Stakeholder Register; the A05 validation summary; project-level critical scope view; high-level role / capability assumptions; delivery approach validation notes; documented scope / estimate / assumption gaps; re-estimation and clarification requests; contract / SOW; known client commitments, constraints, dependencies, expectations; technical solution / architecture notes.

Outputs:
1. Initial Risk Register `[M]`
2. Initial Issue / Blocker Log (where applicable)
3. Updated Assumptions / Constraints List (where applicable)
4. Opportunity & Internal Risk Register `[M]` - opportunities (upsell, scope expansion, reference / case-study potential, process improvement) and Innowise-internal-only risks (for example profitability). Never shared with the client.

Verification criteria:
- Initial risks affecting project start or delivery feasibility documented.
- Known issues and blockers documented where applicable.
- Critical dependencies documented with an owner or expected responsible side.
- Scope / budget / timeline / acceptance gaps that may need clarification or a CR identified.
- Material risks, blockers, dependencies and change gaps linked to the affected critical scope, goals, economy, roadmap, acceptance or stakeholder expectations.
- Critical items have an owner, a next action, or an escalation path.
- The records are usable for roadmap planning, resource planning, customer validation and formal acceptance.
- Opportunities and Innowise-internal-only risk items documented in the Opportunity & Internal Risk Register.

Control metrics:
- Critical Control Coverage = critical risks, blockers, dependencies and change gaps with owner AND next action / total critical items x 100. Target 100% before formal project acceptance. Count only items that can affect project start, critical scope, roadmap, resources, budget, acceptance, client expectations or formal acceptance.
- Critical Dependency Readiness Ratio = critical dependencies with a responsible side and expected action / total critical dependencies x 100. Target >= 90% before the roadmap and resource plan are finalised. Count only dependencies that can materially affect start or feasibility.

Response vocabulary the standard uses: accept, mitigate, clarify, escalate, transfer, defer, monitor, re-estimate, re-align.

Escalation: a critical issue or blocker that prevents roadmap planning, resource planning, economy calculation, customer validation or acceptance must be escalated before that step is called complete. Critical dependencies needing action from client, vendor, Sales, Account, Delivery, RM, Head of Department, Finance, Legal or a technical owner get a responsible side and expected action in the agreed channel. A scope / budget / timeline / acceptance gap that may change sold commitments is a clarification item or CR candidate and must NOT be silently absorbed into baseline scope. A material risk to profitability, contractual obligations, feasibility, the client relationship or strategic value goes to Head of PMO / Delivery management before formal acceptance.

---

## A07. Create initial project roadmap, milestone schedule, and preliminary resource plan
Page 4619207137. Accountable: PM. When: not filled in on the source page.

Inputs: pre-sale WBS / backlog / high-level critical scope; Project Description; Required Project Roles List; initial risk / issue / blocker / dependency records; contract / SOW / client commitments.

Outputs:
1. Milestone Timeline(s) / Project Schedule `[M]`
2. Preliminary Project Resource Plan `[M]`
3. Critical Path documentation `[M]` - Fixed-Price projects over 3,500h only

Verification criteria:
- Major milestones / phases defined.
- Critical project-level scope areas mapped to the roadmap or milestones.
- The resource plan shows required roles, seniority assumptions, approximate allocation and timing.
- Milestone timelines or the schedule show target dates or periods.
- Key dependencies, blockers, risks and constraints reflected as planning assumptions or timeline dependencies.
- Demo, review, UAT, acceptance testing or release validation checkpoints placed on the timeline where applicable.
- Required environment readiness points placed on the timeline where applicable.
- Required client inputs, approvals, access or decisions placed on the timeline where applicable.
- For Fixed-Price projects over 3,500h, the critical path is calculated and documented on the milestone timeline.

Control metrics:
- Critical Scope Roadmap Coverage = critical scope areas mapped to the roadmap / total critical scope areas x 100. Target 100% before resource planning and economy calculation.
- Resource Timeline Coverage = roadmap / milestone areas with a defined role, seniority, allocation and timing / total roadmap areas requiring delivery resources x 100. Target >= 90% before stakeholder baseline validation.
- Critical Path Coverage (large FP only) = critical-path activities identified and documented / total planned activities on the critical delivery chain x 100. Target 100% for Fixed-Price projects over 3,500h, before the milestone timeline is used as the planning baseline.

Role vocabulary: BA, SA, Architect, Tech Lead, FE, BE, QA, DevOps, Designer, Data, Mobile, ML, other.

Escalation: if critical scope cannot be placed into a realistic roadmap, clarify scope / timeline / delivery expectations before resource planning and economy are treated as reliable. A conflict between timeline assumptions and required roles, allocation, seniority or resource constraints forces a revision of the resource model or the timeline before baseline validation. Conflicts between target dates or milestone commitments and validated estimates, dependencies or constraints are documented and escalated before formal acceptance, as are delivery checkpoints, UAT periods and release validation points that cannot be placed. Critical environment readiness or client input needs a clarified responsible side and expected date before the roadmap becomes the planning baseline. Roadmap assumptions that materially affect profitability, feasibility, contractual commitments or client expectations must be reflected in the economy validation and in the PMO Head's acceptance decision.

---

## A08. Calculate and validate initial project economy
Page 4619206956. Accountable: PM. When: during initiation and initial planning.

Inputs: the initial roadmap; milestone timeline / schedule; preliminary resource plan; contract / SOW / budget / cap / expected revenue; average internal rates and cost assumptions provided through the approved economy calculation process; key resource, timeline and economy assumptions.

Outputs:
1. Initial Project Economy Calculation / Pre-Sale P&L `[M]`
2. Project Economy Validation Summary
3. Documented Economy Assumptions / Concerns `[M]` (where applicable)
4. EVM Baseline (Planned Value) `[M]` - Fixed-Price projects only. PV is normally a money figure: it lives with the economy, in the Sensitive folder, under the same rules.

Verification criteria:
- The calculation is prepared in the approved confidential economy file.
- It is based on the A07 roadmap, timeline and preliminary resource plan.
- Planned roles, seniority assumptions, locations where applicable, and planned hours are reflected.
- Average rates / cost assumptions are provided or validated through the approved process.
- Budget / cap / expected revenue is compared against estimated delivery cost.
- The result is visible as healthy, questionable, risky, negative, or acceptable only with strategic justification.
- Economy assumptions and concerns documented where applicable.
- The summary is ready for internal stakeholder validation WITHOUT exposing restricted financial detail outside approved channels.
- For Fixed-Price projects, an EVM Planned Value baseline is established against the milestone timeline.

Control metrics:
- Resource-to-Economy Coverage = resource plan role-periods included in the calculation / total required role-periods x 100. Target 100% before the summary is used for baseline validation.
- EVM Tracking (FP only): SPI = EV / PV and CPI = EV / AC, calculated and reviewed at every economy recalculation point (initial baseline, re-estimation, closure).

Hard confidentiality rules stated in the standard:
- The economy file is stored and shared only through the approved restricted location / Economy Chat. It is never stored or linked in the general project folder.
- Do not assign named people in the calculation unless already confirmed and required by the calculation logic.
- Do not share restricted profitability percentages or sensitive money detail outside approved channels.

Escalation: an economy below target, negative, or materially worse than pre-sale expectations escalates to Head of PMO / Delivery management before baseline validation completes. Low profitability justified by strategic value requires that reason documented before acceptance. Missing budget, revenue, rate, salary, location, contract or exchange-rate data must be provided or confirmed by the responsible owner before the result is treated as reliable. If the result depends on unrealistic staffing, seniority, allocation or unpaid-work assumptions, revise the roadmap, resource plan or baseline before validation. If the economy file leaks outside approved channels, correct access and communication immediately.

---

## A09. Validate project baseline with internal and external stakeholders (THE GATE)
Page 4619206835. Accountable: PM. When: during initiation and initial planning. This is the transition point - after A09 the baseline is approved or accepted with constraints, and only then does setup begin.

Inputs: Project Description; initial roadmap; milestone timeline / schedule; initial economy calculation / pre-sale P&L; initial risk / issue / blocker / dependency records; key assumptions, constraints, open alignment points; business / strategic / technical opportunity context.

Outputs:
1. Internal Stakeholder Validation Outcome `[M]`
2. Internal Project Value Classification, Rationale, and Value Extraction Hypothesis
3. Client Baseline Validation Outcome `[M]`

Verification criteria:
- Internal stakeholders reviewed the baseline and the outcome is documented as exactly one of: approved to continue / approved with constraints / requires rework / paused / rejected - not accepted.
- Value classification documented as one or a combination of: profit-oriented; marketing / reference / market-entry / client-development; technical or domain expertise acquisition.
- If profitability is weak, the non-financial value rationale is documented where applicable.
- If classified as marketing / reference / market-entry / client-development or technical / domain expertise acquisition, a value extraction hypothesis is documented where applicable.
- The client-facing delivery baseline is confirmed by the client, or documented as requiring clarification or rework.
- Client confirmation documented in the contract / SOW, email, meeting follow-up, or another agreed written channel.

Control metrics:
- Stakeholder Validation Coverage = baseline areas reviewed with the required stakeholders / total relevant baseline areas x 100. Target 100% before team appointment and full project setup.

Escalation: no internal go means no team appointment and no setup. A weak or negative economy proceeds only on a documented management decision or non-financial value rationale. An unconfirmed client baseline or material client objections must be clarified before team appointment and setup. Any open point touching critical scope, timeline, economy, client commitment or feasibility gets an owner and a next action in the action / escalation log.

---

## A10. Run staffing process and approve project team composition
Page 4619206729. Accountable: PM.

Inputs: baseline validation summary; preliminary resource plan; initial economy calculation / pre-sale P&L; milestone timeline / schedule; Required Project Roles List; staffing constraints, role requirements, seniority assumptions.

Prerequisite the staffing instruction imposes: the project P&L, the Staffing Master template, and the project Google Chat space with a webhook must exist before staffing starts.

Outputs:
1. Staffing Master / Staffing Run `[M]`
2. Confirmed Project Team Composition `[M]`
3. Updated Project Resource Plan `[M]`
4. Updated Project P&L / Economy Calculation with confirmed candidates `[M]`

Verification criteria:
- Staffing process launched and managed per the staffing instruction.
- Required roles, allocation, periods and seniority expectations reflected in the staffing request.
- Candidate profiles / CVs reviewed before approval.
- Candidate competence, seniority, availability, allocation, location constraints and project fit checked.
- A technical expert is involved where deep technical validation is required.
- Candidate cost, paid hours and allocation checked against the initial P&L.
- Confirmed composition reflected in the updated Resource Plan and the updated P&L.

Control metrics:
- Candidate Vetting Coverage = approved candidates with a documented profile / competence / cost review / total approved candidates x 100. Target > 80% before staffing closure.
- Staffing Data Update Coverage = approved candidates reflected in the Resource Plan and P&L / total approved candidates x 100. Target 100% before kick-off.
- Resource Plan Timeliness: the updated Project Resource Plan is finalised within 3 working days of staffing closure. Target 100%.

Escalation: an unstaffable mandatory role for critical scope escalates to RM / Head / Delivery management before kick-off. Candidates who do not match competence, seniority, location, allocation, availability or constraints must not be approved without clarification or explicit management acceptance. Material P&L, profitability, budget or feasibility impact must be cleared with RM / Head / internal management, and the Resource Plan and P&L updated before approval. If the PM cannot validate technical fit, involve a technical expert before approving.

---

## A11. Set up the minimal required project management system
Page 4619207047. Accountable: PM. When: during setup, after team composition is confirmed, before internal alignment, readiness review and kick-off.

Inputs: confirmed team composition; updated resource plan; updated P&L; Stakeholder Register; initial roadmap / milestone timeline; initial risk / issue / dependency records; project documentation and handover materials.

Outputs:
1. Project Card / PROREP updated `[M]`
2. Project Description created / updated `[M]`
3. Communication Plan draft prepared
4. Project Onboarding / Team Working Rules prepared
5. Project documentation and sensitive storage setup completed

Verification criteria:
- Required PM tools and documentation spaces created or confirmed.
- Sensitive storage created / verified per the relevant instruction.
- Jira / delivery tracking ready for project start.
- The PROREP card holds key project information, links and control artifacts.
- The Project Knowledge Container is created / updated with available materials.
- A Communication Plan draft is ready for internal review and client kick-off alignment.
- Project Onboarding / Team Working Rules prepared for the team.
- Required project chats, participants and pinned links verified per the relevant instruction.

Control metrics:
- Access and Link Readiness Coverage = required resources with verified access and links / total required resources x 100. Target 100% before readiness review, except documented pending external access.

Escalation: a missing tool, tracker, documentation space, sensitive folder or PROREP card must be created or assigned for resolution before kick-off. Sensitive information stored outside the approved location must be corrected immediately. Without Jira / delivery tracking the team must not start delivery work unless a temporary tracking approach is agreed. Missing chats, participants or pins must be completed before readiness review, or documented with an owner and a target date. Unclear onboarding or working rules must be clarified by the PM before internal team alignment.

Referenced instructions: Google Drive Structure; Atlassian / Jira setup; PROREP Project Card in Jira; "NotebookLM. Project Brain - how to build one (mandatory minimum)"; "Google Chats (How to use Internal)"; the Communication Plan description. The onboarding document link is `[Link TBD]` in the standard - a real gap, not a lookup failure.

---

## A12. Align project team on project start
Page 4988764344. Accountable: PM. When: during setup, after the PM system is prepared, before the readiness review and client kick-off.

Inputs: Project Description; confirmed team composition; updated resource plan; updated P&L; initial roadmap / milestone timeline; Communication Plan draft; Onboarding / Team Working Rules; initial risk / issue / dependency records; the PM system setup.

Outputs:
1. Internal Team Alignment Outcome
2. Team Feasibility Confirmation / Concerns `[M]`
3. Updated Communication Plan draft
4. RACI Matrix (Team + Stakeholders) `[M]` - built from the Stakeholder Register and A02's internal RACI; every participant reviews and confirms their role

Verification criteria:
- Internal alignment meeting(s) organised with the confirmed team.
- Team introduced to project context, baseline scope, roadmap, roles, working model.
- Team reviews the Communication Plan draft and gives input where needed.
- Team reviews scope / WBS / estimates against the available information.
- Team feasibility confirmation, or documented concerns, captured.
- Re-estimation, discovery, clarification or escalation needs documented where applicable.
- Open actions have an owner and a next step before the readiness review.
- RACI Matrix (Team + Stakeholders) prepared, and every listed participant has reviewed and confirmed their role.

Control metrics:
- Team Alignment Coverage = confirmed alignment areas / total required alignment areas x 100. Target 100% before the readiness review.
- RACI Acknowledgement Coverage = team members and stakeholders in the RACI who have reviewed and confirmed their role / total participants listed x 100. Target 100% before the readiness review.

Escalation: any team inability to confirm scope, estimates, timeline, budget, resource plan or delivery approach must be documented before the readiness review. A quick re-estimation from existing material is run by the PM before the readiness review; a larger re-estimation (team effort, client input, technical spike, separate discovery) needs effort, ownership, commercial impact and timing aligned with internal management and where needed the client. If the project cannot be delivered within current fixed scope / budget / timeline assumptions, the PM escalates before client kick-off and clarifies re-baselining versus discovery phase versus scope reduction versus CR versus T&M or iterative delivery. Unclear roles, working rules, PM system or communication expectations must be resolved or documented before the readiness review.

Delivery-process documents to assign scope owners for: Test Plan, Test Strategy, QA approach, Deployment Process, Release Management, Code Review rules, Definition of Done / Ready, environment rules.

---

## A13. Prepare for client kick-off
Page 4988633155. Accountable: PM. When: during setup, after internal alignment is complete, before the client kick-off.

Inputs: team feasibility confirmation / concerns; updated action and open-questions list; confirmed team composition; updated resource plan; updated P&L; initial roadmap / milestone timeline; the PM system setup; initial risk / issue / dependency records.

Outputs:
1. Kick-off Agenda / Materials `[M]`
2. Client-facing Process Alignment Topics
3. Client Kick-off Invite sent `[M]`

Verification criteria:
- Kick-off agenda prepared.
- Materials cover project context, team, roadmap, working model and next steps.
- Client-facing process topics prepared for discussion.
- UAT / acceptance, testing, release / deployment, environments and client-input topics prepared where applicable.
- The change request or budget control process is prepared according to the commercial model.
- Open questions and required client inputs documented.
- The invite is sent with the agenda and the required participants.

Control metrics:
- Kick-off Materials Coverage = prepared required kick-off topics / total required kick-off topics x 100. Target 100% before the invite is sent.

Commercial-model split: fixed price covers how scope changes, assumptions, out-of-scope requests and CR approval are handled. T&M covers how budget usage, burn rate, remaining budget and threshold notifications are communicated.

Escalation: if the agenda or materials are not ready enough to align expectations, postpone the invite. Internal uncertainty on client-facing process topics must be cleared with the team, technical owner, Account, Sales or Delivery before kick-off. UAT, acceptance, release, deployment, environment, CR or budget-control topics with commercial or contractual impact require Account / Sales / Delivery involvement before or during client alignment. A critical open question affecting scope, timeline, budget, acceptance or feasibility goes on the kick-off agenda or is escalated before the meeting.

---

## A14. Kick off project
Page 5015830531. Accountable: PM. When: during setup, after the agenda and materials are prepared and the invite is sent. A14 closes the A-block.

Inputs: kick-off agenda / materials; client-facing process alignment topics; initial roadmap / milestone timeline; onboarding / team working rules; initial risk / issue / dependency records; draft delivery process assumptions.

Outputs:
1. Kick-off Meeting Notes / Follow-up sent `[M]`
2. Updated Communication Plan
3. Updated Open Actions / Client Inputs List
4. Updated Project Documents

Verification criteria:
- Client kick-off conducted with the required participants.
- Project goals, roadmap, team setup and working model presented.
- Communication model and meeting cadence aligned with the client.
- UAT / acceptance, testing, release / deployment, environment and client-input topics discussed where applicable.
- CR process or budget control process aligned per the commercial model.
- Start agreements, open actions, owners and next steps documented.
- Relevant project documents updated where kick-off changed or confirmed the setup.

Control metrics:
- Kick-off Agreement Capture Coverage = kick-off agreement topics documented / total agreed or discussed topics x 100. Target 100% after the follow-up.
- Open Action Ownership Coverage = open kick-off actions with an owner and a next step / total open kick-off actions x 100. Target 100% after the follow-up.

Escalation: unconfirmed client assumptions, responsibilities, communication model, acceptance approach or delivery expectations are documented and assigned for follow-up. Any scope, timeline, budget, acceptance, environment or contractual mismatch surfaced at kick-off escalates to Account / Sales / Delivery management before it is absorbed into the delivery baseline. Client requests affecting scope, budget, timeline or assumptions go through the agreed CR or budget-control process. Missing client inputs, access, environments or decisions need an owner and a target date before delivery depends on them. Document updates required by kick-off agreements must land before the first delivery cycle counts as fully ready.

---

## Order and skipping

The standard says plainly: "It is appropriate to change the order of steps based on the project needs. Several steps can be done in parallel as well." Track outputs by EXISTENCE, not by marching A01 to A14.

The one hard sequencing rule: A09 is the gate. After A09 the baseline is approved or accepted with constraints, and only then does setup (A10 onward) begin.

Skipping is allowed but never silent. A skipped or thin step must carry a recorded justification.
