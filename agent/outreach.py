"""Turn matched postings into one outreach draft per company."""

from collections import defaultdict


def _roles_sentence(titles: list[str]) -> str:
    unique = list(dict.fromkeys(titles))
    if len(unique) == 1:
        return unique[0]
    if len(unique) == 2:
        return f"{unique[0]} and {unique[1]}"
    return f"{unique[0]} and {len(unique) - 1} other analyst roles"


def _tidy(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines()) + "\n"


def build_drafts(jobs: list[dict], config: dict) -> list[dict]:
    """Group jobs by company and render one email draft per company."""
    sender = config["sender"]
    template = config["outreach"]
    by_company = defaultdict(list)
    for j in jobs:
        by_company[(j["source"], j["company_slug"])].append(j)

    drafts = []
    for (source, slug), company_jobs in sorted(by_company.items()):
        company = company_jobs[0]["company"]
        titles = [j["title"] for j in company_jobs]
        job_lines = "\n".join(
            f"  - {j['title']} ({j['location']}) — {j['url']}" for j in company_jobs
        )
        n = len(company_jobs)
        openings_phrase = (
            f"your {titles[0]} opening" if n == 1 else f"your {n} open analyst roles"
        )
        fields = {
            "company": company,
            "roles_sentence": _roles_sentence(titles),
            "openings_phrase": openings_phrase,
            "n_roles": len(company_jobs),
            "job_lines": job_lines,
            "sender_name": sender["name"],
            "sender_company": sender["company"],
            "website": sender["website"],
            "calendar_link": sender.get("calendar_link") or "",
        }
        drafts.append({
            "company": company,
            "source": source,
            "company_slug": slug,
            "n_roles": len(company_jobs),
            "roles": "; ".join(titles),
            "job_urls": "; ".join(j["url"] for j in company_jobs),
            "subject": template["subject"].format(**fields),
            "body": _tidy(template["body"].format(**fields)),
        })
    return drafts
