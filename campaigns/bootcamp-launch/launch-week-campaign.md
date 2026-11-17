# AI Analytics Engineer Bootcamp: Launch Week Campaign

**Goal:** 30 enrolled students for Cohort 1 (starts late January 2027)
**Launch week:** Monday Nov 23 to Monday Nov 30, 2026
**Primary CTA everywhere:** Book a sales call
**Landing page:** https://claude.ai/artifact/78XDhEavbRkoePCzuSbNsp (copy also lives in `landing-page.html` next to this file)
**Application / booking:** https://osw86s5725y.typeform.com/to/uuvewuOd

---

## 1. The math behind 30 seats

These are planning assumptions, not benchmarks. Swap in your real numbers once you have a week of data.

| Step | Assumed rate | Needed for 30 seats |
|---|---|---|
| Calls booked | | ~170 |
| Calls held (show rate) | 70% | ~120 |
| Seats sold (close rate on held calls) | 25% | 30 |

You won't book 170 calls in one week, and you don't need to. Launch week has one job: fill the calendar fast and sell the first 8 to 12 seats while attention is highest. The rest of the seats come from a slower drumbeat between December and the January close.

**Launch week target:** 50 calls booked, 10 seats sold.

**Daily scoreboard to track:** Typeform starts, Typeform completions, calls booked, calls held, seats sold. If completions are high but bookings are low, the problem is the scheduling step. If bookings are high but shows are low, fix your reminders (section 7).

---

## 2. Thanksgiving week changes the plan

Thursday Nov 26 is Thanksgiving and Friday is Black Friday. People are distracted Thursday and inboxes are flooded Friday. So the plan front-loads Monday through Wednesday, skips Thursday, and uses the Black Friday to Cyber Monday window for a founding-seat deadline (people already expect a deal to end Monday night).

| Day | Email | Social | Direct outreach |
|---|---|---|---|
| **Mon Nov 23** | Email 1: Doors open | LinkedIn post 1 (announcement) | DM your warmest 50 people |
| **Tue Nov 24** | Email 2: The pipeline | LinkedIn post 2 (the build) | Reply to every comment and DM |
| **Wed Nov 25** | Email 3: "Can I fit this in?" | Short video or story Q&A | Follow up on Monday DMs |
| **Thu Nov 26** | None | None (optional: a short thank-you post) | None |
| **Fri Nov 27** | Email 4: Founding seats | LinkedIn post 3 (founding offer) | DM anyone who started the Typeform but didn't book |
| **Sat Nov 28** | None | Repost post 3 to stories | |
| **Sun Nov 29** | Email 5: Who this isn't for | | |
| **Mon Nov 30** | Email 6a (9am ET) + 6b (7pm ET): Founding seats close tonight | Last-call post | Personal texts/DMs to booked-but-undecided |

**Calendar tip:** Block 20-minute call slots heavily on Mon Nov 30 and Tue Dec 1. Deadline days pull in a big share of the week's bookings.

**Countdown timer:** `assets/countdown-timer.html` already supports a fixed close. For this launch, set `fixed.date` to `2026-11-30` and `time` to `23:00` (ET) before pasting it into the page or emails.

---

## 3. Founding-seat offer (decision needed from you)

A deadline gives people a reason to book this week instead of "sometime in December." The offer below is a suggestion. Pick whatever you're comfortable giving.

**Suggested:** The first 10 people who enroll, or anyone who enrolls by Monday Nov 30 at 11pm ET (whichever comes first), get **the 4-week internship included at no extra cost**.

Why this one: the internship price is still an open item, so it's a bonus with a high perceived value that doesn't cut your core price. Other options if you'd rather not give the internship away:

- An extra 1:1 coaching session with Kedeisha
- A private resume and LinkedIn teardown before Demo Day
- A founding price that goes up on Dec 1

Every email from Email 4 on refers to this as **[FOUNDING BONUS]**. Do a find-and-replace once you decide.

---

## 4. Emails

Sender: Kedeisha. Plain text style, no heavy design. Each email has one link, the booking link. Use the UTM links in section 8 so you can see which email drove which call.

### Email 1: Doors open (Mon Nov 23, 10am ET)

**Subject:** I'm opening 30 seats for a live bootcamp
**Preview:** Analytics engineering, 8 weeks, starts in January

Hi {first_name},

For the past few months I've been building a live bootcamp for analysts who want to move into analytics engineering. It's ready, and I'm opening it to 30 people.

If you know some SQL and you're tired of being the person who cleans up the data before anyone can use it, this was made for you.

Over 8 weeks you'll build one pipeline for a fictional company. It starts as a raw HYROS export and ends as a tested, automated pipeline with a stakeholder dashboard on top. You'll present it live to me at Demo Day.

It runs on Databricks, Spark SQL, Tableau, GitHub and Claude. You get two live 2-hour sessions a week, weekly office hours, and a 90-minute one-on-one coaching session with me.

Cohort 1 starts in late January. Seats go through a short call so I can make sure it fits where you are right now.

[Book a 20-minute call here]

Kedeisha

P.S. If you're still new to SQL, you can still apply. There's pre-work built in, and I'll tell you honestly on the call if the next cohort is a better fit.

---

### Email 2: The pipeline (Tue Nov 24, 10am ET)

**Subject:** what you'd actually build in week 1
**Preview:** Raw export to a Tableau chart in the first week

Hi {first_name},

I wanted people to have something real running in the first week, so that's how the bootcamp starts.

In week one of the bootcamp you take a raw HYROS export, load it into Databricks, and get a working chart in Tableau. It won't be pretty yet. But it'll run end to end, and every week after that you make it better.

Week 2 you add YouTube data. Week 3 is Meta ad spend, so you can calculate cost per lead and CAC, which are the numbers marketing leaders ask about every Monday morning. Then you model it properly as a star schema, add tests and a data dictionary, and schedule it as an automated job. In week 6 we break it on purpose so you know what to do when a run fails at 7am.

By week 8 you have something you can walk a hiring manager through line by line, because you built every piece of it.

If that sounds like the project you've been meaning to build on your own, book a call and I'll show you how the 8 weeks would map to your current role.

[Book your call]

Kedeisha

---

### Email 3: Can I fit this in? (Wed Nov 25, 10am ET)

**Subject:** "I work full time, can I actually do this?"
**Preview:** The honest time commitment

Hi {first_name},

This is the question I get most, so I'll answer it directly.

Plan on 8 to 10 hours a week. That's 4 hours of live sessions (two 2-hour blocks) plus 4 to 6 hours building your own pipeline whenever it suits you. Some weeks run heavier, especially when you add a new data source.

It's a real commitment, and I'd rather tell you that now than have you find out in week 3.

The program is built for people with full-time jobs. There are weekly office hours for when you get stuck, and the build work is broken into pieces you can do on a lunch break or on a Sunday morning.

A few other things people ask about:

- **Python?** Not needed to start. It comes in during week 8, and we start from the basics.
- **SQL level?** If you can write a JOIN and a GROUP BY, you're ready. If not, the week 0 pre-work gets you there.
- **Cost?** We cover pricing and payment options on the call once we know it's a fit.

If you're on the fence because of time, book a call anyway. We'll look at your actual week and figure out whether January works.

[Book your call]

Kedeisha

Have a good Thanksgiving if you're celebrating.

---

### Email 4: Founding seats (Fri Nov 27, 11am ET)

**Subject:** something for the first 10
**Preview:** Ends Monday night

Hi {first_name},

I'm skipping the Black Friday sale. But I do want to reward the people who commit early to Cohort 1.

Anyone who enrolls by Monday, Nov 30 at 11pm ET gets **[FOUNDING BONUS]**. It's capped at the first 10 people, so it may close before Monday.

Quick recap of the bootcamp: 8 weeks, live, starts late January. You build one real pipeline from a raw marketing export to a stakeholder dashboard, then present it at Demo Day. Seats go through a 20-minute call.

If you've been meaning to book, this weekend is the time to do it.

[Grab a call slot]

Kedeisha

---

### Email 5: Who this isn't for (Sun Nov 29, 4pm ET)

**Subject:** please don't join if...
**Preview:** A few reasons to wait

Hi {first_name},

I'd rather have 30 people who finish than 30 people who enroll. So a few honest reasons to skip this cohort:

If you can't give it 8 hours a week between late January and March, wait for the next one. Falling behind in a live program is no fun.

If you want a certificate more than a project, this probably isn't it. The thing you leave with is a working pipeline in your GitHub and a Demo Day presentation.

And if you've never written any SQL at all, start with the fundamentals first. Reply to this email and I'll point you to where to begin.

If none of that is you, the founding bonus ([FOUNDING BONUS]) ends tomorrow night at 11pm ET.

[Book your call]

Kedeisha

---

### Email 6a: Last day (Mon Nov 30, 9am ET)

**Subject:** founding seats close tonight
**Preview:** 11pm ET

Hi {first_name},

Short one. The founding bonus for Cohort 1 ([FOUNDING BONUS]) closes tonight at 11pm ET.

I've opened extra call slots today and tomorrow morning. If you book a call today, you get the bonus even if we talk tomorrow.

[Pick a time today]

Kedeisha

### Email 6b: Final hours (Mon Nov 30, 7pm ET)

**Subject:** 4 hours left
**Preview:** Then the founding bonus is gone

Hi {first_name},

The founding bonus ends at 11pm ET tonight. After that, seats are still open (until all 30 are gone), but without [FOUNDING BONUS].

If you've had the tab open all week, book the call. Twenty minutes and you'll know whether this fits.

[Book your call]

Kedeisha

> Note on 6a: the "book today, talk tomorrow" rule matters. It stops the deadline from being limited by your calendar. Make sure your Typeform/scheduler timestamps the booking.

---

## 5. LinkedIn posts

### Post 1: Announcement (Mon Nov 23)

I've been quietly building something for analysts, and today I'm opening it up.

It's an 8-week live bootcamp for people who want to move from analyst to analytics engineer.

Over the 8 weeks you build one pipeline for a fictional company, starting with a raw HYROS export in week 1. By week 8 it has a star schema, tests, a data dictionary, an automated job, and a stakeholder dashboard on top. Then you present it live at Demo Day.

Stack: Databricks, Spark SQL, Unity Catalog, Lakeflow Jobs, Tableau, GitHub, and Claude.

Cohort 1 starts late January and I'm capping it at 30 so I can coach every person one-on-one.

If you know some SQL and this sounds like your next step, the link to book a call is in the comments.

*(First comment: booking link with `utm_source=linkedin&utm_content=post1`)*

### Post 2: The build (Tue Nov 24)

What a raw marketing export looks like in week 1 of my bootcamp vs. week 8.

Week 1: a CSV from HYROS, loaded into Databricks, with one chart in Tableau. Ugly but it works.

Week 3: YouTube and Meta spend are joined in. Now you can see cost per lead and CAC by channel.

Week 4: it's a proper star schema, so other people can query it without asking you what a column means.

Week 6: it runs on a schedule. We break it on purpose so you practice fixing a failed run.

Week 8: a stakeholder dashboard, an A/B test analysis, and a live demo.

Same project the whole way through. You leave with something you can walk an interviewer through line by line.

30 seats, starts late January. Call link in the comments.

*(Best as a carousel: one slide per week showing the pipeline diagram growing.)*

### Post 3: Founding seats (Fri Nov 27)

No Black Friday sale from me, but there is something for early movers.

The first 10 people to enroll in Cohort 1 of the AI Analytics Engineer Bootcamp (or anyone who enrolls by Monday 11pm ET) get [FOUNDING BONUS].

8 weeks, live, starts late January. You build a real pipeline from raw export to dashboard, and present it at Demo Day.

Book a 20-minute call from the link in the comments and we'll see if it fits.

---

## 6. Direct messages

These usually convert better than anything else in week one. Start with people who already know you: past students, community members, people who've commented on your posts, anyone who's asked you how to break into analytics engineering.

**Opener (warm contact):**
> Hey {name}, I just opened a live analytics engineering bootcamp for January (8 weeks, capped at 30). You came to mind because of {specific thing: their role / something they asked / a post}. Want me to send you the details?

**If they say yes:**
> Here's the page: {link}. The short version is you build one pipeline end to end, from a raw marketing export to a dashboard, and present it at Demo Day. If it looks interesting, grab a 20-min call and I'll tell you honestly whether it fits where you are.

**Follow-up (no reply after 2 days):**
> No pressure on this at all. Just a heads-up that the founding bonus for the first 10 seats ends Monday night. Happy to answer anything here if a call feels like too much.

**Typeform started but didn't book (Friday):**
> Hey {name}, I saw you started the application for the bootcamp. Did something come up, or did you have a question I can answer here?

---

## 7. After someone books

Show rate is where a lot of call-based launches leak. These four messages protect it.

**Confirmation (instant, email):**
**Subject:** you're booked: {date} at {time}

> Hi {first_name}, you're on my calendar for {date} at {time} {timezone}. Here's the link: {meeting_link}.
>
> To make the 20 minutes useful, think about one thing before we talk: what does your work look like today, and what do you want it to look like a year from now?
>
> If something comes up, you can reschedule here: {reschedule_link}.
>
> Kedeisha

**Reminder (24 hours before, email):** "Quick reminder that we're talking tomorrow at {time}. Here's the link again: {meeting_link}."

**Reminder (1 hour before, SMS if you collect phone numbers):** "Hi {first_name}, it's Kedeisha. We're on at {time}. Link: {meeting_link}"

**No-show (30 minutes after a missed call):**
> Hi {first_name}, looks like we missed each other. No problem at all. You can grab a new time here: {reschedule_link}. Seats are filling, so I'd try to pick one this week.

---

## 8. Setup checklist before Monday

- [ ] **Finish the Typeform.** Suggested questions: name, email, phone (optional, for SMS reminder), current role, SQL comfort (1 to 5), "What do you want to be doing a year from now?", and "Can you commit 8 to 10 hours a week from late January?" End it with a scheduler (Calendly, SavvyCal, or GHL calendar) embedded on the last screen so they book in the same flow.
- [ ] **Add hidden fields** `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` in Typeform, so the links below carry through and you can see which email or post drove each call.
- [ ] **Decide the founding bonus** and replace [FOUNDING BONUS] everywhere.
- [ ] **Confirm the start date.** The curriculum doc says mid-December kickoff, but the plan is late January. The page and emails say "late January 2027." Add the exact date once it's set.
- [ ] **Move the landing page to your domain.** The artifact link is private to you until you share it. For a public launch, rebuild it in GHL (or paste the HTML) on datainmotion.co so you can add the HYROS tracking script and your pixel.
- [ ] **Load emails into Kit** as scheduled broadcasts. Segment out current students and anyone who has already booked a call.
- [ ] **Set the countdown timer** to Nov 30, 11pm ET.
- [ ] **Block call slots** for Nov 23 through Dec 2, with extra capacity on Nov 30 and Dec 1.
- [ ] **Have a payment link ready** for the call. People who decide on the call should be able to pay before you hang up.

**UTM links** (base: `https://osw86s5725y.typeform.com/to/uuvewuOd`)

| Where | Append |
|---|---|
| Email 1 | `?utm_source=kit&utm_medium=email&utm_campaign=cohort1_launch&utm_content=email1` |
| Email 2 to 6b | same, with `utm_content=email2` … `email6b` |
| LinkedIn post 1 to 3 | `?utm_source=linkedin&utm_medium=social&utm_campaign=cohort1_launch&utm_content=post1` |
| DMs | `?utm_source=dm&utm_medium=direct&utm_campaign=cohort1_launch` |
| Landing page buttons | `?utm_source=landing&utm_medium=web&utm_campaign=cohort1_launch` |

---

## 9. After launch week (Dec 1 to January close)

Launch week should put you around a third of the way to 30. To get the rest:

- **Weekly email** through December: one student-style story or build walkthrough, one booking link.
- **A live free workshop** in mid-December (for example, "Build a cost-per-lead model in Databricks in 60 minutes") with the call link at the end. This is usually the second-biggest source of calls after launch week.
- **Second deadline** in early January: "Seats close Jan X" with a real enrollment cutoff a week before kickoff.
- **Referral ask** to everyone who enrolls: "Know someone who should be in this cohort with you?"
