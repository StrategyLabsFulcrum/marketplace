# Build Lead List

Research and generate a targeted lead list from scratch. Uses web search to find real leads matching your brand, industry, lead types, and geographic criteria.

## Before Starting

1. Check if a `lead-lists/` directory exists in the user's working folder.
   - If it exists, list existing lead lists and ask: "You have existing lists. Want to create a new list, or use `/update-leads` to expand an existing one?"
2. Check if a `brand-knowledge-center/` directory exists for brand context.
3. Create `lead-lists/` directory if it doesn't exist.

---

## Step 1: Brand Context

### If `brand-knowledge-center/` exists:

Read the following files:
- `business-overview.md` — Industry, products, revenue, team
- `audience-messaging.md` — Audience segments, messaging
- `digital-ecosystem.md` — Active channels and tools
- `competitive-landscape.md` — Competitors
- `brand-identity.md` — Positioning, point of difference

Summarize:
> "I found your Brand Knowledge Center. Here's what I'll use for lead research:
> - **Brand:** [name]
> - **Industry:** [industry]
> - **Products/Services:** [summary]
> - **Active Channels:** [list]
> - **Key Differentiator:** [point of difference]
>
> This helps me find leads that are the right fit and tailor outreach to your positioning."

### If NO brand knowledge exists:

Ask:
1. "What does your business do?" (products/services)
2. "Who is your ideal customer or partner?"
3. "What's your value proposition in one sentence?"
4. "What channels do you use for sales/outreach?"

---

## Step 2: Tool Connections

Run the tool connections audit. This can also be done separately with `/connect-tools`.

### Auto-Detect

If `digital-ecosystem.md` was loaded in Step 1, present detected tools:

> "Based on your Brand Knowledge Center, I see you're using:
> - **CRM:** [detected]
> - **Email/SMS:** [detected]
> - **Advertising:** [detected]
> - **Social:** [detected]
>
> I'll configure these for lead management. You can adjust anytime with `/connect-tools`."

### Quick Setup

For each detected tool, auto-configure with default mappings. Ask about tools not detected:
- "What calendar do you use?" (Google Calendar, Outlook, Apple Calendar)
- "Do you have LinkedIn for outreach?" (URL)

### Channel Routing

Based on detected tools and lead types (once selected in Step 3), configure outreach channel routing:

| Lead Type | Primary | Secondary | Fallback |
|-----------|---------|-----------|----------|
| [auto-suggested based on lead type] | | | |

### Save Config

Save connections to `lead-lists/.config/connections.md` and create export directories.

> "Tools connected. Your dashboard will include action buttons for: [list connected tools]. Outreach drafts will be formatted for your preferred channels."

---

## Step 3: Lead Types

Based on brand context, suggest lead type categories. Tailor suggestions to the brand's business model.

**Present as a checklist:**

> "Based on your brand, here are lead types I'd suggest researching:
>
> 1. **Retail/Wholesale Buyers** — Stores and shops that could carry your products
> 2. **Influencers/Creators** — Social media creators for partnerships and content
> 3. **Media/Press** — Journalists and bloggers for brand coverage
> 4. **Partnership Leads** — Complementary brands for co-marketing or collaboration
> 5. **Event/Pop-up Organizers** — Markets, festivals, and venues for in-person sales
>
> Which of these do you want to include? Or describe other types of leads you're looking for."

For each selected lead type, ask for specifics:
- **Titles/roles** to target: "Any specific job titles? Or should I cast a wide net?"
- **Company types**: "Any preference on company size, type, or industry?"
- **Quantity goal**: "How many leads per type are you aiming for? (e.g., 20 retail buyers, 15 influencers)"

---

## Step 4: Geographic Rules

Ask the user to define their target geography:

> "Where should I look for leads?"
>
> - **Local** — Specific city or metro area (e.g., Portland, OR)
> - **Regional** — Multi-city or state (e.g., Pacific Northwest — WA, OR)
> - **National** — Entire US
> - **International** — Specific countries
> - **Custom** — Zip code radius, specific cities, include/exclude regions

For each option, gather specifics:
- **Local**: "Which city or metro area?"
- **Regional**: "Which states or regions?" Suggest based on brand context.
- **National**: "Any states or regions to prioritize or exclude?"
- **Custom**: "List the specific areas and any exclusions."

---

## Step 5: Additional Filters

Ask optional qualifying questions:

1. "Any minimum company size?" (solo, 1-10, 10-50, 50-200, 200+)
2. "Any industry focus or exclusions?" (e.g., only outdoor/lifestyle retailers, no big box)
3. "Revenue range?" (if targeting businesses)
4. "Any platforms they should be on?" (e.g., must have Instagram, must be on Shopify)
5. "Any other criteria?" (e.g., recently opened, actively posting, carries competitor brands)

---

## Step 6: Research

Execute web research based on all criteria gathered. For each lead type:

### Research Process

1. **Build search queries** — Construct targeted search queries combining lead type, titles, geography, and filters
2. **Search multiple sources** — Google, LinkedIn (public profiles), Google Maps, Instagram, industry directories, trade associations, press databases
3. **Extract lead data** — For each lead found, extract: Name, Title, Company, Location, Contact info (if public), Source URL
4. **Cross-reference** — Fill gaps by checking multiple sources per lead (find company on Google Maps → find the owner on LinkedIn → find their email on the company website)
5. **Score relevance** — Rate each lead 1-5 based on fit criteria
6. **Suggest outreach channel** — Based on lead type and available contact info
7. **Deduplicate** — Check for duplicate entries before adding

### Progress Updates

Report progress as research happens:

> "Researching Retail/Wholesale Buyers in Pacific Northwest..."
> "Found 8 leads so far. Continuing search..."

> "Researching Influencers/Creators..."
> "Found 12 creators with PNW-focused content. Verifying profiles..."

### Batch Presentation

After researching each lead type, present the batch for review before moving to the next:

> "**Retail/Wholesale Buyers — 18 leads found:**
>
> | # | Name | Title | Company | Location | Relevance |
> |---|------|-------|---------|----------|-----------|
> | 1 | Sarah Chen | Buyer | Mountain Outfitters | Portland, OR | ⭐⭐⭐⭐⭐ |
> | 2 | Mike Torres | Owner | Cascadia Goods | Seattle, WA | ⭐⭐⭐⭐ |
> | ... | | | | | |
>
> Want to keep all 18, remove any, or add notes before I move to the next lead type?"

---

## Step 7: Outreach Planning

After all leads are researched and confirmed, for each lead:

1. **Suggest the best outreach channel** based on lead type and available contact info
2. **Draft a personalized outreach message** using brand voice from brand knowledge
3. **Suggest follow-up cadence** per the SKILL.md follow-up sequence

Present a summary:

> "**Outreach Plan:**
> - 18 Retail Buyers → Email (primary), Phone (secondary)
> - 15 Influencers → Instagram DM (primary), Email (secondary)
> - 8 Media contacts → Email (primary), Twitter DM (secondary)
>
> Want me to draft outreach messages now, or save that for `/lead-outreach`?"

If the user wants drafts now, generate 2-3 template variations per lead type (see SKILL.md outreach templates). Personalize with specific references to each lead's business.

---

## Step 8: Generate Files

Create the following files in `lead-lists/`:

### List Name
Ask the user for a list name, or suggest one based on context:
- `pnw-retail-buyers-march-2026`
- `influencer-outreach-q1-2026`
- `[brand]-lead-list-[date]`

### Files Created

1. **`lead-lists/[list-name].csv`** — Full structured data with all schema fields
2. **`lead-lists/[list-name].md`** — Human-readable version organized by lead type with full details
3. **`lead-lists/[list-name]-outreach.md`** — Outreach templates and follow-up cadence per lead type (if outreach was drafted)

---

## Step 9: Dashboard

Ask the user:
> "Want me to generate an interactive dashboard for this lead list? It'll let you filter, search, and track status visually."

If yes, generate `lead-lists/[list-name]-dashboard.html` per the dashboard spec in SKILL.md.

---

## Step 10: Discovery Setup

Configure automated lead discovery for ongoing list growth:

> "Want to set up automated lead discovery? This will search for new leads on a recurring basis."

If yes, run the discovery setup from `/lead-discovery`:
- Set frequency (weekly recommended)
- Configure discovery sources
- Initialize discovery log

> "Discovery configured. I'll search for net-new leads [weekly/bi-weekly/monthly].
> Run `/lead-discovery` anytime to search manually, or `/daily-alerts` will remind you when discovery is due."

---

## Step 11: Completion

Present the final summary:

```
Lead List Complete!

📋 [list-name]
├── 41 total leads across 3 types
├── Retail/Wholesale Buyers: 18 leads
├── Influencers/Creators: 15 leads
├── Media/Press: 8 leads
├── Geography: Pacific Northwest (WA, OR)
├── Relevance: 8 Hot, 14 Strong, 12 Good, 5 Warm, 2 Long Shot

Files generated:
├── lead-lists/[list-name].csv
├── lead-lists/[list-name].md
├── lead-lists/[list-name]-outreach.md
└── lead-lists/[list-name]-dashboard.html

Next steps:
- Review leads and adjust relevance scores if needed
- Run /lead-outreach to draft personalized messages
- Run /daily-alerts each morning for your action plan
- Run /weekly-review every Monday for pipeline performance
- Run /lead-discovery to find new leads (auto-runs per your schedule)
- Run /monthly-report for conversion metrics and strategy
- Open the dashboard HTML to filter and search interactively
- Import the CRM export into [CRM name]
- Run /connect-tools to modify integrations anytime
```
