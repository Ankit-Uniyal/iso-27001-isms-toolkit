# Information Security Incident Response Procedure
## ISO/IEC 27001:2022 — Clause 8.1 & Annex A 5.24–5.28

**Organisation:** Nexus Financial Services Ltd (NFS)
**Document Reference:** NFS-IS-PRO-004
**Version:** 1.0
**Effective Date:** 01 May 2026
**Review Date:** 01 May 2027
**Owner:** Chief Information Security Officer
**Approved By:** Chief Information Security Officer

---

## 1. Purpose and Scope

### 1.1 Purpose
This procedure defines NFS's approach to detecting, reporting, investigating, containing, eradicating, and recovering from information security incidents. It ensures consistent, timely, and effective incident management to minimise business impact and meet regulatory obligations.

### 1.2 Scope
This procedure applies to all information security events and incidents affecting NFS information assets, systems, personnel, or customers — regardless of source, location, or severity. It covers all NFS staff, contractors, and third parties who may detect, report, or respond to security incidents.

---

## 2. Incident Severity Classification

| Severity | Level | Definition | Examples |
|---|---|---|---|
| **P1 — Critical** | 1 | Major breach; significant business/regulatory impact; active attack in progress | Ransomware deployment; confirmed data breach affecting 1,000+ records; core banking system compromise |
| **P2 — High** | 2 | Significant IS event; potential data breach; substantial service disruption | Insider threat confirmed; phishing attack with credential compromise; unauthorised privileged access |
| **P3 — Medium** | 3 | Moderate event; contained threat; limited customer/data impact | Malware detection (contained); lost/stolen device; failed intrusion attempt |
| **P4 — Low** | 4 | Minor event; no data loss; minimal business impact | Policy violation; misdelivered email; single failed login from known user |

---

## 3. Incident Response Process

### Phase 1: Detection and Identification

**Sources of incident detection:**
- Security monitoring tools (SIEM, IDS/IPS, EDR)
- Staff reports to IT Service Desk (itsecurity@nexusfs.co.uk or ext. 4000)
- Third-party notifications (suppliers, regulators, law enforcement)
- Vulnerability scanning results
- Automated alerts from DLP, firewall, or cloud security tools

**Actions:**
1. Any staff member who detects or suspects an IS incident must report it immediately to the IT Service Desk
2. IT Service Desk logs the report in the IS Incident Management System with: date/time, reporter, systems affected, and initial description
3. IT Service Desk performs initial triage to determine if the event is a confirmed incident or a false positive
4. If confirmed as an incident, classify severity (P1–P4) and escalate to the IS Analyst on duty
5. IS Analyst assigns an Incident Reference Number (format: INC-[YEAR]-[SEQUENCE], e.g., INC-2026-001)

### Phase 2: Containment

**Immediate containment actions (within timeframes below):**

| Severity | Containment Target | Initial Containment Actions |
|---|---|---|
| P1 | < 1 hour | Isolate affected systems; invoke CISO and crisis team; invoke Crisis Communications Plan |
| P2 | < 4 hours | Restrict access to affected systems; notify CISO; preserve evidence |
| P3 | < 24 hours | Apply targeted containment; notify ISMS Manager; evidence preservation |
| P4 | < 5 business days | Apply corrective measures; log for tracking |

**Evidence Preservation:**
- Do NOT power off affected systems without CISO authorisation (forensic evidence may be lost)
- Preserve logs, screenshots, memory dumps, and access records as appropriate
- Document all actions taken with timestamps
- Use forensic imaging for critical systems where legally required

### Phase 3: Eradication

1. Identify root cause of the incident
2. Remove malicious code, unauthorised access, or exploited vulnerability
3. Apply patches, configuration changes, or access revocations as appropriate
4. Verify eradication through system scans and log analysis
5. Document all eradication steps

### Phase 4: Recovery

1. Restore systems from known clean backups where required
2. Verify system integrity before returning to production
3. Re-enable services progressively with enhanced monitoring
4. Test functionality before full restoration
5. Notify affected business units when systems are restored
6. Monitor for recurrence for a minimum of 72 hours post-recovery

### Phase 5: Post-Incident Review

Within 5 business days of incident closure (within 10 days for P1/P2):

1. Conduct Post-Incident Review (PIR) meeting
2. Document: timeline, root cause, impact, actions taken, regulatory notifications made
3. Identify lessons learned and improvement actions
4. Update the IS Incident Log with all findings
5. Raise corrective actions in the NCR register where systemic issues identified
6. Brief CISO and relevant stakeholders on findings
7. Update threat intelligence, detection rules, and response procedures as appropriate

---

## 4. Escalation and Notification

### 4.1 Internal Notification

| Severity | Who to Notify | When |
|---|---|---|
| P1 | CISO, CEO, CTO, Legal, PR/Comms, CFO | Within 1 hour |
| P2 | CISO, IT Manager, affected BU Head | Within 4 hours |
| P3 | ISMS Manager, IT Manager | Within 24 hours |
| P4 | ISMS Manager | Within 5 business days |

### 4.2 Regulatory Notification

| Regulator | Trigger | Deadline | Responsible |
|---|---|---|---|
| Information Commissioner's Office (ICO) | Personal data breach with risk to individuals (UK GDPR Art 33) | 72 hours from awareness | DPO + CISO |
| Financial Conduct Authority (FCA) | Material operational incident (SYSC 8.4) | Per FCA guidance (typically within 72 hours) | CISO + Legal |
| PCI DSS Acquirer / Card Brands | Payment card data compromise | Immediately upon discovery | CISO + Finance |
| National Cyber Security Centre (NCSC) | Nationally significant cyber incidents | As appropriate | CISO |

### 4.3 Customer Notification (Data Breaches)

Where a personal data breach poses a high risk to affected individuals:
- Notify affected data subjects "without undue delay" (UK GDPR Art 34)
- Communication approved by Legal, DPO, and CISO before issue
- Notification channel: email, letter, or online portal as appropriate
- Notification records retained in the breach register (minimum 5 years)

---

## 5. Incident Response Team

| Role | Responsibilities |
|---|---|
| Incident Commander (CISO for P1/P2; IS Analyst for P3/P4) | Overall incident management; decision authority; stakeholder briefing |
| IT Security Lead | Technical containment, eradication, and recovery |
| ISMS Manager | Evidence management, regulatory timeline tracking, documentation |
| DPO | GDPR assessment; ICO notification |
| Legal | Legal privilege; law enforcement liaison; contractual notification |
| PR/Comms | Customer and media communications (P1 only) |
| HR | Insider threat investigations |
| Third-Party IR Support | [TBD — contracted DFIR retainer] |

---

## 6. Incident Log

All incidents are recorded in the IS Incident Log (NFS-IS-REG-011) with the following minimum fields:

| Field | Description |
|---|---|
| Incident ID | INC-[YEAR]-[SEQUENCE] |
| Date/Time Detected | ISO 8601 timestamp |
| Date/Time Reported | ISO 8601 timestamp |
| Reported By | Name and role |
| Systems Affected | System names, IPs, services |
| Severity | P1–P4 |
| Incident Type | See taxonomy below |
| Description | Narrative description |
| Containment Actions | Steps taken with timestamps |
| Root Cause | Identified root cause |
| Impact | Business/data/regulatory impact |
| Regulatory Notifications | Regulator, date, reference |
| Date/Time Resolved | ISO 8601 timestamp |
| PIR Completed | Yes/No; date |
| Corrective Actions | NCR reference if raised |
| Status | Open / Contained / Resolved / Closed |

---

## 7. Incident Taxonomy

| Category | Types |
|---|---|
| Malware | Ransomware, virus, Trojan, spyware, cryptojacking |
| Phishing / Social Engineering | Phishing, spear-phishing, smishing, vishing, BEC |
| Unauthorised Access | Account compromise, privilege escalation, insider threat |
| Data Breach | Exfiltration, unintended disclosure, misdelivery |
| Availability | DDoS, system outage, ransomware lockout |
| Physical | Lost/stolen device, physical intrusion, CCTV tampering |
| Third-Party | Supplier breach, cloud provider incident |
| Configuration / Vulnerability | Exploited CVE, misconfiguration, unpatched system |

---

## 8. Related Documents

| Document | Reference |
|---|---|
| IS Incident Log | NFS-IS-REG-011 |
| Business Continuity IS Plan | NFS-IS-PLAN-004 |
| NCR / Corrective Action Register | NFS-IS-REG-012 |
| Breach Notification Procedure | NFS-DPO-PRO-003 |
| Communications Plan | NFS-IS-PLAN-002 |

---

*Nexus Financial Services Ltd | NFS-IS-PRO-004 v1.0*
*ISO/IEC 27001:2022 Annex A 5.24 (IS incident management planning), 5.25 (Assessment), 5.26 (Response), 5.27 (Lessons learned), 5.28 (Evidence collection)*
