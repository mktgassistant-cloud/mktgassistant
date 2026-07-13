"""Title and location filtering for scraped postings."""


def matches(job: dict, filters: dict) -> bool:
    title = job.get("title", "").lower()
    if not any(pat.lower() in title for pat in filters.get("include_titles", [])):
        return False
    if any(pat.lower() in title for pat in filters.get("exclude_titles", [])):
        return False
    locations = filters.get("locations") or []
    if locations:
        loc = job.get("location", "").lower()
        if not any(pat.lower() in loc for pat in locations):
            return False
    return True


def filter_jobs(jobs: list[dict], filters: dict) -> list[dict]:
    return [j for j in jobs if matches(j, filters)]
