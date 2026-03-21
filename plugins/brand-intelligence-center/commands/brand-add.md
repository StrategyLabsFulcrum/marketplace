# /brand-add

Add a new brand to your roster without losing your current active brand.

## What This Does

Runs the full Brand Intelligence Center setup wizard for a new brand, saves it to `brands/[new-slug]/`, then asks whether to switch to the new brand or stay on the current one.

## When to Use

- Onboarding a new client
- Adding a second location or sister brand
- Setting up a brand for a new project

## How to Invoke

```
/brand-add                         → starts wizard, asks for website URL
/brand-add https://unomas.com      → starts wizard pre-loaded with the URL
```

## What Happens

1. If currently in founder mode (single brand, no `brands/` subfolder), offers to convert:
   > "You're currently in single-brand mode. Adding a second brand will switch to agency mode — your existing brand data moves to `brands/[slug]/` automatically. Nothing is lost. Ready?"

2. Runs the full setup wizard for the new brand (scrape → confirm → fill gaps → assemble)

3. When complete, asks:
   > "**[New Brand]** is ready. Would you like to switch to it now, or stay on **[Current Brand]**?"
   >
   > `[ ]` Switch to [New Brand]
   > `[ ]` Stay on [Current Brand]

4. Updates the roster — run `/brand-list` to see all brands.

## Notes

- The wizard is identical to `/brand-setup` but saves to the agency folder structure
- The currently active brand is never interrupted until you choose to switch
- Brand slugs are auto-generated from the business name (e.g., "Uno Mas" → `uno-mas`)
