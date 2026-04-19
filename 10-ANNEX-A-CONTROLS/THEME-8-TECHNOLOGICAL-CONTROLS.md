# Annex A — Theme 8: Technological Controls
## ISO/IEC 27001:2022 — Controls 8.1 to 8.34

**Document Reference:** NFS-IS-REG-018
**Version:** 1.0
**Effective Date:** 01 May 2026

> **IMPORTANT DISCLAIMER:** This document provides a reference guide and implementation notes for ISO/IEC 27001:2022 Annex A Theme 8 controls. It does NOT reproduce the text of the ISO standard. Control titles and numbers are used for reference only. For the normative control text, practitioners must consult the official ISO/IEC 27001:2022 and ISO/IEC 27002:2022 publications.

> **New controls introduced in 2022:** 8.9 (Configuration management), 8.10 (Information deletion), 8.11 (Data masking), 8.12 (Data leakage prevention), 8.16 (Monitoring activities), 8.23 (Web filtering), 8.28 (Secure coding)

---

## Overview

Theme 8 contains **34 technological controls** — the largest group of new controls introduced in the 2022 revision. These controls cover endpoint security, identity management, vulnerability management, data protection, logging, encryption, and secure development.

| Control Range | Topics |
|---|---|
| 8.1–8.8 | User endpoints, privileged access, access restrictions, authentication, capacity |
| 8.9–8.13 | Configuration, deletion, data masking, DLP, backup ⭐ new controls |
| 8.14–8.17 | Redundancy, logging, monitoring, clock synchronisation |
| 8.18–8.23 | Privileged utilities, software installation, network security, web filtering |
| 8.24–8.28 | Cryptography, SDLC, secure configuration, vulnerability management, secure coding |
| 8.29–8.34 | Security testing, outsourced development, separation, DR, audit tools |

---

## Control Reference Table

| Control | Title | Type | NIST CSF | New in 2022? | NFS Status |
|---|---|---|---|---|---|
| 8.1 | User endpoint devices | Preventive | PR.AC | No | ✅ Implemented |
| 8.2 | Privileged access rights | Preventive | PR.AC | No | ✅ Implemented |
| 8.3 | Information access restriction | Preventive | PR.AC | No | ✅ Implemented |
| 8.4 | Access to source code | Preventive | PR.DS | No | ✅ Implemented |
| 8.5 | Secure authentication | Preventive | PR.AC | No | ✅ Implemented |
| 8.6 | Capacity management | Preventive | PR.DS | No | ✅ Implemented |
| 8.7 | Protection against malware | Preventive | PR.DS | No | ✅ Implemented |
| 8.8 | Management of technical vulnerabilities | Preventive | ID.RA | No | ✅ Implemented |
| 8.9 | Configuration management | Preventive | PR.IP | ⭐ YES | 🔄 In progress |
| 8.10 | Information deletion | Preventive | PR.DS | ⭐ YES | ✅ Implemented |
| 8.11 | Data masking | Preventive | PR.DS | ⭐ YES | 🔄 In progress |
| 8.12 | Data leakage prevention | Preventive | PR.DS | ⭐ YES | 🔄 In progress |
| 8.13 | Information backup | Preventive | PR.IP | No | ✅ Implemented |
| 8.14 | Redundancy of information processing facilities | Preventive | PR.IP | No | ✅ Implemented |
| 8.15 | Logging | Detective | DE.AE | No | ✅ Implemented |
| 8.16 | Monitoring activities | Detective | DE.CM | ⭐ YES | ✅ Implemented |
| 8.17 | Clock synchronisation | Preventive | PR.PS | No | ✅ Implemented |
| 8.18 | Use of privileged utility programs | Preventive | PR.AC | No | ✅ Implemented |
| 8.19 | Installation of software on operational systems | Preventive | PR.PS | No | ✅ Implemented |
| 8.20 | Networks security | Preventive | PR.IR | No | ✅ Implemented |
| 8.21 | Security of network services | Preventive | PR.IR | No | ✅ Implemented |
| 8.22 | Segregation of networks | Preventive | PR.IR | No | ✅ Implemented |
| 8.23 | Web filtering | Preventive | PR.AC | ⭐ YES | ✅ Implemented |
| 8.24 | Use of cryptography | Preventive | PR.DS | No | ✅ Implemented |
| 8.25 | Secure development life cycle | Preventive | PR.PS | No | ✅ Implemented |
| 8.26 | Application security requirements | Preventive | PR.PS | No | ✅ Implemented |
| 8.27 | Secure system architecture and engineering principles | Preventive | PR.IP | No | ✅ Implemented |
| 8.28 | Secure coding | Preventive | PR.PS | ⭐ YES | 🔄 In progress |
| 8.29 | Security testing in development and acceptance | Detective | DE.CM | No | ✅ Implemented |
| 8.30 | Outsourced development | Preventive | GV.SC | No | ✅ Implemented |
| 8.31 | Separation of development, test and production environments | Preventive | PR.IP | No | ✅ Implemented |
| 8.32 | Change management | Preventive | PR.IP | No | ✅ Implemented |
| 8.33 | Test information | Preventive | PR.DS | No | ✅ Implemented |
| 8.34 | Protection of information systems during audit testing | Preventive | PR.IP | No | ✅ Implemented |

---

## Implementation Notes — New Controls (2022 Only)

### 8.9 — Configuration Management ⭐ NEW
**Purpose:** Establish, document, implement, and monitor configurations of hardware, software, services, and networks.
**Key requirements:** Configuration baseline for all critical systems; CMDB or equivalent; automated compliance checking; deviation approval process.
**Implementation guidance:** Implement a Configuration Management Database (CMDB). Define secure baselines (CIS Benchmarks recommended). Use automated configuration compliance tools (e.g., Microsoft Endpoint Manager, Chef, Puppet, Ansible).
**Audit evidence:** CMDB; configuration baselines; compliance scan results; deviation approvals.

### 8.10 — Information Deletion ⭐ NEW
**Purpose:** Ensure information is deleted when no longer required to prevent unnecessary exposure.
**Key requirements:** Data retention and deletion policy; deletion schedules; secure deletion for sensitive data; deletion records.
**Implementation guidance:** Implement data lifecycle management. Map retention periods to UK GDPR and legal requirements. Automate deletion where feasible. Use certified deletion tools for Confidential/Highly Restricted data.
**Audit evidence:** Data retention policy; deletion schedule; automated deletion records; secure deletion tool certificates.

### 8.11 — Data Masking ⭐ NEW
**Purpose:** Protect sensitive data through masking, tokenisation, or other obfuscation techniques.
**Key requirements:** Identification of data requiring masking; masking applied in non-production environments; tokenisation for payment card data.
**Implementation guidance:** Ensure PAN (Primary Account Number) data is masked in all non-production environments. Implement tokenisation for card data (PCI DSS requirement). Apply data masking to PII in test/dev datasets.
**Audit evidence:** Data masking policy; evidence of masked data in test environments; PCI DSS tokenisation evidence.

### 8.12 — Data Leakage Prevention ⭐ NEW
**Purpose:** Detect and prevent unauthorised disclosure of sensitive information.
**Key requirements:** DLP controls on email, endpoint, and network; DLP policy defining sensitive data types; monitoring and alerting; response process for DLP events.
**Implementation guidance:** Implement DLP solutions covering email, endpoint, web, and cloud. Define policies for PII, payment card data, and confidential business information. Align DLP rules with data classification scheme.
**Audit evidence:** DLP solution configuration; DLP policy; DLP alert/event logs; response records.

### 8.16 — Monitoring Activities ⭐ NEW
**Purpose:** Monitor networks, systems, and applications to detect anomalous behaviour and security events.
**Key requirements:** Defined monitoring scope and objectives; SIEM or equivalent; anomaly detection; review of monitoring data; escalation process for alerts.
**Implementation guidance:** Deploy SIEM covering all critical systems. Define use cases and alert thresholds. Assign SOC responsibility (internal or contracted). Review SIEM alerts daily; document review records.
**Audit evidence:** SIEM configuration; alert rules; monitoring review records; SOC reports; incident log showing SIEM-detected events.

### 8.23 — Web Filtering ⭐ NEW
**Purpose:** Manage access to external websites to reduce exposure to malicious content.
**Key requirements:** Web filtering solution covering all user internet access; blocked categories defined; management of exceptions; monitoring of filtering effectiveness.
**Implementation guidance:** Implement URL filtering (e.g., Cisco Umbrella, Zscaler, Forcepoint). Block known malicious sites and inappropriate content categories. Log all web traffic. Process for staff to request legitimate site unblocking.
**Audit evidence:** Web filtering solution evidence; blocked category policy; exception request process; filtering effectiveness metrics.

### 8.28 — Secure Coding ⭐ NEW
**Purpose:** Apply secure coding principles to software development to reduce vulnerabilities.
**Key requirements:** Secure coding standards adopted; developer security training; code review processes; SAST/DAST tools in SDLC; security requirements in development standards.
**Implementation guidance:** Adopt OWASP Secure Coding Practices. Implement SAST (Static Application Security Testing) in CI/CD pipeline. Conduct regular code reviews with security focus. Train developers in OWASP Top 10. Conduct annual penetration testing of applications.
**Audit evidence:** Secure coding standard; developer training records; SAST tool results; code review records; pen test reports.

---

## Implementation Notes — Key Existing Controls

### 8.1 — User Endpoint Devices
**Purpose:** Protect information processed on user endpoint devices (laptops, mobile, tablets).
**NFS implementation:** MDM enrollment mandatory; full disk encryption (BitLocker); EDR (endpoint detection and response) deployed; auto-update policy enforced.
**Audit evidence:** MDM enrollment records; BitLocker status reports; EDR deployment evidence; update compliance reports.

### 8.7 — Protection Against Malware
**Purpose:** Protect against malware including viruses, ransomware, and spyware.
**NFS implementation:** EDR solution deployed on all endpoints (CrowdStrike); email filtering with malware scanning; malware alerts feed into SIEM; incident procedure for malware events.
**Audit evidence:** EDR deployment report; malware detection/response records; email filtering configuration; SIEM integration evidence.

### 8.8 — Management of Technical Vulnerabilities
**Purpose:** Identify and remediate technical vulnerabilities in systems and software.
**NFS implementation:** Monthly vulnerability scanning (Tenable.io); CVE tracking against NFS asset inventory; patching SLAs (Critical: 24 hours; High: 7 days; Medium: 30 days; Low: 90 days); annual penetration test.
**Audit evidence:** Vulnerability scan reports; patching records vs SLA; pen test reports; remediation tracking.

### 8.13 — Information Backup
**Purpose:** Protect against loss of data through backup and recovery.
**NFS implementation:** Daily incremental and weekly full backups; encrypted AES-256; offsite (tape) and cloud (Azure) copies; quarterly restoration tests.
**Audit evidence:** Backup configuration; encryption evidence; restoration test records; RPO/RTO achievements.

### 8.15 — Logging
**Purpose:** Generate and retain logs to support detection of security events and post-incident investigation.
**NFS implementation:** Centralised logging to SIEM (Splunk) from all critical systems; log retention 12 months (active) + 6 months (cold archive); log integrity protection; access to logs restricted to IS team.
**Audit evidence:** Log retention policy; SIEM configuration; sample log records; log integrity controls.

### 8.22 — Segregation of Networks
**Purpose:** Separate networks to contain breaches and limit lateral movement.
**NFS implementation:** VLAN segmentation; separate networks for production, development, guest Wi-Fi, POS/branch teller systems; firewall rules reviewed quarterly; DMZ for internet-facing services.
**Audit evidence:** Network diagrams; VLAN configuration; firewall ruleset reviews; DMZ architecture documentation.

### 8.25 — Secure Development Life Cycle
**Purpose:** Integrate security throughout the software development lifecycle.
**NFS implementation:** Security requirements defined at project inception; threat modelling for new systems; SAST in CI/CD pipeline; security review gates before production deployment; annual app pen testing.
**Audit evidence:** SDLC documentation; threat model records; SAST results; security review sign-offs; pen test reports.

### 8.31 — Separation of Environments
**Purpose:** Prevent unauthorised access to production data by separating development, test, and production.
**NFS implementation:** Separate environments enforced (Dev/Test/UAT/Prod); no production data in test environments (anonymised/masked data sets); access to production restricted to operations team.
**Audit evidence:** Environment architecture; access control records showing prod/non-prod separation; data masking evidence for test data.

### 8.32 — Change Management
**Purpose:** Control changes to systems to prevent unauthorised or unintended modifications.
**NFS implementation:** Full change management procedure (NFS-IS-PRO-006) with CAB, IS risk assessment, and rollback procedures.
**Audit evidence:** Change management procedure; CAB meeting records; approved change records; emergency change log.

---

## Theme 8 — Gap Analysis Focus Areas for Financial Services

| Control | Common Gap | Recommended Action |
|---|---|---|
| 8.9 — Configuration management | No CMDB; configurations drift | Implement CMDB; automated compliance scanning |
| 8.11 — Data masking | Production PAN data in test environments | Implement data masking tool; tokenise PAN |
| 8.12 — DLP | No DLP solution | Prioritise DLP for email and endpoint |
| 8.16 — Monitoring | No SIEM; alert fatigue | Deploy SIEM; define use cases; assign SOC responsibility |
| 8.28 — Secure coding | No formal standard; no SAST | Adopt OWASP; implement SAST in pipeline |
| 8.8 — Vulnerability management | Patching SLAs not defined or met | Define SLAs; automate patch deployment; track compliance |

---

*This reference guide covers ISO/IEC 27001:2022 Annex A Theme 8 — Technological Controls (8.1–8.34)*
*For normative control requirements, refer to ISO/IEC 27001:2022 and ISO/IEC 27002:2022*
