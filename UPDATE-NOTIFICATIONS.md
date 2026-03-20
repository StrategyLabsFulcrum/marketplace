# Strategy Labs Plugin Marketplace — Update Notification System

When any Strategy Labs plugin is updated, users who install the new version receive a guided update notification that outlines what changed and helps them set up new features and connections.

## How It Works

### For Plugin Developers

Every plugin must maintain:

1. **Version in `plugin.json`** — Bumped with each release (semver: MAJOR.MINOR.PATCH)
2. **`CHANGELOG.md` in the plugin root** — Human-readable list of changes per version, structured with:
   - **New Features** — What was added, with a brief description of each
   - **Changes** — What was modified in existing behavior
   - **Setup Required for Existing Users** — Numbered list of new connections/configurations needed
3. **Version tracking in user config** — Each plugin's `config.md` stores:
   ```markdown
   ## Plugin Version
   - Installed: [version]
   - Last update acknowledged: [version]
   - Pending setup: [version or "none"]
   - Update reminder count: [0-3]
   ```

### For Users

When a plugin update is installed, the following happens automatically:

#### Step 1: Detect Update
On the next session or command invocation, the plugin compares:
- `Installed` version in config vs. the current plugin version in `plugin.json`
- If different (or if config has no version yet), an update has occurred

#### Step 2: Show Update Briefing
Before any other action, the plugin presents:

```
+--------------------------------------------------+
| [PLUGIN EMOJI] [PLUGIN NAME] — Updated to vX.Y.Z |
+--------------------------------------------------+

Here's what's new:

NEW FEATURES:
├── [Feature 1 with brief description]
├── [Feature 2 with brief description]
└── [Feature 3 with brief description]

CHANGES:
├── [Change 1]
└── [Change 2]

SETUP NEEDED:
├── 1. [New connection/tool] — [brief description] [Set up now]
├── 2. [New configuration] — [brief description] [Configure]
└── 3. [Optional feature] — [brief description] [Enable / Skip]

[Set up all new features] [Set up later] [Show full changelog]
```

#### Step 3: Guided Setup
If the user chooses to set up:
- Walk through **only the new/changed setup steps** — not the full setup wizard
- Pre-fill existing configuration values where possible
- Each step is optional and can be skipped
- After all steps (or skip), update config:
  ```markdown
  - Installed: [new version]
  - Last update acknowledged: [new version]
  - Pending setup: none
  - Update reminder count: 0
  ```

#### Step 4: Deferred Setup
If the user chooses "Set up later":
- Update config:
  ```markdown
  - Installed: [new version]
  - Last update acknowledged: [new version]
  - Pending setup: [new version]
  - Update reminder count: 0
  ```
- On the next 3 invocations of the plugin's primary command, show a brief one-line reminder:
  > "You have new features from v[X.Y.Z] that need setup. Say 'set up updates' to configure."
- After 3 reminders (tracked in `Update reminder count`), stop prompting
- User can always say "set up updates" or "what's new" to access the setup flow manually

### Notification Principles

1. **Non-blocking** — The update briefing is informational. The user can dismiss it and use the plugin normally.
2. **No repeated full prompts** — The full briefing shows once. After that, only the one-line reminder (up to 3 times).
3. **Incremental setup** — Only walk through what's new, never re-run the full setup wizard for an update.
4. **Respect existing config** — Never overwrite existing settings. Only add new configuration fields with sensible defaults.
5. **Cross-plugin consistent** — All Strategy Labs plugins follow this same pattern so users know what to expect.

### Universal Commands

These commands work in any Strategy Labs plugin after an update:

| Command | Action |
|---------|--------|
| "set up updates" | Run the guided setup for pending new features |
| "what's new" | Show the update briefing again for the current version |
| "show changelog" | Display the full CHANGELOG.md |
| "skip update setup" | Dismiss pending setup permanently for this version |

## Adding Update Notifications to a New Plugin

1. Add a `CHANGELOG.md` to the plugin root (see `inbox-command-center/CHANGELOG.md` for format)
2. Add `Plugin Version` tracking to the plugin's config template
3. Add version check logic to the plugin's "Before Starting" / initialization flow
4. Add the update briefing format to the plugin's SKILL.md
5. Bump version in both `plugin.json` and `marketplace.json` with each release
