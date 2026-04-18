#!/usr/bin/env python3
"""
isms_soa_tracker.py
-------------------
ISO/IEC 27001:2022 Statement of Applicability (SoA) Tracker
Tracks implementation status of all 93 Annex A controls.

Usage:
    python isms_soa_tracker.py                         # Show full report
    python isms_soa_tracker.py --theme 5               # Show Theme 5 controls only
    python isms_soa_tracker.py --update 5.1 Implemented  # Update a control status
    python isms_soa_tracker.py --export-csv soa.csv    # Export to CSV
    python isms_soa_tracker.py --summary               # Show summary only

License: MIT
"""

import json
import csv
import argparse
import sys
from datetime import date
from pathlib import Path

# All 93 ISO/IEC 27001:2022 Annex A Controls
# Format: (control_id, title, theme, new_in_2022)
CONTROLS = [
    # Theme 5 - Organisational Controls (37)
    ("5.1", "Policies for information security", 5, False),
    ("5.2", "Information security roles and responsibilities", 5, False),
    ("5.3", "Segregation of duties", 5, False),
    ("5.4", "Management responsibilities", 5, False),
    ("5.5", "Contact with authorities", 5, False),
    ("5.6", "Contact with special interest groups", 5, False),
    ("5.7", "Threat intelligence", 5, True),
    ("5.8", "Information security in project management", 5, False),
    ("5.9", "Inventory of information and other associated assets", 5, False),
    ("5.10", "Acceptable use of information and other associated assets", 5, False),
    ("5.11", "Return of assets", 5, False),
    ("5.12", "Classification of information", 5, False),
    ("5.13", "Labelling of information", 5, False),
    ("5.14", "Information transfer", 5, False),
    ("5.15", "Access control", 5, False),
    ("5.16", "Identity management", 5, False),
    ("5.17", "Authentication information", 5, False),
    ("5.18", "Access rights", 5, False),
    ("5.19", "Information security in supplier relationships", 5, False),
    ("5.20", "Addressing information security within supplier agreements", 5, False),
    ("5.21", "Managing information security in the ICT supply chain", 5, False),
    ("5.22", "Monitoring, review and change management of supplier services", 5, False),
    ("5.23", "Information security for use of cloud services", 5, True),
    ("5.24", "Information security incident management planning and preparation", 5, False),
    ("5.25", "Assessment and decision on information security events", 5, False),
    ("5.26", "Response to information security incidents", 5, False),
    ("5.27", "Learning from information security incidents", 5, False),
    ("5.28", "Collection of evidence", 5, False),
    ("5.29", "Information security during disruption", 5, False),
    ("5.30", "ICT readiness for business continuity", 5, True),
    ("5.31", "Legal, statutory, regulatory and contractual requirements", 5, False),
    ("5.32", "Intellectual property rights", 5, False),
    ("5.33", "Protection of records", 5, False),
    ("5.34", "Privacy and protection of PII", 5, False),
    ("5.35", "Independent review of information security", 5, False),
    ("5.36", "Compliance with policies, rules and standards for information security", 5, False),
    ("5.37", "Documented operating procedures", 5, False),
    # Theme 6 - People Controls (8)
    ("6.1", "Screening", 6, False),
    ("6.2", "Terms and conditions of employment", 6, False),
    ("6.3", "Information security awareness, education and training", 6, False),
    ("6.4", "Disciplinary process", 6, False),
    ("6.5", "Responsibilities after termination or change of employment", 6, False),
    ("6.6", "Confidentiality or non-disclosure agreements", 6, False),
    ("6.7", "Remote working", 6, False),
    ("6.8", "Information security event reporting", 6, False),
    # Theme 7 - Physical Controls (14)
    ("7.1", "Physical security perimeters", 7, False),
    ("7.2", "Physical entry", 7, False),
    ("7.3", "Securing offices, rooms and facilities", 7, False),
    ("7.4", "Physical security monitoring", 7, True),
    ("7.5", "Protecting against physical and environmental threats", 7, False),
    ("7.6", "Working in secure areas", 7, False),
    ("7.7", "Clear desk and clear screen", 7, False),
    ("7.8", "Equipment siting and protection", 7, False),
    ("7.9", "Security of assets off-premises", 7, False),
    ("7.10", "Storage media", 7, False),
    ("7.11", "Supporting utilities", 7, False),
    ("7.12", "Cabling security", 7, False),
    ("7.13", "Equipment maintenance", 7, False),
    ("7.14", "Secure disposal or re-use of equipment", 7, False),
    # Theme 8 - Technological Controls (34)
    ("8.1", "User endpoint devices", 8, False),
    ("8.2", "Privileged access rights", 8, False),
    ("8.3", "Information access restriction", 8, False),
    ("8.4", "Access to source code", 8, False),
    ("8.5", "Secure authentication", 8, False),
    ("8.6", "Capacity management", 8, False),
    ("8.7", "Protection against malware", 8, False),
    ("8.8", "Management of technical vulnerabilities", 8, False),
    ("8.9", "Configuration management", 8, True),
    ("8.10", "Information deletion", 8, True),
    ("8.11", "Data masking", 8, True),
    ("8.12", "Data leakage prevention", 8, True),
    ("8.13", "Information backup", 8, False),
    ("8.14", "Redundancy of information processing facilities", 8, False),
    ("8.15", "Logging", 8, False),
    ("8.16", "Monitoring activities", 8, True),
    ("8.17", "Clock synchronisation", 8, False),
    ("8.18", "Use of privileged utility programs", 8, False),
    ("8.19", "Installation of software on operational systems", 8, False),
    ("8.20", "Networks security", 8, False),
    ("8.21", "Security of network services", 8, False),
    ("8.22", "Segregation of networks", 8, False),
    ("8.23", "Web filtering", 8, True),
    ("8.24", "Use of cryptography", 8, False),
    ("8.25", "Secure development life cycle", 8, False),
    ("8.26", "Application security requirements", 8, False),
    ("8.27", "Secure system architecture and engineering principles", 8, False),
    ("8.28", "Secure coding", 8, True),
    ("8.29", "Security testing in development and acceptance", 8, False),
    ("8.30", "Outsourced development", 8, False),
    ("8.31", "Separation of development, test and production environments", 8, False),
    ("8.32", "Change management", 8, False),
    ("8.33", "Test information", 8, False),
    ("8.34", "Protection of information systems during audit testing", 8, False),
]

VALID_STATUSES = ["Implemented", "Partial", "Planned", "Not Started", "Excluded"]
THEME_NAMES = {5: "Organisational", 6: "People", 7: "Physical", 8: "Technological"}
DEFAULT_STATE_FILE = "isms_soa_state.json"


def load_state(state_file):
    """Load saved SoA state from JSON file."""
    path = Path(state_file)
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {}


def save_state(state, state_file):
    """Save SoA state to JSON file."""
    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)


def get_control_status(state, control_id):
    """Get status for a control, defaulting to Not Started."""
    return state.get(control_id, {}).get("status", "Not Started")


def calculate_stats(state, theme=None):
    """Calculate implementation statistics."""
    controls = [c for c in CONTROLS if theme is None or c[2] == theme]
    stats = {s: 0 for s in VALID_STATUSES}
    for ctrl_id, _, _, _ in controls:
        status = get_control_status(state, ctrl_id)
        stats[status] = stats.get(status, 0) + 1
    total = len(controls)
    implemented = stats["Implemented"]
    included = total - stats.get("Excluded", 0)
    pct = (implemented / included * 100) if included > 0 else 0
    return stats, total, included, implemented, pct


def progress_bar(pct, width=40):
    """Generate a text progress bar."""
    filled = int(width * pct / 100)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {pct:.1f}%"


def print_report(state, theme=None):
    """Print the full SoA implementation report."""
    print("=" * 70)
    print("  ISO/IEC 27001:2022 — Statement of Applicability Tracker")
    print(f"  Report Date: {date.today()}")
    print("=" * 70)

    if theme:
        themes = [theme]
    else:
        themes = [5, 6, 7, 8]

    for t in themes:
        theme_controls = [c for c in CONTROLS if c[2] == t]
        print(f"\n  Theme {t} — {THEME_NAMES[t]} Controls ({len(theme_controls)} controls)")
        print("  " + "-" * 60)
        print(f"  {'ID':<8} {'Status':<16} {'New?':<6} {'Title'}")
        print("  " + "-" * 60)
        for ctrl_id, title, _, is_new in theme_controls:
            status = get_control_status(state, ctrl_id)
            new_flag = " NEW" if is_new else ""
            status_symbol = {"Implemented": "✓", "Partial": "~", "Planned": "→",
                             "Not Started": " ", "Excluded": "✗"}.get(status, " ")
            print(f"  {ctrl_id:<8} [{status_symbol}] {status:<14} {new_flag:<6} {title[:55]}")

    print("\n" + "=" * 70)
    print("  IMPLEMENTATION SUMMARY")
    print("=" * 70)

    total_all = len(CONTROLS)
    for t in [5, 6, 7, 8]:
        stats, total, included, implemented, pct = calculate_stats(state, t)
        print(f"\n  Theme {t} — {THEME_NAMES[t]}")
        print(f"  {progress_bar(pct)}")
        print(f"  Implemented: {implemented}/{included} included controls")

    stats_all, total_all, included_all, impl_all, pct_all = calculate_stats(state)
    print(f"\n  {'OVERALL':}")
    print(f"  {progress_bar(pct_all)}")
    print(f"  Total: {impl_all}/{included_all} controls fully implemented")
    print(f"  Partial: {stats_all.get('Partial', 0)} | Planned: {stats_all.get('Planned', 0)} | Not Started: {stats_all.get('Not Started', 0)} | Excluded: {stats_all.get('Excluded', 0)}")

    # Audit readiness
    if pct_all >= 95:
        readiness = "AUDIT READY — >= 95% implemented"
    elif pct_all >= 80:
        readiness = "NEAR READY — complete remaining controls before Stage 2 audit"
    elif pct_all >= 60:
        readiness = "IN PROGRESS — significant implementation work remaining"
    else:
        readiness = "EARLY STAGE — substantial implementation work required"

    print(f"\n  Audit Readiness: {readiness}")
    print("=" * 70)

    # New controls status
    new_controls = [c for c in CONTROLS if c[3]]
    new_implemented = sum(1 for c in new_controls if get_control_status(state, c[0]) == "Implemented")
    print(f"\n  2022 New Controls ({len(new_controls)} total): {new_implemented}/{len(new_controls)} implemented")
    for ctrl_id, title, _, _ in new_controls:
        status = get_control_status(state, ctrl_id)
        symbol = "✓" if status == "Implemented" else ("~" if status == "Partial" else " ")
        print(f"    [{symbol}] {ctrl_id:<6} {status:<16} {title[:50]}")
    print()


def export_csv(state, filename):
    """Export SoA state to CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Control ID", "Title", "Theme", "New in 2022",
                         "Status", "Justification", "Evidence", "Last Updated"])
        for ctrl_id, title, theme, is_new in CONTROLS:
            ctrl_data = state.get(ctrl_id, {})
            writer.writerow([
                ctrl_id, title, f"Theme {theme} — {THEME_NAMES[theme]}",
                "Yes" if is_new else "No",
                ctrl_data.get("status", "Not Started"),
                ctrl_data.get("justification", ""),
                ctrl_data.get("evidence", ""),
                ctrl_data.get("last_updated", "")
            ])
    print(f"SoA exported to {filename}")


def update_control(state, ctrl_id, new_status):
    """Update status for a specific control."""
    ctrl_ids = [c[0] for c in CONTROLS]
    if ctrl_id not in ctrl_ids:
        print(f"Error: Control {ctrl_id} not found. Valid controls: {', '.join(ctrl_ids[:5])}...")
        return state
    if new_status not in VALID_STATUSES:
        print(f"Error: Invalid status. Choose from: {', '.join(VALID_STATUSES)}")
        return state
    if ctrl_id not in state:
        state[ctrl_id] = {}
    state[ctrl_id]["status"] = new_status
    state[ctrl_id]["last_updated"] = str(date.today())
    ctrl_title = next(c[1] for c in CONTROLS if c[0] == ctrl_id)
    print(f"Updated {ctrl_id} ({ctrl_title}): {new_status}")
    return state


def main():
    parser = argparse.ArgumentParser(
        description="ISO/IEC 27001:2022 SoA Implementation Tracker — 93 Annex A controls"
    )
    parser.add_argument("--state", default=DEFAULT_STATE_FILE, help="Path to state JSON file")
    parser.add_argument("--theme", type=int, choices=[5, 6, 7, 8], help="Filter by theme (5/6/7/8)")
    parser.add_argument("--update", nargs=2, metavar=("CONTROL_ID", "STATUS"),
                        help=f"Update control status. Status options: {', '.join(VALID_STATUSES)}")
    parser.add_argument("--export-csv", metavar="FILENAME", help="Export SoA to CSV")
    parser.add_argument("--summary", action="store_true", help="Show summary only (no control list)")
    parser.add_argument("--version", action="version", version="isms_soa_tracker 1.0.0")

    args = parser.parse_args()
    state = load_state(args.state)

    if args.update:
        state = update_control(state, args.update[0], args.update[1])
        save_state(state, args.state)

    if args.export_csv:
        export_csv(state, args.export_csv)
        return

    if args.summary:
        stats, total, included, implemented, pct = calculate_stats(state)
        print(f"ISO 27001:2022 SoA Progress: {implemented}/{included} controls implemented ({pct:.1f}%)")
        print(progress_bar(pct))
    else:
        print_report(state, args.theme)


if __name__ == "__main__":
    main()
