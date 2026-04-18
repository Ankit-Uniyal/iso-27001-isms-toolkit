# ISO/IEC 27001:2022 ISMS Implementation Guide

## How to Use This Toolkit

**Document ID:** ISMS-GUIDE-001
**Version:** 1.0 | **Date:** 2025 | **Audience:** ISMS implementers, GRC professionals, Lead Auditors

---

## What is ISO/IEC 27001:2022?

ISO/IEC 27001:2022 is the international standard for Information Security Management Systems (ISMS). It provides a systematic approach to managing sensitive information — covering people, processes, and technology — through a risk-based framework.

The 2022 revision replaced ISO/IEC 27001:2013 and introduced a restructured Annex A with **93 controls** across 4 themes (down from 114 controls in 14 domains in the 2013 version).

**Key facts:**
- Clauses 4–10 are mandatory requirements
- Annex A provides 93 information security controls
- A Statement of Applicability (SoA) is mandatory — documenting which controls apply and why
- Certification is awarded by accredited certification bodies (e.g., BSI, Bureau Veritas, DNV)
- Organisations certified to ISO 27001:2013 must transition to ISO 27001:2022 by **31 October 2025**

---

## Implementation Roadmap

### Phase 1 — Foundation (Months 1–3)

| Step | Activity | Folder / File |
|---|---|---|
| 1.1 | Conduct gap assessment against all clauses and 93 controls | [01-GAP-ASSESSMENT/](01-GAP-ASSESSMENT/) |
| 1.2 | Define ISMS scope (boundaries, locations, assets) | [03-CLAUSE4-CONTEXT/ISMS-SCOPE-STATEMENT.md](03-CLAUSE4-CONTEXT/ISMS-SCOPE-STATEMENT.md) |
| 1.3 | Identify internal/external context and interested parties | [03-CLAUSE4-CONTEXT/](03-CLAUSE4-CONTEXT/) |
| 1.4 | Map legal and regulatory requirements | [03-CLAUSE4-CONTEXT/LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md](03-CLAUSE4-CONTEXT/LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md) |
| 1.5 | Obtain top management commitment | [04-CLAUSE5-LEADERSHIP/LEADERSHIP-COMMITMENT-STATEMENT.md](04-CLAUSE5-LEADERSHIP/LEADERSHIP-COMMITMENT-STATEMENT.md) |
| 1.6 | Draft and approve Information Security Policy | [02-ISMS-POLICY/INFORMATION-SECURITY-POLICY.md](02-ISMS-POLICY/INFORMATION-SECURITY-POLICY.md) |
| 1.7 | Define ISMS roles and responsibilities | [04-CLAUSE5-LEADERSHIP/ROLES-RESPONSIBILITIES-AUTHORITIES.md](04-CLAUSE5-LEADERSHIP/ROLES-RESPONSIBILITIES-AUTHORITIES.md) |

### Phase 2 — Risk Assessment (Months 2–4)

| Step | Activity | Folder / File |
|---|---|---|
| 2.1 | Define risk assessment methodology and criteria | [05-CLAUSE6-PLANNING/RISK-ASSESSMENT-METHODOLOGY.md](05-CLAUSE6-PLANNING/RISK-ASSESSMENT-METHODOLOGY.md) |
| 2.2 | Build information asset register | [07-CLAUSE8-OPERATION/ASSET-REGISTER.md](07-CLAUSE8-OPERATION/ASSET-REGISTER.md) |
| 2.3 | Identify and assess IS risks for all assets | [05-CLAUSE6-PLANNING/INFORMATION-SECURITY-RISK-REGISTER.md](05-CLAUSE6-PLANNING/INFORMATION-SECURITY-RISK-REGISTER.md) |
| 2.4 | Determine risk treatment decisions | [05-CLAUSE6-PLANNING/RISK-TREATMENT-PLAN.md](05-CLAUSE6-PLANNING/RISK-TREATMENT-PLAN.md) |
| 2.5 | Complete Statement of Applicability (SoA) for all 93 controls | [05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md](05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md) |
| 2.6 | Set measurable IS Objectives | [02-ISMS-POLICY/IS-OBJECTIVES.md](02-ISMS-POLICY/IS-OBJECTIVES.md) |

### Phase 3 — Controls Implementation (Months 3–9)

| Step | Activity | Folder / File |
|---|---|---|
| 3.1 | Implement all applicable Annex A controls | [10-ANNEX-A-CONTROLS/](10-ANNEX-A-CONTROLS/) |
| 3.2 | Establish access control policy and procedures | [07-CLAUSE8-OPERATION/ACCESS-CONTROL-POLICY.md](07-CLAUSE8-OPERATION/ACCESS-CONTROL-POLICY.md) |
| 3.3 | Implement cryptography policy | [07-CLAUSE8-OPERATION/CRYPTOGRAPHY-POLICY.md](07-CLAUSE8-OPERATION/CRYPTOGRAPHY-POLICY.md) |
| 3.4 | Physical security controls | [07-CLAUSE8-OPERATION/PHYSICAL-SECURITY-POLICY.md](07-CLAUSE8-OPERATION/PHYSICAL-SECURITY-POLICY.md) |
| 3.5 | Supplier security assessment and contracts | [07-CLAUSE8-OPERATION/SUPPLIER-SECURITY-POLICY.md](07-CLAUSE8-OPERATION/SUPPLIER-SECURITY-POLICY.md) |
| 3.6 | Incident response capability | [07-CLAUSE8-OPERATION/INCIDENT-RESPONSE-PROCEDURE.md](07-CLAUSE8-OPERATION/INCIDENT-RESPONSE-PROCEDURE.md) |
| 3.7 | Business continuity and IS continuity | [07-CLAUSE8-OPERATION/BUSINESS-CONTINUITY-IS-PLAN.md](07-CLAUSE8-OPERATION/BUSINESS-CONTINUITY-IS-PLAN.md) |
| 3.8 | Awareness and training programme | [06-CLAUSE7-SUPPORT/AWARENESS-PROGRAMME.md](06-CLAUSE7-SUPPORT/AWARENESS-PROGRAMME.md) |
| 3.9 | Document control system | [06-CLAUSE7-SUPPORT/DOCUMENT-CONTROL-PROCEDURE.md](06-CLAUSE7-SUPPORT/DOCUMENT-CONTROL-PROCEDURE.md) |

### Phase 4 — Operate and Monitor (Months 6–12)

| Step | Activity | Folder / File |
|---|---|---|
| 4.1 | Monitor IS KPIs and metrics | [08-CLAUSE9-PERFORMANCE/IS-KPI-METRICS-DASHBOARD.md](08-CLAUSE9-PERFORMANCE/IS-KPI-METRICS-DASHBOARD.md) |
| 4.2 | Conduct internal audit (minimum annually) | [08-CLAUSE9-PERFORMANCE/INTERNAL-AUDIT-PROGRAMME.md](08-CLAUSE9-PERFORMANCE/INTERNAL-AUDIT-PROGRAMME.md) |
| 4.3 | Hold management review | [08-CLAUSE9-PERFORMANCE/MANAGEMENT-REVIEW-TEMPLATE.md](08-CLAUSE9-PERFORMANCE/MANAGEMENT-REVIEW-TEMPLATE.md) |
| 4.4 | Log and treat nonconformities | [09-CLAUSE10-IMPROVEMENT/NCR-CORRECTIVE-ACTION-REGISTER.md](09-CLAUSE10-IMPROVEMENT/NCR-CORRECTIVE-ACTION-REGISTER.md) |
| 4.5 | Track continual improvement | [09-CLAUSE10-IMPROVEMENT/CONTINUAL-IMPROVEMENT-LOG.md](09-CLAUSE10-IMPROVEMENT/CONTINUAL-IMPROVEMENT-LOG.md) |

### Phase 5 — Certification (Month 12–18)

| Step | Activity |
|---|---|
| 5.1 | Select accredited certification body (BSI, DNV, Bureau Veritas, Schellman, etc.) |
| 5.2 | Stage 1 audit — documentation review (typically 1–2 days) |
| 5.3 | Address Stage 1 findings and close gaps |
| 5.4 | Stage 2 audit — evidence and implementation review (typically 2–5 days) |
| 5.5 | Address any nonconformities raised (major NCs must be closed before certificate issued) |
| 5.6 | Certificate issued — valid 3 years with annual surveillance audits |

---

## Mandatory Documents Checklist

ISO 27001:2022 requires the following documented information as a minimum:

| # | Document | Clause | Status |
|---|---|---|---|
| 1 | ISMS Scope | 4.3 | [ ] |
| 2 | Information Security Policy | 5.2 | [ ] |
| 3 | IS Objectives | 6.2 | [ ] |
| 4 | Risk Assessment Methodology | 6.1.2 | [ ] |
| 5 | Risk Assessment Results | 6.1.2 | [ ] |
| 6 | Risk Treatment Plan | 6.1.3 | [ ] |
| 7 | Statement of Applicability | 6.1.3(d) | [ ] |
| 8 | Competence evidence | 7.2 | [ ] |
| 9 | Documented information policy | 7.5 | [ ] |
| 10 | Operational planning results | 8.1 | [ ] |
| 11 | Risk monitoring results | 9.1 | [ ] |
| 12 | Internal audit programme and results | 9.2 | [ ] |
| 13 | Management review results | 9.3 | [ ] |
| 14 | Nonconformities and corrective actions | 10.1 | [ ] |

---

## Key Changes: ISO 27001:2022 vs 2013

| Change | 2013 | 2022 |
|---|---|---|
| Control count | 114 controls | 93 controls |
| Control domains/themes | 14 domains (Annex A) | 4 themes (Organisational, People, Physical, Technological) |
| New controls | — | 11 new controls including threat intelligence (5.7), cloud security (5.23), data masking (8.11), secure coding (8.28) |
| Merged controls | — | 57 controls merged from 2013 versions |
| Transition deadline | — | 31 October 2025 |
| Attributes | None | 5 attribute sets (control type, security properties, cybersecurity concepts, operational capabilities, security domains) |

---

## How to Use the Worked Examples

The [11-WORKED-EXAMPLE/](11-WORKED-EXAMPLE/) folder contains completed versions of key templates using the fictional **Nexus Financial Services Ltd (NFS)** organisation. Use these to understand what a realistic, completed entry looks like before filling in your own templates.

**Do not copy the worked examples verbatim** — they must be tailored to your organisation's specific context, assets, risks, and regulatory environment.

---

## Glossary of Key Terms

| Term | Definition |
|---|---|
| ISMS | Information Security Management System |
| SoA | Statement of Applicability — mandatory document listing all 93 controls with inclusion/exclusion justifications |
| Risk owner | Person accountable for managing a specific information security risk |
| Control | Measure that modifies or maintains risk (preventive, detective, or corrective) |
| Nonconformity (NC) | Failure to meet a requirement of ISO 27001 or the organisation's own ISMS |
| Major NC | Nonconformity that affects the organisation's ability to achieve intended ISMS outcomes — must be closed before certification |
| Minor NC | Nonconformity that does not fundamentally affect ISMS outcomes — OFI to close within agreed timeframe |
| Observation / OFI | Opportunity for Improvement — not a nonconformity, but a recommendation |
| CIA triad | Confidentiality, Integrity, Availability — the three core information security properties |

---

*ISO/IEC 27001:2022 ISMS Toolkit | Implementation Guide | See README.md for full index*
