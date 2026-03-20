---
name: brand-knowledge
description: >
  Brand Knowledge Center — builds and manages a comprehensive brand profile for business owners.
  Use when the user mentions "brand setup", "brand knowledge", "brand profile", "brand onboarding",
  "business overview", "brand guidelines", "competitive landscape", "audience messaging",
  "financial snapshot", "digital ecosystem", "update brand", "brand context", or wants to set up
  their brand before using other Strategy Labs plugins. Also triggers when plugins reference
  a brand-knowledge-center/ folder that doesn't exist yet.
version: 1.0.0
---

# Brand Knowledge Center

A framework for building a comprehensive brand and business profile through a guided setup wizard. The output is a structured `brand-knowledge-center/` folder that serves as the foundation context for all Strategy Labs marketplace plugins.

## How It Works

The Brand Knowledge Center collects information across 6 areas, then assembles it into structured markdown files and a system prompt. Information can be gathered through:

- **Website scraping** — Extract business info, social links, and industry signals from the brand's website
- **Document uploads** — Parse brand guidelines, P&Ls, balance sheets, and other documents
- **Guided questions** — Step-by-step interview with smart suggestions and feedback loops

Each area produces one output file. The final step auto-assembles a `system-prompt.md` from all collected data.

## Output Structure

All files are created in a `brand-knowledge-center/` directory within the user's working folder.

```
brand-knowledge-center/
├── business-overview.md        # Area 1: Business foundation
├── financial-snapshot.md       # Area 2: Financial context
├── digital-ecosystem.md        # Area 3: Digital presence & tools
├── brand-identity.md           # Area 4: Brand guidelines & identity
├── audience-messaging.md       # Area 5: Audiences & messaging frameworks
├── competitive-landscape.md    # Area 6: Competitors & positioning
└── system-prompt.md            # Auto-assembled from all files
```

---

## Area 1: Business Overview

**Output file:** `business-overview.md`

### Information to Collect

| Field | Required | How to Gather |
|-------|----------|---------------|
| Brand / Company Name | Yes | Ask directly |
| Website URL | Yes | Ask directly |
| Industry / Category | Yes | Suggest based on website content; ask user to confirm or correct |
| Sub-category / Niche | Recommended | Suggest based on website; refine with user |
| Year Founded | Optional | Ask or extract from website |
| Company Size | Optional | Ask (solo, small team, 10+, 50+, enterprise) |
| Accounting Approach | Yes | Ask: Cash basis or Accrual basis |
| Business Model | Recommended | Suggest based on website (DTC eComm, B2B services, SaaS, local business, etc.) |
| Key Roles | Yes | Ask for names and titles — at minimum CEO/Owner. Prompt for CFO, CMO, COO, Head of Marketing, etc. |
| Mission / Vision | Optional | Extract from website "About" page or ask |
| Elevator Pitch | Recommended | If not available, draft one from collected info and ask for approval |

### File Template

```markdown
# Business Overview

## Company
- **Name:** {{brand_name}}
- **Website:** {{website_url}}
- **Industry:** {{industry}}
- **Sub-category:** {{sub_category}}
- **Year Founded:** {{year_founded}}
- **Company Size:** {{company_size}}
- **Business Model:** {{business_model}}

## Accounting
- **Basis:** {{accounting_basis}} (Cash / Accrual)

## Key Team
| Name | Role | Email |
|------|------|-------|
| {{name}} | {{role}} | {{email}} |

## Mission & Vision
{{mission_vision}}

## Elevator Pitch
{{elevator_pitch}}
```

---

## Area 2: Financial Snapshot

**Output file:** `financial-snapshot.md`

### Information to Collect

| Field | Required | How to Gather |
|-------|----------|---------------|
| Uploaded P&L | Optional | Ask if they have P&L statements to upload (PDF, CSV, image) |
| Uploaded Balance Sheet | Optional | Ask if they have balance sheets to upload |
| Revenue (annual or monthly) | Recommended | Extract from P&L or ask for approximate range |
| Gross Margin | Recommended | Extract from P&L or ask |
| Net Margin | Optional | Extract from P&L |
| YoY Growth | Optional | Extract if multiple periods available |
| Key Expense Categories | Optional | Extract top 3-5 from P&L |
| Cash Position | Optional | Extract from balance sheet |
| Debt / Liabilities | Optional | Extract from balance sheet |
| Financial Goals | Recommended | Ask: revenue targets, margin goals, growth plans |

### Extraction Rules

When documents are uploaded:
1. Read the document and identify the type (P&L, balance sheet, other)
2. Extract key line items: revenue, COGS, gross profit, operating expenses, net income
3. If multiple periods are present, calculate trends (growth rates, margin changes)
4. Summarize findings and present to the user for confirmation
5. Flag any numbers that seem unusual and ask the user to verify
6. **Never store raw financial documents** in the output — only the extracted summary

### File Template

```markdown
# Financial Snapshot

## Overview
- **Accounting Basis:** {{accounting_basis}}
- **Reporting Period:** {{period}}
- **Data Source:** {{source}} (uploaded P&L, uploaded balance sheet, manual entry)

## Key Metrics
| Metric | Value | Period |
|--------|-------|--------|
| Revenue | {{revenue}} | {{period}} |
| Gross Margin | {{gross_margin}}% | {{period}} |
| Net Margin | {{net_margin}}% | {{period}} |
| YoY Growth | {{yoy_growth}}% | {{period}} |

## Expense Breakdown
| Category | Amount | % of Revenue |
|----------|--------|-------------|
| {{category}} | {{amount}} | {{pct}} |

## Balance Sheet Highlights
- **Cash Position:** {{cash}}
- **Total Assets:** {{assets}}
- **Total Liabilities:** {{liabilities}}
- **Equity:** {{equity}}

## Financial Goals
{{financial_goals}}

## Notes
{{notes}}
```

### If No Financial Documents Available

Skip extraction. Ask:
- Approximate annual revenue range (under $500K, $500K-$1M, $1M-$5M, $5M-$10M, $10M+)
- Primary revenue source
- Any financial goals they'd like to share
- Mark the file as "manual entry — limited data" so other plugins know the depth available

---

## Area 3: Digital Ecosystem

**Output file:** `digital-ecosystem.md`

### Information to Collect

| Field | Required | How to Gather |
|-------|----------|---------------|
| Website Platform | Yes | Ask (Shopify, WordPress, Wix, Squarespace, custom, etc.) or detect from website |
| Social Media URLs | Yes | Scrape from website footer/header/links, then confirm with user. Ask for any missing. |
| Email / SMS Platform | Recommended | Ask (Klaviyo, Mailchimp, Attentive, Postscript, etc.) |
| CRM | Recommended | Ask (HubSpot, Salesforce, Zoho, none, etc.) |
| Analytics | Recommended | Ask (GA4, Mixpanel, etc.) |
| Advertising Platforms | Recommended | Ask (Meta Ads, Google Ads, TikTok, etc.) |
| Review Platforms | Optional | Ask (Google Business, Yelp, Trustpilot, etc.) |
| Other Tools | Optional | Ask for any other key tools in their stack |
| Social Posting Cadence | Optional | Ask how often they post per platform |

### Website Scraping for Social Links

When the website URL is provided:
1. Fetch the homepage
2. Look for social media links in footer, header, and sidebar (Facebook, Instagram, X/Twitter, LinkedIn, TikTok, YouTube, Pinterest)
3. Present found links to the user for confirmation
4. Ask if any platforms are missing
5. For each confirmed platform, note whether it's active (posting regularly) or dormant

### File Template

```markdown
# Digital Ecosystem

## Website
- **URL:** {{website_url}}
- **Platform:** {{website_platform}}

## Social Media
| Platform | URL | Status | Posting Cadence |
|----------|-----|--------|-----------------|
| {{platform}} | {{url}} | {{active/dormant}} | {{cadence}} |

## Marketing & Communication
- **Email / SMS Platform:** {{email_sms_platform}}
- **CRM:** {{crm}}
- **Advertising Platforms:** {{ad_platforms}}

## Analytics & Tracking
- **Analytics:** {{analytics}}
- **Other Tracking:** {{other_tracking}}

## Reviews
- **Review Platforms:** {{review_platforms}}

## Other Tools
{{other_tools}}
```

---

## Area 4: Brand Identity

**Output file:** `brand-identity.md`

### Information to Collect

This area has two paths based on whether the brand has existing guidelines.

#### Path A: Brand Guidelines Uploaded

If the user uploads a brand guide (PDF, doc, image):
1. Parse the document and extract:
   - Logo descriptions and usage rules
   - Color palette (primary, secondary, accent — hex codes if available)
   - Typography / fonts (headings, body, accent)
   - Brand pillars / values
   - Tone and voice direction
   - Messaging frameworks
   - Any do's and don'ts
2. Present extracted information for user review and edits
3. Fill gaps using guided questions from Path B

#### Path B: Guided Questions (No Existing Guidelines)

| Field | Required | Approach |
|-------|----------|----------|
| Brand Pillars | Yes | Suggest 3-5 based on website content and industry. Ask user to approve, edit, or replace. Each pillar needs: name, one-line description, how it shows up in practice. |
| Brand Voice / Tone | Yes | Ask: "If your brand were a person, how would they talk?" Offer spectrum options (e.g., Casual ↔ Formal, Playful ↔ Serious, Bold ↔ Understated). |
| NEVER List | Recommended | Suggest common items for their industry. Ask what words, phrases, or tones they want to avoid. |
| ALWAYS List | Recommended | Ask what should always be true about their content. |
| Color Palette | Optional | Ask for primary brand color, secondary, accent. Accept hex codes, color names, or "I don't have this yet." |
| Typography | Optional | Ask for heading font, body font, or "I don't have this yet." |
| Logo Description | Optional | Ask them to describe their logo or upload it. |
| Tagline(s) | Recommended | Ask if they have a tagline. If not, suggest 2-3 based on collected info and ask for feedback. |
| Core Promise | Recommended | What is the one thing the brand promises its customers? Suggest based on website and ask for confirmation. |
| Point of Difference | Recommended | What makes the brand fundamentally different from competitors? |

### Suggestion Engine

When suggesting brand pillars, voice traits, or messaging:
1. Reference the industry identified in Area 1
2. Reference the website content scraped in Area 1
3. Reference competitor positioning from Area 6 (if already completed)
4. Offer 3-5 options for each, clearly labeled as suggestions
5. Always ask: "Do these feel right? Edit any that don't fit, or tell me what's missing."

### File Template

```markdown
# Brand Identity

## Source
- **Guidelines Document:** {{uploaded / built from scratch}}

## Core Positioning
- **Core Promise:** {{core_promise}}
- **Point of Difference:** {{point_of_difference}}
- **Tagline(s):** {{taglines}}

## Brand Pillars
| Pillar | Description | In Practice |
|--------|-------------|-------------|
| {{pillar_name}} | {{description}} | {{how_it_shows_up}} |

## Voice & Tone
| Trait | Spectrum Position | In Practice |
|-------|-------------------|-------------|
| {{trait}} | {{position}} | {{example}} |

### NEVER List
{{never_list}}

### ALWAYS List
{{always_list}}

## Visual Identity
- **Primary Color:** {{primary_color}}
- **Secondary Color:** {{secondary_color}}
- **Accent Color:** {{accent_color}}
- **Heading Font:** {{heading_font}}
- **Body Font:** {{body_font}}
- **Logo:** {{logo_description}}

## Vocabulary Reference
| Use This | Instead Of |
|----------|-----------|
| {{preferred}} | {{avoided}} |
```

---

## Area 5: Audience & Messaging

**Output file:** `audience-messaging.md`

### Information to Collect

| Field | Required | Approach |
|-------|----------|----------|
| Primary Audience | Yes | Ask who their ideal customer is. Suggest based on website/industry if needed. Focus on mindset and identity, not just demographics. |
| Secondary Audiences | Recommended | Ask if there are other distinct audience segments. |
| Audience Pain Points | Recommended | For each audience, what problems are they trying to solve? |
| Audience Aspirations | Recommended | What does success look like for each audience? |
| Messaging Framework | Yes | Build a framework per audience: headline angle, key benefit, proof point, CTA direction. Suggest and ask for edits. |
| Content Pillars | Recommended | Suggest 3-6 content themes based on brand pillars, audiences, and industry. Each needs: name, purpose, primary emotion, example topics. |
| Key Messages | Recommended | Core phrases, power phrases, segment-specific language. Suggest from website content. |

### Suggestion Approach

For audiences and messaging:
1. Analyze the website for clues about who they serve (product descriptions, testimonials, about page)
2. Cross-reference with the industry from Area 1
3. Propose 1-2 audience profiles with names, descriptions, pain points, and aspirations
4. For each audience, draft a messaging framework
5. Present everything and ask: "Does this match how you think about your customers? What would you change?"

### File Template

```markdown
# Audience & Messaging

## Primary Audience
- **Name:** {{audience_name}} (e.g., "The Performance Junkie")
- **Who They Are:** {{description}}
- **Pain Points:** {{pain_points}}
- **Aspirations:** {{aspirations}}
- **Where They Are:** {{channels_and_platforms}}

## Secondary Audiences
| Audience | Description | Key Difference |
|----------|-------------|----------------|
| {{name}} | {{description}} | {{difference}} |

## Messaging Framework

### {{Audience Name}}
- **Headline Angle:** {{angle}}
- **Key Benefit:** {{benefit}}
- **Proof Point:** {{proof}}
- **CTA Direction:** {{cta}}

## Content Pillars
| Pillar | Purpose | Primary Emotion | Example Topics |
|--------|---------|-----------------|----------------|
| {{pillar}} | {{purpose}} | {{emotion}} | {{topics}} |

## Key Messages & Power Phrases
| Message | Best Used For | Platform |
|---------|--------------|----------|
| {{message}} | {{context}} | {{platform}} |
```

---

## Area 6: Competitive Landscape

**Output file:** `competitive-landscape.md`

### Information to Collect

| Field | Required | Approach |
|-------|----------|----------|
| Competitors | Yes | Ask for 3-5 competitors. Also attempt to identify competitors from the industry/website and suggest them for confirmation. |
| Competitor URLs | Yes | For each competitor, get their website URL |
| Competitor Positioning | Recommended | For each competitor, note their apparent positioning, strengths, and weaknesses |
| Brand's Counter-Position | Recommended | For each competitor, how is this brand fundamentally different? |
| Competitor Platforms | Optional | Which social/marketing platforms are competitors active on? |

### Competitor Identification

When suggesting competitors:
1. Use the industry and sub-category from Area 1
2. Use the website content and product/service descriptions
3. Suggest 3-5 likely competitors with brief reasoning
4. Ask: "Are these your main competitors? Add, remove, or replace any."
5. For confirmed competitors, scrape their website for basic positioning info if URLs are provided

### File Template

```markdown
# Competitive Landscape

## Our Position
- **Industry:** {{industry}}
- **Our Point of Difference:** {{point_of_difference}}

## Competitors

### {{Competitor Name}}
- **Website:** {{url}}
- **Their Positioning:** {{positioning}}
- **Their Strengths:** {{strengths}}
- **Their Weaknesses:** {{weaknesses}}
- **Our Counter-Position:** {{how_we_differ}}
- **Their Platforms:** {{platforms}}

## Competitive Matrix
| Factor | Our Brand | {{Competitor 1}} | {{Competitor 2}} | {{Competitor 3}} |
|--------|-----------|-------------------|-------------------|-------------------|
| Positioning | {{ours}} | {{theirs}} | {{theirs}} | {{theirs}} |
| Primary Audience | {{ours}} | {{theirs}} | {{theirs}} | {{theirs}} |
| Price Point | {{ours}} | {{theirs}} | {{theirs}} | {{theirs}} |
| Key Strength | {{ours}} | {{theirs}} | {{theirs}} | {{theirs}} |
```

---

## System Prompt Assembly

**Output file:** `system-prompt.md`

After all areas are complete, auto-assemble a system prompt that any AI tool or plugin can use as foundational brand context.

### Assembly Rules

1. Read all 6 knowledge files
2. Build the system prompt in this order:
   - Brand identity and core positioning (from `brand-identity.md`)
   - Business context (from `business-overview.md`)
   - Audience and messaging (from `audience-messaging.md`)
   - Voice and tone rules (from `brand-identity.md`)
   - Competitive context (from `competitive-landscape.md`)
   - Digital ecosystem context (from `digital-ecosystem.md`)
   - Financial context summary — only high-level (from `financial-snapshot.md`)
3. The system prompt should be written as instructions to an AI assistant
4. Include the NEVER and ALWAYS lists verbatim
5. Include the vocabulary reference
6. Keep it under 3000 words — prioritize actionable rules over descriptive context

### File Template

```markdown
# System Prompt — {{Brand Name}}

> Auto-generated from Brand Knowledge Center files. Last updated: {{date}}

You are an AI assistant working for {{brand_name}}. Use the following brand context to inform all work.

## Brand Identity
{{assembled_from_brand_identity}}

## Business Context
{{assembled_from_business_overview}}

## Our Audiences
{{assembled_from_audience_messaging}}

## Voice & Tone Rules
{{assembled_from_brand_identity_voice_section}}

## Competitive Awareness
{{assembled_from_competitive_landscape}}

## Digital Ecosystem
{{assembled_from_digital_ecosystem}}

## Financial Context
{{high_level_summary_from_financial_snapshot}}

## Rules
### NEVER
{{never_list}}

### ALWAYS
{{always_list}}

### Vocabulary
{{vocabulary_reference}}
```

---

## Reading Brand Knowledge (For Other Plugins)

Any Strategy Labs plugin that needs brand context should:

1. Check if `brand-knowledge-center/` exists in the working directory
2. If it exists, read `system-prompt.md` first (contains the assembled context)
3. Read individual files as needed for deeper context
4. If the folder doesn't exist, inform the user: "This plugin works best with brand context. Run `/brand-setup` from the Brand Knowledge Center plugin to create your brand profile."

### Priority Loading Order

1. `system-prompt.md` — Always load first
2. `brand-identity.md` — Voice and positioning
3. `audience-messaging.md` — Who the brand talks to
4. `business-overview.md` — Business fundamentals
5. `competitive-landscape.md` — Market context
6. `digital-ecosystem.md` — Platform details
7. `financial-snapshot.md` — Only when financial context is needed
