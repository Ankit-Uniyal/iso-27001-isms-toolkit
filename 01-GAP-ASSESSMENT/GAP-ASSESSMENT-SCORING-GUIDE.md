# Gap Assessment Scoring Guide
## ISO/IEC 27001:2022 — How to Score and Interpret Your Gap Assessment

**Document Reference:** NFS-IS-PLAN-GAP-002
**Version:** 1.0
**Effective Date:** 01 May 2026
**Owner:** ISMS Manager
**For Use With:** ISO27001-GAP-ASSESSMENT-CHECKLIST.md

---

## 1. Purpose

This guide explains how to use the Gap Assessment Scoring system to rate your organisation's current compliance with ISO/IEC 27001:2022, calculate overall readiness scores, prioritise remediation actions, and produce a gap assessment report for management.

---

## 2. The Scoring Scale

Each control and clause requirement in the Gap Assessment Checklist is scored on a **0–4 maturity scale**:

| Score | Level | Description | Typical Indicators |
|---|---|---|---|
| **0** | Not Started | No awareness or implementation of the requirement | No policy, no process, no controls; staff unaware of requirement |
| **1** | Initial / Ad Hoc | Awareness exists; some informal activity | Some informal practices; not documented; inconsistently applied |
| **2** | Developing / Documented | Control or process exists but is not fully implemented or consistently applied | Documented procedure exists; partial implementation; not monitored |
| **3** | Defined / Implemented | Control is implemented, documented, and consistently applied | Formal process; consistent application; periodic review; some monitoring |
| **4** | Managed / Optimised | Control is fully implemented, monitored, measured, and continually improved | Metrics tracked; management review; continual improvement; audit evidence available |

---

## 3. How to Score Each Item

### Step 1: Read the Requirement
Review the clause or control requirement in the checklist. Refer to ISO/IEC 27001:2022 for the full control text.

### Step 2: Gather Evidence
Before scoring, collect evidence of existing controls:
- Policies and procedures (documented)
- Records and logs (training records, audit records, incident logs)
- System configurations and technical controls
- Interview results (staff awareness, management knowledge)
- Observation (physical walk-through, system demonstrations)

### Step 3: Assign a Score (0–4)
Use the scoring scale above. Be objective and evidence-based. Where in doubt, score conservatively (round down).

**Scoring guidance for common situations:**
- Policy exists but staff are unaware → score 2 (not 3)
- Control implemented but not documented → score 2 (not 3)
- Control documented and implemented but not monitored or reviewed → score 3 (not 4)
- Ad-hoc patching without a formal process → score 1

### Step 4: Record Observations and Evidence
Document what evidence was reviewed and any gaps identified. This creates the audit trail for the assessment.

---

## 4. Calculating Scores

### 4.1 Section Score

For each section (e.g., Clause 4, Theme 5 Controls):

```
Section Score (%) = (Sum of all scores in section / Maximum possible score) × 100
Maximum possible score = Number of requirements × 4
```

**Example — Clause 4 (Context), 4 requirements:**
- 4.1 Context of organisation: 3
- 4.2 Interested parties: 3
- 4.3 Scope: 4
- 4.4 ISMS processes: 2
- Sum = 12; Maximum = 16
- **Section Score = (12/16) × 100 = 75%**

### 4.2 Overall ISMS Readiness Score

```
Overall Score (%) = (Total score across ALL requirements / Maximum possible total) × 100
```

For ISO 27001:2022 with the full checklist (Clauses 4–10 + all 93 Annex A controls):
- Clause requirements: ~45 items
- Annex A controls: 93 items
- Total items: ~138
- Maximum possible: 138 × 4 = 552

---

## 5. Interpreting Your Score

### 5.1 Overall Readiness Rating

| Score | Rating | Interpretation | Estimated Certification Readiness |
|---|---|---|---|
| 0–25% | Level 1 — Initial | Major gaps across most requirements; significant work needed | Not ready; 18–24+ months to certification |
| 26–50% | Level 2 — Developing | Foundation exists in some areas; substantial gaps remain | Not ready; 12–18 months to certification |
| 51–70% | Level 3 — Defined | Most processes documented; implementation gaps remain | Approaching readiness; 6–12 months to certification |
| 71–85% | Level 4 — Managed | Most controls implemented; some gaps and improvements needed | Near-ready; 3–6 months to certification |
| 86–95% | Level 5 — Optimised | Controls implemented and monitored; minor gaps only | Ready to proceed to pre-certification audit |
| 96–100% | Level 5+ — Audit Ready | All controls implemented with evidence; continual improvement active | Ready for Stage 1 + Stage 2 certification audit |

### 5.2 Section-Level Interpretation

| Section Score | Priority Action |
|---|---|
| < 50% | Critical gap — immediate remediation programme required |
| 50–70% | High priority — structured improvement plan needed within 90 days |
| 71–85% | Medium priority — improvement actions within 180 days |
| 86–95% | Low priority — fine-tuning and evidence gathering |
| > 95% | Maintain — ensure ongoing monitoring and review |

---

## 6. Gap Assessment Report Structure

After completing the gap assessment, produce a report with the following sections:

### Recommended Report Structure

1. **Executive Summary** — Overall score, key strengths, critical gaps, and readiness rating
2. **Methodology** — Assessment scope, team, dates, evidence sources, scoring approach
3. **Section Scores** — Score per clause and Annex A theme with visual chart/heatmap
4. **Critical Gaps** (score 0–1) — Detail and immediate action required
5. **High Priority Gaps** (score 2) — Detail and 90-day action plan
6. **Improvement Opportunities** (score 3) — Actions to reach score 4
7. **Strengths** (score 4) — Controls that are fully implemented and should be maintained
8. **Recommended Roadmap** — Prioritised 12-month implementation plan with milestones
9. **Resources Required** — Estimated effort, cost, and skills

---

## 7. Prioritisation Framework

When multiple gaps exist, prioritise remediation using this matrix:

| Priority | Criteria | Examples |
|---|---|---|
| **P1 — Immediate** | Score 0 on mandatory clause (4–10); regulatory obligation at risk; active risk with no controls | No IS policy; no incident response process; no risk assessment |
| **P2 — High** | Score 0–1 on Annex A control; Highly Restricted data unprotected; legal obligation | No access controls on customer data; no encryption on mobile devices |
| **P3 — Medium** | Score 2 on important controls; monitoring or review gaps | Controls in place but undocumented; no annual review |
| **P4 — Low** | Score 3; optimisation needed; nice-to-have improvements | Metrics not yet formal; improvement log not maintained |

---

## 8. Using the Gap Assessment for Certification Planning

### Phase 1: Gap Assessment (Weeks 1–4)
- Complete all checklist sections
- Score every requirement
- Identify P1 and P2 gaps

### Phase 2: Remediation Planning (Weeks 4–6)
- Convert gaps to project actions
- Assign owners and target dates
- Prioritise per framework above
- Present to management

### Phase 3: Remediation Implementation (Months 2–12)
- Execute remediation actions
- Document evidence as you go
- Quarterly progress reviews

### Phase 4: Pre-Certification Readiness Review (Month 10–11)
- Re-run gap assessment
- Target: ≥ 90% across all sections
- Engage certification body for Stage 1 audit

### Phase 5: Certification Audit
- Stage 1 (Document review) — typically 1–2 days
- Stage 2 (Implementation audit) — typically 2–5 days depending on scope

---

## 9. Re-Assessment Frequency

| Trigger | Action |
|---|---|
| Annual (minimum) | Full gap assessment re-run; compare to prior year |
| Major organisational change | Partial re-assessment of affected areas |
| Significant incident | Re-assess controls in incident area |
| Pre-certification / pre-surveillance | Full re-assessment to confirm readiness |
| After significant Annex A control changes | Re-assess affected theme |

---

## 10. Tools and Templates

| Tool | Description |
|---|---|
| ISO27001-GAP-ASSESSMENT-CHECKLIST.md | Complete 93-control + clause gap assessment checklist |
| 12-SCRIPTS/isms_gap_checker.py | Python script to calculate scores from CSV input |
| 05-CLAUSE6-PLANNING/STATEMENT-OF-APPLICABILITY.md | SoA template to track control implementation status |
| 05-CLAUSE6-PLANNING/RISK-ASSESSMENT-METHODOLOGY.md | Risk assessment to prioritise remediation |

---

*ISO/IEC 27001:2022 ISMS Toolkit | Gap Assessment Scoring Guide*
*For use with: 01-GAP-ASSESSMENT/ISO27001-GAP-ASSESSMENT-CHECKLIST.md*
