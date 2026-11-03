#!/usr/bin/env python3
"""Pack the PM Copilot plugin and its distribution zip, with a drift guard.

The pack has silently lagged the source twice (2026-09-03: rules/copilot-baseline.md
and skills/copilot-setup/SKILL.md were edited an hour after the pack, and a PM
installed the stale build). This script makes that impossible to do quietly:

  verify  - compare an existing artifact against the source tree, exit 1 on drift
  pack    - run the validator (refuses on failure, including docs that no longer describe
            what ships), rebuild pm-copilot.plugin and dist/PM-Copilot-alpha-<date>.zip,
            then verify what it just wrote before declaring success
  publish - stage a packed release for the Drive folder PMs install from: re-verify,
            re-validate, refuse unless source/ is committed, tagged v<version> and pushed,
            add the CHANGELOG line, copy the files where the Workspace MCP can read
            them, and print the calls that finish the job (START HERE Doc, zip, dated copy, changelog,
            field guide PDF on Drive, and the install guide page on Confluence)

Entry names are built by hand with forward slashes. PowerShell's
Compress-Archive / ZipFile::CreateFromDirectory can emit backslash separators,
which the plugin installer rejects after a long apparent upload.

Usage:
    python pack-pm-copilot.py verify
    python pack-pm-copilot.py pack [--version 0.40.1] [--label 2026-09-09]
    python pack-pm-copilot.py publish --note "what changed" [--label 2026-09-09]
"""

import argparse
import datetime
import hashlib
import io
import json
import os
import shutil
import sys
import zipfile

# Paths, rewritten 2026-09-21 after the 09-18 move into pm-copilot/. They were still pointing at
# the old skills-to-upload layout, where the packer sat beside the source tree. SRC resolved to a
# folder that does not exist, and os.walk on a missing directory yields nothing rather than
# raising - so a pack would have written an EMPTY .plugin and the drift guard would have reported
# every real file as an orphan. Worth knowing: this script's guard protects the artifact against
# the source, and nothing was protecting the script against the repo being reorganised.
#
# 2026-09-24: build/ moved INTO source/ so the tooling is versioned with the plugin it builds. SRC
# is found as the folder holding .claude-plugin rather than assumed, so this works from either
# place and a second move cannot silently point it at nothing again.
HERE = os.path.dirname(os.path.abspath(__file__))   # pm-copilot/source/build
if os.path.isdir(os.path.join(os.path.dirname(HERE), ".claude-plugin")):
    SRC = os.path.dirname(HERE)                     # the plugin itself - this is what ships
else:
    SRC = os.path.join(os.path.dirname(HERE), "source")
if not os.path.isdir(os.path.join(SRC, ".claude-plugin")):
    raise SystemExit("cannot find the plugin source (no .claude-plugin) near " + HERE)
ROOT = os.path.dirname(SRC)                         # pm-copilot - dist/ and CHANGELOG.txt live here
DIST = os.path.join(ROOT, "dist")
PLUGIN = os.path.join(DIST, "pm-copilot.plugin")

# The three .mcpb extension bundles. Built from mcpb-src/ since 2026-09-09;
# before that they were opaque blobs byte-copied between dist zips, which is how
# PowerShell ConvertTo-Json escaping ("<" as <) survived unnoticed in them.
MCPB_SRC = os.path.join(HERE, "mcpb-src")
MCPB = ["pmc-gws.mcpb", "pmc-nlm.mcpb", "pmc-sheets.mcpb"]
# Copied to the TOP of the dist zip as well as shipping inside the .plugin, because a PM has to be
# able to open them without unpacking anything. The field guide joined them 2026-09-21: it lives in
# source/ so git tracks it beside the skills it documents, which is the only thing that makes it get
# updated when they change. Only the HTML - the PDF is derived from it and lives in dist/, because a
# second copy of the same document is a copy that can silently disagree with the first.
# BEFORE-YOU-START.md folded into SETUP.md 2026-09-24 - one guide, published to Drive as START HERE.
LOOSE = ["SETUP.md", "pm-copilot-field-guide.html"]

JUNK_DIRS = {".git", "__pycache__", ".DS_Store"}
# build/ is in the repo but is not the plugin. Skipped for packing and validating, NOT for git_gate.
SKIP_DIRS = JUNK_DIRS | {"build"}

# The OAuth client secret. Untracked (see source/.gitignore); the packer reads it at build time.
SECRET_FILE = os.path.join(MCPB_SRC, "pmc-sheets", "client_secret.json")
SECRET_PLACEHOLDER = "__FROM_client_secret.json__"

# Distribution, decided 2026-09-23: PMs install from a Drive folder, not from git. The link that
# gets shared is LATEST_ZIP, and it only stays constant because a release REPLACES its content in
# place - deleting and re-uploading it, or keeping a "latest" folder of swapped files, mints a new
# file ID and breaks every link already sent. This script cannot reach Drive itself (no Google
# credentials of its own), so it stages and the Workspace MCP uploads. That MCP only reads files
# under ATTACHMENTS; a path anywhere else fails with "Local file could not be accessed".
DRIVE_FOLDER = "1A3aIWCtIzj-JbVrxMqzbhD4vIY61q1nV"      # PM Copilot/
DRIVE_VERSIONS = "1Ad2Yv5ot6gJGm3iXmEe96ZzPQxZsW5PV"    # PM Copilot/versions/
DRIVE_LATEST_ZIP = "1NcsEQM7zQZNOeMWFDH5tTHnl7hsdFNRC"  # PM-Copilot-latest.zip - the shared link
DRIVE_CHANGELOG = "1oMeZuF4o5Q50z95dJrOzjJuldgSFSWLQ"  # CHANGELOG.txt in the folder
CHANGELOG = os.path.join(ROOT, "CHANGELOG.txt")
# The install guide as a native Google Doc in the folder - the first thing a PM opens. Built from
# SETUP.md at every publish. None until the first one is created; publish then says how.
DRIVE_START_HERE = "1nPWpXLkbW0FDr7pNsEP0LhZvW-oIMNTrQC3o72LRy9c"  # PM Copilot - START HERE
START_HERE_NAME = "PM Copilot - START HERE"
# What the extensions were at the last publish, so the changelog can say when to reinstall them.
EXT_STATE = os.path.join(ROOT, "dist", "published-extensions.json")
# The field guide as a PDF in the folder root - "how to use it" for a PM who has not unpacked
# anything. Printed from the HTML by pack; None until the first upload; publish then says how.
DRIVE_FIELD_GUIDE_PDF = "1rVTVqpCIL1ghLs0RI_5BJm4CYFAjLSn6"  # PM-Copilot-Field-Guide.pdf, folder root
FIELD_GUIDE_PDF = os.path.join(DIST, "PM-Copilot-Field-Guide.pdf")
# The same guide on Confluence, agreed at AI PMO 2026-09-24 so PMs find it where they look for
# process pages. Child of [DRAFT] Claude and PM Copilot. Rebuilt from SETUP.md by every publish,
# so it is not a fourth copy anyone maintains by hand. The H1 is dropped: Confluence shows the title.
CONFLUENCE_GUIDE_PAGE = "5435752483"
BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]
ATTACHMENTS = os.path.join(os.path.expanduser("~"), ".workspace-mcp", "attachments")

# In source/ but deliberately NOT shipped. The git repo is internal and colleagues can read the
# design history there; the .plugin is a distributed artifact and a PM installing it has no use for
# 44 KB of build log whose wikilinks resolve to nothing on their machine. The file only became a
# candidate because the 2026-09-18 move put it under source/, which was a filing decision rather
# than a shipping one. Excluded 2026-09-21.
SKIP_FILES = {"PLUGIN-DESIGN-LOG.md"}


def oauth_client_secret():
    """The Google OAuth client secret, read from the untracked client_secret.json.

    One file feeds both bundles: pmc-sheets ships it as-is, pmc-gws gets its client_secret
    field injected into the manifest env. Same OAuth client, verified 2026-09-24.
    """
    if not os.path.isfile(SECRET_FILE):
        raise SystemExit(
            "missing %s\n"
            "It holds the Google OAuth client secret and is deliberately not in git. Download the\n"
            "Desktop OAuth client JSON from GCP project 121722741974 and save it at that path."
            % SECRET_FILE)
    with open(SECRET_FILE, encoding="utf-8") as fh:
        data = json.load(fh)
    secret = (data.get("installed") or data.get("web") or {}).get("client_secret", "")
    if not secret:
        raise SystemExit("%s has no installed.client_secret" % SECRET_FILE)
    return secret


def build_mcpb(version=None):
    """Build each .mcpb from mcpb-src/<name>/ and return {filename: bytes}.

    Env vars that every bundle must carry, from Tanya Pinchuk's 2026-09-08
    report on the Innowise corporate network - all three are asserted here
    rather than trusted, because a missing one fails at OAuth time on the
    user's machine with nothing naming us as the cause:

      UV_SYSTEM_CERTS        uv is Rust/rustls with its own CA bundle and does
                             not trust the corporate root cert Windows trusts
      UV_PYTHON_INSTALL_DIR  endpoint security blocks uv's exe/DLL writes
                             under %AppData%
      pip-system-certs       (a --with arg) patches Python's ssl module to use
                             the OS store; certifi's fixed list breaks the
                             Google OAuth token exchange
    """
    REQUIRED_ENV = ["UV_SYSTEM_CERTS", "UV_PYTHON_INSTALL_DIR"]
    REQUIRED_WITH = "pip-system-certs"

    out = {}
    for name in MCPB:
        stem = name[:-5]
        d = os.path.join(MCPB_SRC, stem)
        if not os.path.isdir(d):
            raise SystemExit("missing mcpb source: " + d)

        mpath = os.path.join(d, "manifest.json")
        with open(mpath, encoding="utf-8") as fh:
            manifest = json.load(fh)

        cfg = manifest["server"]["mcp_config"]
        env = cfg.get("env", {})
        missing = [k for k in REQUIRED_ENV if k not in env]
        if missing:
            raise SystemExit("%s: manifest missing env %s" % (stem, ", ".join(missing)))
        if REQUIRED_WITH not in cfg.get("args", []):
            raise SystemExit("%s: manifest args missing --with %s" % (stem, REQUIRED_WITH))

        if version and version != manifest.get("version"):
            print("  %s version %s -> %s" % (stem, manifest.get("version"), version))
            manifest["version"] = version
            with open(mpath, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(manifest, fh, indent=2, ensure_ascii=False)
                fh.write("\n")

        # The OAuth client secret is not in git. A tracked manifest carries SECRET_PLACEHOLDER and
        # the real value is filled in here, in memory, from the one untracked file that holds it.
        # The on-disk manifest is never rewritten with it (the version write-back above ran first).
        env = manifest["server"]["mcp_config"].get("env", {})
        for k, v in env.items():
            if v == SECRET_PLACEHOLDER:
                env[k] = oauth_client_secret()
        body = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
        if SECRET_PLACEHOLDER in body:
            raise SystemExit("%s: placeholder left unfilled in the built manifest" % stem)

        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
            # ensure_ascii=False so punctuation stays literal - the escaped form
            # is valid JSON but silently breaks text-based find/replace, which
            # cost real time during the 2026-09-08 diagnosis.
            z.writestr("manifest.json", body)
            for extra in sorted(os.listdir(d)):
                if extra == "manifest.json":
                    continue
                z.write(os.path.join(d, extra), arcname=extra)
        out[name] = buf.getvalue()
        print("  built %s (%d bytes, v%s)" % (name, len(out[name]), manifest["version"]))
    return out


def source_files():
    """Every file in the source tree, as (entry_name, absolute_path)."""
    out = []
    for root, dirs, files in os.walk(SRC):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            if name in SKIP_DIRS or name in SKIP_FILES or name.endswith(".pyc"):
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, SRC).replace(os.sep, "/")
            out.append((rel, path))
    return sorted(out)


def md5(data):
    return hashlib.md5(data).hexdigest()


def verify(archive_path):
    """Compare a .plugin against the source tree. Returns a list of problems."""
    problems = []
    if not os.path.exists(archive_path):
        return ["artifact does not exist: " + archive_path]

    with zipfile.ZipFile(archive_path) as z:
        in_zip = {n: z.read(n) for n in z.namelist() if not n.endswith("/")}

    src = dict(source_files())

    for rel, path in src.items():
        if rel not in in_zip:
            problems.append("MISSING from artifact: " + rel)
            continue
        with open(path, "rb") as fh:
            data = fh.read()
        if md5(data) != md5(in_zip[rel]):
            problems.append(
                "STALE in artifact: %s (packed %d bytes, source %d bytes, %+d)"
                % (rel, len(in_zip[rel]), len(data), len(data) - len(in_zip[rel]))
            )

    for rel in in_zip:
        if rel not in src:
            problems.append("ORPHAN in artifact (not in source): " + rel)
        if "\\" in rel:
            problems.append("BACKSLASH in entry name (installer will reject): " + rel)

    return problems


def build_field_guide_pdf():
    """Print source/pm-copilot-field-guide.html to dist/ as an A4 PDF with a headless browser.

    A throwaway profile is required: with the default one, a browser already open on the machine
    swallows the headless call and exits 0 having written nothing (seen with Edge 2026-09-24).
    So success is judged by the file's mtime, not the exit code.
    """
    import subprocess, tempfile, time
    browser = next((b for b in BROWSERS if os.path.isfile(b)), None)
    if not browser:
        raise SystemExit("no Chrome or Edge found to print the field guide PDF")
    html = os.path.join(SRC, "pm-copilot-field-guide.html")
    url = "file:///" + html.replace(os.sep, "/").replace(" ", "%20")
    started = time.time()
    with tempfile.TemporaryDirectory() as prof:
        subprocess.run([browser, "--headless=new", "--disable-gpu", "--no-first-run",
                        "--user-data-dir=" + prof, "--no-pdf-header-footer",
                        "--print-to-pdf=" + FIELD_GUIDE_PDF, url],
                       capture_output=True, timeout=120)
    if not os.path.isfile(FIELD_GUIDE_PDF) or os.path.getmtime(FIELD_GUIDE_PDF) < started - 1:
        raise SystemExit("the browser did not write %s - print it by hand and re-run" % FIELD_GUIDE_PDF)
    print("wrote %s (%d bytes)" % (FIELD_GUIDE_PDF, os.path.getsize(FIELD_GUIDE_PDF)))


def pack(version, label, mcpb_version):
    # Validate before building. The validator carries the checks that have bitten us - strict YAML,
    # description limits, ASCII, and since 2026-09-24 whether README and the field guide still
    # describe what ships. It only helps if it runs, so pack runs it rather than trusting a person to.
    import subprocess
    check = subprocess.run([sys.executable, os.path.join(HERE, "validate-plugin.py"), SRC])
    if check.returncode != 0:
        print()
        print("PACK REFUSED - the validator failed. Fix the source, then pack again.")
        return 1

    manifest_path = os.path.join(SRC, ".claude-plugin", "plugin.json")
    with open(manifest_path, encoding="utf-8") as fh:
        manifest = json.load(fh)

    if version and version != manifest.get("version"):
        old = manifest.get("version")
        manifest["version"] = version
        with open(manifest_path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(manifest, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print("manifest version %s -> %s" % (old, version))
    version = manifest["version"]

    # --- the .plugin ---
    files = source_files()
    if os.path.exists(PLUGIN):
        shutil.copy2(PLUGIN, PLUGIN + ".bak")
    with zipfile.ZipFile(PLUGIN, "w", zipfile.ZIP_DEFLATED) as z:
        for rel, path in files:
            assert "\\" not in rel, rel
            z.write(path, arcname=rel)
    print("wrote %s (%d entries, %d bytes)" % (PLUGIN, len(files), os.path.getsize(PLUGIN)))

    problems = verify(PLUGIN)
    if problems:
        print("\nPACK FAILED - the artifact does not match the source:")
        for p in problems:
            print("  " + p)
        return 1

    # --- the dist zip ---
    print("\nextension bundles:")
    mcpb_blobs = build_mcpb(mcpb_version)

    os.makedirs(DIST, exist_ok=True)
    out = os.path.join(DIST, "PM-Copilot-alpha-%s.zip" % label)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(PLUGIN, arcname="pm-copilot.plugin")
        for name in LOOSE:
            z.write(os.path.join(SRC, name), arcname=name)
        for name, blob in mcpb_blobs.items():
            z.writestr(name, blob)
    print("wrote %s (%d bytes)" % (out, os.path.getsize(out)))
    build_field_guide_pdf()
    print("\nOK - artifact matches source. version %s, %d files, %d skills." % (
        version, len(files),
        len({r.split("/")[1] for r, _ in files if r.startswith("skills/")}),
    ))
    return 0


def extension_fingerprint(zpath):
    """{bundle name: md5 of its contents} for the .mcpb files in a dist zip.

    Hashes what is INSIDE each bundle, not the bundle bytes, because zip timestamps change on
    every build while the content does not.
    """
    out = {}
    with zipfile.ZipFile(zpath) as z:
        for name in MCPB:
            inner = zipfile.ZipFile(io.BytesIO(z.read(name)))
            h = hashlib.md5()
            for n in sorted(inner.namelist()):
                h.update(n.encode("utf-8"))
                h.update(inner.read(n))
            out[name] = h.hexdigest()
    return out


def git_gate(version):
    """A release on Drive must be the commit on origin. Returns a list of problems.

    Added 2026-09-24: 0.42.2 to 0.43.0 all went to PMs from Drive while the repo sat at 0.42.1,
    so git said one thing and every PM's install said another. Untracked files the packer never
    ships (SKIP_FILES, SKIP_DIRS) do not count as dirty; anything else uncommitted does.
    """
    import subprocess

    def git(*args):
        r = subprocess.run(["git", "-C", SRC] + list(args), capture_output=True, text=True)
        return r.returncode, r.stdout.strip()

    problems = []
    code, out = git("status", "--porcelain")
    if code != 0:
        return ["source/ is not a git repository, or git is not installed"]
    for line in out.splitlines():
        path = line[3:].strip().strip('"')
        parts = path.rstrip("/").split("/")
        if line.startswith("??") and (parts[-1] in SKIP_FILES or any(p in JUNK_DIRS for p in parts)):
            continue
        problems.append("uncommitted: " + line)

    # A Google OAuth client secret has a fixed prefix (matched below, written as a character class
    # so this line does not match itself). None may be tracked, in any file, ever:
    # the repo is org-readable and history is permanent.
    code, hits = git("grep", "-l", "-I", "-E", "GOCSP[X]-", "--", ".")
    if code == 0 and hits:
        problems.append("OAuth secret in tracked files: " + ", ".join(hits.splitlines()))
    code, _ = git("check-ignore", "-q", os.path.relpath(SECRET_FILE, SRC).replace(os.sep, "/"))
    if code != 0:
        problems.append("%s is not ignored by .gitignore" % os.path.relpath(SECRET_FILE, SRC))

    tag = "v" + version
    _, tags = git("tag", "--points-at", "HEAD")
    if tag not in tags.split():
        problems.append("HEAD is not tagged %s" % tag)

    _, head = git("rev-parse", "HEAD")
    _, branch = git("rev-parse", "--abbrev-ref", "HEAD")
    _, remote = git("ls-remote", "origin", "refs/heads/" + branch)
    if not remote or remote.split()[0] != head:
        problems.append("origin/%s is not at HEAD %s - the commit is not pushed" % (branch, head[:7]))
    _, rtag = git("ls-remote", "--tags", "origin", "refs/tags/" + tag)
    if not rtag:
        problems.append("tag %s is not on origin" % tag)
    return problems


def publish(label, note):
    """Stage a packed release for Drive. Changes nothing remote; prints what to run."""
    if not note or not note.strip():
        print("publish needs --note: one line on what changed, written for a PM")
        return 1
    note = " ".join(note.split())
    if not all(ord(c) < 128 for c in note):
        print("--note must be plain ASCII (CHANGELOG.txt is read on Windows by non-technical PMs)")
        return 1

    # Publishing a stale build is the failure this whole script exists to stop, so check twice:
    # the .plugin against the source, and the dated zip against the .plugin.
    problems = verify(PLUGIN)
    if problems:
        print("NOT PUBLISHED - pm-copilot.plugin does not match the source:")
        for p in problems:
            print("  " + p)
        print()
        print("Run: python source/build/pack-pm-copilot.py pack --label %s" % label)
        return 1
    zpath = os.path.join(DIST, "PM-Copilot-alpha-%s.zip" % label)
    if not os.path.exists(zpath):
        print("NOT PUBLISHED - no dist zip for label %s: %s" % (label, zpath))
        return 1
    with zipfile.ZipFile(zpath) as z, open(PLUGIN, "rb") as fh:
        if md5(z.read("pm-copilot.plugin")) != md5(fh.read()):
            print("NOT PUBLISHED - %s carries a different pm-copilot.plugin than dist/." % zpath)
            print("Re-run pack with --label %s so the zip and the plugin are the same build." % label)
            return 1

    with zipfile.ZipFile(PLUGIN) as z:
        version = json.loads(z.read(".claude-plugin/plugin.json"))["version"]

    # Required for every release, before anything is staged: the docs describe what ships
    # (validator), and git holds exactly this build (git_gate).
    import subprocess
    if subprocess.run([sys.executable, os.path.join(HERE, "validate-plugin.py"), SRC],
                      capture_output=True).returncode != 0:
        print("NOT PUBLISHED - the validator fails on source. Run it for the detail:")
        print("  python source/build/validate-plugin.py source")
        return 1
    problems = git_gate(version)
    if problems:
        print("NOT PUBLISHED - git does not hold this build:")
        for p in problems:
            print("  " + p)
        print()
        print("From pm-copilot/source:")
        keep_out = " ".join("':!%s'" % f for f in sorted(SKIP_FILES))
        print('  git add -A -- . %s && git commit -m "PM Copilot v%s - <what changed>"' % (keep_out, version))
        print('  git tag -a v%s -m "PM Copilot v%s"' % (version, version))
        print("  git push origin HEAD && git push origin v%s" % version)
        return 1

    with open(CHANGELOG, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    tag = "  v%s  " % version
    if any(tag in l for l in lines):
        print("NOT PUBLISHED - v%s is already in CHANGELOG.txt. Bump --version on pack." % version)
        return 1
    # A PM reinstalls the extensions only when the changelog says so (SETUP.md, "Updating"). So the
    # sentence is added here from what actually changed, not from anyone remembering: the content
    # of each .mcpb in this zip is compared with the last published one.
    ext_now = extension_fingerprint(zpath)
    ext_prev = None
    if os.path.isfile(EXT_STATE):
        with open(EXT_STATE, encoding="utf-8") as fh:
            ext_prev = json.load(fh)
    if ext_prev is not None and ext_prev != ext_now:
        changed = sorted(n for n in ext_now if ext_now.get(n) != ext_prev.get(n))
        note = note.rstrip(".") + ". Reinstall the extensions."
        print("extensions changed since the last release: %s" % ", ".join(changed))
    elif ext_prev is None:
        print("no record of the last release's extensions - recording this one as the baseline")

    # Header is everything up to the first blank line; newest entry goes straight after it.
    cut = lines.index("") + 1
    lines.insert(cut, "%s%s%s" % (label, tag, note))
    # CRLF on purpose: PMs open this in Notepad from Drive, and it is the one file here that is
    # for people rather than for tools.
    with open(CHANGELOG, "w", encoding="utf-8", newline="\r\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print("CHANGELOG.txt: %s%s%s" % (label, tag, note))

    guide_html = os.path.join(SRC, "pm-copilot-field-guide.html")
    if (not os.path.isfile(FIELD_GUIDE_PDF)
            or os.path.getmtime(FIELD_GUIDE_PDF) < os.path.getmtime(guide_html)):
        print("NOT PUBLISHED - the field guide PDF is older than the HTML. Run pack again.")
        return 1

    with open(EXT_STATE, "w", encoding="utf-8") as fh:
        json.dump(ext_now, fh, indent=1)

    os.makedirs(ATTACHMENTS, exist_ok=True)
    staged_zip = os.path.join(ATTACHMENTS, os.path.basename(zpath))
    staged_log = os.path.join(ATTACHMENTS, "CHANGELOG.txt")
    staged_guide = os.path.join(ATTACHMENTS, START_HERE_NAME + ".md")
    shutil.copy2(zpath, staged_zip)
    shutil.copy2(CHANGELOG, staged_log)
    shutil.copy2(os.path.join(SRC, "SETUP.md"), staged_guide)
    staged_pdf = os.path.join(ATTACHMENTS, os.path.basename(FIELD_GUIDE_PDF))
    shutil.copy2(FIELD_GUIDE_PDF, staged_pdf)
    staged_conf = os.path.join(ATTACHMENTS, "confluence-guide-body.md")
    with open(os.path.join(SRC, "SETUP.md"), encoding="utf-8") as fh:
        guide = fh.read().replace("\r\n", "\n")
    with open(staged_conf, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(guide.split("\n", 2)[2].lstrip("\n"))
    url = lambda p: "file:///" + p.replace(os.sep, "/")

    print()
    print("Staged. Nothing is on Drive yet. Five Workspace MCP calls and one Confluence update finish it:")
    print()
    # The guide PMs open first, before they have the zip. Replaced in place from SETUP.md on every
    # release, so it cannot fall behind the build it describes.
    if DRIVE_START_HERE:
        print("0. update_drive_file  file_id=%s  file_path=%s  source_format=markdown"
              % (DRIVE_START_HERE, url(staged_guide)))
        print("   replaces the START HERE Doc IN PLACE from SETUP.md")
    else:
        print("0. FIRST RELEASE ONLY: import_to_google_doc  file_name=\"%s\"  file_path=%s  folder_id=%s"
              % (START_HERE_NAME, url(staged_guide), DRIVE_FOLDER))
        print("   then set DRIVE_START_HERE in this script to the new Doc's ID")
    print("1. update_drive_file  file_id=%s  file_path=%s" % (DRIVE_LATEST_ZIP, url(staged_zip)))
    print("   replaces PM-Copilot-latest.zip IN PLACE - same ID, same link, same sharing")
    print("2. create_drive_file  folder_id=%s  file_name=%s  mime_type=application/zip  fileUrl=%s"
          % (DRIVE_VERSIONS, os.path.basename(zpath), url(staged_zip)))
    print("3. update_drive_file  file_id=%s  file_path=%s" % (DRIVE_CHANGELOG, url(staged_log)))
    if DRIVE_FIELD_GUIDE_PDF:
        print("4. update_drive_file  file_id=%s  file_path=%s" % (DRIVE_FIELD_GUIDE_PDF, url(staged_pdf)))
        print("   replaces the field guide PDF IN PLACE, in the folder root")
    else:
        print("4. FIRST RELEASE ONLY: create_drive_file  folder_id=%s  file_name=%s  "
              "mime_type=application/pdf  fileUrl=%s"
              % (DRIVE_FOLDER, os.path.basename(FIELD_GUIDE_PDF), url(staged_pdf)))
        print("   then set DRIVE_FIELD_GUIDE_PDF in this script to the new file's ID")
    print("5. Atlassian updateConfluencePage  pageId=%s  contentFormat=markdown  body=<contents of %s>"
          % (CONFLUENCE_GUIDE_PAGE, staged_conf))
    print("   keep the title; the body is SETUP.md without its H1")
    print()
    print("Then check the latest zip's size on Drive is %d bytes." % os.path.getsize(zpath))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["verify", "pack", "publish"])
    ap.add_argument("--version", default=None, help="set the manifest version before packing")
    ap.add_argument(
        "--label",
        default=datetime.date.today().isoformat(),
        help="date label for the dist zip filename",
    )
    ap.add_argument(
        "--mcpb-version", default=None, help="set the version on all three .mcpb manifests"
    )
    ap.add_argument("--note", default=None, help="publish: one line on what changed, for PMs")
    args = ap.parse_args()

    if args.mode == "publish":
        return publish(args.label, args.note)

    if args.mode == "verify":
        problems = verify(PLUGIN)
        if problems:
            print("DRIFT - the packed artifact does not match the source:")
            for p in problems:
                print("  " + p)
            print("\nRun: python pack-pm-copilot.py pack")
            return 1
        print("OK - pm-copilot.plugin matches the source tree.")
        return 0

    return pack(args.version, args.label, args.mcpb_version)


if __name__ == "__main__":
    sys.exit(main())
