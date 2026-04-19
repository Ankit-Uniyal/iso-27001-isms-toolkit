# Physical and Environmental Security Policy
## ISO/IEC 27001:2022 — Annex A 7.1–7.14

**Organisation:** Nexus Financial Services Ltd (NFS)
**Document Reference:** NFS-IS-POL-010
**Version:** 1.0
**Effective Date:** 01 May 2026
**Review Date:** 01 May 2027
**Owner:** Head of Facilities (with CISO oversight)
**Approved By:** Chief Information Security Officer

---

## 1. Purpose and Scope

### 1.1 Purpose
This policy defines NFS's requirements for protecting information assets from physical and environmental threats including unauthorised physical access, theft, damage, and disruption. It ensures NFS premises, equipment, and information are protected proportionate to their sensitivity.

### 1.2 Scope
This policy applies to all NFS premises including:
- Head Office (Manchester)
- 14 regional branch locations
- Data centre facilities (primary and secondary)
- Remote working environments (where NFS equipment is used)
- Third-party co-location facilities hosting NFS equipment

---

## 2. Physical Security Perimeters (Annex A 7.1)

NFS premises are protected by defined physical security perimeters:

| Perimeter Zone | Description | Controls Applied |
|---|---|---|
| Zone 0 — Public | Publicly accessible (reception, lobby) | CCTV; reception desk staffed during business hours |
| Zone 1 — Controlled | General office areas | Swipe card / fob access; visitor sign-in required |
| Zone 2 — Restricted | IT rooms, server rooms, HR, Finance | Dual-factor physical access (card + PIN); access log maintained |
| Zone 3 — Secure | Data centre, vault, DR site | Dual-person integrity; biometric + card; 24/7 CCTV; mantrap at data centre |

Physical perimeters must be clearly identifiable and all entry points must be secured.

---

## 3. Physical Entry Controls (Annex A 7.2)

### 3.1 Staff Access

- All permanent staff issued with photo ID badge and proximity access card on Day 1
- Access rights set according to role; provisioned by IT in consultation with Facilities
- Access cards must be worn visibly at all times within NFS premises
- Lost or stolen access cards must be reported immediately to IT Service Desk; card deactivated within 1 hour
- Access cards returned on last day of employment; leavers procedure applies

### 3.2 Visitor Management

- All visitors must sign in at reception; photo ID verified
- Visitors issued with a dated visitor badge valid for the day only
- Visitors must be escorted by a named NFS employee at all times in Zone 1 and above
- Visitor access to Zone 2/3 requires prior written approval from the relevant department head
- Visitor log retained at reception for 12 months

### 3.3 Contractor and Maintenance Access

- Contractors require prior approval and documented scope of work
- IT contractors accessing Zone 2/3 must be accompanied by an NFS IT team member
- Out-of-hours contractor access requires CISO or Facilities Manager sign-off
- All maintenance work on IT equipment logged in the Asset Maintenance Record

---

## 4. Securing Offices, Rooms, and Facilities (Annex A 7.3)

- Office areas must be locked outside of business hours
- Confidential information must not be visible from public areas (screens, whiteboards, documents)
- Meeting rooms used for confidential discussions must have no external windows or be in Zone 2+
- Server rooms and IT equipment rooms must be locked at all times
- Keys to secure areas held by designated key custodians; key register maintained by Facilities

---

## 5. Physical Security Monitoring (Annex A 7.4)

- CCTV installed at all entry/exit points and Zone 2/3 areas at all NFS premises
- CCTV footage retained for minimum 31 days (90 days at data centre)
- CCTV system monitored by security personnel during business hours; recorded 24/7
- Physical access logs (electronic door systems) retained for 12 months
- Intruder alarm systems installed at all premises; tested quarterly
- Alarm response times agreed with security provider (target: < 10 minutes out of hours)

---

## 6. Protection Against Physical and Environmental Threats (Annex A 7.5)

- Risk assessments conducted for physical and environmental threats (flood, fire, power failure) at all premises
- Physical threat register maintained by Facilities, reviewed annually
- Data centre located on upper floors; flood risk assessment completed
- Fire suppression systems installed in all data centre and server rooms (gas-based; non-water)
- Fire detection systems tested bi-annually
- Temperature and humidity monitoring in data centres; automated alerts for out-of-range conditions

---

## 7. Working in Secure Areas (Annex A 7.6)

- Work in Zone 2/3 areas must be for authorised purposes only
- Lone working in Zone 3 (data centre) is prohibited
- Personal mobile phones and cameras restricted in Zone 3 without explicit CISO approval
- All work in secure areas logged in the Zone Access Register

---

## 8. Clear Desk and Clear Screen Policy (Annex A 7.7)

**Clear Desk:**
- Confidential and Highly Restricted documents must be secured in locked drawers or filing cabinets when not in use
- No Highly Restricted documents left unattended on desks overnight
- Whiteboards and flipcharts containing sensitive information must be erased after use
- Shredding bins (cross-cut) provided in all office areas for paper disposal

**Clear Screen:**
- Computer screens must be locked after 5 minutes of inactivity (enforced by Group Policy)
- Users must lock screens manually (Windows Key + L) when leaving their workstation
- Screens must not display sensitive information when others can see them (shoulder surfing)
- Privacy screens required for laptop users working in public areas (e.g., trains, cafes)

---

## 9. Equipment Security

### 9.1 Equipment Siting and Protection (Annex A 7.8)
- IT equipment sited to minimise risks from environmental hazards and unauthorised access
- Server racks locked; access restricted to IT team
- No equipment placed adjacent to windows or in publicly visible areas

### 9.2 Supporting Utilities (Annex A 7.9)
- UPS (Uninterruptible Power Supply) installed for all critical IT equipment
- Diesel generator on standby at data centre (tested monthly)
- Dual power feeds from independent substations at primary data centre
- Water, fire suppression, and air conditioning systems regularly maintained

### 9.3 Equipment Maintenance (Annex A 7.10)
- All IT equipment maintained in accordance with supplier recommendations
- Maintenance records kept in the Asset Maintenance Register
- Only authorised personnel or approved vendors may carry out equipment maintenance
- Maintenance carried out on-site where possible; data wiped before off-site repair

### 9.4 Equipment Off-Premises (Annex A 7.11 & 7.12)
- Removal of IT equipment from NFS premises requires prior authorisation
- All portable devices (laptops, tablets, phones) must have full disk encryption enabled
- Loss or theft of portable devices reported to IT Service Desk within 1 hour
- Remote wipe capability enabled on all NFS mobile devices

### 9.5 Secure Disposal and Re-Use (Annex A 7.14)
- All storage media containing NFS data must be securely wiped before reuse or disposal
- Hard drives: NIST 800-88 compliant overwriting or physical destruction
- Certificate of destruction obtained for data centre hardware disposal
- Destruction/disposal records retained in the Asset Disposal Register for 3 years

---

## 10. Branch Network (14 Locations)

Branch-specific requirements:
- Each branch has a designated Physical Security Coordinator (typically Branch Manager)
- CCTV and intruder alarms mandatory at all branches
- ATM and cash handling areas subject to additional physical security assessment
- Branch server/networking equipment in locked, access-controlled comms room
- Annual physical security review of all branches by Facilities/CISO

---

## 11. Non-Compliance

Physical security violations (e.g., tailgating, propping open secure doors, leaving sensitive material unattended) are treated as IS incidents. Repeat violations result in disciplinary action.

---

*Nexus Financial Services Ltd | NFS-IS-POL-010 v1.0*
*ISO/IEC 27001:2022 Annex A Theme 7 — Physical Controls (7.1–7.14)*
