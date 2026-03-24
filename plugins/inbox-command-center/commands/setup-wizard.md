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

> "Let's connect your email. The connection method determines what I can do — including whether I can send replies directly or only create drafts:"
>
> **Option A: Gmail via Direct MCP** (simplest setup)
> - ✅ Read, search, draft, and label emails
> - ⚠️ Draft only — cannot send directly. You approve each draft and send it manually from Gmail.
> - Best for: users who want to stay in control of every send, no additional tool needed
>
> **Option B: Gmail via Rube** (full read + write)
> - ✅ Read, search, draft, label AND send directly on your behalf
> - ✅ After you approve a draft, I send it — no manual step required
> - Best for: users who want a fully hands-off workflow after approval
>
> **Option C: Outlook / Microsoft 365** — Connect via Rube (full read + write/send)
>
> **Option D: Other email providers** — Connect via Rube if they have an API
>
> **Recommendation:** If you want me to send replies after you approve them — not just draft them — connect Gmail via Rube. If drafts-only is fine, Gmail MCP is the simpler setup.
>
> "Which email account(s) do you want to manage? And how do you want to connect?"

For each account:
1. If Gmail MCP: detect if the Gmail MCP tool is available — test by searching for a recent email. Confirm draft-only capability.
2. If Gmail via Rube: guide through Rube connection setup. Test read and send capability.
3. If Outlook/365: connect via Rube. Full read + write available.
4. Ask: "Is this your primary sending account?" (for drafting replies)
5. If multiple accounts: "Which is primary? I'll draft replies from this account by default."
6. Note the send capability per account in config — used during triage to determine if direct send is available.

Save to config:
```
## Connected Accounts
| Tool | Connection | Account | Role | Send Capability |
|------|-----------|---------|------|----------------|
| Gmail | MCP | [email] | Primary | Draft only |
| Gmail | Rube | [email] | Primary | Full read + write |
| Outlook | Rube | [email] | Secondary | Full read + write |
| iMessage | AppleScript | [phone/email] | Messaging | Full read + write |
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
>
> **Via Rube** — Rube enables full read AND write access to platforms not available through Claude's built-in MCP tools:
> - **Microsoft Teams** — read and send messages
> - **WhatsApp Business** — read and send messages
> - **SMS/Text** — read and send via Twilio or similar
> - **Discord** — read and send
> - **Outlook / Microsoft 365 email** — full read + write/send (see Step 1)
> - **Other** — describe and we'll check if Rube can connect
> - **None** — skip
>
> Note: Rube is a bridge tool that connects to apps and services not natively available in Claude. If you haven't set up Rube yet, you can add these connections later — it's available as a free MCP tool.

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

> "Who are your most important contacts? I'll always flag their messages as priority. When a VIP emails you, I'll show the full email immediately with a pre-written draft reply ready for your review."

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

### VIP Review Cadence

> "How often do you want to review your VIP list? I'll check for new frequent contacts, inactive VIPs, and suggest changes."
>
> - **Monthly** (default) — Review on the first triage of each month
> - **Bi-weekly** — Every two weeks
> - **Weekly** — Every week
> - **Quarterly** — Every 3 months
> - **On demand only** — Only when you ask ("review my VIP list")

Save to config:
```markdown
## VIP Settings
- Review cadence: [monthly / bi-weekly / weekly / quarterly / on demand]
- Last reviewed: [date]
- Next review due: [date]
- Daily VIP summary: [Yes / No]
- VIP summary delivery: [Slack DM / iMessage / Email / All]
- VIP summary time: [HH:MM AM/PM]
```

### Daily VIP Summary

> "Want a daily summary of all VIP communications? This is a dedicated digest — separate from the morning briefing — that shows every VIP email received, sent, and pending for the day."
>
> - **Yes** (recommended) — Daily VIP summary delivered at your chosen time
> - **No** — VIP emails are still prioritized during triage, but no separate daily summary

If yes:
> "Where should I deliver it?"
> - Slack DM / iMessage / Email / All
>
> "What time?" (default: same as morning briefing)

### VIP Review Prompt

On the cadence the user selected, surface the VIP review:

```
📋 VIP REVIEW — Due for your [monthly / bi-weekly / weekly / quarterly] check-in

CURRENT VIPs: [count] contacts

ACTIVITY SINCE LAST REVIEW:
├── Most active: [Name] — [X] emails exchanged
├── Least active: [Name] — 0 emails in [period]
├── New frequent contacts not on VIP list:
│   ├── [Name] — [X] emails, avg response time [X] hours
│   └── [Name] — [X] emails
│
├── Inactive VIPs (0 emails in [period]):
│   ├── [Name] — still a VIP? [Keep / Remove]
│   └── [Name] — still a VIP? [Keep / Remove]

SUGGESTED ADDITIONS:
├── [Name] — [X] emails this period, you respond within [X] hours
│   Add as VIP? [Yes — relationship: ___] [No]

SUGGESTED CHANGES:
├── [Name] — priority notes still accurate? [Yes / Edit]

[Update list / Skip until next review / Change review cadence]
```

The review ensures the VIP list stays current as relationships evolve — new clients, departing team members, seasonal vendors, etc. Save the last review date in `inbox-command-center/config.md` to track cadence.

---

## Step 7: Set Up Task Tracker & Scheduled Briefing

### Task Tracker

> "Where do you want to track tasks and reminders from your inbox?"
>
> - **Apple Reminders** (recommended for Mac/iPhone users) — Built-in to every Apple device. No account, no signup, no setup beyond this conversation. Syncs automatically across Mac, iPhone, and iPad via iCloud. I'll create a list called "Inbox Tasks" and manage it directly.
> - **Markdown task list** — A `tasks.md` file stored right alongside your Inbox Command Center config (in iCloud or locally). No apps or accounts needed. Simple, always accessible, readable in any text editor.
> - **ClickUp** — If you already use ClickUp for project management. Free tier available. I can create and update tasks directly via Rube.
> - **Google Sheets** — Most flexible for filtering, sorting, and reporting. Requires a Google account.
> - **Calendar only** — No persistent task list — just creates calendar events as reminders. Lighter weight.
> - **Skip** — No task tracking.

For each option:

**Apple Reminders:**
1. Create a Reminders list called "Inbox Tasks" (or use an existing list the user names)
2. Confirm access via macOS Reminders API or Rube
3. Save to config: `task_tracker: apple-reminders | list: Inbox Tasks`

**Markdown task list:**
1. Create `tasks.md` in the user data directory (iCloud or local, matching the sync setting from Step 0)
2. Initialize with header row: ID, Created, Due, Source, From, Description, Priority, Status
3. Save to config: `task_tracker: markdown | path: [data-path]/tasks.md`

**ClickUp:**
1. Confirm Rube has ClickUp connected
2. Ask which workspace and list to use, or create a new "Inbox Tasks" list
3. Save to config: `task_tracker: clickup | list_id: [id]`

**Google Sheets:**
1. Search for existing "Inbox Task Tracker" sheet
2. If not found, offer to create one with the standard columns (ID, Created, Due, Source, From, Subject, Summary, Priority, Status, Completed, Notes)
3. Confirm and save link to config: `task_tracker: google-sheets | url: [url]`

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
> 7. **Unsubscribe handling:** When you mark something as UNSUBSCRIBE, how should I handle it?
>    - **Auto-execute** (recommended) — Execute the unsubscribe immediately using the email's List-Unsubscribe header (one-click) when available; extract the unsubscribe link from the body if not. Confirm once per sender then move on.
>    - **Batch at end of triage** — Queue all unsubscribes during triage, then execute them all together at the end so you're not interrupted mid-session.
>    - **Show me each one** — Surface the unsubscribe link for each sender and let you handle it manually.
>
> Save to config: `unsubscribe_mode: auto | batch | manual`

---

## Step 8b: Configure Folder Rules

> "I can automatically route certain emails into folders with their own review schedules — so noise stays out of your main triage but nothing gets lost."

**Present standard folders:**

```
RECOMMENDED FOLDERS:

📂 LOW PRIORITY — Non-urgent emails that don't need immediate attention
   Auto-routes: CC'd emails, vendor updates, internal FYI
   Review: Weekly digest summary
   Auto-cleanup: Archive after 30 days, delete after 90 days
   → [Enable / Skip / Customize]

📂 NEWSLETTERS — Newsletters you actually read
   Auto-routes: Known newsletter senders
   Review: Weekly digest
   Auto-cleanup: Delete after 14 days unread
   → [Enable / Skip / Customize]

📂 RECEIPTS & ORDERS — Purchase confirmations, shipping
   Auto-routes: Amazon, UPS, FedEx, Stripe, PayPal receipts
   Review: Never (searchable archive)
   Auto-cleanup: Keep indefinitely
   → [Enable / Skip / Customize]

📂 FINANCE — Bank alerts, invoices, payments
   Auto-routes: Bank domains, "invoice", "payment", "statement"
   Review: Daily digest summary
   Auto-cleanup: Keep indefinitely
   → [Enable / Skip / Customize]

📂 AUTOMATED/BOT — CI/CD, system alerts, app notifications
   Auto-routes: GitHub, Jira, no-reply addresses
   Review: Daily count only
   Auto-cleanup: Delete after 7 days
   → [Enable / Skip / Customize]

📂 PENDING REVIEW — Emails you want to come back to
   Auto-routes: Manual only (you route emails here during triage)
   Review: Every triage
   Auto-cleanup: Remind after 3 days
   → [Enable / Skip / Customize]

📂 DELEGATED — Forwarded emails awaiting someone else's response
   Auto-routes: Auto-created when you delegate during triage
   Review: Daily check
   Auto-cleanup: Remind after 5 days if no response
   → [Enable / Skip / Customize]

[Enable all recommended / Select specific ones / Create custom folder / Skip]
```

For each enabled folder, if the user chooses "Customize":
> - "What should be auto-routed here?" (senders, domains, keywords)
> - "How often should you review it?" (every triage / daily / weekly / monthly / never)
> - "How should it be reviewed?" (individual items / summary / count only)
> - "Auto-cleanup?" (archive after X days / delete after X days / keep / remind)

Save to `inbox-command-center/folder-rules.md`.

---

## Step 8c: Configure Rule Suggestion Review

> "As you use triage, I'll learn patterns and suggest new rules (like auto-deleting senders you always delete, or prioritizing senders you always respond to quickly). How often should I present these suggestions?"
>
> - **Every triage** — Show suggestions after each session
> - **Every 3rd triage** (default) — Show after every 3rd session
> - **Weekly** — Once per week at the start of the first triage
> - **Monthly** — Bundle into your monthly inbox report
> - **On demand only** — Only when you ask ("show rule suggestions")

Save to config under `Rule Suggestions`.

---

## Step 8d: Configure Inbox Report

> "I can generate a comprehensive inbox report on a regular schedule. It includes everything: emails sent, received, and deleted (broken down by manual vs. rule-based), response rates, VIP communication summaries, rule performance, folder activity, and trends."

> "How often do you want a report?"
> - **Monthly** (default) — First of each month
> - **Bi-weekly** — Every two weeks
> - **Weekly** — Every week
>
> "When should it be delivered?"
> - **Day:** [1st of month / last business day / specific day]
> - **Time:** [HH:MM AM/PM] (default: same as briefing)
>
> "How should it be delivered?"
> - **Email** (recommended) — Full report sent to your inbox
> - **Slack DM** — Condensed highlights with key numbers
> - **iMessage** — Brief summary with top stats
> - **All**

Save to config:
```markdown
## Inbox Report
- Cadence: [monthly / bi-weekly / weekly]
- Delivery: [Email / Slack DM / iMessage / All]
- Day: [1st of month / last business day / custom]
- Time: [HH:MM AM/PM]
- Last generated: none
```

---

## Step 8e: Configure Voice Profile Review

> "Your voice profile should be revisited regularly to stay accurate as your communication style naturally evolves. I'll re-analyze your recent emails, calls, Slack messages, and any edits you've made to drafts."
>
> "How often should we review your voice profile?"
> - **Monthly** (default, minimum) — Once per month
> - **Bi-weekly** — Every two weeks
> - **Weekly** — Every week

Save to config:
```markdown
## Voice Profile Review
- Review cadence: [monthly / bi-weekly / weekly]
- Last reviewed: [date]
- Next review due: [date]
- Review sources: [transcripts, email, slack, imessage]
```

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
├── Built from: [X] sent emails + [X] transcripts + [X] Slack msgs + [X] A/B pairs
├── Style: [summary]
├── Saved to: voice-profile.md
├── Auto-review: [monthly / bi-weekly / weekly]
├── Run /voice-calibration anytime to refine

VIP CONTACTS: [X] contacts across [X] categories
├── Review cadence: [monthly / bi-weekly / weekly / quarterly]
├── Daily VIP summary: [Yes — via [channel] at [time] / No]
├── VIP emails get immediate alert with pre-written draft

FOLDERS: [X] active folders
├── [List enabled folders with review cadence]

RULES: [X] active rules
├── Rule suggestion review: [every triage / every 3rd / weekly / monthly / on demand]

TASK TRACKER: [type + location]
BRIEFING: [delivery method] at [time] on [days]
REMINDER CHANNEL: [#inbox-reminders / Slack DM / iMessage]

INBOX REPORT: [monthly / bi-weekly / weekly] via [channel]

DAILY COMMANDS:
├── "Check my email" or "triage" — Full triage (VIP emails shown first with drafts)
├── "Any new emails?" — Quick scan since last check
├── "Draft a reply to [person]" — Compose in your voice
├── "Check Slack" — Slack triage
├── "Check iMessage" — iMessage triage
├── "Show my tasks" — Task tracker review
├── "Remind me to [task] at [time]" — Create a standalone reminder
├── /create-rule — Build a new message rule
├── /voice-calibration — Refine your voice profile
├── /inbox-report — Generate inbox activity report

SCHEDULED AUTOMATIONS:
├── 📊 Inbox report: [cadence] — next: [date]
├── 🎙️ Voice profile review: [cadence] — next: [date]
├── ⭐ VIP list review: [cadence] — next: [date]
├── ⭐ Daily VIP summary: [time] via [channel]

Ready to run your first triage? Say "triage" to start.
```
