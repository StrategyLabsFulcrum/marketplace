# Brand Profile Schema

Complete field definitions for all 6 areas of the Brand Knowledge Center. This reference is used by the setup wizard and update commands to ensure consistent, thorough data collection.

---

## Area 1: Business Overview

### Fields

#### Brand / Company Name
- **Required:** Yes
- **Type:** Text
- **Gathering prompt:** "What's the name of your company or brand?"
- **Notes:** Use the brand name (customer-facing) as primary, legal entity name as secondary if different.

#### Website URL
- **Required:** Yes
- **Type:** URL
- **Gathering prompt:** "What's your website URL?"
- **Notes:** This is the starting point for website scraping. Validate the URL is accessible.

#### Industry / Category
- **Required:** Yes
- **Type:** Text
- **Gathering prompt:** Suggest based on website content. "Based on your website, it looks like you're in **{{suggestion}}**. Is that right?"
- **Examples:** eCommerce, SaaS, Professional Services, Local Business (Restaurant), Healthcare, Finance, Education
- **Notes:** Be specific. "eCommerce" is less useful than "eCommerce — Off-Road Vehicle Parts & Accessories"

#### Sub-category / Niche
- **Required:** Recommended
- **Type:** Text
- **Gathering prompt:** "Can you describe your niche more specifically?"
- **Notes:** Helps with competitor identification and industry-specific suggestions.

#### Year Founded
- **Required:** Optional
- **Type:** Year
- **Gathering prompt:** "When was your company founded?"
- **Notes:** Extract from website About page if available.

#### Company Size
- **Required:** Optional
- **Type:** Selection
- **Options:** Solo / 2-5 / 6-10 / 11-50 / 51-200 / 200+
- **Gathering prompt:** "Roughly how many people work at your company?"

#### Accounting Approach
- **Required:** Yes
- **Type:** Selection
- **Options:** Cash basis / Accrual basis
- **Gathering prompt:** "What accounting approach does your business use — cash basis or accrual basis?"
- **Notes:** Cash = revenue/expenses recorded when cash changes hands. Accrual = recorded when earned/incurred. Important for interpreting financial documents.

#### Business Model
- **Required:** Recommended
- **Type:** Text
- **Gathering prompt:** Suggest based on website. "Your business model looks like {{suggestion}}. Does that sound right?"
- **Examples:** DTC eCommerce, B2B Services, SaaS (subscription), Local Business (brick & mortar), Marketplace, Wholesale + DTC, Agency / Consulting

#### Key Roles
- **Required:** Yes (at minimum CEO/Owner)
- **Type:** Table (Name, Role, Email)
- **Gathering prompt:** "Who are the key people in your company? I need at least the owner/CEO, but knowing other key roles (CFO, CMO, COO, Head of Marketing, etc.) helps."
- **Notes:** Email is optional per person. Capture as many roles as the user provides.

#### Mission / Vision
- **Required:** Optional
- **Type:** Text (1-3 sentences)
- **Gathering prompt:** Check website About page first. If found: "I found this on your site: '{{text}}'. Does this capture your mission?" If not found: "In one or two sentences, what does your company exist to do?"

#### Elevator Pitch
- **Required:** Recommended
- **Type:** Text (2-3 sentences)
- **Gathering prompt:** If not available, draft from collected info: "Here's a quick elevator pitch based on what you've told me: '{{draft}}'. How does that sound?"

---

## Area 2: Financial Snapshot

### Fields

#### Accounting Basis
- **Required:** Yes
- **Type:** Selection (Cash / Accrual)
- **Notes:** Carried from Area 1.

#### Reporting Period
- **Required:** When documents uploaded
- **Type:** Date range
- **Gathering prompt:** "What period do these financials cover?"

#### Data Source
- **Required:** Yes
- **Type:** Selection (Uploaded P&L / Uploaded Balance Sheet / Manual Entry)
- **Notes:** Track the source so other plugins know the data quality.

#### Revenue
- **Required:** Recommended
- **Type:** Currency
- **Gathering prompt (upload):** Extract from P&L top line
- **Gathering prompt (manual):** "What's your approximate annual revenue?" Offer ranges: under $500K, $500K-$1M, $1M-$5M, $5M-$10M, $10M+

#### COGS / Cost of Goods Sold
- **Required:** When available from documents
- **Type:** Currency
- **Gathering prompt:** Extract from P&L

#### Gross Profit / Gross Margin %
- **Required:** Recommended
- **Type:** Currency / Percentage
- **Gathering prompt (upload):** Calculate from Revenue - COGS
- **Gathering prompt (manual):** "Do you know your approximate gross margin?"

#### Operating Expenses (Top Categories)
- **Required:** When available from documents
- **Type:** Table (Category, Amount, % of Revenue)
- **Notes:** Extract top 3-5 expense categories from P&L

#### Net Income / Net Margin %
- **Required:** When available from documents
- **Type:** Currency / Percentage

#### YoY Growth
- **Required:** When multiple periods available
- **Type:** Percentage
- **Notes:** Calculate from comparing periods

#### Cash Position
- **Required:** When balance sheet available
- **Type:** Currency

#### Total Assets
- **Required:** When balance sheet available
- **Type:** Currency

#### Total Liabilities
- **Required:** When balance sheet available
- **Type:** Currency

#### Equity
- **Required:** When balance sheet available
- **Type:** Currency

#### Financial Goals
- **Required:** Recommended
- **Type:** Text (bullet points)
- **Gathering prompt:** "What are your key financial goals for the next 12 months? (revenue targets, margin improvements, growth plans, etc.)"

---

## Area 3: Digital Ecosystem

### Fields

#### Website Platform
- **Required:** Yes
- **Type:** Selection / Text
- **Options:** Shopify, WordPress, Wix, Squarespace, Webflow, BigCommerce, Magento, Custom, Other
- **Gathering prompt:** Attempt to detect from website source. If detected: "It looks like your site runs on {{platform}}. Is that right?" If not: "What platform is your website built on?"

#### Social Media Accounts
- **Required:** Yes
- **Type:** Table (Platform, URL, Status, Cadence)
- **Platforms to check:** Facebook, Instagram, X/Twitter, LinkedIn, TikTok, YouTube, Pinterest, Threads
- **Gathering prompt:** Scrape website for social links first. Present findings and ask for corrections/additions.
- **Status options:** Active (posting regularly) / Dormant (has account but rarely posts) / N/A
- **Cadence examples:** Daily, 3-5x/week, Weekly, Monthly, Sporadic

#### Email / SMS Platform
- **Required:** Recommended
- **Type:** Text
- **Common options:** Klaviyo, Mailchimp, Attentive, Postscript, Omnisend, ActiveCampaign, Constant Contact, None
- **Gathering prompt:** "What email or SMS marketing platform do you use?"

#### CRM
- **Required:** Recommended
- **Type:** Text
- **Common options:** HubSpot, Salesforce, Zoho, Pipedrive, Monday, None
- **Gathering prompt:** "Do you use a CRM (Customer Relationship Management) tool?"

#### Advertising Platforms
- **Required:** Recommended
- **Type:** List
- **Common options:** Meta Ads (Facebook/Instagram), Google Ads, TikTok Ads, Pinterest Ads, Microsoft/Bing Ads, Amazon Ads, None
- **Gathering prompt:** "What advertising platforms do you run ads on?"

#### Analytics Tools
- **Required:** Recommended
- **Type:** List
- **Common options:** Google Analytics (GA4), Mixpanel, Hotjar, Amplitude, None
- **Gathering prompt:** "What analytics tools do you use to track website/app performance?"

#### Review Platforms
- **Required:** Optional
- **Type:** List
- **Common options:** Google Business Profile, Yelp, Trustpilot, Yotpo, Judge.me, Stamped, BBB, None
- **Gathering prompt:** "Where do your customers leave reviews?"

#### Other Tools
- **Required:** Optional
- **Type:** List with descriptions
- **Gathering prompt:** "Any other key tools in your stack? (project management, design, customer support, inventory, etc.)"

---

## Area 4: Brand Identity

### Fields

#### Source
- **Required:** Yes
- **Type:** Selection (Uploaded guidelines / Built from guided questions / Hybrid)
- **Notes:** Track whether identity was extracted from a document or built through the wizard.

#### Core Promise
- **Required:** Recommended
- **Type:** Text (1-2 sentences)
- **Gathering prompt:** "What's the one thing your brand promises its customers? Not a tagline — the core truth about what you deliver."
- **Fallback:** Suggest based on website content and ask for confirmation.

#### Point of Difference
- **Required:** Recommended
- **Type:** Text (1-2 sentences)
- **Gathering prompt:** "What makes your brand fundamentally different from the alternatives?"

#### Taglines
- **Required:** Recommended
- **Type:** List
- **Gathering prompt:** "Do you have a tagline or slogan?" If no, suggest 2-3 and ask for feedback.

#### Brand Pillars
- **Required:** Yes
- **Type:** Table (Name, Description, In Practice)
- **Count:** 3-5
- **Gathering prompt:** Suggest based on website/industry first. "Here are some brand pillars that seem to fit your brand. Do these feel right?"
- **Each pillar needs:** A short name, a one-line description, and how it shows up in practice.

#### Voice Traits (Spectrum)
- **Required:** Yes
- **Type:** Table (Trait, Spectrum Position, In Practice)
- **Spectrums:** Casual↔Formal, Playful↔Serious, Bold↔Understated, Technical↔Conversational, Rebellious↔Established
- **Gathering prompt:** "If your brand were a person, how would they talk? For each pair, tell me where you fall."

#### NEVER List
- **Required:** Recommended
- **Type:** Bullet list
- **Gathering prompt:** "Are there words, phrases, or tones your brand should NEVER use?"
- **Notes:** Suggest common industry-specific items to get the conversation started.

#### ALWAYS List
- **Required:** Recommended
- **Type:** Bullet list
- **Gathering prompt:** "What should ALWAYS be true about your brand's content?"

#### Primary Color
- **Required:** Optional
- **Type:** Text (hex code or color name)
- **Gathering prompt:** "What's your brand's primary color? Share a hex code if you have one."

#### Secondary Color
- **Required:** Optional
- **Type:** Text

#### Accent Color
- **Required:** Optional
- **Type:** Text

#### Heading Font
- **Required:** Optional
- **Type:** Text
- **Gathering prompt:** "What font does your brand use for headings?"

#### Body Font
- **Required:** Optional
- **Type:** Text

#### Logo Description
- **Required:** Optional
- **Type:** Text
- **Gathering prompt:** "Can you describe your logo, or upload an image of it?"

#### Vocabulary Reference
- **Required:** Optional
- **Type:** Table (Use This, Instead Of)
- **Gathering prompt:** "Are there specific words your brand prefers over common alternatives? For example, 'rider' instead of 'customer'."

---

## Area 5: Audience & Messaging

### Fields

#### Primary Audience
- **Required:** Yes
- **Type:** Structured profile
- **Fields:** Persona name, Who they are, Pain points, Aspirations, Where they are (channels)
- **Gathering prompt:** Suggest based on website/industry. "Based on your website, your primary audience seems to be: {{profile}}. Does this match?"

#### Secondary Audiences
- **Required:** Recommended
- **Type:** Table of profiles
- **Gathering prompt:** "Do you have other distinct customer segments beyond your primary audience?"

#### Messaging Framework (per audience)
- **Required:** Yes
- **Type:** Structured (Headline Angle, Key Benefit, Proof Point, CTA Direction)
- **Gathering prompt:** Draft a framework and present for feedback. "Here's a messaging framework for {{audience}}. Does this feel like how you'd talk to them?"

#### Content Pillars
- **Required:** Recommended
- **Type:** Table (Name, Purpose, Primary Emotion, Example Topics)
- **Count:** 3-6
- **Gathering prompt:** Suggest based on brand pillars and audience interests.

#### Key Messages / Power Phrases
- **Required:** Recommended
- **Type:** Table (Message, Best Used For, Platform)
- **Gathering prompt:** "Are there specific phrases or messages you use repeatedly in your marketing?"

---

## Area 6: Competitive Landscape

### Fields

#### Competitors
- **Required:** Yes
- **Type:** List (3-5 recommended)
- **Gathering prompt:** Two-pronged: suggest based on industry/website AND ask directly. Merge and confirm.

#### Competitor Details (per competitor)
- **Website URL:** Required per competitor
- **Their Positioning:** What they appear to stand for (scrape + user input)
- **Their Strengths:** What they do well (ask the user)
- **Their Weaknesses:** Where they fall short (ask the user)
- **Our Counter-Position:** How this brand is different (draft and confirm)
- **Their Platforms:** Which social/marketing platforms they use (detect or ask)

#### Competitive Matrix
- **Required:** Recommended
- **Type:** Table comparing all competitors on: Positioning, Primary Audience, Price Point, Key Strength, Key Weakness
- **Notes:** Auto-generate from competitor details. Present for review.
