"""Fetch job postings from public ATS job-board APIs (Greenhouse, Lever, Ashby).

Every fetcher returns a list of normalized job dicts:
    {id, source, company_slug, company, title, location, url}
Boards that 404 (company changed ATS, slug typo) are skipped with a warning.
"""

import requests

TIMEOUT = 15
HEADERS = {"User-Agent": "analyst-outreach-agent/1.0"}


def _company_name(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").title()


def fetch_greenhouse(slug: str) -> list[dict]:
    url = f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"
    resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()
    jobs = []
    for j in resp.json().get("jobs", []):
        jobs.append({
            "id": f"greenhouse:{slug}:{j['id']}",
            "source": "greenhouse",
            "company_slug": slug,
            "company": _company_name(slug),
            "title": j.get("title", "").strip(),
            "location": (j.get("location") or {}).get("name", ""),
            "url": j.get("absolute_url", f"https://boards.greenhouse.io/{slug}"),
        })
    return jobs


def fetch_lever(slug: str) -> list[dict]:
    url = f"https://api.lever.co/v0/postings/{slug}?mode=json"
    resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()
    jobs = []
    for j in resp.json():
        jobs.append({
            "id": f"lever:{slug}:{j['id']}",
            "source": "lever",
            "company_slug": slug,
            "company": _company_name(slug),
            "title": j.get("text", "").strip(),
            "location": (j.get("categories") or {}).get("location", ""),
            "url": j.get("hostedUrl", f"https://jobs.lever.co/{slug}"),
        })
    return jobs


def fetch_ashby(slug: str) -> list[dict]:
    url = f"https://api.ashbyhq.com/posting-api/job-board/{slug}"
    resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    resp.raise_for_status()
    jobs = []
    for j in resp.json().get("jobs", []):
        jobs.append({
            "id": f"ashby:{slug}:{j['id']}",
            "source": "ashby",
            "company_slug": slug,
            "company": _company_name(slug),
            "title": j.get("title", "").strip(),
            "location": j.get("location", ""),
            "url": j.get("jobUrl") or j.get("applyUrl")
                   or f"https://jobs.ashbyhq.com/{slug}/{j['id']}",
        })
    return jobs


FETCHERS = {
    "greenhouse": fetch_greenhouse,
    "lever": fetch_lever,
    "ashby": fetch_ashby,
}


def fetch_all(companies: dict) -> list[dict]:
    """companies: {"greenhouse": [slug, ...], "lever": [...], "ashby": [...]}"""
    all_jobs = []
    for source, slugs in companies.items():
        fetcher = FETCHERS.get(source)
        if fetcher is None:
            print(f"  [warn] unknown ATS '{source}', skipping")
            continue
        for slug in slugs or []:
            try:
                jobs = fetcher(slug)
                all_jobs.extend(jobs)
                print(f"  {source}/{slug}: {len(jobs)} postings")
            except requests.HTTPError as e:
                print(f"  [warn] {source}/{slug}: HTTP {e.response.status_code}, skipping")
            except requests.RequestException as e:
                print(f"  [warn] {source}/{slug}: {e}, skipping")
    return all_jobs
