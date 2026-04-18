# Information Asset Register

## ISO/IEC 27001:2022 | Clause 8.1 & Control 5.9

**Document ID:** ISMS-ASSET-001
**Version:** 1.0 | **Owner:** CISO / IT Operations | **Date:** ___ | **Review Cycle:** Annual / on significant change

---

## Purpose

This register inventories all information assets within the ISMS scope in accordance with ISO/IEC 27001:2022 Annex A control 5.9 (Inventory of information and other associated assets).

---

## Classification Scheme

| Classification | Description | Handling Requirements |
|---|---|---|
| **RESTRICTED** | Highly sensitive — limited distribution | Encrypted at rest and in transit; need-to-know access; no cloud without approval |
| **CONFIDENTIAL** | Sensitive business information | Encrypted in transit; access controlled; labelled; limited sharing |
| **INTERNAL** | For internal use only | Not shared externally without approval |
| **PUBLIC** | Approved for public release | No special handling required |

---

## Asset Register

| Asset ID | Asset Name | Type | Classification | Asset Owner | Location | IS Risk Level | Last Reviewed |
|---|---|---|---|---|---|---|---|
| ASSET-001 | Customer database | Data | CONFIDENTIAL | Head of Data | Cloud (AWS) | HIGH | |
| ASSET-002 | Employee HR records | Data | RESTRICTED | Head of HR | On-premise HR system | HIGH | |
| ASSET-003 | Financial records | Data | CONFIDENTIAL | CFO | ERP system (cloud) | HIGH | |
| ASSET-004 | Source code repository | Data | CONFIDENTIAL | Head of Engineering | GitLab (cloud) | HIGH | |
| ASSET-005 | Authentication credentials / secrets | Data | RESTRICTED | CISO | PAM vault | CRITICAL | |
| ASSET-006 | ISMS documentation | Data | INTERNAL | ISMS Manager | SharePoint / GitHub | MEDIUM | |
| ASSET-007 | Backup data | Data | CONFIDENTIAL | IT Operations | Backup server (encrypted) | HIGH | |
| ASSET-008 | Email system | System | INTERNAL | Head of IT | Microsoft 365 (cloud) | HIGH | |
| ASSET-009 | Core production servers | Hardware | — | Head of IT | Primary data centre | HIGH | |
| ASSET-010 | Endpoint devices (laptops, mobiles) | Hardware | — | Head of IT | Various | MEDIUM | |
| ASSET-011 | Network infrastructure | Hardware | — | Head of IT | Primary data centre | HIGH | |
| ASSET-012 | Cloud infrastructure | System | — | Head of IT | AWS / Azure | HIGH | |
| ASSET-013 | Core business applications (ERP, CRM) | Software | — | Business Owners | Cloud SaaS | MEDIUM | |
| ASSET-014 | Physical records | Physical | CONFIDENTIAL | Department heads | Secure filing rooms | MEDIUM | |

---

## Asset Owner Responsibilities

- Identify and classify assets under their ownership
- Approve access requests for their assets
- Review and recertify access at least annually
- Report IS incidents affecting their assets
- Provide input to IS risk assessment for their assets

---

## Annual Asset Review Log

| Review Date | Assets Added | Assets Removed | Classification Changes | Reviewed By |
|---|---|---|---|---|
| | | | | |

---

*ISO/IEC 27001:2022 ISMS Toolkit | Information Asset Register | Control 5.9 | See root README.md for full index*
