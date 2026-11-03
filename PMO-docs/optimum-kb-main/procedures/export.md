# Export - a document for the client, Sales or leadership

The only way anything leaves. The person sends it; the agent never does.

1. Ask what is needed, for whom, and how technical the reader is.
2. Build from stable notes. A proposed note appears only if the person says so, and then only as
   "to be confirmed". Open Questions appear as open, never as agreed.
3. Strip everything internal:
   - IDs (REQ-, DEC-, QUE- and the rest) and wikilinks (lint checks both)
   - team members' names, unless the person asks for them
   - status lines ("8 of 10 done" goes stale the day after)
   - the KB itself - never mention it
   - images and PDFs stored with sources: internal reference only (`procedures/ingest.md` step 2)
   - the client's figures from a `money: client-domain` rendering: its confidential data, even when
     the export goes back to the client
   Refer to meetings by date: "as discussed on 6 October".
4. Keep three things apart: confirmed, proposed, open.
5. Write it to `pm/exports/<date> <what>.md` from `templates/Template - Export.md`. The frontmatter
   keeps, for us, which notes it was built from (`built_from`) and the procedure version; the body
   is what gets sent.
6. If the text goes out under a person's name and they have a voice skill, run it through that.
7. One line in `log.md`: `<date> export <what> for <audience> - <person>`.
