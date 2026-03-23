# /mail-setup

Configure the Mail Agent — set your inbox folder location, define routing contacts, connect notification channels, and set preferences.

Run this once to get started. Re-run anytime to update settings.

---

## Before Starting

1. Check for existing config: `~/Library/Mobile Documents/com~apple~CloudDocs/mail-agent/mail-config.md` (iCloud) or `mail-agent/mail-config.md` (local).
   - If found: "Found your Mail Agent config. Want to update settings, or jump straight to `/analyze-mail`?"
2. If no config found, start fresh.

---

## Step 0: Data Location

> "Where should I store your mail log and config?"
>
> - **iCloud Drive** (recommended) — syncs across all your Macs automatically
>   - Stores data at: `~/Library/Mobile Documents/com~apple~CloudDocs/mail-agent/`
> - **Local only** — stays on this machine
>   - Stores data at: `mail-agent/` in the current working directory

---

## Step 1: Mail Inbox Folder

> "Where will you drop scanned or photographed mail for me to analyze?"
>
> Provide a full folder path — this is where you'll drag and drop image files before running `/analyze-mail`.
>
> Suggestions:
> - `~/Desktop/mail-inbox/` — easy to access from anywhere
> - `~/Documents/mail-inbox/` — more organized
> - A custom path you specify
>
> I'll create this folder and a `_mail-processed/` subfolder alongside it.

After confirming:
1. Create `_mail-inbox/` at the specified path
2. Create `_mail-processed/` alongside it (organized by date after processing)
3. Create `_mail-archive/` for long-term storage
4. Save the path to config as `inbox_path`

> "✓ Inbox folder created at [path]. Drop your scanned mail there and run `/analyze-mail` to process it."

---

## Step 2: Routing Contacts

> "Who should different types of mail be routed to? I'll use this to tell you who each piece should go to — and can notify them directly if you have Slack or email connected."

For each category, ask who handles it. Skip categories that don't apply.

| Mail Type | Question |
|-----------|---------|
| Bills & Invoices | "Who handles bill payment and invoices?" |
| Financial / Bank Statements | "Who handles financial documents?" |
| Legal / Court Notices | "Do you have a legal contact or attorney?" |
| Government / Tax / IRS | "Who handles tax and government correspondence?" |
| HR / Employment | "Who handles HR and employment documents?" |
| Insurance / Medical | "Who handles insurance correspondence?" |
| Personal (named individual) | "Any team members who receive personal mail here?" |
| Default (unmatched) | "If I can't match a piece to a category, who should it go to by default?" |

For each contact, capture:
- Name
- Role
- Email (for email routing)
- Slack handle (for Slack routing)
- Note (e.g., "CC the CFO on anything over $5,000")

Save to `mail-config.md`:
```markdown
## Routing Contacts

| Type | Name | Email | Slack | Notes |
|------|------|-------|-------|-------|
| Bills & Invoices | [name] | [email] | @[handle] | |
| Legal | [name] | [email] | @[handle] | |
| Government / Tax | [name] | [email] | @[handle] | |
| HR / Employment | [name] | [email] | @[handle] | |
| Insurance | [name] | [email] | @[handle] | |
| Default | [name] | [email] | @[handle] | |
```

---

## Step 3: Notification Delivery

> "When I finish analyzing a batch of mail, how do you want to receive the triage report?"
>
> - **In this conversation** — I'll show the full report here (always available)
> - **Slack DM** — I'll also send a summary to your Slack DM
> - **Slack channel** — Post to a specific channel (e.g., `#mail-triage`)
> - **Email digest** — Send a summary email to a specified address
> - **All of the above**
> - **Conversation only** — no additional notifications

If Slack: test the Slack MCP connection. Ask for channel/DM preference.
If email: ask for the destination address.

Save to config: `notification_method: [conversation / slack-dm / slack-channel / email / all]`

---

## Step 4: Urgency Preferences

> "A few preferences for how I flag and handle urgent mail:"
>
> 1. **Urgent threshold:** What counts as urgent?
>    - Legal deadline within **7 days** (default) / 14 days / 30 days
>
> 2. **Past-due escalation:** If something is past due, who should I notify immediately?
>    - [contact name / skip]
>
> 3. **Certified mail flagging:** Flag all certified mail as urgent regardless of content?
>    - Yes (default) / No
>
> 4. **Shred confirmation:** Should I ask before marking marketing/junk as safe to shred?
>    - Always ask (default) / Auto-approve discards

---

## Step 5: Scanning Guidance

> "Last thing — here's how to get the best results when scanning or photographing mail:"

Display scanning tips:
```
SCANNING TIPS FOR BEST RESULTS:

📄 ENVELOPES
├── Scan or photograph the front of the envelope first
├── Include the full return address and addressee
└── Name files: letter-01-envelope.jpg, letter-02-envelope.jpg...

📃 LETTERS
├── Scan each page separately if multi-page
├── Name pages: letter-01-page1.jpg, letter-01-page2.jpg...
├── Lay flat — avoid shadows and curved edges
└── Minimum resolution: 200 DPI for readable text

📱 PHONE PHOTOS
├── Good lighting — natural light works best
├── Hold the phone directly above, not at an angle
├── Make sure all four corners are visible in the frame
└── Take 2 photos if the first looks blurry

📁 FILE NAMING
├── Group pages from the same piece with the same prefix
├── Envelope + letter from same piece: letter-01-envelope.jpg, letter-01-page1.jpg
└── Or just drop everything in the folder — I'll group related files automatically
```

---

## Step 6: Confirm & Activate

```
✓ Mail Agent — Setup Complete

INBOX FOLDER:     [path]
PROCESSED FOLDER: [path/_mail-processed/]
ARCHIVE FOLDER:   [path/_mail-archive/]

ROUTING:
├── Bills & Invoices  → [name]
├── Legal             → [name]
├── Government / Tax  → [name]
└── Default           → [name]

NOTIFICATIONS: [method]
URGENT THRESHOLD: [X] days

Config saved to: [data-path]/mail-config.md

COMMANDS:
├── /analyze-mail        — Process everything in your inbox folder
├── /analyze-mail [file] — Analyze a specific file or folder path
├── /mail-setup          — Update these settings anytime

Ready. Drop mail into [inbox path] and run /analyze-mail.
```
