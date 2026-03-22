# /add-assets

Add new photos and videos to an existing brand asset library. Scans `_inbox/` (or a specified folder), analyzes assets in batches, generates a visual HTML review page for each batch, waits for approval, then copies, renames, embeds metadata, and updates all catalogs.

## Invoke Options

```
/add-assets                  ← scan _inbox/ automatically
/add-assets [folder path]    ← point to a specific folder of new assets
```

---

## Before Starting

1. Check if `brand-assets/` exists with an `asset-manifest.xlsx`.
   - If it does NOT exist, say: "No asset library found. Run `/asset-setup` to build your folder structure first."
2. Load `brand-assets/asset-config.md` and read the **File Handling Mode** (`duplicate` or `move`). If the file doesn't exist (library created before this feature), default to `move` and note:
   > "File handling mode not set — defaulting to **move and rename** (current behavior). To change this, say 'set file handling mode' at any time."
3. Load the existing `asset-catalog.json` to know what's already in the library (for duplicate detection and session learning).
4. Note the brand's colors from `brand-knowledge-center/brand-identity.md` if available (used to style review pages).
5. Report the current library state and active file handling mode:

> "Your asset library has **[X] photos** and **[Y] videos** across [Z] categories. Last updated: [date].
> File handling: **[Duplicate — originals preserved / Move and rename — originals relocated]**. Ready to add new assets."

---

## Step 1: Find New Assets

### Default: Check `_inbox/`

If no path is provided, check `brand-assets/_inbox/`.

If `_inbox/` is empty:
> "The inbox is empty. Drop new photos or videos into `brand-assets/_inbox/` and run `/add-assets` again. Or provide a folder path: `/add-assets [path]`"

If files are found, report:
> "Found **[X] photos** and **[Y] videos** in your inbox."

### Custom folder path

Scan the provided folder recursively and report what was found.

---

## Step 2: Batch Size

Ask the user their preferred batch size:

> "How many assets would you like to review per batch?
> - **5 at a time** — Small, focused batches
> - **10 at a time** — Good balance of speed and control *(recommended)*
> - **20 at a time** — Faster, for large inboxes
> - **Custom** — I'll specify a number"

Remember the answer for the entire session.

---

## Step 3: Analyze First Batch

**Analyze the first batch completely BEFORE generating the review page.** Do not copy, move, or rename anything.

For each photo:
1. View the image
2. Identify: subject, products visible, shot type, setting, mood, lighting, composition quality, colors, people, seasonality
3. Determine the best category within the **existing** folder structure
4. Generate descriptive filename — check existing files in the target folder to continue the sequence number correctly
5. Write full description and tags
6. Assess quality (High / Medium / Low)
7. Check for duplicates against the loaded `asset-catalog.json`
8. Flag anything uncertain with a specific ⚠️ question

For each video:
1. Identify: duration, content summary, subjects, shot types, audio, aspect ratio, mood
2. Determine category, generate filename, write description
3. Identify 2-3 thumbnail candidate timestamps
4. Assess quality

**Session learning:** Build an internal reference as you analyze each batch. If a subject type, category, or correction has already been established earlier in the session, apply it confidently to similar assets without re-flagging. Reference previously approved assets in descriptions where relevant.

**New category detection:** If an asset clearly doesn't fit any existing folder, note it on the review card: "This doesn't fit an existing category — I suggest creating `[folder/subfolder/]`. Confirm or redirect."

---

## Step 4: Duplicate Check

Before generating the review page, compare each new asset against the existing catalog:

**Exact duplicate:** Same filename + file size match in the catalog → flag on the review card: "⚠️ Appears to be an exact duplicate of `[existing-file.jpg]` already in your library."

**Near duplicate:** Same subject and similar composition to an existing cataloged asset → flag: "Similar to `[existing-file.jpg]` already in your library. Keep as an alternate version?"

**New content:** No flag needed — process normally.

---

## Step 5: Generate HTML Review Page

After analyzing the batch, use Python to base64-encode each image and generate a self-contained HTML file saved to `brand-assets/review-batch-[NN].html`. Number sequentially from the last existing batch file.

```python
import base64

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
- Batch summary: "Batch [N] · [X] photos · [Y] videos · [Z] duplicates flagged"

**Each card must show:**
- Asset number and original filename
- Thumbnail (base64-embedded for photos; video placeholder icon for videos)
- **Suggested Name** — proposed descriptive filename
- **Category** — proposed folder path (note if it's a new folder being proposed)
- **Description** — full searchable description
- **Tags** — comma-separated keywords
- **Suggested Use** — recommended channels/placements
- **Quality** — High / Medium / Low with a brief reason
- **⚠️ Uncertainty flag** — if anything is ambiguous, a specific question
- **Duplicate flag** — similar-to note with existing filename if applicable

**Styling:**
- Use brand primary color from `brand-identity.md` for accents (or `#4f8ef7` if unavailable)
- Dark background (#1a1a2e), dark card surface (#0f172a), light text (#e2e8f0)
- Thumbnail left, metadata right — stacks on mobile
- Fully self-contained — no external CSS or JS

After generating, tell the user:

> "Review page ready: `brand-assets/review-batch-[NN].html` — open it in your browser to see all [N] assets. Come back here with your decisions."

---

## Step 6: Process Decisions

After the user reports decisions for the batch:

**Approved assets — execute in order based on file handling mode:**

**If mode is `duplicate` (non-destructive):**
1. Copy from `_inbox/` (or source folder) to the organized folder with the new descriptive name
2. Leave the original file in `_inbox/` (or source folder) — it is NOT removed. The inbox is not cleared for duplicate-mode sessions.

**If mode is `move` (default):**
1. Copy from `_inbox/` (or source folder) to the organized folder with the new descriptive name
2. Embed EXIF/IPTC metadata into each approved JPEG:

```python
import piexif
from iptcinfo3 import IPTCInfo
import os

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

Skip embedding for: video files, PNG/WEBP files, files moved to `_delete/`, skipped files.

3. Add entry to catalog data with `metadata_embedded: true/false`
4. **If mode is `move`:** Remove processed file from `_inbox/` (approved files only). **If mode is `duplicate`:** Leave the original in `_inbox/` — only the organized copy was created.

**Edited assets:** Ask what to change, apply correction, then process as approved.

**Skipped assets:** Leave in `_inbox/`, do not log.

**Delete:** Move to `brand-assets/_delete/` with original name. Never delete the actual file.

---

## Step 7: Update All Catalogs

After each batch's decisions are fully processed:

**`asset-manifest.xlsx`** — append new rows, update summary counts

**`asset-catalog.json`** — append new entries to the JSON array

**`asset-manifest.md`** — regenerate with updated counts and new entries added to their category sections

Do not wait until all batches are done — update after each batch so the catalog always reflects what's been approved so far.

---

## Step 8: Next Batch

After catalogs are updated, announce progress and move to the next batch:

> "Batch [N] complete — [X] approved, [Y] skipped, [Z] deleted. [Remaining] assets left. Analyzing batch [N+1]..."

Analyze the next batch and generate its review page. Continue until all assets from `_inbox/` (or source folder) are processed.

---

## Step 9: Completion

```
New Assets Added!

Added: [X] photos, [Y] videos
Skipped: [N] (left in _inbox/)
Deleted: [N] (moved to _delete/)
Duplicates flagged: [N]

Metadata embedded: [X] JPEGs

New assets by category:
  [category]: [count]
  ...

Updated library totals:
  Photos: [prev] → [new]
  Videos: [prev] → [new]

All catalogs updated:
  asset-manifest.xlsx · asset-catalog.json · asset-manifest.md

File handling: [Duplicate — originals preserved in _inbox/ / Move — inbox cleared ✓]

Next: Drop more assets in brand-assets/_inbox/ anytime and run /add-assets
```

---

## Inbox Folder Convention

```
New shoot / new content
        ↓
brand-assets/_inbox/     ← drop files here
        ↓
/add-assets              ← run this command
        ↓
Choose batch size → Analyze → HTML review page → Approve → Organize + embed metadata
        ↓
brand-assets/[category]/ ← files land here: renamed, tagged, cataloged
```

- Files in `_inbox/` are never modified until approved
- Skipped files always remain in `_inbox/` for the next session
- **Move mode:** Approved files are removed from `_inbox/` after processing — inbox is cleared
- **Duplicate mode:** Approved files remain in `_inbox/` after processing — originals are preserved alongside the organized copies
- `_inbox/` itself is never deleted — it's the permanent drop zone
