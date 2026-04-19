# Information Security Business Continuity Plan
## ISO/IEC 27001:2022 — Annex A 5.29 & 5.30

**Organisation:** Nexus Financial Services Ltd (NFS)
**Document Reference:** NFS-IS-PLAN-004
**Version:** 1.0
**Effective Date:** 01 May 2026
**Review Date:** 01 May 2027
**Owner:** ISMS Manager / BCM Manager
**Approved By:** Chief Information Security Officer

> **FICTIONAL REFERENCE ONLY — For toolkit demonstration purposes.**
> Not a real business continuity plan. Adapt all recovery times and procedures to your organisation.

---

## 1. Purpose and Scope

### 1.1 Purpose
This plan defines NFS's approach to maintaining information security controls during disruptive events, ensuring that IS continuity requirements are integrated into the organisation's broader Business Continuity Management (BCM) framework. It supports Annex A controls 5.29 (IS during disruption) and 5.30 (ICT readiness for business continuity).

### 1.2 Scope
This plan covers IS continuity arrangements for:
- Critical IT systems and infrastructure
- Core banking platform and customer-facing services
- Information security monitoring (SIEM, IDS/IPS)
- Access control and identity management
- Data backup and recovery
- Communication channels for IS incident management

---

## 2. Critical Information Systems and Recovery Objectives

### 2.1 Business Impact Analysis — IS Systems

| System | Business Criticality | RTO | RPO | IS Classification | Notes |
|---|---|---|---|---|---|
| Core Banking Platform (Temenos T24) | Critical | 4 hours | 1 hour | Highly Restricted | FCA operational resilience obligation |
| Customer Online Banking Portal | Critical | 4 hours | 2 hours | Highly Restricted | FCA operational resilience |
| Payment Processing Gateway | Critical | 2 hours | 30 minutes | Highly Restricted | PCI DSS; FCA |
| Customer Data Platform (CRM) | High | 8 hours | 4 hours | Highly Restricted | Contains PII |
| Email and Communications | High | 8 hours | 4 hours | Confidential | |
| HR and Payroll System | Medium | 24 hours | 24 hours | Confidential | |
| ISMS Management System | Medium | 24 hours | 24 hours | Confidential | |
| Branch Teller Systems (x14) | High | 4 hours per branch | 2 hours | Highly Restricted | |
| Security Monitoring (SIEM) | Critical | 2 hours | 15 minutes | Confidential | IS control |
| Active Directory / IAM | Critical | 2 hours | 1 hour | Highly Restricted | All authentication depends on this |

**RTO** = Recovery Time Objective (maximum acceptable downtime)
**RPO** = Recovery Point Objective (maximum acceptable data loss)

---

## 3. IS Continuity Strategies

### 3.1 Core Banking and Payment Systems

- **Primary site:** Manchester Head Office Data Centre (Tier 3+)
- **DR site:** Salford Co-Location Facility (active-passive configuration)
- **Failover mechanism:** Automated failover for payment gateway (< 30 minutes); manual failover for core banking (target < 4 hours)
- **Replication:** Synchronous database replication between primary and DR site

### 3.2 Data Backup and Recovery

| Backup Type | Frequency | Retention | Storage | Encryption |
|---|---|---|---|---|
| Full system backup | Weekly (Sunday 02:00) | 4 weeks | Tape (off-site) + Cloud (Azure) | AES-256 |
| Incremental backup | Daily (02:00) | 2 weeks | On-site NAS + Cloud (Azure) | AES-256 |
| Database transaction logs | Continuous | 7 days | DR site | AES-256 |
| SIEM log archive | Daily | 12 months | Azure Blob Storage | AES-256 |

Backup restoration is tested quarterly. Full DR test conducted annually.

### 3.3 Identity and Access Management Continuity

- Active Directory: replicated across 3 domain controllers (primary site x2, DR site x1)
- Privileged access emergency credentials (break-glass accounts) held in sealed envelopes in the physical safe (Head Office, accessible to CISO and IT Manager)
- Break-glass access log maintained; usage triggers immediate post-event review
- MFA bypass procedures documented for emergency scenarios (CISO authorisation required)

### 3.4 Security Monitoring Continuity

- SIEM (Splunk): deployed across primary and DR sites; logs forwarded to both
- IDS/IPS: active at both sites; rule synchronisation automated
- In the event of SIEM failure, manual log review protocols activated (IS Analyst on duty)
- 24/7 SOC service: contracted to [External SOC Provider] as fallback during P1 incidents

### 3.5 Remote Working Continuity

In the event of premises evacuation:
- All staff can work remotely via Cisco AnyConnect VPN + MFA
- Remote work IS requirements as per Acceptable Use Policy (NFS-IS-POL-003)
- Critical staff issued with pre-configured laptops and 4G mobile hotspots
- Branch network: minimal remote working capability; branch closure protocols activated

---

## 4. IS-Specific Continuity Procedures

### 4.1 If SIEM / Security Monitoring is Unavailable

1. Alert CISO and IS Analyst immediately
2. Activate manual log review schedule: IS Analyst checks firewall, authentication, and endpoint logs every 2 hours
3. Notify SOC provider to increase monitoring
4. Document monitoring gap and compensating controls in incident log
5. Restore SIEM within RTO (2 hours); escalate to CISO if not met

### 4.2 If Access Control Systems Fail

1. IT Manager notified immediately
2. Physical access: revert to manual visitor sign-in; security staff posted at entry points
3. Logical access: break-glass accounts activated if required (CISO approval)
4. All emergency access logged in the Emergency Access Register
5. Access control systems restored within RTO (2 hours)

### 4.3 If Cryptographic Key Management System is Unavailable

1. CISO notified; IS Analyst activates backup KMS procedures
2. Emergency keys accessible via HSM with dual-control (CISO + IT Security Lead)
3. New key operations suspended until KMS restored
4. Restore KMS within RTO; document any key operations performed during outage

### 4.4 If Data Centre is Unavailable (Full Site Failure)

1. Disaster Recovery Plan (DRP) invoked by CISO or CTO
2. DR site failover initiated per DRP procedures
3. CISO activates IS continuity checklist (security monitoring, access management, comms)
4. FCA notified if outage affects regulated services beyond 2 hours
5. Communication to staff and customers per Crisis Communications Plan

---

## 5. IS Continuity Testing

| Test Type | Frequency | Scope | Owner |
|---|---|---|---|
| Backup restoration test | Quarterly | Restore sample of critical data from backup | IT Manager |
| Tabletop exercise | Annual | IS continuity scenario walkthrough | CISO / ISMS Manager |
| Full DR failover test | Annual | Complete failover to DR site and back | IT Manager + CISO |
| Break-glass access test | Annual | Verify emergency credentials work | CISO + IT Security |
| SIEM failover test | Bi-annual | Verify SIEM DR capability | IS Analyst |

All test results documented and reviewed; failures result in corrective actions.

---

## 6. IS Continuity Roles

| Role | IS Continuity Responsibility |
|---|---|
| CISO | Overall IS continuity authority; activates break-glass; notifies regulators |
| IT Manager | DR site failover; infrastructure recovery |
| IS Analyst | Security monitoring during disruption; log review |
| ISMS Manager | Documents continuity events; updates IS continuity records |
| DPO | Assesses personal data risk during disruption; ICO notification if required |
| BCM Manager | Coordinates with IS team on overall BCP activation |

---

## 7. Regulatory Obligations During Disruption

| Obligation | Trigger | Deadline | Action |
|---|---|---|---|
| FCA operational resilience reporting | Material disruption to important business services | Per FCA guidance | CISO notifies FCA via Connect |
| ICO personal data breach | Data compromised during incident | 72 hours | DPO notifies ICO |
| PCI DSS notification | Payment card data affected | Immediately | CISO notifies acquirer |

---

## 8. Review and Update

This plan is reviewed:
- Annually as part of the ISMS management review
- Following any BC/DR test
- Following any real disruption event
- When significant changes are made to critical systems

---

*Nexus Financial Services Ltd | NFS-IS-PLAN-004 v1.0*
*ISO/IEC 27001:2022 Annex A 5.29 (IS during disruption) and 5.30 (ICT readiness for business continuity)*
