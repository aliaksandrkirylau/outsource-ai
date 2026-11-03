# Open Questions Log

> **Purpose**: Central tracking for all questions requiring Client or Internal Team clarification.  
> **Workflow**: Add questions here -> Batch for meetings -> Answer -> Move to Resolution section

---

## Priority Definitions

| Priority | Definition | Response Time |
|:---:|:---|:---|
| **P0** | **Blocker** - Cannot proceed without answer | ASAP (same day) |
| **P1** | **Important** - Significantly affects design/scope | Within 3 days |
| **P2** | **Clarification** - Nice to know, low impact | Within 1 week |

---

## 1. High Priority Questions (Blockers - P0)

| ID | Question | Context | Affected Spec | Owner | Status | Date Added |
|:---|:---|:---|:---|:---|:---:|:---|
| Q-001 | [Example: What payment gateway?] | [Why we need to know] | Epic-04| Client | Open | 2024-12-XX |
|  |||||||

**CRITICAL**: Don't proceed to implementation until P0 questions are resolved!

---

## 2. Important Questions (P1)

| ID | Question | Context | Affected Spec | Owner | Status | Date Added |
|:---|:---|:---|:---|:---|:---:|:---|
| Q-101 | [Example question] | [Context] | Epic-XX | Client | Open | 2024-12-XX |
|  |||||||

---

## 3. Clarification Questions (P2)

| ID | Question | Context | Affected Spec | Owner | Status | Date Added |
|:---|:---|:---|:---|:---|:---:|:---|
| Q-201 | [Example question] | [Context] | Epic-01 | Team | Open | 2024-12-XX |
|  |||||||

---

## 4. Pending Review (Answered, Needs Validation)

| ID | Question | Proposed Answer | Needs Confirmation From | Date Answered |
|:---|:---|:---|:---|:---|
| Q-050 | [Question] | [Suggested answer] | Client | 2024-12-XX |
|  |||||

---

## 5. Resolved Questions (Archive)

| ID | Question | Answer | Source | Date Resolved | Impact |
|:---|:---|:---|:---|:---|:---|
| Q-000 | [Example: Stripe or PayPal?] | **Stripe Connect**| Client email 12/20 | 2024-12-20 | Updated Epic-04 |
|  ||||||

---

## Adding Questions (Workflow)

### 1. Create Question Entry
```markdown
| Q-XXX | [Clear, specific question] | [Why this matters] | [Which spec] | [Who should answer] | Open | [Today's date] |
```

### 2. Assign Priority
- Blocker (can't proceed): P0
- Design-significant: P1
- Nice to know: P2

### 3. Identify Owner
- **Client**: Only client can answer (business decision)
- **Team**: Internal technical decision
- **Both**: Needs collaboration

### 4. Update Affected Specs
Add reference in the relevant Epic/Feature:
```markdown
## Open Questions
- Q-XXX: [Question summary] (P0)
```

---

## Answering Questions (Workflow)

### 1. Document Answer
Move question to "Pending Review" OR "Resolved"

### 2. Update Decision Log
Log in [`Decision_Log.md`](Decision_Log.md) if answer represents a decision

### 3. Update Affected Specs
Incorporate answer into Epic/Feature files

### 4. Remove Blockers
If P0, notify team that work can proceed

---

## Question Templates

### Business Logic Question
```
| Q-XXX | How should [scenario] be handled? | [Epic/Feature] mentions [X], but unclear if [Y]. This affects [user flow/data model/UI]. | [Spec reference] | Client | P1 | [Date] |
```

### Technical Feasibility Question
```
| Q-XXX | Can we support [feature] with [tech stack]? | Client requested [feature]. Need to verify if [technical constraint] allows this. | [Spec reference] | Team | P1 | [Date] |
```

### Edge Case Question
```
| Q-XXX | What happens when [edge case]? | [Feature] spec doesn't define behavior for [unusual scenario]. | [Spec reference] | Client | P2 | [Date] |
```

---

## Tips for Writing Good Questions

### [x] Good Questions

**Specific**:
```
Q: "Should coaches be able to edit attendance after the session ends? 
If yes, how long after (24hrs, unlimited)?"
```

**Provides Context**:
```
Q: "Do parents need to approve child purchases? 
Context: COPPA compliance concern for users under 13."
```

**Offers Options**:
```
Q: "How should we handle session conflicts?
Option A: Block + error message
Option B: Warn + allow override
Option C: Warn + requires approval"
```

### [no] Poor Questions

**Too Vague**:
```
Q: "How should the dashboard work?" 
(Too broad - break into specific questions)
```

**Assumed Answer**:
```
Q: "We're using dark mode, correct?" 
(Don't assume - ask neutrally)
```

**No Context**:
```
Q: "What about coaches?" 
(What about them? Be specific)
```

---

## Batching for Client Meetings

### Pre-Meeting Prep

1. **Group by topic**:
   - User Management questions
   - Payment questions
   - Content questions

2. **Prioritize**:
   - Start with all P0 questions
   - Then P1 questions
   - P2 if time allows

3. **Prepare materials**:
   - For complex questions, prepare mockups or examples
   - For technical questions, prepare simplified explanation

### During Meeting

- Save transcript/notes to `03_Discussions/Meetings/` (run meeting-processor skill)
- Mark questions as answered in real-time
- Ask follow-up questions immediately

### Post-Meeting

- Move resolved questions to "Resolved" section
- Log decisions in Decision_Log.md
- Update affected specs
- Send summary email with decisions to client

---

## Metrics to Track

Monitor question health:

| Metric | Target | Status |
|:---|---:|:---:|
| **P0 Questions Open** | 0 | ? 3 |
| **P1 Questions Older Than 3 Days** | <5 | ? 2 |
| **Total Open Questions** | <20 | ? 18 |
| **Questions Answered This Week** | >10 | ? 14 |

**Danger Signs**:
- >5 P0 questions (investigation paralyzed)
- P1 questions aging >1 week (client not engaged)
- Total questions >50 (insufficient discovery upfront)

---

## Related Files

- [Meetings](Meetings/)
- [Decision Log](Decision_Log.md)
- [Project Plan](../00_Meta/Project_Plan.md)


