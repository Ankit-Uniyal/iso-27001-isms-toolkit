# ISO/IEC 27001:2022 ISMS Toolkit

> A practical, audit-ready implementation toolkit for ISO/IEC 27001:2022 Information Security Management Systems — covering all 10 clauses, all 93 Annex A controls, risk assessment templates, Statement of Applicability, internal audit guides, and worked examples for GRC professionals and information security practitioners.

---

## What This Toolkit Contains

- All 10 ISO 27001:2022 clauses with implementation templates
- All 93 Annex A controls across 4 themes (Organisational, People, Physical, Technological)
- Full Statement of Applicability (SoA) with pre-populated control mapping
- Risk Assessment Methodology and Risk Register templates
- Internal Audit Programme and Management Review templates
- Legal & Regulatory Requirements Register
- Worked examples for a fictional organisation (Nexus Financial Services Ltd)
- GRC automation scripts (Python)
- Cross-mapping to NIST CSF 2.0, ISO 42001, and CIS Controls v8

---

## Repository Structure

| # | Folder / File | Contents |
|---|---|---|
| — | [README.md](README.md) | This file — full index and navigation guide |
| — | [00-IMPLEMENTATION-GUIDE.md](00-IMPLEMENTATION-GUIDE.md) | How to use this toolkit; implementation roadmap |
| 1 | [01-GAP-ASSESSMENT/](01-GAP-ASSESSMENT/) | 93-control gap assessment checklist |
| 2 | [02-ISMS-POLICY/](02-ISMS-POLICY/) | Information Security Policy and IS Objectives |
| 3 | [03-CLAUSE4-CONTEXT/](03-CLAUSE4-CONTEXT/) | Context, interested parties, ISMS scope |
| 4 | [04-CLAUSE5-LEADERSHIP/](04-CLAUSE5-LEADERSHIP/) | Leadership, roles, responsibilities |
| 5 | [05-CLAUSE6-PLANNING/](05-CLAUSE6-PLANNING/) | Risk assessment, risk treatment, SoA (93 controls) |
| 6 | [06-CLAUSE7-SUPPORT/](06-CLAUSE7-SUPPORT/) | Competence, awareness, communications, documented info |
| 7 | [07-CLAUSE8-OPERATION/](07-CLAUSE8-OPERATION/) | Operational controls, asset management, supplier security |
| 8 | [08-CLAUSE9-PERFORMANCE/](08-CLAUSE9-PERFORMANCE/) | Internal audit, KPIs, management review |
| 9 | [09-CLAUSE10-IMPROVEMENT/](09-CLAUSE10-IMPROVEMENT/) | Nonconformities, corrective actions, continual improvement |
| 10 | [10-ANNEX-A-CONTROLS/](10-ANNEX-A-CONTROLS/) | All 93 controls reference guide |
| 11 | [11-WORKED-EXAMPLE/](11-WORKED-EXAMPLE/) | Fictional NFS implementation examples |
| 12 | [12-SCRIPTS/](12-SCRIPTS/) | Python GRC automation scripts |

---

## Clause-by-Clause File Index

### Implementation Guide (Root)

| File | Purpose |
|---|---|
| [00-IMPLEMENTATION-GUIDE.md](00-IMPLEMENTATION-GUIDE.md) | Step-by-step ISMS implementation roadmap |

---

### Gap Assessment

Folder: [01-GAP-ASSESSMENT/](01-GAP-ASSESSMENT/)

| # | File | Purpose |
|---|---|---|
| 1 | [ISO27001-GAP-ASSESSMENT-CHECKLIST.md](01-GAP-ASSESSMENT/ISO27001-GAP-ASSESSMENT-CHECKLIST.md) | Full 93-control + clause-by-clause gap assessment |
| 2 | [GAP-ASSESSMENT-SCORING-GUIDE.md](01-GAP-ASSESSMENT/GAP-ASSESSMENT-SCORING-GUIDE.md) | Scoring methodology and rating guidance |

---

### ISMS Policy

Folder: [02-ISMS-POLICY/](02-ISMS-POLICY/)

| # | File | Purpose |
|---|---|---|
| 1 | [INFORMATION-SECURITY-POLICY.md](02-ISMS-POLICY/INFORMATION-SECURITY-POLICY.md) | Top-level IS Policy (Clause 5.2) |
| 2 | [IS-OBJECTIVES.md](02-ISMS-POLICY/IS-OBJECTIVES.md) | Measurable IS Objectives (Clause 6.2) |

---

### Clause 4 — Context of the Organisation

Folder: [03-CLAUSE4-CONTEXT/](03-CLAUSE4-CONTEXT/)

| # | File | Purpose |
|---|---|---|
| 1 | [CONTEXT-AND-ISSUES-REGISTER.md](03-CLAUSE4-CONTEXT/CONTEXT-AND-ISSUES-REGISTER.md) | Internal and external issues register |
| 2 | [INTERESTED-PARTIES-REGISTER.md](03-CLAUSE4-CONTEXT/INTERESTED-PARTIES-REGISTER.md) | Stakeholders and their requirements |
| 3 | [ISMS-SCOPE-STATEMENT.md](03-CLAUSE4-CONTEXT/ISMS-SCOPE-STATEMENT.md) | ISMS scope definition |
| 4 | [LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md](03-CLAUSE4-CONTEXT/LEGAL-REGULATORY-REQUIREMENTS-REGISTER.md) | Legal and regulatory obligations |

---

### Clause 5 — Leadership

Folder: [04-CLAUSE5-LEADERSHIP/](04-CLAUSE5-LEADERSHIP/)

| # | File | Purpose |
|---|---|---|
| 1 | [LEADERSHIP-COMMITMENT-STATEMENT.md](04-CLAUSE5-LEADERSHIP/LEADERSHIP-COMMITMENT-STATEMENT.md) | Top management commitment (Clause 5.1) |
| 2 | [ROLES-RESPONSIBILITIES-AUTHORITIES.md](04-CLAUSE5-LEADERSHIP/ROLES-RESPONSIBILITIES-AUTHORITIES.md) | ISMS roles and RACI matrix |
| 3 | [IS-ACCEPTABLE-USE-POLICY.md](04-CLAUSE5-LEADERSHIP/IS-ACCEPTABLE-USE-POLICY.md) | Acceptable use of information assets |

---

### Clause 6 — Planning

Folder: [05-CLAUSE6-PLANNING/](05-CLAUSE6-PLANNING/)

| # | File | Purpose |
|---|---|---|
| 1 | [RISK-ASSESSMENT-METHODOLOGY.md](05-CLAUSE6-PLANNING/RISK-ASSESSMENT-METHODOLOGY.md) | IS risk assessment approach and criteria |
| 2 | [INFORMATION-SECURITY-RISK-REGISTER.md](05-CLAUSE6-PLANNING/INFORMATION-SECURITY-RISK-REGISTER.md) | IS risk register template |
| 3 | [RISK-TREATMENT-PLAN.md](05-CLAUSE6-PLANNING/RISK-TREATMENT-PLAN.md) | Risk treatment decisions and actions |
| 4 | [STATEMENT-OF-APPLICABILITY.md](05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md) | SoA with all 93 Annex A controls |

---

### Clause 7 — Support

Folder: [06-CLAUSE7-SUPPORT/](06-CLAUSE7-SUPPORT/)

| # | File | Purpose |
|---|---|---|
| 1 | [COMPETENCE-AND-TRAINING-REGISTER.md](06-CLAUSE7-SUPPORT/COMPETENCE-AND-TRAINING-REGISTER.md) | Staff IS competence and training records |
| 2 | [AWARENESS-PROGRAMME.md](06-CLAUSE7-SUPPORT/AWARENESS-PROGRAMME.md) | IS awareness training plan |
| 3 | [COMMUNICATIONS-PLAN.md](06-CLAUSE7-SUPPORT/COMMUNICATIONS-PLAN.md) | Internal and external IS communications |
| 4 | [DOCUMENT-CONTROL-PROCEDURE.md](06-CLAUSE7-SUPPORT/DOCUMENT-CONTROL-PROCEDURE.md) | Documented information management |
| 5 | [ISMS-DOCUMENT-MASTER-LIST.md](06-CLAUSE7-SUPPORT/ISMS-DOCUMENT-MASTER-LIST.md) | Master list of all ISMS documents |

---

### Clause 8 — Operation

Folder: [07-CLAUSE8-OPERATION/](07-CLAUSE8-OPERATION/)

| # | File | Purpose |
|---|---|---|
| 1 | [ASSET-REGISTER.md](07-CLAUSE8-OPERATION/ASSET-REGISTER.md) | Information asset inventory and classification |
| 2 | [SUPPLIER-SECURITY-POLICY.md](07-CLAUSE8-OPERATION/SUPPLIER-SECURITY-POLICY.md) | Third-party and supplier security requirements |
| 3 | [INCIDENT-RESPONSE-PROCEDURE.md](07-CLAUSE8-OPERATION/INCIDENT-RESPONSE-PROCEDURE.md) | IS incident detection, response, recovery |
| 4 | [CHANGE-MANAGEMENT-PROCEDURE.md](07-CLAUSE8-OPERATION/CHANGE-MANAGEMENT-PROCEDURE.md) | Change management for ISMS-relevant changes |
| 5 | [BUSINESS-CONTINUITY-IS-PLAN.md](07-CLAUSE8-OPERATION/BUSINESS-CONTINUITY-IS-PLAN.md) | IS continuity and disaster recovery |
| 6 | [CRYPTOGRAPHY-POLICY.md](07-CLAUSE8-OPERATION/CRYPTOGRAPHY-POLICY.md) | Cryptographic controls policy |
| 7 | [ACCESS-CONTROL-POLICY.md](07-CLAUSE8-OPERATION/ACCESS-CONTROL-POLICY.md) | Logical access control requirements |
| 8 | [PHYSICAL-SECURITY-POLICY.md](07-CLAUSE8-OPERATION/PHYSICAL-SECURITY-POLICY.md) | Physical and environmental security |

---

### Clause 9 — Performance Evaluation

Folder: [08-CLAUSE9-PERFORMANCE/](08-CLAUSE9-PERFORMANCE/)

| # | File | Purpose |
|---|---|---|
| 1 | [IS-KPI-METRICS-DASHBOARD.md](08-CLAUSE9-PERFORMANCE/IS-KPI-METRICS-DASHBOARD.md) | IS performance metrics and KPIs |
| 2 | [INTERNAL-AUDIT-PROGRAMME.md](08-CLAUSE9-PERFORMANCE/INTERNAL-AUDIT-PROGRAMME.md) | Annual internal audit schedule and scope |
| 3 | [INTERNAL-AUDIT-REPORT-TEMPLATE.md](08-CLAUSE9-PERFORMANCE/INTERNAL-AUDIT-REPORT-TEMPLATE.md) | Internal audit findings report template |
| 4 | [MANAGEMENT-REVIEW-TEMPLATE.md](08-CLAUSE9-PERFORMANCE/MANAGEMENT-REVIEW-TEMPLATE.md) | Management review agenda and minutes |

---

### Clause 10 — Improvement

Folder: [09-CLAUSE10-IMPROVEMENT/](09-CLAUSE10-IMPROVEMENT/)

| # | File | Purpose |
|---|---|---|
| 1 | [NCR-CORRECTIVE-ACTION-REGISTER.md](09-CLAUSE10-IMPROVEMENT/NCR-CORRECTIVE-ACTION-REGISTER.md) | Nonconformity and corrective action log |
| 2 | [CONTINUAL-IMPROVEMENT-LOG.md](09-CLAUSE10-IMPROVEMENT/CONTINUAL-IMPROVEMENT-LOG.md) | IS improvement initiatives tracker |

---

### Annex A — Controls Reference

Folder: [10-ANNEX-A-CONTROLS/](10-ANNEX-A-CONTROLS/)

| # | File | Purpose |
|---|---|---|
| 1 | [README.md](10-ANNEX-A-CONTROLS/README.md) | Annex A overview and theme structure |
| 2 | [THEME-5-ORGANISATIONAL-CONTROLS.md](10-ANNEX-A-CONTROLS/THEME-5-ORGANISATIONAL-CONTROLS.md) | Controls 5.1–5.37 (37 controls) |
| 3 | [THEME-6-PEOPLE-CONTROLS.md](10-ANNEX-A-CONTROLS/THEME-6-PEOPLE-CONTROLS.md) | Controls 6.1–6.8 (8 controls) |
| 4 | [THEME-7-PHYSICAL-CONTROLS.md](10-ANNEX-A-CONTROLS/THEME-7-PHYSICAL-CONTROLS.md) | Controls 7.1–7.14 (14 controls) |
| 5 | [THEME-8-TECHNOLOGICAL-CONTROLS.md](10-ANNEX-A-CONTROLS/THEME-8-TECHNOLOGICAL-CONTROLS.md) | Controls 8.1–8.34 (34 controls) |

---

### Worked Example — Nexus Financial Services

Folder: [11-WORKED-EXAMPLE/](11-WORKED-EXAMPLE/)

> Fictional implementation reference — completed templates for educational use only.

| # | File | What It Shows |
|---|---|---|
| 1 | [README.md](11-WORKED-EXAMPLE/README.md) | NFS org profile and file index |
| 2 | [NFS-ISMS-SCOPE-STATEMENT.md](11-WORKED-EXAMPLE/NFS-ISMS-SCOPE-STATEMENT.md) | Completed ISMS Scope Statement |
| 3 | [NFS-RISK-REGISTER-ENTRY.md](11-WORKED-EXAMPLE/NFS-RISK-REGISTER-ENTRY.md) | Three populated IS risk register entries |
| 4 | [NFS-SOA-EXCERPT.md](11-WORKED-EXAMPLE/NFS-SOA-EXCERPT.md) | Completed SoA excerpt (Theme 5 controls) |
| 5 | [NFS-INCIDENT-LOG-ENTRY.md](11-WORKED-EXAMPLE/NFS-INCIDENT-LOG-ENTRY.md) | Completed IS incident log entry |

---

### Scripts and Automation

Folder: [12-SCRIPTS/](12-SCRIPTS/)

| File | Purpose |
|---|---|
| [isms_soa_tracker.py](12-SCRIPTS/isms_soa_tracker.py) | SoA tracker — all 93 controls with progress reporting |
| [isms_gap_checker.py](12-SCRIPTS/isms_gap_checker.py) | Automated ISMS gap assessment checker |

---

## ISO 27001:2022 Quick Reference

| Clause | Title | Key Requirement |
|---|---|---|
| 4 | Context | Understand the organisation, interested parties, and ISMS scope |
| 5 | Leadership | Top management commitment, IS policy, roles and responsibilities |
| 6 | Planning | Risk assessment, risk treatment, Statement of Applicability, IS objectives |
| 7 | Support | Resources, competence, awareness, communication, documented information |
| 8 | Operation | Implement controls, manage risks, supplier security |
| 9 | Performance | Monitor, measure, internal audit, management review |
| 10 | Improvement | Nonconformities, corrective actions, continual improvement |

---

## Annex A Control Themes (ISO 27001:2022)

| Theme | Range | Count | Description |
|---|---|---|---|
| 5 — Organisational | 5.1–5.37 | 37 | Policies, roles, asset management, threat intelligence, access control |
| 6 — People | 6.1–6.8 | 8 | Screening, terms, awareness, disciplinary, offboarding |
| 7 — Physical | 7.1–7.14 | 14 | Perimeters, entry, offices, equipment, clear desk |
| 8 — Technological | 8.1–8.34 | 34 | Endpoints, privileged access, malware, logging, vulnerability management |
| **Total** | | **93** | |

---

## Cross-Mapping

This toolkit cross-maps ISO 27001:2022 controls to:
- **NIST CSF 2.0** — Identify / Protect / Detect / Respond / Recover functions
- **ISO/IEC 42001:2023** — AI governance controls that complement ISMS
- **CIS Controls v8** — Implementation Group mappings
- **UK Cyber Essentials** — Baseline technical controls alignment

---

## Maintained by

Ankit Uniyal — ISO 27001 Lead Auditor | GRC Lead

*See [00-IMPLEMENTATION-GUIDE.md](00-IMPLEMENTATION-GUIDE.md) for the full implementation roadmap.*
