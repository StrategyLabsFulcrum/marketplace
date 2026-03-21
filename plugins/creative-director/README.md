# Creative Director

Orchestrates all creative execution for a campaign. The Creative Director develops the unifying creative concept, issues tailored specialist briefs, reviews every output against the brand rubric, runs all copy through the Copy Editor, and assembles the final creative package.

**The Creative Director does not write copy or design assets.** It directs, briefs, reviews, and assembles.

## What It Does

1. Loads brand intelligence — voice and identity files are the primary anchor
2. Reads campaign brief from Campaign Strategist (or collects context in standalone mode)
3. Develops the creative concept — the unifying idea behind all executions
4. Gets concept approved before briefing anyone
5. Issues tailored, self-contained briefs to each needed specialist
6. Spawns all specialists in parallel
7. Reviews every output against the brand voice rubric and creative concept
8. Routes all copy through Copy Editor before assembly
9. Assembles and delivers the complete creative package

## Commands

| Command | What It Does |
|---------|-------------|
| `/creative-brief` | Start a creative project — concept → briefs → parallel execution → package |
| `/creative-review` | Review existing creative against the brand rubric — pass / revise verdicts |

## How It Fits

The Creative Director sits between the Campaign Strategist and all specialist agents:

```
Campaign Strategist
  → creative-brief.md
      ↓
Creative Director
  → develops creative concept (user approves)
  → issues specialist briefs
      ↓ [all in parallel]
  ├── Ad Copywriter
  ├── Email Copywriter
  ├── Direct Response Copywriter
  ├── Brand Storytelling Copywriter
  ├── SEO Copywriter
  ├── Graphic Design Agent
  └── UX/Website Designer
      ↓ [all copy reviewed by Creative Director]
  Copy Editor
      ↓
  Creative Package → Performance Marketing Agent
```

## Specialists Coordinated

| Specialist | When Used |
|-----------|----------|
| Ad Copywriter | Meta, Google, TikTok, LinkedIn ad variants |
| Email Copywriter | Sequences, newsletters, lifecycle, cold outreach |
| Direct Response Copywriter | Landing pages, sales pages, VSLs |
| Brand Storytelling Copywriter | About pages, essays, thought leadership, manifestos |
| SEO Copywriter | Blog posts, pillar pages, programmatic content |
| Graphic Design Agent | Visual asset briefs, image prompts, Canva direction |
| UX/Website Designer | Wireframes, user flows, UX copy |
| Copy Editor | Reviews all copy — always runs, never optional |

## Output Structure

```
campaigns/{{slug}}/creative/
├── creative-concept.md       ← approved unifying concept
├── creative-package.md       ← assembled deliverables summary
├── briefs/                   ← specialist briefs issued
│   ├── ad-copy-brief.md
│   ├── email-copy-brief.md
│   └── [others]
├── copy/                     ← all copy outputs, Copy Editor reviewed
│   ├── ad-copy.md
│   ├── email-copy.md
│   └── [others]
├── design/                   ← design and UX briefs
│   ├── graphic-design-brief.md
│   └── ux-brief.md
└── review/                   ← rubric review notes
    └── creative-review-{{date}}.md
```

## The Creative Concept

The most important output of the Creative Director. Developed before any specialist is briefed. Consists of:

- **Campaign idea** — the overarching creative platform in one sentence
- **Campaign line** — the headline or tagline anchoring all executions
- **Visual direction** — 3–5 words that define the aesthetic world of the campaign
- **Tone calibration** — which brand voice qualities this campaign leans into
- **Non-negotiables** — what every execution must include
- **Guardrails** — what this campaign will never do

The concept is the thread connecting every ad, email, landing page, and social post. Without it, individual outputs may be strong in isolation but feel disconnected as a campaign.

## Plugin Dependencies

- **brand-intelligence-center** (required) — voice-identity.md is the Creative Director's constitution
- **campaign-strategist** (recommended) — provides the creative-brief.md the Creative Director reads in campaign mode
- **competitive-landscape** (recommended) — ad analysis informs concept differentiation
