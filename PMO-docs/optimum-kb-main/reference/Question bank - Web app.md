Ported from Spec Framework v2 (00_Meta/QuestionBanks) on 2026-09-28. Generic, not about this project.

# Question Bank: Web Application Discovery

**Purpose**: Curated questions for web application projects to uncover requirements

**Usage**: Select relevant questions based on client maturity level. Batch for discovery sessions.

---

## 1. Business & Goals (Foundation)

### Problem Definition
- What problem are you solving for your users?
- Who experiences this problem most acutely?
- How do they currently solve this problem (workarounds)?
- What's the cost of NOT solving this problem?

### Success Metrics
- How will you measure if this project is successful?
- What user behavior indicates value (DAU, conversion, retention)?
- What's the target timeline for seeing results?
- What's the acceptable cost per user/transaction?

### Business Model
- How does this application generate revenue?
- Who pays: end users, advertisers, subscribers, other?
- What's the pricing model (freemium, subscription, one-time, usage-based)?
- What's the projected user volume (Year 1, Year 2, Year 5)?

---

## 2. User Roles & Permissions

### User Types
- What distinct user roles exist? (Admin, User, Guest, etc.)
- What can each role do that others cannot?
- Can users have multiple roles?
- Can roles be customized per organization/tenant?

### Authentication
- How do users create accounts (email, social login, SSO, invitation)?
- What information is required to register?
- What password requirements (length, complexity, rotation)?
- Do you need two-factor authentication (2FA)?
- What happens if a user forgets their password?

### Authorization
- What can anonymous visitors see/do?
- What requires authentication?
- Are there tiered permissions (basic vs premium users)?
- Who can invite new users?

---

## 3. Core Features & Flows

### Primary Use Case
- What is the #1 thing users will do in this app?
- Walk me through a typical user session from login to logout
- What's the happy path (ideal flow)?
- What are the top 3-5 features users will use daily?

### Data Management
- What data do users create/upload?
- Who owns the data (user, organization, platform)?
- Can users edit data after creation?
- Can users delete data? What happens (hard delete, soft delete, anonymize)?
- Do you need version history / audit logs?

### Search & Discovery
- How do users find content/data in the app?
- What fields are searchable?
- Do you need filters (date, category, status, etc.)?
- Do you need sorting?
- Do you need autocomplete/suggestions?

---

## 4. UI/UX & Design

### Visual Design
- Do you have brand guidelines (colors, fonts, logos)?
- Do you have design preferences (modern, minimal, corporate)?
- Do you have example sites/apps you like?
- Do you have existing assets (logo, icons) or need design from scratch?

### Responsiveness
- What devices must be supported (desktop, tablet, mobile)?
- What's the primary device (80% of users)?
- What screen sizes must work (mobile-first)?
- Does UX differ significantly by device?

### Accessibility
- Do you need WCAG compliance (Level A, AA, AAA)?
- Do you need screen reader support?
- Do you need keyboard-only navigation?
- Are there regulatory requirements (government, healthcare)?

---

## 5. Technical Requirements

### Performance
- How many concurrent users do you expect?
- What's acceptable page load time (<2s, <5s)?
- What geographic regions (one country, global)?
- Do you need offline mode or PWA capabilities?

### Integrations
- What third-party services must integrate (Stripe, Google Analytics, etc.)?
- Do you have existing systems (CRM, ERP, database) to connect to?
- Do you need an API for other systems to consume?
- Do you need webhooks or real-time notifications?

### Data & Storage
- What's the expected data volume (MB, GB, TB)?
- Do users upload files (images, videos, documents)?
- What file types and size limits?
- Do you need CDN for media delivery?

### Security & Compliance
- Are you handling sensitive data (PII, health, financial)?
- What compliance requirements (GDPR, HIPAA, SOC 2, PCI-DSS)?
- Do you need data encryption (at rest, in transit)?
- Do you need penetration testing or security audits?

---

## 6. Notifications & Communication

### Email
- What emails does the system send (welcome, password reset, notifications)?
- Transactional vs marketing emails?
- What email service (SendGrid, Mailgun, custom SMTP)?
- Do users control email preferences?

### In-App Notifications
- Do you need real-time notifications (WebSockets)?
- What events trigger notifications?
- Do users control notification preferences?

### SMS / Push
- Do you need SMS notifications?
- Do you need browser push notifications?
- What's the trigger criteria?

---

## 7. Administration & Analytics

### Admin Panel
- What admin capabilities are needed (user management, content moderation)?
- Who has admin access?
- Do you need audit logs (who changed what, when)?
- Do you need bulk operations (mass delete, export)?

### Analytics
- What metrics do you need to track?
- Do you need built-in dashboards or external tools (Google Analytics)?
- Do you need reporting (daily/weekly/monthly)?
- Do you need data export (CSV, PDF, Excel)?

---

## 8. Payments & Monetization (If Applicable)

### Payment Processing
- What payment methods (credit card, PayPal, bank transfer)?
- What payment gateway (Stripe, Square, Braintree)?
- Do you need recurring billing (subscriptions)?
- Do you need invoicing?

### Pricing Model
- Free tier? What limitations?
- Subscription tiers? What differentiates them?
- Usage-based pricing?
- Do you need coupons/promotions?

### Transactions
- Who receives payments (you, or facilitated between users)?
- Do you take a platform fee?
- What currency/currencies?
- Do you need refund handling?

---

## 9. Content Management

### Content Types
- What types of content exist (blog posts, products, events)?
- Who creates content (admin, users, both)?
- Do you need rich text editing (WYSIWYG)?
- Do you need media management (image galleries, video embeds)?

### Content Workflow
- Does content need approval before publishing?
- Do you need draft/published states?
- Do you need scheduled publishing?
- Do you need content versioning?

---

## 10. Localization & Internationalization (If Applicable)

### Language
- What languages must be supported?
- Is MVP English-only with multi-language later?
- Who provides translations?
- Do users select language or auto-detect?

### Regional Considerations
- Different date/time/currency formats by region?
- Different content by region?
- Do you need geo-based restrictions?

---

## 11. MVP Scoping

### Must-Have vs Nice-to-Have
- What features are absolutely critical for launch?
- What can wait for v1.1 or v2?
- What's the launch date goal?
- What's the minimum viable feature set?

### Phasing
- Should we build in phases?
- What Phase 1, Phase 2, Phase 3?
- What triggers moving to next phase?

---

## 12. Edge Cases & Constraints

### Limits & Restrictions
- Max users per account/organization?
- Rate limits on API calls?
- File size upload limits?
- Data retention policies?

### Error Scenarios
- What happens when payment fails?
- What if user loses internet mid-action?
- What if third-party service is down?
- What if user reaches storage limit?

---

## Using This Question Bank

### For Level 1 (Idea Only) Clients
**Use**: Sections 1-3 heavily (80% of questions)  
**Goal**: Uncover the basics

### For Level 2 (Partial Vision) Clients
**Use**: Sections 3-6 (fill gaps)  
**Goal**: Refine and validate assumptions

### For Level 3+ Clients
**Use**: Sections 7-12 (edge cases, polish)  
**Goal**: Depth and completeness

---

##Tips for Discovery Sessions

1. **Don't ask all 100+ questions** - Pick 20-30 most relevant
2. **Batch by topic** - "Let's talk about users and authentication first"
3. **Listen for implied answers** - One answer often answers 5 questions
4. **Use examples** - "Like how Uber does X, or more like Airbnb Y?"
5. **Prioritize ruthlessly** - Some questions are Phase 2 concerns
