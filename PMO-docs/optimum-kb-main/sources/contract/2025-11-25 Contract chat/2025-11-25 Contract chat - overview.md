---
type: source
kind: chat
date: 2025-11-25
original: https://chat.google.com/room/AAQAXooObiI
received_from: Google Chat space "(Contract) Optimum Engineering Standards" (spaces/AAQAXooObiI), the contract negotiation chat; read by Anton Oparienko's copilot on 2026-09-28
purpose: how the contract and the SOW came to their final wording, what the client asked for and why, and which risks the team accepted when signing
supersedes:
procedure_version: b4cb7da
---
# 2025-11-25 Contract chat - overview

kind: chat, in three parts by period, rendered by `pm/seed-ingest-scripts/chat2md.mjs` from the Chat
tool's output (finding 46). 665 messages from 2025-11-25 09:50 to 2026-09-28 12:48 UTC. The chat is
still in use: the next ingest starts a part 4 after 2026-09-28 12:48.

| Part | First message | Last message | Rendered | Left out |
|---|---|---|---|---|
| [[2025-11-25 Contract chat - rendering 1]] | 2025-11-25 09:50 | 2026-04-14 12:31 | 274 | 1 empty |
| [[2025-11-25 Contract chat - rendering 2]] | 2026-05-06 08:08 | 2026-06-30 15:13 | 196 | 0 |
| [[2025-11-25 Contract chat - rendering 3]] | 2026-07-07 13:13 | 2026-09-28 12:48 | 194 | 0 |
| [[2025-11-25 Contract chat - rendering 4]] | 2026-09-28 12:52 | 2026-10-12 14:05 | 135 | 0 |
| [[2025-11-25 Contract chat - rendering 5]] | 2026-10-13 09:55 | 2026-10-14 12:47 | 8 | 0 |

Part 4 was added on 2026-10-13, read that day; see "Part 4" at the end. Part 5 was added on
2026-10-14, read that day; see "Part 5". The next part starts after 2026-10-14 12:47.

The breaks: the client's revised contract of 6 May 2026 (the rework), and the client's final comments
of 7 July 2026.

## What it is

The chat where Sales (Lizaveta Shauchenka, Polina Yanovskaya, Dana Kavalchuk, Anton Snotov), presale
(Aliaksei Tsitou, Marina Zaretskaya), Legal (Alex Petrushkevich), PMO's contract group (Andrey
Polovinkin, then Yauheni Krasner, Tanya Pinchuk), finance and later delivery management (Alexey
Gamanovich, Arseniy Klimenko, Michael Labutin, Lizaveta Loseva) negotiated the contract, from the first
drafts in November 2025 to the signed and legalised original in September 2026. It carries the client's
own letters, relayed in full: 23 December 2025, 5 January 2026, 6 May, 7 July, 12 August, 2 September
and 7 September 2026.

Attachments already stored: the v1 WBS and the WBS sent to the client, the presale architecture, the
proposal slides, the project description, the communication plan draft and the answers of 30 December
2025, the financial plan of 11 March 2026, the cybersecurity framework, the SOW v10.4, the final
contract. The contract drafts in between are listed in [[2026-09-07 Final contract - overview]]. Stored
with this batch as link-only overviews: [[2026-07-14 NCNICC-1 translation - overview]] and, from here and
the economy chat, [[2025-11-25 Resource plan - overview]] and [[2026-03-03 April hours plan - overview]].
The economy chat itself: [[2025-11-25 Economy chat - overview]]. The signed and apostilled scan
(2026-09-28) is not stored: signatures, stamps and ID data.

## How far to trust it

As `sources/contract/` says: what people said while negotiating, not the text. The contract binds; the
chat explains how its clauses came about and what the team knew when it accepted them. The client's
letters are relayed by Sales and are the client's own words. Internal summaries of the client's versions
(Lizaveta Shauchenka's of 2026-08-12, Yauheni Krasner's of 2026-08-13) are our reading of a contract
text; check the contract.

## Not for

Legal interpretation (ask a PM), or amounts, rates, margin and payment shares (removed; in Drive and the
P&L).

## Removed at ingest

- Money: every amount, rate, margin, discount and payment-share figure, in 23 messages, replaced in
  square brackets. The redaction map lives outside the repo, because it holds the figures.
- Credentials: two Zoom links with their passwords, a meeting ID and passcode.
- Personal data: one e-mail address in a message, one author shown by e-mail (rendered by name), user
  IDs in two Drive links.
- Left out: 1 empty message. Reactions, and blank lines inside messages.

## Summary

November 2025: Innowise's own frame agreement and a time-and-materials SOW with a budget cap and an
advance, checked by PMO and sent on 2 December. The client answered on 23 December: no costs beyond the
documents, warranty to six weeks, AWS credits explained, the communication plan, "retain only
'engineering calculations'" and a list of essential calculations "not limited to" it, the API included,
milestone payments every two months, Saudi law, and changes to payment terms. Innowise answered on 30
December with the answers document, the communication plan and three two-month phases in the SOW. On 5
January 2026 the client returned redlines (Saudi law, two-month invoicing, non-solicitation out) and
said the calculation samples were examples, the full set to be defined in discovery. The client
proceeded to signing on 9 January, then sent its own contract format with Arabic on 23 February.

March 2026: two-month invoicing clashed with time and materials and with Poland's KSeF invoicing;
monthly invoicing with a one-month payment delay was agreed with the client on 5 March; the SOW was
split into six monthly phases; the financial plan went out on 11 March. A legal meeting with the
client's lawyers was held on 9 April.

May to June 2026: the client's revised contract of 6 May, and a new PMO review: the contract "НЕЛЬЗЯ
подписывать в том виде", "похоже на Lotus". PMO rewrote the SOW with protections for time and materials
(15 May); the client would not accept it; on 22 May the team switched to fixed price with milestones on
the client's contract, moved from MAUI to Flutter, and judged the WBS enough as the requirements, with
everything outside the WBS a change request. The contract and the SOW v10.4, in English and Arabic, went
to the client on 15 June.

July to September 2026: the client's final comments of 7 July (the advance, full Saudi compliance, three
business days to respond, termination paid for completed work with an independent expert, no travel,
confirmation of complete information). The team settled the compliance baseline (NCNICC-1:2025 and the
PDPL, category B, hosting on GCP in the Kingdom) and answered on 14 July. The client's final PDF of 12
August was much stricter and PMO advised not to sign; Innowise countered on 25 August; on 2 September the
client declined to reopen anything and clarified the warranty. On 4 to 7 September management decided
to sign the contract as it stands and listed the risks accepted. Innowise signed; the original was
legalised and apostilled by 28 September, for the client's CEO to collect in the Warsaw office on 29
September. The client signs after that.

## Proposed changes

The batch 6 table. Source keys: K1, K2, K3 = [[2025-11-25 Contract chat - rendering 1]], rendering 2,
rendering 3, with the date and UTC time of the message; E = [[2025-11-25 Economy chat - overview]].

The contract clauses themselves are already in the Commitments from batch 3. These rows add how each
clause came about and, where the team said so on 2026-09-07, that it was accepted as a known risk. The
disputed Commitments stay disputed: the chat shows the negotiation, and the settling is Anton's.

Approved by Anton on 2026-09-28: all rows; DEC-007's decider is Arseniy Klimenko
(human:arseniy.klimenko), so it is proposed; DEC-008 and DEC-009 are draft, with no deciders named, "we
will try to follow the procedure anyway".

| # | Change | Note | What | Origin | Scope | Source | Result |
|---|---|---|---|---|---|---|---|
| 1 | update | QUE-006 Which SOW and which plan are Annex 1 and Annex 2 | Cite the chat for Annex 1: asked by Anton Oparienko for the exact texts, Yauheni Krasner: "это должен быть по идее финальный SOW: UPD SOW Optimum 15.05 (v10.4)", and "фрейма в ворде - не было. Он только в пдф, т.к. это шаблон клиента". The SOW v10.4 went out with the contract on 15 June; the client's final of 12 August was "только контракт". Annex 2: candidates are the SOW's milestone and payment table ("добавил таблицу с майлстоунами и расписанием оплат", 12 June) and the financial plan of 11 March; still open | extracted | - | K3 2026-09-28 09:26, 09:37, 08-12 14:54; K2 06-12 10:11, 06-15 13:24 | applied 2026-09-28 |
| 2 | update | QUE-007 What is the Effective Date | Signing status: Innowise signs first on letterhead, attests at the Chamber of Commerce and legalises at Poland's Ministry of Foreign Affairs; the apostilled original was ready on 28 September, for the client's CEO in the Warsaw office on 29 September; then the client signs and attests. The client's date is still ahead | extracted | - | K3 09-07 08:46, 09-17 12:49, 09-28 08:20 to 12:48 | applied 2026-09-28 |
| 3 | update | COM-015 Saudi cybersecurity and regulatory compliance | How the wording came about: the client's demand to "fully comply with all applicable Saudi cybersecurity regulations" (7 July); inside, "полностью соблюдаем все применимые требования" (Lizaveta) against "мы \"все\" регуляции поддержать не можем ... уж точно не в тот бюджет" (Gamanovich); our letter of 14 July offered NCNICC-1:2025 and the PDPL, with hosting region and data residency outside the SOW; the client's final widened it to all controls, frameworks and directives plus hosting, data residency and cross-border transfers; accepted as a known risk on 7 September. Stays disputed | extracted | - | K3 07-07 13:13, 07-10 15:50, 18:20, 07-14 15:18, 08-13 09:26, 09-07 10:32 | applied 2026-09-28 |
| 4 | update | CON-007 Saudi cybersecurity and data protection rules | The team's reading of the framework: ECC-2:2024 is for government and critical infrastructure, not this client; NCNICC-1:2025 and the PDPL are the baseline; the PDPL needs GCP in the Kingdom; organisational controls (2-1-1, 2-13) sit with the client, Innowise can help; discovery to do a gap analysis; data leaving the region would need a privacy notice and consent logs. The NCNICC-1 translation is stored link-only | extracted | - | K3 07-10 18:06, 07-13 15:50, 07-14 08:46 to 16:43 | applied 2026-09-28 |
| 5 | update | QUE-005 Is the client an NCA Category A or B entity | Our reading: "= category B" (Gamanovich, 14 July 2026), from the category table and "вроде бы у них до 100 сотрудников" (Uladzislau Murashka). For Category B penetration testing is recommended, not required. Not confirmed by the client: open until the client confirms or Anton accepts our reading | evaluated | blocks Total Estimation Development Flutter!25 (unchanged) | K3 07-14 11:42 to 12:05 | applied 2026-09-28 |
| 6 | update | CON-002 Deployment outside public cloud | Hosting, 2026: to the client on 5 January, all AWS environments "owned and managed by Innowise via the Innowise AWS account" until three months after go-live, then handed over; July: AWS in the region "в зоне риска ... часть сервисов недоступно", and the rules do not allow leaving MENA; GCP in Dammam has the services and monthly billing works; "нужно идти с GCP, клиент делает аккаунт (нужно чтобы аккаунт сделал кто-то именнто из KSA)" | extracted | - | K1 2026-01-05 12:47; K3 07-10 18:06, 07-13 15:50, 07-14 09:12 to 12:05 | applied 2026-09-28 |
| 7 | update | COM-004 Twelve-month warranty | How it came in: in the client's final PDF of August; our offer of a paid SLA instead (25 August) was declined; the client's clarification of 2 September: the warranty "relates specifically to the quality of the work delivered", a defect attributable to Innowise is fixed at no cost, "fundamentally different from post-delivery support or further development", new functionality through change requests, an SLA "if and when"; accepted as a known risk on 7 September | extracted | - | K3 08-12 13:28, 08-25 07:27, 09-02 15:55, 09-07 10:32 | applied 2026-09-28 |
| 8 | update | COM-002 Written acceptance of each deliverable | How it came about: our frame had deemed acceptance after 14 days; the client's final removed it ("молчание, тестирование или использование системы не являются приемкой"; the 14 days restart after a fix); our request to keep it was declined; accepted on 7 September: "отсутствие automatic acceptance" | extracted | - | K3 08-12 13:28, 08-25 07:27, 09-02 15:55, 09-07 10:32 | applied 2026-09-28 |
| 9 | update | COM-003 Quality and defect correction at no charge | Accepted on 7 September: fixing "в том числе Minor/Trivial дефектов" within acceptance; "для приемки, мы должны пофиксить все баги. Теперь это не ограничено только Blocker, Critical и Major" (Yauheni). PMO in May: "Слишком широкая обязанность бесплатно исправлять дефекты" | extracted | - | K2 05-06 14:53; K3 09-03 13:03, 09-07 10:32 | applied 2026-09-28 |
| 10 | update | COM-016 Termination and settlement | How it came about: a refund of a share of the price added to section 2 in June; the client asked for payment of completed work only, with an independent expert (7 July); agreed with a mutually chosen expert and a separate agreement for the procedure (9 to 14 July); the client's final: termination for convenience on 10 business days for the client, only an undisputed payment default after 20 business days for Innowise, only completed, delivered and usable work paid; accepted on 7 September. Stays disputed | extracted | - | K2 06-11 09:47; K3 07-07 13:13, 07-09 09:20, 07-14 15:18, 08-13 09:26, 09-07 10:32 | applied 2026-09-28 |
| 11 | update | COM-006 Information sufficient for scope and price | How it came about: the client's "Confirmation of Complete Information" (7 July); our wording keeping the right to ask for more (14 July); the client's final: Innowise confirms it had all information and the discovery it needed, and clarifications alone give no more time or money; accepted on 7 September | extracted | - | K3 07-07 13:13, 07-08 07:31, 07-14 15:18, 08-13 09:26, 09-07 10:32 | applied 2026-09-28 |
| 12 | update | COM-005 Change requests | How it came about: our internal rule of 22 May, "Все, что не в WBS — оформлять как Change Request"; the client's final: clarifications, functions "implicit in the SOW" and work needed for the project's goals are not change requests; our objection declined; the client, 2 September: "Any new functionality, enhancement, or development requested by the Customer outside the agreed scope may properly be handled through the Change Request mechanism" | extracted | - | K2 05-07 17:33, 05-22 13:07; K3 08-13 09:26, 08-25 07:27, 09-02 15:55 | applied 2026-09-28 |
| 13 | update | COM-001 Delivery within six months | History: a start planned "в первую неделю января" (December 2025), then "если контракт считать с апреля" (March 2026); the client's final: "строго 6 месяцев, продление возможно исключительно по подписанному Заказчиком Change Request", clarifying questions give no right to move dates (2.5); our request that client delays extend the term was declined. Stays disputed | extracted | - | K1 2025-12-24 10:23, 2026-03-03 14:52; K3 08-12 13:28, 08-13 09:26, 08-25 07:27 | applied 2026-09-28 |
| 14 | update | COM-007 Client answers clarifications within three business days | History: 24 hours in the earlier text; the client asked for three business days (7 July); agreed, with a request that work may pause while we wait (14 July); the final: a late answer does not extend the project, and only a task that objectively cannot continue may pause | extracted | - | K3 07-07 13:13, 07-14 15:18, 08-13 09:26 | applied 2026-09-28 |
| 15 | update | COM-009 Remote delivery, no travel | History: the client asked to remove all travel, since all information had been given (7 July); our revision: no travel needed, exceptional travel only by separate written agreement (14 July) | extracted | - | K3 07-07 13:13, 07-14 15:18 | applied 2026-09-28 |
| 16 | update | COM-012 Payment schedule | History, without figures: time and materials with a budget cap and an advance (November 2025); three milestone payments every two months asked (December); monthly invoicing with a one-month payment delay agreed on 5 March 2026 (Poland's KSeF); fixed price with milestones (22 May); the advance refused without a bank guarantee (7 July) and our counter (14 July); the client's final: a smaller advance and fixed monthly payments "строго при условии 100% выполнения запланированного объема (фактически отработанные часы больше не учитываются)". Stays disputed | extracted | - | K1 2025-11-28 19:49, 12-23 08:36, 2026-03-04 12:21, 03-05 12:10; K2 05-22 13:07; K3 07-07 13:13, 07-14 15:18, 08-12 13:28 | applied 2026-09-28 |
| 17 | update | COM-017 Liability, indemnity and force majeure | History: our frame capped liability at amounts received; the client's final: a cap not below the total contract value, and no cap for IP, confidentiality and data-security breaches; our objection declined | extracted | - | K3 08-12 13:28, 08-13 09:26, 08-25 07:27 | applied 2026-09-28 |
| 18 | update | COM-019 Non-solicitation | History: the client asked to remove section 8 or 8.2 (5 January 2026); Legal: "из Саудовской Аравии сложно хантить"; it stayed | extracted | - | K1 2026-01-05 10:59, 15:27 | applied 2026-09-28 |
| 19 | update | COM-013 Source code, IP and third-party components | History: the client's May version "may not use any open-source code (пункт 8.3)" (Gamanovich's list); the final 8.4 limits components with copyleft and similar obligations. Drives: DEC-007 | extracted | - | K2 05-07 17:33 | applied 2026-09-28 |
| 20 | update | CON-003 Correct calculations | The client on scope: remove "quick" and "standard", "retain only 'engineering calculations'", list the essential calculations "included but not limited to the listed items" (23 December 2025); the samples "were provided as examples ... the full set of calculations and modeling activities is intended to be defined, detailed, and completed during the discovery stage" (5 January 2026). The BA estimate for the maths: "дифицит в 10%" (May 2026) | extracted | - | K1 2025-12-23 08:36, 2026-01-05 10:59; K2 05-18 16:14 | applied 2026-09-28 |
| 21 | update | REQ-007 Derived values and standard calculations | The same two client statements: examples now, the full set in discovery, "not limited to" | extracted | contracted (unchanged) | K1 2025-12-23 08:36, 2026-01-05 10:59 | applied 2026-09-28 |
| 22 | update | REQ-019 API for other systems | The client's ask of 23 December 2025: "We would like the API to be included. Kindly confirm feasibility." (our answer is already in the note) | extracted | out-of-scope (unchanged) | K1 2025-12-23 08:36 | applied 2026-09-28 |
| 23 | update | DEC-007 Flutter for the desktop app | The decision in the chats: MAUI's risk, one developer with the expertise, since moved to mobile, "+20%" advised (E, 15 May) and "bus factor" (20 May); the call of 22 May: "Переходим с MAUI на Flutter (или другую кроссплатформу), чтобы снизить риски и упростить подбор команды. Проверяем, подходит ли Flutter"; Arseniy, 25 May: "по флатеру даю апрув", about 100 hours fewer, and the web front end in Flutter "как опция". Name the decider (human:arseniy.klimenko), valid_from 2026-05-25, status proposed | extracted | - | K2 05-20 15:51, 05-22 13:07, 05-25 13:53; E | applied 2026-09-28 |
| 24 | update | DEC-004 Backend stack | The May 2026 scope named .NET for the back end: "В скоупе есть React, .NET и MAUI" (Arseniy, economy chat) | extracted | - | E | applied 2026-09-28 |
| 25 | new | DEC-008 Fixed price with milestones, on the client's contract | 22 May 2026: "Формат - fixed price с milestone-ами. Используем текущую версию контракта клиента, дорабатываем ее под свои условия." Options: time and materials with a budget cap (November 2025 to May 2026; PMO's reading on 12 May), lost because "клиент не примет такой договоренности"; fixed price, chosen. Consequences: the WBS taken as the requirements, everything outside it a change request; scope, budget and time fixed before discovery. Deciders not named; draft | extracted | - | K2 05-12 07:44, 05-20 15:27 to 15:51, 05-21 11:27, 05-22 13:07 | applied 2026-09-28 |
| 26 | new | DEC-009 Sign the client's final contract as it stands | 4 to 7 September 2026: "сегодня было принято решение со стороны менеджмента подписываться и стартовать проект". Options: keep negotiating (the client declined on 2 September), walk away (Gamanovich's view on 20 August), sign as is, chosen. The risks accepted, as listed; obligations: watch the P&L, reinforced delivery control, a phased team with strong people first, no development until the scope is understood, keep every agreement and artefact, escalate with the same group. Deciders not named by id; draft | extracted | - | K3 08-20 09:19, 09-02 15:55, 09-03 09:12, 09-04 10:06, 09-07 10:32 | applied 2026-09-28 |
| 27 | update | DEC-001 Delivery quality over margin | Context, without figures: the presale margin was already "ниже допустимой нормы"; management conceded on rates "с учетом необходимости развития домена нефтянки и расширения нас в регионе"; "Для подписания скидку и давали" | extracted | - | K1 2025-12-03 10:06; E | applied 2026-09-28 |
| 28 | update | DEC-002 Senior engineers first | 7 September: "Команду планируем подключать постепенно. На старте нужны сильные специалисты для проработки архитектуры/логики и особенно расчетных формул; после стабилизации требований можно оптимизировать состав и стоимость команды." | extracted | - | K3 09-07 10:32 | applied 2026-09-28 |
| 29 | update | DEC-003 Handling small change requests | 22 May: "Все, что не в WBS — оформлять как Change Request"; the final contract narrows what counts as one (COM-005) | extracted | - | K2 05-22 13:07 | applied 2026-09-28 |
| 30 | no material | Roles and staffing | The DM and PM changes and PMO staff changes: the A02 register | - | - | K2 05-06; K3 09-07 10:32 | recorded 2026-09-28, no note |
| 31 | no material | PMO's contract risk reviews | May and August 2026 ("похоже на Lotus"): the PMO risk register, linked from DEC-009 when filed | - | - | K2 05-06 14:53, 05-07; K3 08-13 09:26 | recorded 2026-09-28, no note |
| 32 | no material | Governing law and language | Saudi law, arbitration in Riyadh, the Arabic text prevails: in the contract and its overview | - | - | K3 08-12 13:28 | recorded 2026-09-28, no note |
| 33 | no material | The economics | Rates, margin, the P&L: held back; the non-money facts are in DEC-001 and the economy overview | - | - | E | recorded 2026-09-28, no note |
| 34 | no material | Translating the contract | The translation bureaus and the internal translator: process | - | - | K2 05-26 to 06-14 | recorded 2026-09-28, no note |
| 35 | no material | AWS credits wording | The December 2025 explanation to the client, overtaken by the move to GCP; kept in the source | - | - | K1 2025-12-24 11:44 | recorded 2026-09-28, no note |

## Part 4 (added 2026-10-13)

[[2025-11-25 Contract chat - rendering 4]]: 135 messages, 2026-09-28 12:52 to 2026-10-12 14:05 UTC,
rendered by `pm/seed-ingest-scripts/chat2md.mjs` (procedure 5d00575). Two thread starters from earlier
parts were put in the script's input so replies point at the right message; they are not rendered.

Removed at ingest: a rate figure in Mikhail's message of 2026-09-29 15:51; a phone number and a postal
address (2026-10-12 13:56, 14:05); company e-mail addresses (2026-10-09 11:03, 11:08); a remark about a
colleague's employment status (2026-10-12 12:53). Left out: nothing (no bot, system or empty messages).
The rendering script dropped a trailing question mark from every message that ended with one (a link-cleanup step trimmed the last character of the whole text); in this part the 26 marks were put back before storing, checked against the Chat tool's output, and the script was fixed on 2026-10-13. Parts 1 to 3 were rendered with the old script and carry the same defect.
Not stored: the signed and stamped Agreement posted on 2026-10-12 10:01 (signatures, stamps); the SOW
versions of 11 March and 15 June 2026 named in the thread; the client-stakeholder table image of
2026-09-29 07:12.

Summary. The client's CEO collected the original in Warsaw on 29 September; the team asked Kavalchuk to
raise a single point of contact, a product owner and access with him. Only the frame is signed, no
annex. Mikhail set the staffing principle: least loss from idle time, seniors who work with Claude,
fewer developers, a BA who prototypes. The SOW was brought in line with the frame and reviewed by PMO
and Legal by 5 October; the changed Arabic text was translated in-house by 9 October. On 12 October
Lizaveta posted the Agreement signed by both sides, dated 7 October by Kavalchuk, and the thread turned
to how to start: a strong BA first, a plan for the client, the Annex 2 wording, the advance still
unpaid. Anton took on the setup and the BA search.

Proposed changes for part 4 are in the table of [[2026-10-13 Optimum Three Caballeros call - minutes]],
which covers this part and the calls of 12 and 13 October.

## Part 5 (added 2026-10-14)

[[2025-11-25 Contract chat - rendering 5]]: 8 messages, 2026-10-13 09:55 to 2026-10-14 12:47 UTC,
rendered by `pm/seed-ingest-scripts/chat2md.mjs` (procedure 5d00575), which since this part can number
a later part on its own. The Chat tool's output also held the last message of part 4 (2026-10-12
14:05); it is not rendered again.

Removed at ingest: nothing beyond reactions. Left out: nothing (no bot, system or empty messages).

Summary. Kavalchuk posted the agreed record of the call of 13 October - send the SOW as it stands and
ask the client for a responsible person, a hybrid discovery with target results, a BA working with
Claude Design, regular re-estimation of budget, scope, quality and client expectations, three risks
with their mitigations - after Mikhail's corrections in the four-person chat
([[2026-10-13 OE Big4 chat - rendering 1]] 09:06 to 09:45). The letter asking for a contact went the
same day. Mikhail asked Anton to open the BA position, with the requirements. On 14 October the client
named a contact; Kavalchuk introduced Anton by e-mail and asked for a slot the following week. The
start now depends on our readiness and the SOW, which is still unsigned.

Proposed changes for part 5 are in the table of [[2026-10-13 OE Big4 chat - overview]], which covers
this part, the OE Big4 chat, the [Core] chat and the e-mail of 14 October.
