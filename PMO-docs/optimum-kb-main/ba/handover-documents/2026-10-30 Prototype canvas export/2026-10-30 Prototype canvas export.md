# 2026-10-30 Prototype canvas export

Anton's export of the Design canvas "Optimum prototypes v0 - topics 1 and 2", for the BA. Written by
Anton's agent (claude-cowork/claude-opus-5-5) on 30 October, at Anton's request. Working material, not
evidence (`ba/AGENTS.md`). Nothing here is ingested. The canvas is the v0 described in
[[2026-10-18 Discovery prototypes v0 - README]], with the 23 October additions (calculated values,
retort oil, funnel viscosity, 60 and 30 RPM).

The master is Anton's canvas. This folder is a snapshot of it: send change requests to Anton, or send back
the changed files and say what changed. Do not keep a parallel design.

## What is in `project/`

- `canvas.json` - the layout: frame positions and titles, section titles, and the three stickies (about,
  rig app assumptions, HQ web app assumptions).
- `Main.dc.html` - the whole rig app (desktop, offline).
- `Web.dc.html` - the whole HQ web app.
- Nine small `.dc.html` files - each opens Main or Web at one screen and role.

No uploaded images or fonts; the only outside resource is IBM Plex from Google Fonts. Comments and version
history are not included.

## Loading it into your own canvas

You need a Claude account where Claude can create a **Design** canvas (an artifact type; check that your
plan offers it).

1. Open a new chat in Claude (Cowork with this folder connected, or claude.ai with the `project/` files
   attached).
2. Paste the prompt below.

```
Create a new Design canvas titled "Optimum prototypes v0 - topics 1 and 2" from the Design artifact type.
Then publish the files from the folder "ba/handover-documents/2026-10-30 Prototype canvas export/project/" into it exactly as
they are, each at its own path under project/ (project/canvas.json plus the 11 .dc.html files), in one
publish call. Do not change, reformat, redesign or "fix" any file: this is a restore of an existing canvas.
Keep canvas.json as given, including its createdOnFiles object.
When done, give me the link. Do not verify or screenshot it.
```

## Using it

- Three rows: rig app, HQ web app, HQ web app topic 2.
- Each frame is live: press **Play** on a frame and click through.
- The rig app starts offline; click the sync status in its header to bring the connection back.
- Every name, rig, well, job and value is made up; the ranges are examples, not the client's.

## Keeping in step

When the canvas changes, Anton replaces the files here with a new export and syncs. To refresh your
canvas, ask your Claude to publish these files into your existing canvas link, replacing the ones there.
