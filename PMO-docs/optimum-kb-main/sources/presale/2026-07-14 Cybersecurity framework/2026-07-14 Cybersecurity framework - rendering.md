---
type: source
kind: rendering
date: 2026-07-14
original: https://docs.google.com/document/d/1SEBpkHih_4OCkGzdXrED-UwKy_sJa3bpt2YfU-7e9Fg
removed:
  - nothing
---

# 2026-07-14 Cybersecurity framework - rendering

Google Doc "Optimum cybersec framework", owned by Aliaksei Tsitou, created and last changed
2026-07-14. Verbatim; checkbox markers dropped. Never edited after storing.

### Framework 1: NCNICC-1:2025 (Private Sector Baseline)

This is your primary mandatory framework. From a development perspective, focus on the
"System/Application Security" and "Operations" domains.

- Secure SDLC Integration: You must formally integrate cybersecurity requirements into your project
  management methodology. Security is not an afterthought—it must be part of requirements gathering,
  design reviews, and change management processes.
- Secure Coding Standards: Mandate the use of recognized secure coding practices (e.g., OWASP Top 10
  and CWE Top 25) for all developers. Use static application security testing (SAST) tools in your
  CI/CD pipeline to enforce this.
- Vulnerability & Patch Management:
  - Conduct vulnerability scans on all environments before go-live.
  - If the client is Category A, you are required to perform regular penetration testing (you may need
    to outsource this to an NCA-approved entity). For Category B, it is recommended.
  - Ensure all underlying OS, middleware, and libraries are fully patched before deployment.
- Identity & Access Management (IAM):
  - Mandatory MFA: Enforce Multi-Factor Authentication for all administrative access and remote access
    to the system.
  - Principle of Least Privilege: Design your application's role-based access control (RBAC) strictly.
    No user or service account should have permissions beyond what is strictly necessary.
- Asset & Endpoint Management: Maintain a precise Software Bill of Materials (SBOM) for all open-source
  and third-party components used in your deliverables.

---

### Framework 2: DCC-1:2022 (Data Cybersecurity Controls)

This framework specifically governs how the application handles data from creation to destruction.

- Data Classification at the Code Level: Your system architecture must support data classification
  labels (e.g., Public, Internal, Confidential, Highly Confidential). The application logic should
  handle data differently based on these labels.
- Encryption Everywhere:
  - In Transit: Enforce TLS 1.2 or higher for all data transmitted between the client, backend, and
    external APIs.
  - At Rest: Implement database/disk encryption. For sensitive fields (e.g., PII), implement
    column-level encryption or application-layer encryption.
  - Key Management: Establish a secure Key Management System (KMS) for rotating and storing
    cryptographic keys—never hard-code keys in source code or config files.
- Audit Logging: Your application must log every access to sensitive data. The log must capture: Who
  (User ID), When (Timestamp), What (Data accessed/modified), and Action (Read, Update, Delete). These
  logs must be immutable and stored securely.
- Secure Data Disposal: Implement logic to securely overwrite or cryptographically erase data when a
  deletion request is triggered, ensuring the data is unrecoverable.

---

### Framework 3: PDPL (Saudi Personal Data Protection Law)

This is the overarching legal requirement for processing any personal data of Saudi residents.

- Privacy by Design: Embed privacy protections into your system architecture from day one. Do not
  collect or store personal data unless explicitly required by the business logic.
- Consent Management Module:
  - Build a user-facing mechanism to capture explicit, informed consent before collecting any personal
    data.
  - Track the consent record (timestamp, version of consent text). The system must allow users to
    withdraw consent easily, and you must code the backend to delete or anonymize their data upon
    withdrawal.
- Data Subject Rights (DSR) Implementation: Your API and frontend must support:
  - Right to Access: Allow users to export/download all their personal data stored in your system.
  - Right to Rectification: Allow users to correct inaccurate data.
  - Right to Erasure ("Right to be Forgotten"): Physically delete or fully anonymize the user's data
    upon verified request.
- Data Localization:
  - Critical: All personal data must be stored inside Saudi Arabia. Ensure your database servers,
    backup locations, and even logging systems do not replicate personal data to foreign regions.
- Records of Processing Activities (RoPA): Your design documentation must include a clear inventory of
  exactly what personal data flows through your system, why it is collected, and where it is stored.

---

### Framework 4: CCC-2:2024 (Cloud Cybersecurity Controls)

Applicable because you are using cloud-hosted components. As a Cloud Service Tenant (CST), you are
responsible for the security "in" the cloud.

- Zero Trust Architecture: Design your cloud network with micro-segmentation. Do not rely only on
  perimeter firewalls; restrict traffic between microservices.
- CI/CD Pipeline Security (DevSecOps):
  - Scan your Docker containers and Infrastructure-as-Code (IaC) templates (e.g., Terraform,
    CloudFormation) for misconfigurations before deployment.
  - Automate security testing in your build pipeline (SAST, DAST, and dependency scanning).
- Cloud IAM:
  - Never use root credentials for programmatic access. Use temporary credentials (STS) or service
    roles with minimal permissions.
  - Enable MFA for all developers accessing the cloud console.
- Cloud Data Protection:
  - Use the cloud provider's native KMS to manage encryption keys for databases and storage buckets.
  - Ensure cloud audit logs (e.g., AWS CloudTrail, Azure Monitor) are enabled, centralized, and
    retained according to the client's data retention policy.
- Vendor Compliance: Verify that your chosen cloud provider (e.g., AWS, Azure, GCP) operates within the
  Saudi Arabia Central Region and explicitly aligns with NCA CCC requirements. Include security
  responsibilities in your SLA with them.
