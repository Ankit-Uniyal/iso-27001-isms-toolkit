# ISMS Continual Improvement Log
## ISO/IEC 27001:2022 — Clause 10.2

**Organisation:** Nexus Financial Services Ltd (NFS)
**Document Reference:** NFS-IS-REG-013
**Version:** 1.0
**Effective Date:** 01 May 2026
**Review Date:** 01 May 2027
**Owner:** ISMS Manager
**Approved By:** Chief Information Security Officer

---

## 1. Purpose

This log records opportunities for improvement and improvement initiatives identified through ISMS operation, monitoring, audits, management reviews, incidents, and stakeholder feedback. It supports Clause 10.2 (Continual improvement) of ISO/IEC 27001:2022.

This log is distinct from the NCR / Corrective Action Register (NFS-IS-REG-012), which records nonconformities. This log captures proactive improvements that are not necessarily triggered by a failure.

---

## 2. Improvement Source Categories

| Code | Source |
|---|---|
| MR | Management Review output |
| AUD | Internal or external audit observation |
| INC | Lesson learned from security incident |
| KPI | KPI or metric below target |
| RISK | Risk assessment or treatment review |
| STAFF | Staff suggestion or awareness feedback |
| TECH | Technology change or new capability |
| REG | Regulatory guidance or industry benchmark |
| SIM | Phishing simulation or tabletop exercise outcome |
| EXT | External benchmarking or peer organisation learning |

---

## 3. Priority Classification

| Priority | Definition | Target Implementation |
|---|---|---|
| High | Significant improvement to ISMS effectiveness or risk reduction | Within 90 days |
| Medium | Moderate improvement; enhances control effectiveness | Within 180 days |
| Low | Minor enhancement; good practice | Within 12 months |

---

## 4. Improvement Log — FY 2026

| ID | Date Identified | Source | Description of Improvement Opportunity | Priority | Owner | Target Date | Status | Completion Date | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| IMP-2026-001 | 15 Jan 2026 | MR | Implement automated certificate expiry monitoring — currently manual tracking leads to near-misses | High | IT Security | 31 Mar 2026 | ✅ Complete | 20 Mar 2026 | Deployed Cert-Manager alerts; 60-day advance warnings now automated |
| IMP-2026-002 | 15 Jan 2026 | KPI | Phishing click rate at 8.2% vs 5% target — deploy targeted micro-learning for repeat clickers | High | ISMS Manager | 30 Apr 2026 | ✅ Complete | 28 Apr 2026 | KnowBe4 automated remedial training deployed; click rate reduced to 6.1% |
| IMP-2026-003 | 20 Jan 2026 | AUD | Gap assessment showed 13% of SoA controls still not implemented — create quarterly SoA review cadence | Medium | ISMS Manager | 30 Jun 2026 | 🔄 In Progress | — | Q1 review completed; 87% implemented (up from 85%) |
| IMP-2026-004 | 05 Feb 2026 | INC | INC-2026-001 showed SIEM alert rule gaps for lateral movement detection — review and tune SIEM rules | High | IS Analyst | 28 Feb 2026 | ✅ Complete | 25 Feb 2026 | 14 new detection rules added; 3 false-positive rules tuned |
| IMP-2026-005 | 10 Feb 2026 | TECH | Azure AD Conditional Access available — implement to replace legacy VPN-only access for cloud apps | Medium | IT Security | 30 Sep 2026 | 🔄 In Progress | — | Pilot running with IT team; full rollout planned Aug 2026 |
| IMP-2026-006 | 01 Mar 2026 | REG | NCSC advisory on MFA fatigue attacks — review and harden MFA implementation | High | IT Security | 31 Mar 2026 | ✅ Complete | 29 Mar 2026 | Number matching enabled in Microsoft Authenticator; push notifications restricted |
| IMP-2026-007 | 15 Mar 2026 | SIM | Tabletop exercise revealed unclear comms chain for P1 incidents involving third parties — update IR procedure | Medium | ISMS Manager | 30 Jun 2026 | 🔄 In Progress | — | IR procedure update drafted; under CISO review |
| IMP-2026-008 | 01 Apr 2026 | STAFF | Staff survey feedback: confusion about what constitutes a reportable incident — improve guidance | Low | ISMS Manager | 31 Jul 2026 | 📋 Planned | — | Quick reference card to be added to intranet |
| IMP-2026-009 | 10 Apr 2026 | RISK | 2 risk treatment actions overdue — implement monthly risk treatment plan checkpoint | Medium | ISMS Manager | 31 May 2026 | 📋 Planned | — | Monthly review calendar created |
| IMP-2026-010 | 15 Apr 2026 | EXT | ISO 27001:2022 peer benchmarking shows NFS lacks formal threat intelligence programme — scope and plan | Medium | CISO | 31 Dec 2026 | 📋 Planned | — | CISO to evaluate threat intel feeds; budget request raised |

**Status Key:** ✅ Complete | 🔄 In Progress | 📋 Planned | ⏸️ On Hold | ❌ Cancelled

---

## 5. Improvement Log Summary

| Status | Count |
|---|---|
| Complete | 4 |
| In Progress | 3 |
| Planned | 3 |
| On Hold | 0 |
| Cancelled | 0 |
| **Total FY 2026** | **10** |

---

## 6. Completed Improvements — Impact Assessment

| ID | Improvement | Measurable Outcome |
|---|---|---|
| IMP-2026-001 | Certificate expiry monitoring automated | Zero cert expiry incidents since deployment |
| IMP-2026-002 | Targeted phishing remedial training | Click rate reduced from 8.2% to 6.1% (target < 5%) |
| IMP-2026-004 | SIEM rule enhancement for lateral movement | Detection coverage increased; 0 missed lateral movement events in next 60 days |
| IMP-2026-006 | MFA hardening (MFA fatigue prevention) | Zero successful MFA fatigue attacks since deployment |

---

## 7. Register Maintenance

This register is updated monthly by the ISMS Manager, following each management review, following each internal audit, and following significant security incidents. Completed improvements with measurable outcomes are reported to the CISO and included in the annual management review.

---

*Nexus Financial Services Ltd | NFS-IS-REG-013 v1.0*
*ISO/IEC 27001:2022 Clause 10.2 — Continual Improvement*
