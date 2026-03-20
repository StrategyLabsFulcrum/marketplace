# Inbox Command Center — Changelog

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
