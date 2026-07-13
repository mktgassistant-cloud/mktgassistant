# Analyst Outreach Agent

Every weekday morning this agent scans company job boards for open **data
analyst** roles, dedupes against everything it has already seen, and produces
ready-to-send outreach emails pitching Data in Motion graduates to each
company that's hiring.

## How it works

1. **Scrape** — pulls postings from the public job-board APIs of three ATS
   platforms (Greenhouse, Lever, Ashby) for every company listed in
   `config.yaml`. No fragile HTML scraping, no TOS problems: these are
   official, structured endpoints.
2. **Filter** — keeps roles whose titles match the analyst keywords in
   `config.yaml` (and drops senior/staff/director-level roles).
3. **Dedupe** — `data/seen_jobs.json` tracks every posting already surfaced,
   so each role appears exactly once.
4. **Draft** — groups new roles by company and renders one outreach email per
   company from the template in `config.yaml`.

## Outputs

| File | Purpose |
|---|---|
| `outreach/YYYY-MM-DD.md` | Human-readable digest: new roles + email drafts |
| `outreach/YYYY-MM-DD.csv` | Import into your sending tool (Instantly, Smartlead, Apollo, ...) |

The GitHub Actions workflow (`.github/workflows/daily-scan.yml`) runs
weekdays at 12:00 UTC and commits the results back to the repo. You can also
trigger it manually from the Actions tab, or run locally:

```bash
pip install -r requirements.txt
python -m agent.run
```

## Setup (do this once)

1. Edit `config.yaml` → `sender:` — put in your real name and, ideally, a
   calendar link.
2. Optionally tune `filters:` (e.g. add `locations: ["remote", "united states"]`
   to skip international postings).
3. Optionally edit the email template under `outreach:`.

## Growing the company list

The seed list has ~45 verified companies. To check where any other company's
board lives:

```bash
python -m agent.discover acme othercompany
```

Slugs that stop working (company switches ATS) are skipped with a warning —
they never break the run.

## Sending the emails

The agent deliberately produces **drafts, not sends**. Import the daily CSV
into a proper cold-email tool (Instantly, Smartlead, or Apollo sequences) so
you get warmed sending domains, reply tracking, and unsubscribe handling.
Sending B2B cold email from your main domain without warmup will hurt your
deliverability — don't do it.

## Sensible next steps

- **Contact enrichment**: auto-find the recruiter/hiring-manager email per
  company (Hunter.io or Apollo API) and add it to the CSV.
- **Member digest**: the same scan output doubles as a daily "fresh analyst
  roles" feed for your community — a retention feature for near-zero extra work.
- **Reply handling**: pipe replies into a simple CRM sheet so interested
  companies get candidate profiles within 24h.
