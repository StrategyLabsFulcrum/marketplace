# /brand-switch

Instantly switch the active brand context. All marketing skills will immediately work with the new brand.

## What This Does

1. Shows your full brand roster with status indicators
2. You select a brand (by number or name)
3. Copies that brand's files to the root `brand-intelligence-center/` folder
4. Re-assembles `system-prompt.md` for the selected brand
5. Confirms the switch — all skills are now loaded with the new brand's context

## When to Use

- Starting a new work session for a different client
- Switching between brands mid-session
- Confirming which brand is currently active

## How to Invoke

```
/brand-switch              → shows brand roster, pick by number or name
/brand-switch uno-mas      → switches directly to Uno Mas if you know the slug
```

## What You'll See

```
Active Brand Roster
───────────────────────────────────
  ★  1. Uno Mas              (restaurant) — last updated Mar 21
     2. Jones Hardware       (retail) — last updated Mar 14
     3. Bloom Skincare       (ecommerce) — last updated Feb 28

Switch to brand #, name, or press Enter to stay on Uno Mas:
```

The ★ marks the currently active brand. Brands are listed by most recently updated.

## After Switching

You'll see a confirmation:

```
✓ Switched to Bloom Skincare
  Brand context loaded. All marketing skills are now working with Bloom Skincare's profile.
  Run /brand-update to edit any section, or start a marketing task.
```

## Notes

- Switching is instant — no re-entering information
- Your previous brand's files are always saved in `brands/[slug]/`
- Run `/brand-list` to see the roster without switching
