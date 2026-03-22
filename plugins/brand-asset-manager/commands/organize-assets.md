# /organize-assets

Analyze, organize, rename, and catalog a folder of unorganized brand photos and videos. Analyzes assets in batches, generates a visual HTML review page for each batch with embedded thumbnails, waits for your approval, then copies, renames, embeds metadata, and catalogs everything.

> **Starting fresh with no library yet?** Use `/asset-setup` first — it builds the folder structure before you load assets.

---

## Before Starting

1. Check if `brand-assets/` already exists with an `asset-manifest.xlsx`.
   - If it exists, say: "You already have an organized asset library. Would you like to re-organize from scratch, or use `/add-assets` to add new files?"
   - If re-organizing from scratch, back up the existing library by renaming to `brand-assets-backup-[date]/`.
2. Load `brand-assets/asset-config.md` and read the **File Handling Mode** (`duplicate` or `move`). If the file doesn't exist (library predates this feature), default to `move` and note:
   > "File handling mode not set — defaulting to **move and rename**. To change this, say 'set file handling mode' at any time."
3. Check if `brand-knowledge-center/` exists for brand context.

---

## Step 1: Brand Context

### If `brand-knowledge-center/` exists:

Read:
- `brand-identity.md` — brand pillars, visual identity, product lines, colors
- `audience-messaging.md` — audience segments, content pillars, channels
- `digital-ecosystem.md` — active platforms and tools
- `business-overview.md` — industry, product types

Note the brand's primary and secondary hex colors — these will style the HTML review pages.

Confirm what was found:

> "I found your Brand Knowledge Center. Here's what I'll use to organize your assets:
> - **Brand:** [name] · **Colors:** [hex values]
> - **Products:** [product types]
> - **Active channels:** [list]
>
> Does this look right?"

### If NO brand knowledge exists:

Ask:
1. "What does your brand sell?"
2. "What channels do you publish on?"
3. "What types of content do you shoot?"
4. "Any specific product lines or collections?"
5. "What are your brand colors?" (hex codes — used to style review pages)

---

## Step 2: Propose Folder Structure

Based on brand context, propose a tailored folder structure as a visual tree. Always include `_inbox/`, `_delete/`, and `_duplicates/`.

Ask:
1. "Does this folder structure work? Anything to add, remove, or rename?"
2. "Any product lines that should get their own subfolders?"
3. "Any campaign names or seasons to add?"

Apply edits and confirm the final structure.

---

## Step 3: Source Assets

Ask where the unorganized assets are:

> "Where are the photos and videos you'd like to organize? Provide a folder path, or upload them directly."

Once the source is identified:
1. Recursively scan for all image and video files
2. Report what was found: "Found **87 photos** and **12 videos** in [source folder]."

---

## Step 4: Batch Size

Ask the user their preferred batch size:

> "How many assets would you like to review per batch?
> - **5 at a time** — Small, focused batches
> - **10 at a time** — Good balance of speed and control *(recommended)*
> - **20 at a time** — Faster, for large inboxes
> - **Custom** — I'll specify a number"

Remember the answer for the entire session.

---

## Step 5: Analyze First Batch

**Analyze the first batch completely BEFORE generating the review page.** Do not copy, move, or rename anything.

For each photo:
1. View the image
2. Identify: subject, products visible, shot type, setting, mood, lighting, composition quality, colors, people, seasonality
3. Determine best category and subfolder
4. Generate descriptive filename (check sequence numbers against existing files)
5. Write full description and tags
6. Assess quality (High / Medium / Low)
7. Check for duplicates against any already-organized assets
8. Flag anything uncertain with a specific ⚠️ question

For each video:
1. Identify: duration, content summary, subjects, shot types, audio, aspect ratio, mood
2. Determine category, generate filename, write description
3. Identify 2-3 thumbnail candidate timestamps
4. Assess quality

**Session learning:** As you process each batch, build an internal reference of what you've seen — subjects confirmed, corrections made, categories established. Use this to improve confidence and reduce uncertainty flags in later batches.

---

## Step 6: Generate HTML Review Page

After analyzing the batch, use Python to base64-encode each image and generate a self-contained HTML review page saved to `brand-assets/review-batch-01.html`.

```python
import base64
import os

def encode_image_for_html(filepath):
    ext = filepath.rsplit(".", 1)[-1].lower()
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp", "gif": "gif"}.get(ext, "jpeg")
    with open(filepath, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:image/{mime};base64,{b64}"
```

### Review Page Requirements

**Page header:**
- Legend: "Review each asset below. When done, come back to chat and reply: **Approve all**, or list asset numbers with **Edit / Skip / Delete** and any corrections."
- Batch summary: "Batch 1 of [N] · [X] photos · [Y] videos · Proposed categories: [list]"

**Each card must show:**
- Asset number (#1 of 10) and original filename
- Thumbnail (base64-embedded for photos; video placeholder icon for videos)
- **Suggested Name** — proposed descriptive filename
- **Category** — proposed folder path
- **Description** — full searchable description
- **Tags** — comma-separated keywords
- **Suggested Use** — recommended channels/placements
- **Quality** — High / Medium / Low with a brief reason
- **⚠️ Uncertainty flag** — if anything is ambiguous, a specific question for the user
- **Duplicate flag** — if similar to an existing asset, note it with the existing filename

**Styling:**
- Use brand primary color for accents (from `brand-identity.md`, or `#4f8ef7` if unknown)
- Dark background (#1a1a2e), light card surface (#0f172a), light text (#e2e8f0)
- Clean card layout: thumbnail left, metadata right (stacks on mobile)
- Clear visual separation between cards
- Fully self-contained — no external CSS or JS dependencies

After generating the file, tell the user:

> "Review page ready: `brand-assets/review-batch-01.html` — open it in your browser to see all [N] assets with suggested names and tags. Come back here when you've made your decisions."

---

## Step 7: Process Decisions

After the user reports decisions:

**Approved assets — execute in order based on file handling mode:**

**If mode is `duplicate` (non-destructive):**
1. Copy from source to the organized folder with the new descriptive name
   — Original file stays in the source folder, untouched, with its original name

**If mode is `move`:**
1. Move from source to the organized folder with the new descriptive name
   — Source folder is cleared of approved files
2. Embed EXIF/IPTC metadata into the JPEG (skip for video, PNG, WEBP):

```python
import piexif
from iptcinfo3 import IPTCInfo

def embed_asset_metadata(filepath, title, description, keywords):
    try:
        exif_dict = piexif.load(filepath)
    except Exception:
        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}}

    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = description.encode("utf-8")
    exif_dict["0th"][piexif.ImageIFD.XPTitle]          = (title + "\x00").encode("utf-16-le")
    exif_dict["0th"][piexif.ImageIFD.XPKeywords]       = (";".join(keywords) + "\x00").encode("utf-16-le")
    exif_dict["0th"][piexif.ImageIFD.XPComment]        = (description + "\x00").encode("utf-16-le")
    piexif.insert(piexif.dump(exif_dict), filepath)

    info = IPTCInfo(filepath, force=True)
    info["keywords"]         = [k.encode("utf-8") for k in keywords]
    info["caption/abstract"] = description.encode("utf-8")
    info["object name"]      = title.encode("utf-8")
    info.save_as(filepath)

    junk = filepath + "~"
    if os.path.exists(junk):
        os.remove(junk)
```

3. Add entry to catalog data with `metadata_embedded: true` (or `false` for non-JPEG)

**Edited assets:** Ask what to change, apply correction, then process as approved.

**Skipped assets:** Leave in source folder, do not log.

**Delete:** Move to `brand-assets/_delete/` with original name. Do not delete any file.

After all decisions are processed, update all three catalog files (see Step 8), then move to the next batch.

---

## Step 8: Repeat for All Batches

After processing decisions for each batch:
1. Update catalogs immediately (don't wait until all batches are done)
2. Announce progress: "Batch 1 complete — 8 approved, 1 skipped, 1 deleted. Moving to batch 2 of [N]."
3. Analyze next batch and generate the next review page
4. Continue until all assets are processed

---

## Step 9: Generate / Update Catalogs

After each batch is processed, regenerate all three catalog formats:

### `asset-manifest.xlsx`
Columns: `file_name, original_name, category, type, description, shot_type, mood, seasonality, tags, suggested_use, quality, duration, aspect_ratio, thumbnail, metadata_embedded, duplicate, duplicate_of, date_added, notes`

### `asset-catalog.json`
One JSON object per asset. Full schema matches the XLSX columns.

### `asset-manifest.md`
Human-readable index with:
1. Summary section — total counts, category breakdown, metadata embedded count, date
2. Quick Search Guide — what keywords to search for
3. Assets by category with full descriptions

---

## Step 10: Completion

```
Organization Complete!

📁 brand-assets/
  [X] photos organized across [N] categories
  [Y] videos organized with thumbnail timestamps noted
  [Z] files moved to _delete/
  [D] duplicate groups flagged

File handling: [Duplicate — originals preserved in source / Move — source cleared]

Metadata embedded: [X] JPEGs (searchable in Finder, Spotlight, Adobe)

Catalog files updated:
  asset-manifest.xlsx  — shareable spreadsheet
  asset-catalog.json   — automation-ready
  asset-manifest.md    — searchable index

Review pages saved: brand-assets/review-batch-01.html through review-batch-[N].html

Next steps:
  → Review anything in _delete/ and permanently remove if confirmed
  → Drop future assets in brand-assets/_inbox/ and run /add-assets
```

Create `brand-assets/_inbox/` if it doesn't exist, with a `.keep` file and a brief README explaining the inbox workflow.
