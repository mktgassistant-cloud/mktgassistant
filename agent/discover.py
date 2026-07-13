"""Check which ATS a company's job board lives on.

Usage: python -m agent.discover <slug> [slug ...]

Tries each slug against Greenhouse, Lever, and Ashby and reports hits,
so you can grow the companies list in config.yaml.
"""

import sys

import requests

from .ats import HEADERS, TIMEOUT

PROBES = {
    "greenhouse": "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs",
    "lever": "https://api.lever.co/v0/postings/{slug}?mode=json",
    "ashby": "https://api.ashbyhq.com/posting-api/job-board/{slug}",
}


def main() -> None:
    slugs = sys.argv[1:]
    if not slugs:
        print(__doc__)
        sys.exit(1)
    for slug in slugs:
        hits = []
        for source, url in PROBES.items():
            try:
                resp = requests.get(url.format(slug=slug), headers=HEADERS, timeout=TIMEOUT)
                if resp.ok:
                    hits.append(source)
            except requests.RequestException:
                pass
        if hits:
            print(f"{slug}: found on {', '.join(hits)} — add under companies.{hits[0]}")
        else:
            print(f"{slug}: not found on any supported ATS")


if __name__ == "__main__":
    main()
