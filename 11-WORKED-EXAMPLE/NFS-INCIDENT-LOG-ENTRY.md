# IS Incident Log — Worked Examples
## Nexus Financial Services Ltd

> **FICTIONAL REFERENCE ONLY — For educational purposes only.**
> All incidents described below are entirely fictional and created to demonstrate how IS incidents should be documented. Not real events.

**Document Reference:** NFS-IS-REG-011 (Excerpt — 2 entries)
**Version:** 1.0

---

## Incident Entry 1 — Phishing Attack with Credential Compromise

| Field | Detail |
|---|---|
| **Incident ID** | INC-2026-004 |
| **Date/Time Detected** | 2026-03-10T09:47:00Z |
| **Date/Time Reported** | 2026-03-10T09:52:00Z |
| **Reported By** | James Patel, IS Analyst (via SIEM alert) |
| **Systems Affected** | Microsoft 365 (email); Azure Active Directory |
| **Severity** | P2 — High |
| **Incident Type** | Phishing / Social Engineering; Unauthorised Access |
| **Status** | ✅ Closed |

### Description
At 09:47 on 10 March 2026, the NFS SIEM (Splunk) generated an alert for impossible travel — user account rachel.ford@nexusfs.co.uk authenticated from Manchester, UK at 09:30 and from an IP address geolocated to Lagos, Nigeria at 09:45. IS Analyst James Patel investigated and identified that Rachel Ford's Microsoft 365 account had been compromised following a phishing email sent on 08 March 2026. The phishing email appeared to come from an NFS IT Service Desk address (spoofed) and directed Rachel to a credential harvesting site. Rachel reported receiving the email but did not believe she had clicked the link; SIEM logs confirmed authentication from the Nigerian IP using valid credentials, suggesting credentials were harvested via the phishing site.

### Timeline

| Time | Action |
|---|---|
| 2026-03-08T14:22:00Z | Phishing email received by Rachel Ford; email blocked by DLP for other recipients |
| 2026-03-10T09:30:00Z | Legitimate authentication from Manchester (Rachel Ford) |
| 2026-03-10T09:45:00Z | Unauthorised authentication from Lagos, Nigeria |
| 2026-03-10T09:47:00Z | SIEM impossible travel alert triggered |
| 2026-03-10T09:52:00Z | IS Analyst escalates to CISO (Tom Briggs) |
| 2026-03-10T10:05:00Z | CISO authorises account reset and session revocation |
| 2026-03-10T10:08:00Z | IT Security revokes all active sessions; resets password; enables additional MFA |
| 2026-03-10T10:15:00Z | Incident confirmed as P2; ISMS Manager (Rachel Ford backup) begins documentation |
| 2026-03-10T11:30:00Z | Email forensics completed; no evidence of data exfiltration or lateral movement |
| 2026-03-10T14:00:00Z | Post-incident review scheduled; all clear confirmed |
| 2026-03-15T10:00:00Z | Post-incident review meeting held |

### Containment Actions
1. Account sessions immediately revoked (all active Microsoft 365 sessions terminated)
2. Password reset enforced via Azure AD
3. Additional Conditional Access policy applied to account (require MFA from all locations)
4. Phishing email domain added to email blocklist
5. All-staff alert issued regarding phishing campaign targeting NFS staff

### Root Cause
Rachel Ford clicked the phishing link and entered credentials on the spoofed site on 08 March 2026. The phishing email bypassed initial email filtering due to a legitimate-looking sender domain (nfs-itsupport.co.uk — not an NFS domain). DMARC was not yet enforced (project completed 31 March 2026 per CI-2026-008).

### Impact Assessment
- **Data Impact:** None confirmed — forensic review of account activity found no evidence of data access or exfiltration during the 15-minute unauthorised session. Only email inbox accessed.
- **Business Impact:** Minimal — account suspended for 35 minutes; Rachel Ford worked from backup account
- **Regulatory Impact:** Assessed by DPO — no personal data exfiltration confirmed; ICO notification not required (no high risk to individuals)
- **Financial Impact:** Nil

### Lessons Learned
1. DMARC enforcement (p=reject) would have blocked the phishing email — accelerated CI-2026-008
2. Impossible travel alerting worked correctly and contained the incident within 23 minutes of breach
3. Rachel Ford had not completed the Q4 2025 phishing simulation — flagged to ISMS Manager for training follow-up
4. All-staff phishing awareness communication issued

### Corrective Actions
| Action | Owner | Target | Status |
|---|---|---|---|
| Accelerate DMARC enforcement to p=reject | IT Security | 31 Mar 2026 | ✅ Completed (28 Mar 2026) |
| Mandatory phishing awareness for all staff who missed Q4 2025 simulation | ISMS Manager | 30 Apr 2026 | ✅ Completed |
| Review Conditional Access policies for all privileged accounts | CISO | 15 Apr 2026 | ✅ Completed |
| Update phishing email filter to block .co.uk lookalike domains | IT Security | 31 Mar 2026 | ✅ Completed |

### Post-Incident Review
- **PIR Date:** 2026-03-15
- **PIR Attendees:** CISO (Tom Briggs), ISMS Manager (Rachel Ford), IS Analyst (James Patel), DPO (Sarah Ahmed)
- **PIR Outcome:** All corrective actions agreed and tracked. No NCR raised — response was effective and timely. Improvements logged as CI-2026-008 (DMARC enforcement accelerated).

---

## Incident Entry 2 — Ransomware Attempt (Contained at Endpoint)

| Field | Detail |
|---|---|
| **Incident ID** | INC-2026-007 |
| **Date/Time Detected** | 2026-04-02T14:33:00Z |
| **Date/Time Reported** | 2026-04-02T14:33:00Z |
| **Reported By** | CrowdStrike EDR (automated detection) |
| **Systems Affected** | Single endpoint — NFS-LT-0847 (Branch Manager, Salford Branch) |
| **Severity** | P2 — High |
| **Incident Type** | Malware (Ransomware attempt) |
| **Status** | ✅ Closed |

### Description
CrowdStrike Falcon EDR detected and blocked a ransomware execution attempt on endpoint NFS-LT-0847 assigned to the Salford Branch Manager. The malware (identified as LockBit 3.0 variant) was delivered via a malicious macro in a Word document attached to an email purportedly from a supplier (invoice attachment). The EDR quarantined the process within 8 seconds of execution. No files were encrypted. SIEM confirmed no lateral movement or command-and-control communication.

### Timeline

| Time | Action |
|---|---|
| 2026-04-02T14:28:00Z | Malicious email received; Office macro warning displayed to user |
| 2026-04-02T14:31:00Z | User enabled macros and opened document |
| 2026-04-02T14:33:00Z | EDR (CrowdStrike Falcon) detects and quarantines ransomware process |
| 2026-04-02T14:33:00Z | SIEM alert generated; IS Analyst paged |
| 2026-04-02T14:38:00Z | IS Analyst confirms P2; isolates endpoint from network via EDR |
| 2026-04-02T14:45:00Z | CISO notified |
| 2026-04-02T15:30:00Z | Forensic image of endpoint taken |
| 2026-04-02T16:00:00Z | Malware sample submitted to threat intelligence platform |
| 2026-04-02T17:00:00Z | Confirmation: no encryption, no lateral movement, no exfiltration |
| 2026-04-03T09:00:00Z | Endpoint wiped and reimaged from golden image |
| 2026-04-03T10:00:00Z | User returned to service on clean device |
| 2026-04-08T10:00:00Z | Post-incident review conducted |

### Containment Actions
1. Endpoint isolated from network via EDR (immediate; remote isolation)
2. Endpoint forensically imaged before remediation
3. Malware quarantined and removed by EDR
4. Endpoint wiped and reimaged from hardened golden image
5. Supplier email domain added to email blocklist
6. NCSC notified via Early Warning Service (optional notification made)

### Root Cause
User enabled Office macros despite macro warning. NFS Group Policy blocks macros from internet-sourced files; however, email attachment was saved locally before opening, bypassing the Mark of the Web (MotW) control. Macro execution policy not enforced for locally-saved files.

### Impact Assessment
- **Data Impact:** None — no files encrypted; no data exfiltration confirmed
- **Business Impact:** Minimal — single endpoint unavailable for ~20 hours; branch continued using shared workstation
- **Regulatory Impact:** Assessed — no personal data affected; no FCA notification required; ICO notification not required
- **Financial Impact:** IT time only (~4 hours IS Analyst + 2 hours IT); replacement device not required

### Corrective Actions
| Action | Owner | Target | Status |
|---|---|---|---|
| Enforce macro blocking for all files regardless of source (registry policy) | IT Security | 30 Apr 2026 | ✅ Completed |
| Update email filtering to block .docm and macro-enabled files from external senders | IT Security | 15 Apr 2026 | ✅ Completed |
| Targeted macro security awareness for all branch staff | ISMS Manager | 30 Apr 2026 | ✅ Completed |
| Submit malware IOCs to NCSC and FS-ISAC | IS Analyst | 07 Apr 2026 | ✅ Completed |

---

## Incident Log Summary (INC-2026 Series — YTD as at 30 Apr 2026)

| ID | Date | Type | Severity | Status | Regulatory Notification |
|---|---|---|---|---|---|
| INC-2026-001 | Jan 2026 | Policy violation (data misdelivery) | P4 | Closed | None |
| INC-2026-002 | Jan 2026 | Lost laptop (remote worker) | P3 | Closed | None (device encrypted; wiped) |
| INC-2026-003 | Feb 2026 | Failed intrusion attempt (external) | P3 | Closed | None |
| INC-2026-004 | Mar 2026 | Phishing / credential compromise | P2 | Closed | None (no data exfiltration) |
| INC-2026-005 | Mar 2026 | DLP alert (false positive) | P4 | Closed | None |
| INC-2026-006 | Mar 2026 | Vulnerability exploited in test env | P3 | Closed | None |
| INC-2026-007 | Apr 2026 | Ransomware attempt (contained) | P2 | Closed | None (no impact) |

**YTD: 0 × P1 | 2 × P2 | 3 × P3 | 2 × P4 — Target P1: 0 ✅ | Target P2 ≤ 2/yr: ✅ (2 with 8 months remaining)**

---

*FICTIONAL REFERENCE ONLY — All incidents are fictional.*
*ISO/IEC 27001:2022 Annex A 5.24–5.28 — Information security incident management*
