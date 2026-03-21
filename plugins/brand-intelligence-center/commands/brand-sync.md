# /brand-sync

Sync brand intelligence files between your local machine and a Fast.io workspace — so your whole team is always working from the same brand context.

## What This Does

Keeps `brand-intelligence-center/` in sync with a shared Fast.io workspace. Any team member can pull the latest brand files, make updates, and push them back for everyone else to use.

## When to Use

- **Pull** — at the start of a session to get the latest brand files your team has updated
- **Push** — after making changes to share them with the team
- **Status** — to see when files were last synced and whether anything might be stale

## How to Invoke

```
/brand-sync pull      ← download latest from Fast.io
/brand-sync push      ← upload local files to Fast.io
/brand-sync status    ← show sync state without changing anything
```

Just `/brand-sync` with no argument will ask which direction you want.

## First-Time Setup

The first time you run `/brand-sync`, it will:
1. Ask for your Fast.io workspace ID (or help you create one)
2. Create `.brand-intel-config.md` to store sync settings
3. Ask if you want auto-pull at session start

Your workspace ID can be found in Fast.io under workspace settings, or your team admin can share it with you.

## Multi-Brand / Agency Mode

In agency mode, sync works per-brand. The active brand's files sync to `brands/{{slug}}/` in the Fast.io workspace. Use `/brand-switch` to change the active brand, then `/brand-sync pull` to get the latest files for that brand.

## What Gets Synced

All files in `brand-intelligence-center/` for the active brand:
- `business.md`, `customer.md`, `differentiation.md`
- `voice-identity.md`, `proof-goals.md`, `digital-ecosystem.md`
- `financial.md` (if it exists)
- `system-prompt.md`
- `changelog.md`

Review documents (`review/`) are uploaded but not pulled — they're shared outbound only.

## Team Workflow

Recommended team pattern:
1. Session start → `/brand-sync pull` (get latest)
2. Make updates via `/brand-revise`
3. Session end → `/brand-sync push` (share with team)
4. Periodically → `/brand-review share` (generate fresh review doc for team)
