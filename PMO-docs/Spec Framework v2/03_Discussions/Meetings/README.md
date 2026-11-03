# Meetings

**Purpose**: Landing zone for all meeting-related output -- processed notes, follow-up drafts, and raw transcripts.

---

## What Goes Here

Every meeting gets two files:

1. **`[YYYY-MM-DD]_[Brief-Description].md`** -- processed output from the `meeting-processor` skill: summary, decisions, open questions, spec impact, follow-up email draft
2. **`[YYYY-MM-DD]_[Brief-Description]_RAW.md`** -- the raw transcript or notes, pasted verbatim

Both files are always created together. The raw transcript is the source of truth; the processed file is the actionable output.

---

## How to Use

**If you have the transcript ready**, say:
> "We just had a call. Here's the transcript: [paste]. Run the meeting-processor skill."

Claude will process the transcript, create both files, and surface what needs to change in the spec.

**If you don't have the transcript yet**, say:
> "We had a meeting about [topic]."

Claude will create the RAW transcript file and ask you to paste the content into it before processing.

---

## What meeting-processor produces

1. Structured summary
2. Decisions made -> logged to `03_Discussions/Decision_Log.md`
3. Open questions raised -> logged to `03_Discussions/Open_Questions.md`
4. Spec impact -- what Platform Spec or Epic files need updating
5. Follow-up email draft for the client

---

## Note

This folder is Claude's working area. You don't need to organize or navigate it manually -- just tell Claude you had a meeting and it handles the rest.
