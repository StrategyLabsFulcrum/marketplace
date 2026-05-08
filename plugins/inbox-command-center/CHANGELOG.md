# Inbox Command Center — Changelog

## v1.4.0

### Headline

The largest update to date. Composio replaces Rube as the connection layer, multi-account email lands, the workspace becomes a Finder-visible folder full of hand-editable markdown, and Fireflies is elevated to the primary signal for ongoing voice and client context.

### New Features

#### Composio replaces Rube
- **Single connection layer** for Gmail, Outlook, Otter, Gong, Fathom, and Outlook Calendar via Composio (`mcp__claude_ai_Composio__COMPOSIO_MULTI_EXECUTE_TOOL`)
- **Rube fully removed** — all `Rube:RUBE_MULTI_EXECUTE_TOOL` calls migrated to Composio equivalents
- **Native MCPs kept** for Slack, Google Calendar, and Fireflies (richer feature surface than Composio wrappers today)
- **Native Gmail MCP fallback** still available for users who can't / won't use Composio — limited to single Gmail account, no Outlook, no multi-platform
- **Strategy Labs onboarding path** — new users at SL email scott@strategylabs.us to be added to the team Composio account; setup wizard documents the flow

#### Multi-account email
- **N Gmail + N Outlook accounts per user** via Composio's multi-account auth flow
- **`.meta.json.connected_inboxes[]`** tracks each account with alias, platform, and address
- **Sequential triage by default** — user picks which inbox to triage per session
- **VIP cross-inbox scan at session start** — surfaces VIP messages across all inboxes before sequential triage begins
- **Aggregated daily briefing** with per-inbox sections; **separate VIP digest per inbox**
- **Single inbox report** with per-inbox sections plus cross-inbox section for unified entities (VIPs, voice, global rules)

#### Hand-editable workspace
- **`~/Inbox Command Center/`** — workspace folder moves out of the hidden iCloud slug path to a Finder-visible iCloud-synced location
- **`contacts.md`** — new per-recipient memory file for tone notes, VIP status (`[VIP]` section tag), interaction timeline, and Fireflies-derived context
- **`todos.md` + `followups.md`** — replace the old Google-Sheet-or-markdown task tracker with two purpose-built files (todos = things you owe yourself; followups = people waiting on you)
- **`session-logs/YYYY-MM-DD.md`** — daily append-only log of meaningful events, including agent actions and detected user edits to workspace files
- **`.meta.json`** — bookkeeping (last_rule_review, session_count, connected_inboxes, last_fireflies_pull)
- **Setup wizard ends with workspace tour** — walks user through their Finder folder so the file model is concrete

#### Fireflies as primary voice/context signal
- **Elevated from optional to recommended** in the setup wizard with explicit framing about ongoing voice authenticity
- **30-day blocking pull during setup** seeds the voice profile from real meetings before first triage
- **Weekly Fireflies pull** as a new scheduled automation — voice extraction (Pass 1) + per-participant tone observations into `contacts.md` (Pass 2)
- **`contacts.md` population scope** — only VIPs and people in your sent mail; transcript participants outside that set don't auto-create entries
- **Triage-time enrichment** — when an email arrives from someone you spoke with on Fireflies in the last 30 days, surface "you spoke with X on Y about Z" inline

#### Two-stakes rules overlay
- **Every rule now has both a type and a stakes level** — `low_stakes` (auto-apply silently) or `high_stakes` (always confirm even after approval)
- **Defaults:** label/route/trash/unsub/prioritize → low_stakes; permanent-delete/auto-reply/auto-forward → high_stakes
- **Existing v1.3 rules auto-tagged** during migration with conservative defaults; user reviews on next rule cycle
- **Per-inbox rule scope by default** with explicit `[global]` flag for cross-inbox rules; VIP-related rules are inherently global

#### Drift-triggered voice calibration
- **Auto-offer mini A/B at session end** when 3+ substantial draft edits are detected in one session
- **Catches voice drift early** without waiting for the monthly review

### Changes
- Skill rewrites every Rube tool call to the Composio equivalent (`COMPOSIO_MULTI_EXECUTE_TOOL` with the same Gmail/Outlook tool slugs)
- Setup wizard adds a Composio prerequisite step (0a) before email connection
- Setup wizard supports adding multiple inboxes per platform; per-inbox folder enablement
- Folder routing now uses a synthetic abstraction — Gmail labels (`ICC/Newsletters`) on Gmail accounts, native subfolders (`Inbox/ICC/Newsletters`) on Outlook/IMAP
- VIP data migrates from `vip-contacts.md` into unified `contacts.md` with `[VIP]` section tag
- Task tracker data migrates from `tasks.md` / Google Sheet / ClickUp into `todos.md` + `followups.md` (Apple Reminders / Google Calendar event creation for time-bound todos preserved)
- Inbox report cadence and structure unchanged; data sourcing now reads session-logs as primary feed
- Default folder set unchanged (7 folders); enablement is per-inbox
- Voice profile sources reordered — Fireflies first, sent email second; A/B calibration and mandatory monthly review preserved
- Two-voice system (personal + brand via BKC) preserved; brand-voice contacts now tagged `[Brand]` in `contacts.md`
- Plugin update notification system (v1.1) extended to handle the v1.3 → v1.4 targeted migration flow

### Removed
- **Rube** — fully replaced by Composio
- **`vip-contacts.md`** — data merges into `contacts.md`
- **`tasks.md` and `task-tracker-link.md`** — replaced by `todos.md` + `followups.md`

### Deferred to v1.5
- **iCloud Mail** and **Generic IMAP** support — requires a new IMAP adapter; scoped out of v1.4 to keep the release focused

### Setup Required for Existing Users
1. Run the setup wizard — it detects v1.3 state and runs a targeted migration (workspace path move, vip-contacts → contacts, tasks → todos/followups, rules tagged with stakes)
2. **Composio account required** for full features. SL team members: email scott@strategylabs.us for team-account access. External users: walk through composio.dev signup (~3 min)
3. **Gmail re-auth** required (moving from native MCP to Composio); Outlook users on Rube also need to re-auth via Composio
4. **Connect Fireflies** if not already connected — biggest single voice-profile improvement
5. Optional: enable additional inboxes via the new multi-account flow
6. Optional: hand-edit `~/Inbox Command Center/contacts.md` to add per-recipient tone notes

---

## v1.3.0

### New Features

#### VIP Immediate Alerts
- **VIP emails surface first during triage** with full body and pre-written draft reply (in your voice + relationship-appropriate tone)
- **Quick-check awareness** — "any new emails?" always shows VIP messages, even when the rest of the inbox is clear
- **Pre-written drafts** generated automatically from email content + sender relationship + thread context + voice profile

#### Daily VIP Communication Summary
- Dedicated daily digest of all VIP communications: received, sent, active threads, pending replies
- Configurable delivery channel (Slack DM / iMessage / email / all) and time
- Separate from (and additional to) the morning briefing

#### Folder-Based Rules
- Seven default folders with custom review cadences and auto-actions: Low Priority, Newsletters, Receipts & Orders, Finance, Automated/Bot, Pending Review, Delegated
- **Low Priority folder** with weekly digest, archive-after-30d, delete-after-90d defaults
- Per-folder review cadence, review style (individual / summary / count), and notification routing
- Stored in `folder-rules.md`

#### Enhanced Rule Suggestions
- Three suggestion categories: **delete rules**, **prioritization rules**, **organization rules**
- **User-selectable review cadence** — every triage / every 3rd / weekly / monthly / on demand
- Pattern-driven suggestions (junked-3+-times, response-within-1h, always-forwarded, etc.)

#### Monthly Inbox Report
- New `/inbox-report` command for on-demand and scheduled analytics
- Sections: email volume, deletion breakdown (manual vs. rule vs. folder cleanup), read-but-not-responded, VIP communications, rules performance, folder activity, trends, period comparison
- Stored in `reports/[YYYY-MM].md`; configurable cadence (monthly / bi-weekly / weekly)

#### Mandatory Monthly Voice Profile Review
- Voice profile **must** be revisited at least once per month (cadence configurable to weekly / bi-weekly)
- Multi-source re-analysis: phone calls, email, Slack, iMessage, draft edits
- Drift detection (tone shifts, new phrases, sign-off changes) with targeted A/B recalibration
- Voice profile version history tracks each review

#### 5-Source Voice Profile
- Voice profile now built from: meeting transcripts, sent email, Slack messages, iMessage / SMS, A/B calibration
- Phone-call transcripts weighted highest as the most authentic voice signal

### Changes (Workflow Improvements bundled into v1.3)

#### Gmail MCP vs. Rube — capability table
- Setup wizard now distinguishes Gmail via MCP (draft-only) vs. Gmail via Rube (full read + write/send)
- Triage send-prompt adapts: "Save as Draft" for MCP-only, "Send" for Rube-connected accounts

#### Batch Draft Approval
- All drafts in a triage batch generated in parallel and presented together
- Approve all at once or edit individually

#### Unsubscribe Execution (not just flagging)
- **List-Unsubscribe header** (one-click) — `mailto:` or `https://` execution
- **Body link extraction** as fallback
- **Auto-junk rule** if no unsubscribe mechanism found
- Three modes: `auto` (immediate), `batch` (end of triage), `manual` (surface only)

#### Task Tracker — Multi-Backend
- Four supported backends: **Apple Reminders** (recommended for Mac users), markdown file, ClickUp, Google Sheets, calendar-only
- Same task data model across all backends
- Calendar event creation for time-bound tasks preserved across backends

#### VIP Review Frequency
- Configurable at setup: 14 / 30 / 90 / never days
- Stored in config under `VIP Review`

#### Dual-Source Email Scanning
- Every email operation queries both Gmail MCP and all Rube-connected accounts in parallel; results merged and deduplicated

### Setup Required for Existing Users
1. Run the setup wizard to configure new features (folder rules, rule suggestion cadence, inbox report cadence, voice review cadence)
2. Optional: enable Apple Reminders as task tracker backend (Mac users)
3. Optional: connect Fireflies / Otter / Gong for richer voice profile sources

---

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
