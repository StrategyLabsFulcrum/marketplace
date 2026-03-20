# Daily Alerts

Morning briefing that shows what needs attention today — overdue follow-ups, new responses, proximity opportunities, scheduled meetings, and quick pipeline stats.

## Before Starting

1. Check for existing lead lists in `lead-lists/`.
   - If none exist: "No lead lists found. Run `/build-lead-list` first."
   - If multiple exist: Load all lists and combine for a unified view.
2. Read the CSV to compute all alerts.

---

## Section 1: Overdue Follow-Ups

Calculate which leads need follow-up based on the cadence schedule:

- **Follow-up 1 due:** Status = "sent" AND last_updated was 3-5 days ago AND no follow-up 1 logged
- **Follow-up 2 due:** Status = "sent" AND follow-up 1 was 7-10 days ago AND no follow-up 2 logged
- **Final follow-up due:** Status = "sent" AND follow-up 2 was 14-21 days ago AND no final follow-up logged
- **Should mark stale:** Status = "sent" AND last activity was 30+ days ago

Color-code by urgency:
- 🔴 **Overdue** — Past the follow-up window by 2+ days
- 🟡 **Due today** — Within the follow-up window
- ⚪ **Upcoming** — Follow-up due in next 2-3 days (preview only)

**Format:**

```
🔴 OVERDUE FOLLOW-UPS (3)
├── L-003 Kendel Froese — Froese Law PLLC
│   Status: sent | Last contact: 3/15 (email) | Follow-up #1 overdue by 2 days
│   Action: Send follow-up email or try phone (509) 514-5317
│
├── L-025 Wyatt Gardiner — STOP Restoration
│   Status: sent | Last contact: 3/14 (phone, no answer) | Follow-up #1 overdue by 3 days
│   Action: Try again by phone or send email
│
└── L-028 Kevin Bunce — AllKlean Inc.
    Status: sent | Last contact: 3/16 (email) | Follow-up #1 overdue by 1 day
    Action: Brief follow-up email with new value

🟡 DUE TODAY (2)
├── L-005 Holland McBurns — Evergreen Elder Law
│   Status: sent | Last contact: 3/13 (email) | Follow-up #2 due — try LinkedIn this time
│
└── L-033 Michael Kilpatrick — SERVPRO of CdA
    Status: sent | Last contact: 3/15 (phone) | Follow-up #1 due — same channel
```

---

## Section 2: New Responses

Check for any leads where `outreach_status` has changed to "responded" since the last daily alert:

```
🟢 NEW RESPONSES (1)
└── L-012 Kristina Mattson — Kristina Mattson Law
    Responded via email: "I'd love to learn more. Can you call me Thursday?"
    → Schedule meeting? [Yes — generate .ics with prep notes]
    → Reply now? [Draft a reply]
    → Just update status? [Mark as responded + add note]
```

For each response, offer:
1. Schedule a meeting (generate .ics with prep notes, talking points, contact info)
2. Draft a reply (use brand voice, reference their message)
3. Just log it (update status + add note)

---

## Section 3: Proximity Opportunities

Ask the user (or detect from calendar):
> "Do you have any appointments or estimates today? Share the address and I'll show nearby uncontacted leads."

If an address is provided, search leads within a configurable radius (default: 2 miles):

```
📍 NEARBY LEADS (3 within 1 mile of downtown Spokane)
You have an estimate at 10am near W Riverside Ave.

├── L-009 Terry Gobel — Gobel Law Office
│   421 W Riverside Ave, Ste 908 (0.2 miles)
│   Status: not_started | Relevance: ★★★★
│   Suggested: Drop off one-pager with receptionist
│
├── L-014 Emily Wilson — Spokane Wills, Trusts & Probate
│   707 W Main Ave (0.4 miles)
│   Status: not_started | Relevance: ★★★★
│   Suggested: Drop off one-pager, mention you work in the neighborhood
│
└── L-008 Steven Schneider — Steven Schneider Law
    1312 N Monroe St (0.9 miles)
    Status: not_started | Relevance: ★★★★
    Suggested: Drop off one-pager on the way back
```

---

## Section 4: Today's Scheduled Meetings

Scan outreach_notes for any meetings noted for today's date:

```
📅 TODAY'S MEETINGS (1)
└── 2:00 PM — Kristina Mattson, Kristina Mattson Law
    Type: Phone call | Duration: 15 min

    PREP NOTES:
    - Founding attorney, 24 years experience, licensed WA/CO/IL
    - Specializes in estate planning, probate, guardianship, Medicaid
    - She replied to our email saying "I'd love to learn more"

    TALKING POINTS:
    - JTC handles estate property demolition + cleanout
    - When her clients inherit property with structures to remove,
      JTC is the one call that handles everything
    - Offer: "Can I be the demo contractor you recommend to estate clients?"

    CONTACT:
    - Phone: (509) 688-4530
    - Email: kristina@kmattsonlaw.com
```

---

## Section 5: Quick Stats

Pipeline snapshot:

```
📊 PIPELINE SNAPSHOT
├── Total leads: 48
├── Not Started: 22 (46%)
├── In Progress: 18 (Drafted: 3, Sent: 12, Responded: 3)
├── Closed: 8 (Converted: 1, Declined: 2, Stale: 5)
├── Response rate (this week): 25%
├── Next discovery run due: March 27
```

---

## Section 6: Recommended Actions

Based on all the above, suggest a prioritized action list for today:

```
TODAY'S RECOMMENDED ACTIONS:
1. ☎️  Call Kristina Mattson at 2pm (meeting scheduled)
2. 📧 Send follow-up to Kendel Froese (overdue by 2 days)
3. 📧 Send follow-up to Kevin Bunce (overdue by 1 day)
4. ☎️  Try Wyatt Gardiner again by phone (overdue by 3 days)
5. 📍 Drop by Terry Gobel's office after your 10am estimate (0.2 miles away)
6. 📍 Drop by Emily Wilson's office (0.4 miles from Gobel)

Estimated time: 45 minutes of active outreach + 2 drop-in visits
```

---

## After Actions

After the user completes actions throughout the day, prompt them to log:
- "Did you reach Kendel Froese? Update status?"
- "How was the meeting with Kristina Mattson? Update status and notes?"
- "Did you drop by Terry Gobel's office? What happened?"

Each log entry:
1. Updates `outreach_status` in CSV
2. Appends timestamped note to `outreach_notes`
3. Updates `last_updated`
4. Auto-regenerates CRM export if connections are configured
5. Offers to regenerate dashboard
