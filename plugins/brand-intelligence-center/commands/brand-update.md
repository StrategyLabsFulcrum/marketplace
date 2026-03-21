# /brand-update

Update one or more areas of your Brand Intelligence Center without running the full wizard.

## What This Does

Reads your existing `brand-intelligence-center/` files, shows you what's captured in the area(s) you want to update, walks you through just those sections, and re-assembles `system-prompt.md` when done.

## When to Use

- After a rebrand or positioning shift
- When you add new products, services, or locations
- When you have new proof points, testimonials, or metrics
- When digital ecosystem changes (new tools, platforms, delivery partners)
- To fill in areas you skipped during initial setup

## How to Invoke

```
/brand-update                     → shows menu of all areas, pick what to update
/brand-update voice               → update brand voice & identity only
/brand-update customer            → update customer profile & psychology
/brand-update competitors         → update competitive landscape
/brand-update proof               → update proof points & goals
/brand-update digital             → update digital ecosystem
/brand-update financial           → update or add financial context
```

## What Gets Updated

Only the area(s) you select are changed. All other files stay the same. `system-prompt.md` is always re-assembled at the end to reflect any changes.
