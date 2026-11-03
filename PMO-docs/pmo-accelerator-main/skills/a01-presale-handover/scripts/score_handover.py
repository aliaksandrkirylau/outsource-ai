#!/usr/bin/env python3
"""Score the A01 pre-sale handover checklist and compute the two control metrics.

Usage:
    python score_handover.py <statuses.yaml>
    (use python3 on macOS/Linux; Windows python.org installs provide only 'python')

The status file maps each checklist item key to one of:
    gathered | partial | missing | na
with an optional note. See references/example-input.yaml for the shape and the
full key list. The rubric (core/critical flags) is canonical and lives here, so
the metric is deterministic and re-runnable by anyone.

Metrics (Standard A, A01, Confluence page 4619206688):
  Pre-sale Handover Maturity Index = confirmed core / relevant core * 100   (target >= 70%)
  Critical Uncertainty Ratio       = material unresolved / relevant core * 100 (target <= 30%)
"""
import os, sys, re

# Windows consoles default to a legacy code page when stdout is a pipe, so a single
# accented or Cyrillic character in a note would crash the script with a traceback.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except (AttributeError, ValueError):
    pass

# Canonical rubric: key -> (label, core, critical). Source: page 3285712947.
RUBRIC = [
    ("contract",        "Project contract + addendums",                 True,  True),
    ("wbs",             "WBS",                                          True,  True),
    ("requirements",    "Pre-sale requirements (specs/Q&A/designs)",    True,  True),
    ("description",     "Project description / vision + goal",          True,  True),
    ("scope",           "Scope details",                                True,  True),
    ("budget",          "Budget (hours)",                               True,  True),
    ("duration",        "Duration",                                     True,  True),
    ("milestones",      "Milestones, schedule, timeline",               True,  True),
    ("contract_type",   "Contract type (T&M/FP/dedicated)",             True,  True),
    ("technologies",    "Mandatory technologies (if applicable)",       True,  False),
    ("hosting",         "Mandatory hosting (if applicable)",            True,  False),
    ("assumptions",     "Assumptions, limitations, risks",              True,  True),
    ("deliverables",    "Deliverables",                                 True,  True),
    ("req_artifacts",   "Required artifacts / documentation",           True,  False),
    ("client_profile",  "Client company profile",                       True,  False),
    ("team_location",   "Team location important to client",            True,  False),
    ("team_composition","Team composition (if in contract)",            True,  False),
    ("stakeholders",    "Stakeholders list / matrix (draft)",           True,  True),
    # nice-to-have (non-core)
    ("business_model",  "Client business model",                        False, False),
    ("call_recordings", "Pre-sale call recordings",                     False, False),
    ("english_level",   "Client English / comm expectations",           False, False),
    ("timezone",        "Customer time zone",                           False, False),
    ("intermediary",    "Direct vs intermediary",                       False, False),
    ("responsibility",  "Innowise area of responsibility",              False, False),
    ("involvement",     "Client involvement & reporting pref",          False, False),
    ("cicd_owner",      "Repo / env / CI-CD accountability",            False, False),
    ("uat",             "UAT process",                                  False, False),
    ("client_tech",     "Client-side PM/SA/TL availability",            False, False),
]
VALID = {"gathered", "partial", "missing", "na"}
WEIGHT = {"gathered": 1.0, "partial": 0.5, "missing": 0.0}


def parse(path):
    """Minimal YAML-ish parser: 'key: status' or 'key: status  # note'. Avoids deps.

    Returns (statuses, notes, unparsed_lines). Values may be quoted. Keys are matched
    case-insensitively against the rubric. Anything that looks like content but does
    not parse is RETURNED, not silently dropped - a wrong gate number that nobody
    knows is wrong is worse than a loud failure.

    The trailing comment is KEPT, not discarded. For an `na` item that comment is the
    justification for dropping the item out of the denominator, which is the one place
    in this script where a free-text note changes a reported number.
    """
    out, notes, unparsed = {}, {}, []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for lineno, line in enumerate(fh, 1):
            line = line.rstrip("\n")
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or stripped == "---":
                continue
            # key: value  |  key: "value"  |  key: 'value'   (trailing # note captured)
            m = re.match(r"""\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*["']?([A-Za-z_]+)["']?\s*(?:#\s*(.*))?$""", line)
            if not m:
                unparsed.append((lineno, stripped[:70]))
                continue
            key = m.group(1).lower()
            out[key] = m.group(2).lower()
            note = (m.group(3) or "").strip()
            if note:
                notes[key] = note
    return out, notes, unparsed


def main():
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        print("Example:")
        print("    python score_handover.py handover-statuses.yaml")
        sys.exit(0 if (len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help")) else 1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print("No such file: %s" % path, file=sys.stderr)
        print("Point this at your statuses file. See references/example-input.yaml "
              "for the shape.", file=sys.stderr)
        sys.exit(2)
    if os.path.isdir(path):
        print("That is a folder, not a statuses file: %s" % path, file=sys.stderr)
        sys.exit(2)

    try:
        statuses, notes, unparsed = parse(path)
    except OSError as exc:
        print("Could not read %s: %s" % (path, exc), file=sys.stderr)
        sys.exit(2)

    known_keys = {k for k, *_ in RUBRIC}
    recognised = [k for k in statuses if k in known_keys]
    if not recognised:
        print("Read %s but found no recognised checklist keys." % path, file=sys.stderr)
        print("Expected lines like 'contract: gathered'. Valid statuses: "
              + ", ".join(sorted(VALID)) + ".", file=sys.stderr)
        print("See references/example-input.yaml for the full key list.", file=sys.stderr)
        sys.exit(2)

    rows, relevant, confirmed, material = [], 0, 0.0, 0.0
    gaps, na_items, unknown = [], [], []
    for key, label, core, critical in RUBRIC:
        st = statuses.get(key, "missing")
        if st not in VALID:
            unknown.append((key, st)); st = "missing"
        rows.append((label, core, critical, st))
        if not core or st == "na":
            if st == "na":
                na_items.append((key, label, notes.get(key, "")))
            continue
        relevant += 1
        confirmed += WEIGHT[st]
        if critical and st == "missing":
            material += 1.0
        elif critical and st == "partial":
            material += 0.5
        if st in ("missing", "partial"):
            gaps.append((label, st, "MATERIAL" if critical else "minor"))

    for key in statuses:
        if key not in known_keys:
            unknown.append((key, "unknown-key"))

    missing_keys = sorted(known_keys - set(statuses))

    maturity = (confirmed / relevant * 100) if relevant else 0
    uncertainty = (material / relevant * 100) if relevant else 0

    p = print
    p("=" * 60)
    p("A01 PRE-SALE HANDOVER - SCORECARD")
    p("=" * 60)
    p(f"Source: {path}")
    p(f"Read {len(recognised)} of {len(known_keys)} checklist keys.")
    if missing_keys:
        p(f"  Not in the file (scored as missing): {', '.join(missing_keys)}")
    if unparsed:
        p(f"  WARNING - {len(unparsed)} line(s) could not be read and were ignored:")
        for lineno, text in unparsed[:6]:
            p(f"    line {lineno}: {text}")
        if len(unparsed) > 6:
            p(f"    ... and {len(unparsed) - 6} more")
        p("    Expected 'key: status'. Check these before trusting the numbers below.")
    total_core = sum(1 for _k, _l, core, _c in RUBRIC if core)
    p("")
    p(f"Relevant core areas: {relevant} of {total_core} core"
      + (f"  ({len(na_items)} marked na and excluded)" if na_items else ""))
    p(f"Confirmed (gathered=1, partial=0.5): {confirmed:g}")
    p("")
    mflag = "PASS" if maturity >= 70 else "BELOW THRESHOLD"
    uflag = "PASS" if uncertainty <= 30 else "ABOVE THRESHOLD"
    p(f"Pre-sale Handover Maturity Index : {maturity:5.1f}%  (target >= 70%)  -> {mflag}")
    p(f"Critical Uncertainty Ratio       : {uncertainty:5.1f}%  (target <= 30%)  -> {uflag}")
    p("")
    if gaps:
        p("GAPS (missing / partial):")
        for label, st, sev in sorted(gaps, key=lambda x: x[2] != "MATERIAL"):
            p(f"  [{sev:8}] {st:8} - {label}")
    else:
        p("No gaps - all relevant core areas gathered.")
    if na_items:
        p("")
        p("NOT APPLICABLE - each of these was REMOVED from the denominator, which RAISES")
        p("the maturity score. Every one needs the PM's explicit agreement and a reason.")
        unjustified = []
        for key, label, reason in na_items:
            if reason:
                p(f"  {label}")
                p(f"      reason: {reason}")
            else:
                p(f"  {label}")
                p(f"      reason: NONE GIVEN - add one or change the status")
                unjustified.append(label)
        without = (confirmed / total_core * 100) if total_core else 0
        p(f"  Maturity would be {without:.1f}% if none of these were excluded"
          f" (reported: {maturity:.1f}%).")
        if unjustified:
            p(f"  {len(unjustified)} na item(s) carry NO reason. Do not present this score"
              " until they do.")
    if unknown:
        p("")
        p("WARNING - unknown keys or statuses (treated as missing): "
          + ", ".join(f"{k}={v}" for k, v in unknown))
    p("=" * 60)


if __name__ == "__main__":
    main()
