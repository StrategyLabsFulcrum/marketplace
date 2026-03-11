# Transcript Parsing Reference

Format detection rules, column mapping, and parsing patterns for processing call transcripts. The analyze-calls skill uses this to normalize any input format into a standard internal structure.

---

## Format Detection

### Auto-Detection Rules

Determine format by file extension and content inspection:

| Extension | Primary Format | Validation |
|-----------|---------------|------------|
| `.txt` | Plain text transcript | Must contain conversational text (not tabular data). If first line looks like CSV headers, treat as CSV. |
| `.csv` | Comma-separated values | Must parse as valid CSV with consistent column count. |
| `.tsv` | Tab-separated values | Must parse as valid TSV. Treat identically to CSV after splitting on tabs. |
| `.mp3`, `.wav`, `.m4a` | Audio file | Binary file. Requires transcription step before parsing. |

### Content Sniffing

If extension is ambiguous or missing, inspect the first 10 lines:

1. **CSV check**: Count commas per line. If 3+ lines have the same comma count > 2, treat as CSV.
2. **TSV check**: Count tabs per line. If 3+ lines have the same tab count > 1, treat as TSV.
3. **Speaker-labeled check**: Look for patterns like `Agent:`, `Caller:`, `Customer:`, `Rep:`, `[Speaker 1]`. If found, treat as speaker-labeled transcript.
4. **Timestamped check**: Look for timestamp patterns like `[00:01:23]`, `0:01:23`, `00:01:23 -`. If found, treat as timestamped transcript.
5. **Plain text fallback**: If none of the above match, treat as unstructured plain text.

---

## CSV/TSV Parsing

### Column Detection

Read the first row as headers. Map columns using flexible matching:

| Internal Field | Accepted Column Names (case-insensitive) |
|---------------|------------------------------------------|
| `caller_name` | caller, customer, name, caller_name, customer_name, contact, client |
| `date` | date, call_date, timestamp, created, created_at, call_time, datetime |
| `duration` | duration, length, call_length, call_duration, time, minutes |
| `transcript` | transcript, text, body, content, call_text, transcript_text, notes, conversation, call_transcript |
| `category` | category, type, call_type, reason, call_reason, topic, department |
| `phone` | phone, phone_number, number, caller_phone, tel |
| `agent` | agent, rep, representative, employee, handler, agent_name |
| `sentiment` | sentiment, mood, tone, satisfaction |
| `notes` | notes, comments, internal_notes, agent_notes |
| `id` | id, call_id, record_id, reference, ticket |

### Column Mapping Rules

1. **Required field**: `transcript` — If no column maps to transcript, abort with error: "Could not identify a transcript column. Please specify which column contains the call transcript text."
2. **Fallback for caller_name**: If no caller name column, use filename or generate sequential IDs (`Caller-001`, `Caller-002`).
3. **Fallback for date**: If no date column, extract from filename if structured (see Filename Parsing below). Otherwise use file modification date.
4. **Multiple transcript columns**: If multiple columns could be the transcript, prefer the one with the longest average content length.
5. **Ignore columns**: Skip any column not in the mapping table. Do not discard the data — store unmapped columns in a `metadata` field for the raw call file.

### CSV Edge Cases

| Scenario | Handling |
|----------|----------|
| Quoted fields with commas | Standard CSV parsing — commas inside double-quotes are not delimiters |
| Newlines inside cells | Preserve newlines in transcript text |
| Empty rows | Skip entirely |
| Header row missing | If first row looks like data (no recognizable header names), prompt user to confirm column order |
| Mixed encodings | Try UTF-8 first, then Latin-1, then CP1252. If all fail, report encoding error. |
| BOM markers | Strip UTF-8 BOM (`\xEF\xBB\xBF`) if present |

### Duration Normalization

Convert any duration format to seconds:

| Input Format | Example | Seconds |
|-------------|---------|---------|
| `MM:SS` | `5:30` | 330 |
| `HH:MM:SS` | `1:05:30` | 3930 |
| `Xm Ys` | `5m 30s` | 330 |
| `X minutes` | `5.5 minutes` | 330 |
| `X min` | `5 min` | 300 |
| `X seconds` | `330 seconds` | 330 |
| Bare number | `330` | 330 (assume seconds if > 10, minutes if ≤ 10) |

### Date Normalization

Convert any date format to ISO 8601 (`YYYY-MM-DD`):

| Input Format | Example |
|-------------|---------|
| `MM/DD/YYYY` | `01/15/2024` |
| `YYYY-MM-DD` | `2024-01-15` |
| `DD-Mon-YYYY` | `15-Jan-2024` |
| `Month DD, YYYY` | `January 15, 2024` |
| `MM-DD-YYYY` | `01-15-2024` |
| `YYYYMMDD` | `20240115` |
| Unix timestamp | `1705276800` |

If a date includes a time component, extract the date portion and store the time separately.

---

## Plain Text Transcript Parsing

### Speaker-Labeled Format

Pattern: `<speaker_label><separator><text>`

Recognized speaker labels:
- Agent-side: `Agent`, `Rep`, `Representative`, `Employee`, `Support`, `Sales`, `Handler`, `Advisor`, `Associate`
- Caller-side: `Caller`, `Customer`, `Client`, `Guest`, `Visitor`, `User`
- Generic: `Speaker 1`, `Speaker 2`, `[S1]`, `[S2]`, `Person A`, `Person B`

Recognized separators: `:`, ` - `, ` -- `, `>`, `|`

Example patterns:
```
Agent: Welcome to Rugged Terrain, how can I help you?
Caller: Yeah, I'm looking for a bumper for my 2019 RZR...

[Agent] Welcome to Rugged Terrain, how can I help you?
[Customer] Yeah, I'm looking for a bumper for my 2019 RZR...

Speaker 1: Welcome to Rugged Terrain...
Speaker 2: Yeah, I'm looking for...
```

**Parsing rules**:
1. Identify all unique speaker labels in the transcript.
2. Map the first speaker to appear as "Agent" (unless label clearly indicates otherwise).
3. Map the second speaker as "Caller."
4. If 3+ speakers, label as Agent, Caller, and Speaker-N.
5. Preserve turn order and all text content.

### Timestamped Format

Pattern: `<timestamp> <speaker_or_text>`

Recognized timestamp patterns:
- `[HH:MM:SS]` or `[MM:SS]`
- `HH:MM:SS` or `MM:SS` (without brackets)
- `HH:MM:SS.mmm` (with milliseconds)
- `(HH:MM:SS)` or `(MM:SS)`

Example:
```
[00:00:05] Agent: Welcome to Rugged Terrain.
[00:00:12] Caller: Hi, I'm looking for a bumper.
[00:00:45] Agent: Sure, what year and model?
```

**Parsing rules**:
1. Extract timestamps and calculate call duration from first to last timestamp.
2. If speaker labels are present, apply speaker-labeled parsing after stripping timestamps.
3. If no speaker labels, attempt to alternate Agent/Caller based on conversational flow.

### Unstructured Text

For plain text with no speaker labels or timestamps:

1. Treat the entire text as a single block transcript.
2. Attempt to identify conversational turns by looking for:
   - Question marks followed by declarative responses.
   - Greeting patterns ("hello", "hi", "welcome") to find the start.
   - Closing patterns ("thank you", "goodbye", "anything else") to find the end.
3. If turns can't be identified, process the entire text as one unit. Analysis will rely on content rather than speaker attribution.

---

## Filename Parsing

### Structured Filename Patterns

Extract metadata from filenames when CSV/text columns don't provide it:

| Pattern | Example | Extracted Fields |
|---------|---------|-----------------|
| `YYYY-MM-DD_name.ext` | `2024-01-15_john-doe.txt` | date: 2024-01-15, caller: John Doe |
| `YYYY-MM-DD_HHMMSS.ext` | `2024-01-15_143022.mp3` | date: 2024-01-15, time: 14:30:22 |
| `name_YYYY-MM-DD.ext` | `john-doe_2024-01-15.txt` | caller: John Doe, date: 2024-01-15 |
| `YYYYMMDD-name.ext` | `20240115-john-doe.txt` | date: 2024-01-15, caller: John Doe |
| `call-NNN.ext` | `call-042.txt` | id: 042 |
| `NNN_YYYY-MM-DD.ext` | `042_2024-01-15.txt` | id: 042, date: 2024-01-15 |

### Name Normalization

Convert filename fragments to proper names:
- Replace hyphens and underscores with spaces: `john-doe` → `John Doe`
- Title case: `john doe` → `John Doe`
- Don't title-case known abbreviations: `LLC`, `USA`, `RZR`, `UTV`

---

## Internal Transcript Structure

After parsing, every transcript is normalized to this internal structure:

```
{
  "id": "call-NNN",
  "source_file": "original-filename.ext",
  "source_format": "csv|txt|audio",
  "caller_name": "Name or Caller-NNN",
  "date": "YYYY-MM-DD",
  "time": "HH:MM:SS or null",
  "duration_seconds": N,
  "agent_name": "Name or null",
  "category": "auto-detected or from source",
  "phone": "number or null",
  "turns": [
    {"speaker": "agent|caller|unknown", "text": "...", "timestamp": "HH:MM:SS or null"},
    ...
  ],
  "full_text": "Complete transcript as single string",
  "metadata": { ... any unmapped fields from source ... }
}
```

This internal structure is what the per-call analysis engine receives. The `full_text` field is the primary input for LLM analysis. The `turns` array provides structure for speaker-specific analysis (e.g., detecting agent versus caller sentiment independently).

---

## Batch Processing Rules

### File Discovery

When scanning a source folder:

```bash
# Find all supported file types
find [source_folder] -type f \( -name "*.txt" -o -name "*.csv" -o -name "*.tsv" -o -name "*.mp3" -o -name "*.wav" -o -name "*.m4a" \) | sort
```

### Deduplication

Before processing, check for duplicates:

1. **Exact filename match**: If `call-042.txt` already exists in `analysis/raw/`, skip unless reprocessing.
2. **Content hash**: For CSV rows, compute a simple hash of caller_name + date + first 100 chars of transcript. Skip duplicates.
3. **Audio + transcript pairs**: If both `call-042.mp3` and `call-042.txt` exist, prefer the text transcript (skip audio transcription).

### Processing Order

1. Sort files by date (oldest first) if dates are available.
2. If no dates, sort by filename alphabetically.
3. Assign sequential IDs: `call-001`, `call-002`, etc.
4. For incremental updates, continue numbering from the last existing ID.

### Error Handling

| Error | Action |
|-------|--------|
| Empty file | Skip, log warning: "Skipped [filename]: empty file" |
| Unreadable encoding | Try fallback encodings. If all fail, skip with warning. |
| CSV with 0 parseable rows | Skip, log error: "Could not parse [filename] as CSV" |
| Transcript under 50 characters | Skip, log warning: "Skipped [filename]: transcript too short for meaningful analysis" |
| Audio file with no transcription tool | Collect all audio files, report count, suggest alternatives |
| Malformed date | Use file modification date as fallback |
| Duplicate detected | Skip, log info: "Skipped [filename]: duplicate of [existing]" |

### Progress Reporting

During batch processing, report progress to the user:
- Before starting: "Found [N] new files to process ([X] text, [Y] CSV rows, [Z] audio)."
- Per file: "Processing [current]/[total]: [filename]..."
- After completion: "Processed [N] calls. [X] skipped (duplicates: [D], errors: [E])."
