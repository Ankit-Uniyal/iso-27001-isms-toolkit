# Annex A — Theme 7: Physical Controls
## ISO/IEC 27001:2022 — Controls 7.1 to 7.14

**Document Reference:** NFS-IS-REG-017
**Version:** 1.0
**Effective Date:** 01 May 2026

> **IMPORTANT DISCLAIMER:** This document provides a reference guide and implementation notes for ISO/IEC 27001:2022 Annex A Theme 7 controls. It does NOT reproduce the text of the ISO standard. Control titles and numbers are used for reference only. For the normative control text, practitioners must consult the official ISO/IEC 27001:2022 and ISO/IEC 27002:2022 publications.

---

## Overview

Theme 7 contains **14 physical controls** covering the protection of premises, equipment, and information from physical threats including unauthorised access, theft, damage, and environmental hazards.

| Control Range | Topics |
|---|---|
| 7.1–7.4 | Physical perimeters, entry controls, offices and facilities, physical security monitoring |
| 7.5–7.7 | Protection against threats, working in secure areas, clear desk/screen |
| 7.8–7.14 | Equipment siting, utilities, cabling, maintenance, off-premises, disposal |

---

## Control Reference Table

| Control | Title | Type | NIST CSF | CIS v8 | NFS Status |
|---|---|---|---|---|---|
| 7.1 | Physical security perimeters | Preventive | PR.AC | 12.1 | ✅ Implemented |
| 7.2 | Physical entry | Preventive | PR.AC | 12.2 | ✅ Implemented |
| 7.3 | Securing offices, rooms and facilities | Preventive | PR.AC | 12.3 | ✅ Implemented |
| 7.4 | Physical security monitoring | Detective | DE.CM | 12.4 | ✅ Implemented |
| 7.5 | Protecting against physical and environmental threats | Preventive | PR.IP | 12.5 | ✅ Implemented |
| 7.6 | Working in secure areas | Preventive | PR.AC | 12.6 | ✅ Implemented |
| 7.7 | Clear desk and clear screen | Preventive | PR.DS | 4.3 | ✅ Implemented |
| 7.8 | Equipment siting and protection | Preventive | PR.IP | 12.7 | ✅ Implemented |
| 7.9 | Security of assets off-premises | Preventive | PR.DS | 1.2 | ✅ Implemented |
| 7.10 | Storage media | Preventive | PR.DS | 3.5 | ✅ Implemented |
| 7.11 | Supporting utilities | Preventive | PR.IP | 12.9 | ✅ Implemented |
| 7.12 | Cabling security | Preventive | PR.IP | 12.10 | ✅ Implemented |
| 7.13 | Equipment maintenance | Preventive | PR.MA | 12.11 | ✅ Implemented |
| 7.14 | Secure disposal or re-use of equipment | Preventive | PR.DS | 3.5 | ✅ Implemented |

---

## Implementation Notes

### 7.1 — Physical Security Perimeters
**Purpose:** Define and protect physical boundaries around areas containing sensitive information or IT equipment.

**Key requirements:**
- Clearly defined perimeters with physical barriers (walls, fences, locked doors)
- Perimeters proportionate to the sensitivity of the information protected
- All entry points controlled and monitored
- Perimeters regularly inspected for weaknesses

**NFS implementation:** Four-zone perimeter model (Public → Controlled → Restricted → Secure) as defined in Physical Security Policy (NFS-IS-POL-010).

**Audit evidence:** Site plans showing security zones; access control system configuration; physical inspection records.

---

### 7.2 — Physical Entry Controls
**Purpose:** Restrict physical access to areas containing information assets.

**Key requirements:**
- Controlled entry to all zones containing sensitive information
- Authentication at entry points (card, PIN, biometric)
- Visitor management process (sign-in, escort, badge)
- Access rights assigned based on business need
- Access logs maintained and reviewed

**NFS implementation:** Proximity card + PIN for Zone 2; biometric + card for Zone 3 (data centre). Visitor log maintained at reception. Access reviewed quarterly.

**Audit evidence:** Access control system logs; visitor log; access provisioning records; quarterly access review records.

**Common gaps:** Tailgating not addressed; no visitor log; access cards not deactivated on leaving; no logging of entry/exit.

---

### 7.3 — Securing Offices, Rooms and Facilities
**Purpose:** Protect office areas and rooms from unauthorised physical access.

**Key requirements:**
- Offices and rooms containing sensitive information locked when unoccupied
- Key management process for physical keys
- Reception/lobby controls
- Meeting rooms used for sensitive discussions appropriately protected

**Audit evidence:** Key register; physical inspection checklist; CCTV footage availability.

---

### 7.4 — Physical Security Monitoring
**Purpose:** Detect and deter unauthorised physical access attempts.

**Key requirements:**
- CCTV covering all entry/exit points and sensitive areas
- CCTV footage retained for appropriate period
- Intruder detection systems at all premises
- Monitoring of physical access logs
- Alert processes for out-of-hours access

**NFS implementation:** CCTV at all NFS premises; footage retained 31 days (90 days at data centre). Access logs retained 12 months and reviewed monthly.

**Audit evidence:** CCTV system configuration; footage retention policy; access log review records; alarm test certificates.

---

### 7.5 — Protecting Against Physical and Environmental Threats
**Purpose:** Protect information assets from natural and man-made physical threats.

**Key requirements:**
- Risk assessment of physical and environmental threats (flood, fire, power failure, extreme weather)
- Appropriate mitigations implemented based on risk
- Critical systems protected from environmental hazards
- Regular inspection and testing of environmental controls

**NFS implementation:** Data centre on upper floors (flood risk mitigation); gas-based fire suppression; temperature/humidity monitoring with automated alerts; annual physical risk assessment.

**Audit evidence:** Physical risk assessment; environmental monitoring records; fire suppression test certificates; temperature/humidity logs.

---

### 7.6 — Working in Secure Areas
**Purpose:** Additional controls for work conducted in secure/restricted areas.

**Key requirements:**
- Work in secure areas only for authorised purposes
- Restrictions on personal devices (cameras, phones) in highest security zones
- Lone working restrictions in highest security areas
- Logging of access to and work in secure areas

**NFS implementation:** Lone working prohibited in Zone 3 (data centre). Mobile phones restricted in Zone 3 without CISO approval. Zone access logged.

---

### 7.7 — Clear Desk and Clear Screen
**Purpose:** Reduce risk of unauthorised access, loss, or damage to information from physical observation.

**Key requirements:**
- Sensitive documents locked away when not in use
- No sensitive information visible to passersby or on unattended screens
- Screen lock policy enforced (5 minute auto-lock)
- Shredding facilities for paper disposal
- Whiteboard/flipchart content erased after use

**NFS implementation:** Screen lock enforced via Group Policy (5 minutes). Cross-cut shredders in all NFS offices. Privacy screens issued to mobile workers.

**Audit evidence:** Group Policy configuration showing screen lock; shredder provision; privacy screen distribution records; spot-check audit results.

**Common gaps:** No enforcement of auto-lock (policy only); no shredders provided; clear desk policy not communicated.

---

### 7.9 — Security of Assets Off-Premises
**Purpose:** Protect information assets used or accessed outside NFS premises.

**Key requirements:**
- Security for assets used off-premises (laptops, phones, documents)
- Encryption mandatory for portable devices
- Reporting process for lost/stolen devices
- No unattended sensitive information in vehicles or public spaces

**NFS implementation:** Full disk encryption on all NFS laptops (BitLocker). MDM with remote wipe. Lost/stolen device reporting within 1 hour.

**Audit evidence:** Laptop encryption configuration; MDM enrolment records; lost device reports; remote wipe records.

---

### 7.10 — Storage Media
**Purpose:** Manage and protect removable storage media throughout its lifecycle.

**Key requirements:**
- Inventory of removable media
- Authorisation required for use of removable media
- Encryption for media containing sensitive information
- Secure disposal of removable media

**NFS implementation:** Removable media use requires CISO pre-approval. All authorised removable media encrypted (VeraCrypt or equivalent). Disposal via certified media destruction.

---

### 7.11 — Supporting Utilities
**Purpose:** Protect information assets from power failures and utility outages.

**Key requirements:**
- UPS for critical IT equipment
- Backup power generation capability
- Regular testing of power failure procedures
- Redundant utility supplies where feasible

**NFS implementation:** UPS at all server rooms. Diesel generator at data centre (tested monthly). Dual power feeds at primary data centre.

**Audit evidence:** UPS specifications; generator test records; utility failure exercise results.

---

### 7.14 — Secure Disposal or Re-Use of Equipment
**Purpose:** Prevent unintended disclosure of information from equipment being disposed of or reused.

**Key requirements:**
- All storage media verified as overwritten or destroyed before disposal or reuse
- Certificate of destruction obtained for data centre hardware
- Process for returning leased equipment (data wiped first)
- Records of disposal maintained

**NFS implementation:** NIST 800-88 compliant overwriting or physical destruction. Certificate of destruction required for all data centre hardware disposals. Disposal records retained 3 years.

**Audit evidence:** Data disposal procedure; certificates of destruction; disposal register; evidence of overwrite tool usage.

**Common gaps:** No formal disposal process; equipment disposed without data wiping; no certificates of destruction.

---

## Theme 7 — Key Risk Areas for Financial Services

| Risk | Controls | NFS Mitigation |
|---|---|---|
| Physical intrusion into server rooms | 7.1, 7.2, 7.4 | Biometric + card access; 24/7 CCTV; Zone 3 dual-person |
| Laptop theft (branch/remote) | 7.9, 7.7 | BitLocker; MDM remote wipe; privacy screens |
| Data on disposed equipment | 7.14 | NIST 800-88 wipe; certificate of destruction |
| Environmental damage to data centre | 7.5, 7.11 | Upper floor DC; gas suppression; UPS + generator |
| Unauthorised visitor access | 7.2, 7.4 | Visitor log; escort policy; CCTV |
| Physical social engineering (tailgating) | 7.1, 7.2 | Mantrap at data centre; staff awareness training |

---

*This reference guide covers ISO/IEC 27001:2022 Annex A Theme 7 — Physical Controls (7.1–7.14)*
*For normative control requirements, refer to ISO/IEC 27001:2022 and ISO/IEC 27002:2022*
