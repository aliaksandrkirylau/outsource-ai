# 2026-09-28 Contract vs SOW disagreements

Anton's note for sharing inside the team, written from the KB at commit a94b25e. Working material,
not evidence: the facts and quotes are in [[COM-001 Delivery within six months]],
[[COM-008 Client cooperation and dependencies]], [[COM-012 Payment schedule]],
[[COM-015 Saudi cybersecurity and regulatory compliance]], [[COM-016 Termination and settlement]],
[[QUE-006 Which SOW and which plan are Annex 1 and Annex 2]], [[QUE-007 What is the Effective Date]]
and [[DEC-009 Sign the client's final contract as it stands]]. The text below is meant to be pasted
into Chat or email as it is.

---

Hi all,

Here's where the signed Optimum contract and the SOW v10.4 disagree, from the KB. 5 commitments are marked disputed there, both versions are kept in the notes, and nothing is settled yet. No figures here, those stay in Drive and the P&L. Internal only, not for the client.

Two things up front. The contract's order of precedence (1.3) puts the Agreement above the SOW, so on the face of it the contract wins every clash below. But nobody has confirmed the SOW v10.4 is actually Annex 1. Also, the Arabic text prevails (15.3), and we only have the English in the KB.

Delivery term (COM-001):
Contract - 6 months from the Effective Date, extended only by a CR the client signs (2.2). Clarification requests give no extra time (2.5).
SOW - "approximately six (6) months" from a start agreed by email. It extends for client or third-party delays, and if discovery finds more work (row 14).
We asked on Aug 25 that client delays extend the term day for day, and the client declined on Sep 2. The English text has no penalty clause for late delivery. What happens instead: a month's payment isn't due until that month's work is done (7.5), and the final payment waits for final acceptance (7.6).

Late client input (COM-008):
Contract - we can pause only a task that is objectively impossible, and only after the client missed its 3 business day answer. Even then only that task pauses (4.5). No idle time compensation, and we can't terminate over it (11.3).
SOW - we can suspend the affected work or start termination, and the client pays for idle time after written notice (row 13).

Payments (COM-012), three versions:
Contract - a capped advance, then a payment at the end of months 1-5, each only on verified completion of that month's work. The final payment comes at the end of month 6, on final acceptance (7.3-7.7). The client can withhold disputed amounts without it counting as a payment default (7.12).
SOW fee schedule - a cost for each of milestones 1-4. Milestone 5's cell says milestones 4 and 5 are "deemed covered by the Advance Payment", and milestone 6 has no cost of its own. The advance is paid per "Clause 4.6 of the Agreement", which doesn't exist in the final contract.
Plan sent on March 11 - an advance, then a payment each month April to September. It's from the T&M days, before fixed price.

Saudi compliance (COM-015):
Contract - we warrant compliance with all applicable Saudi cybersecurity and data rules, NCA included, plus hosting, data residency and cross-border transfers. "No category of applicable Saudi requirement is excluded" (10.1-10.2).
SOW - the client provides the compliance requirements before the start.
Our July 14 letter tried to narrow it to NCNICC-1:2025 + PDPL, and the client widened it instead. It was accepted as a known risk on Sep 7. Related open point: is the client NCA category A or B? We think B, but the client hasn't confirmed. If it's A, pen testing is mandatory, and it isn't in the WBS.

Termination (COM-016):
Contract - the client can terminate for convenience on 10 business days' notice, or for a breach not cured in 15 business days (immediately for "repeated material delay"). We can terminate only for an undisputed payment default that lasts 20 business days (11.1-11.3). On termination we're paid only for work that is completed, delivered and usable (11.4).
SOW - either party can terminate for convenience on 30 days' notice (row 37).
We asked for mutual rights on Aug 25, the client declined on Sep 2, and it was accepted as a known risk on Sep 7.

Smaller mismatches, not marked disputed:
Acceptance (COM-002) - the SOW points to clauses 7.9-7.10 of the Agreement, which in the final contract are the progress report and the price cap. The real terms are 3.2-3.3: 14 business days per delivery, the clock restarts after each fix, and there's no deemed acceptance.
SOW header - it names "Contract No. (1/26) dated 15/05/2026" and a different client registration number from the contract.
Defect fixing (COM-003) - the contract leaves remediation times to the SOW, and the SOW has none. Minor and Trivial defects have to be fixed too.
Liability (COM-017) - the SOW's limits (business impact, code changed by others, other environments) aren't in the contract. Contract 12.3 is a floor, "not less than the total Contract price", with no cap.
Warranty (COM-004) - 12 months from final acceptance, and the SOW puts support under a separate SLA. On Sep 2 the client clarified that the warranty covers defects in our work only. There's no WBS line for it.
Specialists (COM-010) - not a conflict. The contract needs approval only for subcontracting or assigning part of the work (6.2), and the SOW lets us replace a specialist on 15 days' notice. Neither commits to a named team.
14.2 reads "within thirty (15 ) days".

Open questions under all of this:
1) Which SOW is Annex 1, and what is Annex 2 (QUE-006). Yauheni Krasner said v10.4 is "по идее" (in principle) the final one, and on Aug 12 the client sent back only the contract. Annex 2 "Approved Financial Plan and Milestones" is named in 15.6, but nothing is attached. The contract also uses it to value our work on termination (11.6).
2) Effective Date (QUE-007) - used in 2.2, 2.4, 8.5 and 10.3, never defined. The client hasn't signed yet (their CEO collects the original on Sep 29). Until the date is fixed, the 6 months have no start.
3) What we accepted knowingly (DEC-009, the Sep 7 list): no automatic acceptance, fixing Minor/Trivial defects, the 12 month warranty, no termination on our side except payment default, the "we had all information" confirmation, and the broad Saudi compliance wording. The delivery term, the payment schedule and the late-input rules aren't on that list.

The KB has no legal reading of how 1.3 settles any of this, that one is for Legal.
