---
name: model-select
description: Choose which AI model(s) handle creative generation for this session
---

# /model-select

Set which AI model(s) handle creative generation for your current session or as a new default.

## Usage

```
/model-select                    → interactive model picker
/model-select gemini             → set Gemini Imagen 3 as default for images
/model-select gemini+claude      → parallel mode: specs from Claude, visuals from Gemini
/model-select all                → run all connected models for maximum options
```

## Available Models

| Model | Provider | Type | Best For |
|-------|----------|------|----------|
| `gemini` / `imagen` | Google | Image generation | Product shots, ad creative, photorealistic |
| `veo` | Google | Video generation | Video ads, social video, product demos |
| `gemini-pro` | Google | Reasoning / review | Design critique, mockup feedback |
| `claude` | Anthropic | Specs / concepts | Design specs, creative direction, copy-visual |
| `dalle` | OpenAI | Image generation | Illustrations, conceptual art |
| `midjourney` | Midjourney | Image generation | Hero images, editorial, cinematic |

## Multi-Model Syntax

Combine models with `+`:
```
/model-select gemini+dalle        → compare photorealistic vs. illustrative
/model-select gemini+midjourney   → compare two photorealistic approaches
/model-select gemini+claude+dalle → triple comparison
```

## Persistence

- **Session default:** Applies to all generation commands in this conversation
- **Permanent default:** Add `--save` to update your gemini-config.md
