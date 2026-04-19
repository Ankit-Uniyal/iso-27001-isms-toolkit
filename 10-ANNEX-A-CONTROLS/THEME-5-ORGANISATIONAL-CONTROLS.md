# Annex A — Theme 5: Organisational Controls
## ISO/IEC 27001:2022 — Controls 5.1 to 5.37

**Document Reference:** NFS-IS-REG-015
**Version:** 1.0
**Effective Date:** 01 May 2026

> **IMPORTANT DISCLAIMER:** This document provides a reference guide and implementation notes for ISO/IEC 27001:2022 Annex A Theme 5 controls. It does NOT reproduce the text of the ISO standard. Control titles and numbers are used for reference only. For the normative control text, practitioners must consult the official ISO/IEC 27001:2022 and ISO/IEC 27002:2022 publications.

> **New controls introduced in ISO 27001:2022 (not in 2013):** 5.7 (Threat intelligence), 5.23 (IS for use of cloud services), 5.30 (ICT readiness for business continuity)

---

## Overview

Theme 5 contains **37 organisational controls** covering governance, policies, supplier management, incident management, and compliance. This is the largest theme in ISO 27001:2022 Annex A.

| Control Range | Count | Topics |
|---|---|---|
| 5.1–5.8 | 8 | Policies, roles, threat intelligence, contact with authorities |
| 5.9–5.14 | 6 | Asset management, asset use, information classification |
| 5.15–5.18 | 4 | Access control, identity management, authentication, access rights |
| 5.19–5.22 | 4 | Supplier security |
| 5.23 | 1 | Cloud services (NEW in 2022) |
| 5.24–5.28 | 5 | Incident management |
| 5.29–5.31 | 3 | Business continuity and legal compliance |
| 5.32–5.37 | 6 | Intellectual property, privacy, cryptography, IS reviews |

---

## Control Reference Table

| Control | Title | Type | NIST CSF | CIS v8 | NFS Status |
|---|---|---|---|---|---|
| 5.1 | Policies for information security | Preventive | GV.PO | 3.1 | ✅ Implemented |
| 5.2 | Information security roles and responsibilities | Preventive | GV.RR | 17.1 | ✅ Implemented |
| 5.3 | Segregation of duties | Preventive | PR.AC | 6.1 | ✅ Implemented |
| 5.4 | Management responsibilities | Preventive | GV.RR | 17.1 | ✅ Implemented |
| 5.5 | Contact with authorities | Preventive/Corrective | RS.CO | 17.6 | ✅ Implemented |
| 5.6 | Contact with special interest groups | Preventive | ID.RA | 17.6 | ✅ Implemented |
| 5.7 | Threat intelligence ⭐ NEW | Preventive | ID.RA | 7.7 | 🔄 In progress |
| 5.8 | Information security in project management | Preventive | PR.PS | 3.2 | ✅ Implemented |
| 5.9 | Inventory of information and other associated assets | Preventive | ID.AM | 1.1 | ✅ Implemented |
| 5.10 | Acceptable use of information and other associated assets | Preventive | PR.AT | 3.3 | ✅ Implemented |
| 5.11 | Return of assets | Preventive | PR.DS | 1.3 | ✅ Implemented |
| 5.12 | Classification of information | Preventive | PR.DS | 3.3 | ✅ Implemented |
| 5.13 | Labelling of information | Preventive | PR.DS | 3.3 | ✅ Implemented |
| 5.14 | Information transfer | Preventive | PR.DS | 9.2 | ✅ Implemented |
| 5.15 | Access control | Preventive | PR.AC | 5.1 | ✅ Implemented |
| 5.16 | Identity management | Preventive | PR.AC | 5.2 | ✅ Implemented |
| 5.17 | Authentication information | Preventive | PR.AC | 5.3 | ✅ Implemented |
| 5.18 | Access rights | Preventive | PR.AC | 5.4 | ✅ Implemented |
| 5.19 | Information security in supplier relationships | Preventive | GV.SC | 15.1 | ✅ Implemented |
| 5.20 | Addressing information security within supplier agreements | Preventive | GV.SC | 15.1 | ✅ Implemented |
| 5.21 | Managing information security in the ICT supply chain | Preventive | GV.SC | 15.2 | 🔄 In progress |
| 5.22 | Monitoring, review and change management of supplier services | Detective | GV.SC | 15.2 | ✅ Implemented |
| 5.23 | Information security for use of cloud services ⭐ NEW | Preventive | PR.PS | 12.1 | ✅ Implemented |
| 5.24 | Information security incident management planning and preparation | Corrective | RS.RP | 17.3 | ✅ Implemented |
| 5.25 | Assessment and decision on information security events | Detective | RS.AN | 17.4 | ✅ Implemented |
| 5.26 | Response to information security incidents | Corrective | RS.MI | 17.5 | ✅ Implemented |
| 5.27 | Learning from information security incidents | Corrective | RS.IM | 17.6 | ✅ Implemented |
| 5.28 | Collection of evidence | Corrective | RS.EV | 17.7 | ✅ Implemented |
| 5.29 | Information security during disruption | Preventive | PR.IP | 11.1 | ✅ Implemented |
| 5.30 | ICT readiness for business continuity ⭐ NEW | Preventive | PR.IP | 11.2 | ✅ Implemented |
| 5.31 | Legal, statutory, regulatory and contractual requirements | Preventive | GV.PO | 4.1 | ✅ Implemented |
| 5.32 | Intellectual property rights | Preventive | GV.PO | 4.2 | ✅ Implemented |
| 5.33 | Protection of records | Preventive | PR.DS | 3.4 | ✅ Implemented |
| 5.34 | Privacy and protection of PII | Preventive | PR.DS | 4.1 | ✅ Implemented |
| 5.35 | Independent review of information security | Detective | ID.IM | 18.2 | ✅ Implemented |
| 5.36 | Compliance with policies, rules and standards for information security | Detective | GV.PO | 4.3 | ✅ Implemented |
| 5.37 | Documented operating procedures | Preventive | PR.PS | 4.4 | ✅ Implemented |

---

## Implementation Notes by Control Group

### 5.1 — Policies for Information Security
**Purpose:** Establish a top-level policy framework that sets management intent for IS.
**Key deliverables:** Information Security Policy (approved by Board/top management); subsidiary policies covering key risk areas.
**NFS documents:** NFS-IS-POL-001 (IS Policy); NFS-IS-POL-002 (Leadership Commitment Statement)
**Audit evidence:** Approved policy documents; evidence of management sign-off; distribution records; staff acknowledgement log.

### 5.2 — Roles and Responsibilities
**Purpose:** Ensure IS responsibilities are assigned, understood, and communicated.
**Key deliverables:** RACI matrix; CISO/ISMS Manager role definitions; business unit IS responsibilities.
**NFS documents:** NFS-IS-POL-002 (Roles, Responsibilities, Authorities)
**Audit evidence:** Organisation chart; job descriptions with IS responsibilities; RACI matrix.

### 5.7 — Threat Intelligence ⭐ NEW IN 2022
**Purpose:** Collect, analyse, and act on information about information security threats to the organisation.
**Key deliverables:** Threat intelligence feed subscriptions; process for reviewing and acting on intelligence; integration with risk register.
**Implementation guidance:** Subscribe to NCSC alerts, FS-ISAC (financial sector), and relevant threat feeds. Assign responsibility for weekly review. Update risk register when new threats identified.
**NFS documents:** To be developed — Threat Intelligence Process (Q3 2026)
**Audit evidence:** Threat intelligence subscriptions; meeting minutes/records of threat review; risk register updates triggered by intelligence.

### 5.9 — Asset Inventory
**Purpose:** Identify information assets and maintain an accurate inventory.
**Key deliverables:** Documented asset register covering information assets, hardware, software, and services.
**NFS documents:** NFS-IS-REG-005 (Asset Register)
**Audit evidence:** Asset register with classification, owner, and location; process for adding/removing assets; evidence of annual review.

### 5.15–5.18 — Access Control
**Purpose:** Ensure access to information is controlled based on business need.
**Key deliverables:** Access control policy; access provisioning/deprovisioning process; privileged access management; periodic access reviews.
**NFS documents:** NFS-IS-POL-008 (Access Control Policy)
**Audit evidence:** Access control policy; user account listings; access review records; joiners/leavers records; MFA configuration evidence.

### 5.19–5.22 — Supplier Security
**Purpose:** Protect information accessed by or shared with suppliers.
**Key deliverables:** Supplier security policy; security requirements in contracts; ongoing monitoring programme.
**NFS documents:** NFS-IS-POL-011 (Supplier Security Policy); NFS-IS-REG-010 (Supplier Register)
**Audit evidence:** Supplier contracts with security clauses; DPAs; annual review records; supplier questionnaires.

### 5.23 — Cloud Services ⭐ NEW IN 2022
**Purpose:** Address IS requirements for cloud service acquisition, use, management, and exit.
**Key deliverables:** Cloud security policy or procedure; cloud service inventory; shared responsibility documentation.
**Implementation guidance:** Maintain a cloud service register. Document shared responsibility model for each CSP. Ensure data residency, encryption, and exit requirements are contractually agreed.
**Audit evidence:** Cloud service register; CSP contracts with security annexes; shared responsibility matrix; data residency evidence.

### 5.24–5.28 — Incident Management
**Purpose:** Enable consistent, effective response to IS incidents.
**Key deliverables:** Incident management policy/procedure; severity classification; response team; post-incident review process.
**NFS documents:** NFS-IS-PRO-004 (Incident Response Procedure); NFS-IS-REG-011 (Incident Log)
**Audit evidence:** Incident response procedure; incident log; PIR records; evidence of regulatory notifications.

### 5.29–5.30 — Business Continuity
**Purpose:** Maintain IS controls during disruption; ensure ICT systems can support business continuity.
**Key deliverables:** IS continuity plan; BC/DR test records; RTO/RPO definitions.
**NFS documents:** NFS-IS-PLAN-004 (Business Continuity IS Plan)
**Audit evidence:** BCP/IS continuity plan; DR test results; RTO/RPO documented and tested.

---

## Key Mapping: ISO 27001:2022 vs 2013 (Theme 5)

| 2022 Control | 2013 Equivalent | Change |
|---|---|---|
| 5.7 Threat intelligence | No equivalent | **NEW** |
| 5.23 Cloud services | No equivalent | **NEW** |
| 5.30 ICT readiness for BC | A.17.2.1 | Expanded significantly |
| 5.15 Access control | A.9.1.1 | Merged and updated |
| 5.24–5.28 Incident management | A.16.1.x | Restructured |

---

*This reference guide covers ISO/IEC 27001:2022 Annex A Theme 5 — Organisational Controls (5.1–5.37)*
*For normative control requirements, refer to ISO/IEC 27001:2022 and ISO/IEC 27002:2022*
