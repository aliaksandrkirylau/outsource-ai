# Troubleshooting

**What to do when Claude sessions go wrong — and manual prompt patterns for tasks that don't have a skill.**

---

## Common Failure Modes

### Claude Ignored the 8-Step Loop

**Symptom:** Claude jumped straight to writing spec content without proposing a plan or waiting for approval.

**Why it happens:** Context overflow in long sessions. CLAUDE.md instructions get deprioritized.

**Fix:**
> "Stop. Before continuing, check CLAUDE.md and Project_Plan.md. Propose a plan for the next step and wait for my approval."

For very long sessions, start fresh:
> "New session. Read CLAUDE.md and Project_Plan.md. Tell me what's in progress and propose the next step."

---

### A Skill Didn't Trigger

**Symptom:** Asked for a gap analysis (or other skill task) and Claude responded generically instead of running the structured skill process.

**Why it happens:** Skill wasn't loaded, or the phrasing wasn't explicit enough.

**Fix:**
1. Check the Cowork Skills panel — confirm the skill is loaded.
2. Be explicit: `"Run the gap-analysis skill on Epic-02. Follow the skill's process."`
3. If not loaded: upload `.claude/skills/[skill-name]/SKILL.md` via the Skills panel.

---

### Spec Drift — Claude Added Scope That Wasn't Approved

**Symptom:** Spec contains features or detail that weren't discussed or approved.

**Fix:**
1. Point to the section: `"This wasn't in our approved scope: [paste]. Remove it."`
2. Run scope-audit: `"Run scope-audit on Epic-03. Flag everything not in the confirmed Platform Specification."`
3. For recurring issues, add a constraint: `"Don't add scope that isn't explicitly confirmed. Log it as an Open Question instead."`

---

### Spec Is Too Implementation-Heavy

**Symptom:** A section reads like a technical design doc — APIs, schemas, specific libraries.

**Fix:**
> "Review this section for spec/dev boundary violations. Remove implementation details and replace with user-facing requirements."

See `CLAUDE.md` → Spec/Dev Boundary for examples.

---

### Context Lost Between Sessions

**Symptom:** New session, Claude doesn't know what was decided or what's in progress.

**Why it happens:** Claude sessions don't share context by default.

**Fix:** Start every session with:
> "New session. Read CLAUDE.md and 00_Meta/Project_Plan.md. Summarize current state and what's next."

If decisions from the previous session weren't logged:
> "We decided [X] last session. Log it in Decision_Log.md: [decision, rationale, who confirmed]."

---

### Claude Keeps Asking Already-Decided Questions

**Symptom:** Claude keeps asking about things confirmed in a previous session.

**Fix:**
> "This was already decided — check 03_Discussions/Decision_Log.md before asking again."

If the decision isn't in the log, that's the real problem — log it now.

---

### Open Questions Keep Growing Without Resolution

**Symptom:** Open_Questions.md has 20+ items, many old, nothing getting resolved.

**Fix:**
> "Review Open_Questions.md. Check which P0 and P1 items are already answered in Decision_Log.md. Update accordingly."

Then use `workshop-prep` to batch remaining questions for the next client call.

**Red flag**: 50+ open questions = insufficient discovery. Schedule a client workshop before continuing Epic work.

---

### Epic Is Getting Too Large

**Symptom:** Epic file approaching 15+ features, hard to navigate.

**Fix:** Run scope-audit first — most oversize Epics contain post-MVP features.
> "Run scope-audit on Epic-05. It's too large. Identify what can be deferred without blocking MVP."

---

### Contradictions Between Spec Files

**Symptom:** Something in an Epic conflicts with the Platform Specification, or two Epics describe the same behavior differently.

**Fix:**
> "There's a conflict between [A] and [B]: [describe it]. Which is correct? Log as an Open Question until confirmed."

After client confirmation, update and log the decision.

---

## Encoding Issues (Windows Filesystem)

### Root Cause

Framework files live on Windows but Claude writes them from Linux. Any tool on the Windows side that reads those files without explicit UTF-8 encoding (PowerShell's default, some VS Code formatters, markdown linters) will misread non-ASCII bytes as Windows-1252, then re-save the result — double or triple encoding every `—`, `->`, `"`, etc. into garbage like `Ã¢â‚¬"`.

### Prevention (preferred)

**Don't use non-ASCII characters in framework files.** Use ASCII equivalents instead:

| Instead of | Use |
|:---|:---|
| `—` (em dash) | ` - ` or ` -- ` |
| `->` arrow `→` | `->` |
| `"` `"` smart quotes | `"` |
| `'` `'` smart quotes | `'` |

Framework files are read by AI, not typeset for print. ASCII is zero-risk.

If you have VS Code open on the workspace folder with a markdown formatter (Prettier, Markdown All in One), disable format-on-save for `.md` files — that's the most common trigger.

### Detection

Run this in the Python sandbox to find dirty files:

```python
import glob

base = '/sessions/friendly-vibrant-davinci/mnt/Spec Framework v2'
# Skip files that intentionally show encoding examples
SKIP = {'00_Meta/Troubleshooting.md', 'CLAUDE.md'}

for path in glob.glob(f'{base}/**/*.md', recursive=True):
    rel = path.replace(base + '/', '')
    if rel in SKIP:
        continue
    with open(path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='replace')
    non_ascii = [c for c in content if ord(c) > 127]
    if non_ascii:
        print(f'DIRTY: {rel} ({len(non_ascii)} non-ASCII chars)')
```

### Fix (byte-level replacement)

```python
path = '/path/to/file.md'

with open(path, 'rb') as f:
    data = f.read()

# Known corrupted patterns -> correct UTF-8 bytes
replacements = {
    bytes.fromhex('c383c2a2c3a2e2809ac2ace2809d'): '—'.encode('utf-8'),  # em dash
    bytes.fromhex('c383c2a2c3a2e282acc2a0e2809c'): '→'.encode('utf-8'),  # right arrow
    # Add others as discovered — find them with the detection script,
    # check context to identify the correct character, add the mapping here.
}

for bad, good in replacements.items():
    data = data.replace(bad, good)

with open(path, 'wb') as f:
    f.write(data)
```

**How to identify a new pattern**: run the detection script, then check the character's context to determine what it should be (em dash, arrow, quote, etc.), then add a mapping.

The cp1252 round-trip approach (`encode('cp1252').decode('utf-8')`) does NOT work reliably — some intermediate bytes are invalid UTF-8. Always use direct byte replacement.

---

## Manual Prompt Patterns

For tasks that don't have a dedicated skill:

### Cross-Epic Dependency Map
```
Review all Epics in 02_Epics/. Map dependencies between them.
Identify any circular dependencies or missing prerequisite work.
```

### Glossary Update
```
Scan [Epic-XX] for domain-specific terms not yet in 01_Context/Glossary.md.
Add missing terms alphabetically with 1-2 sentence definitions.
```

### Simplification Sweep
```
Review Epic-XX. Can we achieve 80% of the user value with 50% of the complexity?
Suggest what to cut or defer. Don't modify the file — list recommendations only.
```

### Client Change Impact Analysis
```
The client has changed [X]. Which Epics and features are affected?
What needs to update in Platform_Specification.md?
What needs to update in Epic files?
Propose minimal necessary changes.
```

### Full-Spec Consistency Check
```
Read all Epic files in 02_Epics/. Check for:
- Same concept using different terms across files
- Contradicting business rules between Epics
- Assumptions in one Epic that conflict with confirmed decisions in Decision_Log.md
Report findings organized by severity.
```

---

## Context Management Tips

**Large projects**: Claude has a large context window, but for very large spec sets, be explicit about which files to read:
> "Read Epic-01 and Epic-02, then compare how they handle user authentication."

**Between sessions**: Always update `00_Meta/Project_Plan.md` at the end of a session so Claude can pick up where you left off in the next one.

**When Claude seems to have lost track:**
> "Based on Platform_Specification.md and the current state of Open