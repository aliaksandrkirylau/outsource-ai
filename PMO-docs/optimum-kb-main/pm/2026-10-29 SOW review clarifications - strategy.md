# 2026-10-29 SOW review clarifications - strategy

Anton's working note, written with the agent from the KB at commit 1d3c78b and the NCA's public text
of ECC 2:2024 (link below). Working material, not evidence: nothing here is agreed, and nothing is
recorded in `knowledge/` yet. It is for the team to review before we answer the client. No reply is
drafted.

Who should look:

- Arseniy and Alexey: identity, offline sign-in, sync, backup and recovery, and the cost of each
  addition.
- Mikhail and Dana Kavalchuk: scope, what we give, and whether the answers go into the SOW or a letter.
- Leu: the users list export and the document library as requirements.

## What the client asked

From the client's internal review of the SOW (received by 2026-10-29), as sent:

> 1. Identity and Access Management
> - Identity Service: Please confirm the security features included in the project's identity service.
>   - MFA: How will MFA for remote access and privileged accounts be addressed?
>   - Password Recovery: How will users, particularly engineers, reset forgotten passwords?
>   - Offline Authentication: How will cached credentials, offline access, revoked accounts, and
>     unsynchronized data be handled securely?
>
> NCA Compliance: Please clarify how the solution addresses the Identity and Access Management
> requirements in Section 2.2.3 of NCA ECC 2:2024 (see attached screenshot).
> Reference Document: NCA Essential Cybersecurity Controls (ECC 2:2024),
> https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf
>
> 2. Additional Clarifications
> - Data Export and Backup: How can we export all relevant data and attachments and maintain restorable
>   backups?
> - Database Recovery (Milestone 2, Item 2.3): How will data be recovered after database corruption or
>   laptop replacement, including unsynchronized data?
> - Users List Export (Milestone 2, Item 3.3): Can an export option be included for administrative and
>   reporting purposes?
> - Help Documentation (Milestone 6, Item 5.2): We'd like to include a section where authorized
>   personnel can upload and manage user guides, videos, and PDFs?

The screenshot is not with us; the ECC text below is from the PDF itself.

## Where their item numbers point

Their numbers are the section number and the item's order within it in
[[2026-06-15 SOW v10.4 - rendering]], so they read v10.4 or the October version with the same layout.

| Their reference | SOW v10.4 item | What the SOW says now |
|---|---|---|
| IAM (no number) | M2 3 Web, Authorization/Authentication; M2 4 Desktop, Authorization/Authentication | Web: "MFA, single sign-on and social login, and password-reset flows beyond what the identity service already provides are not included." Desktop: offline login with "cached token and credential validation"; "Registration ..., password reset, MFA, and biometric login are not included." |
| Data export and backup (no number) | none | Backups are not mentioned. Report export (PDF, CSV, spreadsheet) is in M6. |
| M2 2.3 | Database structure setup | Schema for the central database and the local desktop store, "plus the foundation for syncing between them". Nothing on recovery. |
| M2 3.3 | Users list | "Bulk actions, import and export, and the audit-trail view are not included." |
| M6 5.2 | Project documentation as agreed | "End-user manuals, the in-app new-user wizard, and a technical user guide are the Customer's responsibility". |

Each question tests one of the SOW's exclusions, or a gap.

## The frame

**Why this is the cheapest moment.** The Agreement is signed and the SOW is not
([[DEC-016 Send the SOW as it stands and start preparing without waiting for its signature]]). Once
it is, these clauses work against anything we left vague
([[2026-09-07 Final contract - rendering]]):

- 4.4: "completion of omitted functions already implicit in the SOW, or measures necessary to achieve
  the agreed purpose shall not constitute Change Requests."
- 10.1: we warrant compliance with "all cybersecurity controls, requirements, frameworks and directives
  issued by the competent authorities in the Kingdom of Saudi Arabia that are applicable to the
  Project, including applicable requirements of the National Cybersecurity Authority (NCA)."
- 10.3: a requirement "publicly issued before the Effective Date or reasonably foreseeable by a
  professional provider ... shall not constitute a Change Request". ECC 2:2024 is public.

**Where the answers must land.** 1.3: "No email, meeting note or proposal shall amend this Agreement
unless expressly signed as an amendment by both Parties." The SOW ranks below the Agreement and is
still unsigned. So the limits we want to hold belong in the SOW text before signature, not only in a
reply e-mail. Against that: changing the SOW means re-translating the Arabic, and in October the
client would not take changes to its wording (DEC-016). This time the client opened the review. For
Dana and Legal to decide.

**The SOW already makes room for detail.** M2 "Clarifications from Phase 1 findings" promises
"Written answers to the open questions and assumptions flagged in the Phase 1 vision and scope document
(role model, identity solution, offline-login expectations, ...)". So we can answer principles and
scope limits now, and leave design detail to the M1 vision and scope document. That only works if the
answer says now what is in and what is out.

**Posture: trade, don't defend.** Give what is cheap, especially what we owe anyway, and use it to
get firm written limits on what is expensive. Every answer ends in one of three places: covered as
written; added at no change; out of scope, available as a change request.

**MFA we probably owe already.** Our own July framework paper said NCNICC-1, the baseline we proposed,
requires MFA "for all administrative access and remote access to the system"
([[CON-007 Saudi cybersecurity and data protection rules]]). The SOW then left MFA out. Under 10.1 that
gap is ours whether or not ECC applies. ECC 2:2024 also widened the control: ECC-1:2018 asked for MFA
"for remote access" only; 2:2024 adds "privileged accounts" (the change table at the end of the PDF).
Better to give it now with credit than have it forced on us later.

## 1. Identity and access

### Does ECC apply at all

ECC's own scope: "government agencies in the Kingdom of Saudi Arabia ... and their affiliated
companies and entities (inside and outside the kingdom), as well as all private sector entities
owning, operating, or hosting Critical National Infrastructures". Everyone else: "The NCA strongly
encourages all other entities in the Kingdom to leverage these Controls". In July the team concluded
ECC does not apply to OES (Tsitou, in CON-007).

Don't lead with that. It reads as dodging, and 10.1 is wide. The risk the other way: answering control
by control can read as accepting ECC as our baseline. Wording that handles both: "how the application
supports OES's compliance with 2-2-3". Say that the entity-level controls are OES's own.

ECC 2:2024, 2-2 Identity and Access Management:

- 2-2-1: requirements "identified, documented, and approved" - OES.
- 2-2-2: requirements "implemented" - OES, with the application's support.
- 2-2-3, as a minimum:
  - 2.2.3.1 "Single-factor authentication based on username and password."
  - 2.2.3.2 "Multi-factor authentication, and defining the suitable authentication factors and their
    numbers as well as the suitable authentication techniques based on the result of impact
    assessment of authentication failure and bypass for remote access and for privileged accounts."
  - 2.2.3.3 "User authorization based on identity and access control principles (Need-to-Know and
    Need-to-Use principle, Least Privilege principle, and Segregation of Duties principle)."
  - 2.2.3.4 "Privileged access management."
  - 2.2.3.5 "Periodic review of identities and access rights."
- 2-2-4: implementation "periodically reviewed" - OES.

The impact assessment in 2.2.3.2 is also OES's: it decides which accounts need which factors.

Ask back: which baseline OES holds itself to - ECC by choice, its customers' requirements, or
NCNICC-1 - and its NCA category ([[QUE-005 Is the client an NCA Category A or B entity]]). General
knowledge, not a project fact: Saudi Aramco has its own third-party cybersecurity standard for its
vendors, which may be where this comes from. Ask; don't assume.

### Control by control

| ECC 2:2024                                                   | Proposed position                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Cost to us                                                                                                                                                                                                                     |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 2.2.3.1 username and password                                | Covered (M2). Add a password policy, lockout after failed attempts, and auto-lock after inactivity on the shared rig computer. Identity-service configuration.                                                                                                                                                                                                                                                                                                    | Very little                                                                                                                                                                                                                    |
| 2.2.3.2 MFA for remote access and privileged accounts        | Give: authenticator-app (TOTP) MFA on the web, mandatory for Administrators; for other HQ users, OES decides from its impact assessment. Hold: no MFA for offline desktop sign-in. Instead, offline sign-in only on a registered rig computer, for engineers assigned to that rig, after one online sign-in there.                                                                                                                                                | Small if the identity service has it built in. Supabase Auth and Keycloak both do (general knowledge; [[DEC-004 Backend stack]] is still open). The real work is enrolment, recovery codes, admin reset and tests. TL to size. |
| 2.2.3.3 need-to-know, least privilege, segregation of duties | Covered: role-based access in M2 and M3, access limited to a supervisor's rigs, and approvals split the duties (the engineer enters, the supervisor approves edits, backfills and reports). The role matrix is settled in discovery ([[REQ-004 Roles and what each role can do]], three roles or four).                                                                                                                                                           | In scope                                                                                                                                                                                                                       |
| 2.2.3.4 privileged access management                         | In the application: a separate admin role, and admin actions logged. The SOW's audit log (M6) covers only "data entry, edit, and backfill actions", so adding user creation, role change, deactivation and password reset is an extension; I'd give it. Privileged access to the cloud console, the database and secrets is hosting: OES's, or set up on GCP with IAM and MFA for operators ([[DEC-012 Host the central system on Google Cloud in the Kingdom]]). | Small                                                                                                                                                                                                                          |
| 2.2.3.5 periodic review                                      | The review is OES's process. The application supports it with the users list (role, status, last sign-in) and its export (section 4 below).                                                                                                                                                                                                                                                                                                                       | Small                                                                                                                                                                                                                          |

### Password recovery

- Web: self-service reset by e-mail, which the SOW allows as far as the identity service provides it.
  It needs an e-mail service, which the SOW puts on the client ("The Customer is responsible for all
  third-party services (e.g., SMS, email ...)"). Admin reset as the fallback.
- Desktop: no self-service at the rig. The admin resets the password on the web; the engineer gets a
  temporary password and must change it at next sign-in; it reaches the rig computer with the next
  sync. This is what our prototype already shows: "Forgot your password? Ask HQ to reset it. The new
  password reaches this computer with the next sync."
  (`pm/prototypes/2026-10-15 OE prototype - desktop and web`). Until then another engineer on that rig
  signs in; 1 to 4 share the computer ([[REQ-003 Sign in on a shared rig computer]]).
- For the TL: does sync run under the device's own identity, separate from any signed-in user? If not,
  an engineer alone on a rig and locked out cannot trigger the sync that brings the reset.
- Not offered: emergency offline unlock codes. Complex, and weak.

### Offline sign-in

- Cached credentials: only a salted, slow hash of the password, never the password. Tokens and the
  local database encrypted under a key Windows protects. "Secure token storage" is already in M2.
- Who can sign in offline: only engineers assigned to that rig whose credentials reached the computer
  by sync, or who signed in online there at least once.
- Expiry: cached credentials stop working after N days without reaching the server; then an online
  sign-in is needed. N is OES's call, weighed against rigs that stay offline for long stretches
  (discovery question X1).
- Revoked accounts: a deactivation reaches the computer with its next sync, which wipes the cached
  credential and ends any session. Until then a revoked engineer can still sign in offline, for at most
  the expiry period. Anything entered after the revocation time is kept, never lost, but flagged for a
  supervisor at sync. A lost or stolen computer is revoked as a device, and its sync is refused.
- Rig clocks: comparing an entry's time with the revocation time needs a clock we can trust; rig clocks
  can't be ([[QUE-011 Who wins when a project is edited on the web and on an offline desktop]]). ECC
  2.3.3.4 asks for "Centralized clock synchronization with an accurate and trusted source". A design
  point for the TL.
- Lockout after failed attempts and auto-lock work offline too.
- Unsynced data stays in the encrypted local store, attributed to whoever entered it. Signing out or
  revoking the account does not delete it, and the app shows sync status.
- Disk encryption (BitLocker) and endpoint security on the rig computers: OES's IT.
- Scope: most of this is how M2 offline login and M3 sync get designed, so in scope. Flagging a revoked
  user's entries and revoking a device are small additions.

## 2. Data export and backup

- Ownership: the contract already gives them the data with no lock-in: 8.1 ("databases" owned by the
  First Party), 6.6 (delivery "without withholding or technical lock-in") and 11.7 (delivery on
  termination, with "reasonable transition assistance"). The central
  database is PostgreSQL in their own hosting, so they can export everything at database level at any
  time.
- Backups: say yes. The v1 WBS estimates `WBS:DevOps!13` "Backup and Disaster Recovery" although the
  SOW never mentions it ([[2026-10-01 SOW v10.4 to v1 WBS scope mapping]], 2a). The WBS the client saw
  in November 2025 promised "automated daily full and incremental backups , including a documented and
  tested Disaster Recovery (DR) restoration procedure" ([[2025-11-05 WBS sent to the client - rendering]]
  DevOps row 18). So:
  - automated backups of the database and file storage, kept in the Kingdom (under the PDPL, backups
    count as stored data; [[CON-007 Saudi cybersecurity and data protection rules]]);
  - retention by their policy (they said "Between 1-2 years" for data;
    [[CON-004 Scale and data volume]]);
  - one tested restore before handover, and the procedure written down.
- After handover: running backups and testing restores regularly (ECC 2.9.3.3 "Periodic testing for
  the effectiveness of backup recovery") is operations: OES, or a separate SLA. The SOW already puts
  support under an SLA.
- Costs: backup storage is a hosting cost, so theirs. Say it explicitly
  ([[K-1 Cloud hosting costs put on us]]).
- "All data and attachments": offer an export-and-restore procedure and a data dictionary in the
  handover documentation; both cheap. A one-click "export everything" in the interface is a change
  request. There are no attachments in the SOW at all ([[REQ-012 Documents uploaded at HQ available at the rig]]
  is a change request candidate), so the answer must not suggest there are.
- Likely source of the question: ECC 4.2.3.1 asks cloud and hosting providers for "returning data (in a
  usable format) upon service completion". The data sits in OES's own cloud account, so the procedure
  and the data dictionary answer it.

## 3. Database recovery (M2 item 2.3)

- Central database: covered by the backups (point-in-time recovery if it runs on a managed database).
- Rig computer: the central database is the system of record; the local store is a working copy.
  - Replaced computer: install the app, sign in online, and the rig's data comes back from the server.
  - Corrupted local store: an integrity check at startup triggers a rebuild from the server.
  - The only thing at risk is data not yet synced.
- Already in scope as sync quality: local writes that survive a crash or power loss; retries that
  cannot create duplicates; syncing whenever a connection is up.
- Offer as a scoped option:
  - an automatic encrypted snapshot of the local store, say at end of shift, to a second disk or a USB
    stick;
  - a restore that re-sends unsynced records;
  - an encrypted export of unsynced data for manual transfer, which also covers rigs with no internet
    at all (Mikhail's point in [[CON-001 Offline operation and sync between rigs and HQ]]).
  ECC 2.3.3.2 asks for "Strict restriction on the use of external storage media and their security", so
  the USB route needs OES's policy to allow it.
- Be honest in the answer: data that was never synced or backed up, on a destroyed computer, cannot be
  recovered. What a rig can lose is what it entered since its last sync or snapshot. This is where the
  client's "99.9% data integrity" (CON-001) can finally get a definition.
- Milestones: M2 item 2.3 is the schema and the sync foundation. Recovery belongs with the M3 sync
  work and must not slide into M2 acceptance.

## 4. Users list export (M2 item 3.3)

The SOW excludes "import and export", but I'd give it: a CSV or spreadsheet of user, role, status and
last sign-in; administrators only; each export logged, since it is personal data under the PDPL
([[COM-014 Confidentiality and personal data]]). Present it as support for the ECC 2.2.3.5 access
reviews. Report export to CSV and spreadsheet is built for M6 anyway; this is the same kind of thing
earlier and smaller.

## 5. Help documentation (M6 item 5.2)

Read it closely: they accept writing the manuals themselves and want a place to upload and manage
them. That is a new feature: upload, storage, categories, permissions, a viewer. It is the same
mechanism as REQ-012, the client's own earlier ask, "Document upload required from HQ but accessible
on the job site" (Q&A E.23), already a change request candidate.

Propose one document library as a change request, in two tiers:

- Tier A, web library: authorised people upload and manage PDFs and videos; web users view and
  download them; the desktop opens the library in a browser when online.
- Tier B, offline at the rig: Tier A plus PDFs synced to the rig computers for offline reading, videos
  excluded or size-capped given rig bandwidth. Much bigger, and depends on the sync design. Don't
  absorb it.
- Cheapest fallback: a Help link in both apps to a place OES controls, such as their intranet.

The in-app wizard stays out ([[REQ-014 Onboarding wizard for new users]]); the client wanted it "very
much", so expect it to come back next to this.

## Give and hold

| Give (cheap, mostly owed anyway) | Hold (change request, or OES's own) |
|---|---|
| MFA on the web for administrators, and other HQ users if OES chooses | MFA for offline desktop sign-in |
| Password policy, lockout, auto-lock | Privileged access to infrastructure, OES's impact assessment, its access reviews |
| Admin actions in the audit log | An "export everything" button in the interface |
| Users list export | The document library, Tier B above all |
| Backups with one tested restore before handover | Running backups and restore tests after handover; hosting and storage costs |
| Export procedure, data dictionary, a Help link | Local snapshots and USB transfer (offered as a priced option) |

Whether the "give" column comes at no change in price is open
([[DEC-003 Handling small change requests]]).

## What they may ask next from ECC

They are reading ECC 2:2024 against the SOW. The neighbouring controls, so we have positions ready:

- 2-11 Penetration testing: "Scope of penetration testing to include all externally provided services
  (via the Internet) ... web applications ..." and "Conducting penetration tests periodically." The
  WBS has no penetration testing (QUE-005). A position is needed: we fix findings from a test OES
  commissions before go-live, or we price one test. Periodic tests are OES's operations.
- 2-12 Event logs and monitoring: logs "for critical and privileged accounts ... as well as for remote
  access events"; SIEM; "Retention period of cybersecurity event logs (shall be at least 12 months)".
  Our audit log covers data edits only; sign-in and admin events need logging too (the 2.2.3.4 addition
  above). SIEM and monitoring are OES's operations; the logs can go to the cloud provider's logging.
- 2-15 Web application security: "Use of web application firewall", "multi-tier architecture",
  "secure protocols (e.g. HTTPS)", and user authentication factors set by OES's impact assessment
  "for users' access". Multi-tier and HTTPS are in the design; a WAF is a hosting service, so a
  hosting cost.
- 2-8 Cryptography: "Encryption of data in-transit and at-rest", "Secure management of cryptographic
  keys". Matches the DCC items in CON-007; the encrypted local store fits here.
- 4-1 Third parties, which is us: contracts must include "the secure removal of the entity's data by
  the third party upon the end of service", incident communication, and "Obligating the third party
  to apply the entity's cybersecurity requirements and policies". Expect OES to send its policies; the
  SOW asked for the compliance requirements before the start ([[COM-015 Saudi cybersecurity and regulatory compliance]],
  disputed). We should be able to say no production data sits with us, or how we remove it at the
  end.
- 4-2 Cloud and hosting: data protection by the provider and "returning data (in a usable format)
  upon service completion" (section 2 above).

## Before we answer

| What | Who | Needed |
|---|---|---|
| Identity service, and so the MFA cost | Arseniy, Alexey | The choice in DEC-004 |
| Device identity for sync; offline expiry default; trusted time for revocation | Arseniy | A design position |
| Size of each "give" item and of the recovery option | Arseniy | Rough size, not hours here |
| SOW text change or reply letter; give at no change in price or not | Dana, Mikhail, Legal | A call |
| Penetration testing position | Mikhail, Alexey | A call before they ask |
| Document library as one change request with REQ-012 | Leu, with Mikhail | Agreement to frame it so |

Questions back to the client:

- Which baseline OES holds itself to: ECC by choice, its customers' requirements, or NCNICC-1? Its
  NCA category, A or B?
- Which accounts count as privileged or remote in OES's impact assessment? Do engineers have phones at
  the rig, for an authenticator app?
- How long may a rig computer accept cached credentials without reaching the server? Are there rigs
  that are never online?
- Who runs backups and restore tests after handover? What is the retention policy for data and for
  logs?
- Who provides the e-mail service for password resets?
- Does OES's policy allow encrypted USB transfer from rig computers?

## When this is decided - what goes into the KB

Through ingest, once there is an answer or a decision:

- The client's clarification e-mail as a source; ECC 2:2024 as a source (public, link only).
- [[CON-007 Saudi cybersecurity and data protection rules]]: the client's request against ECC 2-2-3,
  with both readings of applicability.
- A new Concern for backup and recovery, central and rig.
- A Decision on MFA scope, and on the offline sign-in rules (expiry, revocation, devices).
- [[CAP-001 Identity, roles and access]]: its "Not included, per the SOW: MFA" line, if MFA comes in.
- A Requirement for the users list export; REQ-012 widened to the document library, or a new
  Requirement next to it.
- A Question only for what blocks a WBS line, such as the offline expiry if M2 desktop sign-in waits on
  it.
