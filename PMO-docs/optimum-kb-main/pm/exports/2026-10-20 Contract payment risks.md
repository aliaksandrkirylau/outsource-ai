---
type: export
audience: internal - Michael Labutin and Alexey Gamanovich, Mikhail Andrushkevich fyi; a post in the Google Chat space "Optimum p&l model discussion - Oct 20" (spaces/AAQAZFPju1U). Michael asked for it on the call of 20 October ("А можно это текстом продублировать, как-то более юридически звучит", 3:46), Anton took it ("я отпишу комментарий к нему по поводу где узкие места", 9:09)
date: 2026-10-20
built_from:
  - "[[2026-09-07 Final contract - rendering]]"
  - "[[2026-09-07 Final contract - overview]]"
  - "[[COM-002 Written acceptance of each deliverable]]"
  - "[[COM-004 Twelve-month warranty]]"
  - "[[COM-005 Change requests]]"
  - "[[COM-006 Information sufficient for scope and price]]"
  - "[[COM-012 Payment schedule]]"
  - "[[COM-016 Termination and settlement]]"
  - "[[COM-017 Liability, indemnity and force majeure]]"
  - "[[DEC-009 Sign the client's final contract as it stands]]"
  - "[[DEC-016 Send the SOW as it stands and start preparing without waiting for its signature]]"
  - "[[K-3 The six months run from the client's signature, before discovery starts]]"
  - "[[K-8 Payments held for want of an approved Financial Plan]]"
  - "[[K-10 Fixed price with vague acceptance criteria]]"
  - "[[2026-06-15 SOW v10.4 - rendering]] (row 16, the Milestone 5 and 6 cost cells)"
  - Bluedot "Optimum p&l model discussion", 2026-10-20 11:32 UTC, 13 min (6ad7514411c3987fc8770384), not stored
  - Yauheni Krasner's contract reviews in the contract chat, 2026-05-06 and 2026-08-13 (spaces/AAQAXooObiI threads 2HUIRam_i04 and As17oWpntrU), linked by Mikhail Andrushkevich in the P&L chat at 11:37 and 11:40 UTC
procedure_version: d6eb286
---
# Contract payment risks

Internal post for the P&L model chat, Russian, in Anton's voice. Sent by Anton. No figures: they are
in the P&L that was shown on the call. Clause numbers refer to the signed Agreement's English column.
Before posting: check that the SOW sent for signature no longer has the June wording on Milestones 4
and 5 (the "По документам" paragraph says it will be checked).

Everything below this line is what gets sent. No IDs, no links, no team names unless asked, no
status lines, no mention of the KB.

@Michael Labutin @Alexey Gamanovich Привет!

Расписал по контракту где у нас засады по деньгам. Пункты по подписанному тексту, английская колонка (при расхождении приоритет у арабской, 15.3). Насколько вижу, подписан тот же текст, что Женя Краснер разбирал 13.08, так что его 9 пунктов в силе, их приняли как известные риски 07.09.

Если коротко: оплата привязана к письменному акцепту, у которого нет срока, а оспоренный платеж неоплатой не считается. Юридического рычага получить деньги у нас по сути нет, держимся на отношениях с клиентом и деливери.

Оплата и приемка:
1) Платят только за подтвержденное выполнение работ месяца (7.4, 7.5): "Mere passage of time, staffing allocation, hours incurred, or submission of an invoice shall not by itself create any entitlement to payment". Те формально помесячно, по факту FP с milestone'ами.
2) Акцепт только письменный (3.2): "Silence, use for testing, partial use ... or lapse of time shall not constitute deemed acceptance". На каждую поставку у клиента 14 business days, после каждого исправления отсчет заново (3.3), число кругов не ограничено, а критерии приемки размытые.
3) Оспоренный инвойс или процент выполнения клиент может держать "without such withholding constituting a payment default" (7.12).
4) Ответить нам на это нечем. Расторгнуть можем только при "material and undisputed payment default", который тянется 20 business days после notice (11.3), а оспоренный платеж по 7.12 дефолтом не является. Права приостановить работы за неоплату нет, срока оплаты инвойса и пени за просрочку тоже.
5) Финальный платеж только после 6-го месяца, полной поставки, финального тестирования, "satisfaction of the agreed quality and performance requirements", исправления всех material defects и финального письменного акцепта (7.6).
6) Клиент может выйти for convenience за 10 business days (11.2). Нам тогда платят только за работу "actually completed, delivered and objectively capable of being used" минус оплаченное и минус затраты на исправление наших нарушений (11.4), спор по сумме через независимого эксперта (11.5). Код и незавершенные работы отдаем все, включая неоплаченные (11.7), так что переход IP только после оплаты (8.1) рычагом не назвать.
7) Ответственность не меньше полной цены контракта, по confidentiality, data/security и IP без лимита (12.3). Плюс саудовское право и арбитраж в Эр-Рияде (14), доказывать что-то будет долго и дорого.

Что съедает запас без доп оплаты:
CR - "completion of omitted functions already implicit in the SOW, or measures necessary to achieve the agreed purpose" не CR (4.4), сверх цены только по подписанному клиентом CR (4.3, 7.10).
Срок - 6 месяцев от Effective Date, которая в контракте не определена (2.2), клиент может считать от своей подписи 07.10. Продление только через CR, задержки клиента срок не двигают (2.5, 4.5)
Гарантия - 12 месяцев от финального акцепта, все наши дефекты бесплатно, включая Minor/Trivial (3.4, 3.5).

По документам: Annex 2 (Approved Financial Plan) к контракту не приложен, а платить будут только на счет "identified in the approved Financial Plan" (7.11) - формальный повод придержать даже аванс. SOW пока не подписан, в июньской версии M4 и M5 "deemed covered by the Advance Payment", а по контракту платежи в конце каждого из месяцев 1-5 (7.7). Перед отправкой SOW выравнивали с контрактом, перепроверю что этого там не осталось.

По потоку (цифры в P&L, что показывал на колле): аванс - единственный запас. Деньги за месяц приходят только после акцепта. Пример с колла: стартуем 1 ноября, за ноябрь получаем где-то в декабре, как повезет с приемкой, и каждый круг правок это еще +14 business days. Команда в это время тратит, запас сужается каждый месяц, после финальной поставки с учетом 12 месяцев гарантии выходим близко к нулю. Любой сдвиг акцепта уводит в минус раньше, поэтому и нужен contingency buffer, который PM может придерживать.

По contingency buffer жду итогов колла с Игорем.

@Mikhail Andrushkevich fyi
