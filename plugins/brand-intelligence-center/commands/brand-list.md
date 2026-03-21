# /brand-list

Show all brands in your roster with status and quick actions.

## What This Does

Displays your full brand roster with:
- Which brand is currently active
- Business type and last updated date for each brand
- Completion status (which of the 7 areas are filled in)
- Quick action options

## How to Invoke

```
/brand-list
```

## What You'll See

```
Brand Intelligence Center — Roster
────────────────────────────────────────────────────────
  ★  Uno Mas              restaurant   ████████░  8/8 areas   Mar 21
     Jones Hardware       retail       ██████░░░  6/8 areas   Mar 14
     Bloom Skincare       ecommerce    ████░░░░░  4/8 areas   Feb 28
────────────────────────────────────────────────────────
3 brands  |  Active: Uno Mas

Options:
  [S] Switch brand       → /brand-switch
  [A] Add new brand      → /brand-setup
  [U] Update a brand     → /brand-update
  [D] Delete a brand     → /brand-delete
```

## Completion Status

Each area is shown as filled (█) or empty (░):
1. Business Foundation
2. Customer Profile
3. Differentiation
4. Voice & Identity
5. Proof & Goals
6. Digital Ecosystem
7. Financial (optional)
8. System Prompt (assembled)

## Notes

- The ★ marks the currently active brand
- Incomplete areas can be filled in with `/brand-update`
- Financial (Area 7) shows as complete if explicitly skipped
