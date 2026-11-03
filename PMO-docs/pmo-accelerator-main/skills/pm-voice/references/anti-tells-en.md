# English anti-tells

Scan an English draft against this list AFTER the length is right. Most of these patterns are
downstream of two things: uniform sentence rhythm, and safe high-frequency words. Fixing length and
varying sentence size removes a surprising share of them before the list is even read.

The catalogue is adapted from Wikipedia's "Signs of AI writing" and the humanizer skill (sources at
the end), with the examples rewritten for PM work.

## Length and polish - check these first

| Tell | Why it reads as AI | Instead |
|---|---|---|
| Length itself | A 150-word chat reply is a tell before a word of it is read | The channel budget in `length-and-channels.md` |
| Opening that restates the question | Adds nothing; the reader asked it | Answer in the first sentence |
| Closing recap of what was just said | The reader has just read it | End on the next action, or just end |
| Objectless offer - "Let me know if you'd like me to adjust anything" | Chatbot reflex | Drop it, or give it an object: "Let me know if the OTP error comes back" |
| "Looking forward to your response", "Please don't hesitate", "Kindly note", "We are pleased to inform you" | Boilerplate nobody types in a working thread | Close on substance |
| A clean promise, then a paragraph of caveats | Reads composed | Put the condition inside the sentence |
| Every contraction the same way | Humans mix "we're" and "we are" | Leave the mix |
| Corrected non-native English in pasted text | Removes the strongest human signal there is | Leave dropped articles and agreement slips alone |
| Perfectly even paragraphs | Low burstiness, the core statistical tell | One long sentence, then a short one |

## Content patterns

| # | Pattern | Tell | Instead |
|---|---|---|---|
| 1 | Significance inflation | "This marks a pivotal milestone in our partnership" | "Release 1.4 is live" |
| 2 | Name-dropping for weight | "aligned with industry best practices from leading firms" | Name the practice, or drop it |
| 3 | Empty "-ing" analysis | "...reflecting our commitment, showcasing the team's dedication" | Delete the clause |
| 4 | Promotional language | "a robust, seamless, cutting-edge solution" | Say what it does |
| 5 | Vague attribution | "Stakeholders feel that...", "It is widely believed..." | Who, specifically |
| 6 | Formulaic challenge arc | "Despite challenges, the team continues to deliver" | The specific problem and what was done |

## Language patterns

| # | Pattern | Tell | Instead |
|---|---|---|---|
| 7 | AI vocabulary | "additionally, crucial, delve, landscape, leverage, testament, pivotal, foster" | Plain words |
| 8 | Copula avoidance | "serves as", "functions as", "boasts" | "is", "has" |
| 9 | Negative parallelism | "It's not just a delay, it's a signal" | State the point |
| 10 | Rule of three | "clarity, alignment, and momentum" | However many items there really are |
| 11 | Synonym cycling | "the client... the customer... the stakeholder... the partner" for one person | Repeat the clearest word |
| 12 | False range | "from discovery to deployment" | List what is actually covered |
| 13 | Subjectless fragments | "No action needed." | Say who does or does not need to act, when it matters |

## Style patterns

| # | Pattern | Tell | Instead |
|---|---|---|---|
| 14 | Em dashes | the long dash, especially around an aside | " - " (hyphen with spaces), commas, or a new sentence |
| 15 | Boldface scattered through prose | "**scope**, **timeline**, **budget**" | Plain text |
| 16 | Inline-header bullets | "**Timeline:** The timeline is on track" | Prose, or a plain `Timeline:` label with no bold. The bold is the tell, not the colon |
| 17 | Title Case Headings | "Next Steps And Open Questions" | Sentence case, and in chat no headings at all |
| 18 | Decorative emoji | a rocket before "Launch plan" | Remove, unless the channel uses them |
| 19 | Curly quotes | typographic quotes | Straight quotes |
| 20 | Hyphenated pairs everywhere | "cross-functional, data-driven, client-facing" | Fewer of them |
| 21 | Authority tropes | "At its core...", "The reality is..." | State the point |
| 22 | Signposting | "Let's dive in", "Here's what you need to know" | Start with the content |
| 23 | Heading over a one-line section | "## Risks" then "Two risks." | Drop the heading |

## Communication patterns

| # | Pattern | Tell | Instead |
|---|---|---|---|
| 24 | Chatbot artifacts | "I hope this helps!", "Great question!" | Remove |
| 25 | Sycophancy | "You're absolutely right" | Respond to the content |
| 26 | Knowledge disclaimers | "Based on the information available..." | Find out, or say plainly what is not known |
| 27 | Filler | "in order to", "due to the fact that", "at this point in time" | "to", "because", "now" |
| 28 | Stacked hedges | "could potentially possibly" | One hedge |
| 29 | Generic close | "Exciting times ahead!" | The next concrete step, or nothing |

## The two underlying signals

- **Burstiness** - variation in sentence length. Human writing varies a lot; generated text clusters
  around one length. Varying length on purpose fixes many surface tells at once.
- **Perplexity** - how predictable each word is. Generated text picks the safest word every time.
  The specific word - the ticket number, the client's own term, the house jargon - raises it.

## Sources

- Wikipedia: Signs of AI writing - https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- blader/humanizer SKILL.md v2.5.1 - https://github.com/blader/humanizer
- GPTZero on perplexity and burstiness - https://gptzero.me/news/perplexity-and-burstiness-what-is-it/
