# Weekly review - the model half of lint

`tools/kb-lint.mjs` catches what a script can see. This catches what needs reading. Run it once a
week, or when the person asks. It reports; it changes nothing on its own.

1. Run `node tools/kb-lint.mjs` if Node is installed, and include its errors and warnings.
2. Meetings against the KB (Zeppla's period cross-check). For each agreement in the week's minutes:
   - recorded and unchanged: nothing to do
   - recorded but changed in the meeting: flag the difference, propose a supersede
   - not recorded at all: propose it as new
   The KB always lags the meetings; this is how it catches up.
3. Consistency:
   - contradictions between stable notes
   - Requirements that conflict with a Concern or a Commitment
   - words used in notes that are not a Term or an alias (terms drifting)
   - stable notes whose sources were superseded
4. Staleness: proposed notes older than two weeks, disputed notes, open Questions older than two
   weeks, a passed `valid_to`.
5. Completeness: Requirements with no error-case criterion, Concerns with no treatment,
   Commitments that drive no Requirement.
6. Scope: change request candidates still undecided. That list goes to the PMs.
7. Output:
   - `pm/<date> weekly review.md`: findings grouped as blocker, important, minor, each naming the
     note.
   - The fixes as a proposed-changes table (`procedures/ingest.md` step 6), for the person to
     approve.
   - One line in `log.md`: `<date> review - <n> findings - <person>`.
