# Decision Log

> **Purpose**: Centralized record of all project decisions with rationale and impact tracking  
> **Rule**: Every significant decision gets logged here

---

## Why We Log Decisions

1. **Traceability**: "Why did we choose X?" - answered instantly
2. **Onboarding**: New team members understand context
3. **Client Alignment**: Documented proof of agreements
4. **Change Management**: Understand impact when revisiting decisions

---

## Decision Template

| ID | Date | Decision | Context | Options Considered | Chosen | Rationale | Stakeholders | Impact | Status |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---:|

---

## Active Decisions

### Core Architecture & Technical

| ID | Date | Decision | Context | Options Considered | Chosen | Rationale | Stakeholders | Impact | Status |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---:|
| D-T001 | 2024-XX-XX | [Tech Stack Selection] | [Why this came up] | React / Vue / Angular | React | [Performance, team expertise] | Team, Client | High - Entire frontend | Active |
|  |||||||||

### Business & Monetization

| ID | Date | Decision | Context | Options Considered | Chosen | Rationale | Stakeholders | Impact | Status |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---:|
| D-B001 | 2024-XX-XX | [Payment Gateway] | [Client needs payments] | Stripe / PayPal / Square | Stripe | [Ease of integration, features] | Client, Team | High - Epic-04 | Active |
|  |||||||||

### User Experience & Features

| ID | Date | Decision | Context | Options Considered | Chosen | Rationale | Stakeholders | Impact | Status |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---:|
| D-UX001 | 2024-XX-XX | [Multi-org Support] | [Coaches work for multiple trainers?] | A: Allow multi-org / B: Single-org only | B | [Simplifies permissions, MVP-first] | Client | High - Epic-01 | Active |
|  |||||||||

### MVP Scope

| ID | Date | Decision | Context | Options Considered | Chosen | Rationale | Stakeholders | Impact | Status |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---:|
| D-S001 | 2024-XX-XX | [Camps in MVP] | [Client wants camp registration] | A: Include in MVP / B: Defer to Post-MVP | B | [Complexity too high, 50% feature reduction] | Client, Team | High - Epic-03 | Active |
|  |||||||||

---

## Superseded / Changed Decisions

| ID | Original Decision | Date Changed | New Decision | Reason for Change | Impact |
|:---|:---|:---|:---|:---|:---|
| D-T001-OLD | [Old tech choice] | 2024-XX-XX | [New choice: See D-T001] | [Client requirement changed] | [Epics affected] |
|  ||||||

---

##Deferred / Parking Lot

*Decisions postponed to Phase 2 or future iterations:*

| ID | Deferred Decision | Why Deferred | Target Phase | Stakeholders |
|:---|:---|:---|:---|:---|
| D-DEF001 | [Feature X implementation approach] | [Too complex for MVP] | Phase 2 | Team |
|  |||||

---

## Decision Entry Guidelines

### When to Log a Decision

[x] **Log if**:
- Client chooses between multiple options
- Team makes architectural choice
- Feature is included/excluded from MVP
- Business rule is defined
- Third-party service is selected
- Major UX pattern is chosen

[no] **Don't log**:
- Trivial implementation details (variable names)
- Temporary workarounds
- Personal preferences without impact

---

### How to Create an Entry

**Step 1: Assign ID**

Format: `D-[Category][Number]`

Categories:
- **T** = Technical/Architecture
- **B** = Business/Monetization
- **UX** = User Experience
- **S** = Scope
- **C** = Compliance/Legal

**Numbering**: Sequential within category

---

**Step 2: Complete Template**

```markdown
| D-XXX | 2024-12-25 | [1-line decision summary] | [Why this decision needed] | A: [Option] / B: [Option] / C: [Option] | [Chosen option] | [Why chosen] | Client, Team | High/Medium/Low - [Specs affected] | Active |
```

**Example**:
```markdown
| D-T002 | 2024-12-25 | Video hosting approach | Client needs video content for training | A: Upload to platform / B: YouTube embeds | B | 75% cost reduction, faster MVP | Client, Team | High - Epic-02 | Active |
```

---

### Context Field Tips

**Good Context**:
```
"Client mentioned needing video content for player training (LPPP framework). 
Need to decide storage approach before Epic-02 creation."
```

**Poor Context**:
```
"Videos needed"
```

---

### Rationale Field Tips

**Good Rationale**:
```
"YouTube embeds:
- Save 75% dev time (no transcode/storage)
- Zero ongoing storage costs
- Leverage existing CDN
- Still valuable to users
- Aligns with MVP-first philosophy"
```

**Poor Rationale**:
```
"Easier"
```

---

## Using Decisions

### During Spec Creation

Reference decisions in Epic/Feature files:

```markdown
## 8. Technical Considerations

Video content will use YouTube embeds only (Decision D-T002).
No video uploads in MVP to reduce complexity.
```

---

### During Client Reviews

**Prepare decision summary**:
```
"In our last 3 sessions, we made 8 key decisions:

High-Impact:
- D-T001: React for frontend
- D-B001: Stripe for payments
- D-S001: Defer camps to Phase 2

Medium-Impact:
..."
```

---

### When Client Changes Mind

1. **Don't delete old decision** - Mark as "Superseded"
2. **Create new decision** with updated choice
3. **Link decisions**: "Supersedes D-XXX"
4. **Update affected specs** and note impact
5. **Update Project_Plan.md** with timeline/cost impact

**Example**:
```markdown
### Superseded Decisions
| D-UX001-OLD | 2024-12-20 | Dark mode only | ... | Superseded by D-UX001-NEW | Light mode added per client request |
```

---

## Decision Impact Levels

| Impact | Definition | Examples |
|:---|:---|:---|
| **High** | Affects multiple epics or architecture | Tech stack, payment gateway, MVP scope cuts |
| **Medium** | Affects single epic significantly | Feature workflow, data model for one area |
| **Low** | Affects single feature or UI pattern | Button color, error message wording |

---

## Decision Review Meetings

**Frequency**: Weekly OR at phase boundaries

**Agenda**:
1. Review decisions made this week
2. Confirm client alignment
3. Check for contradictions with previous decisions
4. Identify deferred decisions that need revisiting

**Output**: Update Decision_Log with confirmations

---

## AI Assistance with Decision Logging

**Prompt**:
```
"We just decided to [X]. Document this in Decision_Log.md format:

Decision: [What was decided]
Context: [Why this came up]
Options: [List alternatives we considered]
Chosen: [X]
Rationale: [Why we chose this]
Impact: [Which epics/features affected]

Also check: Does this contradict any existing decisions?"
```

AI will help you:
- Format consistently
- Check for contradictions
- Identify affected specs
- Suggest related decisions to review

---

## Metrics

Track decision health:

| Metric | Target |
|:---|---:|
| **Decisions Logged Last Week** | >5 |
| **P0 Questions Converted to Decisions** | 100% |
| **Decisions Without Rationale** | 0 |
| **Superseded Decisions (Churn)** | <10% |

**Warning Signs**:
- >20% churn (client keeps changing mind - need better discovery)
- Decisions logged without client confirmation (assumption risk)
- Decisions without clear rationale (poor documentation)

---

## Related Files

- [Open Questions](Open_Questions.md) - Feed into decisions
- [Client Interactions](Client_Interactions.md) - Source of decisions
- [Project Plan](../00_Meta/Project_Plan.md) - Decisions drive plan updates
- [Validation Workflow](../00_Meta/Workflow_Validation.md) - Validate decision impact
