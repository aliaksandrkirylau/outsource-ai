# CLAUDE.md — <project name>

Guidance for every agent working in this project. Generated at stage 0 by the
project analyst; extended by anyone who hits a new trap.

## What this project is

<two or three sentences; full picture in `PROJECT-PROFILE.md` §1–2>

Read `HANDOFF.md` first — it is the map of the current state.

## Components

| Folder | What | Stack | Own rules |
|---|---|---|---|

Run every git command inside the component's own repository.

## Commands

The verification matrix is in `PROJECT-PROFILE.md` §3. Repeat here only the
two or three commands every session needs.

## Cross-cutting rules

- <rules that hold across component boundaries: who validates, who adds the
  envelope, where the data store is touched, how tenancy is scoped>

## Pitfalls

- <known traps — mirror of `PROJECT-PROFILE.md` §9, with the "how it fails
  silently" detail>
- <known, intentional breakage — do not fix>

## Code style constraints

- No fabricated fallbacks to mask missing data — "not available", never a
  plausible value.
- No silent excepts and no hidden retries — fail fast.
- Never rename existing environment variables.
- No ticket keys in code comments or docstrings.
- <project-specific: language of user-facing strings, comment density, …>

## Pipeline rules

- One ticket at a time per agent; strict scope; findings are logged, not fixed
  (`/work-ticket`).
- Client specification is implemented literally; discrepancies go to
  `SPEC-DISCREPANCIES.md`.
- Evidence before claims (`verification-before-completion`).
- Root cause before fixes (`systematic-debugging`).
- Git and tracker writes: dispatcher only.
- Forbidden actions: `PROJECT-PROFILE.md` §7.
