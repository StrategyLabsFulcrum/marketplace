# Variable Glossary

Complete reference for all variables used in prompt templates and brand knowledge files.

## Auto-Populated Variables

These are filled automatically by reading the brand knowledge files. No user input needed at generation time.

| Variable | Source File | Section | Description |
|----------|------------|---------|-------------|
| `{{brand_name}}` | brand-foundations.md | Business Snapshot | Official brand name |
| `{{website_url}}` | brand-foundations.md | Business Snapshot | Primary website URL |
| `{{owner_name}}` | brand-foundations.md | Business Snapshot | Owner/founder name |
| `{{category_description}}` | brand-foundations.md | Business Snapshot | Industry/category phrase |
| `{{tech_stack}}` | platform-config.md | Tech Stack | eCommerce + marketing tools |
| `{{core_promise}}` | brand-foundations.md | Core Positioning | The brand's fundamental value statement |
| `{{target_audience}}` | brand-foundations.md | Four-Wall Framework | Target audience identity |
| `{{category}}` | brand-foundations.md | Four-Wall Framework | Category positioning |
| `{{point_of_difference}}` | brand-foundations.md | Four-Wall Framework | Unique differentiator |
| `{{reason_to_believe}}` | brand-foundations.md | Four-Wall Framework | Proof behind the claim |
| `{{competitors}}` | brand-foundations.md | Competitive Positioning | Competitor names + archetypes + counter-positions |
| `{{brand_pillars}}` | brand-foundations.md | Brand Pillars | 3-5 core brand principles |
| `{{product_segments}}` | key-messages.md | Product Segments | Segment names, RTBs, vocabulary |
| `{{tone_spectrum}}` | voice-guidelines.md | Tone Spectrum | Voice trait definitions |
| `{{never_list}}` | voice-guidelines.md | NEVER List | Prohibited words/phrases/patterns |
| `{{always_list}}` | voice-guidelines.md | ALWAYS List | Required content standards |
| `{{vocabulary}}` | voice-guidelines.md | Vocabulary Reference | Preferred vs. avoided terms |
| `{{quality_filter}}` | voice-guidelines.md | Quality Filter | Pre-publish litmus test |
| `{{taglines}}` | key-messages.md | Core Taglines | Brand taglines |
| `{{power_phrases}}` | key-messages.md | Power Phrases | Reusable phrases with platform guidance |
| `{{content_pillars}}` | content-pillars.md | Content Pillars | Theme definitions |
| `{{content_calendar}}` | content-pillars.md | Calendar Framework | Recurring content schedule |
| `{{social_channels}}` | platform-config.md | Social Channels | Platform URLs |
| `{{team_signoff}}` | platform-config.md | Team & Sign-offs | Email/content sign-off style |

## Per-Use Variables

These are gathered from the user each time content is generated. Previous values should be offered as defaults when available.

| Variable | When Required | Description | Example Values |
|----------|--------------|-------------|----------------|
| `{{product_name}}` | Product-specific content | The specific product being promoted | "Gen 2 Heavy-Duty Tie Rods" |
| `{{collection_name}}` | Collection-level content | The product collection or category | "Suspension Upgrades" |
| `{{blog_topic}}` | Blog/content creation | The subject of the content piece | "Why stock suspension fails at speed" |
| `{{content_goal}}` | When ambiguous | The business objective | "Brand awareness", "Product conversion", "Email capture", "Community signups" |
| `{{platform}}` | Multi-platform commands | The specific platform | "Instagram", "Facebook", "TikTok" |
| `{{tone_angle}}` | Ad variations | The emotional angle | "Pain/fear", "Gain/aspiration", "Technical/spec", "Community", "Educational" |
| `{{funnel_stage}}` | Ads and email | Where the audience is | "Cold (awareness)", "Warm (consideration)", "Hot (retargeting/conversion)" |
| `{{season_or_timing}}` | Seasonal content | Time-relevant context | "Spring season", "Holiday", "New Year", "Summer" |
| `{{keyword_group}}` | Google Ads / SEO | Target keyword cluster | "heavy duty UTV axles", "Can-Am X3 suspension" |
| `{{email_type}}` | Email commands | The type of email | "Welcome", "Abandoned Cart", "Newsletter", "Launch", "Win-Back" |
| `{{draft_content}}` | Brand audit | Content to review | Pasted text to be audited |

## Variable Resolution Order

When generating content, resolve variables in this order:

1. **Read brand knowledge files** → populate all auto variables
2. **Check for previously used per-use values** → offer as defaults
3. **Ask user for required per-use variables** → only what's needed for this specific template
4. **Apply defaults for optional variables** → use smart defaults where the user hasn't specified
5. **Assemble the prompt** → system prompt + template + all resolved variables
