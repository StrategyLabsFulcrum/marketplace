# Creative Review Rubric

The Creative Director uses this rubric to review every specialist output before it enters the creative package. Each criterion has a pass/flag/fail determination with specific escalation paths.

---

## Review Outcomes

| Outcome | Definition | Action |
|---------|-----------|--------|
| **Pass** | All criteria met | Route to Copy Editor (copy) or assembly (design) |
| **Pass with notes** | Core criteria met, minor refinements needed | Route to Copy Editor with notes attached |
| **Revise** | One or more criteria materially failed | Return to specialist with specific, actionable feedback |
| **Escalate** | Specialist revision did not resolve the failure | Flag to user with options |

One revision cycle is allowed per output. If the revision still fails the rubric, escalate to the user rather than cycling again.

---

## Copy Rubric

### Criterion 1: Brand NEVER Rules

**Check:** Does the output contain any words, phrases, tones, or approaches listed on the brand NEVER list?

**Pass:** Zero NEVER violations.

**Revise:** Any NEVER violation — regardless of how strong the surrounding copy is. This is a hard rule, not a judgment call.

**Common NEVER failures to watch for:**
- Corporate jargon and buzzwords (varies by brand — check the list)
- Apologetic or overly formal language (if on the NEVER list)
- Specific flagged phrases from voice-identity.md
- Mentioning competitor names disparagingly (unless explicitly permitted)
- Making claims that aren't supported by available proof

---

### Criterion 2: Brand ALWAYS Rules

**Check:** Are all ALWAYS requirements present in this output?

**Pass:** Every ALWAYS rule is fulfilled or clearly present.

**Pass with notes:** ALWAYS rules are present but weak — e.g., required to "feel personal" but the copy is slightly formal. Note for Copy Editor to address.

**Revise:** A required ALWAYS element is entirely absent.

---

### Criterion 3: Core Message Clarity

**Check:** Is the core message from the creative brief present, clear, and prominent?

**Pass:** A reader who knows nothing about the brand could identify the central message after reading.

**Pass with notes:** Message is present but buried — appears later in the copy than it should for the format.

**Revise:** Core message is absent, diluted across too many competing claims, or contradicted by the tone of the copy.

**Note:** "Present" does not mean verbatim — the message can be expressed differently. What matters is that it lands.

---

### Criterion 4: Campaign Concept Alignment

**Check:** Does the output reflect the campaign idea and feel connected to the campaign line?

**Pass:** Could clearly be part of the same campaign as other executions. Shares the conceptual territory.

**Pass with notes:** Loosely connected — the concept is there but the execution doesn't lean into it.

**Revise:** Could have been written for a completely different campaign. No connection to the creative concept.

**Note:** This is a judgment call, not a checkbox. The question is: if you showed this to someone alongside the other campaign outputs, would they read it as part of the same campaign?

---

### Criterion 5: Audience Relevance

**Check:** Does this copy speak to the right person at the right stage?

**Pass:** The audience would recognize themselves in the copy. The pain, aspiration, or situation described matches the segment and journey stage.

**Pass with notes:** Mostly right, but a specific phrase or framing will land differently with this audience than intended.

**Revise:** Copy addresses the wrong segment, wrong stage (e.g., conversion copy for an awareness audience), or uses language the audience wouldn't use about themselves.

**Test:** Read the first 30 words. Would the target customer feel like this was written for them?

---

### Criterion 6: Proof Point Quality

**Check:** Is the designated lead proof point present, and is it specific?

**Pass:** The specific proof point from the brief is used accurately and prominently.

**Pass with notes:** A proof point is present but it's the wrong one (not the lead proof point specified in the brief), or it's used in a weak position.

**Revise:** The output uses generic proof language ("trusted by thousands of customers") in place of the specific evidence. Vague proof is worse than no proof — it signals marketing rather than credibility.

**Hard rule on specificity:**
- ❌ "hundreds of happy customers" → Revise
- ❌ "proven results" → Revise
- ✅ "4.8 stars across 1,200 reviews" → Pass
- ✅ "Used by 340 restaurants in the Southeast" → Pass
- ✅ "[Customer name]: 'This saved us 6 hours a week'" → Pass

---

### Criterion 7: Competitive Differentiation

**Check:** Does this copy sound different from what competitors are saying?

**Pass:** Language, angles, and claims are distinct from the competitor messages flagged in the brief.

**Pass with notes:** Mostly differentiated, but one phrase or claim echoes category clichés.

**Revise:** Copy uses the same positioning, claims, or language as a primary competitor. If a competitor could run this copy with their logo swapped in, it fails.

**Common failure patterns:**
- Category clichés everyone uses ("premium quality," "industry-leading," "trusted partner")
- Same offer mechanic as the primary competitor
- Same emotional angle as what competitors are running in their ad library

---

### Criterion 8: Format Compliance

**Check:** Does the output meet all technical specs from the brief?

Pass requirements vary by format:

**Ad copy:**
- [ ] All required variants delivered (correct quantity)
- [ ] Character counts within spec for each field
- [ ] Required CTA present in each variant
- [ ] Organized by platform and variant with labels

**Email:**
- [ ] All emails in the sequence delivered
- [ ] Subject line options provided (3 per email minimum)
- [ ] Preview text included
- [ ] Full body copy — not descriptions of what the email should say
- [ ] CTA copy and destination specified for each email

**Landing/sales page:**
- [ ] All required sections present
- [ ] Hero headline and subheadline distinct
- [ ] CTAs use specific action language (not "Submit" or "Learn More" without context)
- [ ] Proof section uses actual evidence, not descriptions of evidence

**Brand story / SEO:**
- [ ] Within target word count (within 10% tolerance)
- [ ] For SEO: title tag and meta description included with character counts

---

## Design Brief Rubric

Design briefs from the Graphic Design Agent and UX/Website Designer are reviewed against a separate set of criteria:

### Criterion 1: Visual Direction Alignment

**Check:** Does the design brief reflect the creative concept's visual direction?

**Pass:** Aesthetic described in the brief matches the campaign's visual direction (e.g., if the concept says "raw and high-contrast," the brief specifies photography style, color treatment, and composition that deliver that).

**Revise:** The brief describes a generic aesthetic or one that contradicts the creative concept.

---

### Criterion 2: Brand Visual Identity Compliance

**Check:** Are brand colors, fonts, and visual identity rules correctly applied?

**Pass:** Primary and secondary colors specified correctly. Brand fonts named. Logo usage follows guidelines from voice-identity.md.

**Revise:** Off-brand colors, wrong fonts, logo misuse, or any visual direction that contradicts the brand's visual identity.

---

### Criterion 3: Format Spec Completeness

**Check:** Are all required asset specs present and complete for every channel?

**Pass:** Every asset format has: dimensions (W x H px), file format, quantity, any platform-specific requirements (safe zones, max file size), and text overlay copy if applicable.

**Revise:** Missing specs, wrong dimensions, or copy on assets doesn't match the approved ad copy.

---

### Criterion 4: Executability

**Check:** Can a designer or Canva/AI tool execute from this brief without further input?

**Pass:** A designer seeing this brief for the first time could start work immediately. The brief makes decisions — it doesn't just set parameters.

**Pass with notes:** Brief is directional but leaves some decisions to the designer that should have been made here.

**Revise:** Brief is too vague to execute from. Describes what the asset should "feel like" but doesn't tell the designer what to put in it.

---

## Review Log Format

For each output reviewed, document in `creative/review/creative-review-{{date}}.md`:

```markdown
# Creative Review — {{Campaign Name}}
**Date:** {{date}}
**Reviewed by:** Creative Director

---

## {{File Name}} — {{Specialist}}

**Outcome:** Pass / Pass with notes / Revise

**Rubric results:**
| Criterion | Result | Notes |
|-----------|--------|-------|
| Brand NEVER | ✅ Pass / ❌ Fail | [notes] |
| Brand ALWAYS | ✅ Pass / ⚠️ Weak | [notes] |
| Core message | ✅ Pass / ⚠️ Buried / ❌ Missing | [notes] |
| Concept alignment | ✅ Pass / ⚠️ Loose / ❌ Disconnected | [notes] |
| Audience relevance | ✅ Pass / ❌ Fail | [notes] |
| Proof quality | ✅ Pass / ❌ Generic | [notes] |
| Differentiation | ✅ Pass / ⚠️ Cliché risk | [notes] |
| Format compliance | ✅ Pass / ❌ Missing [field] | [notes] |

**Feedback to specialist (if Revise):**
[Specific, actionable notes — what failed and how to fix it. Not general direction.]

**Notes to Copy Editor (if Pass / Pass with notes):**
[Specific things to watch for during the editorial pass]

---
```
