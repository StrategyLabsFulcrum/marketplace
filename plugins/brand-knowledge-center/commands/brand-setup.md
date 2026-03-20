# Brand Setup Wizard

Create a complete brand knowledge profile through a step-by-step guided onboarding. This wizard produces a `brand-knowledge-center/` folder with structured markdown files that serve as the foundation for all Strategy Labs plugins.

## Before Starting

1. Check if a `brand-knowledge-center/` directory already exists in the user's working folder.
   - If it exists and has files, inform the user: "You already have a brand profile set up. Would you like to update specific sections (try `/update-brand`), or start fresh?"
   - If starting fresh, back up existing files by renaming the folder to `brand-knowledge-center-backup-[date]/`.
2. Create the `brand-knowledge-center/` directory if it doesn't exist.
3. Read the full skill definition at `${CLAUDE_PLUGIN_ROOT}/skills/brand-knowledge/SKILL.md` for field definitions and file templates.

## Wizard Flow

Run each step in order. At the end of each step, confirm the collected information with the user before moving to the next step. The user can say "skip" to move past any optional step.

---

## Step 1: Business Foundation

**Goal:** Establish who the brand is and how the business operates.

### 1a. Get the Website URL

Ask: "What's your website URL?"

Once provided:
- Fetch the homepage and key pages (About, Products/Services if accessible)
- Extract: company name, industry signals, product/service descriptions, about page content, any team member info
- Store the raw findings for use across subsequent steps

### 1b. Identify Industry

Based on the website content:
- Suggest an industry and sub-category (e.g., "eCommerce — Outdoor / Off-Road Parts & Accessories")
- Ask: "Based on your website, it looks like you're in **{{suggested_industry}}**. Is that right, or would you describe it differently?"
- Accept the user's correction or confirmation

### 1c. Accounting Approach

Ask: "What accounting approach does your business use?"
- **Cash basis** — Revenue and expenses recorded when cash changes hands
- **Accrual basis** — Revenue and expenses recorded when earned/incurred

### 1d. Key Roles

Ask: "Who are the key people in your company? At minimum, I need the owner/CEO — but it's helpful to know other key roles too."

Prompt for:
| Role | Name | Email (optional) |
|------|------|-------------------|
| CEO / Owner | | |
| CFO / Finance | | |
| CMO / Marketing | | |
| COO / Operations | | |
| Other | | |

The user can provide as many or as few as they want. Only CEO/Owner is required.

### 1e. Mission & Vision

Check if anything was extracted from the website. If so:
- Present it: "I found this on your website: '{{extracted_text}}'. Does this capture your mission/vision?"
- Let them confirm, edit, or replace

If nothing was found:
- Ask: "In one or two sentences, what does your company exist to do?"

### 1f. Elevator Pitch

If not already captured:
- Draft a 2-3 sentence elevator pitch from the collected info
- Present it and ask for approval or edits

### Step 1 Review

Present all Business Foundation info in a clean summary. Ask: "Does this look right? Edit anything that needs changing, or say 'next' to continue."

**Generate:** `brand-knowledge-center/business-overview.md` using the template from the skill definition.

---

## Step 2: Financial Context

**Goal:** Capture financial fundamentals and key metrics.

### 2a. Document Upload

Ask: "Do you have any P&L (Profit & Loss) statements or balance sheets you'd like to upload? These help us understand your business better. This is completely optional."

**If documents are uploaded:**
1. Read and parse each document
2. Identify the document type (P&L, balance sheet, other)
3. Extract key metrics:
   - **From P&L:** Revenue, COGS, gross profit, gross margin %, operating expenses (top 3-5 categories), net income, net margin %
   - **From Balance Sheet:** Total assets, total liabilities, equity, cash position
4. If multiple periods are present, calculate growth rates and trend direction
5. Present extracted metrics in a clean table
6. Ask: "Here's what I extracted. Does this look accurate? Anything to correct or add?"
7. Flag any unusual numbers: "Your gross margin shows as 85% — is that right?"

**If no documents:**
Ask for approximate ranges:
- "What's your approximate annual revenue?" (offer ranges: under $500K, $500K-$1M, $1M-$5M, $5M-$10M, $10M+)
- "What's your primary revenue source?"
- "Any financial goals you'd like to share? (growth targets, margin goals, etc.)"

### 2b. Financial Goals

Ask: "What are your key financial goals for the next 12 months?"
- Revenue targets
- Margin improvement
- New revenue streams
- Cost reduction areas

### Step 2 Review

Present the financial summary. Mark the data source clearly (uploaded documents vs. manual entry).

**Generate:** `brand-knowledge-center/financial-snapshot.md`

---

## Step 3: Digital Presence

**Goal:** Map the brand's entire digital ecosystem — platforms, tools, and channels.

### 3a. Social Media URLs

Using the website scraped in Step 1:
1. Search for social media links (footer, header, sidebar, contact page)
2. Look for: Facebook, Instagram, X/Twitter, LinkedIn, TikTok, YouTube, Pinterest, Threads
3. Present findings: "I found these social media links on your website:"

| Platform | URL | Found In |
|----------|-----|----------|
| Instagram | {{url}} | Footer |
| Facebook | {{url}} | Footer |

4. Ask: "Are these correct? Any platforms I missed?"
5. For each confirmed platform, ask: "Is this account active (posting regularly) or dormant?"
6. Ask about posting cadence if relevant: "How often do you typically post on {{platform}}?"

If scraping didn't find social links, ask the user to provide them manually.

### 3b. Website Platform

If not already detected from the website:
- Ask: "What platform is your website built on?"
- Suggest common options: Shopify, WordPress, Wix, Squarespace, Webflow, BigCommerce, Custom
- Accept the answer

### 3c. Marketing & Communication Tools

Ask about each category. Offer common suggestions for their industry:

**Email / SMS:**
- "What email or SMS platform do you use?" (Klaviyo, Mailchimp, Attentive, Postscript, Omnisend, none)

**CRM:**
- "Do you use a CRM?" (HubSpot, Salesforce, Zoho, Pipedrive, none)

**Advertising:**
- "What advertising platforms do you run ads on?" (Meta Ads, Google Ads, TikTok Ads, Pinterest Ads, Microsoft/Bing Ads, none)

**Analytics:**
- "What analytics tools do you use?" (Google Analytics / GA4, Mixpanel, Hotjar, none)

**Reviews:**
- "Where do customers leave reviews?" (Google Business, Yelp, Trustpilot, Yotpo, Judge.me, none)

**Other:**
- "Any other key tools in your stack?" (project management, design, customer support, etc.)

### Step 3 Review

Present the full digital ecosystem summary.

**Generate:** `brand-knowledge-center/digital-ecosystem.md`

---

## Step 4: Brand Identity

**Goal:** Capture brand guidelines — visual identity, voice, and positioning.

### 4a. Check for Existing Guidelines

Ask: "Do you have existing brand guidelines (a style guide, brand book, or similar document) you can upload?"

#### Path A: Guidelines Uploaded

1. Parse the document
2. Extract:
   - Logo descriptions and usage rules
   - Color palette (primary, secondary, accent) — capture hex codes if visible
   - Typography / fonts (headings, body, accent)
   - Brand pillars / values
   - Voice and tone direction
   - Messaging frameworks or key phrases
   - Do's and don'ts
3. Present extracted information organized by category
4. Ask: "Here's what I pulled from your brand guide. Anything to correct or add?"
5. For any areas not covered in the document, fall through to Path B questions for those specific gaps

#### Path B: Guided Questions (No Guidelines)

**Core Positioning:**

Ask: "What's the one thing your brand promises its customers — not a tagline, but the core truth about what you deliver?"
- If they struggle, suggest based on website content: "Based on your site, it seems like your core promise might be: '{{suggestion}}'. Does that resonate?"

Ask: "What makes your brand fundamentally different from alternatives?"

**Brand Pillars:**

Suggest 3-5 pillars based on website content and industry:
- "Based on your website, here are some brand pillars that seem to fit:"
- Present each with a name, description, and how it shows up in practice
- Ask: "Do these feel right? Edit, remove, or add any."

If the website didn't provide enough to suggest, ask:
- "What are the 3-5 non-negotiable values or principles that define your brand?"

**Voice & Tone:**

Ask: "If your brand were a person, how would they talk? Pick the point on each spectrum that feels right:"
- Casual ↔ Formal
- Playful ↔ Serious
- Bold ↔ Understated
- Technical ↔ Conversational
- Rebellious ↔ Established

Ask: "Are there words or phrases your brand should NEVER use?" (Suggest common ones for their industry)

Ask: "What should ALWAYS be true about your brand's content?"

**Visual Identity (optional):**

Ask: "Do you have brand colors? If so, share the hex codes or describe them."
- Primary color
- Secondary color
- Accent color

Ask: "What fonts does your brand use?"
- Heading font
- Body font

Ask: "Can you describe your logo, or upload an image of it?"

**Taglines:**

Ask: "Do you have a tagline or slogan?"
- If yes, capture it
- If no, suggest 2-3 based on the core promise and pillars. Ask for feedback.

### Step 4 Review

Present the complete brand identity summary. Clearly note which items came from uploaded guidelines vs. guided answers vs. suggestions.

**Generate:** `brand-knowledge-center/brand-identity.md`

---

## Step 5: Audience & Messaging

**Goal:** Define who the brand speaks to and how.

### 5a. Primary Audience

Using website content (product descriptions, testimonials, about page) and the industry:
1. Draft a primary audience profile:
   - A persona name (e.g., "The Performance Junkie", "The Health-Conscious Parent")
   - Who they are (mindset and identity, not just demographics)
   - Their pain points
   - Their aspirations
   - Where they spend time online
2. Present: "Based on your website and industry, your primary audience seems to be:"
3. Ask: "Does this match how you think about your ideal customer? What would you change?"

### 5b. Secondary Audiences

Ask: "Do you have other distinct customer segments?"
- If yes, build profiles for each using the same structure
- If unsure, suggest 1-2 secondary audiences based on the website and ask for confirmation

### 5c. Messaging Framework

For each audience, draft a messaging framework:
- **Headline Angle** — The hook that grabs attention
- **Key Benefit** — The primary value they care about
- **Proof Point** — Why they should believe it
- **CTA Direction** — What action to drive

Present the framework(s) and ask: "Does this feel like how you'd talk to {{audience_name}}? What would you adjust?"

### 5d. Content Pillars

Suggest 3-6 content themes based on:
- Brand pillars from Step 4
- Audience interests from 5a/5b
- Industry norms

Each pillar needs: name, purpose, primary emotion, example topics.

Present and ask for feedback.

### 5e. Key Messages & Power Phrases

Check if any were captured from the website or brand guidelines. If so, present them.

Ask: "Are there specific phrases, taglines, or messages that you use repeatedly in your marketing?"

If limited input, suggest a few based on the brand's positioning and ask for approval.

### Step 5 Review

Present all audience and messaging information.

**Generate:** `brand-knowledge-center/audience-messaging.md`

---

## Step 6: Competitive Landscape

**Goal:** Identify competitors and map the brand's competitive position.

### 6a. Identify Competitors

Two-pronged approach:

**Suggest competitors:**
1. Based on the industry, sub-category, business model, and website content from earlier steps
2. Suggest 3-5 likely competitors with brief reasoning:
   - "Based on your industry ({{industry}}) and what you sell, here are some likely competitors:"
   - {{Competitor 1}} — "They appear to be a direct competitor because..."
   - {{Competitor 2}} — "They overlap in..."
3. Ask: "Are these your competitors? Remove any that aren't relevant, and add anyone I missed."

**Ask directly:**
- "Who do you consider your top 3-5 competitors?"
- "What are their website URLs?"

Merge both lists, dedup, and confirm with the user.

### 6b. Competitor Analysis

For each confirmed competitor (if URLs are provided):
1. Fetch the competitor's homepage
2. Extract: positioning signals, taglines, product/service focus, apparent audience
3. Summarize their apparent positioning and strengths

Present for each competitor:
- **Their Positioning:** What they seem to stand for
- **Their Strengths:** What they do well
- **Their Weaknesses:** Where they fall short (ask the user — they know this better than a website scrape)
- **Our Counter-Position:** How this brand is fundamentally different (draft based on brand identity, ask for confirmation)

### 6c. Competitive Matrix

Build a comparison table across all competitors on key factors:
- Positioning
- Primary audience
- Price point (if visible)
- Key strength
- Key weakness

Present and ask for corrections.

### 6d. Competitor Platforms

Ask: "Which platforms are your competitors most active on?" (or attempt to detect from their websites)

### Step 6 Review

Present the full competitive landscape.

**Generate:** `brand-knowledge-center/competitive-landscape.md`

---

## Step 7: Review & Generate System Prompt

**Goal:** Final review and system prompt assembly.

### 7a. Full Summary

Present a condensed overview of ALL 6 areas — one paragraph per area highlighting the key points. This gives the user a bird's-eye view before final generation.

### 7b. Gap Check

Review all files for completeness. Flag any areas that are thin:
- "Your financial snapshot is based on estimated ranges — you can upload P&L documents later with `/update-brand financial`"
- "Your brand identity section doesn't have visual identity details yet — you can add these anytime"

### 7c. Generate System Prompt

Read all 6 files and assemble `brand-knowledge-center/system-prompt.md` following the assembly rules in the skill definition:
1. Brand identity and core positioning first
2. Business context
3. Audience and messaging
4. Voice and tone rules (NEVER/ALWAYS lists verbatim)
5. Competitive context
6. Digital ecosystem context
7. High-level financial summary
8. Keep under 3000 words

### 7d. Completion Message

After all files are generated:

1. List all files created:
   ```
   brand-knowledge-center/
   ├── business-overview.md       ✓
   ├── financial-snapshot.md      ✓
   ├── digital-ecosystem.md       ✓
   ├── brand-identity.md          ✓
   ├── audience-messaging.md      ✓
   ├── competitive-landscape.md   ✓
   └── system-prompt.md           ✓
   ```

2. Note completeness per file (fully populated, partially populated, minimal)

3. Suggest next steps:
   - "Your brand knowledge center is ready. Any Strategy Labs plugin can now use this as context."
   - "To update any section later, run `/update-brand` and specify the area."
   - "The more detail in these files, the better results you'll get from other plugins."

4. If any areas were skipped or thin, suggest which to prioritize expanding
