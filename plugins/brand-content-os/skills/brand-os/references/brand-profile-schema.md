# Brand Profile Schema

Complete schema for all brand knowledge areas. Use this as the blueprint for `/brand-setup` and `/brand-import`.

## Area 1: Business Snapshot

**File**: `brand-foundations.md` (top section)

| Field | Required | Description | Example |
|-------|----------|-------------|---------|
| Business Name | Yes | Official brand name | "Rugged Terrain" |
| Website | Yes | Primary URL | "ruggedterrain.com" |
| Owner / Founder | No | Key leadership name(s) | "Kory Kendrick" |
| Annual Revenue Range | No | Approximate scale | "~$1,000,000" |
| Platform / Tech Stack | No | eCommerce platform, email tool, etc. | "Shopify + Klaviyo" |
| Team | No | Key team members and roles | "Kory (Owner), Lauren (Marketing)" |
| Industry / Category | Yes | What space the brand operates in | "High-end UTV performance parts" |

## Area 2: Core Positioning

**File**: `brand-foundations.md`

### Core Promise
One statement that captures the brand's fundamental value. Not a tagline — the internal truth.

**Prompt to gather**: "If you could only say one sentence to a potential customer about what your brand really delivers, what would it be?"

### Four-Wall Positioning Framework

| Element | Question to Ask |
|---------|----------------|
| Target Audience | "Who is your ideal customer? Not demographics — describe their mindset, identity, and what they care about." |
| Category | "How would you describe what you sell in one phrase? Not just the product — the experience or category." |
| Point of Difference | "What makes you fundamentally different from every competitor? The thing only you can claim." |
| Reason to Believe | "Why should someone believe your difference claim? What proof or experience backs it up?" |

## Area 3: Competitive Positioning

**File**: `brand-foundations.md`

For each major competitor (recommend 3-5):

| Field | Description |
|-------|-------------|
| Competitor Name | The brand name |
| Their Archetype | How they position themselves (1-3 word label) |
| Counter-Position | How this brand is fundamentally different (1-2 sentences) |

**Prompt to gather**: "Who are your 3 biggest competitors? For each one, how would you describe their approach in a few words, and what makes your brand the opposite or alternative?"

## Area 4: Brand Pillars

**File**: `brand-foundations.md`

3-5 brand pillars. Each pillar should have:

| Field | Description |
|-------|-------------|
| Pillar Name | Short, memorable label |
| Description | 1-2 sentences explaining what it means |
| In Practice | How this shows up in content and customer experience |

**Prompt to gather**: "What are the 3-5 non-negotiable principles that define everything your brand does? These should be beliefs, not product features."

## Area 5: Voice & Tone

**File**: `voice-guidelines.md`

### Tone Spectrum

Define 4-6 voice traits on a spectrum:

| Field | Description |
|-------|-------------|
| Trait | The dimension of voice (Authority, Energy, Humor, etc.) |
| The Approach | Where the brand sits on this spectrum |
| In Practice | What this sounds like in actual content |

### The NEVER List

Words, phrases, and patterns the brand must NEVER use. These are absolute guardrails.

**Prompt to gather**: "What words or phrases would make you cringe if they appeared in your marketing? What tone or language is completely off-brand? Think about what your worst competitor sounds like — what should you never sound like?"

### The ALWAYS List

Patterns and principles that should appear in EVERY piece of content.

**Prompt to gather**: "What rules should apply to every single piece of content you publish? These are the non-negotiable standards."

### Vocabulary Reference

| Use This | Not This | Why |
|----------|----------|-----|
| Preferred term | Avoided term | Brief reasoning |

**Prompt to gather**: "Are there specific words your brand prefers over common alternatives? Words that feel right vs. words that feel generic?"

### Quality Filter

A litmus test applied before publishing. 1-3 questions that content must pass.

**Prompt to gather**: "If you had to write a quick checklist to decide whether content is 'on-brand enough' to publish, what would the 2-3 test questions be?"

## Area 6: Product Segments

**File**: `key-messages.md`

For brands with distinct product lines, categories, or customer segments:

| Field | Description |
|-------|-------------|
| Segment Name | The product line or category |
| Core RTB | The key "reason to believe" for this segment |
| Key Vocabulary | Segment-specific terms and language |

**Prompt to gather**: "Do you have distinct product lines or categories that each need their own messaging angle? What are they, and what's the key selling point for each?"

## Area 7: Key Messages & Power Phrases

**File**: `key-messages.md`

### Core Taglines
3-6 brand taglines that can be used across channels.

### Power Phrases
Reusable phrases with guidance on where they work best:

| Phrase | Use It For | Best Platforms |
|--------|-----------|----------------|
| The phrase | What context | Where it works |

**Prompt to gather**: "What are the phrases, taglines, or lines that best capture your brand? Include any that have worked well in the past."

## Area 8: Content Pillars

**File**: `content-pillars.md`

3-6 content themes that organize the editorial calendar:

| Field | Description |
|-------|-------------|
| Pillar Name | Short label |
| Core Purpose | What this content achieves |
| Primary Emotion | What the audience should feel |
| Example Topics | 2-3 example content ideas |

### Content Calendar Framework

A repeating weekly or monthly calendar structure:

| Week/Day | Content Theme | Product Focus | Email Hook | Social Angle |
|----------|--------------|---------------|------------|--------------|

**Prompt to gather**: "What are the main themes or categories your content should rotate through? Think about the different reasons someone engages with your brand."

## Area 9: Platform Configuration

**File**: `platform-config.md`

### Social Channels

| Platform | URL | Primary Use |
|----------|-----|-------------|
| Instagram | URL | Visual storytelling |
| Facebook | URL | Community, ads |
| etc. | | |

### Tech Stack

| Tool | Purpose |
|------|---------|
| Shopify | eCommerce |
| Klaviyo | Email/SMS |
| etc. | |

### Team & Sign-offs

| Name | Role | Sign-off Style |
|------|------|---------------|
| Name | Their role | How they sign emails/posts |

## Area 10: AI System Prompt

**File**: `system-prompt.md`

This file is AUTO-GENERATED from the other brand files. It assembles a master system prompt that gets prepended to every content generation request.

### Assembly Template

```
Act as the Lead Content Strategist for {{brand_name}} ({{website_url}}), a {{category_description}}.

BRAND IDENTITY:
{{core_promise}}
{{point_of_difference}}
{{target_audience_description}}

BRAND PILLARS:
{{brand_pillars_formatted}}

SOCIAL CHANNELS:
{{social_channels_formatted}}

VOICE RULES:
{{always_list_formatted}}

NEVER USE:
{{never_list_formatted}}

COMPETITIVE GUARDRAIL:
{{competitive_positioning_formatted}}

VOCABULARY:
{{vocabulary_formatted}}

QUALITY FILTER:
{{quality_filter}}
```

The system prompt should be regenerated whenever brand knowledge files are updated.
