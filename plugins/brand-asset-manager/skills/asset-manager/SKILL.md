---
name: asset-manager
description: >
  Brand Asset Manager for building and maintaining a structured, searchable asset library.
  Use when the user mentions "organize assets", "asset library", "asset setup", "brand photos",
  "brand videos", "photo organization", "image catalog", "content library", "asset management",
  "organize images", "rename photos", "tag assets", "find photos", "search assets",
  "new asset workflow", "inbox folder", "add photos", "add videos", "asset folder structure",
  or wants to build, populate, or maintain a structured library of brand visual content.
---

# Brand Asset Manager

A three-phase system for building and maintaining a structured, searchable brand asset library. Handles setup from scratch, initial organization, and an ongoing inbox-based workflow for adding new assets.

---

## Four-Phase System

### Phase 0 — Apple Photos Import (`/import-from-photos`) *(optional)*
Pull photos and videos directly from Apple Photos into `_inbox/` — by album, date range, keyword, person, or favorites. Uses the `osxphotos` Python library. Originals in Photos are never modified. After import, flows directly into Phase 3.

### Phase 1 — Setup (`/asset-setup`)
Build the folder structure BEFORE assets exist. Interview the brand, propose a custom folder structure, get approval, then create it. Leaves the brand with a ready-to-fill library and a permanent `_inbox/` drop zone.

### Phase 2 — Initial Organization (`/organize-assets`)
Analyze a folder of unorganized existing assets in batches. For each batch, generate an HTML visual review page with embedded thumbnails — user reviews, reports decisions back, then Claude executes. After approval, copies assets with descriptive names, embeds EXIF/IPTC metadata into each JPEG, and updates the catalog.

### Phase 3 — Ongoing Inbox Workflow (`/add-assets`)
The permanent ongoing workflow. Drop new assets into `_inbox/` (or import from Photos with `/import-from-photos`) → run `/add-assets` → choose batch size → review HTML pages → approve → organized, tagged, and cataloged. Inbox cleared after processing.

---

## Core Principles

1. **Analyze first, act second** — Never copy, rename, or move anything until assets are analyzed and the HTML review page is presented.
2. **Human-in-the-loop approval** — Every asset goes through a visual review page. Nothing is renamed or moved until the user explicitly approves it by number.
3. **File handling mode (user's choice)** — Set once during `/asset-setup` and stored in `brand-assets/asset-config.md`. Two modes:
   - **Duplicate (non-destructive):** Organized copies go to `brand-assets/` with new names. Originals stay exactly where they are — untouched, original names preserved.
   - **Move and rename:** Files are relocated from their source into `brand-assets/` with new names. Source location is cleared of approved files.
   The setting applies consistently across all sessions. It is never changed implicitly — only when the user explicitly asks.
4. **Photos library is read-only** — `/import-from-photos` only copies files out of Apple Photos into `_inbox/`. The Photos library itself is never written to, modified, or deleted from.
5. **Metadata lives in the file** — Every approved JPEG gets EXIF + IPTC metadata embedded directly, making it searchable in Finder, Spotlight, Adobe Bridge, and any DAM tool — independent of the catalog files.
6. **Inbox is permanent** — `_inbox/` is always created as part of setup and is the standard drop zone for all new assets going forward.
7. **Catalog always updated** — Every approve/organize action regenerates all catalog formats: `.xlsx`, `.json`, and `.md`.
8. **Session learning** — As assets are approved during a session, build an internal reference so later suggestions are more confident and can reference previously approved assets.

---

## Brand Context Integration

Before organizing assets, check for a `brand-knowledge-center/` folder.

### If brand knowledge exists:
Read these files:
1. `brand-identity.md` — brand pillars, visual identity, product lines, colors
2. `audience-messaging.md` — audience segments, content pillars, channel strategy
3. `digital-ecosystem.md` — active platforms and channels
4. `business-overview.md` — industry, product types

Use brand colors for the HTML review page styling. Use brand context to inform category suggestions, channel recommendations, and descriptions.

### If brand knowledge does NOT exist:
Ask the user:
1. What does your brand sell?
2. What channels do you publish on?
3. What types of content do you shoot?
4. Any specific product lines or collections?
5. What are your brand colors? (hex codes — used for the review page)

---

## Batch Size Control

At the start of every organize or add-assets session, after scanning the inbox or source folder, ask the user their preferred batch size:

> "Found **[X] photos** and **[Y] videos**. How many would you like to review per batch?
> - **5 at a time** — Small, focused batches
> - **10 at a time** — Good balance of speed and control *(recommended)*
> - **20 at a time** — Faster, for large inboxes
> - **Custom** — I'll specify a number"

Remember the user's answer for the entire session. Do not ask again unless the user requests a change.

---

## HTML Visual Review Pages

For each batch, generate a **self-contained HTML review page** saved to `brand-assets/` (e.g., `brand-assets/review-batch-01.html`). Use Python to base64-encode each image so the page works fully offline.

### Python: Base64 Encoding Images

```python
import base64

def encode_image(filepath):
    with open(filepath, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    ext = filepath.rsplit(".", 1)[-1].lower()
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp", "gif": "gif"}.get(ext, "jpeg")
    return f"data:image/{mime};base64,{b64}"
```

For video files (.mp4, .mov, etc.), do not embed the video — show a placeholder card with a video icon and the filename instead.

### Review Page Structure

Each card in the HTML page must show:
- **Asset number** (e.g., #1 of 10) and original filename
- **Thumbnail** — base64-embedded image (or video placeholder icon)
- **Suggested Name** — proposed descriptive filename following the naming convention
- **Category** — proposed folder path
- **Description** — full searchable description
- **Tags** — comma-separated keywords
- **Suggested Use** — recommended channels/placements
- **Quality** — High / Medium / Low with a brief reason
- **⚠️ Uncertainty flag** — if anything is ambiguous, flag it with a specific question (e.g., "⚠️ I can see a product but I'm not sure which colorway — please clarify")
- **Duplicate flag** — if similar to an existing asset, note it: "Similar to `[existing-file.jpg]` already in your library"

### Review Page Layout Requirements

- Clean card layout — thumbnail on the left (or top on mobile), metadata on the right
- Clear visual separation between cards
- **Legend at the top**: "Review each asset below. When done, come back to chat and reply with your decisions: **Approve all**, or list asset numbers with **Edit / Skip / Delete** and any corrections."
- Use brand colors from `brand-identity.md` if available; otherwise use neutral dark theme (#1a1a2e background, #4f8ef7 accent, #e2e8f0 text)
- Fully self-contained — no external CSS, JS, or font dependencies
- Include a summary bar at the top: total assets in batch, counts by proposed category

### Decision Processing

After the user reports decisions:
- **Approved** — copy to organized folder with new name, embed EXIF/IPTC metadata, log to all catalogs
- **Edited** — ask what to change, apply correction, then process as approved
- **Skipped** — leave in `_inbox/`, do not log, note in session
- **Delete** — move to `_delete/` folder with original name (never actually delete files)

After all decisions for a batch are processed, move to the next batch.

---

## Session Learning

As assets are approved during a session, maintain an internal reference table:

```
category → list of approved assets in that category this session
subject tags → what subjects have been confirmed
uncertain flags resolved → corrections the user gave (apply to future similar assets)
```

Use this to improve confidence and descriptions for later batches:

- If 10 flat-lay product shots have been approved, the 11th suggestion should be very confident — no ⚠️ flag
- If the user corrected "outdoor" to "rooftop" for a specific shot, apply that to similar shots going forward
- Reference prior approved assets in descriptions: "Similar composition to `lifestyle-outdoor-morning-run-03.jpg` you approved earlier"
- Reduce repetitive uncertainty flags — if the user has already clarified an ambiguous subject type, don't flag it again

---

## Asset Analysis

### Photo Analysis

For each image file (.jpg, .jpeg, .png, .webp, .heic, .tiff):

1. **Subject identification** — What's in the photo?
2. **Product recognition** — Brand products visible, identified by name/type
3. **Shot type** — Close-up, mid-range, wide, flat lay, overhead, lifestyle, candid, posed
4. **Setting/location** — Studio, outdoor, indoor, urban, nature, etc.
5. **Mood/tone** — Adventurous, cozy, energetic, minimal, bold, warm, rugged
6. **Lighting** — Natural, studio, golden hour, overcast, dramatic
7. **Composition quality** — Is this usable for marketing? Flag blurry or poorly lit images
8. **Color palette** — Dominant colors, alignment with brand colors
9. **People** — Present? How many? Activity?
10. **Seasonality** — Does this feel seasonal?

### Video Analysis

For each video file (.mp4, .mov, .avi, .mkv, .webm):

1. **Duration** — Length of the video
2. **Content summary** — What happens? Key scenes
3. **Subjects** — Products, people, locations featured
4. **Shot types** — Static, handheld, drone, slow-motion, timelapse
5. **Audio** — Music, voiceover, natural sound, silent
6. **Mood/tone**
7. **Thumbnail candidates** — 2-3 strong frames with timestamps
8. **Platform fit** — Aspect ratio and length suggest platforms

### Description Format

```
Subject: [what's in the asset]
Shot Type: [close-up / mid-range / wide / flat lay / overhead]
Mood: [adventurous / cozy / energetic / minimal / bold / warm]
Lighting: [natural / studio / golden hour / overcast / dramatic]
Seasonality: [fall / winter / spring / summer / evergreen]
Tags: [comma-separated keywords]
Suggested Use: [platforms and placements]
Quality: [High / Medium / Low] — [brief reason]
```

---

## File Naming Convention

Original files are never modified. Copies in the organized structure use descriptive names.

**Pattern:** `{category}-{subject}-{detail}-{sequence}.{ext}`

| Original | Renamed |
|----------|---------|
| IMG_4392.jpg | lifestyle-flannel-mountain-trail-01.jpg |
| DSC_0012.jpg | product-flatlay-workman-flannel-charcoal-01.jpg |
| MVI_8834.mp4 | video-lifestyle-fall-lookbook-01.mp4 |

**Rules:**
1. All lowercase, hyphens between words
2. No spaces, underscores, or special characters
3. Category prefix matches the folder it lives in
4. Subject describes what's in the asset
5. Detail adds specificity (product name, color, location)
6. Two-digit sequence number at the end — check existing files in the target folder before assigning
7. Preserve original file extension
8. Maximum 60 characters for filename (excluding extension)

---

## EXIF/IPTC Metadata Embedding

Every approved JPEG gets metadata embedded directly into the file using EXIF + IPTC fields. This makes the asset searchable in Finder, Spotlight, Adobe Bridge, Lightroom, and any DAM tool — independent of the catalog files.

Run this **after renaming the file, before moving it** to the organized folder.

### Python: Embed Metadata

```python
import piexif
from iptcinfo3 import IPTCInfo
import os

def embed_asset_metadata(filepath, title, description, keywords):
    """
    Embeds metadata directly into a JPEG file.
    - filepath    : path to the renamed JPEG (before moving to organized folder)
    - title       : standardized filename without extension
    - description : full searchable description string
    - keywords    : list of keyword strings
    """
    # 1. EXIF fields (readable by Windows, most tools)
    try:
        exif_dict = piexif.load(filepath)
    except Exception:
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}}

    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = description.encode("utf-8")
    exif_dict["0th"][piexif.ImageIFD.XPTitle]          = (title + "\x00").encode("utf-16-le")
    exif_dict["0th"][piexif.ImageIFD.XPKeywords]       = (";".join(keywords) + "\x00").encode("utf-16-le")
    exif_dict["0th"][piexif.ImageIFD.XPComment]        = (description + "\x00").encode("utf-16-le")
    piexif.insert(piexif.dump(exif_dict), filepath)

    # 2. IPTC fields (readable by Spotlight, Adobe, most DAM tools)
    info = IPTCInfo(filepath, force=True)
    info["keywords"]         = [k.encode("utf-8") for k in keywords]
    info["caption/abstract"] = description.encode("utf-8")
    info["object name"]      = title.encode("utf-8")
    info.save_as(filepath)

    # Remove temp file created by iptcinfo3
    junk = filepath + "~"
    if os.path.exists(junk):
        os.remove(junk)

    print(f"✓ Metadata embedded: {os.path.basename(filepath)}")
```

### Auto-Generating Keywords

Build keywords from the asset's metadata. Always include:
- Brand name (slug format, e.g., `acme-brand`)
- Category (lowercase): `product`, `lifestyle`, `video`, `ugc`, etc.
- Subject words (split on hyphens from the filename): `flannel`, `mountain`, `trail`
- Shot type: `flat-lay`, `lifestyle`, `close-up`
- Season if applicable: `fall`, `winter`
- Mood tags: `adventurous`, `cozy`, `bold`
- Channel suggestions: `instagram`, `meta-ads`, `email`

Example: `lifestyle-flannel-mountain-trail-01.jpg` → `['acme-brand', 'lifestyle', 'flannel', 'mountain', 'trail', 'outdoor', 'fall', 'adventurous', 'instagram', 'meta-ads']`

### When NOT to Embed

- **Video files** — piexif/iptcinfo3 only support JPEG; skip for video
- **PNG/WEBP files** — note in catalog that metadata was not embedded
- **Files moved to `_delete/`** — do not embed
- **Skipped files** — do not embed

---

## Duplicate Detection

### Exact Duplicates
- Same file size AND same dimensions = likely exact duplicate
- Flag on the HTML review card before user approves

### Near Duplicates
- Same subject, very similar composition, same shoot session
- Flag with: "Similar to `[existing-file.jpg]` already in your library — keep as alternate version?"

### Duplicate Rules
1. **Never auto-delete** — always flag on review card and let the user decide
2. Move files the user marks as Delete to `_delete/` with original names
3. Mark duplicates in catalog with `duplicate: true` and link to the kept version
4. When adding new assets, load the existing catalog first to check against it

---

## Catalog Formats

All three catalog files are regenerated after every batch is processed.

### 1. Excel Spreadsheet (`asset-manifest.xlsx`)

Columns:
| Column | Contents |
|--------|----------|
| file_name | Renamed file name |
| original_name | Original filename before renaming |
| category | Folder path within brand-assets/ |
| type | photo or video |
| description | Full description |
| shot_type | Close-up, mid-range, wide, flat lay, etc. |
| mood | Mood/tone tags |
| seasonality | Season if applicable |
| tags | Comma-separated searchable tags |
| suggested_use | Recommended channels/placements |
| quality | High, Medium, Low |
| duration | Video duration (blank for photos) |
| aspect_ratio | Video aspect ratio |
| thumbnail | Video thumbnail frame timestamp |
| metadata_embedded | true/false (JPEG only) |
| duplicate | true/false |
| duplicate_of | If duplicate, which file |
| date_added | Date organized |
| notes | Any notes from review session |

### 2. JSON Catalog (`asset-catalog.json`)

Same data as XLSX in JSON format — one object per asset. Updated after each batch.

```json
[
  {
    "file_name": "lifestyle-flannel-mountain-trail-01.jpg",
    "original_name": "IMG_4392.jpg",
    "category": "lifestyle/outdoor",
    "type": "photo",
    "description": "...",
    "tags": ["flannel", "hiking", "outdoor", "fall"],
    "suggested_use": ["instagram", "meta-ads", "website-hero"],
    "quality": "high",
    "metadata_embedded": true,
    "duplicate": false,
    "date_added": "2026-03-21"
  }
]
```

### 3. Markdown Index (`asset-manifest.md`)

Human-readable index with:
1. Summary section (total counts, category breakdown, date)
2. Quick Search Guide
3. Assets by category with full descriptions

---

## Folder Structure

All organized assets live in `brand-assets/`. Always include `_inbox/`, `_delete/`, and `_duplicates/`.

```
brand-assets/
├── asset-manifest.xlsx         ← primary catalog (shareable with team)
├── asset-catalog.json          ← machine-readable catalog for automation
├── asset-manifest.md           ← human-readable index
├── README.md                   ← library guide
├── asset-config.md             ← file handling mode + library settings
├── _inbox/                     ← drop new assets here for processing
├── _delete/                    ← files marked for deletion (never actually deleted)
├── _duplicates/                ← flagged duplicate files + review log
├── review-batch-01.html        ← review pages (generated per batch, can archive)
├── product-photography/
│   ├── flat-lay/
│   ├── on-model/
│   ├── detail-shots/
│   └── lifestyle-product/
├── lifestyle/
│   ├── outdoor/
│   └── seasonal/
├── team-behind-the-scenes/
├── ugc-community/
├── campaigns/
├── logos-brand-marks/
│   ├── primary/
│   ├── secondary/
│   └── icons/
└── video/
    ├── product/
    ├── lifestyle/
    ├── social-clips/
    └── thumbnails/
```

### Folder Generation Rules

1. **Start with defaults**, then ask the user to confirm, edit, add, or remove
2. **Product-specific subfolders** — offer subfolders for distinct product lines
3. **Channel-specific subfolders** — offer folders like `video/reels/` or `email-headers/`
4. **Depth limit** — no more than 3 levels deep
5. **Never remove `_inbox/`, `_delete/`, or `_duplicates/`**

---

## Channel Suggestion Logic

| Asset Characteristics | Suggested Channels |
|----------------------|-------------------|
| Square/vertical, lifestyle, bright, people | Instagram feed, Stories/Reels |
| Horizontal, high-quality, hero-worthy | Website banners, Email headers |
| Flat lay, clean background, product-focused | Shopify PDP, Email product blocks, Pinterest |
| Action shot, bold, high contrast | Meta Ads, Google Ads display |
| Vertical video, <60s, casual/energetic | Instagram Reels, TikTok, YouTube Shorts |
| Horizontal video, >60s, polished | YouTube, Facebook feed, Website |
| Behind-the-scenes, casual, authentic | Instagram Stories, TikTok, Community posts |
| UGC/customer photos | Social proof, Reviews, Instagram reposts |
| Logo files, brand marks | All platforms as needed |

---

## Quality Flags

- **High** — Sharp focus, good composition, proper exposure, usable for marketing as-is
- **Medium** — Decent quality but may need minor editing (cropping, color correction)
- **Low** — Blurry, poorly lit, bad composition, or too small for marketing use

All quality levels are organized and flagged in the catalog — low quality assets are never silently dropped.

---

## Ongoing Inbox Workflow

```
New photos/videos from shoot or download
              ↓
   brand-assets/_inbox/      ← drop files here
              ↓
        /add-assets           ← run this command
              ↓
   Choose batch size          ← 5 / 10 / 20 / custom
              ↓
   Analyze batch              ← no changes made yet
              ↓
   Generate HTML review page  ← saved to brand-assets/review-batch-XX.html
              ↓
   User reviews page          ← sees thumbnails + suggested metadata
              ↓
   User reports decisions     ← Approve / Edit / Skip / Delete by number
              ↓
   Execute approved assets:
     Copy + rename → embed EXIF/IPTC → move to folder → update all catalogs
              ↓
   Next batch                 ← repeat until inbox empty
              ↓
   Clear _inbox/              ← all processed files removed
```

**Inbox rules:**
- Files in `_inbox/` are never modified until approved
- After successful processing, approved files are removed from `_inbox/`
- Skipped files remain in `_inbox/` for the next session
- The `_inbox/` folder itself is never deleted
