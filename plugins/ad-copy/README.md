# Ad Copywriter

Writes paid advertising copy for Meta, Google Ads, TikTok, LinkedIn, and Pinterest. Specialist agent — receives briefs from the Creative Director and produces platform-specific copy variants within character limits, structured around approved hook angles and the brand voice.

## What It Does

1. Loads brand voice from brand-intelligence-center
2. Reads the Ad Copywriter brief from the Creative Director
3. Writes 3+ complete ad variants per hook angle for each platform in scope
4. Self-reviews against brand NEVER rules and character limits
5. Delivers formatted copy with variant labels and character counts

## Platforms Covered

| Platform | Formats |
|---------|---------|
| Meta (Facebook/Instagram) | Feed (static/video), Stories, Carousel, Lead Ads |
| Google Ads | Responsive Search Ads (RSA), Performance Max assets |
| TikTok | In-Feed, TopView, caption + on-screen text + voiceover |
| LinkedIn | Single Image, Carousel, Message Ads, Conversation Ads |
| Pinterest | Promoted Pins |

## Output

`campaigns/{{slug}}/creative/copy/ad-copy.md`

Every ad labeled: platform, format, hook angle, variant number, and character counts per field.

## Dependencies

- **brand-intelligence-center** (required) — brand voice, NEVER rules, campaign line
- **creative-director** (spawns this agent) — brief with hook angles, audience, offer, platforms
