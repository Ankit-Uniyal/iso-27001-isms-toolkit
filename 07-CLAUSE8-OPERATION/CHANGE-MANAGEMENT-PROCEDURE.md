# Change Management Procedure
## ISO/IEC 27001:2022 — Clause 8.1 & Annex A 8.32

**Organisation:** Nexus Financial Services Ltd (NFS)
**Document Reference:** NFS-IS-PRO-006
**Version:** 1.0
**Effective Date:** 01 May 2026
**Review Date:** 01 May 2027
**Owner:** IT Manager
**Approved By:** Chief Information Security Officer

---

## 1. Purpose and Scope

### 1.1 Purpose
This procedure defines NFS's requirements for managing changes to information systems, infrastructure, applications, and ISMS processes to ensure that changes are assessed for information security impact, authorised, tested, and implemented in a controlled manner.

### 1.2 Scope
This procedure applies to all changes to:
- Production IT systems, infrastructure, and networks
- Business applications and software
- Security controls and configurations
- ISMS processes and documented information
- Cloud platforms and SaaS configurations
- Third-party integrations and APIs

It applies to all NFS staff, contractors, and third parties with change rights.

---

## 2. Change Types and Classification

| Change Type | Description | Approval Required | Examples |
|---|---|---|---|
| **Standard Change** | Pre-approved, low-risk, well-defined routine changes | Pre-approved by CAB | Password resets, routine patches, approved software installs |
| **Normal Change** | Non-emergency change with defined scope; requires CAB approval | Change Advisory Board | System upgrades, new integrations, firewall rule changes |
| **Emergency Change** | Urgent change required to restore service or address critical security threat | CISO or CTO (retrospective CAB) | Emergency security patch for active exploit; P1 incident remediation |
| **Major Change** | Significant change with high risk or broad impact | CISO + Executive sign-off | Core banking upgrade; cloud migration; new business system |

---

## 3. Information Security Risk Assessment for Changes

### 3.1 Security Impact Assessment

All Normal, Emergency, and Major changes must include an IS Security Impact Assessment addressing:

- [ ] Does the change affect any Confidential or Highly Restricted data?
- [ ] Does the change modify access controls or authentication mechanisms?
- [ ] Does the change affect encryption or key management?
- [ ] Does the change introduce new third-party integrations or data flows?
- [ ] Does the change affect network segmentation, firewall rules, or DMZ?
- [ ] Does the change affect availability of critical business systems?
- [ ] Does the change affect regulatory-controlled systems (FCA, PCI DSS, GDPR)?
- [ ] Has the change been tested in a non-production environment?
- [ ] Has a rollback plan been documented?

If any answer is "Yes," the IS Analyst must review and sign off the change before it proceeds.

### 3.2 Risk Rating for Changes

| Rating | Criteria | IS Analyst Review | CAB Approval |
|---|---|---|---|
| Low | No IS impact identified | Not required | Standard pre-approval |
| Medium | Limited IS impact; existing controls sufficient | Recommended | Required |
| High | Significant IS impact; additional controls required | Required | Required + CISO notation |
| Critical | Major IS implications; affects regulated data or core security controls | Required | Required + CISO sign-off |

---

## 4. Change Process

### 4.1 Change Request (CR) Submission

1. Requester submits Change Request via the ITSM system (ServiceNow)
2. CR includes: description, business justification, systems affected, planned date/time, rollback plan, IS impact assessment
3. CR assigned a unique reference (CR-[YEAR]-[SEQUENCE])

### 4.2 Change Assessment

1. IS Analyst reviews CR for security impact (within 2 business days for Normal; immediately for Emergency)
2. IT Manager reviews for technical feasibility and resource requirements
3. For High/Critical changes: CISO reviews and adds conditions or risk acceptance notation

### 4.3 Change Advisory Board (CAB)

The CAB meets weekly (Thursdays, 10:00) to review Normal changes scheduled for the following week.

CAB membership:
- IT Manager (Chair)
- IS Analyst
- ISMS Manager
- Representative from affected business unit(s)
- CISO (for High/Critical changes)

CAB Decisions: Approve / Approve with conditions / Defer / Reject

### 4.4 Change Scheduling

- Approved changes scheduled in the Change Calendar (ServiceNow)
- Non-emergency production changes restricted to designated Change Windows:
  - Standard: Tuesday/Wednesday 20:00–23:00
  - Major: Saturday 06:00–Sunday 14:00 (with business owner pre-approval)
- Affected users and business owners notified minimum 48 hours before change

### 4.5 Change Implementation

1. Implementer confirms change window start with IT Manager
2. Change implemented per approved change plan
3. Post-implementation verification test conducted
4. Change marked as Implemented in ServiceNow with outcome recorded

### 4.6 Rollback

If post-implementation verification fails or unexpected issues arise:
1. Rollback plan activated immediately
2. IT Manager and CISO notified
3. Rollback outcome recorded in CR
4. Change rescheduled after root cause identified

### 4.7 Post-Implementation Review (PIR)

For Major and Emergency changes:
- PIR conducted within 5 business days of implementation
- PIR covers: did the change achieve its objective? any unexpected IS implications? lessons learned?
- PIR outcome recorded in CR and shared with CISO

---

## 5. Emergency Change Process

For P1/P2 security incidents requiring urgent changes:

1. CISO or CTO verbally approves the emergency change
2. IS Analyst completes expedited security review (within 1 hour)
3. Change implemented immediately
4. Full CR submitted retrospectively within 24 hours of implementation
5. Emergency change reviewed at next CAB meeting

Emergency changes are tracked separately in the Emergency Change Log and reviewed for trends quarterly.

---

## 6. Change Freeze Periods

Change freezes apply during:
- FCA/PCI DSS audit periods (typically 2 weeks before audit)
- Critical business periods (e.g., year-end, major product launches)
- Major bank holidays (confirmed annually by IT Manager)

Change freeze dates are published in the Change Calendar at the start of each year. Only Emergency changes may proceed during freeze periods.

---

## 7. ISMS Changes

Changes to ISMS processes, controls, or documented information must:
- Be assessed for impact on the ISMS scope and risk profile
- Be reviewed by the ISMS Manager before implementation
- Follow the Document Control Procedure (NFS-IS-PRO-007) for updated documentation
- Be reported to the next management review if materially affecting the ISMS

---

## 8. Metrics and Reporting

| Metric | Target | Reported To |
|---|---|---|
| Change success rate | > 95% | CAB monthly |
| Emergency changes as % of total | < 5% | CISO monthly |
| Changes with IS risk rating High/Critical | Tracked and trended | CISO quarterly |
| Rollbacks | Tracked by root cause | CAB monthly |

---

*Nexus Financial Services Ltd | NFS-IS-PRO-006 v1.0*
*ISO/IEC 27001:2022 Clause 8.1 — Operational planning and control; Annex A 8.32 — Change management*
