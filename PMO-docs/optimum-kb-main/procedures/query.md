# Query - answering a question about the project

Read-only. Filing an answer back into the KB is a separate step, only on the person's yes.

1. Start from `index.md`, then the notes it points to. Search `knowledge/` and `sources/`. Read a
   role folder (`pm/ ba/ tl/ qa/`) only if the person asks or nothing else answers, and say that
   the answer comes from working material.
2. Answer with citations: the note, and for a fact, the source with its timestamp or section.
3. Phrase by status:
   - stable: state it.
   - draft or proposed: "proposed, not confirmed yet", and by whom it waits.
   - disputed: both versions, who holds each, and that it is undecided.
   - deprecated: what replaced it, and since when (`valid_from` of the new note).
4. Exact wording (a contract clause, a client quote): quote the source, not the note. The notes
   serve synthesis; the sources serve verbatim lookups.
5. Say what the KB does not know. Do not fill a gap from general knowledge as if it were a project
   fact, and never use another project's facts for this one.
6. Status questions (who is on what, sprint progress, hours): point to Jira and the P&L. The KB
   does not hold them.
7. If the answer is a new synthesis worth keeping, offer to file it. If the person agrees, it goes
   through `procedures/ingest.md` step 6 as a proposed change, like anything else.
