---
name: client-summary
description: Generate a plain-language summary of an Epic or the full platform for client review. Strips technical spec language and presents what's being built in terms the client understands. Use before sending Epic specs to a client or preparing for a review meeting.
---

# Client Summary Skill

Translate spec language into plain client-facing summaries. What you're sharing with a developer is not what you share with a client.

## When Triggered

User says: "write a client summary", "summarize this epic for the client", "create an executive summary", "prepare something to send Dale", "make this client-readable" — or when preparing materials for a client review meeting.

## What This Is Not

This is NOT a replacement for the spec. The Epic file remains the source of truth. This is a presentation layer — a readable overview the client can confirm without wading through acceptance criteria tables.

## Step 1 — Identify the Target

What to summarize:
- **Single Epic**: One Epic file → one summary doc
- **Multiple Epics**: Several Epics → one summary per Epic, or a combined overview
- **Full platform overview**: Platform Specification → executive summary of the whole product

Read the target file(s). Also read `01_Context/Platform_Specification.md` for context on the project name, client name, and overall framing.

## Step 2 — Write the Summary

### For a Single Epic

```markdown
# [Epic Name] — Overview
**Project**: [Project Name]
**Prepared for**: [Client Name]
**Date**: [Date]

## What This Covers

[1-2 paragraphs in plain language. What area of the product does this epic address? What will users be able to do when it's built? Write as if explaining to a smart non-technical person.]

## What's Included

[Bullet list of the main capabilities — written in user terms, not spec terms]
- Users can [action]
- [Role] will be able to [action]
- The system will [behavior]

## What's Not Included (in this version)

[Brief list of explicitly deferred items — helps set expectations]
- [Item] — planned for a later version
- [Item] — out of scope for now

## Key Questions for You

[List any open questions or assumptions that need client confirmation. Keep to P0 and P1 only.]
- [Question or assumption needing confirmation]

## What We Need From You

[Any content, decisions, or approvals the client needs to provide]
- Confirm: [specific item]
- Provide: [asset or information needed]
```

### For a Full Platform Overview

```markdown
# [Project Name] — Platform Overview
**Prepared for**: [Client Name]
**Date**: [Date]
**Status**: [e.g., "Foundation confirmed, Epic work in progress"]

## What We're Building

[2-3 paragraphs. What is this platform, who is it for, what problem does it solve. Business language only.]

## Who Uses It

[Table or brief description of each user role and what they do]

## What's in the First Version (MVP)

[Plain-language list of the main areas/capabilities being built]

## What's Coming Later

[Brief note on what's explicitly deferred to a later version]

## Current Status

[Progress summary: which areas are spec'd, which are in progress, what's next]

## Open Items for Your Review

[List of decisions or confirmations still needed from the client]
```

## Step 3 — Tone and Language Rules

**Write for a business person, not a developer:**
- ❌ "The system implements role-based access control with JWT authentication"
- ✅ "Only authorized team members can access each area of the platform"

**Feature names in plain language:**
- ❌ "Epic-02: Event Management Scheduling SPEC"
- ✅ "Training Session Booking"

**No spec jargon:**
- Don't use: Epic, User Story, Acceptance Criteria, Given/When/Then, CRUD, API, schema
- Do use: feature, capability, users can, the system will, included/not included

**Be honest about what's not done:**
- If something is an assumption, say "We've assumed X — please confirm"
- If something is out of scope, be clear and give a brief reason

## Step 4 — Output Options

Ask the user how they want to use this:
1. **For a client meeting** — produce the summary as a file to share/walk through
2. **To send by email** — produce a shorter version suitable for email body
3. **For async review** — produce a clean file the client can comment on

Save the output to `03_Discussi