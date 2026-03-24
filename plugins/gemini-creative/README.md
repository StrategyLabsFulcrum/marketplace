# Gemini Creative Engine

Connects Google Gemini's native image and video generation to the Strategy Labs creative pipeline. Adds model selection, multi-model comparison, and direct visual asset generation across all design plugins.

## What It Does

1. Detects whether the user has a Gemini API connection configured
2. Exposes model selection — users choose which AI model(s) handle creative generation
3. Generates images via Gemini (Imagen 3) with brand-aware prompts
4. Generates video concepts via Gemini (Veo 2) with storyboard-to-video pipelines
5. Runs multi-model comparison — same brief sent to Gemini + Claude in parallel, user picks the best output
6. Provides structured prompts optimized for each model's strengths

## Model Registry

| Model | Provider | Strengths | Best For |
|-------|----------|-----------|----------|
| Imagen 3 | Google Gemini | Photorealistic images, text rendering in images, product shots | Ad creative, social media, product photography |
| Veo 2 | Google Gemini | Video generation from text/image, cinematic quality | Video ads, social video, product demos |
| Gemini 2.5 Pro | Google Gemini | Multimodal reasoning, design critique, layout analysis | Design review, mockup feedback, creative direction |
| Claude (Sonnet/Opus) | Anthropic | Strategic thinking, copy-design integration, brand voice | Creative concepts, design specs, copy-visual alignment |
| DALL-E 3 | OpenAI | Illustration, conceptual art, creative interpretation | Conceptual visuals, illustrations, mood boards |
| Midjourney | Midjourney | Aesthetic quality, artistic styles, cinematic lighting | Hero images, brand photography, editorial visuals |

## Commands

| Command | What It Does |
|---------|-------------|
| `/gemini-generate` | Generate images or video using Gemini models with brand-aware prompts |
| `/model-select` | Choose which AI model(s) handle creative generation for this session |
| `/multi-model` | Run the same creative brief through multiple models in parallel for comparison |

## Integration

This plugin is consumed by other design plugins in the system:

- **graphic-design** — uses Gemini for AI image generation (replaces/augments generic AI prompts)
- **video-content-strategy** — uses Veo 2 for video concept visualization and storyboard-to-video
- **ux-website-designer** — uses Gemini for mockup generation and design exploration
- **art-director** — uses multi-model comparison during visual direction development

## Setup

Users configure their Gemini API connection in `brand-intelligence-center/integrations/gemini-config.md`:

```markdown
## Gemini API Configuration
- API Key: [configured via environment variable GEMINI_API_KEY]
- Default image model: imagen-3
- Default video model: veo-2
- Default reasoning model: gemini-2.5-pro
- Multi-model enabled: true
- Preferred comparison set: [gemini, claude]
```

## Output Structure

```
campaigns/{{slug}}/creative/gemini/
├── generated-images/
│   ├── {{asset-name}}-gemini-v1.md    (prompt + generation params + result description)
│   └── {{asset-name}}-gemini-v2.md
├── generated-video/
│   ├── {{video-name}}-veo-v1.md       (storyboard + generation params)
│   └── {{video-name}}-veo-v2.md
├── model-comparisons/
│   └── {{brief-name}}-comparison.md   (side-by-side model outputs + selection rationale)
└── gemini-session-log.md              (all prompts, params, and outputs for this campaign)
```

## Dependencies

- **brand-intelligence-center** (required) — brand colors, fonts, visual identity for prompt grounding
- **art-director** (recommended) — visual direction system for prompt alignment
- **content-library** (recommended) — stores approved generated assets for reuse
