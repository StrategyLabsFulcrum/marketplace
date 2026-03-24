# Voice Calibration

Refine your voice profile through multi-source analysis and A/B message comparison. Run during initial setup, anytime to improve how drafts sound, or as part of the mandatory monthly/bi-weekly/weekly voice review.

Triggers on: "calibrate my voice", "refine my voice", "voice calibration", "drafts don't sound like me", "fix my voice profile", "voice review", "update my voice"

## Before Starting

0. **Resolve data path:** Check for iCloud sync first: `~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/config.md`. If found, use the iCloud path. Otherwise, fall back to `inbox-command-center/` locally.
1. Load existing voice profile from `[data-path]/voice-profile.md`.
   - If it exists: "Your current voice profile was last updated [date]. Let's refine it."
   - If not: "No voice profile found. Run `/setup-wizard` first, or I can build one from scratch here."
2. Load VIP contacts from `[data-path]/vip-contacts.md` for audience-specific scenarios.
3. Check if this is a **scheduled review** (triggered by the mandatory monthly/bi-weekly/weekly cadence) or a **manual run**.
   - If scheduled: Start with multi-source re-analysis (Step 0b) before A/B calibration.
   - If manual: Skip re-analysis unless the user requests it, go straight to A/B calibration.

---

## Step 0b: Multi-Source Re-Analysis (scheduled reviews)

When triggered by the mandatory review cadence, re-analyze all connected sources before A/B calibration:

> "Time for your [monthly / bi-weekly / weekly] voice profile review. Let me re-analyze your recent communications first."

### Source Analysis

1. **Phone calls / Meeting transcripts** — Pull new transcripts since last review from Fireflies, Otter, Gong, Fathom, or Zoom.
   > "Found [X] new transcripts since your last review. Analyzing for speech patterns, tone, and new phrases..."

2. **Sent emails** — Analyze emails sent since last review.
   > "Analyzed [X] sent emails. Detected [changes / no significant changes] in tone and phrasing."

3. **Slack messages** — Analyze sent Slack messages since last review.
   > "Analyzed [X] Slack messages across [X] channels. Your Slack tone has [shifted / stayed consistent]."

4. **iMessage / SMS** — If connected, analyze sent messages since last review.
   > "Analyzed [X] iMessages. Your casual communication style has [shifted / stayed consistent]."

5. **Draft edits** — Compile all edits the user made to plugin-generated drafts since last review.
   > "You edited [X] drafts since last review. Key corrections: [list top changes]."

### Analysis Summary

```
🎙️ VOICE RE-ANALYSIS COMPLETE

SOURCES ANALYZED:
├── 🎙️ Transcripts: [X] new (calls, meetings)
├── 📧 Sent emails: [X] new
├── 💬 Slack messages: [X] new
├── 📱 iMessages: [X] new
├── ✏️ Draft edits: [X] corrections captured

DETECTED CHANGES:
├── [Change 1 — e.g., "Your email tone has shifted slightly more casual"]
├── [Change 2 — e.g., "New phrase: 'let's circle back on this' — used 8 times"]
├── [Change 3 — e.g., "Sign-off shift: 'Cheers' replacing 'Thanks' in casual emails"]
└── [Change 4 — or "No significant changes detected"]

PROFILE UPDATES:
├── ✅ Updated: [list of profile sections updated automatically]
├── ❓ Needs calibration: [areas where A/B testing would help]
└── ⚠️ Conflict: [any contradictory signals — e.g., more formal in email but more casual in Slack]

[Continue to A/B calibration] [Accept updates, skip calibration] [Show full analysis]
```

After re-analysis, proceed to A/B calibration focused on areas that need refinement.

---

## How A/B Calibration Works

For each scenario, the plugin generates two message drafts (A and B) that differ in:
- **Tone** — slightly more formal vs. slightly more casual
- **Structure** — direct opening vs. context-first
- **Length** — concise vs. more detailed
- **Phrasing** — different word choices for the same idea
- **Personality** — warmer vs. more businesslike

The user picks which sounds more like them. Each choice updates the voice profile.

---

## Batch 1: Core Email Scenarios (10 pairs)

> "I'll show you two versions of the same message. Pick the one that sounds more like you — or say 'neither' and tell me what's off."

### Pair Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCENARIO 1 of 10: Responding to a client question

Context: A client asked about timeline for a deliverable that's
running behind schedule.

OPTION A:
───────
Hey Sarah,

Good question — we're running about a week behind on the mockups.
The designer hit a snag with the asset exports but we're past it now.
You should have the first round by Thursday.

Let me know if that works or if we need to adjust.

Thanks,
[Name]

OPTION B:
───────
Hi Sarah,

Thanks for checking in on this. We ran into a delay on the mockup
phase — our designer encountered an issue with asset exports that
set us back about a week. That's been resolved and we're back on
track.

I'm targeting Thursday for the first round of mockups. Does that
timeline work for you, or should we discuss reprioritizing?

[Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Which sounds more like you? [A / B / Neither]
```

### 10 Core Scenarios

| # | Scenario | What It Tests |
|---|---------|---------------|
| 1 | Responding to a client question | Professional tone, how they handle delays |
| 2 | Following up on something overdue | Directness vs. diplomacy |
| 3 | Saying no to a meeting request | Declining gracefully, boundary setting |
| 4 | Thanking someone for their work | Warmth level, specificity of praise |
| 5 | Introducing yourself to a new contact | First impression tone, formality level |
| 6 | Asking for a favor or help | Vulnerability vs. directness |
| 7 | Delivering bad news or a delay | Honesty style, accountability language |
| 8 | Quick acknowledgment (got it, thanks) | Brevity tolerance, one-liner style |
| 9 | Scheduling a call or meeting | Efficiency, how they propose times |
| 10 | Handling a complaint or frustration | Empathy vs. problem-solving orientation |

### After Each Choice

Note the preference silently. After all 10:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BATCH 1 RESULTS — Here's what I'm picking up:

✓ You prefer direct openings — you get to the point fast
✓ You lean casual-professional — warm but not corporate
✓ Your emails are concise — you rarely go past 4-5 sentences
✓ You sign off with "Thanks, [Name]" — not "Best regards"
✓ You take ownership of problems — "we're running behind" not "there was a delay"
✓ You always include a clear next step
✗ You don't use "I hope this finds you well" or long preambles
✗ You don't over-apologize — you acknowledge and redirect

Voice profile updated.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Batch 2: Channel-Specific (recommended)

> "Now let's calibrate for different channels. Your tone might shift on Slack vs. iMessage vs. email vs. text."

### Slack Messages (5 pairs)

Test for:
- Length (one-liner vs. short paragraph)
- Emoji usage (yes/no, which ones)
- Formality (hey vs. hi vs. no greeting)
- Thread etiquette (respond in-thread vs. new message)
- Reaction vs. response (thumbs up vs. "got it")

```
SCENARIO S1: Acknowledging a Slack message from a teammate

Context: Your teammate shared a completed deliverable in Slack.

OPTION A:
"Nice work 👍 I'll review this afternoon"

OPTION B:
"Looks great, thanks for getting this done. I'll take a look this afternoon and follow up if I have questions."

Which sounds more like you? [A / B / Neither]
```

### iMessage (5 pairs)

Test for:
- Tone difference from Slack (iMessage is often more personal)
- Emoji and tapback usage
- Response length for personal vs. professional iMessage contacts
- How style shifts between 1:1 and group chats

```
SCENARIO iM1: Responding to a friend/contact asking for a quick favor via iMessage

OPTION A:
"Yeah for sure — send me the details and I'll take a look tonight"

OPTION B:
"Sure thing! I'll check it out later today 👍"

Which sounds more like you? [A / B / Neither]
```

### SMS Messages (5 pairs)

Test for:
- Abbreviation tolerance (thx vs. thanks, u vs. you)
- Emoji/punctuation style
- Response length
- Formality level

```
SCENARIO T1: Confirming a meeting time via text

OPTION A:
"Sounds good, see you at 2"

OPTION B:
"Perfect — 2pm works. See you there."

Which sounds more like you? [A / B / Neither]
```

### Formal/Client Email (5 pairs)

Test for:
- How much more formal they go for clients vs. internal
- Proposal/SOW language style
- How they handle money conversations
- Sign-off formality shift

```
SCENARIO F1: Sending a proposal to a potential client

OPTION A:
"Hi David,

Great talking with you yesterday. Here's the proposal we discussed —
I kept it straightforward so you can see exactly what you're getting
and what it costs.

Take a look when you get a chance and let me know your thoughts.
Happy to jump on a call to walk through anything.

[Name]"

OPTION B:
"David,

Following up on our conversation. Attached is the proposal outlining
scope, timeline, and investment. I've structured it around the three
priorities you mentioned — lead gen, content, and reporting.

Let me know if you'd like to discuss or if you have questions on
any of the line items. I'm available Thursday or Friday for a call.

All the best,
[Name]"

Which sounds more like you? [A / B / Neither]
```

---

## Continue Until Calibrated

After each batch, ask:

> "Want to do another round? I can generate more scenarios for:"
> - Specific situations you encounter often
> - A particular audience (e.g., "how I talk to my accountant")
> - A specific channel that needs more refinement
> - Tricky situations (negotiations, apologies, pitches)
>
> Or if both options are sounding like you at this point, we can stop — your profile is dialed in.

**Completion signal:** When the user says "both sound like me" on 3+ consecutive pairs, or explicitly says they're satisfied:

> "Voice profile calibrated. Here's your updated profile summary:"
> [Show summary from voice-profile.md]
>
> "I'll use this for all drafts going forward. If a draft ever feels off, just edit it — I'll learn from the changes. You can run `/voice-calibration` anytime to refine further."

---

## Targeted Recalibration

When the user edits drafts during triage, track the changes. If the same type of edit happens 3+ times:

> "I've noticed you keep making similar edits to [type] messages:
> - You shortened my drafts 3 times this week
> - You changed my greeting from 'Hi' to 'Hey' twice
>
> Want to run a quick recalibration? I'll generate 3 pairs focused on [the pattern] to lock it in."

This keeps calibration lightweight and targeted rather than requiring a full re-run.

---

## Save Voice Profile

After every calibration session, update `[data-path]/voice-profile.md`:

1. Update the `A/B Calibration Results` section with new preferences
2. Adjust any core style descriptions that changed
3. Update channel-specific differences if new data
4. Update the `Last updated` timestamp
5. Add entry to the `Review History` table with sources analyzed, key changes, and A/B pairs tested
6. Update config: set `voice_profile_last_reviewed` to today, calculate next review due date
7. Confirm:
   > "Voice profile updated. Next review due: [date].
   > Sources analyzed: [X] transcripts, [X] emails, [X] Slack messages, [X] iMessages, [X] draft edits.
   > Key changes: [brief summary].
   > I'll remind you when your next review is due."
