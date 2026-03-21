# /team-setup

Interview the brand and recommend the right agent team from the Strategy Labs marketplace. Not every brand needs every agent. This command determines which plugins to install, which to skip, and why — based on business model, active channels, goals, and capabilities.

## How to Invoke

**Run after brand setup is complete:**
```
/team-setup
```

**Re-run to update recommendations after a strategy shift:**
```
/team-setup update
```

## What Happens

The agent asks a structured series of questions across 6 areas, then produces a recommended team roster with an explanation for each included and excluded agent.

## What You Get

- **Recommended agent stack** — which plugins to install, in priority order
- **Rationale for each** — why this agent fits your brand's situation
- **Agents to skip (for now)** — what you don't need yet and why
- **Suggested starting workflows** — the first 3 things to do with your new team
- **Team configuration file** — saved to `brand-intelligence-center/team-config.md`
