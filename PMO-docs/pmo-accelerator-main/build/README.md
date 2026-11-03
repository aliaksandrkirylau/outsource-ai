# build - release tooling for the PM Copilot

Lives in the repo so the tooling is versioned with the plugin it builds. Not part of the plugin:
the packer and the validator both skip this folder, so nothing here ships to a PM.

| File | What it does |
|---|---|
| `pack-pm-copilot.py` | `pack` validates, builds `pm-copilot.plugin` and the dated zip. `publish` stages a release for Drive and refuses unless git holds the build. `verify` checks an artifact against the source |
| `validate-plugin.py` | The checks that have bitten us: manifest, strict YAML, description limits, ASCII, dashes, author-local paths, and whether README and the field guide still describe what ships |
| `Test-CleanInstall.ps1` | Checks a clean install on a Windows machine in a throwaway profile |
| `mcpb-src/` | Source of the three `.mcpb` extensions (Google Workspace, NotebookLM, Sheets) |
| `mcpb-probe/` | A small diagnostic extension |

## One file you need that git does not have

`mcpb-src/pmc-sheets/client_secret.json` - the Google OAuth Desktop client JSON from GCP project
121722741974. It is gitignored and must stay that way: the repo is readable across the org and
git history is permanent. The pmc-gws manifest carries the placeholder `__FROM_client_secret.json__`
and the packer fills it in memory at build time. Without the file, `pack` stops and says so.

`publish` also refuses if any tracked file contains a Google OAuth secret, or if that file stops
being ignored.

## A release

The full sequence, and why each step is required, is in `pm-copilot/CLAUDE.md` in the author's
workspace. Short version, from `pm-copilot/`:

1. Update `source/README.md` and `source/pm-copilot-field-guide.html` with the change.
2. `python source/build/pack-pm-copilot.py pack --version X.Y.Z --label <date>`
3. From `source/`: commit, `git tag -a vX.Y.Z`, push `main` and the tag.
4. `python source/build/pack-pm-copilot.py publish --label <date> --note "..."`, then the three
   Drive calls it prints.

The Drive folder IDs in the packer are the author's distribution folder. Anyone else releasing
needs write access to it, or their own IDs.
