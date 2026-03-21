---
name: brand-intelligence
description: >
  Brand Intelligence Center — builds and manages a comprehensive brand profile for any business.
  Use when the user mentions "brand setup", "brand profile", "brand onboarding", "business overview",
  "brand guidelines", "competitive landscape", "audience messaging", "customer psychology",
  "brand voice", "differentiation", "proof points", "set up my brand", "update brand",
  "brand context", or wants to set up their brand before using other Strategy Labs or marketing skills.
  Also triggers when any plugin references a brand-intelligence-center/ folder that doesn't exist yet.
version: 1.0.0
---

# Brand Intelligence Center

A guided setup wizard that builds a complete brand and business profile in 8 areas. Combines operational brand depth (business foundation, financials, digital ecosystem, visual identity) with conversion intelligence (customer psychology, JTBD, objections, switching dynamics, proof points).

Works for both **single-brand founders** (one brand, simple setup) and **agencies** (multiple brands, instant switching). The experience adapts to who's using it.

The output is a structured `brand-intelligence-center/` folder that serves as the shared context for all Strategy Labs marketplace plugins and all marketing skills.

---

## Multi-Brand Architecture

### Folder Structure

**Single brand** (founder mode — simple, no switching needed):
```
brand-intelligence-center/
├── business.md
├── customer.md
├── differentiation.md
├── voice-identity.md
├── proof-goals.md
├── digital-ecosystem.md
├── financial.md
└── system-prompt.md          ← always the active brand context
```

**Multiple brands** (agency mode — full brand roster):
```
brand-intelligence-center/
├── .active-brand              ← plain text file: name of the active brand slug
├── system-prompt.md           ← always a copy of the active brand's system-prompt.md
└── brands/
    ├── uno-mas/
    │   ├── business.md
    │   ├── customer.md
    │   ├── differentiation.md
    │   ├── voice-identity.md
    │   ├── proof-goals.md
    │   ├── digital-ecosystem.md
    │   ├── financial.md
    │   └── system-prompt.md
    └── [brand-slug]/
        └── ...
```

### The Golden Rule for All Skills

Every skill always reads from `brand-intelligence-center/system-prompt.md` at the root — never from inside `brands/`. The root `system-prompt.md` is always kept in sync with the active brand. Skills never need to know whether they're in founder or agency mode.

### Brand Slugs

Brand names are stored as lowercase slugs with hyphens: `uno-mas`, `taco-bell`, `jones-hardware`. The slug is derived automatically from the business name. Show the user the slug and confirm before creating.

### Mode Detection

On first run, check the folder structure to determine mode:
- No `brands/` subfolder → founder mode
- `brands/` subfolder exists → agency mode

When adding a second brand to a founder-mode setup, offer to convert:
> "You already have [Brand Name] set up. Adding another brand will switch to agency mode, which organizes each brand in its own folder and lets you switch between them with `/brand-switch`. Your existing brand data won't be lost — it'll be moved to `brands/[slug]/` automatically. Ready to proceed?"

---

## Core Principle: Scrape First, Ask Second

Before asking a single question:
1. Ask for the business website URL (if not already known)
2. Scrape the homepage, about page, menu/services page, and footer
3. Draft answers for every section you can from what you find
4. Present each section as pre-filled — the user confirms, edits, or replaces
5. Only ask open questions for what you couldn't find

**Never present a blank form. Always come with a draft.**

---

## Output Structure

All files are created in a `brand-intelligence-center/` directory within the user's working folder.

```
brand-intelligence-center/
├── business.md           # Area 1: Business foundation
├── customer.md           # Area 2: Customer profile & psychology
├── differentiation.md    # Area 3: Competitive position & differentiation
├── voice-identity.md     # Area 4: Brand voice, tone & visual identity
├── proof-goals.md        # Area 5: Proof points & conversion goals
├── digital-ecosystem.md  # Area 6: Platforms, tools & channels
├── financial.md          # Area 7: Financial context (optional)
└── system-prompt.md      # Auto-assembled master context for all skills
```

---

## Setup Wizard

### Before Starting

**Step 1 — Check existing state:**

Check if `brand-intelligence-center/` exists.

| State | Action |
|-------|--------|
| Folder doesn't exist | New setup — ask mode question (see below) |
| Folder exists, no `brands/` subfolder | Founder mode — read `system-prompt.md`, offer to update or add a new brand |
| Folder exists, `brands/` subfolder present | Agency mode — show brand roster, offer to update active brand, switch brands, or add a new brand |

**Step 2 — If new setup, ask mode:**

> Are you setting this up for one brand, or will you be managing multiple brands (e.g., for an agency or portfolio)?
>
> `[ ]` **Single brand** — simple setup, no switching needed
> `[ ]` **Multiple brands** — I manage more than one brand and want to switch between them easily

Founder mode proceeds directly to the wizard. Agency mode sets up the `brands/` structure before starting.

**Step 3 — Updating an existing brand:**
- Read `system-prompt.md` and summarize what's captured in 3–5 bullet points
- Ask: "Which areas would you like to update?" (show numbered list)
- Only collect information for selected areas
- Re-assemble `system-prompt.md` and sync to root after updates

---

## Area 1: Business Foundation

**Output file:** `business.md`

### Scrape For
From the homepage and about page: business name, location(s), concept description, year founded, team/owner names, tagline, mission statement, business format.

### Fields to Confirm or Collect

| Field | Required | Input Method |
|-------|----------|--------------|
| Business name | Yes | Scraped — confirm |
| Website URL | Yes | Already collected |
| Location(s) | Yes | Scraped — confirm or add |
| Business type | Yes | Choice (see below) |
| Format | Yes | Choice (see below) |
| Year founded | Optional | Scraped or ask |
| Owner / key team | Yes | Ask for names and roles |
| One-liner | Yes | Scraped draft — edit |
| Tagline | Recommended | Scraped or generate options |
| Mission / elevator pitch | Recommended | Scraped or ask |

### Business Type (Present as Choices)

> What type of business is this? Choose the closest fit:
> - `[ ]` Restaurant / Bar / Café
> - `[ ]` Retail store
> - `[ ]` Service business (agency, consultant, professional services)
> - `[ ]` eCommerce / DTC brand
> - `[ ]` SaaS / software
> - `[ ]` Local service (cleaning, landscaping, trades, etc.)
> - `[ ]` Hospitality (hotel, event venue, experience)
> - `[ ]` Other: ___

### Format (Present as Choices — Adapt by Business Type)

For restaurants/hospitality:
> How does the business operate? Select all that apply:
> - `[ ]` Dine-in
> - `[ ]` Counter service / fast casual
> - `[ ]` Takeout / to-go
> - `[ ]` Delivery (own or third-party)
> - `[ ]` Catering
> - `[ ]` Private events / buyouts
> - `[ ]` Food truck / pop-up
> - `[ ]` Ghost kitchen

For retail/eCommerce:
> - `[ ]` Physical storefront
> - `[ ]` Online only
> - `[ ]` Both (omnichannel)
> - `[ ]` Wholesale / B2B
> - `[ ]` Subscription

### File Template

```markdown
# Business Foundation

## Identity
- **Name:** {{business_name}}
- **Website:** {{website_url}}
- **Location(s):** {{locations}}
- **Business Type:** {{business_type}}
- **Format:** {{format}}
- **Year Founded:** {{year_founded}}

## Team
| Name | Role |
|------|------|
| {{name}} | {{role}} |

## Positioning
- **One-liner:** {{one_liner}}
- **Tagline:** {{tagline}}
- **Mission / Elevator Pitch:** {{mission}}
```

---

## Area 2: Your Customer

**Output file:** `customer.md`

This area captures who your customer is, why they choose you, and the psychological forces behind that decision.

### Scrape For
From testimonials, reviews (Google, Yelp, etc.), about page, and any "who we serve" language: customer descriptions, occasions mentioned, language used.

### Sub-section A: Customer Profile

| Field | Required | Input Method |
|-------|----------|--------------|
| Primary customer | Yes | Scraped draft — confirm |
| Secondary audiences | Recommended | Suggest from context |
| Occasions / scenarios | Yes | Choice list (see below) |
| Decision-maker | Yes | Choice (see below) |
| Jobs to be done (JTBD) | Yes | Suggest 3 — confirm |

### Occasions (Present as Choices — Adapt by Business Type)

For restaurants:
> When do people typically come to you? Select all that apply:
> - `[ ]` Casual weeknight dinner
> - `[ ]` Weekend outing
> - `[ ]` Date night
> - `[ ]` Family meal / celebration
> - `[ ]` Business lunch
> - `[ ]` Happy hour / drinks
> - `[ ]` Special occasion (birthday, anniversary)
> - `[ ]` Quick lunch / takeout
> - `[ ]` Late night
> - `[ ]` Catering / private event
> - `[ ]` Neighborhood regular / habit

### Decision-Maker (Present as Choices)

> Who typically decides to come here? Select all that apply:
> - `[ ]` Individual deciding for themselves
> - `[ ]` One person deciding for a couple
> - `[ ]` Group deciding together
> - `[ ]` One person organizing a group
> - `[ ]` Corporate / event planner

### Jobs to Be Done (JTBD)

Present 3–5 suggested JTBD statements based on the business type and scrape, then ask the user to confirm, edit, or replace. Format:

> When a customer comes to you, what are they really "hiring" you to do?
> Here are my best guesses based on what I found — edit anything that doesn't fit:
>
> 1. "Help me have a good time without having to think too hard about where to go"
> 2. "Give me a reliable spot I can bring people to and look good"
> 3. "Feed me something that actually tastes like it was made with care"
>
> → Add any I missed. Remove any that don't apply.

### Sub-section B: Switching Dynamics (JTBD Four Forces)

Capture the psychological forces that bring customers to you and keep them (or don't).

| Force | What to Capture |
|-------|----------------|
| **Push** | What frustrates them about alternatives (cooking at home, other restaurants, delivery apps) |
| **Pull** | What attracted them to you specifically |
| **Habit** | What keeps people stuck with their current default (e.g., always ordering the same delivery spot) |
| **Anxiety** | What might make them hesitant to try you or come back |

Present as guided prompts, not blank fields:

> Let's understand why customers switch TO you — and what holds them back.
>
> **What frustrates people about their current options?**
> (e.g., "delivery food that tastes like the container," "chain restaurants with no soul," "can't find good Mexican food that isn't Tex-Mex")
>
> **What do they say when they recommend you?**
> (Think of the last time someone told a friend about you — what did they say?)
>
> **What's their default if they don't come to you?**
> (e.g., cooking at home, a specific competitor, ordering DoorDash)
>
> **What might make someone hesitant to try you or return?**
> (e.g., parking, price perception, not knowing the menu, wait times)

### File Template

```markdown
# Customer Profile

## Who They Are
- **Primary Customer:** {{primary_customer}}
- **Secondary Audiences:** {{secondary_audiences}}
- **Decision-Maker:** {{decision_maker}}

## When They Come
**Primary occasions:**
{{occasions}}

## Jobs to Be Done
When a customer chooses us, they're really hiring us to:
1. {{jtbd_1}}
2. {{jtbd_2}}
3. {{jtbd_3}}

## Switching Dynamics
- **Push** (frustrations with alternatives): {{push}}
- **Pull** (what attracts them to us): {{pull}}
- **Habit** (their current default): {{habit}}
- **Anxiety** (what holds them back): {{anxiety}}

## Customer Language
**How they describe us (verbatim):**
- "{{quote_1}}"
- "{{quote_2}}"

**Words/phrases to use:** {{use_these}}
**Words/phrases to avoid:** {{avoid_these}}
```

---

## Area 3: Differentiation & Competitive Position

**Output file:** `differentiation.md`

### Scrape For
From the about page, homepage hero, and any "why us" language: differentiators, competitor mentions, positioning claims.

### Competitor Identification

Suggest competitors based on business type, location, and scraped context:

> Based on what I found, here are your likely competitors:
> **Direct** (same concept, same audience):
> - [Scraped or inferred list]
>
> **Indirect** (different approach, same customer need):
> - Cooking at home
> - Delivery apps (DoorDash, Uber Eats)
> - [Other local options]
>
> → Remove any that don't apply. Add any I missed.

For each confirmed competitor, capture:
- Their apparent positioning
- Their key strength
- Where they fall short
- Your counter-position

### Objections & Anti-Persona

> What are the top reasons someone might NOT choose you — even if they're the right customer?
>
> Common objections for your type of business:
> - `[ ]` Price — "seems expensive"
> - `[ ]` Location / parking
> - `[ ]` Wait times
> - `[ ]` Not sure what to order / unfamiliar menu
> - `[ ]` Dietary restrictions / limited options
> - `[ ]` Didn't know about you
> - `[ ]` Bad past experience
> - Other: ___
>
> For each selected, we'll capture how you address it.

> **Anti-persona** — Who is NOT a good fit for you?
> (e.g., "someone looking for the cheapest meal possible," "someone who wants a chain experience")

### File Template

```markdown
# Differentiation & Competitive Position

## Our Position
- **How we're different:** {{key_differentiator}}
- **Why that matters:** {{why_it_matters}}
- **Why customers choose us over alternatives:** {{why_us}}

## Competitors

### Direct
| Competitor | Their Strength | Where They Fall Short | Our Counter-Position |
|------------|---------------|----------------------|----------------------|
| {{name}} | {{strength}} | {{weakness}} | {{counter}} |

### Indirect
| Alternative | Why Customers Default To It | Why We're Better |
|-------------|----------------------------|-----------------|
| {{alt}} | {{reason}} | {{advantage}} |

## Objections & Responses
| Objection | How We Address It |
|-----------|------------------|
| {{objection}} | {{response}} |

## Anti-Persona
**Not a good fit:** {{anti_persona}}
```

---

## Area 4: Brand Voice & Identity

**Output file:** `voice-identity.md`

### Scrape For
From website copy, social media, and any uploaded brand guidelines: tone signals, vocabulary, visual identity clues.

### Voice & Tone (Choice-Based)

> What's your brand personality? Select up to 5 that feel true:
>
> **Energy:**
> `[ ]` Warm & welcoming  `[ ]` Bold & confident  `[ ]` Playful & fun
> `[ ]` Calm & reassuring  `[ ]` Energetic & vibrant  `[ ]` Cool & understated
>
> **Register:**
> `[ ]` Casual & conversational  `[ ]` Polished & professional
> `[ ]` Straight-talking & no-BS  `[ ]` Storytelling & evocative
>
> **Identity:**
> `[ ]` Local & community-rooted  `[ ]` Culturally authentic
> `[ ]` Trend-forward  `[ ]` Classic & timeless  `[ ]` Rebellious & opinionated
>
> → Anything that doesn't quite fit? Tell me how you'd describe it instead.

### NEVER / ALWAYS Lists

> Let's define what's always true about your voice — and what's never acceptable.
>
> **ALWAYS (things every piece of content must reflect):**
> I'll suggest a few based on what you've told me — edit or add:
> - Always feel like it came from a real person, not a corporation
> - Always reflect [cultural authenticity / local pride / etc.]
> - [Add from scrape]
>
> **NEVER (words, phrases, tones to avoid):**
> - Never use corporate jargon or buzzwords
> - Never sound apologetic or overly formal
> - [Add from scrape / ask]

### Visual Identity (Optional — Skip if No Guidelines)

| Field | Input |
|-------|-------|
| Primary color | Hex code or color name — or "I don't have this yet" |
| Secondary color | Same |
| Accent color | Same |
| Heading font | Name or "I don't know" |
| Body font | Name or "I don't know" |
| Logo description | Describe or upload |

### File Template

```markdown
# Brand Voice & Identity

## Personality
**We are:** {{personality_adjectives}}

## Voice Traits
| Trait | What It Means In Practice |
|-------|--------------------------|
| {{trait}} | {{in_practice}} |

## ALWAYS
{{always_list}}

## NEVER
{{never_list}}

## Vocabulary
| Use This | Instead Of |
|----------|-----------|
| {{preferred}} | {{avoided}} |

## Visual Identity
- **Primary Color:** {{primary_color}}
- **Secondary Color:** {{secondary_color}}
- **Accent Color:** {{accent_color}}
- **Heading Font:** {{heading_font}}
- **Body Font:** {{body_font}}
- **Logo:** {{logo_description}}
```

---

## Area 5: Proof Points & Goals

**Output file:** `proof-goals.md`

### Scrape For
From homepage, Google/Yelp reviews, press mentions: ratings, review counts, years open, notable accolades, testimonial snippets.

### Proof Points

Present scraped proof first, then ask for anything missing:

> Here's what I found that you can use as proof:
> - [Star rating + review count from Google/Yelp]
> - [Years in business]
> - [Any press or awards found]
>
> → What else should we add?
> - Awards or recognition?
> - A number you're proud of (covers served, events hosted, etc.)?
> - A testimonial or review that captures what you're about?

### Goals (Choice-Based)

> What's the primary thing you want someone to do when they encounter your brand?
> - `[ ]` Walk in and dine
> - `[ ]` Make a reservation
> - `[ ]` Place an online order
> - `[ ]` Inquire about catering / private events
> - `[ ]` Follow on social / join the community
> - `[ ]` Sign up for email/SMS list
> - `[ ]` Purchase (eCommerce)
> - `[ ]` Book a service / consultation

> What's your current biggest business focus?
> - `[ ]` Getting more new customers
> - `[ ]` Getting existing customers to come back more often
> - `[ ]` Growing a specific revenue stream (catering, events, delivery)
> - `[ ]` Building brand awareness in a new area
> - `[ ]` Launching something new
> - Other: ___

### File Template

```markdown
# Proof Points & Goals

## Proof Points
**Ratings & Reviews:** {{ratings}}
**Years in Business:** {{years}}
**Accolades / Press:** {{accolades}}
**Key Metrics:** {{metrics}}

## Testimonials
> "{{quote}}" — {{source}}

## What We're Known For
{{known_for}}

## Conversion Goal
**Primary action we want people to take:** {{primary_cta}}

## Current Business Focus
{{current_focus}}

## Metrics to Reference
{{metrics_to_cite}}
```

---

## Area 6: Digital Ecosystem

**Output file:** `digital-ecosystem.md`

### Scrape For
From website footer, header, and link tags: social media URLs, reservation platform links, delivery platform links, email signup forms.

### Fields to Confirm or Collect

| Field | Required | Input Method |
|-------|----------|--------------|
| Social media profiles | Yes | Scraped — confirm + add missing |
| Reservation platform | Recommended | Choice list |
| Delivery platforms | Recommended | Choice list |
| Email / SMS platform | Recommended | Choice list |
| POS system | Optional | Choice list |
| CRM / loyalty | Optional | Choice list |
| Analytics | Optional | Choice list |
| Posting cadence | Optional | Ask per platform |

### Platform Choices (Present as Lists)

**Reservation platforms:**
`[ ]` OpenTable  `[ ]` Resy  `[ ]` Yelp Reservations  `[ ]` Toast  `[ ]` Own website  `[ ]` Phone only  `[ ]` None

**Delivery platforms:**
`[ ]` DoorDash  `[ ]` Uber Eats  `[ ]` Grubhub  `[ ]` Own delivery  `[ ]` None

**Email / SMS:**
`[ ]` Klaviyo  `[ ]` Mailchimp  `[ ]` Toast Marketing  `[ ]` Attentive  `[ ]` None yet

**POS:**
`[ ]` Toast  `[ ]` Square  `[ ]` Lightspeed  `[ ]` Clover  `[ ]` Other: ___

### File Template

```markdown
# Digital Ecosystem

## Website
- **URL:** {{website_url}}
- **Platform:** {{website_platform}}

## Social Media
| Platform | URL | Status | Posting Cadence |
|----------|-----|--------|-----------------|
| {{platform}} | {{url}} | Active / Dormant | {{cadence}} |

## Reservations
- **Platform:** {{reservation_platform}}
- **Link:** {{reservation_link}}

## Delivery
| Platform | Link | Active |
|----------|------|--------|
| {{platform}} | {{link}} | Yes / No |

## Marketing & Communication
- **Email / SMS:** {{email_sms_platform}}
- **CRM / Loyalty:** {{crm}}
- **Analytics:** {{analytics}}

## POS
- **System:** {{pos_system}}
```

---

## Area 7: Financial Context (Optional)

**Output file:** `financial.md`

This area is optional. Skip it by saying "skip finances" at any point.

### When to Complete
- When financial context will inform marketing decisions (e.g., margin-aware pricing copy, budget allocation)
- When working with brands who want full business intelligence

### Fields

| Field | Required | Source |
|-------|----------|--------|
| Revenue range | Recommended | Ask (range options) |
| Primary revenue streams | Yes | Ask |
| Gross margin range | Optional | P&L upload or ask |
| YoY growth trend | Optional | Ask |
| Financial goals | Recommended | Ask |
| Accounting basis | Optional | Choice: Cash / Accrual |

### Revenue Range (Choice-Based)

> Approximately what is annual revenue?
> - `[ ]` Under $500K
> - `[ ]` $500K – $1M
> - `[ ]` $1M – $3M
> - `[ ]` $3M – $5M
> - `[ ]` $5M – $10M
> - `[ ]` $10M+
> - `[ ]` Prefer not to say

### File Template

```markdown
# Financial Context

*Data source: {{manual entry / uploaded P&L / estimate}}*

## Revenue
- **Annual Range:** {{revenue_range}}
- **Primary Streams:** {{revenue_streams}}
- **Gross Margin:** {{gross_margin}}
- **YoY Trend:** {{growth_trend}}

## Goals
{{financial_goals}}

## Notes
{{notes}}
```

---

## System Prompt Assembly

**Output file:** `system-prompt.md`

After all areas are complete (or skipped), auto-assemble a master context file that any skill can load as its first action.

### Assembly Rules

1. Read all completed area files
2. Build the system prompt in this order:
   - Brand identity and personality (from `voice-identity.md`)
   - Business foundation (from `business.md`)
   - Customer profile and JTBD (from `customer.md`)
   - Differentiation and competitive position (from `differentiation.md`)
   - Proof points and goals (from `proof-goals.md`)
   - Digital ecosystem summary (from `digital-ecosystem.md`)
   - Financial context — high-level only (from `financial.md`, if completed)
3. Write it as instructions to an AI assistant
4. Include NEVER/ALWAYS lists verbatim
5. Include vocabulary reference
6. Include conversion goal prominently
7. Keep under 3000 words — prioritize rules over descriptions
8. Mark any skipped sections as `[Not yet completed — run /brand-update to add]`

### File Template

```markdown
# Brand Intelligence — {{Business Name}}

> Auto-assembled from Brand Intelligence Center. Last updated: {{date}}
> To update any section, run `/brand-update`.

You are an AI assistant working for {{business_name}}. Use the following brand context to inform all work. Read this before taking any marketing action.

## Who We Are
{{assembled_from_business}}

## Our Customer
{{assembled_from_customer}}

## Why Customers Choose Us
{{assembled_from_differentiation}}

## Brand Voice & Personality
**We are:** {{personality}}
**Tone:** {{tone}}

### ALWAYS
{{always_list}}

### NEVER
{{never_list}}

### Vocabulary
{{vocabulary}}

## Proof Points
{{assembled_from_proof_goals}}

## Our Goal
**Primary conversion action:** {{primary_cta}}
**Current focus:** {{current_focus}}

## Digital Presence
{{assembled_from_digital_ecosystem}}

## Financial Context
{{assembled_from_financial — high level only}}
```

---

## Reading Brand Intelligence (For Other Skills)

Any Strategy Labs plugin or marketing skill that needs brand context should:

1. Read `brand-intelligence-center/system-prompt.md` — always at the root, always the active brand
2. Do not read from inside `brands/[slug]/` directly — always use the root file
3. Do not re-ask for information already captured in the system prompt
4. If the file doesn't exist: "This skill works best with brand context. Run `/brand-setup` to create your brand profile. I'll proceed with what you provide in the meantime."

### Priority Loading Order for Other Skills

1. `brand-intelligence-center/system-prompt.md` — Always load first (active brand master)
2. `brand-intelligence-center/customer.md` — For copywriting, email, CRO, paid ads
3. `brand-intelligence-center/differentiation.md` — For competitive analysis, positioning, sales enablement
4. `brand-intelligence-center/voice-identity.md` — For content creation, copy editing, social
5. `brand-intelligence-center/proof-goals.md` — For landing pages, ads, email
6. `brand-intelligence-center/digital-ecosystem.md` — For platform-specific work
7. `brand-intelligence-center/financial.md` — Only when financial context is explicitly needed

> **Agency mode note:** In agency mode, the root files are always copies of the active brand. Skills don't need to know about `brands/` — they just read from the root.

### Backward Compatibility

If `brand-knowledge-center/system-prompt.md` or `.agents/product-marketing-context.md` exist but `brand-intelligence-center/` does not, load those as fallback context and note: "For richer brand context, run `/brand-setup` to build your Brand Intelligence Center."

---

## Active Brand Sync Rules

Whenever the active brand changes (via `/brand-switch`) or a brand's files are updated:

1. Copy the active brand's individual files (`business.md`, `customer.md`, etc.) to the root `brand-intelligence-center/` folder
2. Re-assemble and overwrite `brand-intelligence-center/system-prompt.md` from the active brand's files
3. Update `.active-brand` with the new brand slug
4. Confirm: "Now working on **[Brand Name]**. All marketing skills are loaded with their context."

The root files are always a live copy — never a symlink — so every skill can read them without any special handling.

---

## Team Collaboration

The Brand Intelligence Center supports team review, revision, and sync workflows so multiple team members can stay aligned on brand context.

### Configuration File

`.brand-intel-config.md` — sits one level above `brand-intelligence-center/` (in the working directory root). Local only, never synced.

```markdown
# Brand Intelligence Config

## Storage
- **mode:** local | fast.io
- **workspace_id:** [19-digit Fast.io workspace ID]
- **workspace_name:** [human-readable name]

## Sync
- **last_pull:** [ISO 8601 timestamp]
- **last_push:** [ISO 8601 timestamp]
- **auto_pull_on_start:** true | false

## Team
- **team_members:** [comma-separated names or emails for changelog attribution]
- **review_share_id:** [Fast.io share ID, populated after first /brand-review share]
```

---

### /brand-review — Generate a Team Review Document

Produces a clean, human-readable brand document for team distribution. Not a raw dump of the markdown files — a formatted, plain-language summary any team member can read and annotate.

**Step 1 — Check for existing config:**
Read `.brand-intel-config.md`. Note whether Fast.io sync is configured.

**Step 2 — Read all area files:**
Read all brand-intelligence-center area files for the active brand. Note which areas are complete vs. marked `[Not yet completed]`.

**Step 3 — Check revision history:**
Read `brand-intelligence-center/changelog.md` if it exists. Note the date of the last revision for each area.

**Step 4 — Generate the review document:**

Read `${CLAUDE_PLUGIN_ROOT}/skills/brand-intelligence/references/review-templates.md` for the full output format.

The review document is written in plain, human-readable language — no raw markdown syntax, no code blocks, no template variables. Written as if a brand strategist summarized the brand for a colleague.

Save to `brand-intelligence-center/review/brand-review-{{YYYY-MM-DD}}.md`.

**Step 5 — Handle `share` argument:**

If `/brand-review share` was invoked:
1. Authenticate with Fast.io (read config for workspace_id; if not configured, ask and save to config)
2. Upload the review document to the Fast.io workspace using `upload text-file`
3. Create a Fast.io share with `share create` (type: "send", access: "anyone_with_link")
4. Save the share ID to `.brand-intel-config.md` as `review_share_id`
5. Return the share URL: "Your brand review is ready to share: [URL] — anyone with this link can read it and add comments."

**Step 6 — Report:**
> Brand review generated for **[Brand Name]** — [N] areas documented.
>
> Saved to: `brand-intelligence-center/review/brand-review-{{date}}.md`
> [If shared]: Share link: {{url}}
>
> **Areas to complete:** [list any incomplete areas]
>
> To collect team feedback and apply revisions, run `/brand-revise`.

---

### /brand-revise — Apply Team Revisions

Accepts revision input, proposes specific changes as before/after comparisons, requires confirmation, applies changes, rebuilds system-prompt.md, and logs everything.

**Step 1 — Collect revision input:**

> How would you like to provide revision notes?
> - `[ ]` Paste notes now (copy from email, Slack, a doc, or a review document)
> - `[ ]` Pull from Fast.io review comments (requires sync to be configured)
> - `[ ]` Describe changes conversationally

If pasting: accept the input and proceed to Step 2.
If Fast.io: use `execute` action `ai chat-create` on the review document to extract all comments. Summarize for confirmation before proceeding.
If conversational: gather changes through dialogue, confirm understanding before proposing.

**Step 2 — Parse revision notes:**

Read the revision input and identify:
- Which area each revision affects (business, customer, differentiation, voice-identity, proof-goals, digital-ecosystem, financial)
- Which specific field within that area
- What the proposed new value is
- Whether the revision is an addition, edit, or removal

For ambiguous revisions, ask a clarifying question before proposing a change.

**Step 3 — Read current values:**

For each identified area, read the current file content. Extract the specific field values that are being changed.

**Step 4 — Present before/after for each change:**

Present changes one area at a time, grouped. For each field:

```
─────────────────────────────────────────
Area: Customer Profile
Field: Primary Customer

CURRENT:
  Young professionals aged 28–40, urban, household income $80K+,
  interested in fitness and outdoor recreation.

PROPOSED:
  Young professionals aged 25–45, urban and suburban, household
  income $75K+, interested in fitness, outdoor recreation, and
  sustainable lifestyle choices.

Confirm? [Y]es / [S]kip / [E]dit
─────────────────────────────────────────
```

After all individual changes are presented, offer: "Confirm all [N] changes at once? [Y/N]"

**Step 5 — Apply confirmed changes:**

For each confirmed change:
1. Read the current area file
2. Apply the specific field edit
3. Write the updated file
4. Note the change in a running log for the changelog entry

Do not apply skipped changes. For edited changes, show the edited version and confirm again before applying.

**Step 6 — Rebuild system-prompt.md:**

After all changes are applied:
1. Read all updated area files
2. Re-assemble `system-prompt.md` following the Assembly Rules from the Setup Wizard section
3. Write the new `system-prompt.md`
4. In agency mode: also write to `brands/{{slug}}/system-prompt.md` and sync to root

**Step 7 — Update changelog:**

Append to `brand-intelligence-center/changelog.md` (create if it doesn't exist):

```markdown
## {{YYYY-MM-DD}} — [N] changes applied

**Revised by:** {{team_members from config, or "User"}}
**Areas updated:** {{list of affected areas}}

### Changes

**{{Area Name}} — {{Field}}**
- Before: {{previous value}}
- After: {{new value}}

**{{Area Name}} — {{Field}}**
- Before: {{previous value}}
- After: {{new value}}
```

**Step 8 — Auto-push if sync is configured:**

If `.brand-intel-config.md` exists and `mode` is `fast.io`:
> Your brand files have been updated. Push the changes to Fast.io so your team has the latest version?
> `[ ]` Yes — push now
> `[ ]` No — I'll push manually with `/brand-sync push`

---

### /brand-sync — Fast.io File Synchronization

Syncs `brand-intelligence-center/` files between local and a Fast.io workspace.

**Before starting:**
1. Read `.brand-intel-config.md`. If not found: offer to set it up (ask for workspace ID) or create a new Fast.io workspace.
2. If `mode` is `local`: inform user sync is disabled. Offer to switch to `fast.io`.
3. If `mode` is `fast.io`: proceed.

**Argument routing** (check `$ARGUMENTS`):
- `pull` → Pull Workflow
- `push` → Push Workflow
- `status` → Status Workflow
- empty → Ask which direction

**Pull Workflow (Fast.io → Local):**
1. Authenticate (read config; if session inactive, use `auth pkce-login`)
2. List files in `brand-intelligence-center/` folder in the Fast.io workspace
3. For each brand area file: fetch from Fast.io, write locally
4. For agency mode: pull from `brands/{{slug}}/` folder for the active brand
5. Update `last_pull` in config
6. Re-assemble `system-prompt.md` from pulled files
7. Report: "[N] brand files pulled. system-prompt.md rebuilt."

**Push Workflow (Local → Fast.io):**
1. Authenticate
2. Read all files in local `brand-intelligence-center/`
3. Upload each file to the Fast.io workspace's `brand-intelligence-center/` folder using `upload text-file`
4. For agency mode: upload to `brands/{{slug}}/` folder
5. Update `last_push` in config
6. Report: "[N] brand files pushed to [workspace name]."

**Status Workflow:**
1. Read config — display storage mode, workspace name, last pull/push timestamps (with "X hours/days ago")
2. List local files with last-modified dates
3. If `last_pull` > 24 hours: "Your local files may be out of date. Run `/brand-sync pull` to check."
4. If `last_push` > local file modification dates: "You have local changes not yet pushed. Run `/brand-sync push` to share with your team."

**Sync scope — files included:**
- All 7 area files (`business.md`, `customer.md`, `differentiation.md`, `voice-identity.md`, `proof-goals.md`, `digital-ecosystem.md`, `financial.md`)
- `system-prompt.md`
- `changelog.md`
- Agency mode: `.active-brand` file

**Sync scope — files excluded:**
- `review/` directory (review documents are shared outbound via share links, not pulled)
- `.brand-intel-config.md` (local-only, never synced)

**Error handling:**

| Scenario | Behavior |
|----------|----------|
| No config file | Offer to create one (ask for workspace ID) |
| mode is `local` | Inform sync is disabled. Offer to switch |
| Auth fails | Trigger `auth pkce-login` flow |
| Workspace not found | Report workspace ID from config. Suggest verifying |
| File not found on remote (pull) | Create locally from scratch or skip with note |
| File not found locally (push) | Skip with note |
| Network failure | Report which files succeeded/failed. Don't update timestamps if any failed |

---

### Changelog

`brand-intelligence-center/changelog.md` is automatically maintained by the revision workflow. Never edit manually — always through `/brand-revise`.

**Format:**
```markdown
# Brand Intelligence Changelog — {{Brand Name}}

## {{YYYY-MM-DD}} — [N] changes applied
**Revised by:** {{name}}
**Areas updated:** {{list}}

### Changes
**{{Area}} — {{Field}}**
- Before: {{value}}
- After: {{value}}

---

## {{earlier date}} — [N] changes applied
...
```

The changelog travels with the brand files — it syncs to Fast.io alongside the area files so team members can see the full revision history.
