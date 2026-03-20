# Lead List Builder

Research, generate, and manage targeted lead lists with personalized outreach, status tracking, and interactive dashboards. Built by Strategy Labs.

## What It Does

The Lead List Builder uses web research to find real leads matching your brand, industry, and target criteria. It generates structured lead lists, drafts personalized outreach messages, tracks lead status through a pipeline, and deploys interactive HTML dashboards for visualizing your prospecting efforts.

## Commands

| Command | Description |
|---------|-------------|
| `/build-lead-list` | Full wizard: brand context → lead types → geography → research → generate list + dashboard |
| `/lead-outreach` | Draft personalized outreach messages per lead type and channel with follow-up sequences |
| `/update-leads` | Track status, add notes, find net-new leads, refresh stale leads, bulk updates |
| `/lead-dashboard` | Generate or regenerate an interactive HTML dashboard for any lead list |

## Getting Started

1. **Install the plugin** in Claude Cowork
2. **(Recommended)** Run the Brand Knowledge Center plugin first to set up your brand profile
3. **Run `/build-lead-list`** to start the research wizard
4. **Review leads** as they're found, adjust relevance, and confirm
5. **Run `/lead-outreach`** to draft personalized messages
6. **Run `/lead-dashboard`** to generate a visual tracker
7. **Use `/update-leads`** ongoing to manage your pipeline

## Lead Types

The plugin suggests lead types based on your brand and business model:

- **Retail/Wholesale Buyers** — Stores and shops to carry your products
- **Influencers/Creators** — Social media partnerships and content
- **Media/Press** — Journalists and bloggers for coverage
- **Partnership Leads** — Complementary brands for collaboration
- **Event/Pop-up Organizers** — In-person sales and visibility
- **Corporate/Gift Buyers** — Bulk and custom orders
- **Custom types** — Define your own with specific titles and criteria

## Research Sources

The plugin searches across public sources:
- Google Search (targeted queries by title, industry, location)
- LinkedIn (public profiles)
- Google Maps (local businesses)
- Instagram (influencers and creators)
- Industry directories and trade associations
- Press databases and media sites

## Output Structure

```
lead-lists/
├── [list-name].csv                    # Full structured data (CRM-importable)
├── [list-name].md                     # Human-readable lead details
├── [list-name]-outreach.md            # Drafted outreach messages + follow-up sequences
└── [list-name]-dashboard.html         # Interactive visual dashboard
```

## Lead Pipeline

Each lead moves through a tracked pipeline:

```
Not Started → Drafted → Sent → Responded → Converted
                                    ↘ Declined
                         ↘ Stale (30+ days no response)
```

## Dashboard Features

The interactive HTML dashboard includes:
- **Summary cards** — Total leads, by type, by status, pipeline funnel
- **Filter bar** — Filter by type, location, relevance, status, channel + full-text search
- **Sortable lead table** — Click to expand details, outreach notes, and suggested messages
- **Outreach tracker** — Follow-ups due, recent activity, stale lead alerts
- **CSV export** — Download filtered views for import into other tools

Zero dependencies — single HTML file that works in any browser.

## Integration

Works best with the **Brand Knowledge Center** plugin. Brand context enables:
- Smarter lead type suggestions based on your business model
- Outreach messages that match your brand voice
- Channel recommendations aligned to your active platforms
- Positioning-aware messaging that highlights your differentiators

## Tips

- **Start with Brand Knowledge Center** for better targeting and outreach messaging
- **Review leads in batches** — confirm each lead type before moving to the next
- **Use the dashboard daily** — open the HTML file to track follow-ups and pipeline status
- **Run `/update-leads` weekly** to mark status changes and discover net-new leads
- **Net-new leads are deduplicated** — the plugin checks against your existing list before adding
- **Export CSV to your CRM** — the CSV format is compatible with HubSpot, Salesforce, Zoho, and most CRM import tools
