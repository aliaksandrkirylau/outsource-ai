# Question Bank: SaaS Product Discovery

**Purpose**: Curated questions for Software-as-a-Service products

**Usage**: Select relevant questions based on project unknowns. SaaS has unique multi-tenancy, subscription, and scalability concerns.

---

## 1. Multi-Tenancy & Organization Structure

### Tenant Model
- [ ] What is a "tenant" in this system (company, team, workspace)?
- [ ] Can users belong to multiple tenants?
- [ ] Can users switch between tenants easily?
- [ ] What's the max tenants per user?
- [ ] Are there tenant-to-tenant relationships (parent/child orgs)?

### Data Isolation
- [ ] How is data isolated between tenants?
- [ ] Can tenants see each other's data ever (marketplace, directory)?
- [ ] What data is shared across tenants (templates, resources)?
- [ ] How is data segregation enforced (database, schema, row-level)?

### Tenant Configuration
- [ ] Can tenants customize features per their needs?
- [ ] Can tenants upload custom branding (logo, colors)?
- [ ] Can tenants configure workflows or rules?
- [ ] Custom domains per tenant (tenant.yourapp.com)?
- [ ] White-labeling capabilities?

---

## 2. Subscription & Billing

### Pricing Model
- [ ] What pricing tiers exist (Free, Pro, Enterprise)?
- [ ] What differentiates each tier (features, limits, support)?
- [ ] Per-user pricing, per-tenant pricing, or usage-based?
- [ ] Are there annual vs monthly pricing options?
- [ ] Volume discounts or enterprise pricing?

### Billing Mechanics
- [ ] What payment gateway (Stripe, Chargebee, Paddle)?
- [ ] What payment methods (credit card, invoice, PO)?
- [ ] Billing cycle (monthly, annual, usage-based)?
- [ ] Proration on plan changes?
- [ ] Tax calculation and collection?

### Trial & Freemium
- [ ] Free trial period? How long?
- [ ] What happens when trial ends?
- [ ] Credit card required for trial?
- [ ] Freemium tier with limitations?
- [ ] Conversion tactics (paywall, upgrade prompts)?

### Subscription Management
- [ ] Can users upgrade/downgrade plans?
- [ ] Immediate change or at billing cycle end?
- [ ] Can users add/remove seats (user licenses)?
- [ ] What happens when downgrading (feature loss, data access)?
- [ ] Cancellation process and timing?
- [ ] Reactivation after cancellation?

---

## 3. User Management & Team Collaboration

### User Roles & Permissions
- [ ] What user roles exist (Owner, Admin, Member, Guest)?
- [ ] What can each role do?
- [ ] Can roles be customized per tenant?
- [ ] Role-based or permission-based access control?
- [ ] Can permissions be set at team/project level?

### Team Invitations
- [ ] How are new users invited (email, link, bulk import)?
- [ ] Who can invite users?
- [ ] Email verification required?
- [ ] Approval workflow for new users?
- [ ] Domain-based auto-join (anyone @company.com)?

### User Onboarding
- [ ] Onboarding flow for new users?
- [ ] Different onboarding per role?
- [ ] Interactive tutorial or guided tour?
- [ ] Sample data or templates for new tenants?
- [ ] Required setup steps before using product?

### Seat Management
- [ ] How are seats/licenses managed?
- [ ] Automatic billing when adding users?
- [ ] What happens when seat limit reached?
- [ ] Deactivating vs deleting users?
- [ ] Transferring user licenses?

---

## 4. Single Sign-On & Enterprise Auth

### SSO Requirements
- [ ] SAML-based SSO needed?
- [ ] OAuth/OIDC support?
- [ ] Which identity providers (Okta, Azure AD, Google Workspace)?
- [ ] Just-in-time (JIT) user provisioning?
- [ ] SSO for specific plans only (Enterprise tier)?

### Directory Integration
- [ ] SCIM for user provisioning?
- [ ] Auto-sync with directory (add/remove/update users)?
- [ ] Group/team sync from directory?
- [ ] Role mapping from identity provider?

### Session Management
- [ ] Session timeout policies?
- [ ] Can enterprise customers enforce session length?
- [ ] Enforce re-authentication frequency?
- [ ] Multi-device session limits?

---

## 5. Usage Limits & Quotas

### Resource Limits
- [ ] What resources have limits (users, storage, API calls)?
- [ ] Limits per plan tier?
- [ ] Hard limits (block) or soft limits (charge overage)?
- [ ] How are users notified approaching limits?
- [ ] Grace period when exceeding limits?

### Usage Tracking
- [ ] Real-time usage visibility for users?
- [ ] Usage dashboard or reports?
- [ ] Usage-based billing alerts?
- [ ] Historical usage data retention?

### Overage Handling
- [ ] What happens when limits exceeded?
- [ ] Overage charges or upgrade required?
- [ ] Automatic scaling or manual intervention?
- [ ] Can users set spending caps?

---

## 6. Self-Service & Account Management

### Account Settings
- [ ] What can users configure themselves?
- [ ] Billing and payment info self-service?
- [ ] Plan upgrades self-service or sales-assisted?
- [ ] Invoice access and download?
- [ ] Payment history and receipts?

### Subscription Changes
- [ ] Can users cancel without contacting support?
- [ ] Cancellation feedback collection?
- [ ] Win-back offers on cancellation?
- [ ] Pause subscription option?
- [ ] Immediate cancellation or end-of-period?

### Data Export & Portability
- [ ] Can users export their data?
- [ ] What format (CSV, JSON, PDF)?
- [ ] Complete data export or selective?
- [ ] API for data extraction?
- [ ] Compliance with data portability regulations (GDPR)?

---

## 7. Compliance & Security (SaaS-Specific)

### Data Residency
- [ ] Where is data stored (US, EU, Asia)?
- [ ] Multi-region hosting?
- [ ] Can enterprise customers choose data region?
- [ ] Data sovereignty requirements?

### Compliance Certifications
- [ ] SOC 2 Type I / Type II needed?
- [ ] ISO 27001 certification?
- [ ] GDPR compliance?
- [ ] HIPAA compliance (if health data)?
- [ ] PCI-DSS (if handling payments)?
- [ ] Industry-specific certifications?

### Security Features
- [ ] Data encryption at rest and in transit?
- [ ] Encryption key management approach?
- [ ] Customer-managed encryption keys (CMEK)?
- [ ] Security audit logs?
- [ ] IP whitelisting/blacklisting?
- [ ] Two-factor authentication (2FA) enforcement?

### Penetration Testing & Audits
- [ ] Regular penetration testing?
- [ ] Bug bounty program?
- [ ] Third-party security audits?
- [ ] Vulnerability disclosure policy?

---

## 8. Scalability & Performance

### Expected Scale
- [ ] How many tenants at launch, Year 1, Year 3?
- [ ] Average users per tenant?
- [ ] Expected data volume per tenant?
- [ ] Peak usage patterns (time of day, seasonality)?

### Performance SLAs
- [ ] Uptime commitment (99.9%, 99.99%)?
- [ ] Response time guarantees?
- [ ] Consequences of SLA breaches (credits, refunds)?
- [ ] Monitoring and status page?

### Infrastructure
- [ ] Cloud provider (AWS, Azure, GCP)?
- [ ] Multi-region for redundancy?
- [ ] CDN for global performance?
- [ ] Auto-scaling capabilities?
- [ ] Database sharding strategy?

---

## 9. API & Integrations

### Public API
- [ ] REST API for customer integrations?
- [ ] GraphQL API?
- [ ] API documentation (auto-generated)?
- [ ] API versioning strategy?
- [ ] Sandbox/test environment?

### API Access
- [ ] API access per plan tier?
- [ ] API rate limiting?
- [ ] API keys vs OAuth for authentication?
- [ ] Webhook support?
- [ ] Real-time API (WebSockets)?

### Integration Marketplace
- [ ] Pre-built integrations with other tools?
- [ ] Which tools (Salesforce, Slack, Zapier, etc.)?
- [ ] Custom integration development by partners?
- [ ] Integration marketplace or directory?
- [ ] OAuth apps by third parties?

---

## 10. Customer Success & Support

### Support Tiers
- [ ] Support included in all plans or paid add-on?
- [ ] Different support levels per tier (email, chat, phone)?
- [ ] Response time commitments (SLA)?
- [ ] Business hours or 24/7 support?
- [ ] Dedicated support for enterprise?

### Self-Service Support
- [ ] Knowledge base or help center?
- [ ] Community forum?
- [ ] Video tutorials?
- [ ] In-app contextual help?
- [ ] Chatbot or automated support?

### Customer Success
- [ ] Onboarding assistance for enterprise?
- [ ] Dedicated customer success manager?
- [ ] Regular business reviews?
- [ ] Training and certification programs?
- [ ] Proactive health monitoring and outreach?

---

## 11. Analytics & Reporting (Admin/Owner View)

### Tenant Analytics
- [ ] Usage analytics per tenant?
- [ ] User activity tracking?
- [ ] Feature adoption metrics?
- [ ] Which metrics are most important?

### Admin Dashboards
- [ ] Usage dashboard for tenant admins?
- [ ] Team productivity or activity reports?
- [ ] Billing and cost reports?
- [ ] Exportable reports?
- [ ] Scheduled report delivery?

### Product Analytics
- [ ] What events to track for product insights?
- [ ] Funnel analysis?
- [ ] Cohort analysis?
- [ ] Churn prediction?
- [ ] NPS or satisfaction surveys?

---

## 12. Notification & Communication

### Transactional Emails
- [ ] What emails does system send?
  - Welcome, email verification?
  - Password reset, security alerts?
  - Billing notifications, invoices?
  - Usage limit warnings?
  - Subscription renewal reminders?

### Product Updates
- [ ] In-app announcements for new features?
- [ ] Release notes or changelog?
- [ ] Email newsletters for updates?
- [ ] Notification preferences per user?

### System Status
- [ ] Status page for outages/maintenance?
- [ ] Incident notifications?
- [ ] Subscribe to status updates?
- [ ] Historical uptime data?

---

## 13. Data Backup & Disaster Recovery

### Backup Strategy
- [ ] Automated backups frequency?
- [ ] Backup retention period?
- [ ] Can customers trigger manual backups?
- [ ] Point-in-time recovery?

### Disaster Recovery
- [ ] What's the Recovery Time Objective (RTO)?
- [ ] What's the Recovery Point Objective (RPO)?
- [ ] Disaster recovery testing frequency?
- [ ] Failover to secondary region?
- [ ] Customer-visible DR documentation?

### Data Deletion
- [ ] What happens when tenant cancels?
- [ ] Grace period before data deletion?
- [ ] Soft delete with recovery window?
- [ ] Hard delete and data purging process?
- [ ] Compliance with right-to-be-forgotten (GDPR)?

---

## 14. Marketplace & Partner Ecosystem

### Partner Program
- [ ] Reseller or referral partner program?
- [ ] Partner portal for managing customers?
- [ ] Commission structure?
- [ ] White-label for partners?

### App Marketplace
- [ ] Third-party apps or extensions?
- [ ] App review and approval process?
- [ ] Revenue share for marketplace apps?
- [ ] App analytics for developers?

### System Integrator Partnerships
- [ ] Consulting partners for implementation?
- [ ] Certification program for partners?
- [ ] Partner-led implementations?

---

## 15. Go-to-Market & Growth

### Sales Model
- [ ] Self-serve signup or sales-assisted?
- [ ] Product-led growth (PLG)?
- [ ] Enterprise sales motion?
- [ ] Demo environment or sandbox?

### Trial-to-Paid Conversion
- [ ] Trial conversion tactics?
- [ ] Upgrade prompts and CTAs?
- [ ] Feature gating strategy?
- [ ] Sales hand-off from trial?

### Customer Acquisition
- [ ] Referral program?
- [ ] Affiliate program?
- [ ] Free tier as acquisition channel?
- [ ] Viral/social features for growth?

### Churn Prevention
- [ ] Churn prediction and alerts?
- [ ] Win-back campaigns?
- [ ] Exit surveys and feedback?
- [ ] Downgrade option vs full cancellation?

---

## SaaS-Specific MVP Guidance

### Must-Have for MVP
- Core product value
- Single tenant model (can add multi-tenancy later)
- Basic user roles (Owner/Admin/Member)
- Self-service signup and payment
- Essential security (encryption, auth)
- Basic support channel (email)

### Probably MVP
- Free trial (crucial for conversion)
- 2-3 pricing tiers
- Usage limits per tier
- In-app help/documentation
- Basic analytics dashboard

### Likely Post-MVP
- SSO/SAML (build when enterprise customers demand it)
- Advanced permissioning
- API and webhooks (unless core to product)
- Integration marketplace
- White-labeling
- Multi-region hosting
- SOC 2 compliance (start process early, certify later)

---

## SaaS Discovery Tips

1. **Start with tenant model** - Single most important SaaS decision
2. **Don't over-build permissions** - Start simple, add complexity when needed
3. **Self-service is key** - Reduce support overhead from day one
4. **Billing is complex** - Plan more time than you think
5. **Security/compliance** - Know what's needed for target market (SMB vs Enterprise)
6. **Usage limits drive upgrades** - Design thoughtfully
7. **Churn is the enemy** - Build retention features early

---

## SaaS vs Web App Differences

| Aspect | Traditional Web App | SaaS Product |
|:---|:---|:---|
| **Users** | Single organization | Multiple organizations (tenants) |
| **Billing** | One-time or project-based | Recurring subscriptions |
| **Data** | Centralized | Isolated per tenant |
| **Access** | Role-based | Tenant + role-based |
| **Compliance** | Project-specific | Multi-tenant compliance (SOC 2, etc.) |
| **Support** | Project support | Scaled customer support |
| **Growth** | Feature adoption | New tenant acquisition + retention |

---

**Related**:
- [Web App Questions](Web_App_Questions.md)
- [Mobile App Questions](Mobile_App_Questions.md)
- [Integration Questions](Integration_Questions.md)
- [Open Questions Template](../../03_Discussions/Open_Questions.md)


