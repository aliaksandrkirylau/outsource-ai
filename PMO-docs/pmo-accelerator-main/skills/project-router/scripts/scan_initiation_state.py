#!/usr/bin/env python3
"""
scan_initiation_state.py - deterministic Standard A readiness scanner (v2).

Given a project folder, detect what initiation work already exists and score it
two ways:

  1. Per A-STEP (A01-A14)      - what work is left to do.
  2. Per MANDATORY ARTIFACT    - what the PMO will look for (the 23-item
     Project Initiation Artifacts Checklist, Confluence 5166432427).

The two answer different questions and the router should show both. The step map
says "where are you in the process"; the artifact map says "what is missing that
someone will ask you for". On a taken-over project the artifact map is the more
useful of the two, because it does not assume the project started at A01.

What changed from v1, and why:
  - Content sniffing, not just filenames. v1 detected purely by filename, so a
    project not named the way one particular PM names things scored near zero
    (InamuH scored 2/13 despite having real A01 deliverables).
  - Artifact scoring against the 23-item checklist.
  - Honest about what it cannot see. Most mandatory artifacts live in Drive,
    Jira, Confluence, Chat or NotebookLM. Those are reported as needs-connector-
    check, never as missing.
  - Money-in-the-wrong-place check. A P&L or rate file inside the common project
    folder is a policy problem, and the scanner flags it.
  - Unknown-file bucket, so the PM can map anything the scanner could not place
    instead of it being silently dropped.

Usage:
    python scan_initiation_state.py <project_folder> [--json] [--thin-bytes N]
    (use python3 on macOS/Linux; Windows python.org installs provide only 'python')

No third-party dependencies.
"""

import argparse
import json
import os
import re
import sys

# Windows consoles fall back to a legacy code page when stdout is a pipe, which is
# exactly what happens when a tool runs this script. One Cyrillic or accented filename
# would otherwise crash it with a traceback.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

# ---------------------------------------------------------------- A-step table
# keywords = filename fragments. signals = phrases looked for INSIDE text files.
# Keep both specific enough not to cross-assign: "internal kickoff" is A12,
# "client kickoff" is A13.

STEPS = [
    ("A01", "Receive handover + onboard",
     ["handover", "onboard", "presale-handover", "presale handover", "harvest"],
     ["pre-sale handover", "presale handover", "handover maturity",
      "handover brief", "client problem statement", "assumptions and commitments"]),

    ("A02", "Actors, ownership, channels",
     ["stakeholder-register", "stakeholder register", "raci-matrix", "raci matrix",
      "stakeholder", "actors", "ownership", "comm-plan", "communication-plan", "raci"],
     ["stakeholder register", "decision-ownership", "decision ownership",
      "client decision clarity", "internal ownership readiness",
      "internal communication channels"]),

    ("A03", "Review final contract",
     ["contract-commitments", "commitments-register", "commitments register", "contract-review"],
     ["commitments register", "contractual baseline", "contract version comparison",
      "contract discrepancy"]),

    ("A04", "Describe project + context",
     ["project-description", "project description", "context-summary",
      "charter", "vision-and-scope"],
     ["project description", "project definition maturity",
      "observable success criteria", "goals and expected outcomes",
      "business / strategic value", "business and strategic value"]),

    ("A05", "Validate scope / estimates",
     ["validation", "scope-validation", "scope validation", "validation-summary", "estimate-review",
      "wbs", "critical-scope", "acceptance-criteria"],
     ["critical scope estimate coverage", "required project roles",
      "acceptance criteria", "scope baseline", "estimate realism",
      "sold vs", "sold-vs"]),

    ("A06", "Risks / dependencies / blockers",
     ["risk-register", "risk register", "risk-problems", "risk log", "risklog",
      "blocker", "issue-log", "issue log"],
     ["risk register", "critical control coverage", "dependency readiness",
      "issue / blocker", "issue/blocker", "mitigation", "risk id"]),

    ("A07", "Roadmap + resource plan",
     ["milestone-schedule", "milestone schedule", "project-roadmap", "phase-timeline",
      "roadmap", "resource-plan", "resource plan", "milestone", "timeline",
      "schedule", "gantt"],
     ["milestone schedule", "resource timeline coverage",
      "roadmap coverage", "role x month", "critical path"]),

    ("A08", "Initial economy",
     ["economy", "p&l", "pnl", "pl-staff", "economics", "project-economy",
      "margin", "profit"],
     ["resource-to-economy coverage", "economy calculation",
      "pre-sale p&l", "economy assumptions"]),

    ("A09", "Baseline gate",
     ["baseline", "baseline-package", "gate", "start-decision", "go-no-go",
      "value-classification"],
     ["stakeholder validation coverage", "approved to continue",
      "approved with constraints", "value classification",
      "value extraction hypothesis", "baseline validation"]),

    ("A10", "Staffing + team composition",
     ["staffing-request", "staffing request", "team-composition", "team composition",
      "staffing", "resource-request", "fair-hours", "candidates"],
     ["candidate vetting", "staffing data update", "confirmed team composition",
      "staffing master", "approved candidate", "staffing request"]),

    ("A11", "Set up PM system",
     ["a11-project-setup", "jira-setup", "confluence-setup", "drive-structure",
      "prorep", "proreps", "onboarding-rules", "working-rules"],
     ["access and link readiness", "prorep", "project card",
      "team working rules", "onboarding rules", "sensitive folder",
      "knowledge container"]),

    ("A12", "Align team on start",
     ["internal-kickoff", "internal kickoff", "team-align", "team alignment",
      "internal-align", "team-summary", "readiness-review"],
     ["team alignment coverage", "team feasibility",
      "internal alignment", "internal kick-off", "internal kickoff"]),

    ("A13", "Prepare client kick-off",
     ["client-kickoff", "client kickoff", "kickoff-deck", "kickoff deck",
      "kick-off-prep", "kickoff-agenda", "kick-off", "kickoff"],
     ["kick-off materials coverage", "kick-off agenda", "kickoff agenda",
      "client kick-off", "kick-off invite"]),

    ("A14", "Kick off project",
     ["kickoff-notes", "kickoff-agreements", "kick-off-log", "kickoff-follow",
      "kickoff-followup", "kickoff-recap"],
     ["kick-off agreement capture", "open action ownership",
      "kick-off follow-up", "kickoff follow-up", "start agreements"]),
]

STEP_LABEL = {c: l for c, l, _k, _s in STEPS}
PRE_GATE = ["A01", "A02", "A03", "A04", "A05", "A06", "A07", "A08"]

# ------------------------------------------ the 23 mandatory starting artifacts
# Live Starting Project Artifacts Checklist, Confluence 5166432427 (v16, 2026-09-24).
# where: "connector" - only a system check can confirm it
#        "either"    - may be a local file or may live in a system
# never_local: finding this in the common project folder is a POLICY PROBLEM.
# fp_only: applies to Fixed-Price projects only - report it as N/A otherwise, never missing.

ARTIFACTS = [
    ("knowledge_container", "Project Knowledge Container (NotebookLM)", "NotebookLM",      "connector", None,  False),
    ("project_folders",     "Common & Sensitive Project Folder",        "Google Drive",    "connector", None,  False),
    ("project_description", "Project Description",                      "Confluence",      "either",    "A04", False),
    ("stakeholder_register","Stakeholder Register",                     "Confluence",      "either",    "A02", False),
    ("wbs_critical_scope",  "WBS / Critical Scope Baseline + Estimates","Confluence/Sheet","either",    "A05", False),
    ("risk_register",       "Risk Register",                            "Jira/Confluence", "either",    "A06", False),
    ("opportunity_register","Opportunity & Internal Risk Register",     "Internal only",   "either",    "A06", False),
    ("team_composition",    "Project Team Composition",                 "Spreadsheet",     "either",    "A10", False),
    ("raci",                "RACI Matrix (Team + Stakeholders)",        "Confluence/Sheet","either",    "A12", False),
    ("staffing_master",     "Staffing Master",                          "Staffing Folder", "connector", "A10", False),
    ("resource_plan",       "Resource Plan",                            "Spreadsheet",     "either",    "A07", False),
    ("pl",                  "Project Economy (P&L)",                    "Sensitive Folder","connector", "A08", True),
    ("evm_baseline",        "EVM Baseline (Fixed-Price only)",          "Sensitive Folder","connector", "A08", True),
    ("roadmap",             "Roadmap / Timeline / Schedule",            "Confluence/MSP",  "either",    "A07", False),
    ("chats",               "Project Chats with pinned sources",        "Google Chat",     "connector", "A02", False),
    ("baseline_validation", "Baseline Validation (Expectations Matrix)","Mail/Chat",       "connector", "A09", False),
    ("start_approval",      "Project (Start) Approval",                 "Mail/Chat",       "connector", "A09", False),
    ("communication_plan",  "Communication Plan",                       "Confluence",      "either",    "A11", False),
    ("prorep",              "Project Card / PROREP",                    "PROREP (Jira)",   "connector", "A11", False),
    ("tracker",             "Progress Tracking Board configured",       "Jira/Other",      "connector", "A11", False),
    ("docs_space",          "Project Documentation Space",              "Confluence/Drive","connector", "A11", False),
    ("onboarding_rules",    "Onboarding / Team Working Rules",          "Confluence",      "either",    "A11", False),
    ("kickoff_deck",        "Kick-off Slide Deck",                      "Google Slides",   "either",    "A13", False),
]

FP_ONLY = {"evm_baseline"}

# A file can hit more than one key: an "opportunity-internal-risk-register" also matches
# risk_register. That over-counts the Risk Register by one file at most, and never makes
# a missing register look present on its own, so it is left alone.
ARTIFACT_KEYS = {
    "project_description":  ["project-description", "project description", "charter", "vision"],
    "stakeholder_register": ["stakeholder"],
    "wbs_critical_scope":   ["wbs", "critical-scope", "critical scope", "acceptance-criteria",
                             "scope-baseline", "estimate", "estimates", "effort"],
    "risk_register":        ["risk-register", "risk register", "riskregister", "risk-log", "risks"],
    "opportunity_register": ["opportunity-register", "opportunity register", "opportunities",
                             "internal-risk", "internal risk"],
    "team_composition":     ["team-composition", "team composition"],
    "raci":                 ["raci"],
    "resource_plan":        ["resource-plan", "resource plan", "resourceplan"],
    "roadmap":              ["roadmap", "timeline", "schedule", "milestone"],
    "communication_plan":   ["communication-plan", "communication plan", "comm-plan", "commplan"],
    "onboarding_rules":     ["onboarding", "working-rules", "working rules", "team-rules"],
    "kickoff_deck":         ["kickoff", "kick-off"],
    "staffing_master":      ["staffing-master", "staffing master"],
    "pl":                   ["p&l", "pnl", "p-and-l", "economics", "economy", "margin"],
    "evm_baseline":         ["evm", "earned-value", "earned value", "planned-value"],
}

CONTENT_ARTIFACTS = {
    "stakeholder_register": "stakeholder register",
    "risk_register":        "risk register",
    "opportunity_register": "internal risk register",
    "project_description":  "project description",
    "communication_plan":   "communication plan",
    "wbs_critical_scope":   "acceptance criteria",
    "onboarding_rules":     "working rules",
    "raci":                 "raci matrix",
}

ARTIFACT_EXT_HINT = {
    "kickoff_deck":     {".pptx", ".gslides", ".key", ".pdf"},
    "wbs_critical_scope": {".xlsx", ".gsheet", ".csv", ".tsv", ".md"},
    "resource_plan":    {".xlsx", ".gsheet", ".csv", ".md"},
    "team_composition": {".xlsx", ".gsheet", ".csv", ".md"},
}

MONEY_FILENAME_SIGNALS = ["p&l", "pnl", "salary", "margin", "profit", "rate-card",
                          "ratecard", "economics", "invoice"]

# An A-step code in a filename. Two forms, deliberately:
#   - zero-padded anywhere:  "A01-brief.md", "brief_A03.md", "notes (a12).md"
#   - bare digit only at the start: "a5 risks.md"
# The leading class excludes & and alphanumerics so "Q&A-05.md" is not a step code, and
# requiring the pad away from the start stops "column-a2-mapping.csv" reading as A02.
# Both are plausible real filenames that fooled the first version.
CODE_PADDED = re.compile(r'(?:^|[\-_ .()\[\]])a[\-_ ]?(0\d|1[0-4])(?![0-9])', re.IGNORECASE)
CODE_LEAD   = re.compile(r'^a[\-_ ]?(\d{1,2})(?![0-9])', re.IGNORECASE)

SKIP_DIRS = {".git", ".obsidian", "node_modules", "__pycache__", ".claude",
             ".venv", "venv", "_archive", "archive", "sources", "raw",
             "pm-copilot-references"}

# The copilot's own files DESCRIBE artifacts rather than being them. Scored, they poison
# the map: a notes file discussing the project description reads as the project
# description, and a workspace copy of the reference pack scores every step present off
# the standard's own text. Detected and reported separately instead of classified.
COPILOT_FILES = {"project-context.md", "copilot-feedback.md", "pm-profile.md",
                 "pm-copilot-baseline.md", "pm-copilot-setup.md",
                 "takeover-brief.md", "source-register.md", "tasks.md", "pm-tasks.md"}
COPILOT_PREFIXES = ("copilot-", "pm-copilot-")

# Phrases that turn up in documents ABOUT an artifact as readily as in the artifact.
# Every feature spec in a Confluence export contains "acceptance criteria"; a
# communication plan mentions the risk register. On their own they are a hint, never
# evidence that the step was done.
GENERIC_SIGNALS = {"acceptance criteria", "mitigation", "critical path",
                   "project description", "prorep", "project card", "sold vs",
                   "sold-vs", "risk id", "scope baseline", "staffing master",
                   "knowledge container", "sensitive folder"}

TEXT_EXT = {".md", ".txt", ".yaml", ".yml", ".rst"}
DOC_EXT = {".doc", ".docx", ".gdoc", ".pdf", ".xlsx", ".xls", ".gsheet", ".csv",
           ".tsv", ".pptx", ".gslides", ".key", ".odt"}
SCAN_EXT = TEXT_EXT | DOC_EXT

# Google Drive shortcut files are ~100-300 byte JSON link stubs. Their size says nothing
# about the document behind them, so they must never be judged "thin" - a Drive-synced
# project folder would otherwise score close to zero across the board.
LINK_STUB_EXT = {".gdoc", ".gsheet", ".gslides", ".gdraw", ".gform", ".url", ".lnk"}

SNIFF_BYTES = 6000


def read_head(path):
    """First chunk of a text file, lowercased. Never raises."""
    try:
        with open(path, "rb") as fh:
            raw = fh.read(SNIFF_BYTES)
        return raw.decode("utf-8", errors="ignore").lower()
    except OSError:
        return ""


STRONG_MIN_LEN = 11

# Single words that ARE an artifact's proper name and rarely mean anything else, so they
# carry as much weight as a compound. Deliberately short: "onboard", "kickoff", "staffing",
# "risks", "schedule" and "timeline" are all excluded because each one matched an unrelated
# file on a real project - a client onboarding-flow spec, a delivery tracker, a required-
# roles list. The test for adding a word here is whether a file named for it could
# plausibly be something else.
STRONG_BARE = {"roadmap", "wbs", "gantt", "raci"}


def is_strong(keyword):
    """A long compound keyword names an artifact ('risk-register',
    'internal kickoff', 'project-description'). A short or bare one
    ('kick-off', 'risk log', 'risks', 'schedule') is only a hint.

    Strong keywords beat content signals; weak ones lose to them. The length
    floor matters: 'kick-off' is hyphenated but says nothing about which
    kick-off artifact this is, so it must not outrank a content signal.
    """
    if keyword in STRONG_BARE:
        return True
    return (("-" in keyword or " " in keyword) and len(keyword) >= STRONG_MIN_LEN)


LEGACY_CODE_HITS = []   # (filename, code in the name, step the name says)


def classify_step(name, head):
    """Map a file to an A-step. Returns (code, how, strength) or (None, None, None).

    Precedence, in order:
      1. an explicit A-code in the filename        - STRONG, the PM named the step
      2. a COMPOUND filename keyword               - STRONG, the filename names the artifact
      3. a specific content signal                 - MEDIUM, the file says what it is
      4. a generic content signal                  - WEAK, could be any document
      5. a bare filename keyword                   - WEAK, weakest hint

    Content sits above bare keywords because filenames are a local convention and
    content is not, but below compound keywords because risk-register-customer.md is
    a risk register whatever phrases it happens to contain.

    Strength is the point of this function, not a by-product. A step supported only by
    weak or medium evidence is a HINT that something might exist, and real runs show it
    is wrong often enough that counting it as done misleads the PM: 'onboard' matched
    two client onboarding-flow feature docs and claimed the pre-sale handover was done;
    'kickoff' matched a delivery tracker and claimed the client kick-off was prepared.
    """
    lower = name.lower()

    code_hit = None
    m = CODE_PADDED.search(lower) or CODE_LEAD.match(lower)
    if m:
        n = int(m.group(1))
        if 1 <= n <= 14:
            code_hit = "A%02d" % n

    kw_hit = None
    for code, _l, keywords, _s in STEPS:
        for kw in keywords:
            if is_strong(kw) and kw in lower:
                kw_hit = (code, kw)
                break
        if kw_hit:
            break

    # Copilot releases before 0.45.0 numbered A03 onward one lower (the contract review was
    # "A02.5"), and they wrote those codes into filenames - A03-project-description.md is
    # today's A04. When the code and the artifact name disagree, the name wins.
    if code_hit and kw_hit and kw_hit[0] != code_hit:
        LEGACY_CODE_HITS.append((name, code_hit, kw_hit[0]))
        return (kw_hit[0], "filename names the artifact ('%s'); its code %s disagrees"
                % (kw_hit[1], code_hit), "strong")
    if code_hit:
        return code_hit, "step code in filename", "strong"
    if kw_hit:
        return kw_hit[0], "filename names the artifact ('%s')" % kw_hit[1], "strong"

    if head:
        for code, _l, _kw, signals in STEPS:
            for sig in signals:
                if sig in head and sig not in GENERIC_SIGNALS:
                    return code, "content signal '%s'" % sig, "medium"
        for code, _l, _kw, signals in STEPS:
            for sig in signals:
                if sig in head:
                    return code, "generic phrase '%s'" % sig, "weak"

    for code, _l, keywords, _s in STEPS:
        for kw in keywords:
            if not is_strong(kw) and kw in lower:
                return code, "filename keyword '%s'" % kw, "weak"

    return None, None, None


def classify_artifacts(name, ext, head):
    """Which mandatory-artifact keys this file plausibly satisfies."""
    lower = name.lower()
    hits = set()
    for key, frags in ARTIFACT_KEYS.items():
        allowed = ARTIFACT_EXT_HINT.get(key)
        if allowed and ext not in allowed:
            continue
        for frag in frags:
            if frag in lower:
                hits.add(key)
                break
    if head:
        for key, phrase in CONTENT_ARTIFACTS.items():
            if phrase in head:
                hits.add(key)
    return hits


def scan(folder, sensitive_folder=False):
    step_hits = {code: [] for code, _l, _k, _s in STEPS}
    artifact_hits = {key: [] for key, *_rest in ARTIFACTS}
    unknown = []
    money_flags = []
    unreadable = []
    copilot_state = []
    scanned = 0
    skipped = set()

    def on_error(exc):
        # A directory we cannot read means the score is computed on partial data. Say so
        # rather than silently reporting a lower number.
        unreadable.append(str(getattr(exc, "filename", exc)))

    for root, dirs, files in os.walk(folder, onerror=on_error):
        for d in list(dirs):
            if d.lower() in SKIP_DIRS or d.startswith("."):
                skipped.add(d)
        dirs[:] = [d for d in dirs if d.lower() not in SKIP_DIRS and not d.startswith(".")]

        for fn in files:
            if fn.startswith("."):
                continue
            ext = os.path.splitext(fn)[1].lower()
            if ext not in SCAN_EXT:
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, folder)

            low_fn = fn.lower()
            if low_fn in COPILOT_FILES or low_fn.startswith(COPILOT_PREFIXES):
                copilot_state.append(rel)
                continue

            scanned += 1
            try:
                size = os.path.getsize(path)
            except OSError:
                size = 0

            head = read_head(path) if ext in TEXT_EXT else ""
            is_stub = ext in LINK_STUB_EXT

            # Money in a COMMON project folder is a policy problem. In the Sensitive
            # folder it is exactly where it belongs, so do not cry wolf.
            if not sensitive_folder:
                lower_rel = rel.lower()
                for signal in MONEY_FILENAME_SIGNALS:
                    if signal in lower_rel:
                        money_flags.append({"file": rel, "signal": signal})
                        break

            code, how, strength = classify_step(fn, head)
            if code:
                step_hits[code].append({"file": rel, "bytes": size,
                                        "matched_by": how, "strength": strength,
                                        "link_stub": is_stub})

            akeys = classify_artifacts(fn, ext, head)
            for akey in akeys:
                artifact_hits[akey].append({"file": rel, "bytes": size, "link_stub": is_stub})

            if not code and not akeys:
                unknown.append({"file": rel, "bytes": size})

    return (step_hits, artifact_hits, unknown, money_flags, scanned,
            sorted(skipped), unreadable, sorted(copilot_state))


def status_for(entries, thin_bytes):
    """missing / possible / thin / present.

    PRESENT requires at least one STRONG hit - a step code or a compound filename
    keyword. Anything resting only on a bare keyword or a generic phrase is POSSIBLE:
    worth a look, not worth counting. That distinction is what stops the headline
    number claiming work that has not happened.
    """
    if not entries:
        return "missing"
    strong = [e for e in entries if e.get("strength") == "strong"]
    if not strong:
        return "possible"
    # A Drive link stub is small by nature; treat it as present and let the PM confirm.
    if any(e.get("link_stub") for e in strong):
        return "present"
    if max(e["bytes"] for e in strong) < thin_bytes:
        return "thin"
    return "present"


def build_report(folder, thin_bytes, sensitive_folder=False):
    (step_hits, artifact_hits, unknown, money_flags, scanned,
     skipped, unreadable, copilot_state) = scan(folder, sensitive_folder)

    steps = {}
    for code, label, _kw, _sg in STEPS:
        entries = step_hits[code]
        steps[code] = {"label": label,
                       "status": status_for(entries, thin_bytes),
                       "files": entries}

    artifacts = {}
    for key, label, storage, where, step, never_local in ARTIFACTS:
        entries = artifact_hits[key]
        if entries:
            state = "found_locally"
        elif where == "connector":
            state = "needs_connector_check"
        else:
            state = "not_found_locally"
        artifacts[key] = {"label": label, "storage": storage,
                          "confirmable": where, "produced_at": step,
                          "state": state, "files": entries}
        if never_local and entries:
            artifacts[key]["policy_warning"] = (
                "Money-bearing artifact inside the project folder. The P&L "
                "belongs in the Sensitive folder only.")

    present = [c for c in steps if steps[c]["status"] == "present"]
    thin = [c for c in steps if steps[c]["status"] == "thin"]
    possible = [c for c in steps if steps[c]["status"] == "possible"]
    missing = [c for c in steps if steps[c]["status"] == "missing"]
    pre_present = [c for c in PRE_GATE if steps[c]["status"] == "present"]
    pre_missing = [c for c in PRE_GATE if steps[c]["status"] != "present"]

    # One phrase pulling in a pile of files is noise, not corroboration. 29 feature specs
    # each containing "acceptance criteria" is a Confluence export, not a validated scope.
    noise = []
    for code in steps:
        counts = {}
        for e in steps[code]["files"]:
            if e.get("strength") != "strong":
                counts[e["matched_by"]] = counts.get(e["matched_by"], 0) + 1
        for how, n in counts.items():
            if n >= 5:
                noise.append({"step": code, "matched_by": how, "files": n})

    # The two maps run off separate keyword tables and can disagree about the same file.
    # Surface that rather than printing a contradiction and leaving the PM to spot it.
    reconcile = []
    for key, label, _storage, _w, step, _nl in ARTIFACTS:
        if not step or artifacts[key]["state"] != "found_locally":
            continue
        if steps.get(step, {}).get("status") in ("missing", "possible"):
            reconcile.append({"artifact": label, "step": step,
                              "step_status": steps[step]["status"],
                              "files": [f["file"] for f in artifacts[key]["files"][:3]]})

    found_local = [k for k in artifacts if artifacts[k]["state"] == "found_locally"]
    need_check = [k for k in artifacts if artifacts[k]["state"] == "needs_connector_check"]
    not_found = [k for k in artifacts if artifacts[k]["state"] == "not_found_locally"]

    # Gate-aware: prefer an unfinished PRE-GATE step, because A09 is the one hard
    # sequencing rule in the standard. Only once A01-A08 are present look past it.
    next_suggested = None
    for code in PRE_GATE:
        if steps[code]["status"] != "present":
            next_suggested = code
            break
    if next_suggested is None:
        for code, _l, _k, _s in STEPS:
            if steps[code]["status"] != "present":
                next_suggested = code
                break

    return {
        "project": os.path.abspath(folder),
        "scanned_files": scanned,
        "skipped_dirs": skipped,
        "unreadable_paths": unreadable,
        "steps": steps,
        "artifacts": artifacts,
        "unknown_files": unknown,
        "money_in_common_folder": money_flags,
        "copilot_state_files": copilot_state,
        "noise_signals": noise,
        "map_disagreements": reconcile,
        "legacy_code_filenames": [{"file": f, "code_in_name": c, "classified_as": s}
                                  for f, c, s in LEGACY_CODE_HITS],
        "coverage": {"present": len(present), "total": len(STEPS),
                     "pct": round(100.0 * len(present) / len(STEPS), 1)},
        "artifact_coverage": {
            "found_locally": len(found_local),
            "needs_connector_check": len(need_check),
            "not_found_locally": len(not_found),
            "total": len(ARTIFACTS),
            "note": "Local files can only confirm some of the 23. The rest need a "
                    "Drive / Jira / Chat / NotebookLM / Mail check - they are NOT "
                    "missing, they are unverified.",
        },
        "pre_gate_readiness": {"present": len(pre_present), "of": len(PRE_GATE),
                               "pct": round(100.0 * len(pre_present) / len(PRE_GATE), 1),
                               "missing": pre_missing},
        "thin": thin,
        "possible": possible,
        "missing": missing,
        "next_suggested": next_suggested,
        "notes": [
            "Order is flexible - steps may run in parallel or out of order. "
            "next_suggested prefers an unfinished pre-gate step because A09 is "
            "the one hard sequencing rule.",
            "PRESENT means a file names the step or names the artifact. POSSIBLE means "
            "the only evidence is a bare keyword or a generic phrase - a hint to check, "
            "not work you can count. Possible is excluded from coverage on purpose.",
            "This measures what has MATERIAL ON DISK, not what is finished. A draft "
            "agenda counts as present. Confirm the map with the PM before routing on it.",
            "Anything the scanner could not place is in unknown_files. Show that "
            "list to the PM rather than dropping it.",
        ],
    }


def print_table(rep):
    ICON = {"present": "[x] present ", "thin": "[~] thin    ",
            "possible": "[?] possible", "missing": "[ ] missing "}
    ASTATE = {"found_locally":         "[x] found locally",
              "needs_connector_check": "[?] check system ",
              "not_found_locally":     "[ ] not in folder"}

    print("Standard A - initiation state for: %s" % rep["project"])
    print("Scanned %d files.\n" % rep["scanned_files"])

    print("A-STEP MAP - what work is left")
    print("  Step  Status        Output")
    print("  ----  ------------  ------------------------------------------")
    for code, _l, _k, _s in STEPS:
        s = rep["steps"][code]
        note = ""
        if s["files"]:
            # Lead with the strongest evidence - that is what the status rests on.
            ranked = sorted(s["files"],
                            key=lambda e: {"strong": 0, "medium": 1}.get(e.get("strength"), 2))
            note = "  <- " + ", ".join(e["file"] for e in ranked[:2])
            if len(ranked) > 2:
                note += " (+%d)" % (len(ranked) - 2)
            note += "  [%s]" % ranked[0].get("matched_by", "?")
        print("  %s   %s  %s%s" % (code, ICON[s["status"]], s["label"], note))

    if rep["legacy_code_filenames"]:
        print()
        print("  OLD NUMBERING: %d filename(s) carry a step code that disagrees with the artifact"
              % len(rep["legacy_code_filenames"]))
        print("    they name - placed by the name. Files written by copilot releases before 0.45.0")
        print("    use codes one lower from A03 on, so a filename with ONLY a code (no artifact")
        print("    name) in this folder may be one step low. Confirm those with the PM.")

    cov, pre = rep["coverage"], rep["pre_gate_readiness"]
    thin_n = len(rep["thin"])
    thin_note = ""
    if thin_n:
        # Say this on the headline. A bare "0%" next to six thin steps reads as
        # "nothing exists", which is the opposite of what the scan found.
        thin_note = "  (+%d more found but sparse - see Thin below)" % thin_n
    print("\n  Coverage: %d/%d steps have material on disk (%.1f%%)%s"
          % (cov["present"], cov["total"], cov["pct"], thin_note))
    print("    This counts what EXISTS, not what is finished - a draft counts.")
    print("  Ready for the A09 gate (A01-A08): %d/%d (%.1f%%)"
          % (pre["present"], pre["of"], pre["pct"]))
    if pre["missing"]:
        print("    still needed before the gate: %s" % ", ".join(pre["missing"]))
    if rep["thin"]:
        print("  Thin - a file exists but is small, so it may be a stub: %s"
              % ", ".join(rep["thin"]))
    if rep["possible"]:
        print("  Possible, NOT counted: %s" % ", ".join(rep["possible"]))
        print("    Only a bare keyword or a generic phrase matched. Check these by hand -")
        print("    they are as often an unrelated file as a real deliverable.")
    if rep["noise_signals"]:
        print("\n  Probably noise - one phrase matching many files:")
        for n in rep["noise_signals"]:
            print("    %s: %d files all matched on %s" % (n["step"], n["files"], n["matched_by"]))
        print("    A bulk export where every document shares a phrase, most likely.")
    if rep["map_disagreements"]:
        print("\n  The two maps disagree - artifact found locally, step not counted:")
        for d in rep["map_disagreements"]:
            print("    %s exists (%s) but %s is %s"
                  % (d["artifact"], ", ".join(d["files"]), d["step"], d["step_status"]))
        print("    Resolve with the PM - usually the artifact is real and the step counts.")
    if rep["copilot_state_files"]:
        print("\n  Copilot's own files (not scored as deliverables): %s"
              % ", ".join(rep["copilot_state_files"]))
    else:
        print("\n  No project-context.md here - the copilot has no memory of this project yet.")

    if rep["skipped_dirs"]:
        print("\n  Folders NOT scanned (by design): %s" % ", ".join(rep["skipped_dirs"]))
        print("    If a real deliverable lives in one of these, the score is understated.")
    if rep["unreadable_paths"]:
        print("\n  Could not read (permissions?) - the score is based on partial data:")
        for p in rep["unreadable_paths"][:5]:
            print("    %s" % p)

    print("\nMANDATORY ARTIFACTS - what the PMO will look for (23 on the Starting checklist; EVM is Fixed-Price only)")
    print("  Status             Artifact                                 Lives in")
    print("  -----------------  ---------------------------------------  ----------------")
    for key, label, storage, _w, _st, _nl in ARTIFACTS:
        a = rep["artifacts"][key]
        print("  %s  %-39s  %s" % (ASTATE[a["state"]], label[:39], storage))
        if a.get("policy_warning"):
            print("      !! %s" % a["policy_warning"])
    ac = rep["artifact_coverage"]
    print("\n  Found in the project folder: %d/%d" % (ac["found_locally"], ac["total"]))
    print("  Need a system check: %d" % ac["needs_connector_check"])
    print("  Expected locally but not found: %d" % ac["not_found_locally"])
    print("  %s" % ac["note"])

    if rep["money_in_common_folder"]:
        print("\n  POLICY WARNING - money-bearing files inside the project folder:")
        for m in rep["money_in_common_folder"]:
            print("    %s  (matched '%s')" % (m["file"], m["signal"]))
        print("    The P&L and rate data belong in the Sensitive folder only.")

    if rep["unknown_files"]:
        print("\n  Unplaced files (%d) - ask the PM what these are:"
              % len(rep["unknown_files"]))
        for u in rep["unknown_files"][:12]:
            print("    %s" % u["file"])
        if len(rep["unknown_files"]) > 12:
            print("    ... and %d more" % (len(rep["unknown_files"]) - 12))

    ns = rep["next_suggested"]
    print("\n  Suggested next step: %s (%s)"
          % (ns or "-", STEP_LABEL[ns] if ns else "all present"))
    print("  Order is flexible; this is a hint, not a sequence.")


def main():
    ap = argparse.ArgumentParser(
        description="Scan a project folder for Standard A readiness and mandatory-artifact coverage.")
    ap.add_argument("folder", help="Path to the project folder to scan")
    ap.add_argument("--json", action="store_true", help="Print JSON only")
    ap.add_argument("--thin-bytes", type=int, default=500,
                    help="Files smaller than this count as thin (default 500). "
                         "Google Drive link stubs are exempt.")
    ap.add_argument("--sensitive-folder", action="store_true",
                    help="Scanning the Sensitive folder, where the P&L belongs. "
                         "Suppresses the money-in-the-wrong-place warning.")
    args = ap.parse_args()

    if not os.path.exists(args.folder):
        print("No such folder: %s" % args.folder, file=sys.stderr)
        return 2
    if not os.path.isdir(args.folder):
        print("That is a file, not a folder: %s" % args.folder, file=sys.stderr)
        return 2

    try:
        rep = build_report(args.folder, args.thin_bytes, args.sensitive_folder)
    except OSError as exc:
        print("Could not scan %s: %s" % (args.folder, exc), file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(rep, indent=2))
    else:
        print_table(rep)
    return 0


if __name__ == "__main__":
    sys.exit(main())
