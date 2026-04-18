# Information Security Risk Assessment Methodology

## ISO/IEC 27001:2022 | Clause 6.1.2

**Document ID:** ISMS-RISK-001
**Version:** 1.0 | **Owner:** CISO / ISMS Manager | **Date:** ___ | **Review Cycle:** Annual

---

## 1. Purpose

This document defines [Organisation Name]'s methodology for identifying, analysing, and evaluating information security risks in accordance with ISO/IEC 27001:2022 Clause 6.1.2. All IS risk assessments must be conducted using this methodology to ensure consistent and comparable results.

---

## 2. Risk Assessment Scope

IS risk assessments are conducted for:
- All information assets within the ISMS scope
- New systems, processes, or services before deployment
- Significant changes to existing systems
- After IS incidents
- At least annually as part of the ISMS review cycle

---

## 3. Risk Assessment Process

### Step 1: Asset Identification
Identify the information asset (or group of assets) to be assessed. All assets should be in the Information Asset Register (ISMS-ASSET-001).

### Step 2: Threat Identification
For each asset, identify the threats that could exploit vulnerabilities and cause harm. Threats include:
- **Technical threats:** Malware, ransomware, DDoS, vulnerability exploitation, data leakage
- **Human threats:** Phishing, insider threat, social engineering, accidental deletion
- **Physical threats:** Theft, fire, flood, power failure, hardware failure
- **Organisational threats:** Process failures, supplier failure, change management errors

### Step 3: Vulnerability Identification
Identify the weaknesses associated with the asset or its controls that could be exploited by a threat.

### Step 4: Impact Assessment
Assess the potential impact on Confidentiality, Integrity, and/or Availability if the risk materialises.

### Step 5: Likelihood Assessment
Assess the likelihood of the risk materialising, taking into account existing controls.

### Step 6: Risk Score Calculation
Calculate the inherent and residual risk scores using the matrices below.

### Step 7: Risk Evaluation
Compare risk scores against the risk acceptance criteria to determine whether treatment is required.

### Step 8: Risk Treatment Decision
Select treatment option and document in the Risk Treatment Plan.

---

## 4. Risk Scoring Criteria

### 4.1 Likelihood Scale

| Score | Label | Definition |
|---|---|---|
| 1 | Rare | Unlikely to occur; no known incidents; strong controls in place |
| 2 | Unlikely | Could occur but unlikely; few known incidents |
| 3 | Possible | Might occur; some known incidents in the sector |
| 4 | Likely | Will probably occur; recurring incidents |
| 5 | Almost Certain | Expected to occur; frequent incidents; known active threats |

### 4.2 Impact Scale

| Score | Label | Confidentiality | Integrity | Availability | Business Impact |
|---|---|---|---|---|---|
| 1 | Negligible | Minimal data exposure | Minor data error | < 1 hour outage | Negligible financial/reputational harm |
| 2 | Minor | Limited internal data | Detectable error; correctable | 1–4 hour outage | Minor operational disruption |
| 3 | Moderate | Significant internal data or limited personal data | Significant error affecting operations | 4–24 hour outage | Moderate financial loss or regulatory attention |
| 4 | Significant | Large volume PII or sensitive data | Data corruption with operational impact | 1–7 day outage | Significant financial loss, regulatory investigation |
| 5 | Catastrophic | Breach of highly sensitive data (financial, health, special category) | Irrecoverable data corruption | > 7 day outage | Existential threat; major regulatory penalty |

### 4.3 Risk Score Matrix

| | **Impact 1** | **Impact 2** | **Impact 3** | **Impact 4** | **Impact 5** |
|---|---|---|---|---|---|
| **Likelihood 5** | 5 | 10 | 15 | 20 | 25 |
| **Likelihood 4** | 4 | 8 | 12 | 16 | 20 |
| **Likelihood 3** | 3 | 6 | 9 | 12 | 15 |
| **Likelihood 2** | 2 | 4 | 6 | 8 | 10 |
| **Likelihood 1** | 1 | 2 | 3 | 4 | 5 |

### 4.4 Risk Rating

| Score | Rating | Description | Action Required |
|---|---|---|---|
| 1–3 | LOW | Acceptable risk | Monitor only; review annually |
| 4–6 | MEDIUM | Tolerable with controls | Active monitoring; additional controls considered |
| 7–12 | HIGH | Requires treatment | Treatment plan required; escalate to CISO |
| 13–25 | CRITICAL | Unacceptable | Immediate treatment required; senior management notification |

---

## 5. Risk Acceptance Criteria

| Risk Level | Acceptance Criteria |
|---|---|
| LOW (1–3) | Accepted without treatment — documented and monitored |
| MEDIUM (4–6) | Accepted with existing controls — documented; treatment considered |
| HIGH (7–12) | Not accepted without treatment plan — CISO sign-off required |
| CRITICAL (13–25) | Not accepted — immediate senior management action required |

**Risk appetite statement:** [Organisation Name] has a [LOW / MEDIUM] risk appetite for information security risks affecting customer data, financial data, and operational continuity.

---

## 6. Risk Treatment Options

| Option | Description | When to Use |
|---|---|---|
| **Modify (Treat)** | Implement controls to reduce likelihood or impact | Most IS risks — preferred option |
| **Avoid** | Change the activity that causes the risk | When risk cannot be reduced to acceptable level |
| **Transfer** | Shift risk to third party (insurance, outsourcing) | When another party is better placed to manage |
| **Accept** | Tolerate the risk without treatment | LOW / MEDIUM risks within appetite; formally documented |
| **Share** | Distribute risk between parties | Joint ventures; shared infrastructure |

---

## 7. Risk Assessment Frequency

| Trigger | Frequency | Action |
|---|---|---|
| Planned review | Annual | Full risk register review |
| Significant system change | On change | Assessment of affected assets |
| New system / service | Before go-live | Full IS risk assessment |
| IS incident | Within 30 days | Post-incident risk review |
| Regulatory change | On change | Legal requirements review |
| Context change | On change | Review affected risks |

---

## 8. Risk Register Management

All identified risks are recorded in the Information Security Risk Register (ISMS-RISKRG-001). The risk register includes:
- Risk ID and title
- Asset affected
- Threat and vulnerability
- CIA dimension affected
- Inherent risk (before controls)
- Current controls
- Residual risk (after controls)
- Risk owner
- Treatment plan reference
- Review date

---

## Review History

| Version | Date | Changes | Approved By |
|---|---|---|---|
| 1.0 | | Initial issue | |

---

*ISO/IEC 27001:2022 ISMS Toolkit | Risk Assessment Methodology | Clause 6.1.2 | See root README.md for full index*
