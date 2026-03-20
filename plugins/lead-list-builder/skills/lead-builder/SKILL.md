---
name: lead-builder
description: >
  Lead List Builder for researching, generating, and managing targeted lead lists.
  Use when the user mentions "lead list", "find leads", "build leads", "prospecting",
  "lead generation", "outreach", "find contacts", "business development", "sales leads",
  "lead tracking", "lead dashboard", "lead status", "find partners", "find influencers",
  "find retailers", "find buyers", "daily leads", "weekly review", "monthly report",
  "lead discovery", "connect tools", "CRM sync", or wants to research and compile a list
  of people or companies to contact for business purposes.
version: 2.0.0
---

# Lead List Builder

A complete lead generation and management system — from initial research through ongoing pipeline management, automated discovery, outreach tracking, tool integrations, and reporting.

## How It Works

The Lead List Builder has eight layers:

1. **Brand Context Layer** — Reads brand knowledge to understand the business, products, audience, and channels. Informs what types of leads are relevant and how to position outreach.
2. **Tool Connections Layer** — Identifies and configures integrations with CRM, email, calendar, social, and advertising tools for seamless lead management.
3. **Research Layer** — Uses web search to find real leads matching the user's criteria. Searches directories, LinkedIn, Google Maps, industry sites, social platforms, and other public sources.
4. **List Management Layer** — Structures leads into a searchable CSV and markdown format with deduplication and categorization.
5. **Outreach Layer** — Drafts personalized outreach messages per lead type and suggests the best channel to reach each lead.
6. **Dashboard Layer** — Generates a deployable interactive HTML dashboard for visualizing, filtering, and tracking leads.
7. **Workflow Layer** — Daily alerts, weekly reviews, monthly reports, and quarterly audits that keep the pipeline moving.
8. **Discovery Layer** — Automated recurring research that finds net-new leads, detects changes, and keeps the list growing.

## Brand Context Integration

Before building a lead list, check for a `brand-knowledge-center/` folder in the user's working directory.

### If brand knowledge exists:
1. Read `business-overview.md` — Industry, products, revenue, team
2. Read `audience-messaging.md` — Audience segments, messaging framework, content pillars
3. Read `digital-ecosystem.md` — Active platforms, tools, advertising channels
4. Read `competitive-landscape.md` — Competitors and positioning
5. Read `brand-identity.md` — Brand pillars, voice, point of difference

Use this context to:
- Suggest relevant lead types based on the business model
- Tailor outreach messaging to brand voice
- Identify which channels the brand already uses for sourcing
- Position the brand's value prop in outreach drafts

### If NO brand knowledge exists:
Ask the user:
1. What does your business do? (products/services, industry)
2. Who are your ideal customers or partners?
3. What's your value proposition in one sentence?
4. What channels do you currently use for sales/outreach?

## Lead Types

Based on brand context, suggest relevant lead categories. Common types:

### For eCommerce / DTC Brands
| Lead Type | Description | Example Titles |
|-----------|-------------|----------------|
| Retail/Wholesale Buyers | Stores that could carry the brand | Buyer, Purchasing Manager, Store Owner, Merchandiser |
| Influencers/Creators | Social media creators for partnerships | Content Creator, Influencer, Brand Ambassador |
| Media/Press | Journalists and bloggers for coverage | Editor, Writer, Journalist, Blogger, Podcast Host |
| Partnership/Co-brand | Complementary brands for collaboration | Marketing Director, Brand Manager, Partnership Lead |
| Event/Pop-up | Venues and event organizers | Event Coordinator, Venue Manager, Market Organizer |
| Corporate/Gift Buyers | Companies for bulk/custom orders | Office Manager, HR Director, Corporate Gifting Manager |

### For Agencies / B2B Services
| Lead Type | Description | Example Titles |
|-----------|-------------|----------------|
| Decision Makers | People who approve vendor contracts | CEO, CMO, VP Marketing, Director of Growth |
| Marketing Managers | Day-to-day marketing operators | Marketing Manager, Digital Marketing Manager, eComm Manager |
| Founders/Owners | Startup and SMB owners | Founder, Owner, Co-founder, Managing Partner |
| Procurement | Enterprise purchasing contacts | Procurement Manager, Vendor Relations |

### For Local / Hospitality Businesses
| Lead Type | Description | Example Titles |
|-----------|-------------|----------------|
| Local Partners | Nearby businesses for cross-promotion | Owner, General Manager, Marketing Manager |
| Tourism/Travel | Travel sites and guides | Travel Writer, Tourism Board Contact, Hotel Concierge |
| Event Planners | For catering, hosting, partnerships | Event Planner, Wedding Coordinator |
| Food/Lifestyle Media | Local food bloggers, reviewers | Food Blogger, Restaurant Critic, Local Journalist |

The user can also define custom lead types with their own titles and descriptions.

## Research Sources

When researching leads, use these public sources:

### Web Search
- **Google search** with targeted queries:
  - `"{job title}" "{industry}" "{location}" site:linkedin.com`
  - `"{company type}" "{city}" "{state}"`
  - `"top {industry} influencers" "{region}"`
  - `"{industry} directory" "{location}"`
  - `"{industry} trade show" "exhibitor list"`

### Platform-Specific
- **LinkedIn** — Search for people by title, company, location (public profiles)
- **Instagram** — Search hashtags and location tags for influencers/creators
- **Google Maps** — Search for local businesses by category and location
- **Industry directories** — Trade associations, chamber of commerce, professional orgs
- **Yelp/TripAdvisor** — For hospitality and local business leads
- **Crunchbase/AngelList** — For startup and tech company leads
- **Press/media databases** — Masthead pages, contributor lists, podcast directories

### Research Process
1. Build search queries based on lead type, geography, and filters
2. Execute searches across multiple sources
3. Extract: Name, Title, Company, Location, Contact info (if public), Source URL
4. Cross-reference to fill gaps (find a company on Google Maps → look up the owner on LinkedIn)
5. Verify information is current (check for recent activity, updated profiles)

## Lead Data Schema

Each lead record contains:

| Field | Description | Required |
|-------|-------------|----------|
| `id` | Auto-generated unique ID (L-001, L-002...) | Yes |
| `name` | Full name of the contact | Yes |
| `title` | Job title or role | Yes |
| `company` | Company or organization name | Yes |
| `lead_type` | Category (Retail Buyer, Influencer, etc.) | Yes |
| `email` | Email address (if publicly available) | No |
| `phone` | Phone number (if publicly available) | No |
| `linkedin` | LinkedIn profile URL | No |
| `instagram` | Instagram handle (for influencers/creators) | No |
| `website` | Company or personal website | No |
| `location` | City, State | Yes |
| `source` | Where the lead was found | Yes |
| `source_url` | URL where the lead info was found | No |
| `company_size` | Estimated company size | No |
| `industry` | Industry/vertical | No |
| `relevance_score` | 1-5 rating of how relevant this lead is to the brand | Yes |
| `suggested_channel` | Best channel to reach this lead | Yes |
| `outreach_status` | not_started, drafted, sent, responded, converted, declined, stale | Yes |
| `outreach_notes` | Notes on outreach attempts | No |
| `date_added` | Date the lead was added to the list | Yes |
| `last_updated` | Date the lead record was last updated | Yes |
| `tags` | Searchable tags | No |

## Relevance Scoring

Each lead gets a 1-5 relevance score based on:

| Score | Criteria |
|-------|----------|
| 5 — Hot | Perfect fit: right title, right industry, right location, evidence of interest (follows competitors, engages with similar brands) |
| 4 — Strong | Strong fit: most criteria match, high likelihood of interest |
| 3 — Good | Good fit: title and industry match, location may be broader, worth pursuing |
| 2 — Warm | Partial fit: some criteria match, may require more qualification |
| 1 — Long Shot | Loose fit: tangentially related, low priority but worth noting |

## Output Files

### Lead List CSV (`lead-lists/[list-name].csv`)

Full structured data with all fields from the schema. Importable into any CRM, spreadsheet, or email tool.

### Lead List Markdown (`lead-lists/[list-name].md`)

Human-readable version organized by lead type:

```markdown
# Lead List: [List Name]

## Summary
- **Total leads:** 47
- **Lead types:** Retail Buyers (18), Influencers (15), Media (8), Partners (6)
- **Geography:** Pacific Northwest (WA, OR)
- **Generated:** 2026-03-19
- **Relevance breakdown:** Hot (8), Strong (14), Good (16), Warm (7), Long Shot (2)

## Status Overview
- Not Started: 47
- Drafted: 0
- Sent: 0
- Responded: 0
- Converted: 0

---

## Retail Buyers

### L-001: Sarah Chen — Buyer, Mountain Outfitters
- **Company:** Mountain Outfitters (outdoor retail, ~15 employees)
- **Location:** Portland, OR
- **Source:** Google Maps + LinkedIn
- **LinkedIn:** linkedin.com/in/sarachen
- **Website:** mountainoutfitters.com
- **Relevance:** ⭐⭐⭐⭐⭐ (5) — PNW outdoor retailer, carries similar brands, recently expanded apparel section
- **Suggested Channel:** Email → LinkedIn follow-up
- **Outreach Status:** Not Started
- **Tags:** retail, portland, outdoor, apparel buyer

[...continues for all leads...]
```

## Outreach System

### Channel Selection Logic

For each lead, suggest the best outreach channel based on:

| Lead Type | Primary Channel | Secondary Channel | Notes |
|-----------|----------------|-------------------|-------|
| Retail/Wholesale Buyers | Email | Phone call | Formal intro, include line sheet/lookbook |
| Influencers/Creators | Instagram DM | Email | Casual, authentic, reference their content |
| Media/Press | Email | Twitter/X DM | Press angle, newsworthy hook, include press kit |
| Partnership Leads | Email | LinkedIn message | Mutual value prop, specific collaboration idea |
| Event/Pop-up Organizers | Email | Phone call | Event-specific pitch, include brand one-pager |
| Corporate/Gift Buyers | Email | LinkedIn message | Volume pricing, customization options |
| Local Business Partners | In-person visit | Email | Neighbor-to-neighbor, keep it casual |

### Outreach Message Templates

For each lead type and channel, generate personalized outreach drafts that:

1. **Use brand voice** — Pull tone and vocabulary from brand knowledge
2. **Reference something specific** — About the lead's business, recent post, or shared connection
3. **Lead with value** — What's in it for them, not what you want
4. **Include a clear ask** — Specific next step (meeting, sample, call)
5. **Keep it short** — 3-5 sentences for email, 2-3 for DM

### Email Template Structure

```
Subject: [Personalized — reference their business or a shared connection]

Hi [First Name],

[Opening — specific reference to their business, a recent post, or why you're reaching out to them specifically]

[Value prop — what's in it for them, tied to brand positioning]

[Ask — specific, low-friction next step]

[Sign-off in brand voice]
[Name]
[Brand]
```

### DM Template Structure (Instagram/LinkedIn)

```
Hey [First Name] — [specific compliment or reference to their content/business].

[One sentence on why you're reaching out + what's in it for them].

[Simple ask — "Would love to chat" or "Can I send you some info?"]
```

### Follow-Up Cadence

Suggest a follow-up sequence for each lead:

| Touchpoint | Timing | Channel | Action |
|------------|--------|---------|--------|
| Initial outreach | Day 0 | Primary channel | Send personalized message |
| Follow-up 1 | Day 3-5 | Same channel | Brief follow-up, add new value |
| Follow-up 2 | Day 7-10 | Secondary channel | Try alternate channel |
| Final follow-up | Day 14-21 | Primary channel | Last touch, leave door open |
| Mark stale | Day 30+ | — | Move to stale status if no response |

## Lead Status Tracking

### Status Definitions

| Status | Meaning | Next Action |
|--------|---------|-------------|
| `not_started` | Lead identified, no outreach yet | Draft outreach message |
| `drafted` | Outreach message drafted, not sent | Review and send |
| `sent` | Outreach sent, awaiting response | Wait, then follow up per cadence |
| `responded` | Lead replied (positive, neutral, or negative) | Respond and advance or close |
| `converted` | Lead became a customer/partner/collaborator | Move to active relationships |
| `declined` | Lead explicitly said no | Archive, revisit in 6+ months |
| `stale` | No response after full follow-up cadence | Archive or retry with new angle |

### Tracking Workflow

When updating lead status:
1. Update the `outreach_status` field in the CSV
2. Add a note to `outreach_notes` with the date and what happened
3. Update `last_updated` timestamp
4. Regenerate the markdown summary with updated status counts
5. Update the dashboard if deployed

## Net-New Lead Discovery

When adding new leads to an existing list:

### Deduplication Rules

Before adding any new lead, check against the existing list:

1. **Exact match** — Same name + same company = duplicate, skip
2. **Company match** — Same company, different contact = new lead (may be worth adding a second contact)
3. **Name match, different company** — Same person may have changed jobs, flag for review
4. **Similar company name** — Fuzzy match (e.g., "Mountain Outfitters" vs "Mountain Outfitters LLC") = likely duplicate, flag

### Net-New Research Process

1. Load existing `lead-lists/[list-name].csv`
2. Note all companies and names already in the list
3. Research with exclusion: search for new leads while filtering out known ones
4. Present only net-new leads:
   > "Found 12 new leads not in your current list. 3 are new contacts at companies you already have."
5. User confirms which to add
6. Append to existing CSV and regenerate markdown + dashboard

## Interactive Dashboard

### Dashboard Structure

Generate a single-file HTML dashboard (`lead-lists/[list-name]-dashboard.html`) with:

**Header Section:**
- List name, date generated, total leads
- Status summary bar (color-coded: not started, drafted, sent, responded, converted, declined, stale)

**Filter Bar:**
- Filter by: Lead Type, Location, Relevance Score, Status, Channel, Date Added
- Search box: search across name, company, title, tags
- Sort by: Relevance, Date Added, Status, Company, Location

**Lead Table:**
- Sortable, filterable table with all lead fields
- Color-coded relevance scores (5=green, 4=blue, 3=yellow, 2=orange, 1=gray)
- Color-coded status badges
- Click to expand: shows full lead details, outreach notes, suggested message
- Quick actions: Update status dropdown, add note

**Summary Cards:**
- Total leads by type (bar chart)
- Leads by status (pie chart)
- Leads by location (grouped list or map)
- Relevance distribution (bar chart)
- Outreach pipeline: not_started → drafted → sent → responded → converted (funnel)

**Outreach Tracker:**
- Timeline view of all outreach activity
- Upcoming follow-ups due
- Response rate metrics

### Dashboard Tech

- Single HTML file, no dependencies — uses inline CSS + vanilla JavaScript
- Responsive layout — works on desktop and mobile
- Data embedded as JSON in a `<script>` tag
- Export button: download current filtered view as CSV
- Print-friendly mode for sharing

### Dashboard Refresh

When the lead list is updated (status changes, new leads added), regenerate the dashboard HTML with the latest data. The dashboard file is always overwritten with the current state.

## Tool Connections

### Connections Audit

During initial setup (`/build-lead-list`) or via `/connect-tools`, audit the user's existing tools and configure integrations.

### Auto-Detection

If `brand-knowledge-center/digital-ecosystem.md` exists, pull known tools:
- CRM (House Call Pro, HubSpot, Salesforce, etc.)
- Email/SMS platform (Klaviyo, Mailchimp, House Call Pro, etc.)
- Advertising platforms (Meta Ads, Google Ads)
- Social accounts (Instagram, Facebook, LinkedIn, etc.)
- Calendar (Google Calendar, Outlook, Apple Calendar)
- Accounting (QuickBooks, Xero, etc.)

### Connection Types

| Type | How It Works |
|------|-------------|
| **API-connected** | Direct push/pull via API (HubSpot, Salesforce, Google Calendar) |
| **Template-based** | Generate import-ready files matching the tool's format (House Call Pro CSV, Klaviyo import) |
| **Manual tracking** | Store data in the lead list, user takes action in the tool (phone calls, in-person visits) |

### Connection Priority Tiers

| Priority | Tool Category | Why It Matters |
|----------|--------------|---------------|
| Must Have | CRM | Where leads become customers. Sync so team works from one system. |
| Must Have | Email | Primary outreach channel. Send, track, follow up. |
| Must Have | Calendar | Schedule meetings with prep notes on lead response. |
| High Value | LinkedIn | B2B outreach, profile viewing, connection requests. |
| High Value | Facebook | Local business engagement, community presence. |
| High Value | Phone/SMS | Direct outreach, especially for service businesses. |
| Nice to Have | Meta Ads | Retarget leads, build lookalike audiences from lead list. |
| Nice to Have | Google Ads | Track lead sources, optimize spend toward converting types. |
| Nice to Have | Accounting | Connect revenue to leads for ROI tracking. |

### Connection Config File

Store configuration in `lead-lists/.config/connections.md`:

```markdown
# Lead List — Tool Connections

## Connected Tools
| Tool | Type | Status | Details |
|------|------|--------|---------|
| [Tool Name] | [CRM/Email/etc.] | [Active/Template/Manual] | [Details] |

## CRM Field Mapping
| Lead List Field | CRM Field |
|----------------|-----------|
| name | Customer Name |
| email | Email |
| phone | Phone |
| company | Company |
| lead_type | Tag: Lead Type |
| outreach_status | Tag: Status |
| notes | Customer Notes |

## Outreach Channel Routing
| Lead Type | Primary | Secondary | Fallback |
|-----------|---------|-----------|----------|
| [Type] | [Channel] | [Channel] | [Channel] |
```

### Dashboard Action Buttons

When tools are connected, the dashboard adds action buttons per lead row:

| Button | Action | Link Type |
|--------|--------|-----------|
| Email | Opens mailto with pre-drafted subject | `mailto:` |
| Call | Click-to-call | `tel:` |
| LinkedIn | Opens their profile | URL |
| Facebook | Opens their page | URL |
| Schedule | Downloads .ics with prep notes | File download |
| SMS | Opens SMS with pre-drafted message | `sms:` |

## Workflow — Daily Alerts

### Morning Briefing

The `/daily-alerts` command generates a morning action plan:

1. **Overdue follow-ups** — Leads where outreach was sent and enough time has passed for the next follow-up per the cadence schedule. Color-coded by urgency (red = overdue, yellow = due today).
2. **New responses** — Leads whose status was updated to "responded" since last check. Prompt to schedule meeting or reply.
3. **Proximity opportunities** — If the user provides today's location/schedule, show uncontacted leads within a configurable radius (default 2 miles). Suggest drop-in visits.
4. **Today's scheduled meetings** — Pull from outreach notes for any meetings noted for today. Show prep notes.
5. **Quick stats** — Pipeline snapshot: total leads, how many in each status, response rate trend.

### Alert Prioritization

Actions are prioritized in this order:
1. Respond to new responses (highest — a warm lead is cooling)
2. Overdue follow-ups (they're past the cadence window)
3. Today's follow-ups (due today per cadence)
4. Proximity drop-ins (opportunistic, if user is already nearby)
5. New outreach (if capacity allows, suggest next batch from Not Started)

### Action Logging

After each action, prompt the user to log what happened:
- Status change (sent → responded, etc.)
- Note with timestamp
- Next action scheduled (follow-up date, meeting date)
- Update dashboard automatically

## Workflow — Weekly Review

### Pipeline Summary

The `/weekly-review` command generates a weekly performance report:

1. **Pipeline movement** — How many leads moved between statuses this week
2. **Outreach activity** — Messages sent, responses received, meetings scheduled
3. **Wins and losses** — Converted leads (celebrate), declined leads (learn from)
4. **Going stale** — Leads with no activity in 14+ days, not in terminal status
5. **Velocity metrics:**
   - Average days from first contact to response
   - Response rate by channel (email vs. phone vs. LinkedIn vs. drop-in)
   - Response rate by lead type
   - Best day/time patterns (if enough data)
6. **Recommended actions** — Specific leads to contact this week, follow-ups due, suggested batch size

### Discovery Prompt

At the end of each weekly review, prompt:
> "Last lead discovery run was [X] days ago. Run discovery now to find net-new leads?"

If discovery hasn't run in 7+ days, recommend running it.

## Workflow — Monthly Report

### Conversion Metrics

The `/monthly-report` command generates a comprehensive monthly analysis:

1. **Funnel visualization:**
   ```
   Not Started (X) → Drafted (X) → Sent (X) → Responded (X) → Converted (X)
                                                         ↘ Declined (X)
                                              ↘ Stale (X)
   ```

2. **Conversion metrics:**
   - Total leads in pipeline
   - Outreach sent (% of total contacted)
   - Response rate (responses / sent)
   - Meeting rate (meetings / sent)
   - Conversion rate (converted / sent)
   - Average deal value from converted leads (if tracked)

3. **By lead type:**
   - Response rate per type
   - Conversion rate per type
   - Best and worst performing types
   - Recommendation: double down on winners, adjust approach for losers

4. **By channel:**
   - Response rate per channel (email, phone, LinkedIn, drop-in, etc.)
   - Best performing channel overall
   - Recommendation: shift strategy based on data

5. **Strategy recommendations:**
   - Which lead types to prioritize next month
   - Channel strategy adjustments
   - Geographic expansion suggestions (if list is saturating)
   - New lead type suggestions based on conversion patterns

6. **Discovery summary:**
   - New leads added this month
   - Discovery runs completed
   - List growth rate

## Workflow — Quarterly Audit

### Full Pipeline Audit

The quarterly audit (triggered within `/monthly-report` every 3 months) includes everything in the monthly report plus:

1. **ROI analysis:**
   - Total leads generated (cumulative)
   - Converted to active relationships
   - Jobs/revenue received from lead referrals
   - Estimated lifetime value of converted leads
   - Time invested vs. value generated
   - Cost per converted lead

2. **Win/loss analysis:**
   - Why leads converted (common patterns)
   - Why leads declined or went stale (common patterns)
   - Demographic/firmographic patterns in wins vs. losses

3. **List health:**
   - % of list contacted
   - % in terminal states (converted + declined)
   - % stale (needs refresh or archive)
   - Active pipeline (sent + responded)
   - Untouched inventory (not started)

4. **Expansion planning:**
   - List saturation by lead type and geography
   - New lead types to explore (based on what converted)
   - Geographic expansion opportunities
   - Referral chain mapping from converted leads

5. **Stale lead refresh:**
   - All stale leads reviewed
   - Re-research for job changes, company updates, new contact info
   - Recommend: retry with new angle, archive, or remove

## Automated Lead Discovery

### Discovery System

The `/lead-discovery` command is the engine for continuously growing the lead list with net-new, deduplicated leads.

### Discovery Settings

Stored in `lead-lists/.config/discovery-settings.md`:

```markdown
# Lead Discovery Settings

## Schedule
- **Frequency:** weekly
- **Last run:** [ISO date]
- **Next run:** [ISO date]

## Search Criteria
- **Lead types monitored:** [list]
- **Geography:** [geo definition]
- **Filters:** [any additional filters]

## Discovery Sources
- **New business filings:** [state registry URLs]
- **Professional directories:** [bar association, trade org URLs]
- **Google Maps monitoring:** [category + location queries]
- **Franchise announcements:** [franchise brands to watch]
- **Referral prompts:** [enabled/disabled]

## Deduplication
- **Existing list:** [path to CSV]
- **Known companies:** [auto-populated from CSV]
- **Known contacts:** [auto-populated from CSV]
```

### Discovery Sources

| Source | What It Catches | How |
|--------|----------------|-----|
| New business filings | New companies opening in the area | Search state business registrations, Google Maps "recently opened" |
| Job changes | Existing contacts who changed companies, new hires at target firms | LinkedIn profile changes, firm website team page updates |
| Franchise announcements | New franchise locations (SERVPRO, PuroClean, etc.) | Search franchise press releases, Google Maps |
| Professional directories | New professionals in the area (attorneys, adjusters) | State bar new admissions, trade association member lists |
| Google Maps monitoring | New businesses matching target categories | Search "[category] near [location]" filtered to recently added |
| Referral chains | Second-degree introductions from converted leads | Post-conversion prompt: "Who else should we know?" |
| Competitor client signals | Companies engaging with competitors | Social media research, review responses |
| Industry events | Conference attendee/exhibitor lists | Trade show websites, event directories |

### Discovery Run Process

1. **Load existing inventory** — Read CSV, extract all known names + companies
2. **Execute source searches** — Run queries across all configured discovery sources
3. **Categorize findings into buckets:**

| Bucket | What It Means | Action |
|--------|--------------|--------|
| Net-New Company | A company not in the list at all | Add as new lead |
| New Contact at Existing Company | A new person at a firm already in the list | Offer to add as additional contact |
| Lead Update | Something changed about an existing lead (promotion, new role, etc.) | Update existing record |
| Possible Duplicate | Fuzzy match — might be the same lead under a different name | Flag for user review |

4. **Smart score new leads** — Apply relevance scoring with bonus points:

| Signal | Score Boost |
|--------|-------------|
| Just opened / new to area (< 6 months) | +2 |
| Recently changed roles | +1 |
| Existing lead referred them | +2 |
| Engages with similar brands/competitors | +1 |
| High review count / active online presence | +1 |
| Fills a geographic gap in the list | +1 |

5. **Present findings** — Show all new discoveries grouped by bucket. User confirms which to add.
6. **Append to list** — Assign new IDs, update CSV, regenerate markdown + dashboard.

### Discovery History Log

Track all discovery runs in `lead-lists/.config/discovery-log.md`:

```markdown
# Lead Discovery Log

| Date | Type | Searched | New Found | Added | Skipped | Notes |
|------|------|----------|-----------|-------|---------|-------|
| 2026-03-19 | Initial build | Full research | 40 | 40 | 0 | First list |
| 2026-03-27 | Weekly discovery | All sources | 6 | 4 | 2 | 2 fuzzy dupes skipped |
```

### List Saturation Detection

Track coverage by lead type and geography. When a category reaches 80%+ saturation:

> "Your Estate/Probate Attorney list covers ~90% of firms in the Spokane 40-mile radius. Consider:
> - Expanding geography to 60 miles (adds Pullman, Moscow, Sandpoint)
> - Adding a new lead type (title companies, home inspectors, bankruptcy trustees)
> - Deepening existing — find additional contacts at firms where you only have one person"

### Referral Chain Discovery

After a lead converts, the plugin prompts:

1. "Congratulations on converting [Lead Name]! Who else could they introduce you to?"
2. "Based on [Lead Name]'s industry and network, here are 3-5 potential referral leads I'd suggest asking about:"
3. Add referred leads with source tagged as "Referral from [Lead Name]" and a +2 relevance boost.

## Lead Lifecycle — Complete Flow

```
SETUP → DISCOVER → QUALIFY → OUTREACH → FOLLOW UP → CONVERT → NURTURE → EXPAND
  ↑                                                       |              |
  |                     Referral chains ←─────────────────┘              |
  └──────────────── New lead types / expanded geo ←──────────────────────┘
```

| Stage | Plugin Feature | Command | Frequency |
|-------|---------------|---------|-----------|
| Setup | Brand context + tool connections | `/build-lead-list` | Once |
| Discover | Research + dedup + smart scoring | `/lead-discovery` | Weekly |
| Qualify | Relevance scoring + enrichment | Auto during discovery | — |
| Outreach | Personalized drafts + channel routing | `/lead-outreach` | Bi-weekly |
| Follow Up | Cadence tracking + alerts | `/daily-alerts` | Daily |
| Pipeline Review | Velocity metrics + strategy | `/weekly-review` | Weekly |
| Convert | Win/loss capture + relationship tracking | `/update-leads` | As needed |
| Analyze | Conversion metrics + ROI | `/monthly-report` | Monthly |
| Nurture | Referral prompts + re-engagement | `/lead-discovery` | Ongoing |
| Expand | New types + geo expansion + audit | `/monthly-report` (quarterly) | Quarterly |

## Calendar Integration

### Meeting Generation

When a lead status changes to "responded" and a meeting is appropriate:

1. **Prompt for meeting details:** date, time, duration, location (phone/in-person/video)
2. **Generate .ics file** with:
   - Event title: "Meeting: [Lead Name] — [Company]"
   - Pre-populated description with:
     - Lead summary (type, relevance, company, role)
     - Outreach history (what was sent, when they responded, what they said)
     - Talking points (customized based on lead type and brand context)
     - Contact info (phone, email, LinkedIn)
   - Location (address for in-person, link for video)
   - Reminder: 30 minutes before
3. **Post-meeting prompt** — On next `/daily-alerts` after the meeting time, ask:
   - "How did the meeting with [Lead Name] go?"
   - Status update options: converted, follow-up needed, declined
   - Capture notes

### .ics File Format

```
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART:[datetime]
DTEND:[datetime]
SUMMARY:Meeting: [Lead Name] — [Company]
DESCRIPTION:
  LEAD: [Name], [Title] at [Company]
  TYPE: [Lead Type] | RELEVANCE: [stars]

  HISTORY:
  - [Date]: Initial outreach sent via [channel]
  - [Date]: They responded: "[summary of response]"

  TALKING POINTS:
  - [Point 1 based on lead type + brand context]
  - [Point 2]
  - [Point 3]

  CONTACT:
  - Phone: [phone]
  - Email: [email]
  - LinkedIn: [url]
LOCATION:[location]
BEGIN:VALARM
TRIGGER:-PT30M
ACTION:DISPLAY
DESCRIPTION:Meeting with [Lead Name] in 30 minutes
END:VALARM
END:VEVENT
END:VCALENDAR
```

## CRM Sync

### Export Format

Generate CRM-ready CSV files that match the target CRM's import format:

**House Call Pro:**
- Customer Name, Email, Phone, Address, Tags, Notes
- Tags map: lead_type + outreach_status
- Notes map: outreach_notes (chronological)

**HubSpot:**
- First Name, Last Name, Email, Phone, Company, Job Title, Lead Status, Notes
- Lead Status maps to HubSpot lifecycle stages

**Salesforce:**
- First Name, Last Name, Email, Phone, Company, Title, Lead Source, Status, Description

### Sync Triggers

CRM export files are auto-regenerated:
- After every `/update-leads` run
- After every `/lead-discovery` run that adds new leads
- On manual request via `/connect-tools sync`

The CRM export file lives at `lead-lists/.exports/[crm-name]-import.csv`.
