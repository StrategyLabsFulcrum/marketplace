# Gemini API Configuration Template

Copy this to `brand-intelligence-center/integrations/gemini-config.md` and fill in your settings.

---

## Gemini API Connection
- **API Key:** Configured via environment variable `GEMINI_API_KEY`
- **Project ID:** [your Google Cloud project ID, if applicable]
- **Region:** us-central1

## Default Models
- **Image generation:** imagen-3
- **Video generation:** veo-2
- **Design reasoning/review:** gemini-2.5-pro

## Other Connected Models
- **Claude:** [connected / not connected] — used for design specs, creative concepts
- **DALL-E 3:** [connected / not connected] — used for illustrations, conceptual art
- **Midjourney:** [connected / not connected] — used for hero images, editorial visuals

## Multi-Model Settings
- **Multi-model enabled:** true
- **Default comparison set:** gemini, claude
- **Auto-recommend models:** true (engine suggests best model per task type)

## Generation Preferences
- **Default image aspect ratio:** 1:1
- **Default video duration:** 15s
- **Always generate alternatives:** true (primary + 2 variations per request)
- **Auto-apply brand colors:** true (inject brand palette into every prompt)
- **Save all prompts to session log:** true

## Brand Integration
- **Brand profile source:** brand-intelligence-center/system-prompt.md
- **Visual standards source:** design-system/brand-standards.md
- **Apply NEVER rules to all prompts:** true
