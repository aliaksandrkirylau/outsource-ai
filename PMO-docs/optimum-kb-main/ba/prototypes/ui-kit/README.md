# UI kit options - README

Internal, never sent. Leu's working material, not evidence (`ba/AGENTS.md`); local, not shared yet.
Written by Leu's agent (claude-code/claude-opus-5-5) on 2 November 2026.

## What is here

`OES UI kit options.html` with `option-A.png`, `option-B.png`, `option-C.png`: the three UI kit
options for the client to choose from in S00 ([[S00 Vision and UI kit]],
[[DEC-017 Choose the UI kit with the client from three variants]]). Opens in any browser offline; keep
the four files together and send them as one zip. The screenshots are separate files, not embedded:
embedded image data trips the KB money check (random base64 text can look like a currency code followed
by a digit), which would stop kb-sync. For the client and, later, the developers, so the Material widget names stay.

| Option | Colour | Feel |
|---|---|---|
| A: OES Brand, "Warm" | Brand orange #ED712E from oes.com.sa | Branded, familiar Material |
| B: "Crisp" | Slate blue-grey #455A64 | Precise, data-dense, tool-like |
| C: "Calm" | Ocean blue #0B6BCB | Soft, spacious, approachable |

## Source

Outside the KB, in `OES Project/oes-ui-kits/`: the Flutter gallery (Material 3 standard widgets,
fl_chart), one theme file per option, the screenshots, the source zip and the internal share page of
30 October. This page is that share page with the internal draft line, "The options" table and "How it
is built" (which carried KB IDs) removed, and the build and font notes moved into the intro. Each
option's description is in its screenshot's header; the exact sizes and seed colours are in this
README's table and the source README. Regenerate the screenshots there if a theme changes.

## Before it goes to the client

- **Differs from DEC-017's wording.** DEC-017 has Mikhail's kit plus two of Leu's; all three here are
  Leu's, A taking the "from the client's site" place. Tell Mikhail.
- **Arseniy's component library check** (DEC-017): the kits should use the libraries the developers
  accept.
- **Sample content is as built**: it shows some things not agreed or not estimated (sync status,
  "3 of 4 checks, next due 18:00", shift times, low stock and expiry, a drilling-progress bar, a third
  "Mixed" unit set). The page says the samples are illustrations, not agreed features; be ready to
  say it in S00 too ([[K-5 Scope grows through the prototypes]]).
- **Sent only through `procedures/export.md`**, by Anton. The client's choice is confirmed in writing
  ([[COM-018 Written minutes, notices and amendments]]).
