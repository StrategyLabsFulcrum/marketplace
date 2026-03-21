# /content-store

Add approved copy or asset references to the Content Library. Use after a campaign's copy or assets have been approved and are ready for reuse.

## How to Invoke

**Store approved copy:**
```
/content-store copy
```
You will be prompted to provide:
- The copy text (paste it directly)
- Type: Ad copy / Email / Landing page / Social / Brand / SEO
- Channel: Meta / Google / TikTok / LinkedIn / Email / All
- Campaign slug (or "Evergreen")
- Approval status and who approved it
- Tags (the system will suggest based on content analysis)

**Store an asset reference:**
```
/content-store asset
```
You will be prompted for:
- Asset name and file path (in brand-asset-manager storage)
- Type: Photo / Video / Graphic / Illustration / Logo / Icon / Template
- Format and dimensions
- License type and any usage restrictions
- Model release status (if people are in the image)
- Approved channels
- Tags

**Store from a campaign output folder:**
```
/content-store from-campaign 2026-03-spring-launch
```
Crawls the campaign's `copy/` and `creative/design/outputs/` folders and bulk-adds all approved items, prompting for approval status confirmation before indexing.

## What Happens

1. Copy is saved to the appropriate subfolder in `content-library/copy/`
2. Asset references are added to `content-library/assets/index.md`
3. An index entry is created in `content-library/copy/index.md` with a new sequential ID
4. Items are tagged for discoverability
5. Status is set to ✅ Approved (or 🔄 In review if confirmation is pending)

## After Campaigns Run

Use `/content-store` to update performance tags on existing copy:
```
/content-store performance-update COPY-2026-001 high-performer
/content-store performance-update COPY-2026-002 fatigued
```
