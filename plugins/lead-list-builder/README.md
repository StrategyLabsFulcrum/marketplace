# Lead List Builder

A complete lead generation and pipeline management system — from initial research through ongoing discovery, outreach, tracking, reporting, and tool integrations. Built by Strategy Labs.

## What It Does

The Lead List Builder uses web research to find real leads, generates structured lists, drafts personalized outreach, tracks leads through a pipeline, discovers new leads automatically, connects to your CRM/email/calendar/social tools, and provides daily/weekly/monthly workflow management with interactive dashboards.

## Commands

### Setup & Research
| Command | Description |
|---------|-------------|
| `/build-lead-list` | Full wizard: brand context → tool connections → lead types → geography → research → generate list + dashboard |
| `/connect-tools` | Configure integrations with CRM, email, calendar, LinkedIn, Facebook, Meta Ads, etc. |

### Outreach & Tracking
| Command | Description |
|---------|-------------|
| `/lead-outreach` | Draft personalized outreach messages per lead type and channel with follow-up sequences |
| `/update-leads` | Track status, add notes, find net-new leads, refresh stale leads, bulk updates |
| `/lead-dashboard` | Generate or regenerate an interactive HTML dashboard for any lead list |

### Workflow & Reporting
| Command | Description |
|---------|-------------|
| `/daily-alerts` | Morning briefing: overdue follow-ups, new responses, proximity opportunities, scheduled meetings |
| `/weekly-review` | Pipeline performance: movement, velocity, wins/losses, stale leads, recommended actions |
| `/monthly-report` | Conversion metrics, channel analysis, strategy recommendations, quarterly ROI audit |

### Growth
| Command | Description |
|---------|-------------|
| `/lead-discovery` | Automated research for net-new leads with deduplication, smart scoring, and enrichment |

## Getting Started

1. **Install the plugin** in Claude Cowork
2. **(Recommended)** Run the Brand Knowledge Center plugin first
3. **Run `/build-lead-list`** — walks through the full setup:
   - Load brand context
   - Connect your tools (CRM, email, calendar, social)
   - Define lead types and geography
   - Research and generate leads
   - Set up automated discovery
4. **Run `/daily-alerts`** each morning for your action plan
5. **Run `/weekly-review`** every Monday to track performance
6. **Run `/lead-discovery`** weekly to grow your list

## Workflow Cadence

| Frequency | Command | Time | What Happens |
|-----------|---------|------|--------------|
| Daily | `/daily-alerts` | 5-10 min | Follow-up reminders, new responses, proximity drop-ins, meeting prep |
| After each action | `/update-leads` | 30 sec | Log calls, emails, meetings, status changes |
| Weekly | `/weekly-review` | 15-20 min | Pipeline review, velocity metrics, plan the week |
| Weekly | `/lead-discovery` | 10 min | Find new leads, detect changes, grow the list |
| Bi-weekly | `/lead-outreach` | 10 min | Batch draft outreach messages |
| Monthly | `/monthly-report` | 30 min | Conversion metrics, channel analysis, strategy |
| Quarterly | `/monthly-report` | 1 hour | Full ROI audit, expansion planning, pipeline health |

## Lead Lifecycle

```
SETUP → DISCOVER → QUALIFY → OUTREACH → FOLLOW UP → CONVERT → NURTURE → EXPAND
  ↑                                                       |              |
  |                     Referral chains ←─────────────────┘              |
  └──────────────── New lead types / expanded geo ←──────────────────────┘
```

## Lead Discovery

The plugin continuously grows your list by monitoring:
- **New business filings** — Companies opening in your area
- **Professional directories** — New attorneys, adjusters, professionals
- **Franchise announcements** — New SERVPRO, PuroClean, etc. locations
- **Firm website changes** — New hires at target companies
- **Google Maps** — Recently added businesses in target categories
- **Referral chains** — Introductions from converted leads

All new leads are deduplicated, scored, enriched, and presented for approval before being added.

## Tool Connections

Connect your existing tools for seamless lead management:

| Priority | Tools | Integration Type |
|----------|-------|-----------------|
| Must Have | CRM (House Call Pro, HubSpot, Salesforce) | Auto CSV export |
| Must Have | Email (Gmail, Outlook, Klaviyo) | Outreach draft formatting |
| Must Have | Calendar (Google, Outlook, Apple) | .ics meeting generation |
| High Value | LinkedIn, Facebook | Profile tracking + outreach drafts |
| High Value | Phone/SMS | Click-to-call + scripts |
| Nice to Have | Meta Ads, Google Ads | Audience export + source tracking |
| Nice to Have | QuickBooks | Revenue tracking for ROI |

Dashboard action buttons connect directly to your tools: `[Email] [Call] [LinkedIn] [Facebook] [Schedule] [SMS]`

## Dashboard Features

The interactive HTML dashboard includes:
- **Morning alerts** — Follow-ups due, responses, proximity leads
- **Pipeline funnel** — Visual flow from discovery through conversion
- **Filter bar** — By type, location, relevance, status, channel + full-text search
- **Sortable lead table** — Click to expand for full details, outreach history, action buttons
- **Outreach tracker** — Follow-ups due, recent activity, stale alerts
- **CSV export** — Download filtered views for CRM import

## Reports

- **Weekly:** Pipeline movement, velocity metrics, channel performance, recommended actions
- **Monthly:** Conversion rates, ROI analysis, strategy recommendations, discovery summary
- **Quarterly:** Full audit — ROI, win/loss patterns, list health, expansion planning

## Integration

Works best with the **Brand Knowledge Center** plugin. Brand context enables:
- Smarter lead type suggestions
- Outreach messages in brand voice
- Channel recommendations aligned to your platforms
- Tool auto-detection from your digital ecosystem

## Output Structure

```
lead-lists/
├── [list-name].csv                     # Full lead data (CRM-importable)
├── [list-name].md                      # Human-readable lead details
├── [list-name]-outreach.md             # Outreach drafts + follow-up sequences
├── [list-name]-dashboard.html          # Interactive dashboard
├── .config/
│   ├── connections.md                  # Tool integration settings
│   ├── discovery-settings.md           # Discovery frequency + sources
│   └── discovery-log.md               # Discovery run history
├── .exports/
│   ├── [crm]-import.csv               # CRM-formatted export
│   ├── meta-audience.csv              # Meta Custom Audience export
│   └── events/                         # .ics calendar files
└── reports/
    ├── weekly-[date].md               # Weekly review reports
    └── monthly-[month]-[year].md      # Monthly/quarterly reports
```

## Tips

- **Start with Brand Knowledge Center** for auto-detected tools and brand-voice outreach
- **Run `/daily-alerts` every morning** — it takes 5 minutes and keeps your pipeline moving
- **Drop-in visits win** — if you're already in the area, stop by. In-person converts at 2-3x email
- **Discovery keeps the list fresh** — run weekly to catch new businesses, hires, and opportunities
- **Track job values on converted leads** — this powers the quarterly ROI analysis
- **Export to your CRM regularly** — the CSV auto-updates, just import after each update cycle
