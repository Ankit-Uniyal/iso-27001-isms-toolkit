# ISMS Scope Statement — Nexus Financial Services Ltd
## Worked Example | ISO/IEC 27001:2022 — Clause 4.3

> **FICTIONAL REFERENCE ONLY** — For educational purposes. See 03-CLAUSE4-CONTEXT/ISMS-SCOPE-STATEMENT.md for the blank template.

**Document Reference:** NFS-IS-REG-001
**Version:** 2.1
**Effective Date:** 01 January 2026
**Review Date:** 01 January 2027
**Owner:** ISMS Manager
**Approved By:** Chief Information Security Officer and Board of Directors
**Certification Body:** BSI Group UK
**Certificate Number:** IS-88234
**Standard:** ISO/IEC 27001:2022

---

## 1. Organisation Overview

Nexus Financial Services Ltd (NFS) is a UK-based FCA-regulated retail banking institution headquartered in Manchester. NFS provides personal banking, mortgages, savings products, and business banking to approximately 850,000 customers across the United Kingdom through a 14-branch network and digital channels (online banking and mobile app).

NFS employs approximately 3,200 staff across its Head Office (Manchester) and 14 regional branches in the North West and Yorkshire.

---

## 2. ISMS Scope Statement

**The NFS ISMS encompasses:**

The design, development, operation, and maintenance of information security controls protecting the confidentiality, integrity, and availability of information assets associated with:

1. **Retail banking services** — personal current accounts, savings, mortgages, and personal loans
2. **Business banking services** — SME current accounts, overdraft facilities, and trade finance
3. **Digital banking channels** — online banking portal (nexusfs.co.uk/banking) and NFS Mobile App (iOS/Android)
4. **Payment processing** — BACS, CHAPS, Faster Payments, and card payment processing
5. **Customer data management** — storage, processing, and transmission of customer personal and financial data
6. **Core IT infrastructure** — all systems, networks, and applications supporting the above services

---

## 3. Included Locations

| Location | Type | ISMS Included? |
|---|---|---|
| NFS Head Office, 1 Deansgate, Manchester, M3 1AX | Head Office | ✅ Yes — full scope |
| NFS Primary Data Centre, Manchester | Data Centre | ✅ Yes — full scope |
| NFS DR Site, Salford Co-Location Facility | DR Site | ✅ Yes — full scope |
| 14 NFS Branch Locations (North West + Yorkshire) | Retail Branches | ✅ Yes — branch operations in scope |
| Remote working locations (staff home offices, approved co-working) | Remote | ✅ Yes — where NFS systems are accessed |

---

## 4. Excluded from Scope

| Exclusion | Justification |
|---|---|
| NFS Insurance Ltd (separate subsidiary) | Separate legal entity; separate ISMS maintained |
| NFS Asset Management Ltd (separate subsidiary) | Separate legal entity; separate IS programme; no shared infrastructure |
| Third-party ATM network (operated by LINK) | Operated entirely by LINK; NFS has no operational control |

All exclusions have been assessed and confirmed not to affect NFS's ability to provide services conforming to customer requirements and applicable regulatory obligations, and do not affect the integrity of the ISMS.

---

## 5. ISMS Boundary Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    NFS ISMS BOUNDARY                            │
│                                                                 │
│  ┌─────────────┐    ┌─────────────────┐    ┌───────────────┐  │
│  │ Head Office │    │ Primary Data    │    │  DR Site      │  │
│  │ Manchester  │◄──►│ Centre          │◄──►│  Salford      │  │
│  └──────┬──────┘    └────────┬────────┘    └───────────────┘  │
│         │                   │                                   │
│  ┌──────▼──────┐    ┌────────▼────────┐                        │
│  │  14 Branch  │    │  Azure Cloud    │                        │
│  │  Locations  │    │  (IaaS/PaaS)    │                        │
│  └─────────────┘    └─────────────────┘                        │
│         │                                                       │
│  ┌──────▼──────────────────────────────────────────────────┐  │
│  │              Remote Working (VPN-connected)              │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│         ── ── EXCLUDED ── ──                                   │
│         NFS Insurance Ltd | NFS Asset Management Ltd           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. Interfaces and Dependencies

The ISMS boundary interfaces with the following external parties who are not within scope but whose activities affect NFS's information security:

| External Party | Nature of Interface | IS Requirements Contractually Applied? |
|---|---|---|
| Temenos (T24 Core Banking Support) | Remote access for maintenance | ✅ Yes — Tier 1 Supplier Agreement |
| Microsoft (Azure, M365) | Cloud service provider | ✅ Yes — Microsoft Enterprise Agreement; shared responsibility model |
| Payment Service Provider (PCI DSS L1) | Payment processing | ✅ Yes — PSP Agreement; PCI DSS scope defined |
| Experian / Equifax | Credit reference queries | ✅ Yes — Data Processing Agreement |
| FCA | Regulatory oversight | N/A (regulator) |
| BSI Group UK | Certification body | ✅ Yes — Certification Agreement |

---

## 7. Regulatory Context

NFS's ISMS scope is designed to support compliance with:

| Regulation / Standard | Scope Implication |
|---|---|
| UK GDPR / Data Protection Act 2018 | All personal data of customers and staff within scope |
| FCA SYSC — Senior Management Arrangements | IS governance and operational resilience requirements |
| FCA PS21/3 — Operational Resilience | Core systems identified as Important Business Services |
| PCI DSS v4.0 | Card payment processing systems within scope |
| NIS Regulations 2018 | NFS classified as Essential Service Operator for banking |
| ISO/IEC 27001:2022 | Full ISMS scope as defined above |

---

## 8. Scope Approval History

| Version | Date | Change Summary | Approved By |
|---|---|---|---|
| 1.0 | Oct 2023 | Initial ISMS scope at certification | Board |
| 2.0 | Jan 2025 | Added Azure cloud environments to scope following migration | CISO + Board |
| 2.1 | Jan 2026 | Remote working locations formally included; NFS Insurance excluded (new subsidiary) | CISO + Board |

---

*Nexus Financial Services Ltd — FICTIONAL REFERENCE ONLY*
*ISO/IEC 27001:2022 Clause 4.3 — Determining the scope of the information security management system*
*NFS-IS-REG-001 v2.1 | Certificate IS-88234*
