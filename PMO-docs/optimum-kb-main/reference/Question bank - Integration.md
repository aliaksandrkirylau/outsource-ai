Ported from Spec Framework v2 (00_Meta/QuestionBanks) on 2026-09-28. Generic, not about this project.

# Question Bank: API & Integration Projects

**Purpose**: Curated questions for API development and system integration projects

**Usage**: These questions focus on integration patterns, API design, data sync, and interoperability concerns.

---

## 1. Integration Type & Scope

### Integration Pattern
- What type of integration is this?
  - REST API development
  - Third-party API integration (consuming external APIs)
  - Webhook-based integration
  - ETL/data pipeline
  - iPaaS/middleware configuration (Zapier, Make, Workato)
  - Message queue/event-driven
  - Real-time sync (WebSockets, GraphQL subscriptions)

### Systems Involved
- What systems are being integrated?
- Which system is the source of truth for what data?
- Are all systems under your control or third-party?
- What existing APIs or integrations already exist?

### Integration Goals
- What problem does this integration solve?
- What data needs to flow between systems?
- One-way or bi-directional sync?
- Real-time or batch processing?
- Event-driven or scheduled?

---

## 2. API Design & Architecture (If Building API)

### API Type
- REST API, GraphQL API, or other?
- Public API, private API, or partner API?
- Synchronous (request/response) or asynchronous?
- Stateless or stateful?

### Resources & Endpoints
- What resources does the API expose (users, products, orders)?
- What operations per resource (CRUD)?
- Nested resources or flat structure?
- Bulk operations needed?

### Data Format
- Request/response format (JSON, XML, Protocol Buffers)?
- Date/time format standards (ISO 8601)?
- Pagination style (offset, cursor, page number)?
- Filtering and sorting capabilities?
- Field selection/sparse fieldsets?

### API Versioning
- API versioning strategy (URL, header, query param)?
- Breaking change policy?
- Deprecation timeline and process?
- How many versions supported concurrently?
- Version sunset communication?

---

## 3. Authentication & Authorization

### Authentication Method
- API key, OAuth 2.0, JWT, or other?
- Where are credentials passed (header, query, body)?
- Credential rotation policy?
- Multiple credentials per user/application?

### OAuth Implementation (if applicable)
- OAuth flows needed (authorization code, client credentials, implicit)?
- Scopes and permissions granularity?
- Token expiration (access token, refresh token)?
- Token revocation mechanism?

### Authorization
- Per-user permissions or per-application?
- Role-based access control (RBAC)?
- Fine-grained permissions (per resource/operation)?
- Tenant isolation (multi-tenant API)?
- Admin/super-user bypass capabilities?

### Security
- HTTPS only or HTTP allowed?
- IP whitelisting?
- Certificate pinning?
- Request signing (HMAC, JWS)?
- Encryption of sensitive fields?

---

## 4. Rate Limiting & Throttling

### Rate Limit Strategy
- Rate limits per endpoint or global?
- Rate limit tier (free, paid, enterprise)?
- Limit by time window (per second, minute, hour, day)?
- What happens when limit exceeded (429 error, queue)?

### Rate Limit Communication
- Rate limit headers (X-RateLimit-Remaining, etc.)?
- Retry-After header when limited?
- Advance notice of approaching limit?
- Rate limit visible in dashboard?

### Burst vs Sustained
- Burst limits vs sustained throughput?
- Token bucket vs fixed window?
- Can enterprise customers request higher limits?

---

## 5. Data Synchronization

### Sync Strategy
- Real-time sync or batch/scheduled?
- How often does sync occur (every 5 min, hourly, daily)?
- Full sync or incremental/delta sync?
- Change detection method (timestamps, version numbers, webhooks)?

### Conflict Resolution
- What happens when data conflicts between systems?
- Last-write-wins or merge strategy?
- Manual conflict resolution UI?
- Which system wins in conflicts (source of truth)?

### Data Transformation
- Is data transformed during sync?
- Field mapping between systems?
- Data validation rules?
- Default values for missing data?
- Enrichment from other sources?

### Sync Monitoring
- How is sync status tracked?
- Success/failure logging?
- Alert on sync failures?
- Sync history and audit trail?
- Retry policy on failures?

---

## 6. Error Handling & Retries

### Error Responses
- Standard error format (Problem Details, custom)?
- HTTP status codes used (4xx, 5xx)?
- Error codes and messages?
- Detailed error info or generic (security concern)?
- Error localization?

### Retry Strategy
- Which errors are retryable?
- Automatic retry on client or server?
- Exponential backoff strategy?
- Maximum retry attempts?
- Idempotency considerations?

### Failure Scenarios
- What happens if third-party API is down?
- Fallback or cached data available?
- Circuit breaker pattern?
- Dead letter queue for failed events?
- Alert humans on persistent failures?

---

## 7. Webhooks & Events (If Applicable)

### Webhook Strategy
- What events trigger webhooks?
- Webhook delivery guarantees (at-least-once, exactly-once)?
- Webhook payload format?
- Webhook signature for verification (HMAC)?

### Webhook Management
- How do users register webhook endpoints?
- Webhook URL validation?
- Retry policy for failed webhook deliveries?
- Webhook delivery logs and history?
- Webhook testing tools (replay, simulate)?

### Event Types
- What events are published?
- Event schema versioning?
- Event ordering guarantees?
- Event filtering or subscription options?

---

## 8. Documentation & Developer Experience

### API Documentation
- Auto-generated docs (OpenAPI/Swagger)?
- Interactive API explorer?
- Code examples in multiple languages?
- Postman collection or similar?
- Versioned documentation?

### Developer Portal
- Self-service API key creation?
- Usage dashboard for developers?
- Sandbox/test environment?
- Sample data for testing?
- API changelog and updates?

### Guides & Tutorials
- Getting started guide?
- Common use case tutorials?
- Best practices documentation?
- Troubleshooting guide?
- Migration guides (between versions)?

---

## 9. Testing & Validation

### Test Environment
- Sandbox or staging API?
- Test credentials separate from production?
- Test data available?
- Can test environment be reset?

### Data Validation
- Input validation rules?
- Schema validation (JSON Schema)?
- Required vs optional fields?
- Data type enforcement?
- Max string lengths, number ranges?

### Testing Support
- Mock API for client testing?
- Webhook testing tools?
- API monitoring and uptime?
- Performance/load testing results?

---

## 10. Performance & Scalability

### Expected Load
- Expected requests per second/minute?
- Peak load times?
- Data volume per request?
- Concurrent connection limits?

### Performance Targets
- Target response time (p50, p95, p99)?
- Acceptable timeout duration?
- Throughput requirements?
- Latency requirements for sync?

### Scalability
- Auto-scaling capabilities?
- Horizontal or vertical scaling?
- Database connection pooling?
- Caching strategy (CDN, Redis)?
- Query optimization approach?

---

## 11. Monitoring & Observability

### Logging
- What is logged (all requests, errors only)?
- Log retention period?
- Structured logging format?
- PII scrubbing in logs?
- Centralized log aggregation?

### Metrics & Alerting
- What metrics are tracked?
  - Request count, error rate, latency
  - Rate limit hits, auth failures
  - Sync success/failure rates
- Real-time monitoring dashboard?
- Alert thresholds and notifications?
- On-call rotation for critical alerts?

### Tracing
- Distributed tracing (Jaeger, Zipkin)?
- Request ID propagation?
- Cross-system trace correlation?

### Customer-Facing Monitoring
- Status page for API uptime?
- Historical uptime data?
- Scheduled maintenance notifications?
- Incident postmortems?

---

## 12. Data Governance & Compliance

### Data Handling
- What data is transmitted (PII, PHI, PCI)?
- Data encryption in transit (TLS version)?
- Data encryption at rest?
- Data retention policies?
- Data deletion/purging process?

### Compliance Requirements
- GDPR compliance (data subject rights)?
- HIPAA compliance (if health data)?
- PCI-DSS compliance (if payment data)?
- SOC 2 or ISO certifications?
- Regional data residency requirements?

### Audit & Traceability
- Audit logs for all data access?
- Change tracking (who, what, when)?
- Data lineage tracking?
- Compliance reporting capabilities?

---

## 13. Third-Party API Integration (Consuming APIs)

### API Selection
- Which third-party API (Stripe, Twilio, SendGrid, etc.)?
- Official SDK available or raw HTTP?
- API stability and versioning?
- Pricing model (per call, monthly, tiered)?

### API Limitations
- Rate limits from third-party?
- Usage quotas or caps?
- Geographic restrictions?
- Deprecation timeline awareness?

### Failure Handling
- What's backup plan if third-party API is down?
- Cached data acceptable?
- Alternative provider as fallback?
- Degraded functionality mode?

### Cost Management
- API call costs monitoring?
- Usage optimization strategies?
- Cost alert thresholds?
- Batch operations to reduce calls?

---

## 14. Deployment & DevOps

### Deployment Strategy
- Blue-green deployment?
- Canary releases?
- Feature flags for gradual rollout?
- Rollback procedure?

### Environment Management
- Development, staging, production environments?
- Environment parity?
- Secrets management (API keys, credentials)?
- Configuration management?

### CI/CD
- Automated testing in pipeline?
- Contract testing (Pact)?
- Integration testing before deploy?
- Automated deployment or manual gate?

---

## 15. Migration & Backwards Compatibility

### Migration Strategy (If Replacing Existing Integration)
- Parallel run of old and new integration?
- Migration timeline and phases?
- Data migration required?
- Cutover plan and rollback?

### Backwards Compatibility
- Must support existing clients?
- Deprecation period for old endpoints?
- Communication plan for breaking changes?
- Version support matrix?

---

## Integration-Specific MVP Guidance

### Must-Have for MVP
- Core data sync (one-way or bi-directional)
- Basic authentication
- Error handling and logging
- Essential endpoints/operations
- Documentation (at least basic)

### Probably MVP
- Rate limiting (even simple)
- Webhook support (if event-driven)
- Basic monitoring
- Test environment
- Retry logic

### Likely Post-MVP
- Advanced filtering/querying
- Bulk operations
- Comprehensive SDKs
- Advanced analytics
- Multi-version support
- GraphQL (if starting with REST)

---

## Integration Project Tips

1. **Start with data mapping** - Document every field and transformation
2. **Authentication first** - Get security right from the start
3. **Error handling is critical** - Integrations fail, plan for it
4. **Idempotency matters** - Retry logic requires idempotent operations
5. **Test edge cases** - Empty responses, malformed data, timeouts
6. **Monitor everything** - You can't fix what you can't see
7. **Version early** - Easier to add versioning from start than retrofit
8. **Document assumptions** - What happens when X fails or is missing?

---

## Common Integration Patterns

| Pattern | Use Case | Example |
|:---|:---|:---|
| **REST API** | Exposing data/operations | CRM API for partners |
| **Webhook** | Real-time event notifications | Payment successful |
| **ETL/Batch** | Scheduled bulk data sync | Nightly data warehouse load |
| **Event Stream** | High-volume event processing | User activity tracking |
| **iPaaS** | No-code integrations | Zapier connector |
| **Middleware** | Legacy system integration | SOAP to REST translator |
| **GraphQL** | Flexible client-driven queries | Mobile app backend |
