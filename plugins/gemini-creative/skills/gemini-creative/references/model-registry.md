# AI Model Registry

Reference file for the Gemini Creative Engine. Lists all supported models, their capabilities, prompt formats, and selection criteria.

---

## Image Generation Models

### Imagen 3 (Google Gemini)
- **API:** `gemini-2.0-flash` with image generation enabled / Imagen 3 endpoint
- **Strengths:** Photorealistic images, accurate text rendering in images, product photography, brand-accurate color reproduction
- **Limitations:** Less artistic/stylized than Midjourney, fewer creative "surprises"
- **Prompt format:** Structured natural language, very specific descriptions, supports negative prompts
- **Aspect ratios:** 1:1, 3:4, 4:3, 9:16, 16:9
- **Best for:** Ad creative, social media assets, product shots, email headers, e-commerce imagery
- **Brand accuracy:** HIGH — follows color and composition instructions precisely

### DALL-E 3 (OpenAI)
- **API:** OpenAI Images API
- **Strengths:** Creative interpretation, illustration, conceptual art, complex multi-element scenes
- **Limitations:** Less photorealistic than Imagen 3, can over-interpret prompts
- **Prompt format:** Natural language, conversational, benefits from style references
- **Aspect ratios:** 1:1, 16:9, 9:16 (1024×1024, 1792×1024, 1024×1792)
- **Best for:** Conceptual visuals, mood boards, illustrations, abstract brand imagery
- **Brand accuracy:** MEDIUM — interprets creatively, may drift from exact brand specs

### Midjourney
- **API:** Via Discord bot or Midjourney API (if available)
- **Strengths:** Highest aesthetic quality, cinematic lighting, editorial photography feel, consistent style with --sref
- **Limitations:** Less controllable composition, requires style reference for brand consistency
- **Prompt format:** Comma-separated descriptors, parameters at end (--ar, --style, --sref)
- **Aspect ratios:** Any via --ar parameter
- **Best for:** Hero images, brand photography, editorial visuals, campaign key visuals
- **Brand accuracy:** MEDIUM-HIGH — excellent with style references, otherwise interprets freely

---

## Video Generation Models

### Veo 2 (Google Gemini)
- **API:** Gemini API with video generation / Veo 2 endpoint
- **Strengths:** Text-to-video, image-to-video, cinematic quality, natural motion
- **Limitations:** Short durations (5-15s per generation), limited fine control over mid-video actions
- **Prompt format:** Structured scene descriptions, opening frame emphasis, camera movement
- **Durations:** 5s, 10s, 15s per generation (stitch for longer)
- **Best for:** Video ads, social video, product demos, b-roll, motion brand assets
- **Tip:** Describe the opening frame in extreme detail — it anchors the generation

---

## Reasoning / Review Models

### Gemini 2.5 Pro (Google)
- **API:** Gemini API
- **Strengths:** Multimodal reasoning, can analyze images/designs and provide detailed critique
- **Use case:** Design review, mockup feedback, visual direction validation, accessibility checks
- **Not for:** Direct image/video generation

### Claude Opus / Sonnet (Anthropic)
- **API:** Anthropic API
- **Strengths:** Strategic creative thinking, copy-visual integration, structured specifications, brand voice
- **Use case:** Design specs, Canva direction, creative concepts, wireframe descriptions, copy-design alignment
- **Not for:** Direct image/video generation (produces specifications, not pixels)

---

## Model Selection Matrix

| Task | Primary | Compare With | Why |
|------|---------|-------------|-----|
| Meta feed ad (1:1, 4:5) | Imagen 3 | Midjourney | Imagen for accuracy, MJ for aesthetics |
| Google Display banner | Imagen 3 | — | Needs precise text + CTA placement |
| TikTok video ad | Veo 2 | — | Only video-native option |
| Instagram Reel | Veo 2 | — | Short-form video generation |
| Product hero shot | Imagen 3 | Midjourney | Compare realism approaches |
| Brand lifestyle photo | Midjourney | Imagen 3 | MJ excels at editorial feel |
| Email header graphic | Imagen 3 | — | Precise dimensions + text |
| Landing page hero | Midjourney | Imagen 3 | Aesthetic impact matters most |
| Dashboard mockup | Claude (specs) | Gemini Pro (review) | Structure + critique |
| Website mockup | Claude (wireframe) | Imagen 3 (hero visual) | Specs + generated hero |
| Illustration / icon set | DALL-E 3 | — | Best at illustrated styles |
| Mood board | Midjourney | DALL-E 3 | Aesthetic exploration |
| Design review | Gemini 2.5 Pro | Claude | Multimodal analysis |

---

## Multi-Model Parallel Presets

### Preset: "Maximum Options"
Run all connected image models. Best when the creative direction is open and you want to explore.

### Preset: "Photorealistic Comparison"
Imagen 3 + Midjourney. Best when you need photorealistic imagery and want to compare controlled (Imagen) vs. aesthetic (MJ) approaches.

### Preset: "Full Creative Pipeline"
Claude (specs + copy) + Imagen 3 (images) + Veo 2 (video). Best for complete campaign asset generation.

### Preset: "Design + Review"
Claude (design specs) + Gemini 2.5 Pro (review/critique). Best for mockups and wireframes that need validation.
