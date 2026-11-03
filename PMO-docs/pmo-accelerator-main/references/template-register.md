---
source: Innowise PMO Confluence space PMO (multiple pages) + PMO Drive templates
synced: 2026-07-27
maintainer: PM Copilot (refresh with the standards-sync skill)
---
# Template register - what exists, where it lives, which step needs it

The point of this file: a PM should never have to know where the template is. When a skill is about to produce an artifact, it looks the artifact up here and tells the PM which template to copy, or that there is no template and we are drafting from the format spec.

Confluence pages resolve as `https://innowise-group.atlassian.net/wiki/spaces/PMO/pages/<id>`.
Sheets resolve as `https://docs.google.com/spreadsheets/d/<id>`.

Kind legend: FILL = a real fillable template to copy. SPEC = a format description, draft against it. EXAMPLE = a worked instance, not a blank. REQUEST = issued by a person, not self-serve.

## A01 - handover

| What | Kind | Where |
|---|---|---|
| Checklist: Acceptance From Pre-sale | FILL | Confluence 3285712947 (page is marked `[DRAFT]`) |
| Mandatory materials for contract (filled by DM) | FILL | Sheet `1IkVpQPPc-TzImiis0kAi_vgXLzSSo-0opDvUhjIW8tc`. PMO will not proceed with the contract without it |
| NotebookLM Project Brain - mandatory minimum | SPEC | Confluence 4955406559 - steps, mandatory source list, custom-instruction snippet |
| Google Drive Structure (PMO Private / PMO Sensitive) | SPEC | Confluence 5257166927 (instruction), 5257167110 (structure description), 5262049359 (Project Folder Structure Template) |
| Assumptions examples | EXAMPLE | Confluence 3324805284 + Sheet `1BSsIvN9AlgmQmjDyGpDA43yAt4_chZwI8zREvO8wJkA` |

Caveat: A01 in the standard cites "Checklist: Acceptance From Pre-sale v2". Only the v1 `[DRAFT]` page exists. The copilot's bundled rubric (`skills/a01-presale-handover/references/acceptance-checklist.md`) is derived from 3285712947. If a PM asks, say it is our derived rubric based on that page, not an official v2.

## A02 - actors, ownership, channels

| What | Kind | Where |
|---|---|---|
| Stakeholder Register Template | FILL | Confluence 2900164811 - Customer team + Innowise team tables, embedded in Confluence |
| Stakeholder Register (power / interest grid) | SPEC | Confluence 2882175845 |
| RACI Matrix | FILL | Confluence 5057675462 + Sheet `1cd95PYsEZDfhtSImD7RXNeEp_kkI7uj-XvXGOu-TdX8` (16-process reference matrix pre-filled). Page marked `[Draft]` |
| Project Roles / Roles and Responsibilities | SPEC | Confluence 3349938278, 3345449006, 3813507250, 3994320921 |
| Google Chats (How to use Internal) | SPEC | Confluence 3006398548 - 8 chat types and their required pins |

## A03 - contract review

| What | Kind | Where |
|---|---|---|
| Contract review step | SPEC | Confluence 5142544653 |
| Contracts and Legal Processes | SPEC | Confluence PMO space, search "Contracts and Legal Processes" |

No template. The output is a comparison result recorded in Contract Chat. Remember the confidentiality rule: the comparison happens in a SEPARATE confidential notebook, never the shared project brain.

## A04 - project description

| What | Kind | Where |
|---|---|---|
| Project Description template | FILL | Confluence 2886959244 - skeleton with placeholders. Page marked `[Need Update]` |
| Project Scope Document / Project Charter | EXAMPLE | Confluence 3802267838 - a filled Beauty Affairs instance, NOT a blank |
| Project Management Plan | FILL | Confluence 2114289665 - revision history, scope, deliverables, milestones, DoR/DoD, comms, lifecycle, QA. Page marked `[Update]` |

## A05 - scope and estimate validation

| What | Kind | Where |
|---|---|---|
| WBS Detailed Template (Outsource / Fixed Price, Min-Max) | FILL | Sheet `19P47nYbey6oKLuXfEeb8bojojrmTfxPO2aYotTa9Hp4`, via Confluence 2882733190. 6 tabs, Jira-import ready |
| WBS Optimised (Solution Request, Min-Max) | FILL | Sheet `12B4wRsuI_aEmttlcZN3mMtK5t6dk3Ot3ikBNtQRDX3k`. 6 tabs |
| Assumptions examples | EXAMPLE | Confluence 3324805284 |

High-Level Critical Scope with Acceptance Criteria is a mandatory standalone artifact with no dedicated format - it is currently reachable only through the WBS templates. Draft it as its own Confluence section: scope area, observable acceptance criterion, estimate, estimate confidence.

## A06 - risks

| What | Kind | Where |
|---|---|---|
| Risk Register | EXAMPLE | Confluence 2991947807 (PromoveTM). No blank template exists |
| Project Management Risk Framework | SPEC | Confluence 2992373795 |
| Risk response strategies | SPEC | Confluence 2118385704 |
| Risk Library | REFERENCE | Confluence PMO space, search "Risk Library". A large catalogue of known risks - use it to prompt for risks the PM has not thought of. Not bundled; it is too large and changes often |
| Issue Log Template (Master File) | FILL | Confluence 5057020108 + Sheet `16Dl5Y1Tda6Rp8TIp5Ai8S2YHzQG8skPAskmsvQb_ZAg`; usage guide 4907630743. 3 tabs (Business / Project / Customer). Stored in the Sensitive folder |

## A07 - roadmap and resource plan

| What | Kind | Where |
|---|---|---|
| Project Resource Plan 3.0 | FILL | Sheet `1WKcXz9W2BGrtRChNQ8DsZghcUFqvDcqbhOx8u1cDKJU`; instruction Confluence 4757127285; template folder Drive `1prLFEiUAmlLO1emGzGu2KE5aGy2iNZA0`. Copy from the template and put a SHORTCUT into the project Drive - this is mandatory, do not rebuild it by hand. FILLED AFTER STAFFING (A10), not at A07: it needs confirmed people. At A07 the preliminary resource plan is the role-by-month hour table. Note the connector cannot create shortcuts on a shared drive - hand that step to the PM explicitly |
| Project Schedule and Project Road Map | SPEC | Confluence 3557687710 - tool comparison, marked `[DRAFT]`, its example links were stripped in the export |
| Capacity Planning Template | FILL | Confluence 2153840768 - velocity / person-day estimation |

## A08 - economy

| What | Kind | Where |
|---|---|---|
| Project Economy calculation process (P&L) | SPEC | Confluence 4040687712 |
| P&L file structure | REFERENCE | `references/pl-structure.md` in this plugin |

There is deliberately no self-serve P&L template. The file is created by PMO RM in one central sensitive folder. If the project has no P&L yet, the action is to request one, not to build one.

## A09 - baseline gate

No template. Outputs are a documented validation outcome, a value classification, and the client confirmation. The client confirmation lands in the contract / SOW, an email, a meeting follow-up, or another agreed written channel - there is no boilerplate, so the copilot drafts it and the PM sends.

## A10 - staffing

| What | Kind | Where |
|---|---|---|
| Staffing Master | REQUEST | No self-serve template. The PM requests the file from RM PMO. Instructions Confluence 4957110283 (`[WiP]`), 4954554594 |
| Project Resource Plan 3.0 | FILL | see A07 |

## A11 - PM system setup

| What | Kind | Where |
|---|---|---|
| Google Drive Structure | SPEC | Confluence 5257166927 + template 5262049359 |
| PROREP Project Card in Jira | SPEC | Confluence 3723624953 + field subpages 3728376200, 3723100702, 3722871940, 3725394135, 3725951029, 3728081539, 3728048794, 4146266185 |
| Communication Plan description | SPEC | Confluence 3272082121 - 6 columns plus a channels table; worked example 3271000087 |
| Google Chats (How to use Internal) | SPEC | Confluence 3006398548 |
| NotebookLM Project Brain - mandatory minimum | SPEC | Confluence 4955406559 |
| Quality Management Process (how to set up) | SPEC | Confluence 5056921990, marked `[Blank]` |
| Checklist: Project Start | FILL | Confluence 3072917506 |
| Checklist: Security | FILL | Confluence 3071213622 |
| DoR and DoD examples | EXAMPLE | Confluence 3426353304 |

## A12 - team alignment

| What | Kind | Where |
|---|---|---|
| Checklist: Project Start | FILL | Confluence 3072917506 |
| DoR and DoD examples | EXAMPLE | Confluence 3426353304 |
| Test Plan Template | FILL | Confluence 3302588732 |
| Manual QA Test Plan | SPEC | Confluence PMO space, search "Manual QA Test Plan" |

## A13 and A14 - kick-off

| What | Kind | Where |
|---|---|---|
| Project Kick-off Slide Deck | FILL | "[PROJECT] Kick-off Slide deck - TEMPLATE", Slides `1L1ukfexCcqm2-fMnsKWicy4mP-c7oXoMDWKq62fEFKg`, 12 slides, verified 2026-07-28; content guide Confluence 2891284612. Fill the PM's own copy, do not build a parallel one. Slide-by-slide map in the a12-a14-kickoff skill's `output-shapes.md`. NOTE the template's agenda differs from the content guide's section list - the template wins. Slide 8 carries the FP / T&M-with-Cap fork including the 70% and 85% cap-notification thresholds |
| Best Practice: Kick-off the project | SPEC | Confluence 4619206917 - 5 steps, M-Manager quality gate, dry run, 24h follow-up, recording consent scripts |
| Checklist: Kick-off | FILL | Confluence 3035070505 |
| Internal Project Kickoff Meeting Checklist | FILL | Confluence 3211985503 |
| UAT Plan Template | FILL | Confluence 2192769066, marked `[DRAFT]` |
| Change Request Form Template | FILL | Confluence 2799928052, marked `[Update]` |
| Customer report templates (weekly / monthly / sprint / release / timeline) | FILL | Confluence 3195371651, 3195731969, 3209625723, 3195306114, 3194749056, 3802595361 |

## Known template gaps - say so, do not improvise silently

These are mandatory artifacts with no usable template. When a skill hits one, tell the PM plainly that there is no company template, draft from the format spec, and note it as a PMO gap rather than presenting the draft as house standard.

1. Project Onboarding / Team Working Rules - mandatory. The A11 task literally ends with `[Link TBD]`. The hardest gap: mandatory with zero source material.
2. Risk Register - mandatory, no blank template. The Risk Framework's own tools section still carries unresolved `[Link to Risk Status Report Template]` and `[Link to Lessons Learned Template]` placeholders.
3. Project Team Composition - mandatory, storage "Spreadsheet", no template. In practice it lives inside the Resource Plan or Staffing Master.
4. Project Charter blank - the Project Description page links to a filled example, not a blank.
5. Roadmap / Timeline / Project Schedule - mandatory, but the page is a tool comparison with its example links stripped.
6. WBS / Critical Scope Baseline with Acceptance Criteria and Estimates - one mandatory row since Sep 2026; the live checklist itself calls it a full documentation gap (only an old `[DRAFT] WBS`).
7. Kick-off Agenda - mandatory A13 output, no agenda template separate from the deck.
8. Baseline Validation (Expectations Matrix) and Project (Start) Approval - two mandatory rows since Sep 2026 (the A09 client half and internal half). Baseline Validation points at the Project Deliverables Acceptance & Acceptance Protocol page; Project (Start) Approval is TBD on the checklist - no template.
9. Project Documentation Space - mandatory, no project-space template. (The `For Copy` skeleton cited here before, 4947477404, is gone - 404 on 2026-09-24.)
10. Acceptance From Pre-sale v2 - cited by A01, only a v1 `[DRAFT]` exists.
11. Opportunity & Internal Risk Register (A06) - mandatory since Sep 2026, TBD on the checklist: no instruction, no template, no wiki. Internal only.
12. RACI Matrix (Team + Stakeholders) (A12) - mandatory since Sep 2026, TBD on the checklist. The old `[Draft] RACI Matrix` 2133164167 is deprecated. A02 internal RACI (Sales / DM / Competency Center) has no template either.
13. EVM Baseline (A08, Fixed-Price only) - mandatory since Sep 2026, TBD on the checklist. Planned Value is normally money, so the template question belongs with the economy, not the brain.
14. Critical Path documentation (A07, Fixed-Price over 3,500h) - mandatory, no template named.

For 11-14: open question to PMO (Artem) as of 2026-09-24 - are templates coming? Until then the copilot drafts to the step verification criteria and says it is our draft.

Not gaps, by design: P&L and Staffing Master have no links because both are issued by PMO RM. Treat those as REQUEST, not missing.

## A note on resolving links

The Confluence export flattened inline links to bare text, so the standard mentions template names without URLs ("Google Drive Structure", "PROREP Project Card in Jira", "Communication Plan description"). Resolve by title against this register or against Confluence search - do not report a template as missing just because the standard's text has no URL.
