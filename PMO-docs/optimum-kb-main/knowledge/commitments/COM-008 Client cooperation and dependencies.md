---
type: commitment
id: COM-008
status: disputed
origin: extracted
author: claude-code/claude-opus-5-5
party: client
due: not stated; compliance requirements "before the project start" (SOW)
clause: "5.1; 2.5, 2.6, 4.5, 11.3; SOW v10.4 assumptions, row 13"
sources:
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-06-15 SOW v10.4 - rendering]]"
  - "[[2026-09-28 Optimum discuss next steps - transcript]]"
  - "[[2025-11-25 Contract chat - rendering 2]]"
  - "[[2026-10-01 Optimum Three Caballeros call - transcript]]"
  - "[[2025-11-25 Contract chat - rendering 4]]"
  - "[[2026-10-13 Optimum Three Caballeros call - transcript]]"
  - "[[2025-11-25 Contract chat - rendering 5]]"
  - "[[2026-10-13 OE Big4 chat - rendering 1]]"
  - "[[2026-10-14 Project email thread - rendering 1]]"
  - "[[2026-10-20 Introductory call - transcript]]"
tags:
  - client-dependency
---
# COM-008 Client cooperation and dependencies

## What is owed

The contract: "The First Party shall provide the cooperation expressly required by the SOW, nominate
authorized contacts, and pay undisputed amounts that become due in accordance with Article 7."
([[2026-09-07 Final contract - rendering]] 5.1)

What the SOW v10.4 requires of the client ([[2026-06-15 SOW v10.4 - rendering]], assumptions):

- Infrastructure: "The Customer provides all required infrastructure (servers, hosting, licenses, VPN
  access, etc.) in working condition and within the timelines agreed".
- Third-party services: "The Customer is responsible for all third-party services (e.g., SMS, email,
  payment gateways)".
- Data: "All test and production data (including content, directories, and media assets) are provided
  by the Customer in a correct and agreed format."
- Formulas: "The Customer shall provide the Contractor with clear formulas, calculation logic,
  algorithms, and related business rules required for implementation of calculations and modeling
  functionality."; and, for the calculator, "deriving or validating the engineering formulas themselves
  is the Customer's responsibility" (Milestone 5).
- Approvals: "The First Party is responsible for obtaining all necessary approvals and licenses from
  any third party required for the services."
- Compliance: "Security, data protection, certification, and compliance requirements (GDPR, ISO, local
  regulations) must be provided by the Customer before the project start." - see the dispute in
  [[COM-015 Saudi cybersecurity and regulatory compliance]].
- User documentation: "Preparation of the user documentation is the responsibility of the Customer".
- Timely participation: feedback, approvals, clarifications, data, infrastructure (assumptions, first
  paragraph).

### When the client's input is late - disputed

Added 2026-09-28 (a query). The contract and the SOW v10.4 give different remedies. Both kept for the
PMs; none is picked.

- Version A, the contract: "The First Party shall respond to reasonable written clarification
  requests within three (3) business days." (2.6) "The Second Party may not suspend performance merely
  because a clarification is pending, unless the specific unanswered item makes the affected task
  objectively impossible and the First Party has failed to respond within the three- business-day
  period after a clear written request. Any suspension shall be limited strictly to the affected task
  and shall not affect unrelated work." (4.5) Clarifying questions give no right to "additional fees,
  suspension, termination or extension of time" without a signed Change Request (2.5), and Innowise
  "may not terminate because of ordinary clarification requests, disagreements, or matters already
  included in the agreed scope" (11.3). The contract has no compensation for idle time.
- Version B, the SOW v10.4: if the parties cannot agree on requirements, scope, approach, estimation or
  acceptance criteria, "or if the Customer fails to provide timely feedback, approvals,
  clarifications, or participation reasonably required for continuation of the Project activities, the
  Contractor shall be entitled to suspend the affected activities and/or initiate termination of this
  SOW"; and "the Customer shall compensate the Contractor for the idle time resulting from such delays
  or failure to provide required input, provided that the Contractor has given the Customer a prior
  written notice of the upcoming downtime", pro rata ([[2026-06-15 SOW v10.4 - rendering]] row 13).

The contract's order of precedence puts the Agreement above the SOW (1.3); the SOW v10.4 is not
confirmed as Annex 1 ([[QUE-006 Which SOW and which plan are Annex 1 and Annex 2]]). The SOW clause
came from PMO's time-and-materials protections of 15 May 2026: "добавлено право приостановки
работ/termination при отсутствии обратной связи или невозможности согласовать требования" (Yauheni
Krasner, [[2025-11-25 Contract chat - rendering 2]] 2026-05-15 07:04). The delivery term:
[[COM-001 Delivery within six months]].

Who the authorized contacts are is not known yet (added 2026-09-28, the call of that day;
[[2026-09-28 Optimum discuss next steps - transcript]]). Anton: "А вот они никогда не говорили, с кем мы
реально работать будем?" (00:15:22). Arseniy, from what he heard: "сами ребята, с которыми мы будем уже
работать, которые ответственны за реализацию с их стороны, они англоязычные, они все есть, и нам выделят
конкретных людей. вот просто decision-maker. вот этот чел, который говорит только на арабском"
(00:15:40); the presale call with the owners ran through an interpreter (00:14:17). Mikhail: "вот они
еще как бы decision-maker и не владеют языком" and "Вопросы будут возникать, без них никуда" (00:18:36,
00:18:47).

Who the client's people are (added 2026-10-13, the contract chat's part 4): "Ishaq Lawal - General
Manager", "Dr.Yahya Alsayel - юрист", "Dr. Jaber - CEO", "Ayaa Khalid - ассистент", "Через Айю
координируем все" (Lizaveta Shauchenka, [[2025-11-25 Contract chat - rendering 4]] 2026-09-29 08:21, 08:22). No project contact yet:
"Будет отправлено письмо клиенту, и клиент потом выдаст контактное лицо для этого проекта" (Kavalchuk,
12:25); on 13 October he is writing that letter ([[2026-10-13 Optimum Three Caballeros call - transcript]] 00:48:04). What we ask the client for
(Mikhail, 2026-09-29 07:02): an English-speaking project lead as the single point of contact; a product
or business owner "with sufficient authority to clarify business requirements, make product decisions
and approve project deliverables"; timely access to subject experts; an escalation path; a kickoff;
executive support with IT security approvals and access; "Monday through Thursday as the primary
collaboration window". Mikhail on delays: "по текущим условиям контракта задержки со стороны клиента
не освобождают нас от обязательства выполнить delivery в установленный срок" (15:51). Kavalchuk, from
experience in the region: the person named may not engage, or "в душе не знает ничего про этот проект"
(00:12:43, 00:18:18). [[K-4 No client contact with authority, or a slow one]].
The project contact (added 2026-10-14): the letter asking the client for a responsible person went on 13
October ([[2025-11-25 Contract chat - rendering 5]] 2026-10-13 12:57). On 14 October the client named Ishaq Lawal, its General Manager: "пока
получил это лицо как контакт" (Kavalchuk, [[2026-10-13 OE Big4 chat - rendering 1]] 2026-10-14 08:21); "Сегодня получили контактное лицо для
проекта (возможно будет ещё кто-то)" ([[2025-11-25 Contract chat - rendering 5]] 2026-10-14 12:47). Our letter to him the same day ([[2026-10-14 Project email thread - rendering 1]]) asks
for kick-off slots the following week, for confirmation of "who on your side will review and approve
final decisions on the Project scope and the Milestone deliverables. We would be glad if this could be
you, or please let us know whom else we should involve", and whether other business colleagues should be
involved; it names Anton Oparienko our PM and "main point of contact for day-to-day project coordination,
planning and progress updates". Whether the contact can decide is open: "в письме надо проверить,
насколько это контактное лицо будет что-то решать, может этот человек условно чуть выше, и будет кто-то
ещё ниже, кто будет заниматсья проектом напрямую" (Kavalchuk, [[2026-10-13 OE Big4 chat - rendering 1]] 2026-10-14 08:32). The client has not
answered.

Who does what on the client's side (added 2026-10-30, the introductory call of 20 October;
[[2026-10-20 Introductory call - transcript]]). Mr. Lawal: "I'm the project sponsor from our end. So
most of the decisions will be made by myself", and he provides the subject matter expertise
(00:05:40). Asked by Mikhail whether he will be "accepting these prototypes and rest of requirements":
"That is correct." (00:36:57, 00:37:16); he attends the working sessions, "unless I'm not available"
(00:38:33). Ms. Ayaa: "anything that is contractual, financial issues, contractual issues, you know,
business side things" (00:17:06). Ms. Zahra, "the focal point for anything technical" (Ayaa,
00:00:00), and Ms. Joud, "both IT specialists" (00:17:06): "You will be actively on a day-to-day basis
dealing with both Zara and Jude", and they are the interface to the client's internal people
(00:19:24). The window: "Yes, we'll be meeting Monday through Thursday" (Ayaa, 00:27:24); "our working
hours are from 8 to 5:30", late morning or early afternoon preferred (00:27:34, 00:27:47). So the
contact decides on the prototypes and requirements; who confirms minutes and deliverables in writing
is still not stated ([[COM-018 Written minutes, notices and amendments]],
[[COM-002 Written acceptance of each deliverable]]).

### Who checks the formulas - two texts

Added 2026-10-30 (the introductory call of 20 October; [[2026-10-20 Introductory call - transcript]]).
Both kept; none is picked.

- The SOW v10.4: the client provides "clear formulas, calculation logic, algorithms, and related
  business rules", and "deriving or validating the engineering formulas themselves is the Customer's
  responsibility" (above).
- Mr. Lawal, 20 October: "There needs to be from your side some level of control also, because
  otherwise, if we make— if we made any mistake from our side or we miss something important, you will
  not be able to capture it or address it until it becomes too late. And then it will become, oh, but
  that is what you said." and "there needs to be a level of double-checking from your side in case if
  something is wrong or there's a mistake, you can identify it and we can discuss it" (00:12:59).
  Arseniy: "Yeah, absolutely. We understand you absolutely. That's the only right approach."
  (00:14:21) The data and formulas they send: "only for to gain insight. You know, as a general guide.
  Okay, not as something to replicate." (00:48:10)

Asked whether Innowise has in-house subject experts in oil and gas or drilling (00:09:44), Anton: "we
are basically inviting the domain experts from our PE team, though we cannot specifically promise that
they will have the expertise" (00:15:05). The risk: [[K-2 Losses from a calculation defect fall on us]];
the quality: [[CON-003 Correct calculations]].

### Who pays for the hosting - two texts

Added 2026-10-02 (the call of 1 October). The SOW v10.4 has the client provide "all required
infrastructure (servers, hosting, licenses, VPN access, etc.)" (above). The contract: "The total
Contract price shall not exceed [amount removed], inclusive of all fees and costs necessary to perform
the agreed scope." ([[2026-09-07 Final contract - rendering]] 7.1); components that "impose ... recurring licence fees" need "prior
written approval" (8.4); the Agreement ranks above the SOW (1.3). Mikhail's reading: "Там есть риск, что
они могут попытаться на нас стоимость костов за облачного провайдера переложить ... Но там опять-таки
явно не прописано, что мы за это должны платить, и Common Sense говорит, что это их часть."
([[2026-10-01 Optimum Three Caballeros call - transcript]] 00:25:49). Both kept; legal reading: ask a PM. [[K-1 Cloud hosting costs put on us]]; the
hosting proposal is [[DEC-012 Host the central system on Google Cloud in the Kingdom]].

## By when

Not stated, except compliance requirements before the start. Clarifications: [[COM-007 Client answers clarifications within three business days]].

## How it is accepted

Not stated.

## Drives

- [[CON-003 Correct calculations]]
- [[CON-002 Deployment outside public cloud]]
- [[DEC-012 Host the central system on Google Cloud in the Kingdom]]
- [[K-1 Cloud hosting costs put on us]]
