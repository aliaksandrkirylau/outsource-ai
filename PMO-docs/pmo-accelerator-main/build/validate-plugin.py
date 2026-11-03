#!/usr/bin/env python3
"""Pre-package validator for the PM Copilot plugin.

Run this BEFORE zipping. It checks the things that have actually bitten us, so a
bundle does not get as far as Claude's own validator (or a PM's machine) before
failing.

    python source/build/validate-plugin.py source      (from pm-copilot/)

Exit code 0 = safe to package. Non-zero = do not ship.
"""

import json
import os
import re
import sys

# Limits enforced by Claude's plugin validator.
MAX_PLUGIN_DESC = 500
MAX_SKILL_DESC = 1024

# Paths that only exist in the author's own vault. A shipped bundle must not name them.
AUTHOR_LOCAL = [
    "automations/", "superbrain/sources", "C:\\Users\\USER",
    "Notebook magic", "/sessions/",
]

try:
    import yaml
except ImportError:
    yaml = None


def packer_skips():
    """Read SKIP_DIRS / SKIP_FILES from the packer, so a file the packer never ships
    is not flagged here. One list, owned by the packer."""
    import importlib.util
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("packer", os.path.join(here, "pack-pm-copilot.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return set(mod.SKIP_DIRS), set(mod.SKIP_FILES)


SKIP_DIRS, SKIP_FILES = packer_skips()

# Files allowed to carry non-ASCII. The Russian anti-tell list is a list of Cyrillic phrases, and a
# transliterated phrase list does not match the text it is meant to catch. The ASCII rule exists
# because PowerShell 5.1 Set-Content mangles non-ASCII; the zip and the skill loader do not.
# Paths are relative to the plugin root, forward slashes.
ALLOW_NON_ASCII = {"skills/pm-voice/references/anti-tells-ru.md"}

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    return m.group(1) if m else None


def field(fm, name):
    m = re.search(r'^%s:\s*(.*?)(?=\n[a-zA-Z_]+:|\Z)' % name, fm, re.S | re.M)
    return m.group(1).strip() if m else None


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "pm-copilot"
    if not os.path.isdir(root):
        print("Not a folder: %s" % root, file=sys.stderr)
        return 2

    print("Validating %s\n" % os.path.abspath(root))

    # ---- manifest
    mpath = os.path.join(root, ".claude-plugin", "plugin.json")
    if not os.path.isfile(mpath):
        err("missing .claude-plugin/plugin.json")
    else:
        try:
            man = json.load(open(mpath, encoding="utf-8"))
        except ValueError as exc:
            err("plugin.json is not valid JSON: %s" % exc)
            man = {}
        name = man.get("name", "")
        desc = man.get("description", "")
        ver = man.get("version", "")
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', name):
            err("plugin name is not kebab-case: %r" % name)
        if len(desc) > MAX_PLUGIN_DESC:
            err("plugin description is %d chars, limit %d" % (len(desc), MAX_PLUGIN_DESC))
        if not re.match(r'^\d+\.\d+\.\d+$', ver):
            err("plugin version is not semver: %r" % ver)
        print("  manifest: %s v%s, description %d/%d chars" % (name, ver, len(desc), MAX_PLUGIN_DESC))

    # ---- skills
    sdir = os.path.join(root, "skills")
    skills = sorted(d for d in os.listdir(sdir)) if os.path.isdir(sdir) else []
    print("\n  skills (%d):" % len(skills))
    for s in skills:
        sp = os.path.join(sdir, s, "SKILL.md")
        if not os.path.isfile(sp):
            err("%s: no SKILL.md" % s)
            continue
        text = open(sp, encoding="utf-8").read()
        fm = frontmatter(text)
        if fm is None:
            err("%s: SKILL.md has no --- frontmatter block" % s)
            continue
        # A ": " inside an unquoted description is a nested mapping to a strict
        # parser. The regex below reads it fine, so check with a real one.
        if yaml is not None:
            try:
                yaml.safe_load(fm)
            except yaml.YAMLError as exc:
                err("%s: frontmatter is not strict YAML (use ' - ', not ': ', in an unquoted "
                    "description): %s" % (s, str(exc).splitlines()[0]))
        n = field(fm, "name")
        d = field(fm, "description")
        if n != s:
            err("%s: frontmatter name %r does not match folder name" % (s, n))
        if not d:
            err("%s: no description in frontmatter" % s)
            continue
        flag = "OVER" if len(d) > MAX_SKILL_DESC else "ok  "
        print("    %s %4d/%d  %s" % (flag, len(d), MAX_SKILL_DESC, s))
        if len(d) > MAX_SKILL_DESC:
            err("%s: description is %d chars, limit %d (trim %d)"
                % (s, len(d), MAX_SKILL_DESC, len(d) - MAX_SKILL_DESC))

    # ---- the docs PMs read describe what actually ships
    # Added 2026-09-24: pmo-guide shipped in 0.42.3 and pm-voice was built in 0.43.0 with the
    # README still saying v0.41.0 and the field guide "seventeen". Nothing caught it.
    print("\n  docs match the skills:")
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
             "eighteen", "nineteen", "twenty", "twenty-one", "twenty-two", "twenty-three",
             "twenty-four", "twenty-five"]
    shipped_ver = man.get("version", "") if os.path.isfile(mpath) else ""
    for doc in ("README.md", "pm-copilot-field-guide.html"):
        dp = os.path.join(root, doc)
        if not os.path.isfile(dp):
            err("%s not found - PMs read it, it must ship" % doc)
            continue
        dt = open(dp, encoding="utf-8").read()
        missing = [s for s in skills if s not in dt]
        if missing:
            err("%s does not mention: %s" % (doc, ", ".join(missing)))
        counts = {int(n) for n in re.findall(r'\b(\d+) skills\b', dt)}
        counts |= {words.index(w.lower()) for w in
                   re.findall(r'\b(%s)\b(?= skills|</h2>)' % "|".join(words), dt, re.I)}
        wrong = sorted(c for c in counts if c != len(skills))
        if wrong:
            err("%s gives a skill count of %s, but %d skills ship" % (doc, wrong, len(skills)))
        stale = sorted({v for v in re.findall(r'\bv(\d+\.\d+\.\d+)\b', dt) if v != shipped_ver})
        if stale:
            err("%s names version %s, the manifest is %s - drop the version or fix it"
                % (doc, ", ".join(stale), shipped_ver))
        if not (missing or wrong or stale):
            print("    ok    %s: all %d skills, count and version consistent" % (doc, len(skills)))

    # ---- the NotebookLM sign-in command a PM types must match the server the extension runs
    # Added 2026-09-24: SETUP.md gives PMs a terminal fallback with a pinned version. If it drifts
    # from the pmc-nlm pin, the sign-in and the server are different builds.
    here = os.path.dirname(os.path.abspath(__file__))
    nlm_manifest = os.path.join(here, "mcpb-src", "pmc-nlm", "manifest.json")
    if os.path.isfile(nlm_manifest):
        pin = re.findall(r"notebooklm-mcp-cli==([0-9.]+)", open(nlm_manifest, encoding="utf-8").read())
        pin = pin[0] if pin else None
        for doc in ("SETUP.md", os.path.join("skills", "copilot-setup", "SKILL.md")):
            dp = os.path.join(root, doc)
            if not os.path.isfile(dp):
                continue
            found = set(re.findall(r"notebooklm-mcp-cli==([0-9.]+)", open(dp, encoding="utf-8").read()))
            bad = sorted(v for v in found if v != pin)
            if bad:
                err("%s pins notebooklm-mcp-cli %s, the pmc-nlm extension pins %s" % (doc, ", ".join(bad), pin))

    # ---- content hygiene across every shipped text file
    print("\n  content checks:")
    bad_ascii, bad_dash, bad_paths, bad_py = [], [], [], []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [x for x in dirnames if x not in SKIP_DIRS]
        for fn in filenames:
            if fn in SKIP_FILES:
                continue
            if not fn.endswith((".md", ".py", ".json", ".ps1", ".sh", ".yaml", ".yml")):
                continue
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(p, root)
            raw = open(p, "rb").read()
            try:
                raw.decode("ascii")
            except UnicodeDecodeError:
                if rel.replace(os.sep, "/") not in ALLOW_NON_ASCII:
                    bad_ascii.append(rel)
                elif raw.startswith(b"\xef\xbb\xbf"):
                    err("%s: UTF-8 BOM - write it with node, bash or the Write tool, not PowerShell" % rel)
            txt = raw.decode("utf-8", errors="replace")
            if "\u2014" in txt or "\u2013" in txt:
                bad_dash.append(rel)
            for frag in AUTHOR_LOCAL:
                if frag in txt:
                    bad_paths.append("%s (%s)" % (rel, frag))
                    break
            # "python3 " in prose is fine now that we lead with the Cowork sandbox,
            # but a bare "python3 script.py" as the ONLY instruction is not.
            if fn.endswith(".md") and re.search(r'^python3 (?!")', txt, re.M):
                bad_py.append(rel)

    for label, items in [("non-ASCII", bad_ascii), ("em/en dashes", bad_dash),
                         ("author-local paths", bad_paths), ("unquoted python3 call", bad_py)]:
        if items:
            err("%s in: %s" % (label, ", ".join(sorted(set(items)))))
        else:
            print("    ok    no %s" % label)

    # ---- scripts compile
    print("\n  scripts:")
    import py_compile, tempfile
    tmpc = os.path.join(tempfile.gettempdir(), "pmcopilot-validate.pyc")
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [x for x in dirnames if x != "__pycache__"]
        for fn in filenames:
            if fn.endswith(".py"):
                p = os.path.join(dirpath, fn)
                try:
                    py_compile.compile(p, doraise=True, cfile=tmpc)
                    print("    ok    compiles: %s" % os.path.relpath(p, root))
                except py_compile.PyCompileError as exc:
                    err("%s does not compile: %s" % (os.path.relpath(p, root), exc))

    for sh in ("scripts/setup/install-pm-copilot.sh",):
        p = os.path.join(root, sh)
        if os.path.isfile(p):
            if os.system("bash -n '%s' 2>/dev/null" % p) == 0:
                print("    ok    bash syntax: %s" % sh)
            else:
                err("%s has a bash syntax error" % sh)
        else:
            warn("%s not found" % sh)

    # ---- report
    print()
    if yaml is None:
        warn("PyYAML not installed, strict-YAML frontmatter check skipped (pip install pyyaml)")
    for w in warnings:
        print("  WARN  %s" % w)
    if errors:
        print("\nFAILED - %d problem(s), do not package:\n" % len(errors))
        for e in errors:
            print("  - %s" % e)
        return 1
    print("PASS - safe to package.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
