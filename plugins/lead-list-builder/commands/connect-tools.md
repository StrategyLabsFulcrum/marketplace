# Connect Tools

Configure integrations with CRM, email, calendar, social, and advertising tools for seamless lead management. Auto-detects existing tools from Brand Knowledge Center.

## Before Starting

1. Check for `brand-knowledge-center/digital-ecosystem.md` — auto-detect existing tools.
2. Check for existing connections config at `lead-lists/.config/connections.md`.
   - If it exists: Show current connections and offer to modify.
   - If not: Run full setup.

---

## Step 1: Auto-Detect Existing Tools

If `digital-ecosystem.md` exists, read and summarize:

```
DETECTED TOOLS (from Brand Knowledge Center):

| Tool | Category | Status |
|------|----------|--------|
| House Call Pro | CRM | Detected ✓ |
| House Call Pro | Phone/SMS | Detected ✓ |
| Klaviyo | Email | Detected ✓ |
| Google Ads | Advertising | Detected ✓ |
| Meta Ads | Advertising | Detected ✓ |
| Instagram | Social | Detected ✓ |
| Facebook | Social | Detected ✓ |
| QuickBooks | Accounting | Detected ✓ |

NOT DETECTED (ask user):
| Calendar | ? |
| LinkedIn | ? |
```

Ask about missing tools:
> "What calendar do you use? (Google Calendar, Outlook, Apple Calendar, other)"
> "Do you have a LinkedIn profile or company page for outreach?"

---

## Step 2: Connection Recommendations

Present tiered recommendations based on what's detected:

```
RECOMMENDED CONNECTIONS:

MUST HAVE — Set up now:
├── 📋 CRM: House Call Pro
│   Type: Template-based (CSV export matching HCP import format)
│   What it does: Auto-generates CRM-ready import file on every list update
│   Setup: Map your lead fields to HCP customer fields
│
├── 📧 Email: Gmail / Klaviyo
│   Type: Manual + Template
│   What it does: Outreach drafts formatted as ready-to-send emails,
│   follow-up sequences for Klaviyo if batch emailing
│   Setup: Confirm which email you send outreach from
│
└── 📅 Calendar: [User's choice]
    Type: .ics file generation
    What it does: Creates calendar events with prep notes when leads respond
    Setup: Confirm calendar app (Google Calendar, Outlook, Apple)

HIGH VALUE — Set up if you want deeper integration:
├── 💼 LinkedIn
│   Type: Manual tracking
│   What it does: Stores profile URLs, formats outreach as LinkedIn messages,
│   tracks connection status
│   Setup: Provide your LinkedIn profile URL
│
├── 📘 Facebook
│   Type: Manual tracking
│   What it does: Stores page URLs, suggests engagement actions
│   (follow, comment, message), tracks interactions
│   Setup: Provide your Facebook business page URL
│
└── 📱 Phone/SMS: House Call Pro
    Type: Manual tracking
    What it does: Click-to-call from dashboard, phone scripts per lead type,
    SMS templates, call outcome logging
    Setup: Already detected via HCP

NICE TO HAVE — Set up later:
├── 📊 Meta Ads
│   Type: Template-based
│   What it does: Export lead email list for Custom Audiences,
│   build lookalike audiences from converted leads
│   Setup: Link to Meta Business Manager
│
├── 🔍 Google Ads
│   Type: Manual tracking
│   What it does: Tag leads sourced from Google Ads,
│   track which keywords drive best leads
│   Setup: UTM parameter tracking on landing pages
│
└── 💰 QuickBooks
    Type: Manual tracking
    What it does: Log job values from converted leads,
    calculate ROI per lead type in monthly/quarterly reports
    Setup: Already detected. Just log revenue when jobs come in.

Which would you like to set up? [All must-have / All / Select specific]
```

---

## Step 3: CRM Field Mapping

For the selected CRM, walk through field mapping:

### House Call Pro

```
CRM FIELD MAPPING — House Call Pro

I'll map your lead data to HCP's customer import format:

| Lead List Field | → | HCP Field | Notes |
|----------------|---|-----------|-------|
| name | → | Customer Name | Direct map |
| email | → | Email | Direct map |
| phone | → | Phone | Direct map |
| company | → | Company | Direct map |
| location | → | Address | City, State only (no street for leads) |
| lead_type | → | Tag | "Lead Type: Estate Attorney" |
| outreach_status | → | Tag | "Status: Responded" |
| relevance_score | → | Tag | "Relevance: 5-star" |
| notes | → | Customer Notes | Full outreach history |
| suggested_channel | → | — | Not mapped (internal use) |
| tags | → | Tags | Comma-separated |

Does this mapping look right? [Yes / Edit]
```

### HubSpot

```
| Lead List Field | → | HubSpot Field |
|----------------|---|---------------|
| name (split) | → | First Name, Last Name |
| email | → | Email |
| phone | → | Phone Number |
| company | → | Company |
| title | → | Job Title |
| outreach_status | → | Lead Status |
| lead_type | → | Industry / Custom Property |
| notes | → | Notes |
| website | → | Website URL |
| linkedin | → | LinkedIn URL (custom) |
```

### Salesforce

```
| Lead List Field | → | Salesforce Field |
|----------------|---|-----------------|
| name (split) | → | First Name, Last Name |
| email | → | Email |
| phone | → | Phone |
| company | → | Company |
| title | → | Title |
| outreach_status | → | Status |
| source | → | Lead Source |
| notes | → | Description |
```

---

## Step 4: Outreach Channel Routing

Based on connected tools and lead types, configure which channel to use first:

```
OUTREACH CHANNEL ROUTING:

Based on your tools and lead types, here's the recommended routing:

| Lead Type | Primary | Secondary | Fallback |
|-----------|---------|-----------|----------|
| Estate/Probate Attorneys | Email (Gmail) | Phone (HCP) | LinkedIn |
| Insurance/Restoration | Phone (HCP) | Email (Gmail) | Drop-in visit |

Does this routing look right? [Yes / Edit]
```

The routing determines:
- Which outreach draft format is generated first in `/lead-outreach`
- Which channel is suggested in daily alerts
- Which action buttons appear first in the dashboard

---

## Step 5: Generate Config

Save all settings to `lead-lists/.config/connections.md`:

```markdown
# Lead List — Tool Connections

## Connected Tools
| Tool | Category | Type | Status | Details |
|------|----------|------|--------|---------|
| House Call Pro | CRM | Template | Active | CSV export at lead-lists/.exports/hcp-import.csv |
| Gmail | Email | Manual | Active | Outreach drafts formatted as email |
| Google Calendar | Calendar | .ics export | Active | Events generated on lead response |
| LinkedIn | Social | Manual | Active | Profile: [URL] |
| Facebook | Social | Manual | Active | Page: [URL] |
| House Call Pro | Phone/SMS | Manual | Active | Click-to-call, SMS templates |
| Meta Ads | Advertising | Template | Active | Custom Audience export |
| QuickBooks | Accounting | Manual | Active | Revenue tracking on converted leads |

## CRM Field Mapping
[mapping table]

## Outreach Channel Routing
[routing table]

## Export Paths
- CRM import: lead-lists/.exports/hcp-import.csv
- Meta Audiences: lead-lists/.exports/meta-audience.csv
- Calendar events: lead-lists/.exports/events/

## Auto-Export Triggers
- CRM CSV regenerated on: /update-leads, /lead-discovery
- Meta Audience regenerated on: monthly (manual trigger)
- Calendar events generated on: lead status → responded
```

Also create the export directories:

```
lead-lists/
├── .config/
│   ├── connections.md
│   ├── discovery-settings.md
│   └── discovery-log.md
├── .exports/
│   ├── hcp-import.csv
│   ├── meta-audience.csv
│   └── events/
├── reports/
│   ├── weekly-[date].md
│   └── monthly-[month]-[year].md
```

---

## Step 6: Completion

```
Tool Connections Configured!

🔗 Connected:
├── CRM: House Call Pro (CSV auto-export)
├── Email: Gmail (outreach draft formatting)
├── Calendar: Google Calendar (.ics generation)
├── LinkedIn: Manual tracking + outreach drafts
├── Facebook: Manual tracking + engagement suggestions
├── Phone/SMS: House Call Pro (click-to-call + templates)
├── Meta Ads: Custom Audience export
├── QuickBooks: Revenue tracking on conversions

Dashboard updated with action buttons:
[📧 Email] [📞 Call] [in LinkedIn] [fb Facebook] [📅 Schedule] [💬 SMS]

These connections are active across all commands:
├── /build-lead-list — CRM import generated with initial list
├── /lead-outreach — Drafts formatted per connected channel
├── /update-leads — CRM export auto-refreshed on changes
├── /daily-alerts — Action buttons use connected tools
├── /lead-dashboard — Click-to-action links for all tools

Modify anytime with /connect-tools
```

---

## Modify Existing Connections

If connections already exist, show current state and offer modifications:

```
/connect-tools

CURRENT CONNECTIONS:
[table of connected tools]

What would you like to do?
1. Add a new tool connection
2. Edit CRM field mapping
3. Change outreach channel routing
4. Remove a connection
5. Regenerate all export files
6. Test connections (verify export files are current)
```
