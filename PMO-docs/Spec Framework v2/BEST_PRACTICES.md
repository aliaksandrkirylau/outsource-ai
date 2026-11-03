# Best Practices & Lessons Learned

Proven patterns from real spec projects. Read this when you're unsure how detailed to go, how to handle scope pressure, or how to structure client interactions.

---

## The Spec/Dev Boundary

**The single most important rule in this framework.**

Specs describe **WHAT users need and WHY**. Developers (and their AI) decide **HOW to build it**.

### The Line

| Belongs in spec | Does NOT belong in spec |
|:---|:---|
| User stories, acceptance criteria | API endpoint definitions |
| Business rules and constraints | Database schemas or table structures |
| Data involved and states | Specific libraries or frameworks |
| Performance and security requirements | Code or pseudocode |
| Integration requirements (e.g., "pays via Stripe") | Implementation details (e.g., "use Stripe Checkout API with webhooks") |

### Examples

**Authentication:**
- [no] Wrong: "Use JWT with RS256, store refresh tokens in httpOnly cookies, expire after 15 minutes"
- [x] Right: "Only authenticated users can access this feature. Sessions expire after a period of inactivity. Users can log out from all devices."

**Payment:**
- [no] Wrong: "Use Stripe Checkout API, generate session IDs server-side, handle webhooks for confirmation"
- [x] Right: "Users pay for events via Stripe. Payment confirmation is immediate. Trainers receive payouts monthly."

**Data Storage:**
- [no] Wrong: "Store user data in PostgreSQL with indexed email column"
- [x] Right: "User profiles include name, email, and contact information. Email must be unique and queryable."

### The Hotel Test

You're describing the house you want to live in, not teaching someone how to build houses. A developer reading your spec should think: "I know what needs to happen. I'll choose the best architecture for this."

### When developers ask "How should I...?"

**Bad response:** "Use JWT with RS256, store in localStorage, refresh every 15 minutes."
-> You're doing their job.

**Good response:** "The session should keep users logged in for [X time], be secure, and survive page refreshes. If there are trade-offs to discuss, let's talk."
-> You're defining requirements. They choose implementation.

**When technical specifics ARE appropriate:**
- Client has contractually mandated a specific technology
- Integration requires a specific protocol
- Compliance requires a specific approach (HIPAA, PCI-DSS)

---

## Scope Control Patterns

### The Scope Audit Trigger

Run `scope-audit` any time you're about to add something. Not just before client reviews -- **any time**:
- A feature is being added to an existing Epic
- The Platform Specification scope is changing
- A "while we're at it" thought appears
- A client email implies a new capability

The question: **Is this still MVP, or are we drifting?**

### Saying No to Clients

Frame every scope addition as a trade-off:

> "That's a useful idea. Here's the impact: including this adds significant complexity to Epic-XX and will delay MVP by [timeframe]. We can either include it now (with the impact), simplify it (here's how), or defer it to Phase 2 and keep MVP on track. What matters more right now -- launch speed or this feature?"

Empower clients to make informed choices. Never silently add scope.

### When Client Changes Mind

1. Log the old decision in `03_Discussions/Decision_Log.md` with status "Superseded"
2. Create a new decision entry with the change and rationale
3. Run impact analysis: which Epics and features are affected?
4. Update the Platform Specification if scope changed
5. Get client re-confirmation on updated scope

Traceability prevents blame games.

### Post-MVP Items

When something doesn't pass scope-audit, it goes to the **Out of Scope section** of the relevant Epic (prefixed with [no]) -- not a separate folder or file. The Out of Scope section is part of the spec. Developers need to know what's explicitly not being built just as much as what is.

---

## Strategic Decision Patterns

### Pattern 1: Build vs Buy vs Link

**Common Scenario**: Client needs to incorporate existing content or services (videos, documents, payment processing, etc.)

**Options to Consider**:
- A) **Build**: Implement from scratch (full control, high cost)
- B) **Buy/Integrate**: Use third-party service (medium cost, dependencies)
- C) **Link/Aggregate**: Reference external resources (low cost, limited control)

**Decision Framework**:
```
If (feature is NOT core differentiator):
    Prefer: Buy or Link
If (MVP timeline is tight):
    Prefer: Link over Buy over Build
If (ongoing costs are concern):
    Calculate: Build cost vs Subscription cost over 3 years
```

**Example**: Video content in training platform
- Build = Host videos (storage + transcoding + CDN)
- Link = YouTube embeds
- **Impact**: Linking saved 75% dev time, zero storage costs

**Takeaway**: **Challenge "upload" assumptions. For MVP, aggregation often beats hosting.**

---

### Pattern 2: Relationship Complexity

**Common Scenario**: Client wants flexible many-to-many relationships (users belong to multiple orgs, items in multiple categories, etc.)

**Options**:
- A) **Many-to-Many**: Full flexibility, complex permissions
- B) **One-to-Many**: Single primary relationship, simpler model
- C) **Hybrid**: Primary + secondary references

**Decision Framework**:
```
If (>3 permission rules needed):
    Consider: Simplifying to one-to-many
If (user confusion likely):
    Prefer: Simpler model
If (Phase 2 expansion possible):
    Start: Simple, add flexibility later
```

**Example**: User-organization relationships
- A = Users belong to multiple orgs (context-switching, complex RBAC)
- B = Users belong to one org (clear context, simple permissions)
- **Impact**: Single-org reduced edge cases by 60%, clearer UX

**Takeaway**: **Complexity compounds exponentially. Start simple, expand if validated.**

---

### Pattern 3: Guest Access & Public Flows

**Common Scenario**: Client wants public registration or guest checkout for specific features

**Complexity Indicators**:
- Provisional accounts (guest -> registered user conversion)
- Mixed anonymous + authenticated states
- Permission edge cases (what can guests see/do?)
- Data migration (guest data -> user account)

**Decision Framework**:
```
If (feature requires >5 edge case rules):
    Probably: Post-MVP
If (affects core security model):
    Requires: Extra validation
If (alternative exists):
    Consider: Require login upfront
```

**Example**: Public event registration with guest checkout
- Complexity: Guest data structure, conversion flow, email verification, duplicate detection
- **Alternative**: Require simple account creation first (email + name = low friction)
- **Impact**: Deferring guest flows can reduce feature complexity by 40-50%

**Takeaway**: **If a feature needs 5+ edge case rules, evaluate if it's truly MVP.**

---

## ? Requirements Process

### Use the 8-Step Loop Religiously

**What it looks like in practice**:

```
Session Start:
1. AI: "I've analyzed Client Brief. Here's my plan..." (Analyze + Plan)
2. You: "Approved, proceed" (Approve)
3. AI: Creates Epic-01 draft (Execute)
4. AI: "Created Epic-01. Questions: Does X include Y?" (Report + Question Check)
5. You: Review Epic-01, answer questions (Review)
6. AI: Updates Project_Plan.md with next steps (Next Steps)
```

**Why it works**:
- Prevents AI from going rogue
- Forces validation at each step
- Creates audit trail
- Builds muscle memory

---

### How Much Detail? The Goldilocks Principle

**The Big Question**: "How detailed should my specs be?"

**The Answer**: **Just enough to transfer knowledge without prescribing implementation.**

---

#### The Three Zones

**Zone 1: Too Vague [no]**
```markdown
Feature: User Management
- Users can log in
- Admins can manage users
```

**Problem**: Developer has to guess everything. 100+ questions coming.

---

**Zone 2: Too Prescriptive [no]**
```markdown
Feature: User Login
- Create table: users (id INT PRIMARY KEY, email VARCHAR(255), password_hash CHAR(60))
- Use bcrypt with cost factor 12
- Implement JWT with RS256 algorithm
- Token expiry: 3600 seconds
- Refresh token stored in Redis with TTL
- API endpoint: POST /api/v1/auth/login
- Response: { "access_token": string, "expires_in": number }
```

**Problem**: You're doing the developer's job. Removes flexibility, prescribes implementation.

---

**Zone 3: Just Right [x]**
```markdown
Feature: User Login

User Story:
As a registered user, I want to log in with my email and password, 
so that I can access my personalized dashboard.

Acceptance Criteria:
- Given a valid email and password
- When I submit the login form
- Then I am authenticated and redirected to my dashboard
- And I remain logged in for [X duration - ask client]

Edge Cases:
- Invalid credentials -> Show error, don't reveal which field is wrong (security)
- Account locked (3 failed attempts) -> Show lockout message, email user
- Password reset in progress -> Invalidate old sessions

Business Rules:
- Session duration: [Client to decide - 30 min? 24 hours? Remember me option?]
- Password must meet requirements [defined in Platform_Specification.md or the relevant Epic]
- Max failed login attempts: 3 within 15 minutes

Data & State:
- User provides: email, password, optional "remember me"
- System validates: credentials, account status
- System creates: authenticated session
- System stores: session token (secure, httpOnly)

Implementation Considerations:
- Use secure password hashing (bcrypt, argon2, or similar)
- Session tokens must be cryptographically secure
- Tokens should expire after inactivity
- Consider rate limiting on login endpoint (prevent brute force)
- Audit log: Track login attempts for security monitoring
```

**What's Different**:
- [x] Describes **what** should happen, not **how** to build it
- [x] Includes **why** (security, UX, business needs)
- [x] Covers **edge cases** and **error scenarios**
- [x] Provides **constraints** (security, performance)
- [x] Leaves **implementation choices** to developer (which library, which database, which architecture)

---

#### The Detail Checklist

**For Each Feature, Ask**:

| Question | If NO, add more detail | If YES, you might be too detailed |
|:---|:---|:---|
| **Can a developer understand WHAT users will experience?** | Add user stories, flows | |
| **Are edge cases and error scenarios documented?** | Add edge case table | |
| **Are success criteria clear and testable?** | Add acceptance criteria | |
| **Are business rules and constraints defined?** | Add business rules section | |
| **Can a developer choose their own implementation approach?** | | Remove API specs, database schemas |
| **Is the spec technology-agnostic?** | | Remove library names, frameworks |
| **Would changing the tech stack break the spec?** | | Generalize technical details |

---

#### Rule of Thumb: "The Hotel vs. Blueprint Test"

**Bad Spec = Blueprint**:
"The bathroom should have 2.5" copper pipes, Kohler K-596-VS faucet, 
12x12 porcelain tiles, grout color #D4C5B9..."

**Good Spec = Hotel Description**:
"Modern bathroom with rain shower, double vanity, good water pressure, 
clean aesthetic, easy to maintain."

**Why**: The contractor (developer) is the expert on HOW to build. 
You're the expert on WHAT the user needs.

---

#### Examples by Section

**Good Level of Detail**:

| Section | What to Include | What to Avoid |
|:---|:---|:---|
| **User Story** | Role, goal, benefit | Implementation steps |
| **Description** | What it does, why it exists, user experience | How to code it |
| **User Flow** | Steps user takes, what they see | API calls, state management |
| **Acceptance Criteria** | Observable outcomes, testable scenarios | Unit test code |
| **Edge Cases** | What should happen when X | How to handle it technically |
| **Business Rules** | Constraints, policies, limits | Validation regex, SQL queries |
| **Data & State** | What data is involved, what states exist | Database schema, field types |
| **Implementation Considerations** | Performance needs, security requirements, scale expectations | Specific libraries, frameworks |
| **Dependencies** | What's needed, integrations | API endpoints, database tables |

---

#### When Developers Ask "How Should I...?"

**If they ask**: "How should I implement the login session?"

**Bad BA Response**: "Use JWT with RS256, store in localStorage, refresh every 15 minutes"
-> *You're doing their job*

**Good BA Response**: "The session should keep users logged in for [X time], be secure, and survive page refreshes. If there are security or UX trade-offs, let's discuss."
-> *You're defining requirements, they choose implementation*

**When to Provide Technical Detail**:
- [x] Client has mandated a specific technology (contractual)
- [x] Integration requires specific API/protocol (external system)
- [x] Compliance requires specific approach (HIPAA, PCI-DSS)
- [x] You're working with junior devs who need more guidance (team decision)

**Otherwise**: Trust your developers to make technical decisions.

---

#### AI Guidance Prompt

Use this prompt to check your detail level:

```
"Review [Feature Name]. Is this spec:
1. Clear enough for a developer to understand WHAT to build?
2. Flexible enough for developer to choose HOW to build it?
3. Specific enough to prevent misinterpretation?

Identify:
- Vague areas that need more detail
- Over-specified areas that should be generalized
- Missing edge cases or acceptance criteria"
```

---

#### Red Flags You're Too Detailed

- ? You're naming specific libraries or frameworks
- ? You're specifying database tables and column types
- ? You're writing API endpoint specifications
- ? You're defining algorithms or data structures
- ? Developer says "I can't make any technical decisions"
- ? Changing from React to Vue would require rewriting the spec

#### Red Flags You're Not Detailed Enough

- ? Developers asking 10+ clarifying questions per feature
- ? Multiple interpretations of the same requirement
- ? Missing edge cases discovered in development
- ? "What should happen if...?" questions from QA
- ? Features getting built wrong the first time

---

#### The Collaboration Model

**Your Job (BA)**:
- Define WHAT users need
- Define WHEN/WHERE they need it
- Define WHY it matters (business value)
- Define constraints (performance, security, scale)
- Define success criteria (how to test)

**Developer's Job**:
- Decide HOW to build it
- Choose technology stack (unless mandated)
- Design architecture and data models
- Optimize for performance and maintainability
- Handle technical edge cases

**Shared Job** (via Developer_Questions.md):
- Clarify ambiguities
- Discuss trade-offs
- Validate assumptions
- Adjust scope based on technical findings

---

#### Quick Reference

**The Goldilocks Formula**:
```
Enough detail to answer:
1. What does the user see/do?
2. What happens in each scenario (success, errors, edge cases)?
3. What are the rules and constraints?
4. How will we know it's working correctly?

Not so much detail that you answer:
5. What technology should we use?
6. How should we structure the code?
7. What database schema should we create?
8. Which libraries should we choose?
```

---

**Remember**: Specs are **communication tools**, not **construction manuals**. 

You're describing **the house you want to live in**, not teaching someone how to build houses.

---

### Batch Questions for Clients

**Bad Pattern [no]**:
```
Email 1: "What color should buttons be?"
Email 2: "How many users in a team?"
Email 3: "Do you need export to CSV?"
```

**Good Pattern [x]**:
```
Email 1: "Based on our analysis, we have 8 questions 
organized by priority. Can we schedule 30 min to review?"

Meeting:
- P0 (Blockers): Questions 1-3
- P1 (Important): Questions 4-6
- P2 (Nice to have): Questions 7-8
```

**Tool**: `Open_Questions.md` with priority matrix

---

### Document Every Decision

**Why**: 
- "Why did we choose X?" comes up 3 months later
- New team members need context
- Client may forget what they approved

**How**: `Decision_Log.md` structure:
```markdown
| ID | Decision | Options Considered | Chosen | Rationale | Date | Stakeholders | Impact |
```

**Example**:
```markdown
| D-003 | Parent/Child Approval | (A) No restriction (B) Approval flow | B | Prevent unauthorized purchases | 2024-12-24 | Client, Team | High - New feature |
```

---

## ? Working with AI

### Prompt Engineering Tips

**Poor Prompt [no]**:
```
"Create a feature for user authentication"
```

**Better Prompt [x]**:
```
"Using the Epic_Template.md, draft the User Registration section within Epic-01.
- User story: registration via email
- Include: acceptance criteria (Given/When/Then), edge cases, business rules
- Cross-cutting rules belong in Platform_Specification.md -- reference them from Epics as needed
- Edge cases to consider: Duplicate emails, invalid domains, rate limiting
```

**Why**: Specific, contextual, refers to existing docs, anticipates gaps

---

### AI Validation Prompts

Use these regularly:

**Gap Analysis**:
```
"Analyze Epic-03 and all its child features. Identify:
1. Logical inconsistencies
2. Missing edge cases
3. Undefined terms (not in Glossary)
4. Missing dependencies
5. Potential simplifications"
```

**Cross-Reference Check**:
```
"Compare Open_Questions.md against Epic-01 and Epic-02. 
Are there any resolved questions that should update the specs?
Are there new questions implied by the specs?"
```

**Simplification Sweep**:
```
"Review Feature-04.03 (Marketing). Can we achieve 80% of the 
user value with 50% of the complexity? Suggest cuts."
```

---

## ? Validation & Quality

### Quality Gate Checklist

Before moving to next phase:

**Phase 1 -> 2** (Context -> Epics):
- [ ] System Overview clear to non-technical reader
- [ ] Glossary has all domain terms
- [ ] At least 10 questions in Open_Questions.md
- [ ] Tech Stack decisions documented

**Phase 2 -> 3** (Epics -> Features):
- [ ] 3-7 Epics defined (not too many)
- [ ] Epic dependencies mapped
- [ ] MVP vs Post-MVP scope clear
- [ ] No epic is "miscellaneous" or "other"

**Phase 3 -> 4** (Features -> Validation):
- [ ] All features have acceptance criteria
- [ ] Edge cases documented
- [ ] No "TBD" or "TODO" in spec
- [ ] Validation report run

**Phase 4 -> 5** (Validation -> Handoff):
- [ ] All P0 questions resolved
- [ ] Client approval documented
- [ ] Team reviewed for feasibility
- [ ] Development handoff complete

---

### Red Flags (Stop and Fix)

| Red Flag | Meaning | Action |
|:---|:---|:---|
| **10+ epics** | Scope creep or bad grouping | Consolidate or defer |
| **Feature with no epic** | Orphaned work | Create parent or delete |
| **50+ open questions** | Insufficient discovery | Schedule client intensive |
| **Epic changes daily** | Unstable foundation | Lock down and validate |
| **"TBD" in spec** | Not ready for dev | Hold handoff |
| **No decisions logged** | Audit trail missing | Backfill Decision_Log |

---

## ? Design & UX

### Device Strategy: Know Your Audience

**Assess Primary Usage Context First**:

**Ask Client**:
- What devices will 80% of users access from?
- Where will they use it (office, field, commute)?
- What's their typical connectivity (WiFi, LTE, 3G)?

**Common Patterns**:

| Project Type | Primary Device | Design Approach |
|:---|:---|:---|
| Consumer app | Mobile (60-80%) | Mobile-first |
| Business tool | Desktop (70%+) | Desktop-first, mobile-responsive |
| Field service | Mobile (90%+) | Mobile-only initially |
| Dashboard/Analytics | Desktop (80%+) | Desktop-optimized |
| Hybrid SaaS | Mixed (50/50) | True responsive (test both) |

**Mobile Considerations** (when relevant):
- Touch targets ?44px
- Readable without zoom (16px+ base font)
- Works on slow 3G
- High contrast for outdoor visibility

**Desktop Considerations** (when relevant):
- Keyboard shortcuts
- Mouse hover interactions
- Multi-window workflows
- Large data tables

**Note**: Document device strategy in Platform_Specification.md (under Constraints) or in 04_Designs/

---

### Don't Design by Committee

**Bad**:
```
"What do you think the dashboard should look like?"
(Gets 5 different opinions, analysis paralysis)
```

**Good**:
```
"Based on your requirements, here are 2 dashboard layouts 
(Option A: metrics-focused, Option B: action-focused). 
Which aligns better with your primary user workflow?"
```

**Provide options, not blank canvases.**

---

## ? Scope & Pricing

### The 50% Rule

**Reality**: First estimate is usually 2x optimistic

**Defense**:
- Spec everything before estimating
- Add buffer for unknowns
- Separate MVP from Phase 2

**For AI context**: "Assume we know 50% of the full story. What questions would de-risk the other 50%?"

---

### Saying No to Clients

**Framework**:
```
"That's a great idea! Let me show you the impact:

Option A: Include Feature X
- Timeline: +4 weeks
- Cost: +$15K
- Risk: Medium (new dependency)

Option B: Defer to Phase 2
- Timeline: No change
- Cost: No change
- Risk: Low

What matters more right now: speed to market or feature completeness?"
```

**Empower clients to make informed trade-offs.**

---

## ? Change Management

### When Client Changes Mind

**Don't**:
- Silently update spec
- Complain that "this was decided"

**Do**:
1. Log old decision in `Decision_Log.md` (Status: Superseded)
2. Create new decision entry
3. Ask AI: *"Client changed decision D-003. Analyze impact on all epics/features."*
4. Update Project_Plan with impact summary
5. Get client sign-off on changes

**Traceability prevents blame games.**

---

## ? Miscellaneous Tips

### Naming Conventions Matter

**Bad**: `stuff.md`, `doc2.md`, `final_FINAL_v3.md`

**Good**: `Epic-01_UserManagement.md`, `Feat-03.02_Calendar.md`

See: naming conventions in `CLAUDE.md`

---

### Templates are Living Documents

If you find yourself repeating work, update the relevant skill or template.

Example: You keep adding the same type of edge case that gap-analysis misses?
-> Note it in `00_Meta/Templates/Epic_Template.md` as a reminder

---

## ? Common Mistakes

| Mistake | Why It Happens | Fix |
|:---|:---|:---|
| **No Glossary** | Seems tedious | Start from Day 1, ask AI to extract terms |
| **Epic = Feature** | Confusion on granularity | Epic = group of 3-5 features |
| **Skipping Validation** | Pressure to move fast | Fast ? Right. Always validate. |
| **AI overwrite** | Trust AI blindly | **You are the human validator** |
| **Parallel docs** | "Quick client summary" | Slippery slope. Generate on-demand only. |
| **No question tracking** | Assume you'll remember | You won't. Use Open_Questions.md |

---

## ? Advanced Techniques

### Pattern: Decision Matrix

When client has options, create a table in `Client_Interactions.md`:

| ID | Decision Point | Option A | Option B | Option C | Chosen | Rationale |
|:---|:---|:---|:---|:---|:---|:---|
| MKT1 | Marketing ownership | Super Admin | Trainer | Both | A | Centralized control |

**Benefits**: Visual, scannable, great for meetings

---

### Pattern: Traceability Matrix

Map features -> client requirements:

| Client Requirement | Source | Epic | Features | Status |
|:---|:---|:---|:---|:---|
| "Coaches must clock in" | Email 2024-12-10 | Epic-03 | Feat-03.04 | [x] |
| "Parents approve purchases" | Kickoff transcript | Epic-01 | Feat-01.03 | [x] |
| "Export to Excel" | Client email | Epic-04 | Feat-04.06 | ? Design |

**When to use**: Large, compliance-heavy projects

---

### Pattern: Assumption Log

Separate from decisions (which are validated), track assumptions:

| ID | Assumption | Confidence | Validation Plan | Status |
|:---|:---|:---|:---|:---|
| A-001 | Users have stable internet | Medium | Test on 3G | Pending |
| A-002 | <100 concurrent users | High | Client confirmed | [x] |

**Why**: Makes hidden assumptions 