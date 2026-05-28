# Voice Calibration

Refine your voice profile through multi-source analysis (Fireflies primary) and A/B message comparison. Runs in three modes:

1. **Initial setup** — full calibration from blank profile (called by `/setup-wizard`)
2. **Mandatory periodic review** — monthly minimum, bi-weekly or weekly optional
3. **Drift-triggered** — auto-fires at session end when 3+ substantial draft edits occur in one triage

## Before Starting

1. **Read** `~/Inbox Command Center/voice-profile.md` (and `voice-profile-brand.md` if BKC connected)
2. **Read** `.meta.json`:
   - `last_fireflies_pull` — note when transcripts were last pulled
   - `voice_drift_counter` — non-zero indicates drift since last review
   - `schedules.voice_review_cadence`
3. **Determine mode:**
   - Called from `/setup-wizard` → initial mode
   - Called by user explicitly → either targeted recalibration or full review (ask)
   - Called automatically (cadence due OR drift-triggered) → review mode

## Step 0: Mode Selection

```
Voice calibration — what kind of session?

  [ ] Full review (re-analyze all sources + A/B calibration, ~10-15 min)
  [ ] Quick review (re-analyze sources, no A/B, ~3 min)
  [ ] Targeted recalibration (5-pair A/B on specific scenarios, ~3 min)
  [ ] Drift recalibration (5-pair A/B on scenarios that triggered edits, ~3 min)
```

If invoked automatically by drift trigger, default to **Drift recalibration** with no menu.

If invoked by cadence-due review, default to **Full review** unless user picks otherwise.

If invoked from setup wizard, run full Phase A → Phase B → Phase C without menu.

## Step 0b: Multi-Source Re-Analysis (Phase A)

For Full or Quick review modes, re-analyze all connected sources. Source priority:

### Source A: Fireflies transcripts (PRIMARY)

```
Pull Fireflies transcripts since last review:
  mcp__claude_ai_Fireflies__fireflies_get_transcripts
  date_range: [last_voice_review_date] → today
  
Extract per transcript:
  - Greetings and openings
  - Sign-offs and closings
  - Decision-making language
  - Tone shifts by audience (1:1 vs. group, internal vs. external)
  - New phrases used multiple times
  - Vocabulary patterns
  - Sentence structure (short bursts vs. longer)
  - Humor / casual register usage

Weight: highest — this is the user's unscripted voice.
```

### Source B: Sent email (across all connected inboxes)

```
For each inbox in .meta.json.connected_inboxes:
  himalaya_alias = inbox.himalaya_alias

  # Gmail: read from [Gmail]/Sent Mail
  # Outlook: read from "Sent Items"
  sent_folder = "[Gmail]/Sent Mail" if inbox.platform == "gmail" else "Sent Items"

  Bash:
    ~/.cargo/bin/himalaya envelope list \
      -a <himalaya_alias> -f "<sent_folder>" -o json --page-size 100 \
      -- 'after <last_voice_review_date>' 2>/dev/null

  For each envelope returned, fetch the full message body:
    Bash:
      ~/.cargo/bin/himalaya message read \
        -a <himalaya_alias> -f "<sent_folder>" <envelope.id> -o json 2>/dev/null

Extract:
  - Greeting patterns by recipient type
  - Sign-off patterns
  - Average length per audience
  - Tone range (formal ↔ casual)
  - Common phrases / structures
  - How user handles requests, follow-ups, difficult conversations
```

The envelope list returns headers only; you need `message read` to access the body. Batch the reads as parallel `Bash` calls to keep this fast — 100 sequential reads would be slow over IMAP.

### Source C: Slack (if connected)

```
mcp__claude_ai_Slack__slack_search_users (for user's own ID)
mcp__claude_ai_Slack__slack_search_public_and_private with from:me filter
date: since last_voice_review_date

Extract:
  - Tone by channel (public / DM / thread)
  - Emoji usage
  - Length by context
  - Feedback / question / acknowledgment patterns
  - Team-facing vs. client-facing tone differences
```

### Source D: iMessage (if connected)

```
AppleScript pull of sent messages since last_voice_review_date

Extract:
  - Casual tone patterns
  - Abbreviation / emoji usage
  - Personal vs. professional contact tone
  - Response patterns (length, speed, brevity)
```

### Source E: Draft edits (continuous)

```
Read voice corrections accumulated in contacts.md (under "Voice notes" sub-sections)
since last review.

These are direct, explicit signals of voice corrections. Highest signal-per-edit
because they reflect what the user changed AWAY FROM in a generated draft.
```

## Analysis Summary

After Phase A completes, present a summary to the user:

```
🎙️ Multi-source analysis since [last review date]:

  ✓ Fireflies: [N] transcripts ([H] hours of audio)
  ✓ Email: [N] sent messages across [M] inboxes
  ✓ Slack: [N] messages across [C] channels
  ✓ iMessage: [N] messages
  ✓ Draft edits: [N] voice corrections captured

DETECTED SHIFTS:
  • Tone has shifted slightly more [casual / formal] in [context]
  • New phrase: "[phrase]" — used [N] times in last [period]
  • Sign-off change: "[new]" appearing more than "[old]"
  • Greeting pattern: [observation]
  • [Any other detected drift]

[Areas where the profile seems outdated and could use A/B recalibration]:
  - [Scenario / audience that drifted]
  - [Scenario / audience that drifted]

[Continue to A/B calibration] [Quick review only — skip A/B]
```

If Quick review mode, skip A/B and go straight to Save (Phase C).

If drift-triggered mode, skip the menu — go straight to drift A/B (5 pairs scoped to drift scenarios).

---

## How A/B Calibration Works

The skill generates message pairs — Option A and Option B — for various scenarios. Each pair has the same intent but different tone, structure, or word choice. User picks which sounds more like them (or "neither" with explanation, or "both sound like me" to confirm a scenario is calibrated).

Preferences accumulate in the voice profile. When the user says "both sound like me" on a pair, that scenario is dialed in — move to the next.

### Pair format

```
─── A/B Pair [N] of [M] — Scenario: [description] ───

OPTION A:
[Generated message in style A]

OPTION B:
[Generated message in style B]

Which sounds more like you?
  [ ] A
  [ ] B
  [ ] Both — this scenario is calibrated, move on
  [ ] Neither — let me explain why
```

After each choice, log preference to voice profile. If "Neither" with explanation, capture the explanation as a free-form correction note.

---

## Batch 1: Core Email Scenarios (10 pairs)

For initial setup or Full review modes, run 10 pairs covering:

1. Responding to a client question
2. Following up on a missed deadline
3. Saying no to a meeting request
4. Thanking someone for their work
5. Introducing yourself to a new contact
6. Asking for a favor
7. Delivering bad news
8. Quick acknowledgment
9. Scheduling a call
10. Handling a complaint

Each pair generated with two distinct tonal approaches (e.g., direct vs. cushioned, brief vs. context-rich, warm vs. neutral).

### After each choice

Update voice profile:
- If user picks A consistently with pattern X → reinforce X in profile
- If user picks B consistently with pattern Y → reinforce Y
- If user mixes → that scenario benefits from contextual choice; note both styles

---

## Batch 2: Channel-Specific (recommended)

After Batch 1 refines the core email voice, run channel-specific pairs.

### Slack messages (5 pairs)

Shorter, more casual scenarios:
1. Quick yes/no to a teammate
2. Reacting to someone's update
3. Asking a teammate for help
4. Channel announcement
5. DM with a more formal external partner

### iMessage (5 pairs)

```
1. Quick check-in with spouse / close family
2. Plan-making with a friend
3. Brief professional reply over text
4. Acknowledgment ("got it", "thanks", etc.)
5. Apology / reschedule
```

### SMS messages (5 pairs)

Same as iMessage but for non-iMessage SMS — slightly more formal default since users tend to write SMS more carefully.

### Formal / client email (5 pairs)

For users in client-facing or business-development roles. Longer, more structured:
1. Proposal or pitch follow-up
2. Sensitive client question
3. Setting boundaries professionally
4. Closing a deal / next steps
5. Apologizing for a mistake

If BKC is connected and user has a brand voice, these pairs use the brand voice profile (`voice-profile-brand.md`) rather than personal voice.

---

## Continue Until Calibrated

After Batches 1 and 2:

```
You've completed [N] A/B pairs. Voice profile has been refined.

Want to continue with more pairs in any specific area?

  [ ] Yes — pick an area:
       [ ] Email (any scenario)
       [ ] Slack
       [ ] iMessage / SMS
       [ ] Formal/client (brand voice)
       [ ] Specific recipient (e.g., "more like Bryan")
  [ ] No — done for now
```

If user picks "specific recipient": pull recent emails to that recipient + relevant Fireflies transcripts (if any), generate 5 recipient-targeted pairs.

---

## Targeted Recalibration

If user picks "Targeted recalibration" mode, ask which area:

```
Which area needs recalibration?

  [ ] Email greetings
  [ ] Email sign-offs
  [ ] Slack tone
  [ ] iMessage register
  [ ] Brand / client-facing
  [ ] Specific scenario (describe in your words)
  [ ] Specific recipient
```

Generate 5 pairs scoped to the picked area. Run through them. Update voice profile. Done.

---

## Drift Recalibration

Triggered automatically at session end when `voice_drift_counter >= 3` in `.meta.json`.

```
🎙️ Quick drift recalibration

I noticed [N] substantial edits this session. Running a focused
5-pair A/B on the scenarios where you edited.

[Show pair 1 of 5]
```

How drift A/B picks scenarios:
1. Read the session log for substantial-edit events
2. Cluster edits by edit-type tag (tone / wording / structure / sign-off / cc)
3. Pick the 5 most common drift dimensions
4. Generate one A/B pair per drift dimension

After 5 pairs:
1. Update voice profile with new preferences
2. Reset `voice_drift_counter` to 0 in `.meta.json`
3. Log to session log:
   ```
   **HH:MM** — Drift A/B completed: 5 pairs, [N] preferences updated, drift counter reset
   ```

---

## Phase C: Save Voice Profile

After A/B calibration (or quick review without A/B):

1. **Update `voice-profile.md`** with:
   - All Phase A observations (drift detected, new phrases, sign-off changes, etc.)
   - All A/B pair results
   - Updated tone tables, signature phrases, NEVER list
   - New entry in `## Review History` table:
     ```
     | 2026-05-08 | Fireflies 14, email 247, Slack 412, iMessage 89, edits 5 | Tone shifted casual; new sign-off detected | 5 pairs |
     ```
2. **Update `voice-profile-brand.md`** if brand-voice pairs ran
3. **Update `.meta.json`:**
   - `last_voice_review` = today
   - `voice_drift_counter` = 0
   - `next_voice_review_due` = today + cadence
4. **Log to session log:**
   ```
   **HH:MM** — Voice review completed: [N] sources analyzed, [M] A/B pairs tested, profile updated
   ```
5. **Confirm:**
   ```
   ✓ Voice profile updated.
   
   Next mandatory review: [date] (cadence: [monthly/bi-weekly/weekly])
   You can run a manual recalibration anytime by saying "calibrate my voice".
   ```

---

## Notes for the skill

- **Fireflies first** — always weight Fireflies transcripts as primary signal. Other sources reinforce or refine, they don't override.
- **Edit-tracking is continuous** — drift counter increments during triage, not during calibration. Calibration just consumes the counter.
- **Generate pairs in parallel** — when running a batch, generate all pairs in one or few tool calls to keep it fast
- **Show pairs one at a time** — user attention drops after 3-4 simultaneous pairs; serial presentation works better
- **"Both sound like me" is a real signal** — that scenario is dialed in; don't keep grinding it. Move on.
- **Capture "Neither" explanations verbatim** — they're often the most useful corrections in the whole session
- **For brand voice users** — formal/client-facing pairs should use `voice-profile-brand.md`; everything else uses personal voice
- **Don't run drift recalibration during initial setup** — drift counter is 0 there; only fire it on subsequent sessions
