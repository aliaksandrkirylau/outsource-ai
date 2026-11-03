# Editing a Google Slides deck through the connector - what actually goes wrong

Every item here cost a rebuild or a silent wrong result on a real deck. Read before touching a
presentation, not after.

## Before you edit anything

**Ask whether a template copy already exists.** The most expensive mistake is building a parallel
deck when the PM already has their own copy of the PMO template - branded, named for the project,
with placeholder text waiting to be filled. Filling that copy IS the job. A freshly generated deck,
however good, gets thrown away.

**Read the rendered content before editing.** The connector's `get_presentation` and `get_page`
summarise tables and grouped graphics but do NOT dump their cell text. A deck adapted from another
project will be full of carryover you cannot see that way - the old client's name, their vendor,
their feature names. Open the deck in a browser and look at each slide, or you will ship someone
else's project name to a client.

## The traps

**Tables and groups report as type Unknown, with no child object IDs.** A table inside a group is
not cell-addressable at all - `insertText` with a cellLocation errors with "object is not a table",
and there is no way to get the nested table's id through the connector.

Workaround that works: `deleteObject` the group, then `createTable` a fresh one and re-style it.
Verify by screenshot which Unknown object is the table before deleting - delete one, re-screenshot,
and Ctrl+Z if wrong. A created table does NOT inherit the old look, so you must restore:
- column widths via `updateTableColumnProperties`, needing `columnWidth` in EMU
- header fill via `updateTableCellProperties` with a tableRange rowSpan and columnSpan
- bold via `updateTextStyle`

**Object IDs you create must be at least 5 characters.** `dot0` and `bMob` are rejected; `mdot0`
and `barMob` work.

**Deleting and re-inserting text collapses run styling to the box default.** After replacing text,
re-apply font size, bold and colour explicitly. Template boxes often auto-bullet every paragraph,
so `deleteParagraphBullets` on header lines you do not want bulleted, and re-`createParagraphBullets`
on the ones you do.

**Do not surgically insert a line into a list by character index.** Off-by-one merges lines. For a
whole list, rewrite the box clean and re-bullet.

**`replaceAllText` with zero matches does NOT error.** A silent no-op looks exactly like success.
Two defences: scope replacements with `pageObjectIds` per slide so duplicated text on two slides
cannot collide, and match on anchors without apostrophes or ampersands so a curly-quote mismatch
cannot cause a silent miss. Then verify visually.

**Longer replacement text overflows a fixed text box** and overlaps whatever is below it. After a
copy edit, check the length against the equivalent box on sibling slides.

**Build a timeline or roadmap from SHAPES, not an embedded image.** Rectangles, ellipses and text
boxes with explicit EMU transforms. Image embedding through the connector is unreliable, and shapes
stay editable by the PM afterwards. Canvas is 10 x 5.625 inches = 9144000 x 5143500 EMU, at
914400 EMU per inch.

**Generate large batch requests with a script.** Computing indices and EMU positions by hand across
a dozen slides invites arithmetic errors; build the JSON programmatically and pass it to
`batch_update_presentation`.

## Verifying

Screenshot every slide you changed. `get_page_thumbnail` returns a URL whose image egress is blocked,
so a browser is the reliable eyeball. Given that `replaceAllText` fails silently, verification is not
optional politeness - it is the only thing standing between a silent no-op and a client seeing a
half-edited deck.

## Numbers must foot

If the deck contains hour splits, budget lines or team allocations, check that they add up to their
own headers after editing. On a real adapted deck the per-role hour rows summed to 50 while the
header said 40 - because the header was edited and the table was not. Nobody caught it until the
slide was read aloud.

## Adding the finished deck to NotebookLM

Native Google Slides and Docs add cleanly as Drive sources. Office files and Sheets pushed through
the connector do not sync reliably. Combine many small documents into one source rather than adding
a dozen - source limits are real. Hold out anything money-bearing, contract text, and candidate CVs.
