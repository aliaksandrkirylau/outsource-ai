---
type: decision
id: DEC-009
status: draft
origin: extracted
author: claude-code/claude-opus-5-5
kind: business
sources:
  - "[[2025-11-25 Contract chat - rendering 3]]"
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-09-28 Optimum discuss next steps - transcript]]"
valid_from: 2026-09-04
tags:
  - contract
  - risk
---
# DEC-009 Sign the client's final contract as it stands

## Context

Through the summer of 2026 Innowise tried to adapt the client's contract to its own terms
([[DEC-008 Fixed price with milestones, on the client's contract]]). In August the client, through its
intermediary, brought back terms PMO judged undeliverable. Alexey Gamanovich, 20 August: "мы по сути
откатились на шаг назад с этим посредником к условиям при которых проект нельзя физически сделать для
конечника" ([[2025-11-25 Contract chat - rendering 3]] 2026-08-20 09:19).

On 2 September the client declined further changes: "our position is that we are prepared to proceed
with the Agreement in its current form and move directly to execution", and "Reopening these provisions
at this stage would effectively reopen matters that have already been extensively reviewed and
negotiated between our teams." It clarified the warranty: "The warranty relates specifically to the
quality of the work delivered under the Agreement" (the client's letter, relayed by Lizaveta Shauchenka,
2026-09-02 15:55; [[COM-004 Twelve-month warranty]]). Sales: "Считаем, что нужно соглашаться с их
условиями и принимать последнюю версию договора." (same message)

PMO's condition, 3 September: "если апрувают Иван Шатухо и Миша Лабутин от производства, то будем
работать", with the warning "при данных формулировках у нас нет юридических защит если кастомер начнет
"чудить"" (Alexey Gamanovich, 2026-09-03 09:12). PMO's contract risk reviews belong in the PMO risk
register; they are linked here when it is filed.

## Options considered

1. Keep negotiating. Closed by the client on 2 September (above).
2. Walk away. Alexey Gamanovich on 20 August: if the client "не идет навстречу согласовать условия при
   кот. можно этот проект заделиверить ... то смысла тут что-то дополнительно придумывать не вижу
   смысла" (2026-08-20 09:19). Not taken.
3. Sign the client's final version as it stands and start. Chosen.

## Decision

Yauheni Krasner, 4 September: "сегодня было принято решение со стороны менеджмента подписываться и
стартовать проект." (2026-09-04 10:06). The call of 7 September: "По итогам звонка договорились идти в
проект и принимать текущую редакцию контракта, несмотря на сохраняющиеся контрактные риски."
(2026-09-07 10:32). Who in management decided is not stated by id, so no deciders are named; the
7 September summary is copied to Alexey Gamanovich, Lizaveta Loseva, Anton Snotov, Lizaveta Shauchenka,
Ivan Shatuho, Michael Labutin and Arseniy Klimenko.

## Rationale

The sources give no rationale beyond the options above: the client called its version final, and the
one option left was to walk away. Why the project is worth taking at all:
[[DEC-001 Delivery quality over margin]].

## Consequences

The risks accepted, as the 7 September summary lists them (point 2):

- "отсутствие automatic acceptance (потенциальная бесконечная приемка без оплаты)":
  [[COM-002 Written acceptance of each deliverable]];
- "необходимость исправления в рамках приемки в том числе Minor/Trivial дефектов":
  [[COM-003 Quality and defect correction at no charge]];
- "12-месячная гарантия": [[COM-004 Twelve-month warranty]];
- "отсутствие возможности расторгнуть договор с нашей стороны, кроме payment default":
  [[COM-016 Termination and settlement]];
- "подтверждение, что до старта мы получили всю необходимую информацию для разработки проекта":
  [[COM-006 Information sufficient for scope and price]];
- "широкая формулировка compliance со всеми применимыми требованиями Saudi Arabia":
  [[COM-015 Saudi cybersecurity and regulatory compliance]], [[CON-007 Saudi cybersecurity and data protection rules]].

The new obligations, from the same summary:

- "постоянно контролировать P&L и не допустить быстрого выгорания бюджета" (point 3);
- "Со стороны delivery проект берем под усиленный контроль: Арсений - DM, Леша - PM." (point 4);
- the team joins in phases, strong people first (point 5; [[DEC-002 Senior engineers first]]);
- "Разработку не начинаем, пока не закроем основные вопросы и не убедимся, что команда одинаково
  понимает scope - чтобы минимизировать переделки на FP." (point 6);
- "В ходе проекта отдельно сохраняем все договоренности и артефакты по требованиям, приемке и
  коммуникации с клиентом с учетом контрактных рисков." (point 9);
- "В случае проблем и эскалацией - собираемся тем же составом и определяем стратегию работы." (point 10).

Hard to reverse: once signed, the contract gives Innowise no way out short of a payment default (COM-016).

Restated on 28 September (added 2026-09-28, the call of that day;
[[2026-09-28 Optimum discuss next steps - transcript]]):

- Arseniy: "вот сейчас они сказали, что все, мы больше типа не намерены с вами делать правки и
  корректировки в контракт, вот финальная версия у нас есть, или подписывайте ее, или все, не надо. И мы
  сказали, будем подписывать" (00:03:10).
- Anton's reading of the acceptance terms, the same risk as the 7 September list's "потенциальная
  бесконечная приемка без оплаты": "Технически, если ребята очень этого хотят, мы можем типа не
  заделерить это никогда по текущим условиям контракта и работать типа очень долго, бесплатно."
  (00:16:40). Arseniy on taking it on: "Я с технички, меня спросили, готов ли я поставить свою пятую
  точку. Я сказал, что готов. Технически мы это все сделаем." (00:17:01)
- Two proposals of that call run against point 6 above ("Разработку не начинаем, пока не закроем
  основные вопросы"): [[DEC-010 Confirm the product with the client through prototypes in code]] and
  [[DEC-011 Move scope between milestones and start building in the first month]]. Not settled; for the
  deciders.
