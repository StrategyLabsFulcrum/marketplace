# Setup Wizard

Complete onboarding for the Inbox Command Center — connect accounts, build voice profile, calibrate with A/B testing, set up VIP contacts, configure rules, task tracker, and scheduled briefings.

## Before Starting

1. **Check for existing iCloud sync:** Look for `~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/config.md`
   - If found: "Found your Inbox Command Center config synced via iCloud from another device. You're all set — want to verify connections on this device, or jump to `/triage`?"
   - Auto-detect device name and add to the devices list in config
   - Verify MCP connections (Gmail, Slack, etc.) are active on this device — prompt to re-authenticate any that aren't
   - Skip to Step 11 (Review & Activate) with existing config
2. Check if `inbox-command-center/config.md` exists locally.
   - If yes: "You've already set up the Inbox Command Center. Want to reconfigure, or jump straight to `/triage`?"
3. If no config found anywhere, start fresh setup. Create the data directory (location chosen in Step 0).

---

## Step 0: Cross-Device Sync

> "Do you use Claude on more than one device? I can sync your Inbox Command Center config, voice profile, rules, and VIP contacts across devices automatically."
>
> - **Yes, sync via iCloud** (recommended for Mac users) — Stores all user data in iCloud Drive so it's available on every Mac signed into the same Apple ID
>   - Checks that iCloud Drive is available: `~/Library/Mobile Documents/com~apple~CloudDocs/`
>   - Creates: `~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/`
>   - "What's this device? (e.g., MacBook Pro, iMac)" — saved to config for tracking
> - **No, keep local only** — Data stays in `inbox-command-center/` in the working directory. Fine for single-device use.
>
> Note: Your task tracker (Google Sheets), calendar events, and Slack messages already sync via their own cloud services. This setting controls your plugin config, voice profile, rules, and VIP contacts.

Save the choice to config:
```markdown
## Cross-Device Sync
- Enabled: Yes / No
- Storage: iCloud Drive / Local
- Path: [resolved path]
- Devices: [device name]
```

---

## Step 1: Connect Email

> "Let's connect your email. I can connect via:"
>
> **Direct MCP** — If Gmail is available in Claude's tool settings, it's the fastest:
> - Gmail: Read, search, draft, label — built into Claude
>
> **Rube** — For tools not available via MCP:
> - Outlook / Microsoft 365
> - Other email providers with API access
>
> "Which email account(s) do you want to manage?"

For each account:
1. Detect if the Gmail MCP tool is available — if so, test it by searching for a recent email
2. If not available, suggest: "Connect Gmail in Claude's MCP tool settings, or use Rube to connect via API"
3. Ask: "Is this your primary sending account?" (for drafting replies)
4. If multiple accounts: "Which is primary? I'll draft replies from this account by default."

Save to config:
```
## Connected Accounts
| Tool | Connection | Account | Role |
|------|-----------|---------|------|
| Gmail | MCP | [email] | Primary |
| Gmail | MCP | [email2] | Secondary |
| iMessage | AppleScript | [phone/email] | Messaging |
```

---

## Step 2: Connect Messaging Platforms

### Slack

> "Do you use Slack?"
> - **Yes** → Test Slack MCP connection. Ask for key channels to monitor and priority DMs.
>   - "Which channels should I always check?" (e.g., #team, #client-alerts)
>   - "Which channels should I skip?" (e.g., #random, #watercooler)
>   - "Any specific people whose DMs are always priority?"
> - **No** → Skip Slack.

### iMessage

> "Do you use iMessage?"
> - **Yes** → Test iMessage connection via macOS AppleScript/Shortcuts.
>   - Requires: macOS with Messages app configured and iMessage account active
>   - "What's your iMessage ID?" (phone number or Apple ID email)
>   - "Which conversations should I always check?" (e.g., specific contacts, group chats)
>   - "Any contacts whose iMessages are always priority?" (auto-matched with VIP list)
>   - "Would you like to receive scheduled reminders via iMessage instead of Slack?" (default: Slack)
> - **No** → Skip iMessage.

### Other Messaging Platforms

> "Do you use any other messaging platforms you'd like to connect?"
> - **Microsoft Teams** — via Rube
> - **WhatsApp Business** — via Rube
> - **SMS/Text** — via Rube (Twilio, etc.)
> - **Discord** — via Rube
> - **Other** — describe and we'll check if Rube can connect
> - **None** — skip

For each connected platform, configure:
- Priority contacts/channels
- Muted channels/groups
- Integration with triage batches (numbered alongside email)

---

## Step 3: Connect Calendar

> "Which calendar should I check for conflicts, unresponded invites, and meeting prep?"
>
> - **Google Calendar** — Auto-detected if Gmail is connected (MCP)
> - **Outlook Calendar** — via Rube
> - **Apple Calendar** — limited API, manual sync
>
> "What time zone are you in?" (auto-detect or ask)

Test the calendar connection by pulling today's events. Confirm:
> "Found [X] events on your calendar today. Connection is working."

---

## Step 4: Connect Meeting/Transcript Tools

> "Do you use any tools that record or transcribe your meetings? Connecting these lets me learn how you actually communicate — your phrases, tone, and style — so my drafts sound like you, not a template."

**Available via MCP:**
- Fireflies.ai — Meeting transcripts and summaries

**Available via Rube:**
- Otter.ai — Meeting transcripts
- Gong — Sales call recordings and transcripts
- Fathom — Meeting recordings and notes
- Zoom — Cloud recordings with transcripts
- Google Meet — Recorded meetings (via Google Drive)
- Loom — Video messages with transcripts

**None right now:**
> "No problem. I'll build your voice profile from sent emails and guided questions instead. You can connect transcript tools anytime later."

For each connected tool:
> "How far back should I analyze? (Last 30 days recommended for a solid voice profile)"

---

## Step 5: Build Voice Profile

### Phase A: Analyze Sources

**If transcript tools connected:**
1. Pull transcripts from the configured time range
2. Analyze for: greetings, closings, common phrases, tone shifts by audience, vocabulary, humor, sentence structure, filler words
3. Report: "Analyzed [X] transcripts. Found [X] unique phrases, [X] greeting patterns, tone ranges from [casual] to [formal]."

**Sent email analysis (always run):**
1. Search sent emails from the last 30-60 days
2. Analyze for: greeting patterns, sign-offs, email length, tone range, common phrases, structure
3. Report: "Analyzed [X] sent emails. Your emails average [X] sentences. Most common greeting: '[greeting]'. Most common sign-off: '[sign-off]'."

**Guided questions (fill gaps):**

> 1. "How do you typically greet people in emails?"
>    - Hey [Name], / Hi [Name], / [Name], / Depends on the person
>
> 2. "How do you sign off?"
>    - Thanks, [Name] / Best, [Name] / Talk soon / Just your name / Depends
>
> 3. "How would you describe your communication style?"
>    - Direct and to the point / Warm and conversational / Professional but approachable / Casual and friendly / Depends on who I'm talking to
>
> 4. "Words or phrases you'd NEVER use?"
>    - (e.g., "I hope this email finds you well", "Per my last email", "Synergy")
>
> 5. "Words or phrases you use all the time?"
>    - (e.g., "Let me know how you want to proceed", "Here's what I'm thinking")
>
> 6. "How long are your typical emails?"
>    - 1-2 sentences / A short paragraph / A few paragraphs / Depends
>
> 7. "When someone asks you something you don't know yet, how do you respond?"
>    - "Let me look into that" / "I'll get back to you" / "Good question — give me a day"

### Phase B: A/B Voice Calibration

After building the initial profile from analysis, calibrate with direct preference testing.

> "Now let's dial in your voice. I'll show you two versions of the same message. Pick the one that sounds more like you — or say 'neither' and tell me what's off."

**Batch 1: 10 Core Scenarios**

Generate two versions (A and B) for each scenario. Versions should differ in:
- Tone (slightly more formal vs. slightly more casual)
- Structure (direct opening vs. context-first)
- Length (concise vs. more detailed)
- Phrasing (different word choices for the same idea)

| # | Scenario |
|---|---------|
| 1 | Responding to a client question |
| 2 | Following up on something that's overdue |
| 3 | Saying no to a meeting request |
| 4 | Thanking someone for their work |
| 5 | Introducing yourself to a new contact |
| 6 | Asking for a favor |
| 7 | Delivering bad news or a delay |
| 8 | Quick acknowledgment ("got it, thanks") |
| 9 | Scheduling a call |
| 10 | Handling a complaint or frustration |

**Format for each pair:**

```
SCENARIO 3: Declining a meeting request

OPTION A:
"Hi Mark, I appreciate the invite but I'm going to have to pass on this one —
my calendar is stacked this week. Let me know if there's anything I can
review async instead. Thanks, [Name]"

OPTION B:
"Mark — thanks for thinking of me. Unfortunately I can't make this work
with my current schedule. Happy to catch up on the notes after, or if
there's a specific question for me, fire it over and I'll get back to you.
[Name]"

Which sounds more like you? [A / B / Neither]
```

After each choice, note the preference and update the voice profile.

After all 10, summarize:
> "Based on your choices, here's what I'm picking up:
> - You prefer [direct/contextual] openings
> - You lean [concise/detailed]
> - You're [more casual/more professional] than I initially thought
> - You [do/don't] use humor in declines"

**Batch 2: Channel-Specific (recommended after Batch 1)**

> "Now let me calibrate for different channels. Same format — pick A or B."

- 5 Slack message pairs (shorter, more casual, emoji usage)
- 5 SMS pairs (ultra-short, abbreviation tolerance)
- 5 formal email pairs (client-facing, proposals, longer-form)

**Continue until calibrated:**

After each batch, ask:
> "Want to do another round of calibration, or do both options sound like you at this point?"

When the user says both options sound right, that channel/scenario is dialed in. Continue offering new scenarios until the user confirms they're satisfied across all channels.

### Phase C: Generate Voice Profile

Compile all analysis + calibration results into `inbox-command-center/voice-profile.md` per the schema in SKILL.md.

Present a summary:
> "Your voice profile is built. Here's the snapshot:
> - **Style:** [summary]
> - **Greetings:** [pattern]
> - **Sign-offs:** [pattern]
> - **Tone range:** [casual end] to [formal end]
> - **NEVER says:** [list]
> - **Signature phrases:** [list]
>
> This will evolve as I learn from your edits and new transcripts."

---

## Step 6: Set Up VIP Contacts

> "Who are your most important contacts? I'll always flag their messages as priority."

### Auto-Detection

Scan sent emails from the last 30 days and rank contacts by:
- Frequency (most emails exchanged)
- Recency (most recent exchanges)
- Reply speed (contacts user responds to fastest — they're probably important)

Present top 15-20 as suggestions:

```
Based on your email activity, these appear to be your most important contacts:

SUGGESTED VIPs:
1. [Name] — [email] — [X] emails, you respond within [avg time]
   Suggested relationship: [Team / Client / Partner / Personal]
2. [Name] — [email] — [X] emails
   Suggested relationship: [guess based on domain/patterns]
3. ...

✓ Add all? Edit relationships? Add more manually?
```

For each VIP, capture:
- Name
- Email(s)
- Relationship: Team, Client, Partner, Family, Advisor, Vendor
- Priority notes (e.g., "Always respond same day", "CC [person] on replies")
- Voice override (e.g., "More formal with this person", "Very casual")

Save to `inbox-command-center/vip-contacts.md`.

### Monthly VIP Review

Set a recurring monthly review prompt. On the first triage of each month, surface:

```
📋 MONTHLY VIP REVIEW — It's been 30 days since your last review.

CURRENT VIPs: [count] contacts

ACTIVITY SINCE LAST REVIEW:
├── Most active: [Name] — [X] emails exchanged
├── Least active: [Name] — 0 emails in 30 days
├── New frequent contacts not on VIP list:
│   ├── [Name] — [X] emails, avg response time [X] hours
│   └── [Name] — [X] emails
│
├── Inactive VIPs (0 emails in 30 days):
│   ├── [Name] — still a VIP? [Keep / Remove]
│   └── [Name] — still a VIP? [Keep / Remove]

SUGGESTED ADDITIONS:
├── [Name] — [X] emails this month, you respond within [X] hours
│   Add as VIP? [Yes — relationship: ___] [No]

SUGGESTED CHANGES:
├── [Name] — priority notes still accurate? [Yes / Edit]

[Update list / Skip until next month]
```

The monthly review ensures the VIP list stays current as relationships evolve — new clients, departing team members, seasonal vendors, etc. Save the last review date in `inbox-command-center/config.md` to track cadence.

---

## Step 7: Set Up Task Tracker & Scheduled Briefing

### Task Tracker

> "Where do you want to track tasks and reminders from your inbox?"
>
> - **Google Sheet** (recommended) — Persistent list + Calendar event reminders
> - **ClickUp** — If you use it for project management
> - **Calendar only** — Lighter weight, just reminders
> - **Skip** — No task tracking

If Google Sheet:
1. Search for existing "Inbox Task Tracker" sheet
2. If not found, offer to create one with the standard columns
3. Confirm and save link to `inbox-command-center/task-tracker-link.md`

### Scheduled Daily Briefing

> "Want a daily briefing delivered automatically? Here's what it includes:"
>
> - Email summary (unread count, top 🔴 items)
> - Slack summary (if connected)
> - Calendar flags (conflicts, unresponded, marathon blocks)
> - Task reminders (due today, overdue)
> - Rules summary (auto-processed count)
>
> "How do you want it delivered?"
>
> - **Slack DM** — Message to yourself at a set time
> - **iMessage** — Text to yourself at a set time (requires iMessage connected)
> - **Email digest** — Summary email to your inbox
> - **Calendar block** — Recurring 15-min event with briefing in description
> - **All of the above**
> - **None** — I'll just be ready when you say "triage"
>
> "Where should I send scheduled reminders?" (when you say `remind [time]` during triage or create one standalone)
>
> - **Slack Channel** (recommended) — Post reminders to a dedicated channel for easy tracking
>   - "Create a new channel? I'd suggest `#inbox-reminders` (private). Or pick an existing channel."
>   - If yes: Create the private channel via Slack MCP. Confirm: "✓ Created #inbox-reminders. All reminders will post here."
>   - If existing: "Which channel?" → Confirm selection
> - **Slack DM** — Reminder sent as a Slack message to yourself
> - **iMessage** — Reminder sent as an iMessage to yourself
> - "You can override this per-reminder during triage by saying `remind tomorrow 9am via imessage` or `remind tomorrow 9am via slack`"
> - "You can also create reminders anytime by saying 'Remind me to [task] at [time]' — they'll be delivered to your chosen channel."
>
> "What time?" (default: 7:30 AM on weekdays)
> "Which days?" (default: Monday-Friday)

---

## Step 8: Configure Triage Preferences

> "A few preferences for how I manage your inbox:"
>
> 1. **Batch size:** How many messages per batch? (default: 10)
> 2. **Auto-junk social notifications?** LinkedIn, Instagram, Facebook, X (default: Yes)
> 3. **Newsletter handling:** Any newsletters you actually read? (everything else → junk)
>    - Ask for specific senders/domains to whitelist
> 4. **Quiet hours:** Hold non-urgent messages until morning? (default: 8 PM - 7 AM)
> 5. **Thread bundling:** Summarize long threads as one item? (default: Yes, for threads > 5 messages)
> 6. **Cross-platform dedup:** If someone emails AND Slacks about the same thing, show once? (default: Yes)

---

## Step 9: Standard Rules & Suggestions

Scan the user's inbox and suggest standard rules based on what's found:

> "I scanned your recent inbox and found some patterns. Here are rules I'd recommend:"

**Present rules grouped by category:**

```
RECOMMENDED RULES:

📱 SOCIAL NOTIFICATIONS (found [X] in last 30 days)
├── Rule: Auto-junk LinkedIn notifications → [Enable / Skip]
├── Rule: Auto-junk Instagram notifications → [Enable / Skip]
├── Rule: Auto-junk Facebook notifications → [Enable / Skip]
└── Rule: Auto-junk X/Twitter notifications → [Enable / Skip]

📦 TRANSACTIONAL (found [X])
├── Rule: Auto-archive Amazon order confirmations → Label "Orders" → [Enable / Skip]
├── Rule: Auto-archive shipping tracking emails → Label "Shipping" → [Enable / Skip]
└── Rule: Auto-archive payment confirmations → Label "Finance" → [Enable / Skip]

📣 MARKETING (found [X])
├── Rule: Auto-junk promotional emails from [top senders] → [Enable / Skip]
├── Rule: Auto-junk cold outreach / vendor pitches → [Enable / Skip]
└── Rule: Bundle newsletters into weekly digest → [Enable / Skip]

⭐ PRIORITY
├── Rule: VIP contacts always flagged as 🔴 RESPOND → [Enable / Skip]
├── Rule: Urgency keywords escalate to 🔴 HIGH → [Enable / Skip]
└── Rule: New senders flagged for verification → [Enable / Skip]

⏰ AUTOMATION
├── Rule: Stale follow-ups (sent, no reply in 3 days) → Create reminder → [Enable / Skip]
├── Rule: Calendar confirmations → Mark read, archive → [Enable / Skip]
└── Rule: Quiet hours ([X PM] - [Y AM]) → Hold for morning → [Enable / Skip]

Enable all recommended? Select specific ones? Skip for now?
```

After the user selects, save all enabled rules to `inbox-command-center/rules.md`.

> "Rules are active. You can create new rules anytime with `/create-rule`, and I'll suggest new ones based on your triage patterns."

---

## Step 10: Brand Knowledge Center Integration

> "Do you have a Brand Knowledge Center set up? If so, I can use your brand voice for client-facing and business emails, and your personal voice for everything else."
>
> - **Yes** → Check for `brand-knowledge-center/` folder. Load `brand-identity.md` voice guidelines.
>   - "Got it. I'll use your brand voice for emails to clients and business contacts, and your personal voice for internal and casual messages."
> - **No** → "No problem. I'll use your personal voice profile for everything. You can connect a Brand Knowledge Center anytime."

---

## Step 11: Review & Activate

```
Inbox Command Center — Setup Complete!

CONNECTED:
├── 📧 Email: [account(s)]
├── 💬 Slack: [workspace] ([X] priority channels, [X] muted)
├── 💬 iMessage: [phone/email] ([X] priority contacts)
├── 📅 Calendar: [type]
├── 🎙️ Transcripts: [tool] ([X] analyzed)
├── [Other messaging platforms]

VOICE PROFILE:
├── Built from: [X] sent emails + [X] transcripts + [X] A/B pairs
├── Style: [summary]
├── Saved to: voice-profile.md
├── Run /voice-calibration anytime to refine

VIP CONTACTS: [X] contacts across [X] categories
TASK TRACKER: [type + location]
RULES: [X] active rules
BRIEFING: [delivery method] at [time] on [days]

REMINDER CHANNEL: [#inbox-reminders / Slack DM / iMessage]

DAILY COMMANDS:
├── "Check my email" or "triage" — Full triage
├── "Any new emails?" — Quick scan since last check
├── "Draft a reply to [person]" — Compose in your voice
├── "Check Slack" — Slack triage
├── "Check iMessage" — iMessage triage
├── "Show my tasks" — Task tracker review
├── "Remind me to [task] at [time]" — Create a standalone reminder
├── /create-rule — Build a new message rule
├── /voice-calibration — Refine your voice profile

Ready to run your first triage? Say "triage" to start.
```
