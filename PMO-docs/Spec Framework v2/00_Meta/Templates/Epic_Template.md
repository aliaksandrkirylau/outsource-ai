# Epic-[Number]: [Title]

> **ID**: Epic-[Number]
> **Status**: [Draft | In Review | Approved | In Development | Complete]
> **Last Updated**: [Date]
> **Owner**: [Team/Person]
> **Naming Convention**: `Epic-[NN]_[Name]_SPEC.md` (e.g., Epic-01_User_Management_SPEC.md)

---

## IMPORTANT NOTE

**Describe WHAT users need and WHY. Do not prescribe API design, database schemas, specific libraries, or technical architecture.** That is the developer's domain. Keep language business-focused and user-centric.

---

## Epic Overview

### Description

*High-level summary of what this Epic covers. What is the business value? What problem does this solve?*

[2-3 paragraphs explaining the epic and its purpose]

### Business Value

**Problem Statement**: [What pain point does this address?]

**User Impact**: [How does this improve user experience or business outcomes?]

---

## In Scope (MVP)

*Broad capabilities and features included in this Epic:*

- [ ] Capability 1
- [ ] Capability 2
- [ ] Capability 3

---

## Out of Scope

*Explicitly excluded to prevent scope creep:*

- [no] [Feature/Capability] -- Reason: [Deferred to Phase 2 / Not required for MVP / Complexity]
- [no] [Feature/Capability] -- Reason: [Deferred to Phase 2 / Not required for MVP / Complexity]

---

## Dependencies

### Required Before This Epic

*Other Epics or systems that must exist first:*

- **None** OR
- Epic-XX: [Name] -- [Why needed]

### Blocks These Epics

*What depends on this Epic being complete:*

- Epic-XX: [Name] -- [Why needed]

### External Dependencies

*Third-party services, APIs, or integrations:*

- [Service/API Name] -- [Purpose and what it provides]

---

## User Roles Involved

| Role | Primary Actions | Access Level |
|:---|:---|:---|
| **[Role Name]** | [What they do in this epic] | [What they can access] |
| **[Role Name]** | [What they do in this epic] | [What they can access] |

*Reference*: `01_Context/Platform_Specification.md` or `01_Context/Glossary.md` for role definitions

---

## Features

Each feature below is a major capability within this Epic. Document each with its own section using the structure below.

---

## Feature: [Feature Name 1]

### User Story

**As a** [User Role],
**I want to** [Action/Capability],
**So that** [Business Benefit/User Value].

**Example**:
> As a **Player**, I want to **RSVP for training sessions**, so that **the coach knows I'm attending and reserves my spot**.

---

### Description & Context

*Detailed explanation of what this feature does and why it exists.*

[2-4 paragraphs describing the feature, how it works, and its importance]

**Key Points**:
- Point 1
- Point 2
- Point 3

---

### User Flow / UI Requirements

#### Primary Flow (Happy Path)

1. User [starts at location/screen]
2. User [performs action X]
3. System [responds with Y]
4. User [sees Z]
5. System [completes with outcome]

#### UI Components Needed

| Component | Description | Design Reference |
|:---|:---|:---|
| **[Component Name]** | [What it does] | See 04_Designs/ or [reference] |

---

### Acceptance Criteria

*Use Gherkin-style (Given-When-Then) format. Mark assumptions with [ASSUMPTION: ...] tags.*

#### Scenario 1: [Success Case Description]

**Given** [initial context/state]
**When** [action is performed]
**Then** [expected outcome]

**Example**:
- **Given** I am a logged-in Player
- **And** there are available spots in the session
- **When** I click "RSVP" on a session
- **Then** my reservation is confirmed
- **And** the available spots count decrements by 1

#### Scenario 2: [Edge Case or Alternative Flow]

**Given** [different context]
**When** [action is performed]
**Then** [expected outcome]

#### Scenario 3: [Error Case]

**Given** [error condition]
**When** [action attempted]
**Then** [error handling behavior]

---

### Edge Cases & Error Handling

| Edge Case | Expected Behavior |
|:---|:---|
| **Network fails during action** | Show retry option, don't lose user's action |
| **User double-clicks button** | Prevent duplicate submissions (debounce) |
| **User already performed this action** | Show different state or prevent re-action |
| **Invalid input** | Show inline validation error |
| **Server error** | Show friendly error message, allow retry |
| **Permission denied** | Show appropriate access denied message |

---

### Business Rules

*Constraints, policies, and limits specific to this feature:*

1. **Rule Name**: [Description]
   - Example: **Cancellation Window**: Users can cancel up to 2 hours before session start

2. **Rule Name**: [Description]
   - Example: **Age Restriction**: Players under 13 require parent approval for RSVP

*Note: Cross-cutting business rules belong in Platform_Specification.md -- reference or quote them here as needed.*

---

### Data & State

#### What Data Is Involved

*Describe the information this feature works with (not how it's stored):*

**Data Captured/Modified**:
- User identification (who performed the action)
- Target object (what they're acting on)
- Timestamp (when action occurred)
- Status/State (confirmed, pending, cancelled, etc.)
- Any user-provided input fields

#### Data Sources

- **User input**: [List what user provides]
- **System generated**: [List what system creates automatically]
- **From other features**: [List dependencies on other data]
- **External sources**: [List third-party data if applicable]

#### State Management

*Describe the states this feature can be in:*

| State | Description | User Can... |
|:---|:---|:---|
| **[State Name]** | [Description of state] | [What actions available] |
| **[State Name]** | [Description of state] | [What actions available] |

---

### Implementation Considerations

> **Note**: This section helps developers understand what needs to be built, without prescribing exactly how to build it.

**Data Persistence**
- What data needs to be stored long-term vs. temporary?
- What data relationships exist?
- What data needs to be retrieved quickly? (performance considerations)

**Integration Points**
- Does this feature call other features or services?
- Does this feature expose data/functionality to other features?
- Are there third-party services involved? (payment, email, SMS, etc.)

**Real-time vs. Asynchronous**
- What needs to happen immediately?
- What can happen in the background?
- What needs real-time updates?

**Scale & Performance**
- Expected volume (users per day, transactions per hour)?
- Any performance requirements? (must load in <2 seconds)
- Caching opportunities?

**Security & Permissions**
- Who can access this feature?
- What data is sensitive and needs protection?
- Any audit trail needed? (who did what when)

---

### Dependencies

#### Feature Dependencies
- **Requires**: [Feature or capability] must be complete
- **Blocks**: [Feature or capability] needs this feature
- **Related**: [Feature or capability] works together with this

#### External Dependencies
- [Service Name]: [Purpose and what it provides]
- [External API]: [What it provides]

#### Business Dependencies
- Client must approve: [specific aspect]
- Legal/Compliance: [If applicable]
- Content needed: [Copy, images, etc.]

---

### Out of Scope (For This Feature)

*Explicitly excluded to prevent scope creep:*

- [no] [Excluded item] -- Reason: [Defer to Phase 2 / Not required for MVP]
- [no] [Excluded item] -- Reason: [Defer to Phase 2 / Not required for MVP]

---

### Open Questions

*Questions blocking or affecting this feature. Also log in `03_Discussions/Open_Questions.md`:*

| ID | Question | Priority | Owner | Status |
|:---|:---|:---:|:---|:---|
| Q-[XX] | [Question text] | P0/P1/P2 | [Name] | Open |

---

### Decisions Made

*Key decisions for this feature. Also log in `03_Discussions/Decision_Log.md`:*

| Date | Decision | Rationale |
|:---|:---|:---|
| YYYY-MM-DD | [Decision] | [Why this approach] |

---

### Developer Questions

*Developers: If you have questions during implementation, log them here and tag the BA for clarification.*

| Date | Question | Asked By | Answer | Answered By |
|:---|:---|:---|:---|:---|
| | | | | |

---

---

## Feature: [Feature Name 2]

*[Repeat the same structure for each significant feature in this Epic]*

---

## Feature: [Feature Name 3]

*[Repeat the same structure for each significant feature in this Epic]*

---

## Epic-Level Questions & Decisions

### Open Questions

*Unresolved questions affecting the entire Epic:*

| ID | Question | Priority | Owner | Status |
|:---|:---|:---:|:---|:---|
| Q-[XX] | [Question text] | P0/P1/P2 | [Name] | Open |

*Full log*: `03_Discussions/Open_Questions.md`

---

### Epic Decision Log

*Major decisions made for this Epic:*

| Date | Decision | Rationale | Alternatives Considered |
|:---|:---|:---|:---|
| YYYY-MM-DD | [Decision] | [Why] | [What else was considered] |

*Full log*: `03_Discussions/Decision_Log.md`

---

## Epic Acceptance Criteria

This Epic is complete when:

- [ ] All features listed above are implemented and tested
- [ ] User can complete end-to-end flows without errors
- [ ] All P0 and P1 questions resolved
- [ ] Client approval received
- [ ] Edge cases handled gracefully
- [ ] No "TBD" or undefined terms in specs

---

## Mockups / Design References

*Links to design files or screenshots for this Epic:*

- [Figma Link]
- [Design Assets Location]: `04_Designs/Epic-[Number]/`

---

## Related Files

- **[Platform Specification](../../01_Context/Platform_Specification.md)** -- Complete platform context
- **[Glossary](../../01_Context/Glossary.md)** -- Term definitions
- **[Open Questions](../../03_Discussions/Open_Questions.md)** -- Full question log
- **[Decision Log](../../03_Discussions/Decision_Log.md)** -- Full decision log


                                                                                                                                               