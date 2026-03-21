# Inbox Command Center — Changelog

## v1.2.0

### New Features

#### Cross-Device Sync via iCloud
- **Automatic iCloud sync** — All user data (config, voice profile, rules, VIP contacts) stored in iCloud Drive and synced across macOS devices automatically
- **Data path:** `~/Library/Mobile Documents/com~apple~CloudDocs/inbox-command-center/`
- **Zero-friction sync** — No manual pull/push needed; changes propagate within seconds
- **New device detection** — When the plugin finds an existing iCloud config from another device, it auto-syncs and verifies connections
- **Conflict handling** — Detects iCloud conflict copies and prompts user to resolve with a diff summary
- **Local fallback** — If iCloud Drive is unavailable, falls back to local storage with a warning
- **Setup:** New Step 0 in the setup wizard — choose iCloud sync or local-only storage

### Changes
- Triage now resolves the data path (iCloud → local fallback) before loading config
- Setup wizard detects existing iCloud config from other devices and skips to verification
- Config now tracks sync settings, storage path, and device list
- File structure documentation updated to distinguish plugin source vs. synced user data

### Setup Required for Existing Users
1. Run the setup wizard — Step 0 will offer to migrate your existing config to iCloud
2. On your second device, the plugin will auto-detect the synced config on first run

---

## v1.1.0

### New Features

#### iMessage Integration
- **Read & triage iMessages** alongside email and Slack in unified triage batches
- **Send iMessage replies** drafted in your authentic voice (calibrated via A/B testing)
- **iMessage as reminder channel** — receive scheduled reminders via iMessage instead of Slack
- **iMessage as briefing channel** — morning briefings delivered via iMessage
- **Connection:** macOS AppleScript/Shortcuts integration (requires Messages app configured)
- **Setup:** Added to Step 2 of the setup wizard — connect your iMessage ID (phone/Apple ID email), choose priority contacts, and set reminder preference

#### Scheduled Reminders System
- **Dedicated Slack channel** — Create a private `#inbox-reminders` channel (or custom name) to centralize all reminders in one visible log
- **Standalone reminder creation** — Say "Remind me to [task] at [time]" anytime, not just during triage
- **Recurring reminders** — "Remind me every Monday at 9am to check the report" with auto-scheduling
- **Per-reminder channel override** — Add `via imessage`, `via slack`, or `via channel` to any remind action
- **Three delivery channels:** Slack channel (recommended), Slack DM, or iMessage

#### Plugin Update Notifications
- **Automatic update detection** — Plugin compares installed version vs. current version on load
- **Update briefing** — Shows what's new, what needs setup, and guides you through configuring new features
- **Guided new-feature setup** — Walk through only the new/changed steps (not the full setup wizard)
- **Gentle reminders** — If you skip setup, a brief reminder appears on the next 3 triages

### Changes
- Triage batches now include iMessage items numbered after Slack (email #1-8, Slack #9-10, iMessage #11-12)
- Voice calibration adds 5 iMessage-specific A/B pairs for tone, emoji, and style
- Create Rule now supports platform filtering (Email / Slack / iMessage / All)
- Task tracker Source column now includes iMessage
- Briefing content now includes iMessage summary section
- Config now tracks Plugin Version, Reminder Delivery channel, and Slack reminder channel name

### Setup Required for Existing Users
1. **iMessage** — Run setup wizard Step 2 or say "connect iMessage" to configure
2. **Reminder channel** — Choose Slack channel, Slack DM, or iMessage as your default
3. **Slack reminder channel** — Optionally create `#inbox-reminders` for centralized reminder tracking

---

## v1.0.0

### Initial Release
- Email triage (Gmail via MCP, Outlook via Rube)
- Slack triage (MCP)
- Calendar triage (Google Calendar via MCP)
- Voice profile system (transcripts + sent emails + A/B calibration)
- Two-voice system (personal + brand via BKC)
- Rules engine (standard, custom, learned suggestions)
- VIP contacts with monthly review
- Task tracker (Google Sheet + Calendar events)
- Scheduled daily briefings (Slack DM, Email, Calendar)
- Quick action codes for rapid triage
- Brand Knowledge Center integration
