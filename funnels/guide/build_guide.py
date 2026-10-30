"""Build the Top 10 Remote Jobs (2026) guide as HTML, then print it to PDF.

Copy source: funnels/top-10-remote-jobs-guide.md
Usage:  python3 funnels/guide/build_guide.py
Output: funnels/guide/top-10-remote-jobs-2026.html and .pdf
"""
import base64
import html
import pathlib
import subprocess

HERE = pathlib.Path(__file__).parent
VSL_URL = "https://datacareerblueprint.com"
AUDIT_URL = "https://datacareerblueprint.com/mass-market-opt-in-page"

JOBS = [
    {
        "title": "Customer Support Specialist",
        "do": "Help customers by chat, email or phone. Fix order problems, answer questions, and step in when the chatbot can't handle it.",
        "pay": "$15–$22 an hour. Senior and “escalation” roles pay more.",
        "ai": 3,
        "ai_note": "AI handles the easy stuff now, like password resets and order tracking. Companies still need real people for upset customers and messy problems. That's where the jobs are moving.",
        "steps": [
            "Search “remote customer support” or “chat support” on Indeed and LinkedIn. Filter by “Remote” and “Entry level.”",
            "On your resume, put any job where you dealt with people: retail, food service, call centers, even volunteering.",
            "Practice one story: “a time I calmed down an upset customer.” You'll almost always be asked.",
        ],
        "upgrade": "Support team lead → support operations → <b>customer data analyst</b> (the person who figures out <i>why</i> customers keep complaining).",
    },
    {
        "title": "Data Entry Specialist",
        "do": "Type and update information in spreadsheets and company systems: orders, invoices, customer records, inventory.",
        "pay": "$13–$18 an hour.",
        "ai": 2,
        "ai_note": "Simple typing is being automated. The jobs that last are the ones where you check and clean the data, not just type it in. Be the person who catches mistakes.",
        "steps": [
            "Get comfortable in Google Sheets or Excel: sorting, filtering, and simple formulas like SUM. Free YouTube tutorials are enough.",
            "Take a free typing test and put your speed and accuracy on your resume.",
            "Apply to “data entry,” “data clerk” and “records specialist” roles. Avoid any listing that asks you to pay for training or equipment.",
        ],
        "upgrade": "This is the most direct path on the list. Every hour in a spreadsheet is practice for <b>data analytics</b> (Job #10).",
    },
    {
        "title": "Virtual Assistant",
        "do": "Keep a busy person or small business organized: email, calendar, booking, simple paperwork, research.",
        "pay": "$15–$30 an hour. Beginners start lower, and specialists charge more.",
        "ai": 3,
        "ai_note": "AI tools make VAs faster, not obsolete. Business owners still want one trusted person who “just handles it.”",
        "steps": [
            "Pick two or three things you're already good at (scheduling, inbox cleanup, social media posting) and offer just those.",
            "Make a free profile on Upwork or OnlineJobs.ph, and tell your network you're taking clients.",
            "Offer your first client a small paid trial week. Ask for a testimonial when it goes well.",
        ],
        "upgrade": "Executive assistant → operations coordinator → <b>operations or business analyst</b>.",
    },
    {
        "title": "Appointment Setter",
        "do": "Message or call people who showed interest in a product or program, ask a few questions, and book the good fits onto a sales call. You don't do the selling yourself.",
        "pay": "Often a base plus commission. Roughly $3,000–$6,000 a month for people who hit their targets. Pay depends heavily on the company.",
        "ai": 4,
        "ai_note": "This job runs on trust and timing. People can tell when they're talking to a bot.",
        "steps": [
            "Search “appointment setter remote” and “SDR remote” (SDR stands for sales development rep).",
            "Look for companies that train you and pay a base, not commission only.",
            "In the interview, show you can ask good questions and listen. That's 80% of the job.",
        ],
        "upgrade": "Sales rep → sales operations → <b>sales analyst</b> (the person who tracks which leads turn into customers).",
    },
    {
        "title": "Content Moderator",
        "do": "Review posts, videos, ads or comments, and flag anything that breaks a platform's rules or could embarrass an advertiser.",
        "pay": "$16–$25 an hour.",
        "ai": 4,
        "ai_note": "AI flags the obvious stuff. Humans make the judgment calls on tone, context and intent, and platforms keep learning that the hard way.",
        "steps": [
            "Search “content moderator,” “trust and safety associate” and “content reviewer.”",
            "Many roles are through outsourcing companies that hire in big groups. Apply to several.",
            "Be honest with yourself: some content can be upsetting. Ask about wellness support in the interview.",
        ],
        "upgrade": "Senior moderator → policy specialist → <b>trust &amp; safety analyst</b>.",
    },
    {
        "title": "Short-Form Content Clipper",
        "do": "Watch long videos and podcasts, find the moments most likely to go viral, and cut them, or tell an editor what to cut, into TikToks, Reels and Shorts.",
        "pay": "Freelance. Beginners often charge per clip or per month, and experienced strategists can earn well. It varies a lot.",
        "ai": 3,
        "ai_note": "Auto-clipping tools exist, but picking the moment that actually hooks people is still a human skill.",
        "steps": [
            "Pick one creator you like. Make five sample clips from their long videos for free, as practice.",
            "Post them on a simple portfolio page or a TikTok account.",
            "Pitch small podcasters and coaches: “I made these from your episode. Want more?”",
        ],
        "upgrade": "Content strategist → <b>content analytics</b> (reading the numbers to see which videos work and why).",
    },
    {
        "title": "Lead &amp; CRM Coordinator",
        "do": "Make sure every sales lead gets tracked and followed up on. You keep the company's customer list (the CRM) clean and up to date, so no customer falls through the cracks.",
        "pay": "$40,000–$55,000 a year to start. Some roles add commission.",
        "ai": 3,
        "ai_note": "Software sends the reminders. A person still has to keep the data clean and spot when something's off.",
        "steps": [
            "Learn the basics of one free CRM, like HubSpot's free version. Their free online courses are enough to start.",
            "Search “CRM coordinator,” “lead coordinator” and “sales coordinator remote.”",
            "Highlight anything organized on your resume: scheduling, inventory, tracking orders.",
        ],
        "upgrade": "Sales or marketing operations → <b>marketing analyst</b>.",
    },
    {
        "title": "Small Business Tech Helper",
        "do": "Help small businesses that are behind on tech. Fix their website, set up online invoicing and booking, and walk the owner through new tools.",
        "pay": "$18–$30 an hour, or a flat fee per project.",
        "ai": 4,
        "ai_note": "AI tools are everywhere now, and most small business owners don't know how to set them up. That gap is the job.",
        "steps": [
            "Get good at one common tool, like WordPress, Google Workspace or a booking app.",
            "Offer to fix one thing for a local business you already know, for cheap or free, in exchange for a referral.",
            "Search “WordPress support,” “IT support remote” and “help desk” for steady part-time or full-time work.",
        ],
        "upgrade": "IT support → automation specialist → <b>business systems analyst</b>.",
    },
    {
        "title": "Process &amp; Documentation Writer",
        "do": "Turn “how we do things around here” into clear step-by-step guides (SOPs, help articles, how-to docs) so companies stop relying on one person's memory.",
        "pay": "$20–$35 an hour freelance to start. Experienced writers can earn much more.",
        "ai": 3,
        "ai_note": "AI can draft. It can't interview the person who actually knows the process, or notice the step everyone forgets.",
        "steps": [
            "Write two sample guides about anything you know well, like “how to onboard a new hire” or “how to process a return.”",
            "Search “SOP writer,” “documentation specialist” and “technical writer entry level.”",
            "Pitch small businesses on Upwork: “I'll turn your messy process into a clear one-page guide.”",
        ],
        "upgrade": "Technical writer → operations → <b>process or business analyst</b>.",
    },
]

TOTAL_PAGES = 14


def stars(n):
    return "★" * n + '<span class="off">' + "★" * (5 - n) + "</span>"


def footer(page):
    return f'<div class="foot"><span>Top 10 Remote Jobs · 2026 Edition</span><span>{page} / {TOTAL_PAGES}</span></div>'


def job_page(num, job, page):
    steps = "".join(f"<li>{s}</li>" for s in job["steps"])
    return f"""
<section class="page job">
  <div class="jobhead"><span class="num">#{num}</span><div><div class="kicker">JOB #{num} OF 10</div><h2>{job["title"]}</h2></div></div>
  <div class="label">What you'd do</div>
  <p class="lead">{job["do"]}</p>
  <div class="facts">
    <div class="fact"><div class="label">Typical pay (2026)</div><p>{job["pay"]}</p></div>
    <div class="fact"><div class="label">AI-proof score</div><p class="stars">{stars(job["ai"])}</p></div>
  </div>
  <div class="label">Why it's still hiring</div>
  <p>{job["ai_note"]}</p>
  <div class="label">How to land your first one</div>
  <ol class="steps">{steps}</ol>
  <div class="upgrade"><div class="label coral">Your upgrade path</div><p>{job["upgrade"]}</p></div>
  {footer(page)}
</section>"""


def build():
    logo = "data:image/png;base64," + base64.b64encode((HERE / "logo.png").read_bytes()).decode()
    jobs = "".join(job_page(i + 1, j, i + 4) for i, j in enumerate(JOBS))
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Top 10 Remote Jobs You Can Start With No Experience (2026 Edition)</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  @page {{ size: Letter; margin: 0; }}
  :root {{ --navy: #0d1336; --ink: #14172b; --muted: #5a6180; --line: #e2e6f3; --blue: #0038ff; --violet: #667eea; --coral: #ff6240; --green: #1f9d4a; --tint: #f4f6ff; }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; font: 13.5px/1.6 Inter, Arial, sans-serif; color: var(--ink); -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  .page {{ width: 8.5in; height: 11in; padding: 0.8in 0.85in 0.9in; position: relative; page-break-after: always; overflow: hidden; }}
  .page:last-child {{ page-break-after: auto; }}
  h1 {{ font-weight: 900; letter-spacing: -.03em; line-height: 1.05; margin: 0; }}
  h2 {{ font-size: 28px; font-weight: 900; letter-spacing: -.02em; line-height: 1.15; margin: 0; }}
  h3 {{ font-size: 18px; font-weight: 800; margin: 26px 0 8px; }}
  p {{ margin: 0 0 10px; }}
  .kicker {{ font-size: 11px; font-weight: 800; letter-spacing: .14em; color: var(--coral); margin-bottom: 6px; }}
  .label {{ font-size: 11px; font-weight: 800; letter-spacing: .1em; text-transform: uppercase; color: var(--blue); margin: 20px 0 6px; }}
  .label.coral {{ color: var(--coral); margin-top: 0; }}
  .lead {{ font-size: 16px; }}
  .foot {{ position: absolute; left: 0.85in; right: 0.85in; bottom: 0.45in; display: flex; justify-content: space-between; font-size: 10px; color: var(--muted); border-top: 1px solid var(--line); padding-top: 8px; }}
  .bar {{ position: absolute; top: 0; left: 0; right: 0; height: 8px; background: linear-gradient(90deg, var(--blue), var(--violet), var(--coral)); }}

  /* Cover */
  .cover {{ background: radial-gradient(900px 500px at 50% -100px, rgba(0,56,255,.35), transparent 70%), #07080d; color: #fff; display: flex; flex-direction: column; justify-content: center; text-align: center; padding: 1in; }}
  .cover img {{ width: 110px; height: 110px; border-radius: 50%; margin: 0 auto 40px; box-shadow: 0 0 40px rgba(24,139,246,.45); }}
  .cover .edition {{ display: inline-block; margin: 0 auto 26px; padding: 6px 14px; border: 1px solid rgba(255,255,255,.25); border-radius: 999px; font-size: 12px; font-weight: 800; letter-spacing: .14em; color: var(--coral); }}
  .cover h1 {{ font-size: 52px; }}
  .cover h1 span {{ color: #8ea2ff; }}
  .cover .sub {{ font-size: 17px; color: #b9c0dc; max-width: 5.6in; margin: 26px auto 0; }}
  .cover .brand {{ position: absolute; bottom: 0.7in; left: 0; right: 0; font-size: 12px; color: #8a91ad; letter-spacing: .04em; }}

  /* Intro */
  .checks {{ list-style: none; padding: 0; margin: 10px 0 16px; }}
  .checks li {{ padding-left: 26px; position: relative; margin-bottom: 7px; }}
  .checks li::before {{ content: "✓"; position: absolute; left: 0; color: var(--coral); font-weight: 900; }}
  .callout {{ background: var(--tint); border-left: 4px solid var(--blue); border-radius: 8px; padding: 14px 18px; margin: 18px 0; }}
  .callout.coral {{ border-left-color: var(--coral); background: #fff4f1; }}
  .big {{ font-size: 19px; font-weight: 800; line-height: 1.35; margin: 18px 0; }}

  /* Job pages */
  .jobhead {{ display: flex; align-items: center; gap: 18px; padding-bottom: 18px; border-bottom: 2px solid var(--line); margin-bottom: 6px; }}
  .num {{ flex: 0 0 auto; width: 64px; height: 64px; border-radius: 14px; background: var(--navy); color: #fff; display: grid; place-items: center; font-size: 24px; font-weight: 900; }}
  .facts {{ display: grid; grid-template-columns: 1.4fr 1fr; gap: 14px; margin: 8px 0 4px; }}
  .fact {{ background: var(--tint); border-radius: 10px; padding: 2px 16px 6px; }}
  .fact .label {{ margin-top: 12px; }}
  .stars {{ font-size: 20px; color: var(--coral); letter-spacing: 2px; }}
  .stars .off {{ color: #d5d9e8; }}
  .steps {{ padding-left: 0; margin: 4px 0 0; list-style: none; counter-reset: s; }}
  .steps li {{ counter-increment: s; position: relative; padding-left: 38px; margin-bottom: 10px; }}
  .steps li::before {{ content: counter(s); position: absolute; left: 0; top: 0; width: 24px; height: 24px; border-radius: 50%; background: var(--blue); color: #fff; font-size: 12px; font-weight: 800; display: grid; place-items: center; }}
  .upgrade {{ margin-top: 22px; border: 2px solid var(--coral); border-radius: 12px; padding: 14px 18px 6px; }}

  .job {{ font-size: 15.5px; line-height: 1.65; }}
  .job h2 {{ font-size: 34px; }}
  .job .num {{ width: 76px; height: 76px; font-size: 28px; }}
  .job .lead {{ font-size: 18.5px; }}
  .job .label {{ font-size: 12px; margin-top: 28px; }}
  .job .fact .label {{ margin-top: 14px; }}
  .job .stars {{ font-size: 26px; }}
  .job .steps li {{ margin-bottom: 14px; padding-left: 42px; }}
  .job .steps li::before {{ width: 28px; height: 28px; font-size: 13px; }}
  .job .upgrade {{ margin-top: 30px; padding: 18px 22px 10px; }}

  /* Job 10 */
  .upgradepage {{ background: linear-gradient(180deg, #0d1336, #07080d); color: #fff; }}
  .upgradepage .foot {{ color: #8a91ad; border-top-color: rgba(255,255,255,.12); }}
  .upgradepage .label {{ color: #8ea2ff; }}
  .upgradepage .num {{ background: var(--coral); }}
  .upgradepage .jobhead {{ border-bottom-color: rgba(255,255,255,.12); }}
  .badge {{ display: inline-block; background: var(--coral); color: #fff; font-size: 11px; font-weight: 900; letter-spacing: .14em; padding: 5px 12px; border-radius: 999px; margin-bottom: 8px; }}
  .upgradepage .fact {{ background: rgba(255,255,255,.06); }}
  .upgradepage .stars .off {{ color: rgba(255,255,255,.2); }}
  .upgradepage .callout {{ background: rgba(102,126,234,.14); border-left-color: var(--coral); }}
  .upgradepage .steps li::before {{ background: var(--coral); }}
  .btn {{ display: block; text-align: center; text-decoration: none; background: var(--blue); color: #fff; font-weight: 800; font-size: 16px; padding: 14px; border-radius: 10px; margin-top: 16px; }}
  .btn.ghost {{ background: transparent; color: var(--blue); border: 2px solid var(--blue); }}

  /* Scams */
  .flags {{ list-style: none; padding: 0; margin: 10px 0; }}
  .flags li {{ border: 1px solid var(--line); border-radius: 10px; padding: 12px 16px 12px 48px; margin-bottom: 9px; position: relative; }}
  .flags li::before {{ content: "!"; position: absolute; left: 14px; top: 12px; width: 22px; height: 22px; border-radius: 50%; background: var(--coral); color: #fff; font-weight: 900; font-size: 13px; display: grid; place-items: center; }}
  .plan {{ display: grid; gap: 12px; margin: 14px 0; }}
  .plan div {{ background: var(--tint); border-radius: 10px; padding: 14px 18px; }}
  .plan b {{ color: var(--blue); }}
  .fine {{ font-size: 10.5px; color: var(--muted); margin-top: 26px; }}
</style></head><body>

<section class="page cover">
  <img src="{logo}" alt="Data in Motion">
  <div class="edition">2026 EDITION</div>
  <h1>TOP 10 REMOTE JOBS<br><span>You Can Start With<br>No Experience</span></h1>
  <p class="sub">What each one pays, where to find it, how to get hired, and the fastest path from each one into a higher-income skill.</p>
  <div class="brand">From the $100K Work-From-Home Skill Audit · Data Career Blueprint</div>
</section>

<section class="page">
  <div class="bar"></div>
  <div class="kicker">READ THIS FIRST</div>
  <h2>The easiest remote jobs to get are usually the boring ones.</h2>
  <p style="margin-top:16px">They don't go viral. Nobody brags about them. That's exactly why they're always hiring: most people don't even know they exist.</p>
  <p>This guide covers 10 of them. For each one, you'll get:</p>
  <ul class="checks">
    <li><b>What you'd actually do</b> all day, in plain English</li>
    <li><b>What it typically pays</b> in 2026</li>
    <li><b>Why it's still hiring</b> in a world full of AI</li>
    <li><b>How to land your first one</b>, step by step</li>
    <li><b>Your upgrade path</b>, where it can lead once you're in</li>
  </ul>
  <div class="callout coral"><b>One more thing.</b> Jobs 1–9 are about getting your <b>first</b> remote paycheck, fast. Job 10 is different. It's the one that can take you from “paying the bills” to “replacing your income.” Read that one last.</div>
  {footer(2)}
</section>

<section class="page">
  <div class="bar"></div>
  <div class="kicker">BEFORE YOU PICK</div>
  <h2>The 2026 test: can AI do this job?</h2>
  <p class="big">Before you pick a remote job in 2026, ask one question: <span style="color:var(--blue)">Will a robot be doing this in two years?</span></p>
  <p>Every job in this guide was picked because it needs something AI is still bad at:</p>
  <div class="plan">
    <div><b>Judgment:</b> knowing when something feels off</div>
    <div><b>People:</b> calming someone down, building trust</div>
    <div><b>Context:</b> understanding what a business actually needs</div>
  </div>
  <p>Each job gets an <b>AI-Proof Score</b> from 1 to 5. Higher is safer.</p>
  <p class="stars" style="font-size:26px">★★★★★</p>
  {footer(3)}
</section>

{jobs}

<section class="page upgradepage">
  <div class="bar"></div>
  <div class="jobhead"><span class="num">#10</span><div><span class="badge">THE UPGRADE</span><h2>Data Analytics</h2></div></div>
  <p class="lead" style="margin-top:14px"><b>Jobs 1–9 get you a remote paycheck. This one can replace your income.</b></p>
  <div class="label">What you'd do</div>
  <p>Look at a company's numbers (sales, customers, costs, orders) and tell them what's working, what isn't, and what to do next. You don't need to be a math genius. You need to be curious and good at explaining things.</p>
  <div class="facts">
    <div class="fact"><div class="label">Typical pay (2026)</div><p>Entry-level roles often start around $55,000–$75,000. Experienced people commonly earn $80,000–$120,000+, and many of these jobs are remote.</p></div>
    <div class="fact"><div class="label">AI-proof score</div><p class="stars">{stars(5)}</p><p style="font-size:12px">AI makes analysts faster. It doesn't replace the person who asks the right question and explains the answer.</p></div>
  </div>
  <div class="callout"><b>Did you notice?</b> Every upgrade path in this guide ends in analysis: customer data, sales numbers, marketing results, business systems. Data skills are the “next level” for almost every remote job.</div>
  <div class="label">Why it's #10, not #1</div>
  <p>It takes longer to learn than the other nine, usually a few months of focused practice. That's why most people never try. It's also why it pays so much more.</p>
  <div class="label">How to get started</div>
  <ol class="steps">
    <li>Get good at spreadsheets: sorting, filtering, formulas and simple charts.</li>
    <li>Practice with real-world numbers, like your own budget or a free public dataset.</li>
    <li>Learn the right skills in the right order, with proof you can do the work. This is where most people get stuck.</li>
  </ol>
  <a class="btn" href="{VSL_URL}">▶ Want the roadmap? Watch the Free Training →</a>
  {footer(13)}
</section>

<section class="page">
  <div class="bar"></div>
  <div class="kicker">PROTECT YOURSELF</div>
  <h2>How to spot a work-from-home scam</h2>
  <p style="margin-top:14px">Remote job scams are everywhere in 2026. Walk away if you see any of these:</p>
  <ul class="flags">
    <li><b>They ask you to pay</b> for training, equipment or a “starter kit”</li>
    <li><b>They send you a check</b> and ask you to send some of the money back</li>
    <li><b>The whole interview happens by text</b> or on Telegram or WhatsApp, with no video call</li>
    <li><b>The pay sounds too good</b> for too little work (“$50/hr, no experience, 2 hours a day!”)</li>
    <li><b>The email comes from Gmail or Yahoo</b> instead of a company address</li>
    <li><b>They pressure you</b> to accept today</li>
  </ul>
  <div class="callout coral" style="font-size:16px"><b>Rule of thumb:</b> a real job pays <i>you</i>. You never pay <i>them</i>.</div>

  <div class="kicker" style="margin-top:26px">YOUR NEXT STEP</div>
  <div class="plan">
    <div><b>Step 1:</b> Pick one job from 1–9 that fits your life right now. Apply to 10 openings this week.</div>
    <div><b>Step 2:</b> While you work it, build your spreadsheet skills on the side.</div>
    <div><b>Step 3:</b> When you're ready for the bigger jump, come back to Job #10, and retake the audit to watch your score go up.</div>
  </div>
  <a class="btn ghost" href="{AUDIT_URL}">Retake the $100K Work-From-Home Skill Audit →</a>
  <p class="fine">Pay ranges are typical estimates for U.S. remote roles in 2026 and vary by company, location and experience. They are not a promise or guarantee of earnings. Always research a company before applying. © Data Career Blueprint · Data in Motion</p>
  {footer(14)}
</section>

</body></html>"""
    out = HERE / "top-10-remote-jobs-2026.html"
    out.write_text(doc, encoding="utf-8")
    return out


if __name__ == "__main__":
    html_path = build()
    pdf_path = html_path.with_suffix(".pdf")
    script = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://{html_path.resolve()}', {{ waitUntil: 'networkidle' }});
  await p.pdf({{ path: '{pdf_path.resolve()}', format: 'Letter', printBackground: true, preferCSSPageSize: true }});
  await b.close();
}})();
"""
    subprocess.run(["node", "-e", script], check=True)
    print("wrote", pdf_path)
