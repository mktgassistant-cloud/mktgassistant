# The $100K Work-From-Home Skill Audit — Lead Magnet Funnel

**Traffic:** Cold YouTube viewers coming from side-hustle, work-from-home and data-entry content. Low awareness, not looking for a data career yet.
**YouTube hook:** "Which Remote/WFH Skill Could Pay You $100K?"
**Job of this funnel:** Get the email. Show each person which remote skill they have the best shot at. Make data analytics the clear top path for the people who fit it.

**Copy rules**
- Frame data work as "analyzing business numbers to help companies make decisions." Don't lead with SQL, BI tools or the "data analyst" job title.
- Mass-market, simple, fast, outcome-focused.
- Under 8 questions. One CTA per result page.
- Same core email sequence for everyone. Only the opening angle changes by tier.

**Live page:** `funnels/skill-audit/ghl-custom-html.html`, pasted into a Custom HTML/Javascript element on https://datacareerblueprint.com/mass-market-opt-in-page. That file holds the final copy; this doc mirrors it.

**Contents**
1. [Opt-in page copy and structure](#1-opt-in-page-copy-and-structure)
2. [Audit questions and scoring](#2-audit-questions-and-scoring)
3. [Result pages](#3-result-pages)
4. [First follow-up email per tier](#4-first-follow-up-email-per-tier)
5. [Sequence roadmap](#5-sequence-roadmap)
6. [GoHighLevel setup](#6-gohighlevel-setup)

Placeholders are in `[BRACKETS]`.

---

## 1. Opt-in page copy and structure

Quiz first, email gate last. Everything is on one page; the screens swap in place.

```
[Logo]
LANDING     Eyebrow · Headline · Subheadline · Button · small trust line
   ↓ click
QUESTIONS   7 screens, one question each, progress bar, Back link
   ↓ after Q7
EMAIL GATE  Headline · line of copy · GoHighLevel form (first name, email) · trust line
   ↓ submit → form redirects to ?step=results
RESULT      Tier headline · subhead · body · one CTA button
[Earnings disclaimer under every screen]
```

### Landing

- **Eyebrow:** FREE 60-SECOND AUDIT
- **Headline:** The $100K Work-From-Home Skill Audit
- **Subheadline:** Find out which remote skill you already have the best shot at - and which one could actually replace your income.
- **Button:** Start My 60-Second Audit →
- **Under the button:** Free. 7 quick questions. No tech background needed.

### Email gate (after question 7)

- **Eyebrow:** ✓ AUDIT COMPLETE
- **Headline:** Where should we send your result?
- **Copy:** Enter your first name and email to see your result now. We'll send you a copy too.
- **Fields:** First name, email
- **Button:** Show Me My Highest-Paying Remote Skill
- **Trust line:** No spam. Unsubscribe anytime.

### Disclaimer (small print, every screen)

> Results vary. Income figures reflect what some people in these roles earn and are not a promise or guarantee of earnings. Your results depend on your effort, experience and the job market.

---

## 2. Audit questions and scoring

Each question is a skill the visitor rates themselves on. Above every question: **"Be honest: how good are you at this right now?"**

The 7 skills are the core of data analytics work, written as things people already do in everyday life. Cold traffic from data-entry and side-hustle videos can honestly rate themselves above zero, and nothing reads as SQL, BI tools or coding. The "named back as" label is how the Medium and High result pages describe the skills each person rated highest.

| Answer | Points |
|---|---|
| Never done it | 0 |
| Tried it once or twice | 1 |
| Can do it confidently | 2 |
| Could teach someone else | 3 |

| # | Skill (as shown) | Named back as | Hidden field |
|---|---|---|---|
| 1 | Cleaning up a messy list or spreadsheet so it actually makes sense (like a budget, contact list or inventory) | cleaning up messy numbers | `q1_spreadsheets` |
| 2 | Digging through a pile of emails, receipts or orders to find the one answer you need | digging answers out of a pile of records | `q2_records` |
| 3 | Turning numbers into a simple chart or summary someone can understand at a glance | turning numbers into something people can understand | `q3_charts` |
| 4 | Spotting a pattern in numbers, like which months you spend the most or which products sell best | spotting patterns in numbers | `q4_trends` |
| 5 | Explaining something complicated to someone in plain English | explaining things in plain English | `q5_explaining` |
| 6 | Figuring out what the real problem is before jumping to a fix | finding the real problem before jumping to a fix | `q6_problems` |
| 7 | Using AI tools like ChatGPT to get work done faster | using AI tools to work faster | `q7_ai_tools` |

**Total possible: 21.**

| Points | Tier | Result headline | CTA |
|---|---|---|---|
| 0–7 | **Low** | Your fastest remote skill: Admin / Data Entry | Get the Free Remote Jobs Guide |
| 8–14 | **Medium** | Your highest-leverage skill: Data Analytics | Watch the Free Training |
| 15–21 | **High** | You're built for Data Analytics | Book Your Clarity Call |

**Score shown:** Data Analytics Fit Score = `round(points ÷ 21 × 100)`, shown on Medium and High only. The Low page leads with the skill instead of a low number.

---

## 3. Result pages

Each page: eyebrow, headline, subhead, the visitor's name ("Jamie, here's your result."), body, one CTA.

`{{top skills}}` = up to 3 skills the person rated 2 or 3, highest first, joined like "spotting patterns in numbers, explaining things in plain English and using AI tools to work faster." Medium and High always have at least one.

### Low (0–7)

**Eyebrow:** YOUR FASTEST REMOTE SKILL
**Headline:** Admin / Data Entry
**Subhead:** This is the easiest remote skill to land quickly - no tech background needed. But if you want to get to $100K, the next step up is data analytics.

Most people start here because it pays faster than waiting tables, gig work, or retail. The roles are real, the hours are flexible, and you can get in without a degree.

The trade-off is the ceiling. Most admin and data entry work tops out around $40K to $55K.

If your goal is to replace your income and eventually scale into six figures, the move is to add one high-value skill on top of this. Data analytics is the cleanest upgrade because companies already pay $80K to $120K for people who can turn raw numbers into decisions.

**Your next step:** Download the free guide below. It breaks down the top 10 remote/WFH jobs you can start with now, plus the fastest path from each one into a higher-income skill.

> **[ Get the Free Remote Jobs Guide → ]** → `https://drive.google.com/file/d/1GElm5hkxd_9Zwro2ihG4PSfp-1XkFla5/view`

### Medium (8–14)

**Score dial** · **Eyebrow:** YOUR HIGHEST-LEVERAGE SKILL
**Headline:** Data Analytics
**Subhead:** You already have the mindset and some of the pieces. Here's how to turn that into a real remote career.

Based on your answers, you're not starting from zero. You're already good at {{top skills}}. Those are real pieces of data analytics work. That's the exact profile of someone who can break into data analytics without a CS degree.

The difference between people who make $80K+ in this field and people who stay stuck isn't intelligence. It's knowing which skills actually matter, which ones to ignore, and how to position yourself so companies trust you before you've even been hired.

**Your next step:** Watch the free training. It walks you through the exact roadmap from where you are now to a $100K+ data + AI career, including the mistakes that slow most people down.

> **[ ▶ Watch the Free Training → ]** → `[VSL LINK]`

### High (15–21)

**Score dial** · **Eyebrow:** YOUR RESULT
**Headline:** You're built for Data Analytics
**Subhead:** You have the highest probability of landing a $100K+ remote career in this field. Let's map it out.

Your answers show the combination that matters most. You're already confident at {{top skills}}. That's the heart of what data analysts do every day: take messy numbers, figure out what they mean, and explain it so a business can act.

That's not common. Most people who take this audit can't say that.

The fastest way to turn this into an actual offer is to get a personalized roadmap. Not a generic course. A straight-line plan based on your background, your timeline, and the exact skills that get people hired right now.

**Your next step:** Book a free Career Clarity Call. We'll look at where you are, where you want to be, and whether our program is the right fit. If it's not, you'll still walk away with a clear game plan.

> **[ Book Your Clarity Call → ]** → `[CALENDAR LINK]`

---

## 4. First follow-up email per tier

Sent the moment the form is submitted, by the GoHighLevel workflow. Same structure for every tier: deliver the result, one reason it matters, the same single CTA as the result page. Only the opening angle changes.

### 4A. Low — Email 1 (immediate)

**Subject:** {{contact.first_name}}, your fastest remote skill
**Preview:** It's not the one most people guess.

Hi {{contact.first_name}},

Your $100K Work-From-Home Skill Audit is in.

**Your fastest remote skill: Admin / Data Entry.**

That's good news. It's the easiest remote work to land quickly, with no degree and no tech background. It usually pays better than gig work or retail, and the hours are flexible.

Here's the part most people miss: admin and data entry tends to top out around $40K to $55K. The people who get to six figures add one more skill on top. For most of them, that's analyzing business numbers to help companies make decisions.

Start with the free guide. It breaks down the top 10 remote jobs you can start now, plus the fastest path from each one into higher-paying work.

**[Get the Free Remote Jobs Guide →](https://drive.google.com/file/d/1GElm5hkxd_9Zwro2ihG4PSfp-1XkFla5/view)**

Talk soon,
[SENDER NAME]

### 4B. Medium — Email 1 (immediate)

**Subject:** {{contact.first_name}}, your highest-leverage skill
**Preview:** You're not starting from zero.

Hi {{contact.first_name}},

Your $100K Work-From-Home Skill Audit is in.

**Your highest-leverage skill: Data Analytics.**

In plain English, that means analyzing a company's numbers and telling them what's working and what to do next. It's laptop work, a lot of it is remote, and experienced people in it can earn $80K and up.

Your answers show you're not starting from zero. You already have some of the pieces. What separates the people who get hired from the ones who stay stuck isn't intelligence. It's knowing which skills matter, which to ignore, and how to get companies to trust you before you've been hired.

That's exactly what the free training covers:

**[Watch the Free Training →]([VSL LINK])**

Watch it before you apply to another $15/hour job.

Talk soon,
[SENDER NAME]

### 4C. High — Email 1 (immediate)

**Subject:** {{contact.first_name}}, you scored in the top group
**Preview:** Let's map out your path.

Hi {{contact.first_name}},

Your $100K Work-From-Home Skill Audit is in.

**Your result: You're built for Data Analytics.**

That puts you in the top group of people who take this audit. You already have the skills that matter most for analyzing business numbers and helping companies make decisions, and that's the work companies pay $100K+ for when you're experienced.

The fastest way to turn that into an actual offer is a personalized plan, not a generic course. One based on your background, your timeline, and the skills that get people hired right now.

Book a free Career Clarity Call and we'll map it out together:

**[Book Your Clarity Call →]([CALENDAR LINK])**

If it's not a fit, you'll still walk away with a clear game plan.

Talk soon,
[SENDER NAME]

P.S. Calendar spots fill up each week. If you're even a little curious, grab a time now. You can always reschedule.

---

## 5. Sequence roadmap

For High and Medium people who don't book. Same core emails for everyone; only the first line changes by tier ("You scored in the top group…" vs. "You already have some of the pieces…").

| Day | Email | Objection it answers | CTA |
|---|---|---|---|
| 0 | Email 1 (above) | Result delivery | Tier CTA |
| 1 | Why data? | "Why this skill and not admin or VA work?" | Training |
| 3 | Why now? | "Can't I just do this later?" | Training / Call |
| 5 | Why me? | "People like me don't get these jobs." (student story) | Call |
| 7–8 | What if I'm not technical? | "I'm not a computer person." | Call |
| 9–10 | (Optional) Last call | Gentle close | Call |

**Exit rules:** stop the sequence when someone books a call. Non-bookers move to long-term nurture after the last email.
**Low tier:** Email 1 → guide, then long-term nurture with remote-job tips. Every few weeks, send a "ready for the next level?" email that invites them to retake the audit.

---

## 6. GoHighLevel setup

**Form "Mass Market Lead Mag Opt In"** (`jHLG6cDRBPe9IeZiC6m4`)
- Fields: First name + Email. Remove Phone, or make it optional.
- Button text: "Show Me My Highest-Paying Remote Skill".
- Hidden fields (query keys): `audit_tier` (high / medium / low), `audit_score` (0–100), and optionally `q1_spreadsheets` … `q7_ai_tools` (0–3 each). The page passes these into the form.
- **On Submit → Redirect URL:** `https://datacareerblueprint.com/mass-market-opt-in-page?step=results`, then **Save**. The page shows the result after the redirect. GoHighLevel also passes the hidden-field values along with the redirect, so the result still shows if the browser didn't save it.

**Page:** the "mass market opt in" funnel step. Section full width, 0 padding. One Custom HTML/Javascript element with the contents of `ghl-custom-html.html`. Fill in the `CONFIG` block (calendar, VSL and its length, guide link).

**Workflow:** trigger "Form Submitted" (this form) → If/Else on Audit Tier → add tag `audit-wfh-high` / `-medium` / `-low` → send that tier's Email 1 → wait → core sequence. A calendar booking adds `booked-clarity-call` and removes them from the sequence.

**What to track first:** landing → started audit, started → finished Q7, finished → opted in, the tier split, then per tier: call bookings (High), training views (Medium), guide clicks (Low). If more than about 40% land in High, raise the High cutoff.

**Compliance:** keep the earnings disclaimer on every screen. Never say "you will earn $100K." Say "can," "could," or "some people earn."
