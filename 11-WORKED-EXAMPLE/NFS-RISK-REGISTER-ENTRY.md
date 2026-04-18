# IS Risk Register — Worked Examples

## ISO/IEC 27001:2022 | Clause 6.1.2 | FICTIONAL REFERENCE ONLY

> **FICTIONAL:** All content relates to fictional Nexus Financial Services Ltd. Educational use only.

---

## Risk Entry 1: Ransomware — Score 20 CRITICAL → 10 HIGH

**Asset:** Core banking (T24); 860K customer records | **Threat:** Ransomware via phishing/RDP

**Controls:** Email filtering, CrowdStrike EDR, MFA, network segmentation, immutable backups, PAM, phishing simulation (click rate 3.2%), patching 99.1%, ransomware IRP.

**Treatment:** SOAR (Q3 2025), purple team exercise (Q2 2025).

---

## Risk Entry 2: Insider Threat — Score 15 CRITICAL → 8 HIGH

**Asset:** Customer DB; HR records | **Threat:** Privileged user data exfiltration

**Controls:** RBAC, PAM, session recording, background checks, DLP (partial), UEBA (partial).

**Treatment:** Complete DLP + UEBA deployment (Q2-Q3 2025).

---

## Risk Entry 3: Cloud Misconfiguration — Score 12 HIGH → 6 MEDIUM (within appetite)

**Asset:** AWS S3 storage | **Threat:** Accidental public bucket exposure

**Controls:** CSPM (Wiz.io 94%), S3 Block Public Access, IaC scanning (Checkov), quarterly IAM reviews, CloudTrail, AES-256.

---

*ISO/IEC 27001:2022 ISMS Toolkit | Worked Example — Clause 6.1.2 | See root README.md for full index*
