# Access Control Policy
## ISO/IEC 27001:2022 — Annex A 5.15–5.18 & 8.2–8.5

**Organisation:** Nexus Financial Services Ltd (NFS)
**Document Reference:** NFS-IS-POL-008
**Version:** 1.0
**Effective Date:** 01 May 2026
**Review Date:** 01 May 2027
**Owner:** Chief Information Security Officer
**Approved By:** Chief Information Security Officer

---

## 1. Purpose and Scope

### 1.1 Purpose
This policy defines NFS's requirements for controlling access to information assets, systems, applications, and networks. It ensures that access is granted on a need-to-know and least-privilege basis, protecting the confidentiality, integrity, and availability of NFS information.

### 1.2 Scope
This policy applies to all NFS employees, contractors, third parties, and systems that access NFS information assets — including on-premises systems, cloud platforms, remote access, and privileged access.

---

## 2. Access Control Principles

NFS applies the following core principles to all access control decisions:

| Principle | Definition |
|---|---|
| **Need to Know** | Access granted only where required to perform job functions |
| **Least Privilege** | Users granted minimum permissions necessary; no excessive access |
| **Separation of Duties** | Critical tasks split between multiple individuals to prevent fraud/error |
| **Default Deny** | Access denied by default; explicit grant required |
| **Periodic Review** | All access rights reviewed at least annually; privileged access quarterly |

---

## 3. Access Control Requirements

### 3.1 User Account Management

| Requirement | Standard |
|---|---|
| Unique user accounts | Each individual must have a unique, non-shared account |
| Shared / generic accounts | Prohibited except for documented exceptions (CISO approval required) |
| Joiners (new starters) | Access provisioned within 1 business day of start date; based on approved role profile |
| Movers (role changes) | Access reviewed and adjusted within 5 business days of role change |
| Leavers (departures) | All access revoked on last day of employment (or earlier if risk warrants) |
| Contractors | Access provisioned for defined engagement period only; auto-expire set |
| Dormant accounts | Accounts inactive for 90+ days disabled; inactive for 180+ days deleted |

### 3.2 Password and Authentication Requirements

| Requirement | Standard |
|---|---|
| Minimum password length | 14 characters |
| Password complexity | Mix of upper/lower case, numbers, special characters |
| Password history | Cannot reuse last 12 passwords |
| Maximum password age | 90 days (standard); see MFA exceptions below |
| Multi-Factor Authentication | Mandatory for: all remote access, privileged accounts, cloud admin, email |
| Password manager | NFS-approved password manager must be used for all business accounts |
| Failed login lockout | Account locked after 5 failed attempts; unlock requires IT Service Desk |

### 3.3 Privileged Access Management

Privileged access (administrator, root, super-user accounts) carries elevated risk and requires enhanced controls:

- Privileged accounts must be separate from standard user accounts
- Privileged access requests require CISO approval
- All privileged session activity is logged and reviewed
- Privileged access reviewed quarterly
- Just-in-Time (JIT) access used for cloud privileged access where technically feasible
- Privileged accounts subject to annual recertification
- No standing privileged access to production systems without documented business justification

### 3.4 Remote Access

| Requirement | Standard |
|---|---|
| VPN requirement | All remote access to NFS systems via approved VPN (Cisco AnyConnect) |
| MFA | Mandatory for all VPN connections |
| Approved devices | Remote access permitted from NFS-managed devices only; BYO requires MDM enrolment |
| Session timeout | VPN sessions auto-disconnect after 60 minutes of inactivity |
| Split tunnelling | Not permitted; all traffic routed through VPN |

### 3.5 Third-Party and Supplier Access

- Third-party access requires formal approval (CISO + business sponsor)
- Access limited to specific systems required for contracted services
- Remote access by third parties logged and monitored
- Access revoked immediately upon contract end or termination
- Supplier access reviewed quarterly as part of supplier management process

---

## 4. Access Control for Systems and Applications

### 4.1 Role-Based Access Control (RBAC)

NFS uses RBAC for all major systems. Access roles are defined by the system owner and approved by the CISO. Role profiles must be documented and reviewed annually.

### 4.2 System Access Levels

| Access Level | Description | Approval Required |
|---|---|---|
| Standard User | Normal business function access | Line Manager + IT |
| Power User | Extended read/write access to specific datasets | Line Manager + CISO |
| Application Admin | Admin access within a specific application | CISO |
| System Admin | OS/infrastructure level admin | CISO |
| Security Admin | SIEM, DLP, firewall management | CISO |
| Emergency Access | Break-glass access for incident response | CISO (verbal OK; documented retrospectively) |

### 4.3 Sensitive System Access

The following systems require enhanced access controls and additional approval:

| System | Classification | Enhanced Control |
|---|---|---|
| Core Banking Platform | Highly Restricted | CISO approval; quarterly review; all access logged |
| Customer Data Platform | Highly Restricted | DPO + CISO approval; access logged |
| HR and Payroll System | Confidential | HR Director approval; access logged |
| Financial Reporting System | Confidential | CFO approval; dual control for critical transactions |
| ISMS Document Management | Confidential | ISMS Manager approval |

---

## 5. Access Review Process

| Review Type | Frequency | Conducted By | Records Retained |
|---|---|---|---|
| All-user access review | Annual | ISMS Manager + System Owners | Yes — review certificates |
| Privileged access review | Quarterly | CISO | Yes — review report |
| Third-party access review | Quarterly | ISMS Manager + Procurement | Yes — supplier register |
| Post-incident access review | Following P1/P2 incidents | CISO | Yes — incident report |
| Role-change review | On each role change | IT + Line Manager | Yes — change record |

Discrepancies identified during access reviews must be resolved within 10 business days. Unexplained access is treated as a potential security incident and escalated to the CISO.

---

## 6. Access Control for Physical and Logical Assets

For physical access controls, refer to the Physical Security Policy (NFS-IS-POL-010).

Logical network access is governed by:
- Network segmentation (VLAN architecture)
- Firewall rules reviewed quarterly
- Zero-trust network access (ZTNA) being implemented for cloud systems (target: Q4 2026)

---

## 7. Monitoring and Audit

- All access to Highly Restricted systems is logged and retained for 12 months
- Privileged session recordings enabled for critical systems
- Access logs reviewed monthly by the IS team for anomalies
- Automated alerting for: login outside business hours, multiple failed logins, access from new geolocation

---

## 8. Exceptions

Requests for exceptions to this policy require:
1. Written justification from the requesting user/manager
2. Risk assessment completed by ISMS Manager
3. Written CISO approval
4. Time limit defined (maximum 90 days; renewable)
5. Compensating controls documented
6. Exception logged in the Exceptions Register

---

## 9. Non-Compliance

Violations of this policy are treated as IS incidents. Depending on severity:
- Access immediately revoked pending investigation
- Disciplinary action under HR policy
- Escalation to CISO, HR, Legal as appropriate
- Criminal referral where unlawful access is confirmed

---

*Nexus Financial Services Ltd | NFS-IS-POL-008 v1.0*
*ISO/IEC 27001:2022 Annex A 5.15 (Access control), 5.16 (Identity management), 5.17 (Authentication), 5.18 (Access rights), 8.2 (Privileged access), 8.3 (Information access restriction), 8.5 (Secure authentication)*
