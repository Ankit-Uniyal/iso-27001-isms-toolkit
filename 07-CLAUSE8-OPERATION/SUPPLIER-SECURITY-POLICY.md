# Supplier and Third-Party Security Policy
## ISO/IEC 27001:2022 — Annex A 5.19–5.22

**Organisation:** Nexus Financial Services Ltd (NFS)
**Document Reference:** NFS-IS-POL-011
**Version:** 1.0
**Effective Date:** 01 May 2026
**Review Date:** 01 May 2027
**Owner:** Chief Information Security Officer
**Approved By:** Chief Information Security Officer

---

## 1. Purpose and Scope

### 1.1 Purpose
This policy defines NFS's requirements for managing information security risks associated with suppliers, third parties, and outsourced service providers that access, process, store, or transmit NFS information assets or connect to NFS systems.

### 1.2 Scope
This policy applies to all third parties including:
- IT service providers and managed service providers (MSPs)
- Cloud service providers (CSPs) and SaaS vendors
- Data processors under UK GDPR
- Professional services firms (legal, audit, consultancy)
- Outsourced business process providers
- Hardware and software vendors with system access

---

## 2. Supplier Risk Classification

All suppliers are classified based on access to NFS information and systems:

| Tier | Classification | Criteria | Review Frequency |
|---|---|---|---|
| Tier 1 — Critical | Highest risk | Access to Highly Restricted data; core system integration; cloud hosting of NFS data | Annually + event-triggered |
| Tier 2 — High | High risk | Access to Confidential data; business-critical services; payroll/HR systems | Annually |
| Tier 3 — Standard | Medium risk | Limited data access; non-critical services; professional services | Every 2 years |
| Tier 4 — Low | Low risk | No NFS data access; commodity services | On-boarding only |

---

## 3. Supplier Onboarding Requirements

### 3.1 Pre-Engagement Due Diligence

Before engaging any Tier 1 or Tier 2 supplier, NFS must complete:

- [ ] Supplier Security Questionnaire (NFS-IS-TMP-005) completed and reviewed
- [ ] Evidence of ISO 27001 certification, SOC 2 Type II, or equivalent (Tier 1 mandatory)
- [ ] UK GDPR / Data Processing Agreement (DPA) in place where personal data is processed
- [ ] Right-to-audit clause included in contract
- [ ] Data residency requirements confirmed (UK/EEA unless approved exception)
- [ ] Incident notification requirements agreed (72-hour notification of breaches)
- [ ] Sub-processor list reviewed and approved
- [ ] Business continuity and recovery capability assessed (Tier 1)
- [ ] Financial stability check completed (Tier 1)

### 3.2 Contractual Security Requirements

All supplier contracts must include (at minimum):

| Clause | Requirement |
|---|---|
| Confidentiality | NDA / confidentiality obligations covering NFS data |
| Data Protection | GDPR-compliant Data Processing Agreement where applicable |
| Security Standards | Compliance with NFS security requirements; ISO 27001 or equivalent |
| Incident Notification | 24-hour notification for P1/P2 incidents; 72-hour for personal data breaches |
| Right to Audit | NFS right to audit supplier security controls (minimum annually for Tier 1) |
| Sub-contracting | Prior written approval required for sub-processors |
| Data Return / Deletion | Return or certified deletion of NFS data upon contract end |
| Termination | Immediate access revocation upon contract termination |

---

## 4. Supplier Access Controls

- All supplier access to NFS systems must be formally approved by the CISO and documented in the Supplier Register
- Supplier access is provisioned on a least-privilege basis for the minimum time required
- All supplier remote access is via NFS-approved VPN with MFA
- Supplier sessions are logged and monitored
- Access is reviewed quarterly for Tier 1 and Tier 2 suppliers
- Access is revoked immediately upon contract end or termination

---

## 5. Ongoing Supplier Management

### 5.1 Annual Security Reviews

Tier 1 and Tier 2 suppliers are subject to annual security review including:
- Review of current security certifications (ISO 27001, SOC 2, PCI DSS as applicable)
- Updated Supplier Security Questionnaire
- Review of incidents and near-misses in the preceding 12 months
- Assessment of any changes to sub-processors or data flows
- Performance against SLA and contractual security obligations

### 5.2 Supplier Incident Management

If a supplier experiences a security incident affecting NFS data or services:
1. Supplier must notify NFS within 24 hours of confirming the incident
2. NFS CISO assesses impact and activates NFS Incident Response Procedure (NFS-IS-PRO-004)
3. CISO determines if FCA, ICO, or other regulatory notification is required
4. Post-incident review completed with supplier within 10 business days
5. Supplier required to provide root cause analysis and remediation plan

### 5.3 Supplier Offboarding

Upon contract termination:
- All NFS data returned in agreed format or certified as deleted within 30 days
- All access credentials revoked on last day of contract
- NFS-issued equipment returned and wiped
- Supplier Offboarding Certificate obtained and filed
- Supplier record archived in Supplier Register

---

## 6. Cloud Service Providers

Cloud services present specific risks that require additional controls:

| Requirement | Standard |
|---|---|
| Data residency | UK or EEA preferred; US/other requires CISO approval and adequate safeguards |
| Encryption | Data encrypted at rest (AES-256) and in transit (TLS 1.2+) |
| Access logs | Cloud audit logs retained for 12 months; exported to NFS SIEM |
| Certifications | ISO 27001 and SOC 2 Type II mandatory for Tier 1 CSPs |
| Shared responsibility model | Documented and understood; NFS responsibilities clearly defined |
| Exit strategy | Data portability and exit plan documented before go-live |

---

## 7. Supplier Register

All active suppliers are recorded in the Supplier Security Register (NFS-IS-REG-010) with:
- Supplier name, contact, and tier classification
- Services provided
- Data types shared/processed
- Security certifications held
- Contract expiry and review dates
- Access rights and systems accessed
- Incident history

---

## 8. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Procurement | Initiates supplier engagement; ensures security requirements in contracts |
| CISO | Approves Tier 1/2 supplier engagements; oversees supplier security programme |
| ISMS Manager | Maintains Supplier Register; coordinates annual reviews |
| Legal | Reviews and negotiates DPAs and security clauses |
| DPO | Approves data processing activities; ICO notification if breach |
| Business Owner | Accountable for day-to-day supplier relationship and performance |

---

*Nexus Financial Services Ltd | NFS-IS-POL-011 v1.0*
*ISO/IEC 27001:2022 Annex A 5.19 (IS in supplier relationships), 5.20 (Addressing IS in agreements), 5.21 (ICT supply chain), 5.22 (Monitoring and review of supplier services)*
