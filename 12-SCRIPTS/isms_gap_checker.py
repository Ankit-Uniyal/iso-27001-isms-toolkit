#!/usr/bin/env python3
"""
ISMS Gap Assessment Checker - ISO/IEC 27001:2022
=================================================
Nexus Financial Services Ltd (NFS) ISMS Toolkit
Document Reference: NFS-IS-SCRIPT-002
Version: 1.0

PURPOSE:
    Automated gap assessment checker for ISO/IEC 27001:2022.
    Reads gap assessment scores from a CSV file and generates:
    - Overall maturity score and band
    - Theme-by-theme breakdown with RAG status
    - Prioritised remediation list (P1-P4)
    - Certification readiness assessment
    - Executive summary report

USAGE:
    python3 isms_gap_checker.py --demo
    python3 isms_gap_checker.py --input gap_scores.csv
    python3 isms_gap_checker.py --input gap_scores.csv --output report.txt

CSV FORMAT (gap_scores.csv):
    control_id,applicable,score,notes
    5.1,yes,3,Policy approved by Board May 2026
    5.7,yes,1,Informal only - NCSC subscription active
    ...

SCORE DEFINITIONS:
    0 = Not in place
    1 = Initial / Ad hoc (informal activity only)
    2 = Developing (partial implementation)
    3 = Defined (fully implemented and consistent)
    4 = Managed / Optimised (measured and improving)
"""

import argparse
import csv
import sys
import os
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Optional, Tuple


# All 93 ISO/IEC 27001:2022 Annex A controls
CONTROLS = [
    # Theme 5 - Organisational (37 controls)
    ("5.1","Policies for information security",5),
    ("5.2","Information security roles and responsibilities",5),
    ("5.3","Segregation of duties",5),
    ("5.4","Management responsibilities",5),
    ("5.5","Contact with authorities",5),
    ("5.6","Contact with special interest groups",5),
    ("5.7","Threat intelligence",5),
    ("5.8","Information security in project management",5),
    ("5.9","Inventory of information and other associated assets",5),
    ("5.10","Acceptable use of information and other associated assets",5),
    ("5.11","Return of assets",5),
    ("5.12","Classification of information",5),
    ("5.13","Labelling of information",5),
    ("5.14","Information transfer",5),
    ("5.15","Access control",5),
    ("5.16","Identity management",5),
    ("5.17","Authentication information",5),
    ("5.18","Access rights",5),
    ("5.19","Information security in supplier relationships",5),
    ("5.20","Addressing information security within supplier agreements",5),
    ("5.21","Managing information security in the ICT supply chain",5),
    ("5.22","Monitoring, review and change management of supplier services",5),
    ("5.23","Information security for use of cloud services",5),
    ("5.24","IS incident management planning and preparation",5),
    ("5.25","Assessment and decision on information security events",5),
    ("5.26","Response to information security incidents",5),
    ("5.27","Learning from information security incidents",5),
    ("5.28","Collection of evidence",5),
    ("5.29","Information security during disruption",5),
    ("5.30","ICT readiness for business continuity",5),
    ("5.31","Legal, statutory, regulatory and contractual requirements",5),
    ("5.32","Intellectual property rights",5),
    ("5.33","Protection of records",5),
    ("5.34","Privacy and protection of PII",5),
    ("5.35","Independent review of information security",5),
    ("5.36","Compliance with policies, rules and standards for IS",5),
    ("5.37","Documented operating procedures",5),
    # Theme 6 - People (8 controls)
    ("6.1","Screening",6),
    ("6.2","Terms and conditions of employment",6),
    ("6.3","IS awareness, education and training",6),
    ("6.4","Disciplinary process",6),
    ("6.5","Responsibilities after termination or change of employment",6),
    ("6.6","Confidentiality or non-disclosure agreements",6),
    ("6.7","Remote working",6),
    ("6.8","Information security event reporting",6),
    # Theme 7 - Physical (14 controls)
    ("7.1","Physical security perimeters",7),
    ("7.2","Physical entry",7),
    ("7.3","Securing offices, rooms and facilities",7),
    ("7.4","Physical security monitoring",7),
    ("7.5","Protecting against physical and environmental threats",7),
    ("7.6","Working in secure areas",7),
    ("7.7","Clear desk and clear screen",7),
    ("7.8","Equipment siting and protection",7),
    ("7.9","Security of assets off-premises",7),
    ("7.10","Storage media",7),
    ("7.11","Supporting utilities",7),
    ("7.12","Cabling security",7),
    ("7.13","Equipment maintenance",7),
    ("7.14","Secure disposal or re-use of equipment",7),
    # Theme 8 - Technological (34 controls)
    ("8.1","User endpoint devices",8),
    ("8.2","Privileged access rights",8),
    ("8.3","Information access restriction",8),
    ("8.4","Access to source code",8),
    ("8.5","Secure authentication",8),
    ("8.6","Capacity management",8),
    ("8.7","Protection against malware",8),
    ("8.8","Management of technical vulnerabilities",8),
    ("8.9","Configuration management",8),
    ("8.10","Information deletion",8),
    ("8.11","Data masking",8),
    ("8.12","Data leakage prevention",8),
    ("8.13","Information backup",8),
    ("8.14","Redundancy of information processing facilities",8),
    ("8.15","Logging",8),
    ("8.16","Monitoring activities",8),
    ("8.17","Clock synchronisation",8),
    ("8.18","Use of privileged utility programs",8),
    ("8.19","Installation of software on operational systems",8),
    ("8.20","Networks security",8),
    ("8.21","Security of network services",8),
    ("8.22","Segregation of networks",8),
    ("8.23","Web filtering",8),
    ("8.24","Use of cryptography",8),
    ("8.25","Secure development life cycle",8),
    ("8.26","Application security requirements",8),
    ("8.27","Secure system architecture and engineering principles",8),
    ("8.28","Secure coding",8),
    ("8.29","Security testing in development and acceptance",8),
    ("8.30","Outsourced development",8),
    ("8.31","Separation of development, test and production environments",8),
    ("8.32","Change management",8),
    ("8.33","Test information",8),
    ("8.34","Protection of information systems during audit testing",8),
]

THEME_NAMES = {5:"Organisational",6:"People",7:"Physical",8:"Technological"}

MATURITY_LABELS = {
    0:"Not in Place",1:"Initial/Ad hoc",2:"Developing",3:"Defined",4:"Managed/Optimised"
}

# Demo scores simulating a mid-size org at ~50% maturity
DEMO_SCORES = {
    "5.1":(True,3),"5.2":(True,3),"5.3":(True,2),"5.4":(True,3),
    "5.5":(True,2),"5.6":(True,1),"5.7":(True,0),"5.8":(True,2),
    "5.9":(True,2),"5.10":(True,3),"5.11":(True,2),"5.12":(True,2),
    "5.13":(True,1),"5.14":(True,2),"5.15":(True,3),"5.16":(True,3),
    "5.17":(True,2),"5.18":(True,3),"5.19":(True,2),"5.20":(True,2),
    "5.21":(True,1),"5.22":(True,2),"5.23":(True,2),"5.24":(True,2),
    "5.25":(True,2),"5.26":(True,2),"5.27":(True,1),"5.28":(True,1),
    "5.29":(True,2),"5.30":(True,2),"5.31":(True,3),"5.32":(True,2),
    "5.33":(True,3),"5.34":(True,3),"5.35":(True,1),"5.36":(True,2),
    "5.37":(True,2),"6.1":(True,3),"6.2":(True,3),"6.3":(True,2),
    "6.4":(True,3),"6.5":(True,2),"6.6":(True,3),"6.7":(True,2),
    "6.8":(True,2),"7.1":(True,3),"7.2":(True,3),"7.3":(True,3),
    "7.4":(True,2),"7.5":(True,2),"7.6":(True,2),"7.7":(True,2),
    "7.8":(True,3),"7.9":(True,2),"7.10":(True,1),"7.11":(True,3),
    "7.12":(True,2),"7.13":(True,3),"7.14":(True,2),"8.1":(True,3),
    "8.2":(True,2),"8.3":(True,3),"8.4":(True,1),"8.5":(True,2),
    "8.6":(True,2),"8.7":(True,3),"8.8":(True,2),"8.9":(True,0),
    "8.10":(True,1),"8.11":(True,0),"8.12":(True,1),"8.13":(True,3),
    "8.14":(True,3),"8.15":(True,2),"8.16":(True,2),"8.17":(True,3),
    "8.18":(True,2),"8.19":(True,2),"8.20":(True,3),"8.21":(True,2),
    "8.22":(True,3),"8.23":(True,1),"8.24":(True,2),"8.25":(True,2),
    "8.26":(True,1),"8.27":(True,2),"8.28":(True,0),"8.29":(True,2),
    "8.30":(True,2),"8.31":(True,3),"8.32":(True,3),"8.33":(True,2),
    "8.34":(True,2),
}


def rag(pct):
    if pct >= 75: return "GREEN"
    elif pct >= 50: return "AMBER"
    return "RED"


def maturity_band(pct):
    if pct <= 20: return "L0 - Non-existent"
    elif pct <= 40: return "L1 - Initial"
    elif pct <= 60: return "L2 - Developing"
    elif pct <= 80: return "L3 - Defined"
    elif pct <= 90: return "L4 - Managed"
    return "L5 - Optimised"


def priority(score):
    return {0:"P1-Critical (30 days)",1:"P2-High (60 days)",
            2:"P3-Medium (90 days)",3:"P4-Low (180 days)"}.get(score,"P4-Low")


def load_csv(path):
    scores = {}
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            cid = row.get('control_id','').strip()
            app = row.get('applicable','yes').strip().lower() in ('yes','y','true','1')
            try: s = int(row.get('score',0))
            except: s = 0
            notes = row.get('notes','').strip()
            scores[cid] = (app, s, notes)
    return scores


def analyse(scores):
    theme_totals = defaultdict(lambda:{'app':0,'score':0,'gaps':[]})
    gaps, total_app, total_score = [], 0, 0
    for cid, title, theme in CONTROLS:
        if cid in scores: app, s, notes = scores[cid]
        elif cid in DEMO_SCORES: app, s, notes = DEMO_SCORES[cid][0], DEMO_SCORES[cid][1], ""
        else: app, s, notes = True, 0, ""
        if not app: continue
        theme_totals[theme]['app'] += 1
        theme_totals[theme]['score'] += s
        total_app += 1; total_score += s
        if s < 3:
            g = {'id':cid,'title':title,'theme':theme,'score':s,'notes':notes}
            theme_totals[theme]['gaps'].append(g)
            gaps.append(g)

    overall = round(total_score/(total_app*4)*100,1) if total_app else 0
    themes = {}
    for t, d in theme_totals.items():
        pct = round(d['score']/(d['app']*4)*100,1) if d['app'] else 0
        themes[t] = {'name':THEME_NAMES[t],'app':d['app'],'pct':pct,
                     'rag':rag(pct),'band':maturity_band(pct),
                     'gaps':sorted(d['gaps'],key=lambda x:x['score'])}
    return {'overall':overall,'rag':rag(overall),'band':maturity_band(overall),
            'total_app':total_app,'themes':themes,
            'gaps':sorted(gaps,key=lambda x:(x['score'],x['theme'])),
            'critical':[g for g in gaps if g['score']==0],
            'high':[g for g in gaps if g['score']==1]}


def report(r, outfile=None):
    L = []
    L += ["="*68,"  ISO/IEC 27001:2022 GAP ASSESSMENT REPORT",
          f"  {datetime.now().strftime('%Y-%m-%d %H:%M')}","="*68,"",
          "EXECUTIVE SUMMARY","-"*40,
          f"  Overall Score:    {r['overall']}%",
          f"  Maturity Band:    {r['band']}",
          f"  RAG Status:       {r['rag']}",
          f"  Controls in scope: {r['total_app']} / 93",
          f"  At Level 3+:      {r['total_app']-len(r['gaps'])}",
          f"  Below Level 3:    {len(r['gaps'])}",
          f"  P1 Critical:      {len(r['critical'])}",
          f"  P2 High:          {len(r['high'])}","",
          "THEME RESULTS","-"*40]
    for tn in [5,6,7,8]:
        if tn not in r['themes']: continue
        t = r['themes'][tn]
        bar = chr(9608)*int(t['pct']/5)+chr(9617)*(20-int(t['pct']/5))
        L.append(f"  Theme {tn} {t['name']:<22} [{bar}] {t['pct']:5.1f}%  {t['rag']}")
        L.append(f"         {t['band']} | Gaps: {len(t['gaps'])}")
    L += ["","REMEDIATION — P1 CRITICAL (Score 0)","-"*40]
    if r['critical']:
        for g in r['critical']:
            L.append(f"  [{g['id']:5s}] {g['title'][:55]}")
    else: L.append("  None — excellent!")
    L += ["","REMEDIATION — P2 HIGH (Score 1)","-"*40]
    if r['high']:
        for g in r['high']:
            L.append(f"  [{g['id']:5s}] {g['title'][:55]}")
    else: L.append("  None")
    L += ["","CERTIFICATION READINESS","-"*40]
    pct = r['overall']
    if pct>=85: L.append("  READY - Consider scheduling Stage 1 audit.")
    elif pct>=70: L.append("  NEARLY READY - Close P1/P2 gaps first. Est: 3-6 months.")
    elif pct>=50: L.append("  DEVELOPING - Structured programme needed. Est: 6-12 months.")
    else: L.append("  SIGNIFICANT GAPS - Major work required. Est: 12-18+ months.")
    L += ["","="*68,
          "  iso-27001-isms-toolkit | ISO/IEC 27001:2022",
          "  Indicative only - not a substitute for formal audit.","="*68]
    out = "\n".join(L)
    print(out)
    if outfile:
        with open(outfile,'w',encoding='utf-8') as f: f.write(out)
        print(f"\n  Saved to: {outfile}")


def main():
    p = argparse.ArgumentParser(description='ISO 27001:2022 Gap Checker')
    p.add_argument('--input','-i',help='CSV file with gap scores')
    p.add_argument('--output','-o',help='Output file for report')
    p.add_argument('--demo',action='store_true',help='Run with built-in demo data')
    args = p.parse_args()
    if args.demo:
        print("\n  Running with DEMO data (~50% maturity organisation)\n")
        scores = {k:(v[0],v[1],"") for k,v in DEMO_SCORES.items()}
    elif args.input:
        if not os.path.exists(args.input):
            print(f"Error: {args.input} not found",file=sys.stderr); sys.exit(1)
        scores = load_csv(args.input)
    else:
        p.print_help()
        print("\nTip: run with --demo to see a sample report.")
        sys.exit(0)
    report(analyse(scores), args.output)

if __name__ == '__main__':
    main()
