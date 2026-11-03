---
name: pm-voice
description: Draft or fix any text a PM will SEND so it reads as a working PM typed it, not as AI - a client email or chat reply, a PROREP weekly comment, a kick-off invite or follow-up, an escalation, a note to leadership, a post to the PM group. English and Russian. Fires on the OUTPUT, not the request - "reply to the client", "answer Roman", "post the status", "write the follow-up" all count, and so do "make this less AI", "humanize this", "this is too formal", "shorten this", and the same asks in Russian. Other copilot skills hand their outbound text here when the PM has no personal voice skill of their own. If the PM has one, that one wins and this skill steps aside. Sets the length by channel first, then removes English and Russian AI tells against how Innowise channels actually read. Not for documents nobody sends, code, or other people's writing.
---

# pm-voice - text a PM sends, sounding like a PM sent it

A copilot draft almost never fails on vocabulary. It fails on length. A chat reply comes out at 150
words where a PM would type 20, a weekly status comes out three times the size of the ones around it
in the channel, and no list of banned phrases catches that. So this skill decides the length FIRST,
before a word is written, and only then goes looking for tells.

The second failure is polish. Innowise channels are mostly one-liners, typed between calls, with
typos nobody fixes. A perfectly parallel, typo-free, fully hedged post reads as generated in that
setting even when every individual rule was followed.

## Who wins

Check in this order and stop at the first that exists.

1. **The PM's own voice skill.** The voice line in `pm-profile.md` names it if there is one. Hand the
   text to it and step aside - a voice built from the PM's own writing beats anything here.
2. **The PM's saved writing samples.** `copilot-setup` offers to save a few real messages as
   `voice-samples.md` next to `pm-copilot-setup.md`, and the voice line in `pm-profile.md` says where.
   Read them. Their greeting, their sign-off, their language mix and their typical length beat the
   defaults below wherever the two disagree.
3. **This skill's defaults**, below and in `references/`.

A PM saying "that is not how I write" is the most useful thing that can happen here. Change the
draft, and offer to add the correction to their samples or their `pm-profile.md` so it sticks.

## The pass, in order

1. **Name the channel and the audience.** Client chat, client email, team chat, a DM, a post to the
   PM group, a status to leadership. Then take the budget for it from
   `references/length-and-channels.md`. Decide the size before drafting.
2. **Draft to the budget, or cut to it.** The cutting rules are in the same file. The short version:
   drop the opening scene-setting sentence, drop the closing recap or offer, and cut ceremony but
   never specifics.
3. **Scan for tells** in the language of the text - `references/anti-tells-en.md` or
   `references/anti-tells-ru.md`. Mixed Russian with English terms is normal and is not a tell.
4. **Check it against the channel.** Would this post look out of place next to the last five
   messages in the same space? If it is longer, more formal, more structured or cleaner than all of
   them, it will read as generated.
5. **Deliver the text only.** Ready to paste. No "here is a draft", no list of what you changed. If it
   is over the channel's ceiling, one line saying why it had to be.

## When a calling skill owns the structure

`prorep-card`, `a12-a14-kickoff` and others hand text here with a required shape - a PROREP field
set, a kick-off follow-up's content list, a template section. That shape is fixed. The voice applies
INSIDE it: shorter sentences in each field, no recap in the last one, labels as plain text. Never
drop a required field to hit a budget; shorten what is in it.

## Rules that hold everywhere

- Specifics stay. Names, ticket IDs, dates, versions and numbers are what make a message useful, and
  they are the first thing a "tightening" pass wrongly removes.
- Never correct typos or non-native slips in text the PM pasted, unless asked. A dropped article is
  a human signal, not an error to fix. Never introduce fake typos either.
- Do not normalise contractions one way. "We're" and "we are" side by side is normal.
- No em dashes. " - ", commas or parentheses.
- Text to a colleague about their work is written in first person - "I would nudge these, here is my
  version" - never as a verdict on theirs, positive or negative.
- If the PM does not know the house convention for something, the draft says so rather than
  inventing one: "not sure what we usually do here, this is my draft".

## When the house register does not apply

Formal letters to government bodies, HR documents, contract correspondence, and clients in
conservative industries who write formally themselves. There, use a neutral formal register. The
length budget still applies; the channel habits do not.
