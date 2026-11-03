# NFRs

Non-functional requirements for Discovery: the business side I collect in the sessions, with a measure for each ([[00 discovery-BA-plan]], section 4). Working material, not evidence. The Tech Lead owns the Concern notes and the technical side (the questionnaire in S08); agreed measures go into the Concern notes and the V&S constraints ([[vision-and-scope]]).

| Attribute | The client's words, or the source | Measure | Asked in | Concern |
|---|---|---|---|---|
| Data integrity | "99.9% data integrity" (Q&A A.1) | to define | S00 E1, S02 B7 | [[CON-001 Offline operation and sync between rigs and HQ\|CON-001]] |
| Offline work and sync | Unreliable rig connections; "efficient synchrony" (Q&A A.1, A.2) | to define | S08 | [[CON-001 Offline operation and sync between rigs and HQ\|CON-001]] |
| Responsiveness | "low latency" (Q&A A.1) | to define | S00 E2, S06 A5, S07 A4 | [[CON-005 Easy and responsive interface\|CON-005]] |
| Usability | "User friendly interface" (Q&A A.1); "very, very modern" (20 October) | to define | S00 | [[CON-005 Easy and responsive interface\|CON-005]] |
| Quality at go-live | "minimal bugs" (Q&A A.1) | to define | S00 E5 | - |
| Report completeness | "complete and accurate reports" (Q&A A.1) | to define | S00 E1, S06 | - |
| Correct calculations | The client's formulas; deviation to agree | to define | S05 D1 | [[CON-003 Correct calculations\|CON-003]] |
| Scale and retention | About 70 rigs, up to 100; data kept as long as needed | to define | S00 C2, S08 | [[CON-004 Scale and data volume\|CON-004]] |
| Deployment and updates | Rig computers often offline; the client's servers | Tech Lead | S08 | [[CON-002 Deployment outside public cloud\|CON-002]] |
| Availability, backup and recovery, data export | Asked in the SOW review; not in the SOW | Tech Lead | S08 | none yet |
| Customer data confidentiality | Data about the client's customers | to define | S08 | [[CON-006 Confidentiality of the client's customers' data\|CON-006]] |
| Saudi cybersecurity | NCA controls; category open | Tech Lead | S08 | [[CON-007 Saudi cybersecurity and data protection rules\|CON-007]] |
| ISO 9001, ISO 14001, API | Mr. Lawal, 20 October | to define | S03 C2, S05 B2, S06 C4 | [[CON-008 Compliance with ISO 9001, ISO 14001 and API standards\|CON-008]] |
