# Information Security KPI and Metrics Dashboard
## ISO/IEC 27001:2022 — Clause 9.1

**Organisation:** Nexus Financial Services Ltd (NFS)
**Document Reference:** NFS-IS-REG-014
**Version:** 1.0
**Effective Date:** 01 May 2026
**Review Date:** 01 May 2027
**Owner:** ISMS Manager
**Reported To:** CISO, Board Risk Committee (quarterly)

---

## 1. Purpose

This dashboard tracks NFS's information security performance against defined Key Performance Indicators (KPIs) and metrics. It supports Clause 9.1 (Monitoring, measurement, analysis, and evaluation) of ISO/IEC 27001:2022 and provides evidence for management reviews.

---

## 2. IS KPI Summary — FY 2026

### 2.1 Dashboard Overview (as at 01 May 2026)

| # | KPI | Target | Current | Trend | Status |
|---|---|---|---|---|---|
| 1 | IS Awareness Training Completion | ≥ 95% | 98% | ↑ | 🟢 On Target |
| 2 | Phishing Simulation Click Rate | < 5% | 6.1% | ↓ (improving) | 🟡 Near Target |
| 3 | Critical Patch Deployment (within 72h) | ≥ 98% | 97% | → | 🟡 Near Target |
| 4 | High Patch Deployment (within 14 days) | ≥ 95% | 96% | ↑ | 🟢 On Target |
| 5 | Mean Time to Detect (MTTD) — P1/P2 | < 4 hours | 2.8 hours | ↓ | 🟢 On Target |
| 6 | Mean Time to Respond (MTTR) — P1/P2 | < 24 hours | 18 hours | ↓ | 🟢 On Target |
| 7 | IS Incidents (P1/P2) per Quarter | 0 P1; ≤ 2 P2 | 0 P1, 1 P2 | → | 🟢 On Target |
| 8 | Open Critical/High Risk Register Items | < 10 | 7 | ↓ | 🟢 On Target |
| 9 | Overdue Risk Treatment Actions | 0 | 2 | ↑ | 🔴 Off Target |
| 10 | Supplier Security Reviews Completed | 100% by due date | 90% | → | 🟡 Near Target |
| 11 | Internal Audit Findings (Critical) | 0 | 0 | → | 🟢 On Target |
| 12 | Internal Audit Findings (Major) Closed | 100% within 90 days | 85% | ↓ | 🟡 Near Target |
| 13 | Access Reviews Completed on Schedule | 100% | 100% | → | 🟢 On Target |
| 14 | SoA Control Implementation (% Implemented) | ≥ 90% | 87% | ↑ | 🟡 Near Target |
| 15 | Management Review Conducted (Annual) | 1 per year | 1 (Dec 2025) | → | 🟢 On Target |

**Legend:** 🟢 On Target | 🟡 Near Target (within 5%) | 🔴 Off Target

---

## 3. KPI Detail — Definitions and Measurement

### 3.1 Training and Awareness

| KPI | Definition | Measurement Method | Frequency | Data Source |
|---|---|---|---|---|
| IS Awareness Training Completion | % of all staff with completed annual IS refresher | LMS completion report | Monthly | Learning Management System |
| Phishing Simulation Click Rate | % of staff who click on simulated phishing emails | Phishing simulation platform report | Per simulation (quarterly) | KnowBe4 / Proofpoint |
| AUP Acknowledgement Rate | % of staff with signed AUP for current year | Electronic signature records | Annually (January) | SharePoint |

### 3.2 Vulnerability and Patch Management

| KPI | Definition | Measurement Method | Frequency | Data Source |
|---|---|---|---|---|
| Critical Patch Deployment Rate | % of critical CVEs (CVSS ≥ 9.0) patched within 72 hours of release | Vulnerability scanner + CMDB | Weekly | Qualys / Tenable |
| High Patch Deployment Rate | % of high CVEs (CVSS 7.0–8.9) patched within 14 days | Vulnerability scanner + CMDB | Weekly | Qualys / Tenable |
| Outstanding Critical Vulnerabilities | Count of unmitigated critical vulnerabilities > 72 hours old | Vulnerability scanner | Weekly | Qualys / Tenable |

### 3.3 Incident Management

| KPI | Definition | Measurement Method | Frequency | Data Source |
|---|---|---|---|---|
| MTTD (Mean Time to Detect) | Average time from incident occurrence to detection for P1/P2 | Incident log timestamp analysis | Monthly | ServiceNow / IS Incident Log |
| MTTR (Mean Time to Respond/Resolve) | Average time from detection to resolution for P1/P2 | Incident log timestamp analysis | Monthly | ServiceNow / IS Incident Log |
| P1/P2 Incident Count | Number of confirmed Critical and High incidents per quarter | Incident log count | Quarterly | IS Incident Log (NFS-IS-REG-011) |
| Repeat Incidents (same root cause) | Count of incidents with same root cause as prior incident | Root cause analysis comparison | Quarterly | IS Incident Log |

### 3.4 Risk Management

| KPI | Definition | Measurement Method | Frequency | Data Source |
|---|---|---|---|---|
| Open Critical/High Risk Register Items | Count of risks rated Critical or High with no accepted treatment | Risk register query | Monthly | IS Risk Register (NFS-IS-REG-006) |
| Overdue Risk Treatment Actions | Count of risk treatment actions past agreed due date | Risk treatment plan review | Monthly | Risk Treatment Plan (NFS-IS-PLAN-005) |
| Risk Register Review Frequency | Number of formal risk register reviews conducted | ISMS Manager log | Quarterly | Risk register version history |

### 3.5 Compliance and Controls

| KPI | Definition | Measurement Method | Frequency | Data Source |
|---|---|---|---|---|
| SoA Control Implementation | % of applicable Annex A controls marked as Implemented in SoA | SoA review | Quarterly | Statement of Applicability |
| Supplier Reviews Completed | % of Tier 1/2 suppliers with completed annual security review by due date | Supplier register | Quarterly | Supplier Register (NFS-IS-REG-010) |
| Access Reviews Completed | % of scheduled access reviews completed on time | IT Manager confirmation | Quarterly | Access review records |

### 3.6 Audit Performance

| KPI | Definition | Measurement Method | Frequency | Data Source |
|---|---|---|---|---|
| Critical Audit Findings | Count of Critical (immediate action required) findings | Internal audit reports | Per audit | Audit reports |
| Major Finding Closure Rate | % of Major audit findings closed within 90 days | NCR register review | Monthly | NCR Register (NFS-IS-REG-012) |
| Audit Programme Completion | % of planned annual audits completed on schedule | Audit programme tracker | Quarterly | Internal Audit Programme |

---

## 4. Monthly Metrics Trend — FY 2026

### 4.1 Phishing Click Rate Trend

| Month | Emails Sent | Click Rate | Trend |
|---|---|---|---|
| February 2026 (Sim #1) | 3,200 | 8.2% | Baseline |
| April 2026 (Sim #2) | 3,200 | 6.1% | ↓ Improving |
| July 2026 (Sim #3) | 3,200 | TBD | — |
| October 2026 (Sim #4) | 3,200 | TBD | — |
| **Target** | | **< 5%** | |

### 4.2 Incident Volume Trend

| Quarter | P1 | P2 | P3 | P4 | Total |
|---|---|---|---|---|---|
| Q1 2026 (Jan–Mar) | 0 | 1 | 4 | 12 | 17 |
| Q2 2026 (Apr–Jun) | 0 | 0 | 3 | 9 | 12 |
| Q3 2026 | TBD | TBD | TBD | TBD | TBD |
| Q4 2026 | TBD | TBD | TBD | TBD | TBD |

### 4.3 Risk Register Status Trend

| Quarter | Critical Risks Open | High Risks Open | Overdue Actions |
|---|---|---|---|
| Q4 2025 (baseline) | 2 | 9 | 5 |
| Q1 2026 | 1 | 8 | 3 |
| Q2 2026 | 0 | 7 | 2 |
| Target (Year-End) | 0 | ≤ 5 | 0 |

---

## 5. IS Objectives Progress — FY 2026

| Objective | Target | Q1 Status | Q2 Status | On Track? |
|---|---|---|---|---|
| Reduce phishing click rate to < 5% | < 5% by Dec 2026 | 8.2% | 6.1% | 🟡 |
| Achieve SoA 93% implemented | 93% by Dec 2026 | 85% | 87% | 🟡 |
| Zero P1 incidents | 0 for FY 2026 | ✅ 0 | ✅ 0 | 🟢 |
| ISO 27001 surveillance audit passed | Pass by Oct 2026 | Prep in progress | Prep in progress | 🟢 |
| All Tier 1 supplier reviews completed | 100% by Sep 2026 | 60% | 80% | 🟡 |
| Critical patch rate ≥ 98% | ≥ 98% sustained | 97% | 97% | 🟡 |

---

## 6. Dashboard Reporting Cadence

| Report | Audience | Frequency | Prepared By |
|---|---|---|---|
| IS Metrics Summary | CISO | Monthly | ISMS Manager |
| IS Performance Dashboard | Board Risk Committee | Quarterly | CISO |
| IS KPI Report | Management Review | Annual | ISMS Manager |

---

*Nexus Financial Services Ltd | NFS-IS-REG-014 v1.0*
*ISO/IEC 27001:2022 Clause 9.1 — Monitoring, measurement, analysis and evaluation*
