---
name: lead-builder
description: >
  Lead List Builder for researching, generating, and managing targeted lead lists.
  Use when the user mentions "lead list", "find leads", "build leads", "prospecting",
  "lead generation", "outreach", "find contacts", "business development", "sales leads",
  "lead tracking", "lead dashboard", "lead status", "find partners", "find influencers",
  "find retailers", "find buyers", or wants to research and compile a list of people
  or companies to contact for business purposes.
version: 1.0.0
---

# Lead List Builder

A framework for researching, generating, tracking, and managing targeted lead lists with outreach drafting, channel sourcing, status tracking, and interactive dashboard deployment.

## How It Works

The Lead List Builder has five layers:

1. **Brand Context Layer** — Reads brand knowledge to understand the business, products, audience, and channels. Informs what types of leads are relevant and how to position outreach.
2. **Research Layer** — Uses web search to find real leads matching the user's criteria. Searches directories, LinkedIn, Google Maps, industry sites, social platforms, and other public sources.
3. **List Management Layer** — Structures leads into a searchable CSV and markdown format with deduplication and categorization.
4. **Outreach Layer** — Drafts personalized outreach messages per lead type and suggests the best channel to reach each lead.
5. **Dashboard Layer** — Generates a deployable interactive HTML dashboard for visualizing, filtering, and tracking leads.

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
