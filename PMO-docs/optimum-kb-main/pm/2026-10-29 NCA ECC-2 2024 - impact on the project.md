# 2026-10-29 NCA ECC-2 2024 - impact on the project

Mikhail's working note, written with the agent from the KB at commit 1ba5f53 and the NCA's public
text of ECC-2:2024
(https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf).
Working material, not evidence: nothing here is agreed, and nothing is recorded in `knowledge/` yet.
It complements [[2026-10-29 SOW review clarifications - strategy]], which already covers identity and
access (2-2-3), backup and recovery, and first positions on 2-11, 2-12, 2-15, 2-8, 4-1 and 4-2. This
note covers the rest of the document. The Arabic text of ECC binds; quotes below are from the English
version.

## Bottom line

ECC-2:2024 does not formally apply to OES, but in practice it is now the yardstick: the client cites
it in its SOW review, contract 10.1 warrants compliance with "all cybersecurity controls ...
applicable to the Project, including applicable requirements of the National Cybersecurity Authority
(NCA)", and under 10.3 a requirement "publicly issued before the Effective Date ... shall not
constitute a Change Request" ([[2026-09-07 Final contract - rendering]]). ECC-2:2024 is public. The
cheapest moment to draw the limits is before the SOW is signed.

## Applicability

- ECC's scope: government agencies, their affiliated companies, and "all private sector entities
  owning, operating, or hosting Critical National Infrastructures (CNIs)". OES is none of these; the
  July reading was that ECC does not apply ([[CON-007 Saudi cybersecurity and data protection rules]]).
- Why "it does not apply" is a weak argument: ECC 4-1-2-3 obliges an entity to bind its third parties
  to "apply the entity's cybersecurity requirements and policies". General knowledge, not a project
  fact: Saudi Aramco is in ECC's scope, and OES is its supplier
  ([[2025-10-23 OES company research - rendering]]). So ECC can reach OES, and through OES us, by
  contract, whatever its own scope says. Ask; don't assume.

## Who owns which control

Proposal: put a shared-responsibility table like this one into the SOW before signature. It is what
actually limits 10.1; a reply e-mail does not amend the Agreement (1.3).

| Owner | ECC-2:2024 controls | What it means for us |
|---|---|---|
| Us - the product and how we build it | 1-6-2 and 1-6-3 secure development; 2-2-3 in the application; 2-8 encryption; 2-12 logs the application writes; 2-15-3-2 to 2-15-3-5 (multi-tier, HTTPS, authentication); 2-6-3 data on the rig laptops | Scope, mostly M2, M3 and M6 |
| Hosting (GCP in the Kingdom, [[DEC-012 Host the central system on Google Cloud in the Kingdom]]) | 2-5-3 segmentation, IPS, DDoS protection; 2-15-3-1 WAF; 2-9 backups; 4-2-3 data protection, separation and return | Cloud configuration, and running costs ([[K-1 Cloud hosting costs put on us]]) |
| OES as an entity | 1-1 to 1-5 and 1-7 to 1-10 governance; 2-1 assets; 2-4 e-mail; 2-13 incident reporting to the NCA; 2-14 physical security; SIEM and continuous monitoring; periodic reviews and tests | Not ours; the application supports them |

## Impacts beyond the SOW review note

1. **Penetration testing becomes effectively mandatory.** 2-11-3-1: "Scope of penetration testing to
   include all externally provided services (via the Internet) ... web applications". This holds
   whatever the NCA category, so if ECC is the yardstick,
   [[QUE-005 Is the client an NCA Category A or B entity]] no longer decides it. Neither WBS has a
   penetration test. A position is needed before they ask: we price one test before go-live, or we fix
   the findings of a test OES commissions. Periodic tests (2-11-3-2) are OES's operations. Whether
   the gap is costed internally: see private notes.
2. **Secure development is ours as the developer.** 1-6-3: "Using the secure coding standards";
   "Using trusted and licensed sources for software development tools and libraries" (also contract
   8.4 on licences, and an SBOM as in CON-007); "Conducting compliance test for software against the
   cybersecurity requirements within the entity"; "Secure integration between applications";
   reviewing "secure configuration and hardening" before launch (also 1-6-2-2). These belong in M6
   acceptance and in the definition of done.
3. **Claude-assisted development.** 1-6-3-2 asks for trusted tools, and 4-1-2-3 can bind us to OES's
   policies, which may cover AI tools ([[DEC-014 Staff on demand, seniors who work with Claude, fewer developers]]).
   Better to state our practice up front, including that no production data goes into AI tools, than
   to have it found later.
4. **Our team as a third party.** 1-9-3-2 "screening or vetting for personnel in ... technical
   positions with critical and privileged powers"; our remote access to their cloud needs MFA
   (2-2-3-2) and logging (2-12-3-2); access revoked when someone leaves. Linked to
   [[QUE-009 Where may our team members be located]]. If we ever offer monitoring or operations after
   go-live, 4-1-3-2: "Cybersecurity managed service centers for monitoring and operations which use
   remote access shall be fully located in the Kingdom of Saudi Arabia."
5. **The audit log is too narrow.** 2-12-3-5: "Retention period of cybersecurity event logs (shall be
   at least 12 months)", and logs for "privileged accounts" and "remote access events" (2-12-3-2).
   `WBS:Development Flutter!21` covers data entry, edit and backfill, "Up to 30 logged actions";
   sign-ins and admin actions are not in it.
6. **Network and web protection are hosting services with a running cost.** 2-5-3-2 "Isolation of
   production network from testing and development environment networks" (separate GCP projects or
   networks per environment); 2-5-3-6 IPS; 2-5-3-9 DDoS protection (new in ECC-2); 2-15-3-1 WAF. The
   SOW should say who pays (K-1).
7. **Cryptography per the national standards.** 2-8-3-1 "Approved cryptographic systems and solutions
   standards and their technical and regulatory restrictions"; the summary of 2-8 points to the NCA's
   National Cryptographic Standards. The TL checks the encryption of the desktop's local store and the
   TLS configuration against them.
8. **Rig laptops.**
   - 2-6-3-1 "Separation and encryption of the entity's data and information stored on mobile
     devices", 2-6-3-3 deletion "in cases of device loss": supports the encrypted local store and
     device revocation.
   - 2-3-3-2 "Strict restriction on the use of external storage media": works against moving data by
     USB stick for rigs that are never online ([[CON-001 Offline operation and sync between rigs and HQ]]).
   - 2-10-3-4 patches verified "using a non-production environment before being applied": applies to
     the update pipeline for the rig desktops, which has no internal WBS line
     ([[CON-002 Deployment outside public cloud]]).
9. **A cheap early win in M1.** 1-5-3-1 asks for a risk assessment "At early stage of technology
   projects". A short security risk assessment in the M1 vision and scope document also fixes in
   writing which controls we agreed to.
10. **Incident procedure.** 4-1-2-2 "Communication procedures in case of the occurrence of a
    cybersecurity incident"; contract 10.4. We need a written way of reporting incidents to OES during
    development.
11. **Two changes in ECC-2 not to lean on.**
    - Data hosting inside the Kingdom (ECC-1 4-2-3-3) was deleted from ECC and moved to the National
      Data Management Office. The PDPL, the NDMO and contract 10.2 still bind, so DEC-012 does not
      change.
    - The industrial control systems domain (ECC-1 domain 5) moved to the OTCC. Not our application,
      but the rig owners' networks may limit connectivity and updates. Worth asking.

## Questions to add to the client list

- Is OES bound by Aramco's supplier cybersecurity requirements, and which version?
- Will OES send its own cybersecurity policies (4-1-2-3)? Do they cover AI-assisted development?
- Who runs and pays for the WAF, DDoS protection, IPS, SIEM and penetration tests after go-live?
- Do the rig owners' network rules limit the application's connectivity or updates?

## When this is decided - what goes into the KB

Through ingest, with the SOW review note's list: ECC-2:2024 as a source (public, link only);
[[CON-007 Saudi cybersecurity and data protection rules]] updated with the applicability reading and
the flow-down through 4-1-2-3; a Decision on penetration testing; the responsibility table, if agreed,
into [[COM-015 Saudi cybersecurity and regulatory compliance]].
