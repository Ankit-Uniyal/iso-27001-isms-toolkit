# Statement of Applicability (SoA)

## ISO/IEC 27001:2022 | Clause 6.1.3

**Document ID:** ISMS-SOA-001
**Version:** 1.0 | **Owner:** CISO | **Date:** ___ | **Review Cycle:** Annual / on risk treatment change
**Organisation:** [Organisation Name] | **ISMS Scope Reference:** ISMS-SCOPE-001

---

## Purpose

This Statement of Applicability (SoA) is a mandatory document required by ISO/IEC 27001:2022 Clause 6.1.3(d). It lists all 93 Annex A controls and for each control states whether it is included or excluded, provides a justification, and records the current implementation status.

The SoA must be reviewed and updated whenever risk treatment decisions change, new risks are identified, or at each annual ISMS review.

---

## Inclusion / Exclusion Key

**Inclusion reasons:**
- **R** = Risk treatment (control reduces identified IS risk)
- **L** = Legal / regulatory requirement
- **C** = Contractual requirement
- **B** = Business requirement / good practice

**Implementation Status:**
- **Implemented** = Control fully in place and effective
- **Partial** = Control partially implemented
- **Planned** = Control planned; implementation in progress
- **Not Started** = Control selected but not yet implemented
- **N/A** = Control excluded

---

## Theme 5 — Organisational Controls (5.1–5.37)

| Control | Title | Included | Justification | Inclusion Reason | Implementation Status | Evidence Reference |
|---|---|---|---|---|---|---|
| 5.1 | Policies for information security | Yes | Baseline IS governance requirement | B, L | Implemented | ISMS-POL-001 |
| 5.2 | Information security roles and responsibilities | Yes | Accountability for IS controls | B | Implemented | ISMS-ROLES-001 |
| 5.3 | Segregation of duties | Yes | Reduces risk of fraud and error in critical processes | R, B | Partial | Access control policy |
| 5.4 | Management responsibilities | Yes | Management must ensure IS obligations are met | B, L | Implemented | ISMS-ROLES-001 |
| 5.5 | Contact with authorities | Yes | Regulatory reporting obligations; incident notification | L | Implemented | Incident response procedure |
| 5.6 | Contact with special interest groups | Yes | Threat intelligence; best practice sharing | B | Partial | CISO membership of ISAC/NCSC alerts |
| 5.7 | Threat intelligence | Yes | Proactive threat awareness to inform risk treatment | R, B | Partial | Threat intel feed subscription |
| 5.8 | Information security in project management | Yes | New projects may introduce IS risks | R, B | Partial | Project IS checklist |
| 5.9 | Inventory of information and other associated assets | Yes | Asset identification is prerequisite for risk assessment | R, B | Partial | ISMS-ASSET-001 |
| 5.10 | Acceptable use of information and other associated assets | Yes | Defines permitted use; reduces insider risk | R, B | Implemented | ISMS-AUP-001 |
| 5.11 | Return of assets | Yes | Ensures assets recovered on termination | R, B | Implemented | HR leaver procedure |
| 5.12 | Classification of information | Yes | Risk-proportionate protection of data | R, L | Partial | Data classification scheme |
| 5.13 | Labelling of information | Yes | Enables classification-based handling | R, B | Partial | Labelling procedure |
| 5.14 | Information transfer | Yes | Secure transmission of information to external parties | R, L, C | Partial | Transfer policy |
| 5.15 | Access control | Yes | Prevents unauthorised access to information | R, L, C | Implemented | ISMS-AC-001 |
| 5.16 | Identity management | Yes | Manages user identities across systems | R, B | Implemented | IAM procedure |
| 5.17 | Authentication information | Yes | Protects credentials from compromise | R, B | Implemented | Password policy |
| 5.18 | Access rights | Yes | Least privilege; formal access provisioning/deprovisioning | R, L, C | Implemented | Access rights procedure |
| 5.19 | Information security in supplier relationships | Yes | Supply chain risk management | R, C | Partial | Supplier IS policy |
| 5.20 | Addressing IS within supplier agreements | Yes | Contractual IS requirements for suppliers | R, C, L | Partial | IS contract clauses |
| 5.21 | Managing IS in the ICT supply chain | Yes | Software and hardware supply chain risk | R, B | Partial | ICT supply chain procedure |
| 5.22 | Monitoring, review and change management of supplier services | Yes | Ongoing supplier IS assurance | R, C | Partial | Supplier review schedule |
| 5.23 | Information security for use of cloud services | Yes | Cloud services in scope of ISMS | R, L, C | Partial | Cloud security policy |
| 5.24 | IS incident management planning and preparation | Yes | Incident response capability required | R, L | Implemented | ISMS-INC-001 |
| 5.25 | Assessment and decision on IS events | Yes | Triage and classification of IS events | R | Implemented | Incident triage procedure |
| 5.26 | Response to IS incidents | Yes | Effective incident handling | R, L | Implemented | Incident response procedure |
| 5.27 | Learning from IS incidents | Yes | Continual improvement from incidents | R, B | Partial | Post-incident review process |
| 5.28 | Collection of evidence | Yes | Supports investigation and legal proceedings | R, L | Partial | Digital forensics procedure |
| 5.29 | IS during disruption | Yes | IS continuity during adverse events | R, B | Partial | IS BCP |
| 5.30 | ICT readiness for business continuity | Yes | Technical IS continuity requirements | R, B | Partial | DR plan |
| 5.31 | Legal, statutory, regulatory and contractual requirements | Yes | Compliance obligation management | L, C | Implemented | ISMS-LEGAL-001 |
| 5.32 | Intellectual property rights | Yes | Protection of IP and licensed software | L, B | Partial | Software asset management |
| 5.33 | Protection of records | Yes | Retention and integrity of ISMS and business records | L, B | Partial | Records retention policy |
| 5.34 | Privacy and protection of PII | Yes | UK GDPR / DPA 2018 compliance | L, C | Implemented | GDPR / DPA programme |
| 5.35 | Independent review of information security | Yes | Certification requirement; independent assurance | L, B | Implemented | Internal audit programme |
| 5.36 | Compliance with policies, rules and standards for IS | Yes | Ensures policies are followed | R, B | Partial | Compliance monitoring procedure |
| 5.37 | Documented operating procedures | Yes | Consistent operational practices | R, B | Partial | IT operations procedures |

---

## Theme 6 — People Controls (6.1–6.8)

| Control | Title | Included | Justification | Inclusion Reason | Implementation Status | Evidence Reference |
|---|---|---|---|---|---|---|
| 6.1 | Screening | Yes | Pre-employment background checks reduce insider threat | R, B | Implemented | HR screening procedure |
| 6.2 | Terms and conditions of employment | Yes | IS obligations in employment contracts | R, L, B | Implemented | Employment contract IS clause |
| 6.3 | IS awareness, education and training | Yes | Staff are a critical IS control layer | R, B | Implemented | ISMS-AWARE-001 |
| 6.4 | Disciplinary process | Yes | Enforces IS policy compliance | R, B | Implemented | HR disciplinary procedure |
| 6.5 | Responsibilities after termination or change | Yes | Access revocation; ongoing confidentiality obligations | R, L, B | Implemented | HR leaver procedure |
| 6.6 | Confidentiality or non-disclosure agreements | Yes | Protects sensitive information shared with staff and third parties | R, C, L | Implemented | NDA templates |
| 6.7 | Remote working | Yes | Remote working in scope of ISMS | R, B | Implemented | Remote working policy |
| 6.8 | Information security event reporting | Yes | Enables early detection of incidents | R, B | Implemented | Incident reporting procedure |

---

## Theme 7 — Physical Controls (7.1–7.14)

| Control | Title | Included | Justification | Inclusion Reason | Implementation Status | Evidence Reference |
|---|---|---|---|---|---|---|
| 7.1 | Physical security perimeters | Yes | Protect physical IS assets | R, B | Implemented | Physical security policy |
| 7.2 | Physical entry | Yes | Prevent unauthorised physical access | R, B | Implemented | Access control logs |
| 7.3 | Securing offices, rooms and facilities | Yes | Protect information processing areas | R, B | Implemented | Physical security policy |
| 7.4 | Physical security monitoring | Yes | Detect physical security breaches | R, B | Partial | CCTV; alarm system |
| 7.5 | Protecting against physical and environmental threats | Yes | Environmental threats to availability | R, B | Partial | Environmental controls |
| 7.6 | Working in secure areas | Yes | Control activity in sensitive areas | R, B | Partial | Secure area procedure |
| 7.7 | Clear desk and clear screen | Yes | Prevent inadvertent disclosure | R, B | Implemented | Clear desk policy |
| 7.8 | Equipment siting and protection | Yes | Physical protection of IS equipment | R, B | Implemented | Facilities management |
| 7.9 | Security of assets off-premises | Yes | Mobile working and remote assets | R, B | Implemented | Asset off-premises policy |
| 7.10 | Storage media | Yes | Protect data on removable media | R, L | Implemented | Media handling procedure |
| 7.11 | Supporting utilities | Yes | Power, cooling, and other utility failures | R, B | Implemented | UPS; generator policy |
| 7.12 | Cabling security | Yes | Network cable physical protection | R, B | Partial | Cabling standards |
| 7.13 | Equipment maintenance | Yes | Maintain IS equipment in working order | R, B | Implemented | Equipment maintenance schedule |
| 7.14 | Secure disposal or re-use of equipment | Yes | Prevent data recovery from disposed equipment | R, L | Implemented | Secure disposal procedure |

---

## Theme 8 — Technological Controls (8.1–8.34)

| Control | Title | Included | Justification | Inclusion Reason | Implementation Status | Evidence Reference |
|---|---|---|---|---|---|---|
| 8.1 | User endpoint devices | Yes | Protect endpoints from compromise | R, B | Implemented | Endpoint security policy |
| 8.2 | Privileged access rights | Yes | Reduce risk of privileged account abuse | R, B | Implemented | PAM procedure |
| 8.3 | Information access restriction | Yes | Enforce access control at application level | R, L, C | Implemented | Access control policy |
| 8.4 | Access to source code | Yes | Protect intellectual property; secure SDLC | R, B | Partial | Source code access procedure |
| 8.5 | Secure authentication | Yes | Multi-factor authentication; strong credentials | R, L, C | Implemented | Authentication policy |
| 8.6 | Capacity management | Yes | Prevent availability failures from capacity exhaustion | R, B | Implemented | Capacity management procedure |
| 8.7 | Protection against malware | Yes | Defend against malicious software | R, B | Implemented | Antimalware policy |
| 8.8 | Management of technical vulnerabilities | Yes | Reduce attack surface through patching | R, B, C | Implemented | Vulnerability management procedure |
| 8.9 | Configuration management | Yes | Secure baseline configurations | R, B | Partial | CIS benchmarks; SCCM |
| 8.10 | Information deletion | Yes | Data minimisation; right to erasure | R, L | Partial | Data deletion procedure |
| 8.11 | Data masking | Yes | Protect PII in non-production environments | R, L | Partial | Data masking procedure |
| 8.12 | Data leakage prevention | Yes | Prevent unauthorised data exfiltration | R, L, C | Partial | DLP tooling |
| 8.13 | Information backup | Yes | Protect information availability | R, B | Implemented | Backup procedure |
| 8.14 | Redundancy of information processing facilities | Yes | High availability for critical systems | R, B | Partial | Redundancy architecture |
| 8.15 | Logging | Yes | Audit trail; incident detection; forensics | R, L, B | Implemented | Logging policy |
| 8.16 | Monitoring activities | Yes | Real-time threat detection | R, B | Implemented | SIEM / SOC |
| 8.17 | Clock synchronisation | Yes | Accurate timestamps for logs and forensics | R, B | Implemented | NTP policy |
| 8.18 | Use of privileged utility programs | Yes | Control powerful system tools | R, B | Partial | Privileged tools procedure |
| 8.19 | Installation of software on operational systems | Yes | Prevent unauthorised software | R, B | Implemented | Software installation policy |
| 8.20 | Networks security | Yes | Protect network infrastructure | R, B | Implemented | Network security policy |
| 8.21 | Security of network services | Yes | Secure network services and connectivity | R, B, C | Partial | Network services procedure |
| 8.22 | Segregation of networks | Yes | Isolate sensitive environments | R, B | Implemented | Network segmentation |
| 8.23 | Web filtering | Yes | Block malicious and inappropriate web content | R, B | Implemented | Web proxy / filtering |
| 8.24 | Use of cryptography | Yes | Protect data confidentiality and integrity | R, L, C | Implemented | Cryptography policy |
| 8.25 | Secure development life cycle | Yes | Build security into software development | R, B | Partial | SDLC security procedure |
| 8.26 | Application security requirements | Yes | Define IS requirements for applications | R, B | Partial | Application security policy |
| 8.27 | Secure system architecture and engineering principles | Yes | Secure by design | R, B | Partial | Architecture review process |
| 8.28 | Secure coding | Yes | Prevent common code vulnerabilities (OWASP) | R, B | Partial | Secure coding standards |
| 8.29 | Security testing in development and acceptance | Yes | Verify IS before deployment | R, B | Partial | Security testing procedure |
| 8.30 | Outsourced development | Yes | IS requirements for third-party developers | R, B, C | Partial | Outsourced dev IS requirements |
| 8.31 | Separation of development, test and production environments | Yes | Prevent test/dev access to production data | R, B | Implemented | Environment separation policy |
| 8.32 | Change management | Yes | IS review of all changes to information systems | R, B | Implemented | Change management procedure |
| 8.33 | Test information | Yes | Protect production data used in testing | R, L | Partial | Test data management procedure |
| 8.34 | Protection of IS during audit testing | Yes | Prevent audit activities from causing IS incidents | R, B | Partial | Audit testing procedure |

---

## SoA Summary

| Theme | Total Controls | Included | Excluded | Implemented | Partial | Planned | Not Started |
|---|---|---|---|---|---|---|---|
| 5 — Organisational | 37 | 37 | 0 | 18 | 17 | 2 | 0 |
| 6 — People | 8 | 8 | 0 | 8 | 0 | 0 | 0 |
| 7 — Physical | 14 | 14 | 0 | 9 | 5 | 0 | 0 |
| 8 — Technological | 34 | 34 | 0 | 18 | 14 | 2 | 0 |
| **TOTAL** | **93** | **93** | **0** | **53** | **36** | **4** | **0** |

> **Note:** The above status figures are template placeholders. Update with actual implementation status.

---

## SoA Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Chief Information Security Officer | | | |
| Chief Executive Officer | | | |
| ISMS Manager | | | |

---

## Review History

| Version | Date | Changes | Approved By |
|---|---|---|---|
| 1.0 | | Initial SoA — all 93 controls assessed | |

---

*ISO/IEC 27001:2022 ISMS Toolkit | Statement of Applicability | Clause 6.1.3 | See root README.md for full index*
