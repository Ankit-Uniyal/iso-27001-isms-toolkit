# Information Security Risk Register

## ISO/IEC 27001:2022 | Clause 6.1.2 & 8.2

**Document ID:** ISMS-RISKRG-001
**Version:** 1.0 | **Owner:** CISO / ISMS Manager | **Date:** ___ | **Review Cycle:** Quarterly

---

## Purpose

This register records all identified information security risks for assets within the ISMS scope. All entries must conform to the Risk Assessment Methodology (ISMS-RISK-001).

---

## Risk Register

### How to Use

For each row, complete all fields:
- **Risk ID:** Sequential (ISMS-RISK-XXX)
- **CIA Impact:** Confidentiality (C), Integrity (I), Availability (A), or combination
- **Likelihood / Impact:** Score 1–5 per methodology
- **Risk Score:** Likelihood x Impact
- **Rating:** LOW / MEDIUM / HIGH / CRITICAL

---

### Active Risks

| Risk ID | Asset | Threat | Vulnerability | CIA | Likelihood | Impact | Inherent Score | Rating | Current Controls | Residual Likelihood | Residual Impact | Residual Score | Residual Rating | Treatment | Risk Owner | Review Date | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ISMS-RISK-001 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | Treat / Accept / Transfer / Avoid | ___ | ___ | Active |
| ISMS-RISK-002 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | Active |
| ISMS-RISK-003 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | Active |

---

## Common IS Risk Scenarios (Reference)

Use these as starting points when identifying risks for your specific assets:

| Threat Category | Example Threat | Common Vulnerabilities | Typical CIA Impact |
|---|---|---|---|
| Malware / Ransomware | Ransomware encrypts file servers | Unpatched systems; poor email filtering; lack of MFA | C, I, A |
| Phishing / Social Engineering | Credentials harvested via phishing | Insufficient awareness training; no MFA | C, I |
| Insider Threat | Disgruntled employee exfiltrates data | Excessive access rights; lack of monitoring | C, I |
| Unauthorised Access | External attacker gains network access via VPN | Weak authentication; unpatched VPN; no network segmentation | C, I, A |
| Data Leakage | Sensitive data emailed to wrong recipient | No DLP; classification gaps; human error | C |
| Supplier Breach | Third-party breached; customer data exposed | Insufficient supplier IS assessment; excessive third-party access | C |
| Physical Theft | Laptop stolen from employee's car | No full-disk encryption; no screen lock | C |
| Cloud Misconfiguration | S3 bucket publicly accessible | Poor cloud configuration management; lack of CSPM | C |
| Denial of Service | DDoS attack on web application | No DDoS protection; single point of failure | A |
| Vulnerability Exploitation | CVE exploited in unpatched web server | Slow patching cycle; no vulnerability scanning | C, I, A |
| Backup Failure | Backups not recoverable when needed | Backups untested; single backup location | A |
| Data Centre Outage | Power failure takes down servers | No UPS; no generator; no DR site | A |
| Account Compromise | Admin credentials reused and exposed | Password reuse; lack of PAM | C, I, A |
| Software Supply Chain | Malicious code in third-party library | No software composition analysis; no SBOM | C, I |
| Regulatory Non-Compliance | ICO penalty for data breach | GDPR gaps; inadequate DPIA process | C, I (reputational) |

---

## Risk Heat Map

| | **Impact 1** | **Impact 2** | **Impact 3** | **Impact 4** | **Impact 5** |
|---|---|---|---|---|---|
| **Likelihood 5** | 🟡 5 | 🟡 10 | 🔴 15 | 🔴 20 | 🔴 25 |
| **Likelihood 4** | 🟢 4 | 🟡 8 | 🔴 12 | 🔴 16 | 🔴 20 |
| **Likelihood 3** | 🟢 3 | 🟡 6 | 🟡 9 | 🔴 12 | 🔴 15 |
| **Likelihood 2** | 🟢 2 | 🟢 4 | 🟡 6 | 🟡 8 | 🟡 10 |
| **Likelihood 1** | 🟢 1 | 🟢 2 | 🟢 3 | 🟢 4 | 🟡 5 |

🟢 LOW (1–3) | 🟡 MEDIUM (4–9) | 🔴 HIGH/CRITICAL (10–25)

---

## Risk Register Summary

| Risk Rating | Count | % of Total |
|---|---|---|
| CRITICAL (13–25) | | |
| HIGH (7–12) | | |
| MEDIUM (4–6) | | |
| LOW (1–3) | | |
| **Total** | | 100% |

---

## Review and Approval

| Review Date | Reviewer | Key Changes | Approved By |
|---|---|---|---|
| | | | |

---

*ISO/IEC 27001:2022 ISMS Toolkit | Information Security Risk Register | Clause 6.1.2 | See root README.md for full index*
