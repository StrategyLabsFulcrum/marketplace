# Platform Prompt Templates

Generalized prompt templates organized by platform. Each template uses `{{variables}}` that get populated from brand knowledge files (auto) or per-use input (asked at generation time).

All templates assume the brand's system prompt has already been loaded as foundational context.

---

## META ADS

### META-1: Ad Copy Generator — Pain / Gain / Tech Variations

```
TASK: Create 3 ad copy variations for a Meta campaign promoting {{product_name}}.

TARGET: {{target_audience}} — someone who identifies with the {{brand_name}} mindset.
AD TYPE: Short-form text for Facebook/Instagram feed ads.

VARIATION A — THE PAIN (fear of failure / breakdown / performance compromise):
- Headline (max 40 chars), 2-3 body sentences, Performance CTA, 3-5 emojis

VARIATION B — THE GAIN (confidence, aspiration, elite status):
- Headline (max 40 chars), 2-3 body sentences, Aspirational CTA, 3-5 emojis

VARIATION C — THE TECH (overbuilt specs, material quality, engineering):
- Headline (max 40 chars), 2-3 body sentences, Spec-driven CTA, 3-5 emojis

RULES:
- Apply all voice rules from brand guidelines
- No words from the NEVER list
- CTAs should drive to a build, an upgrade, or community — not just a cart
```

### META-2: Dynamic Creative — Visual & Video Concepts

```
TASK: Describe visual and video concepts for a Meta DCO campaign for {{product_name}}.

DELIVER 3-5 VISUAL CONCEPTS:
- Lighting, angle, and key elements for each
- Reference the brand's visual standard
- Describe the aesthetic: lighting style, texture focus, action vs. detail

DELIVER 1-2 VIDEO CONCEPTS (15-30 sec):
- Pacing and edit style (speed ramping, cuts, transitions)
- Camera angles (ground-level, drone, POV, macro detail)
- VO tone: aligned with brand voice traits

AVOID: Low-quality or generic visuals. Reference the brand's visual NEVER list.
```

### META-3: Retargeting Ad — Warm Audience

```
TASK: Write retargeting ad copy for {{product_name}} targeting warm audiences (site visitors or video viewers who have not yet purchased).

CONTEXT: This person already knows {{brand_name}}. Speak as if you know them.

FORMAT:
- Headline: Reference the specific product or collection they viewed
- Body: 2-3 sentences acknowledging hesitation, then a performance reason to act
- Social proof hook
- Urgency element: limited stock, season, or upcoming event (never price-led)
- CTA: Direct, action-oriented

TONE: Familiar but expert. Peer-to-peer. No NEVER list words. No price-led urgency.
```

### META-4 (DCA): Retargeting — Viewed Product, Not Added to Cart

```
TASK: Create a dynamic ad copy TEMPLATE for Meta's "Viewed Content" retargeting campaign.

TARGET: User viewed {{product_name}} but did not add to cart.

HEADLINE OPTIONS (2 variations — product name pulled dynamically):
A: "Still thinking about {{product_name}}? [Performance benefit CTA]."
B: "That {{product_name}} you checked out? It's ready for [brand promise action]."

PRIMARY TEXT (2 options):
Option A: Acknowledge the browse, connect to brand promise, performance reason to act.
Option B: Connect the product to the aspirational outcome the brand sells.

CALL TO ACTION: "Shop Now" / "View Product" / "[Brand-aligned upgrade CTA]"

TONE: Expert, confident, slightly urging — not pushy. Peer who noticed they haven't upgraded.
EMOJIS: Use 2-3 relevant emojis. No NEVER list words. No price-led urgency.
```

### META-5 (DCA): Retargeting — Added to Cart, Not Purchased

```
TASK: Create a dynamic ad copy TEMPLATE for Meta's "Add to Cart" retargeting campaign.

TARGET: User added {{product_name}} to cart but did not complete purchase.

HEADLINE OPTIONS (2 variations):
A: "Don't leave performance on the table. Your {{product_name}} awaits."
B: "Ready? Complete your {{brand_name}} order."

PRIMARY TEXT (2 options):
Option A: One step away from transformation. Product = confidence to push limits.
  Frame around the ALWAYS list principles.
Option B (with shipping offer): Same as A, plus a logistical bonus framed as convenience, never as a discount.

CALL TO ACTION: "Complete Purchase" / "Finish Order"
TONE: Direct, confident, focused on VALUE OF COMPLETION. NOT discount-led.
EMOJIS: 2-3 relevant. No NEVER list words.
```

### META-6 (DCA): Prospecting — Broad Catalog Promotion

```
TASK: Create a dynamic ad copy TEMPLATE for Meta's broad "Catalog Sales" prospecting campaign targeting cold audiences.

GOAL: Introduce {{brand_name}}'s curated selection to new audiences.
Highlight the Point of Difference: {{point_of_difference}}.

HEADLINE OPTIONS (2 variations):
A: Lead with aspiration + brand promise.
B: Lead with authority + curation claim.

PRIMARY TEXT: Speak to the identity of the target audience. Lead with who they ARE, not a product list. Reference the core promise and reason to believe.

CALL TO ACTION: "Shop Now" / "Discover [Category]"
TONE: Authoritative, aspirational, confident. Cold audience first impression.
EMOJIS: 2-3 relevant. No NEVER list words.
```

---

## KLAVIYO EMAIL

### EMAIL-1: Welcome Series — Email 1

```
TASK: Draft Email 1 of the Welcome Series for new subscribers.

Subject Line: High-energy — hint at elite community, not a newsletter.
Preview Text: Tease the story, not a discount.

Opening: 2-3 sentences. Use a brand-voice hook (story, scenario, or self-deprecating humor). No generic "Welcome to the family!" openers.

Body: Welcome the reader as a peer. Introduce the Core Promise.
Highlight: Expert advice, curated selection, the confidence/experience the brand delivers.

CTA: Drive to exploration, community, or a signature experience — not just the store.
Sign-off: Use the team sign-off style from platform-config.

RULES: No NEVER list words. Apply the quality filter. 200-300 words.
```

### EMAIL-2: Abandoned Cart — Reminder 1

```
TASK: Write an Abandoned Cart Reminder email.

Subject Line: Reference the pain of not having the product, not the cart itself.
Preview Text: Tease the consequence of inaction.

Body:
- Acknowledge what they left: use {{product_name}} dynamic variable
- Peer-to-peer tone — speak to the pain of the weak link / missed upgrade
- Remind them of the brand promise
- Mid-email: Direct link back to cart

CTA: Action-oriented, brand-voiced (not "Complete your purchase")

RULES: No price discounting. No generic "Your cart is waiting!" 150-250 words.
```

### EMAIL-3: Newsletter

```
TASK: Generate content for the recurring brand newsletter.

STRUCTURE — 3 sections:

1. THE LEAD (3-4 sentences):
   A real story, scenario, or insight. Specific and authentic to the brand voice. Self-deprecating humor or earned authority.

2. THE GEAR:
   Highlight {{product_name}} as the brand's recommended solution.
   Include a "Brand Recommendation" — WHY this product, from the brand's POV. Not specs — experience.

3. THE COMMUNITY:
   CTA to engage with the brand's social channels. Tag, share, or join the community.

Total: 250-400 words. Aggressive line breaks. No walls of text. Mobile-first.
```

### EMAIL-4: New Product Launch

```
TASK: Write a new product launch email for {{product_name}}.

Subject: High-energy hype OR fear-of-failure framing (provide both options).

Body:
Para 1: Scenario where this product matters most. Paint the picture.
Para 2: What it IS through what it DOES (experience, not spec sheet).
Para 3: The Brand Recommendation — why this was chosen/built/sourced.
Para 4: 3-5 spec bullets — benefit first, then the spec.

CTA: "Shop {{product_name}}"
TONE: Launch energy with earned authority. 250-350 words.
```

### EMAIL-5: Win-Back Campaign

```
TASK: Write a win-back email for customers who have not purchased in 90+ days.

Subject: Reference time away with brand-voice humor — not drama.

Body:
Para 1: Acknowledge the time gap. Brand-voice humor — not desperate.
Para 2: "Here's what's new since you left" — 2-3 new products or highlights.
Para 3: Re-establish the brand standard and why it matters.

CTA: Invite back with brand-aligned language.
TONE: Like a friend checking in. No desperation. No NEVER list words.
```

---

## SMS

### SMS-1: New Product Drop Alert

```
TASK: Create an SMS alert for a new product drop: {{product_name}}.

Max 160 characters including the link.
Tone: Urgent, high-energy, exclusive.
Content: Announce product, hint at the brand's key benefit/promise.
Include shortened URL. Use 1-2 emojis max.

RULES: No price mention. No generic "Check out our new..." opener.
```

### SMS-2: Exclusive Offer — VIP/Community

```
TASK: Craft an SMS for an exclusive community flash sale or early access offer.

Max 160 characters including link.
Tone: Highly exclusive, appreciative — not salesy.
Content: Thank the community. State the offer. State urgency. Direct link.
Reinforce the exclusivity — community-only, not sent to everyone.
Use 1-2 emojis.
```

---

## GOOGLE ADS

### GOOGLE-1: Responsive Search Ad — Headlines & Descriptions

```
TASK: Generate headlines and descriptions for a Google RSA.
Keyword Group: {{keyword_group}}

HEADLINES (max 30 chars each — 5-7 options):
Mix: keyword-heavy | benefit-led | brand authority | urgency
Focus: Brand pillars and key differentiators

DESCRIPTIONS (max 90 chars each — 3-4 options):
Address: pain points, expertise, premium positioning
Include: performance-focused CTA

RULES: No NEVER list words. Never lead with price or shipping speed.
```

### GOOGLE-2: Shopping Feed — Product Title & Description

```
TASK: Rewrite product title and description for {{product_name}} for Google Shopping.

PRODUCT TITLE (max 70 chars, keyword-rich):
{{brand_name}} + Product Type + Compatible Model/Category + Primary Benefit

PRODUCT DESCRIPTION (200-300 words):
Para 1: Experience first — what does this feel like / enable?
Para 2: Engineering/quality details — materials, construction, advantages
Para 3: Brand Recommendation — why this over alternatives
Close: CTA to view the full product page

TONE: Specialist expertise. Premium positioning. No NEVER list words.
```

### GOOGLE-3: Performance Max — Asset Copy

```
TASK: Generate Performance Max asset copy for {{product_name}}.

HEADLINES (max 30 chars — 15 variations):
Vary: benefit-led, keyword-heavy, RTB, urgency, brand authority

LONG HEADLINES (max 90 chars — 5 variations):
Each should stand alone as a complete brand value proposition

DESCRIPTIONS (max 90 chars — 5 variations)

CALL TO ACTION OPTIONS (5 variations):
Brand-aligned action CTAs.

RULES: High variety. No duplicate language across variations. No NEVER list words.
```

### GOOGLE-4 (DCA): Product Title Optimization

```
TASK: Optimize the product title for {{product_name}} for Google Shopping visibility and brand alignment.

FORMAT: [Brand] + [Product Type] + [Key Features/Benefits] + [Compatibility]
LENGTH: Max 150 characters. Most important info in first 70 chars for mobile.

CONTENT RULES:
- Emphasize brand pillar language and key differentiators
- Include model/category compatibility where relevant
- Lead with brand and most-searched product type
- Use natural search language — how the target audience actually searches

DELIVER:
- 3 title variations (different keyword priority orders)
- Note which performs best for mobile truncation at 70 chars

AVOID: All NEVER list words.
```

### GOOGLE-5 (DCA): Product Description Enhancement

```
TASK: Enhance the product description for {{product_name}} within the Google Shopping feed.

FOCUS: Experience first. Don't list features — explain the benefit to the target audience.

STRUCTURE:
Hook (2-3 sentences): Attention-grabbing opening tied to the brand experience.
  What does this product ENABLE the buyer to do?

Testing/Quality Story (1-2 sentences): How was this vetted? What's the proof?

Engineering Details (2-3 sentences): Technical language appropriate to the category.
  Precision terms, materials, construction methods.

Problems Solved (bullet points, 3-5):
  - No more [specific failure]
  - Eliminates [specific problem]
  - Delivers [specific performance gain]

Reason to Believe: Brand authority statement.

Close / CTA: Link back to product page.

MAX 5000 characters. No NEVER list words.
```

### GOOGLE-6 (DCA): Negative Keyword Generator

```
TASK: Generate 15-20 negative keywords for a Google Shopping campaign.

GOAL: Protect the brand's premium positioning. Prevent ads from showing for searches that signal price-shopping, low quality, or non-buyer intent.

NEGATIVE KEYWORD THEMES:
- Price signals: cheap, budget, affordable, discount, free, clearance
- Quality signals: used, secondhand, broken, damaged, knockoff, replica
- Problem signals: repair, broken, fix, replacement under warranty
- Intent signals: DIY, homemade, build your own
- Competitor terms (review and exclude specific competitor brand names from brand-foundations.md)
- Include all words from the brand's NEVER list as negative keywords

OUTPUT FORMAT:
Phrase match: "keyword"
Exact match: [keyword]

DELIVER:
- 15-20 negative keywords across phrase and exact match types
- Grouped by theme
- Note: review and update quarterly

APPLY TO: All Shopping campaigns and Performance Max campaigns.
```

---

## SHOPIFY

### SHOPIFY-1: Full Product Page

```
TASK: Write a complete Shopify product page for {{product_name}}.

SHORT DESCRIPTION (above the fold):
Capture the brand promise in 1-2 sentences. Experience-first.

LONG DESCRIPTION:
Para 1: Scenario — where/when this product matters most
Para 2: What it IS through what it DOES
Para 3: Engineering/quality details
Para 4: Brand Recommendation — why this was chosen

SPEC SECTION: 3-5 benefit-first bullets (benefit → then the spec)

BRAND RECOMMENDATION SECTION:
The WHY behind the pick, from the brand's expert POV.

SEO META:
- Title tag (max 60 chars): {{brand_name}} + Product + Primary Benefit
- Meta description (max 155 chars): Experience-first hook + CTA

RULES: Product names follow format: Brand + Type + Model/Category + Benefit.
No NEVER list words.
```

### SHOPIFY-2: Collection Page

```
TASK: Write a Shopify collection page introduction for the {{collection_name}} collection.

INTRO (2-3 paragraphs):
Para 1: Why this category matters to the target audience
Para 2: The brand's approach to curating this collection — quality standard, testing
Para 3: Who this collection is for — speak to the specific segment

If applicable, include segment-specific messaging from brand knowledge.

SEO: Include relevant keywords naturally. No keyword stuffing.
```

---

## MASTER TEMPLATES

### MULTIPLY-1: Content Multiplier — 1 Input → 5 Assets

```
TASK: Convert the following into a complete content bundle.
INPUT: {{product_name}} OR {{blog_topic}}

DELIVER ALL 5 ASSETS:

1. PERFORMANCE BLOG (800+ words)
   - Open: Scenario or story hook
   - Body: Technical breakdown through experience
   - Include: "Brand Recommendation" section
   - Include: "When to Call a Professional" warning block (if applicable)
   - Close: CTA to product page or community

2. EMAIL
   - Subject: Fear-of-failure or high-energy (no price leads)
   - Body: Short, punchy, story-driven. 3-5 paragraphs max.
   - CTA: Single, clear, brand-voiced

3. SHORT VIDEO SCRIPT (30-45 seconds)
   - Visual: Brand aesthetic shots
   - VO: Brand voice — confident, expert perspective
   - Pacing: Dynamic edits, speed ramping where appropriate

4. SOCIAL CAPTION (Instagram / Facebook)
   - Line 1: High-energy hook (no generic openers)
   - 3-5 sentences, brand voice, active verbs
   - CTA + social handle + hashtag block

5. CAROUSEL (5 slides)
   - Slide 1: The Hook
   - Slide 2: The Problem
   - Slide 3: The Solution
   - Slide 4: The Result
   - Slide 5: CTA
```

### AUDIT-1: Brand Voice Audit

```
TASK: Rewrite the following draft to align with the brand voice.

INSTRUCTIONS:
- Remove all NEVER list words and patterns
- Elevate vocabulary using the brand's preferred terminology
- Maintain the brand's energy level — do not sanitize the personality
- Apply the quality filter test
- Flag all violations and explain removals
- Provide before/after comparison for major changes

[PASTE DRAFT HERE]
```
