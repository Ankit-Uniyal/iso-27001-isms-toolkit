# Document Control Procedure
## ISO/IEC 27001:2022 — Clause 7.5

**Organisation:** Nexus Financial Services Ltd (NFS)
**Document Reference:** NFS-IS-PRO-007
**Version:** 1.0
**Effective Date:** 01 May 2026
**Review Date:** 01 May 2027
**Owner:** ISMS Manager
**Approved By:** Chief Information Security Officer

---

## 1. Purpose and Scope

### 1.1 Purpose
This procedure establishes the controls required for the creation, review, approval, distribution, maintenance, retention, and disposal of documented information within the NFS Information Security Management System (ISMS). It ensures all ISMS documents are current, authorised, legible, and available to those who need them.

### 1.2 Scope
This procedure applies to all documented information required by ISO/IEC 27001:2022, including:
- Policies, procedures, standards, and guidelines
- Plans and programmes (risk treatment, audit, awareness)
- Registers and logs (risk register, asset register, incident log)
- Records and evidence (audit reports, training records, management review minutes)
- External documents referenced by the ISMS (legislation, standards, regulations)

---

## 2. Document Types and Hierarchy

| Level | Type | Description | Examples |
|---|---|---|---|
| L1 | Policy | High-level strategic intent, Board-approved | IS Policy, AUP |
| L2 | Standard | Mandatory requirements derived from policies | Cryptography Standard, Password Standard |
| L3 | Procedure | Step-by-step processes for implementing standards | Incident Response Procedure, Access Control Procedure |
| L4 | Guideline / Work Instruction | Non-mandatory guidance and best practice | Secure Coding Guide, Remote Working Guidance |
| L5 | Record / Evidence | Completed templates; evidence of activity | Risk register entries, audit reports, training records |

---

## 3. Document Identification and Naming Convention

### 3.1 Document Reference Format

All ISMS documents follow the reference format:
```
NFS-[DOMAIN]-[TYPE]-[SEQUENCE]
```

| Code | Domain | Code | Type |
|---|---|---|---|
| IS | Information Security | POL | Policy |
| DPO | Data Protection | PRO | Procedure |
| IT | Information Technology | STD | Standard |
| HR | Human Resources | PLAN | Plan / Programme |
| RK | Risk | REG | Register |
| AUD | Audit | RPT | Report |
| — | — | TMP | Template |

**Examples:** NFS-IS-POL-001 (Information Security Policy), NFS-IS-PRO-004 (Incident Response Procedure)

### 3.2 Version Numbering

| Change Type | Version Increment | Example |
|---|---|---|
| Major revision (structural change) | +1.0 | 1.0 → 2.0 |
| Minor revision (content update) | +0.1 | 1.0 → 1.1 |
| Administrative amendment (typos, formatting) | +0.0.1 | 1.0 → 1.0.1 |

---

## 4. Document Lifecycle

### 4.1 Creation

1. Document owner drafts new document using the approved template
2. Draft includes: title, reference, version, date, owner, classification, scope, content
3. Owner conducts self-review for accuracy, completeness, and alignment with policy hierarchy
4. Draft submitted to ISMS Manager for technical review

### 4.2 Review

1. ISMS Manager reviews for ISMS alignment, accuracy, and completeness
2. Subject matter experts (SMEs) consulted where required
3. Legal/Compliance review for documents with regulatory implications
4. Review comments returned to document owner within 10 working days
5. Owner revises document and resubmits

### 4.3 Approval

| Document Level | Approver |
|---|---|
| L1 Policy | Board of Directors |
| L2 Standard | CISO |
| L3 Procedure | CISO or ISMS Manager (delegated) |
| L4 Guideline | ISMS Manager |
| L5 Record | ISMS Manager (template approval only) |

Approval is recorded via electronic signature in the Document Management System (SharePoint) or via the approval section of the document itself.

### 4.4 Publication and Distribution

1. Approved document uploaded to the ISMS SharePoint document library
2. Previous version moved to the Archive folder
3. All staff notified via email for L1 and L2 documents
4. Affected teams notified for L3–L4 documents
5. ISMS Document Master List updated by ISMS Manager

### 4.5 Review Schedule

| Document Level | Review Frequency | Trigger Events |
|---|---|---|
| L1 Policy | Annual (minimum) | Regulatory change, major incident, business change |
| L2 Standard | Annual | Technology change, regulatory change |
| L3 Procedure | Annual or when process changes | Process change, incident lessons learned |
| L4 Guideline | Biennial | Significant change in guidance or technology |
| L5 Record | N/A (completed at time of use) | N/A |

All documents display a "Review Date" field. The ISMS Manager sends review reminders 4 weeks before the due date.

### 4.6 Obsolescence and Disposal

1. Documents superseded by a new version are marked "OBSOLETE" and moved to the Archive folder
2. Obsolete documents are retained for the minimum period defined in the retention schedule (see Section 6)
3. Obsolete documents are removed from all active distribution lists
4. Hard copies of obsolete documents must be destroyed using approved secure disposal

---

## 5. External Documents

External documents referenced by the ISMS (legislation, standards, regulations) are:
- Listed in the ISMS Document Master List with source, version/date, and responsible owner
- Monitored for updates by the responsible owner
- Updated in the register when new versions are published

---

## 6. Document Retention Schedule

| Document Category | Minimum Retention Period | Disposal Method |
|---|---|---|
| L1–L3 Active documents | Duration of use + 3 years after supersession | Secure deletion |
| Audit reports and findings | 3 years | Secure deletion |
| Incident records | 5 years | Secure deletion |
| Training and awareness records | 3 years | Secure deletion |
| Management review minutes | 3 years | Secure deletion |
| Risk register (all versions) | 5 years | Secure deletion |
| Regulatory correspondence | 7 years | Secure deletion |
| Legal holds | Per legal instruction | Per legal instruction |

---

## 7. Document Control System

NFS uses Microsoft SharePoint as the primary ISMS Document Management System. Access is controlled as follows:

| User Group | Access Level |
|---|---|
| All NFS Staff | Read — published L1–L4 documents |
| ISMS Team | Read/Write — all active ISMS documents |
| Document Owners | Read/Write — their own documents |
| ISMS Manager | Read/Write/Approve — all documents |
| CISO | Full control |

---

## 8. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Document Owner | Creates, maintains, and reviews their documents; ensures accuracy and currency |
| ISMS Manager | Manages ISMS document library, Document Master List, and review schedule |
| CISO | Approves L2 documents; provides oversight of document control system |
| Board | Approves L1 policies |
| All Staff | Reads and complies with current versions of relevant ISMS documents |

---

## 9. Document Control in External Parties

Where ISMS documents are shared with external parties (auditors, regulators, suppliers):
- Only approved, current versions may be shared
- Sharing requires CISO approval for L1–L2 documents
- All external sharing is logged in the Document Sharing Register
- Recipients must be advised that the document is confidential and for their use only

---

*Nexus Financial Services Ltd | NFS-IS-PRO-007 v1.0*
*ISO/IEC 27001:2022 Clause 7.5 — Documented Information*
