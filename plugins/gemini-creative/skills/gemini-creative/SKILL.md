---
name: gemini-creative
description: "Generate images and videos using Google's Gemini API (Imagen 4, Gemini Flash Image, Veo 3.1). Use this skill whenever the user mentions generating images, creating visuals, making videos, AI-generated art, creating brand assets, generating product shots, creating social media visuals, making video content, image generation, video generation, or anything involving creating visual content with AI. Also triggers on 'generate an image of', 'create a video of', 'make me a picture', 'design a visual', 'AI image', 'AI video', 'Gemini image', 'Imagen', 'Veo', or any request to produce visual or video assets for a brand. Use aggressively — if image or video generation is mentioned at all, use this skill."
---

# Gemini Creative — AI Image & Video Generation

Generate production-quality images and videos using Google's Gemini API, then save them directly to the right brand asset folder on Google Drive.

## How It Works

This skill uses three generation approaches depending on what the user needs:

1. **Gemini Flash Image** (`gemini-3.1-flash-image-preview`) — Fast, high-quality image generation with text-and-image understanding. Best for creative exploration, iterative design, and image editing. Supports multi-turn conversations.
2. **Imagen 4** (`imagen-4.0-generate-001`) — Google's dedicated image generation model. Best for batch generation (up to 4 images at once) and production-quality output.
3. **Veo 3.1** (`veo-3.1-generate-preview`) — Video generation from text prompts. Produces 4-8 second clips with native audio, cinematic styles, and realistic physics.

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

## Workflow

### Step 1: Understand the Request

Determine what the user wants:
- **Image generation** — use Gemini Flash Image for single creative images, or Imagen 4 for batch generation
- **Image editing** — use Gemini Flash Image (pass existing image + editing prompt)
- **Video generation** — use Veo 3.1
- **Iterative refinement** — use Gemini Flash Image in multi-turn mode

Ask which brand this is for if not obvious from context. This determines where files get saved.

### Step 2: Generate the Content

Run the appropriate generation script from this skill's `scripts/` directory. All scripts read the API key from `~/.gemini-creative-config.json` automatically.

#### For Images (Gemini Flash Image)

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

#### For Batch Images (Imagen 4)

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

#### For Videos (Veo 3.1)

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

#### For Image Editing

```bash
python {SKILL_DIR}/scripts/generate_image.py \
  --prompt "remove the background and replace with a sunset" \
  --input-image "/path/to/source.png" \
  --output "/path/to/edited.png" \
  --model "gemini-3.1-flash-image-preview"
```

### Step 3: Save to the Right Place

Generated assets should be saved to the brand's Google Drive asset folder. The standard path convention is:

```
[Brand Name]/Assets/AI-Generated/[type]/[descriptive-filename].[ext]
```

Where `[type]` is `images/` or `videos/`.

Since the user has Google Drive Desktop, these folders are accessible as local paths. Use `request_cowork_directory` if you don't already have filesystem access, or save to the Cowork outputs folder and let the user know where files are.

**File naming convention**: Use descriptive, lowercase, hyphenated names with the date:
```
hero-banner-sunset-mountains-2026-03-23.png
product-showcase-rotating-bottle-2026-03-23.mp4
```

### Step 4: Present Results

After generation:
1. Show the user the generated image inline (for images) or confirm the video file location
2. Share a `computer://` link to the output file
3. Ask if they want refinements — for images, you can use multi-turn conversation mode to iterate

## Prompt Engineering Tips

When the user gives a brief prompt, enhance it before sending to the API. Good image prompts include:
- **Subject**: What's in the image
- **Style**: Photography, illustration, watercolor, 3D render, etc.
- **Lighting**: Natural, studio, golden hour, dramatic, etc.
- **Composition**: Close-up, wide angle, overhead, etc.
- **Mood/Tone**: Vibrant, moody, minimal, warm, etc.

For video prompts, also include:
- **Camera movement**: Pan, zoom, dolly, static, etc.
- **Pacing**: Slow motion, time-lapse, real-time, etc.

Always tell the user what enhanced prompt you're sending so they can adjust.

## Model Selection Guide

| Need | Recommended Model | Why |
|------|------------------|-----|
| Quick creative image | Gemini Flash Image | Fast, good quality, free tier |
| Multiple variations | Imagen 4 | Batch generation up to 4 |
| Production hero image | Gemini Pro Image | Highest quality |
| Edit existing image | Gemini Flash Image | Supports image input |
| Short video clip | Veo 3.1 | Best quality, native audio |
| Fast video preview | Veo 3.1 Fast | Quicker turnaround |

## Error Handling

- **API key invalid**: Re-prompt the user and update `~/.gemini-creative-config.json`
- **Rate limited**: Wait and retry, or suggest switching to a different model
- **Safety filter blocked**: Let the user know their prompt was flagged and suggest rewording
- **Video generation timeout**: Veo can take up to 5 minutes — increase the poll timeout
