# Statement of Applicability — Excerpt (Theme 5: Organisational Controls)
## Nexus Financial Services Ltd — Worked Example

> **FICTIONAL REFERENCE ONLY — For educational purposes only.**
> This is an excerpt from the NFS Statement of Applicability showing how Theme 5 Organisational Controls are documented. It illustrates the level of detail expected in a real SoA.

**Document Reference:** NFS-IS-REG-007 (Excerpt)
**Full SoA Reference:** See 05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md for all 93 controls
**Version:** 1.0
**Effective Date:** 01 May 2026
**ISMS Manager:** Rachel Ford | **CISO:** Tom Briggs

---

## How to Read This SoA Excerpt

Each control entry shows:
- **Applicable:** Yes / No (with justification if No)
- **Implementation Status:** Implemented / Partially Implemented / Planned / Not Started
- **Justification for Inclusion/Exclusion:** Business reason
- **Implementation Notes:** How the control is implemented at NFS
- **Evidence Reference:** Document or system that evidences implementation

---

## Theme 5 — Organisational Controls (5.1–5.37) — NFS SoA Excerpt

### 5.1 — Policies for Information Security

| Field | Detail |
|---|---|
| **Applicable** | ✅ Yes |
| **Justification** | Mandatory for ISMS; required by ISO 27001:2022 Clause 5.2 |
| **Implementation Status** | ✅ Implemented |
| **Implementation Notes** | NFS Information Security Policy (NFS-IS-POL-001) approved by Board 01 May 2026. Subsidiary policies cover access control, cryptography, physical security, AUP, and supplier security. All policies published on NFS intranet. Annual review cycle in place. |
| **Evidence** | NFS-IS-POL-001; Board minutes 01 May 2026; intranet publication record |

### 5.7 — Threat Intelligence ⭐ NEW IN 2022

| Field | Detail |
|---|---|
| **Applicable** | ✅ Yes |
| **Justification** | NFS is an FCA-regulated financial services firm handling sensitive customer data; threat intelligence is essential for proactive risk management |
| **Implementation Status** | 🔄 Partially Implemented |
| **Implementation Notes** | NCSC Early Warning Service subscription active. FS-ISAC membership pending approval (Q3 2026). Informal review of NCSC alerts weekly by IS Analyst. Formal threat intelligence process to be documented by Q3 2026. |
| **Evidence** | NCSC subscription confirmation; IS Analyst weekly review log (informal); CI-2026 improvement tracker |
| **Gap / Action** | Formal threat intelligence procedure to be developed. Owner: ISMS Manager. Target: 30 Sep 2026. |

### 5.19 — Information Security in Supplier Relationships

| Field | Detail |
|---|---|
| **Applicable** | ✅ Yes |
| **Justification** | NFS uses 180+ third-party suppliers including critical cloud services, payment processors, and managed services; supplier risk is a top-5 ISMS risk |
| **Implementation Status** | ✅ Implemented |
| **Implementation Notes** | Supplier Security Policy (NFS-IS-POL-011) in place. Supplier Security Questionnaire (NFS-IS-TMP-005) completed for all Tier 1/2 suppliers. Annual review cycle established. 23 Tier 1 suppliers reviewed in 2025/26. |
| **Evidence** | NFS-IS-POL-011; Supplier Register (NFS-IS-REG-010); completed questionnaires on file |

### 5.23 — Information Security for Use of Cloud Services ⭐ NEW IN 2022

| Field | Detail |
|---|---|
| **Applicable** | ✅ Yes |
| **Justification** | NFS uses Microsoft Azure (Online Banking), Microsoft 365, Salesforce, and Workday as cloud services hosting customer and employee data |
| **Implementation Status** | ✅ Implemented |
| **Implementation Notes** | Cloud services register maintained (7 CSPs). Shared responsibility model documented for Azure UK South and M365. Data residency confirmed as UK for all services hosting personal data. CSP contracts include security annexes and DPAs. Exit strategy documented for Azure (Online Banking). Salesforce and Workday: annual security review completed. |
| **Evidence** | Cloud services register; CSP contracts with security annexes; shared responsibility documentation; data residency confirmations; DPAs |

### 5.24 — IS Incident Management Planning and Preparation

| Field | Detail |
|---|---|
| **Applicable** | ✅ Yes |
| **Justification** | Mandatory for ISMS; required for FCA operational resilience obligations |
| **Implementation Status** | ✅ Implemented |
| **Implementation Notes** | Incident Response Procedure (NFS-IS-PRO-004) approved and published. Severity classification (P1–P4) defined. Incident response team roles assigned (CISO, IT Security, ISMS Manager, DPO, Legal). Annual tabletop exercise planned (Oct 2026). SIEM alerting integrated with incident workflow. |
| **Evidence** | NFS-IS-PRO-004; IS Incident Log (NFS-IS-REG-011); SIEM alert configuration; tabletop exercise plan |

### 5.29 — Information Security During Disruption

| Field | Detail |
|---|---|
| **Applicable** | ✅ Yes |
| **Justification** | NFS provides critical financial services; continuity of IS controls during disruption is a regulatory requirement (FCA PS21/3) |
| **Implementation Status** | ✅ Implemented |
| **Implementation Notes** | IS continuity requirements integrated into Business Continuity Plan (NFS-IS-PLAN-004). DR failover tested annually. Break-glass access procedures documented. SIEM DR capability tested bi-annually. RTO/RPO defined for all critical systems. |
| **Evidence** | NFS-IS-PLAN-004; DR test records; break-glass access procedure; RTO/RPO documentation |

### 5.30 — ICT Readiness for Business Continuity ⭐ NEW IN 2022

| Field | Detail |
|---|---|
| **Applicable** | ✅ Yes |
| **Justification** | NFS is critically dependent on ICT for all banking operations; ICT readiness is essential for meeting FCA operational resilience requirements |
| **Implementation Status** | ✅ Implemented |
| **Implementation Notes** | ICT continuity strategy defined in BC IS Plan. Core Banking: active-passive DR (RTO 4 hours). Payment Gateway: automated failover (RTO 2 hours). Annual DR test completed Feb 2026 — all critical systems failed over within RTO. Backup restoration tested quarterly. |
| **Evidence** | NFS-IS-PLAN-004; DR test report Feb 2026; backup restoration test records; RTO achievement records |

---

## Key Statistics — NFS SoA at a Glance

| Theme | Total Controls | Applicable | Not Applicable | Implemented | Partially | Planned |
|---|---|---|---|---|---|---|
| 5 — Organisational | 37 | 37 | 0 | 34 | 3 | 0 |
| 6 — People | 8 | 8 | 0 | 8 | 0 | 0 |
| 7 — Physical | 14 | 13 | 1* | 13 | 0 | 0 |
| 8 — Technological | 34 | 34 | 0 | 29 | 5 | 0 |
| **Total** | **93** | **92** | **1** | **84** | **8** | **0** |

*7.6 (Working in secure areas) — N/A for branch network locations that have no secure area classification above Zone 1.

**Overall SoA implementation rate: 91.3% (84/92 applicable controls fully implemented)**

---

*FICTIONAL REFERENCE ONLY — Nexus Financial Services Ltd does not exist.*
*For the full 93-control SoA, see: 05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md*
