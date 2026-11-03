# 02_Epics -- All Active Specifications

This folder contains all spec files for the project. **Everything lives here.**

---

## What is an Epic?

An Epic covers a complete feature area of the application: what it does, who uses it, what's in scope, what's out of scope, and all the detail a developer needs.

Features are documented as **sections within each Epic file** -- there are no separate feature files. One Epic file = complete context for that feature area.

---

## File Naming

**Format:** `Epic-[NN]_[ShortName]_SPEC.md`

The `_SPEC` suffix signals the file is development-ready.

Examples:
- `Epic-01_User_Management_SPEC.md`
- `Epic-02_Event_Scheduling_SPEC.md`
- `Epic-03_Payments_SPEC.md`

---

## When to Create an Epic

Create an Epic when you have a logical grouping of related capabilities sharing a common business goal and a distinct area of the application.

**Sweet spot:** 3-7 Epics for most projects.
- Fewer than 3: Too coarse-grained -- break them down
- More than 10: Scope creep or bad grouping -- consolidate

---

## How to Create an Epic

Use the `epic-writer` skill:
> "Let's write Epic-03 for the payments area."

Or manually: copy `00_Meta/Templates/Epic_Template.md`, rename it, and fill in all sections.

---

## Epic Dependencies

Document dependencies in each Epic's Dependencies section:

```
Epic-01 (User Management) -- must exist before:
  -> Epic-02 (Event Scheduling) -- needs users
  -> Epic-03 (Payments) -- needs user accounts
```

---

## Related Files

- **Epic Template**: `00_Meta/Templates/Epic_Template.md`
- **Platform Specification**: `01_Context/Platform_Specification.md` (confirms scope before Epic work)
- **Active Task Tracking**: `00_Meta/Project_Plan.md`
