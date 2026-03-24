---
name: gemini-creative
description: >
  Generate images and videos using Google's Gemini API (Imagen 4, Gemini Flash Image, Veo 3.1) with model selection and multi-model comparison. Use this skill whenever the user mentions generating images, creating visuals, making videos, AI-generated art, creating brand assets, generating product shots, creating social media visuals, making video content, image generation, video generation, or anything involving creating visual content with AI. Also triggers on 'generate an image of', 'create a video of', 'make me a picture', 'design a visual', 'AI image', 'AI video', 'Gemini image', 'Imagen', 'Veo', 'model select', 'compare models', 'multi-model', or any request to produce visual or video assets for a brand. Also activates when any design plugin needs to produce visual assets via Gemini. Use aggressively — if image or video generation is mentioned at all, use this skill.
version: 1.1.0
allowed-tools: Read, Write, Glob, Grep, Bash
---

# Gemini Creative Engine — AI Image & Video Generation

Generate production-quality images and videos using Google's Gemini API, then save them directly to the right brand asset folder on Google Drive. Supports model selection, multi-model comparison, and brand-aware prompt generation across the full creative pipeline.

You are both a standalone agent (users invoke you directly) and a service layer consumed by other design plugins (graphic-design, video-content-strategy, ux-website-designer, art-director).

## How It Works

This skill uses three generation approaches depending on what the user needs:

1. **Gemini Flash Image** (`gemini-3.1-flash-image-preview`) — Fast, high-quality image generation with text-and-image understanding. Best for creative exploration, iterative design, and image editing. Supports multi-turn conversations.
2. **Imagen 4** (`imagen-4.0-generate-001`) — Google's dedicated image generation model. Best for batch generation (up to 4 images at once) and production-quality output.
3. **Veo 3.1** (`veo-3.1-generate-preview`) — Video generation from text prompts. Produces 4-8 second clips with native audio, cinematic styles, and realistic physics.

---

## Before You Start

### First-Time Setup

The skill needs a Gemini API key stored locally. Check for an existing config:

```bash
cat ~/.gemini-creative-config.json 2>/dev/null
```

If no config exists, ask the user for their API key, then save it:

```bash
cat > ~/.gemini-creative-config.json << 'CONF'
{
  "api_key": "THE_USERS_KEY_HERE"
}
CONF
chmod 600 ~/.gemini-creative-config.json
```

### Install the SDK

```bash
pip install google-genai Pillow --break-system-packages -q
```

---

## Step 1: Model Selection

When a creative task arrives, present the model selection prompt so the user chooses which AI model(s) handle the work:

### Model Selection Prompt

```
## Model Selection

What would you like to handle the creative generation for this task?

### Single Model (Gemini)
1. **Gemini Flash Image** — Fast, iterative, supports image editing and multi-turn (free tier)
2. **Imagen 4** — Batch generation (up to 4 images), production-quality output
3. **Gemini Pro Image** — Highest quality single images
4. **Veo 3.1** — Video generation with native audio, cinematic quality
5. **Veo 3.1 Fast** — Quicker video turnaround

### Multi-Model (parallel runs — more options to choose from)
6. **Gemini + Claude** — Generated visuals from Gemini AND structured design specs from Claude
7. **Gemini + DALL-E** — Compare photorealistic (Gemini) vs. illustrative (DALL-E)
8. **Gemini + Midjourney** — Compare Gemini precision vs. Midjourney aesthetics
9. **All available models** — Maximum options — run every connected model in parallel
10. **Custom combination** — Choose your own set

Your choice (or just describe what you need and I'll recommend): ___
```

### Auto-Recommendation Logic

If the user describes the task without selecting a model, recommend based on:

| Task Type | Recommended Model(s) | Why |
|-----------|---------------------|-----|
| Quick creative image | Gemini Flash Image | Fast, good quality, free tier |
| Multiple variations | Imagen 4 | Batch generation up to 4 |
| Production hero image | Gemini Pro Image | Highest quality |
| Edit existing image | Gemini Flash Image | Supports image input |
| Product photography / packshot | Imagen 4 + Midjourney (compare) | Precision vs. aesthetics |
| Lifestyle imagery / brand photos | Imagen 4 + Midjourney | Compare approaches |
| Ad creative (Meta, Google Display) | Imagen 4 (primary) + Claude (specs) | Images + specifications |
| Video ad / social video | Veo 3.1 + Claude (script) | Video + script |
| Dashboard / data visualization | Claude (specs) + Gemini Pro (review) | Structure + critique |
| Website mockup / wireframe | Claude (structure) + Imagen 4 (hero visuals) | Specs + generated hero |
| Short video clip | Veo 3.1 | Best quality, native audio |
| Fast video preview | Veo 3.1 Fast | Quicker turnaround |

---

## Step 2: Load Brand Context

Before generating any prompt, load visual identity:

1. `brand-intelligence-center/system-prompt.md` — brand colors (hex), fonts, logo rules, voice
2. `design-system/brand-standards.md` — accumulated visual standards (if exists)
3. `campaigns/{{slug}}/creative/design/visual-direction-system.md` — campaign visual direction (if in campaign context)

Extract and hold:
- Brand color palette (hex values)
- Typography stack
- Photography / illustration style preferences
- Brand NEVER rules (visual guardrails)
- Campaign motif (if applicable)

Ask which brand this is for if not obvious from context. This determines where files get saved.

---

## Step 3: Generate the Content

Run the appropriate generation script from this skill's `scripts/` directory. All scripts read the API key from `~/.gemini-creative-config.json` automatically.

### For Images (Gemini Flash Image)

```bash
python {SKILL_DIR}/scripts/generate_image.py \
  --prompt "your detailed prompt here" \
  --output "/path/to/output.png" \
  --model "gemini-3.1-flash-image-preview" \
  --aspect-ratio "16:9" \
  --resolution "1K"
```

Options:
- `--model`: `gemini-3.1-flash-image-preview` (default), `gemini-3-pro-image-preview`, or `gemini-2.5-flash-image`
- `--aspect-ratio`: `1:1`, `3:2`, `4:3`, `9:16`, `16:9`, `4:5`, `5:4`, `3:4`, `21:9`
- `--resolution`: `512`, `1K` (default), `2K`, `4K`

### For Batch Images (Imagen 4)

```bash
python {SKILL_DIR}/scripts/generate_imagen.py \
  --prompt "your detailed prompt here" \
  --output-dir "/path/to/output/directory/" \
  --count 4 \
  --aspect-ratio "16:9" \
  --size "1K"
```

Options:
- `--count`: 1-4 images (default: 4)
- `--aspect-ratio`: `1:1`, `3:4`, `4:3`, `9:16`, `16:9`
- `--size`: `1K` (default), `2K`

### For Videos (Veo 3.1)

```bash
python {SKILL_DIR}/scripts/generate_video.py \
  --prompt "your detailed prompt here" \
  --output "/path/to/output.mp4" \
  --aspect-ratio "16:9" \
  --resolution "1080p" \
  --duration 8
```

Options:
- `--model`: `veo-3.1-generate-preview` (default), `veo-3.1-fast`
- `--aspect-ratio`: `16:9` (default), `9:16`
- `--resolution`: `720p`, `1080p` (default), `4k`
- `--duration`: `4`, `6`, `8` (default, in seconds)

Video generation takes 1-3 minutes. The script polls automatically and saves when ready.

### For Image Editing

```bash
python {SKILL_DIR}/scripts/generate_image.py \
  --prompt "remove the background and replace with a sunset" \
  --input-image "/path/to/source.png" \
  --output "/path/to/edited.png" \
  --model "gemini-3.1-flash-image-preview"
```

---

## Step 4: Brand-Aware Prompt Engineering

When the user gives a brief prompt, enhance it using loaded brand context before sending to the API.

### Image Prompt Architecture

Build prompts using this structure:

```
## Image Generation Brief

**Subject:** [Precise description of what appears in the image]
**Scene/Environment:** [Setting, background, context]
**Composition:** [Framing — tight/medium/wide, rule of thirds, angle, orientation]
**Lighting:** [Quality, direction, color temperature, mood]
**Color Palette:** [Brand colors to emphasize — provide hex values as color descriptions]
  - Primary: [color name matching brand hex]
  - Supporting: [color name]
  - Accent: [color name]
**Style:** [Photorealistic / editorial / lifestyle / product / flat lay]
**Mood/Tone:** [The emotional quality — calm, energetic, premium, approachable]
**Text in Image:** [Any text — Gemini Flash Image handles text rendering well]
**Aspect Ratio:** [1:1 / 4:5 / 9:16 / 16:9 / custom]
**Technical:** [Resolution preference, quality level]

**Brand Guardrails:**
- MUST: [brand requirements from visual standards]
- NEVER: [brand NEVER rules]

**Negative Prompt:** [What to exclude — stock photo feel, specific elements to avoid]
```

### Video Prompt Architecture (Veo 3.1)

```
## Video Generation Brief

**Concept:** [One-sentence video description]
**Duration:** [4s / 6s / 8s]
**Opening Frame:** [What the viewer sees first — this anchors the generation]
**Scene Progression:**
  - Beat 1 (0-Xs): [Description — action, camera, mood]
  - Beat 2 (X-Ys): [Description]
  - Final Frame: [CTA moment or closing visual]
**Camera Movement:** [Static / pan / dolly / drone / handheld / tracking]
**Pacing:** [Slow cinematic / quick-cut energy / steady confident]
**Color Grade:** [Reference brand palette — warm/cool/desaturated/vibrant]
**Style Reference:** [e.g., "like an Apple product video", "like a Nike training ad"]
**Aspect Ratio:** [9:16 vertical / 16:9 horizontal]

**Brand Guardrails:**
- MUST: [brand requirements]
- NEVER: [brand NEVER rules]
```

### Prompt Enhancement Guidelines

- **Subject**: Be specific — vague prompts produce generic images
- **Lighting**: Most important technical variable — describe it first
- **Composition**: Describe explicitly (rule of thirds, centered, tight crop)
- **Brand colors**: Include as descriptive color names alongside hex values
- **Text in image**: Gemini Flash handles text rendering well — include exact text and style
- **Camera movement** (video): Specific descriptions produce better than vague "cinematic"
- **Negative prompts**: Always include — significantly improve output quality

Always tell the user what enhanced prompt you're sending so they can adjust.

### Generate Variations

For every request, produce:
1. **Primary prompt** — the best interpretation of the brief
2. **Alternative A** — different composition or angle
3. **Alternative B** — different mood or style treatment

---

## Step 5: Multi-Model Comparison Mode

When the user selects multi-model or you recommend it:

1. Take the single creative brief
2. Translate it into optimized prompts for each selected model (prompt syntax differs per model)
3. Generate with Gemini models directly via scripts
4. Present prompts for non-Gemini models (DALL-E, Midjourney) for the user to run
5. Present all outputs in a comparison document:

```markdown
## Multi-Model Creative Comparison

### Brief
[The original creative request]

### Model 1: Gemini Imagen 4
**Optimized prompt:** [prompt tailored to Imagen 4]
**Generated:** [file path to generated image(s)]
**Strengths of this output:** [what Imagen 4 did well here]

### Model 2: [Second model]
**Optimized prompt:** [prompt tailored to this model's syntax]
**Expected output:** [description of likely result]
**How to generate:** [instructions for DALL-E/Midjourney if not auto-generated]

---

### Recommendation
**Best single model for this brief:** [model] — because [reason]
**Best combination:** [models] — because [reason]
```

---

## Step 6: Design Plugin Integration Protocol

When called by another plugin (graphic-design, art-director, video-content-strategy, ux-website-designer), follow this protocol:

### Receiving a Brief from Another Plugin

The calling plugin passes:
- **Asset type** (image / video / mockup / dashboard visual)
- **Brief content** (the design brief or visual direction)
- **Format specs** (dimensions, aspect ratio, platform)
- **Brand context loaded** (yes/no — if no, load it yourself)
- **Model selection** (from Art Director's Step 4b, if set)

### Returning to the Calling Plugin

Return a structured output block:

```markdown
## Gemini Creative Output

**Request:** [what was asked for]
**Model used:** [model name]
**Generated files:** [file paths to generated assets]
**Generation prompts used:**

[Full prompt(s)]

**Post-generation notes:**
- [Any refinement suggestions]
- [How to iterate if the first generation isn't right]

**File naming:** {{brand}}_{{slug}}_{{format}}_{{model}}_v{{n}}
```

---

## Step 7: Save to the Right Place

Generated assets should be saved to the brand's Google Drive asset folder. The standard path convention is:

```
[Brand Name]/Assets/AI-Generated/[type]/[descriptive-filename].[ext]
```

Where `[type]` is `images/` or `videos/`.

Since the user has Google Drive Desktop, these folders are accessible as local paths.

**File naming convention**: Use descriptive, lowercase, hyphenated names with the date:
```
hero-banner-sunset-mountains-2026-03-23.png
product-showcase-rotating-bottle-2026-03-23.mp4
```

For campaign assets, also save to the campaign folder:
```
campaigns/{{slug}}/creative/gemini/
├── generated-images/
│   ├── {{asset-name}}-v1.png
│   └── {{asset-name}}-v2.png
├── generated-video/
│   ├── {{video-name}}-v1.mp4
│   └── {{video-name}}-v2.mp4
└── model-comparisons/
    └── {{brief-name}}-comparison.md
```

---

## Step 8: Present Results & Session Logging

After generation:
1. Show the user the generated image inline (for images) or confirm the video file location
2. Share a `computer://` link to the output file
3. Ask if they want refinements — for images, you can use multi-turn conversation mode to iterate

Log every generation session to `campaigns/{{slug}}/creative/gemini/gemini-session-log.md`:

```markdown
## Session: {{date}}

### Request
[What was asked]

### Model(s) Used
[Model selection and rationale]

### Prompts Generated
[All prompts with parameters]

### Outputs
[File paths and descriptions of generated assets]

### User Selection
[Which output was chosen, any refinement notes]
```

---

## Error Handling

- **API key invalid**: Re-prompt the user and update `~/.gemini-creative-config.json`
- **Rate limited**: Wait and retry, or suggest switching to a different model
- **Safety filter blocked**: Let the user know their prompt was flagged and suggest rewording
- **Video generation timeout**: Veo can take up to 5 minutes — increase the poll timeout

---

## Prompt Optimization Notes by Model

### Gemini Flash Image Tips
- Fast iteration — use multi-turn for refinement
- Handles text-in-image well
- Supports image editing (pass existing image + edit prompt)
- Good for creative exploration before committing to Imagen 4 batch

### Imagen 4 Tips
- Best for final production images — batch 4 variations at once
- Be extremely specific about subject positioning and composition
- Include brand colors as descriptive color names, not just hex codes
- Negative prompts significantly improve output

### Veo 3.1 Tips
- Describe the opening frame in extreme detail — it anchors the generation
- Camera movement descriptions produce better results than vague "cinematic"
- Native audio generation included — describe sound/music style
- Keep to single clear visual idea per generation — stitch for longer videos

### Claude Tips (Design Specs)
- Claude excels at structured specifications — Canva direction, wireframes, design specs
- Claude integrates copy and visual direction better than any image model
- Use Claude to write the brief, then send to Gemini for generation

### DALL-E 3 Tips
- Excels at creative interpretation — good for conceptual and illustrative work
- Less photorealistic than Imagen 4 — better for stylized or artistic outputs
- Handles complex scenes with multiple elements well

### Midjourney Tips
- Strongest aesthetic quality for photography-style outputs
- Use style references (--sref) for consistent brand aesthetics
- Best for hero images and editorial-quality brand photography
