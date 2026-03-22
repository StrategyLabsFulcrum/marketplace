# /import-from-photos

Pull photos and videos directly from your Apple Photos library into the asset library inbox — by album, date range, keyword, person, or recent captures. Once imported to `_inbox/`, run `/add-assets` to analyze, review, and organize them.

## Invoke Options

```
/import-from-photos                        ← interactive mode, browse everything
/import-from-photos album "Fall 2026"      ← import a specific album by name
/import-from-photos recent 7               ← import last N days
/import-from-photos date 2026-03-01 2026-03-21  ← import a date range
/import-from-photos favorites              ← import all favorited photos
/import-from-photos keyword "product"      ← import by keyword/tag
```

---

## Step 1: Check osxphotos

Check if `osxphotos` is installed:

```python
import subprocess
result = subprocess.run(["python3", "-c", "import osxphotos"], capture_output=True)
if result.returncode != 0:
    # Not installed
```

If NOT installed, tell the user:

> "`osxphotos` is required to access Apple Photos. Install it with:
> ```
> pip3 install osxphotos
> ```
> Run that in Terminal, then try `/import-from-photos` again."

Stop here until confirmed installed.

---

## Step 2: Connect to Photos Library

```python
import osxphotos

photosdb = osxphotos.PhotosDB()
total = len(photosdb.photos())
albums = sorted(photosdb.album_names())
keywords = sorted(photosdb.keywords_as_dict.keys()) if hasattr(photosdb, 'keywords_as_dict') else []
persons = sorted(photosdb.persons_as_dict.keys()) if hasattr(photosdb, 'persons_as_dict') else []
```

If the Photos library can't be opened (permissions), tell the user:

> "Claude needs permission to access your Photos library. Go to **System Settings → Privacy & Security → Photos** and make sure Claude (or Terminal) is allowed. Then try again."

---

## Step 3: Discover Library

Report what's available:

```
Apple Photos Library Connected
─────────────────────────────────────
Total photos & videos: [N]
Albums: [count] ([list first 10, "...and X more" if over 10])
Keywords: [count] ([sample])
People: [count] ([sample if any])
```

---

## Step 4: Select What to Import

If invoked without arguments (interactive mode), present options:

> "What would you like to import?
>
> **1. By album** — choose from your albums
> **2. By date range** — e.g., last 7 days, or March 1–21
> **3. Favorites** — all photos you've marked as favorites
> **4. By keyword** — photos tagged with a specific keyword
> **5. By person** — photos featuring a specific person (if face recognition is on)
> **6. Recent** — last N days
> **7. Smart search** — I'll describe what I want
>
> Reply with a number or describe what you're looking for."

If invoked with arguments, skip this step and go directly to Step 5.

### Handling Each Mode

**Album mode:**
```python
# List albums with photo counts
for album in photosdb.album_info:
    print(f"{album.title}: {len(album.photos)} assets")
```
If the user names an album, fuzzy-match against the list. If ambiguous, show the closest matches and ask for confirmation.

**Date range mode:**
```python
from datetime import datetime, timedelta
photos = photosdb.photos(from_date=start_dt, to_date=end_dt)
```

**Recent N days:**
```python
from datetime import datetime, timedelta
cutoff = datetime.now() - timedelta(days=n)
photos = photosdb.photos(from_date=cutoff)
```

**Favorites:**
```python
photos = [p for p in photosdb.photos() if p.favorite]
```

**Keyword:**
```python
photos = photosdb.photos(keywords=[keyword])
```

**Person:**
```python
photos = photosdb.photos(persons=[person_name])
```

**Smart search (natural language):**
Map the user's description to the appropriate query. Examples:
- "photos from last month's shoot" → date range (last 30 days)
- "all the food photos tagged restaurant" → keyword="restaurant"
- "my starred photos" → favorites
- "shots from the spring campaign album" → album fuzzy match

---

## Step 5: Preview Before Importing

Before exporting anything, show a preview:

```python
# Count by type
photos_count = sum(1 for p in selected if not p.ismovie)
videos_count = sum(1 for p in selected if p.ismovie)

# Date range of selection
dates = [p.date for p in selected if p.date]
date_range = f"{min(dates).strftime('%b %d')} – {max(dates).strftime('%b %d, %Y')}" if dates else "unknown dates"

# Total size estimate
total_mb = sum((p.original_filesize or 0) for p in selected) / (1024 * 1024)
```

Report:

> "Ready to import:
> - **[X] photos** and **[Y] videos**
> - Date range: [range]
> - Estimated size: [N] MB
> - Destination: `brand-assets/_inbox/`
>
> Proceed? (yes / change selection)"

---

## Step 6: Export to Inbox

After confirmation, export all selected assets to `brand-assets/_inbox/`:

```python
import os
from pathlib import Path

inbox_path = Path("brand-assets/_inbox")
inbox_path.mkdir(parents=True, exist_ok=True)

exported = []
skipped_duplicates = []

for photo in selected:
    # Check if already in inbox or organized library
    original_name = photo.original_filename

    # Skip if exact filename already exists in inbox
    if (inbox_path / original_name).exists():
        skipped_duplicates.append(original_name)
        continue

    try:
        results = photo.export(
            str(inbox_path),
            use_photos_export=False,   # export original file, not Photos-processed
            original=True,             # always get original, not edited version
            skip_edited=False,
            overwrite=False,
            timeout=120,
        )
        if results.exported:
            exported.append(results.exported[0])
    except Exception as e:
        print(f"Could not export {original_name}: {e}")

```

Report progress during export for large batches:
> "Exporting... 24/87 complete"

### Export Options to Preserve

When exporting, preserve:
- **Original filename** — use `photo.original_filename` so the file lands in inbox with its real name
- **Original file** (not Photos-edited version) — use `original=True`
- **Live Photos** — export as JPEG + MOV pair; both land in inbox
- **RAW files** — export the RAW if available

---

## Step 7: Confirm Import

After export is complete:

```
Import Complete!
─────────────────────────────────────
Exported to brand-assets/_inbox/:
  Photos:  [X]
  Videos:  [Y]
  Total:   [Z] files

Skipped (already in inbox): [N]
Export errors: [N] (list if any)

Source: [Album name / Date range / etc.]
```

Then offer to continue:

> "Your [Z] assets are in the inbox. Would you like to run `/add-assets` now to review, organize, and catalog them?"

If yes, proceed directly into the `/add-assets` workflow starting at the batch size question — no need for the user to invoke it separately.

---

## Handling Failures Gracefully

**Permission denied on Photos library:**
> "macOS is blocking access to Photos. Go to System Settings → Privacy & Security → Photos and grant access, then try again."

**Album not found:**
> "I couldn't find an album named '[name]'. Here are the closest matches: [list]. Which did you mean?"

**Export error on individual file:**
Log the error, skip the file, continue with the rest. Report skipped files at the end.

**osxphotos version mismatch:**
> "There was a compatibility issue with osxphotos. Try updating it: `pip3 install --upgrade osxphotos`"

---

## Notes

- **Originals are never modified** — this command only reads from Photos and copies files to `_inbox/`. Your Photos library is untouched.
- **iCloud photos** — if a photo is stored in iCloud and not downloaded locally, osxphotos will attempt to download it. This may be slow for large iCloud libraries. Consider enabling "Download Originals" in Photos settings for bulk imports.
- **HEIC format** — iPhones shoot HEIC by default. The Brand Asset Manager handles HEIC analysis. EXIF embedding is skipped for HEIC (only applied to JPEG copies).
- **Live Photos** — the JPEG frame and .MOV clip are exported as separate files. Both land in inbox and are processed independently.
