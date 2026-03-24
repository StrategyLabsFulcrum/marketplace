---
name: gemini-generate
description: Generate images or video using Gemini models with brand-aware prompts
---

# /gemini-generate

Generate visual assets using the Gemini Creative Engine.

## Usage

```
/gemini-generate [type] [description]
```

**Type:** `image` | `video` | `mockup`
**Description:** What you want to generate

## Examples

```
/gemini-generate image Product hero shot of our newest coffee blend on a marble countertop
/gemini-generate video 15-second Instagram Reel showing the unboxing experience
/gemini-generate mockup Landing page for our spring sale campaign
```

## What Happens

1. Loads your Gemini API config and brand visual standards
2. Asks which model(s) you want to use (or auto-recommends)
3. Builds optimized prompts grounded in your brand identity
4. Produces primary prompt + 2 alternatives for each asset
5. Logs the session for content library cataloging
