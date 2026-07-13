"""Daily run: scrape ATS boards, filter for analyst roles, emit outreach drafts.

Usage: python -m agent.run

Outputs (per run, only when new roles are found):
  outreach/YYYY-MM-DD.md   human-readable digest + email drafts
  outreach/YYYY-MM-DD.csv  import into your cold-email tool (Instantly, Smartlead, Apollo, ...)
  data/seen_jobs.json      dedupe state so each posting is only surfaced once
"""

import csv
import json
from datetime import date
from pathlib import Path

import yaml

from .ats import fetch_all
from .filters import filter_jobs
from .outreach import build_drafts

ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = ROOT / "data" / "seen_jobs.json"
OUT_DIR = ROOT / "outreach"


def load_state() -> set[str]:
    if STATE_FILE.exists():
        return set(json.loads(STATE_FILE.read_text()))
    return set()


def save_state(seen: set[str]) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(sorted(seen), indent=0) + "\n")


def write_outputs(drafts: list[dict], jobs: list[dict], run_date: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    csv_path = OUT_DIR / f"{run_date}.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "company", "source", "company_slug", "n_roles",
            "roles", "job_urls", "subject", "body",
        ])
        writer.writeheader()
        writer.writerows(drafts)

    md_path = OUT_DIR / f"{run_date}.md"
    lines = [
        f"# Analyst role scan — {run_date}",
        "",
        f"**{len(jobs)} new matching postings across {len(drafts)} companies.**",
        "",
        "## New postings",
        "",
    ]
    for j in jobs:
        lines.append(f"- **{j['company']}** — [{j['title']}]({j['url']}) ({j['location']})")
    lines += ["", "---", "", "## Outreach drafts (one per company)", ""]
    for d in drafts:
        lines += [
            f"### {d['company']} ({d['n_roles']} role{'s' if d['n_roles'] > 1 else ''})",
            "",
            f"**Subject:** {d['subject']}",
            "",
            "```",
            d["body"].rstrip(),
            "```",
            "",
        ]
    md_path.write_text("\n".join(lines) + "\n")
    print(f"\nWrote {md_path.relative_to(ROOT)} and {csv_path.relative_to(ROOT)}")


def main() -> None:
    config = yaml.safe_load((ROOT / "config.yaml").read_text())
    run_date = date.today().isoformat()

    print("Scanning job boards...")
    all_jobs = fetch_all(config["companies"])
    matched = filter_jobs(all_jobs, config["filters"])
    print(f"\n{len(all_jobs)} postings scanned, {len(matched)} match analyst filters")

    seen = load_state()
    new_jobs = [j for j in matched if j["id"] not in seen]
    print(f"{len(new_jobs)} are new since the last run")

    if not new_jobs:
        print("Nothing new today — no output written.")
        return

    drafts = build_drafts(new_jobs, config)
    write_outputs(drafts, new_jobs, run_date)

    seen.update(j["id"] for j in matched)
    save_state(seen)
    print(f"State updated: {len(seen)} postings tracked")


if __name__ == "__main__":
    main()
