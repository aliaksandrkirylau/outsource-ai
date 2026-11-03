"""PM Copilot runtime probe - a deliberately useless MCP server.

It exists to answer one question that decides how the copilot ships its tools:
can a .mcpb extension carry its own uv binary and bootstrap a Python MCP server
on a machine that has neither Python nor uv?

WHAT v0.1 GOT WRONG, because it is the whole lesson of this file. The first
version redirected UV_CACHE_DIR and UV_PYTHON_INSTALL_DIR inside the extension
folder, on the reasoning that a self-contained bundle should keep its files to
itself. On Windows that is fatal. The extension folder path is already about 145
characters, and uv's cache adds
"uv-cache\\archive-v0\\<hash>\\Lib\\site-packages\\" before a package name even
starts - roughly 191 characters of a 260 character budget. uv downloaded all 98 MB
successfully and then Python could not read its own site-packages back:

    FileNotFoundError: [WinError 3] ...jsonschema_specifications\\schemas\\
    draft201909\\metaschema.json          (270 chars, MAX_PATH is 260)

The goal is ZERO PREREQUISITES, not zero footprint. uv's normal per-user cache
needs nothing pre-installed and is short. So the only thing this bundle ships is
the uv binary; uv keeps its cache and interpreters where it normally does.

Corollary worth remembering: keep extension names short. Every character in
"local.mcpb.<author>.<name>" is a character taken from the path budget.

ASCII only - this ends up on a Windows machine.
"""

import os
import platform
import shutil
import sys

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("pm-copilot-probe")


def _is_uv_managed(path):
    """Is this interpreter one uv downloaded, rather than a system install?

    uv names its managed builds cpython-<version>-<platform>, so that marker in
    the base prefix is the signal. Deliberately NOT "is it inside the extension
    folder" - that was the v0.1 test, and it only passed in the configuration
    that breaks on MAX_PATH.
    """
    if not path:
        return False
    low = path.replace("/", "\\").lower()
    return "cpython-" in low


@mcp.tool()
def pm_copilot_probe() -> str:
    """Report which Python and uv this extension used, and where they came from."""
    base = sys.base_prefix
    managed = _is_uv_managed(base)
    verdict = (
        "SELF-CONTAINED - uv downloaded this interpreter, so a machine with no "
        "Python and no uv would have worked"
        if managed
        else "BORROWED - this is a system interpreter, so it does NOT prove a "
        "clean machine would work"
    )

    lines = [
        "PM Copilot runtime probe",
        "",
        "verdict            : " + verdict,
        "",
        "python version     : " + sys.version.split()[0],
        "sys.base_prefix    : " + base,
        "  uv-managed build : " + str(managed),
        "",
        "extension folder   : " + os.environ.get("PMC_PROBE_DIRNAME", "(not set)"),
        "uv on PATH         : " + str(shutil.which("uv") or "not found"),
        "python on PATH     : " + str(shutil.which("python") or "not found"),
        "",
        "mcp package from   : " + _mcp_location(),
        "platform           : " + platform.platform(),
    ]

    # Path length is the thing that broke v0.1, so report the headroom rather than
    # waiting to trip over it again.
    longest = max((len(p) for p in sys.path if p), default=0)
    lines += [
        "",
        "longest sys.path    : " + str(longest) + " chars (Windows MAX_PATH is 260 "
        "unless long paths are enabled)",
    ]
    return "\n".join(lines)


def _mcp_location():
    try:
        import mcp as _m

        return getattr(_m, "__file__", "(unknown)") or "(unknown)"
    except Exception as exc:  # pragma: no cover - diagnostic only
        return "import failed: %s" % exc


if __name__ == "__main__":
    mcp.run()
