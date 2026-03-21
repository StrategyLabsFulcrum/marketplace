# Design Brief Templates

Complete brief formats for all design specialists the Art Director briefs. Each is self-contained — the specialist executes from it plus the visual direction system plus their own skill knowledge.

All briefs share a common header block, then specialist-specific sections.

---

## Common Header Block (all design briefs)

```markdown
# [Specialist Name] Design Brief — {{Campaign Name}}

> **From:** Art Director
> **To:** {{Specialist name}}
> **Campaign:** {{campaign-slug}}
> **Date issued:** {{date}}
> **Output due:** {{date}}
> **Save output to:** campaigns/{{slug}}/creative/briefs/{{filename}}.md

---

## Brand Visual Identity
**Brand:** {{brand name}}
**Read first:** `brand-intelligence-center/voice-identity.md` — visual identity section
**Design system:** `design-system/brand-standards.md` (if exists)

**Core brand colors:**
- Primary: #{{hex}} (CMYK: {{values}})
- Secondary: #{{hex}} (CMYK: {{values}})
- Accent: #{{hex}} (CMYK: {{values}})

**Fonts:**
- Headline: {{font, weight}}
- Body: {{font, weight}}

**Logo:** {{description + usage rules}}

## Visual Direction System
**Full system:** `creative/visual-direction-system.md` — read before starting.

**Summary for this assignment:**
- **Visual direction:** {{3–5 words}}
- **Campaign line:** "{{line}}"
- **Color treatment:** {{summary}}
- **Typography direction:** {{summary}}
- **Photography/illustration style:** {{summary}}
- **Campaign motif:** {{description and placement rules}}
- **Layout principles:** {{summary}}

## Visual Guardrails
**Never:**
{{List most relevant visual guardrails for this medium}}

## Copy on Assets
{{Either paste approved copy or note: "Placeholder copy — apply final copy when received from copywriter"}}
```

---

## Graphic Design Agent Brief (Digital)

Append after common header:

```markdown
---

## Your Assignment — Digital Asset Direction

Produce a comprehensive design brief and production specifications for all digital assets in this campaign. For each asset type, provide: art direction description, image generation prompts (if AI imagery), Canva direction (if applicable), and complete technical specifications.

### Asset Requirements

{{Repeat for each format group}}

#### Meta — Feed Ads (1:1 and 4:5)
| Spec | Value |
|------|-------|
| Dimensions | 1080×1080px (1:1), 1080×1350px (4:5) |
| Color profile | RGB / sRGB |
| File format | JPG or PNG |
| Max file size | 30MB |
| Text overlay limit | <20% of image area (Meta guideline) |
| Safe zones | Keep key content 100px from all edges |
| Variants needed | {{N}} |

**Art direction:**
{{What does the image contain? Subject, composition, treatment. Specific enough to brief a photographer or AI generator.}}

**Copy placement:**
{{Where does text sit? What hierarchy? Style of text overlay?}}

**Image generation prompt (if AI imagery):**
```
Subject: {{description}}
Style: {{photography style from visual direction}}
Lighting: {{lighting direction}}
Color: {{color treatment}}
Composition: {{framing and crop}}
Mood: {{emotional quality}}
Aspect ratio: 1:1 / 4:5
Negative: {{what to exclude}}
```

**Canva direction (if applicable):**
- Template type: {{Social media post}}
- Key design decisions: {{what to customize}}
- Brand kit elements: {{colors, fonts, logo to apply}}

---

#### Meta — Stories and Reels (9:16)
| Spec | Value |
|------|-------|
| Dimensions | 1080×1920px |
| Color profile | RGB / sRGB |
| File format | JPG/PNG (static), MP4/MOV (video) |
| Safe zones | Keep content 14% (250px) from top and bottom — UI overlay zone |
| Text safe area | Center 1080×1420px |
| Variants needed | {{N}} |

**Art direction:**
{{Subject and composition for vertical format. How does the visual direction adapt here?}}

**Motion direction (if animated):**
{{Entry animation, hold, exit. Timing in seconds.}}

---

#### Google Display
| Spec | Value |
|------|-------|
| Required sizes | 300×250, 728×90, 160×600, 300×600, 320×50 |
| Color profile | RGB / sRGB |
| File format | JPG, PNG, or HTML5 |
| Max file size | 150KB per banner |
| Animation | Max 30 seconds, max 3 loops |
| Variants needed | {{N}} per size |

**Art direction:**
{{Simplified direction for small formats — brand color background, logo, campaign line, single strong visual or no image. Clarity over complexity.}}

---

#### Email Header / Template
| Spec | Value |
|------|-------|
| Width | 600px (renders consistently across clients) |
| Header image height | 200–300px typical |
| Color profile | RGB / sRGB |
| File format | JPG or PNG |
| Max file size | Keep total email under 1MB including all images |
| Mobile | Must render well at 320px width |

**Art direction:**
{{What the email header contains. How the visual system applies on a white email background. Campaign motif placement.}}

**Template direction:**
{{Any specific email layout guidance — section colors, dividers, button styles using brand colors}}

---

#### Organic Social
**Platforms:** {{Instagram, Facebook, LinkedIn, TikTok, Pinterest}}

| Platform | Primary Size | Notes |
|----------|-------------|-------|
| Instagram feed | 1080×1080 or 1080×1350 | |
| Instagram Stories | 1080×1920 | |
| LinkedIn feed | 1200×627 | Landscape preferred |
| Facebook feed | 1200×630 | |
| Pinterest | 1000×1500 | Vertical |
| TikTok | 1080×1920 | Video preferred |

**Art direction:**
{{How organic social posts differ from paid ads for this campaign. More candid? More educational? Platform-specific notes.}}

**Variants needed per platform:** {{N}}

### Overall Digital Design Notes
{{Any cross-format consistency notes, production dependencies, or handoff instructions}}
```

---

## Print Design Agent Brief

Append after common header:

```markdown
---

## Your Assignment — Print Design Direction

Produce detailed design briefs and production specifications for all print assets. All print files must be CMYK, at specified resolution, with correct bleed and safe zone.

**Print production fundamentals (apply to all):**
- Color mode: CMYK (not RGB — convert all colors)
- Resolution: 300 DPI minimum (images placed at 100%)
- Bleed: 0.125" (3mm) on all edges unless specified otherwise
- Safe zone: Keep all critical content 0.125" (3mm) inside trim edge
- File format: PDF/X-1a for press-ready files; layered source files retained

**Brand CMYK values:**
- Primary: C{{}} M{{}} Y{{}} K{{}}
- Secondary: C{{}} M{{}} Y{{}} K{{}}
- Accent: C{{}} M{{}} Y{{}} K{{}}

### Magazine / Newspaper Ads

#### Full-Page Magazine Ad
| Spec | Value |
|------|-------|
| Trim size | {{W" × H"}} — confirm with publication |
| Bleed | +0.125" all sides |
| Safe zone | 0.25" inside trim |
| Resolution | 300 DPI |
| Color | CMYK |
| Black | Rich black for large areas: C60 M40 Y40 K100 |
| Variants needed | {{N}} |

**Art direction:**
{{Full execution of the visual direction. This is the richest, highest-quality version of the campaign — the reference standard all other executions are measured against. Photography at full resolution. Complete typography system. Campaign motif in full.}}

**Placement context:** {{Publication name, section, facing page context if known}}

---

#### Half-Page / Quarter-Page Ad
| Spec | Value |
|------|-------|
| Trim size | {{W" × H"}} — confirm with publication |
| Format | Horizontal / Vertical |
| Resolution | 300 DPI |
| Color | CMYK |

**Art direction:**
{{Simplified from full-page — one strong visual, campaign line, brand mark, single CTA. What stays, what's cut?}}

---

### Direct Mail

#### Postcard
| Spec | Value |
|------|-------|
| Size | 6"×4" (standard) / 6"×9" (oversized) / 6.5"×9" (jumbo) |
| Bleed | +0.125" all sides |
| Safe zone | 0.25" inside trim |
| Resolution | 300 DPI |
| Color | CMYK |
| **Front** | Full campaign visual — headline, image, brand mark |
| **Back** | Address area (right 40%), message (left 60%), return address, indicia area |
| Variants needed | {{N}} |

**Front art direction:**
{{Strong single image or color field. Campaign line dominant. Clear CTA. Read in under 3 seconds.}}

**Back art direction:**
{{Campaign message in 50–75 words. Supporting proof point. CTA repeated. Postal compliance — indicia area top right, return address top left.}}

---

#### Brochure / Mailer
| Spec | Value |
|------|-------|
| Flat size | {{W" × H"}} |
| Folded size | {{W" × H"}} |
| Fold type | {{Trifold / Bifold / Z-fold / Gate fold}} |
| Panels | {{N front, N back}} |
| Resolution | 300 DPI |
| Color | CMYK |

**Panel-by-panel art direction:**
{{Describe the content and visual treatment for each panel in sequence — cover, inside panels, back cover}}

**Cover:**
{{Art direction}}

**Inside panels:**
{{How information flows across panels. What each panel contains. Visual hierarchy.}}

**Back cover:**
{{Brand mark, contact info, CTA. Clean and clear.}}

---

### Print Production Notes
- **Paper stock direction:** {{Coated / Uncoated / Specialty}} — {{weight recommendation}}
- **Special finishes:** {{Spot UV / Foil / Emboss / None}}
- **Printing method:** {{Offset / Digital / Flexo (for packaging)}}
- **Vendor notes:** {{Any specific vendor or print partner requirements}}
```

---

## OOH Design Agent Brief (Outdoor, Transit, Environmental)

Append after common header:

```markdown
---

## Your Assignment — Out-of-Home Design Direction

Produce design briefs and production specifications for all outdoor and environmental advertising. OOH design principles are fundamentally different from digital and print — designs must communicate in 3 seconds or less, at distance, often while moving.

**OOH Design Principles (apply to all formats):**
- Maximum 7 words of copy (aim for 5)
- One image or one strong color field — never multiple competing visuals
- Headline must be readable at 50 feet minimum
- Logo must be visible and legible
- No small copy — if it can't be read at viewing distance, it shouldn't be there
- High contrast between text and background is non-negotiable

### Billboard

#### Standard Bulletin Billboard (14' × 48')
| Spec | Value |
|------|-------|
| Design dimensions | 14'×48' (168"×576") |
| Digital file size | Submit at 1:10 or 1:12 scale minimum |
| Resolution | 100 DPI at full size (some vendors specify differently — confirm) |
| Color | CMYK (print) or RGB (digital billboard) |
| Bleed | +0.5" all sides for static |
| Viewing distance | Primary read at 300–500 feet |
| Viewing duration | 3 seconds average at 65 mph |
| Variants | {{N}} |

**Art direction:**
{{One strong visual or color field. Campaign line dominant — set large. Logo at {{position}}. No body copy. High contrast. How does the campaign motif appear at this scale?}}

**Copy (7 words maximum):**
{{Exact copy — every word is a decision at this format}}

---

#### Junior Poster (6' × 12')
| Spec | Value |
|------|-------|
| Design dimensions | 6'×12' (72"×144") |
| Viewing distance | Primary read at 50–100 feet |
| Variants | {{N}} |

**Art direction:**
{{More intimate viewing distance — can support slightly more copy than bulletin. Same principles.}}

---

### Transit Advertising

#### Bus Shelter (Backlit, 4' × 6')
| Spec | Value |
|------|-------|
| Design dimensions | 48"×72" |
| Backlit | Yes — colors will appear more saturated, darks deeper |
| Resolution | 100 DPI at full size |
| Color | CMYK (confirm with vendor for backlit profile) |
| Viewing distance | 3–10 feet |
| Viewing duration | 15–30 seconds (captive audience) |

**Art direction:**
{{Backlit execution — colors pop more than print. Viewing distance is close and dwell time is longer than billboards, so can support more copy. Full visual system. Campaign motif prominent.}}

---

#### Interior Transit (Subway, Bus Interior)
| Spec | Value |
|------|-------|
| Standard car card | 11"×28" or 22"×28" |
| Viewing distance | 2–6 feet |
| Viewing duration | Multiple minutes (captive audience) |
| Color | CMYK |

**Art direction:**
{{Closest and longest viewing of all OOH formats. More copy permitted. More detail in photography. Still typography-dominant — no clutter. Can tell a more complete story.}}

---

#### Bus Wrap / Vehicle Wrap
| Spec | Value |
|------|-------|
| Configuration | {{Full wrap / Partial wrap / King side / Queen side}} |
| Provide | {{Blank vehicle template from vendor}} |
| Resolution | 100 DPI at full size (wrap substrate) |
| Color | CMYK or specific wrap profile |
| Viewing | Moving — 3 seconds |

**Art direction:**
{{Bold, simple, high contrast. The vehicle shape is part of the design — align visual elements with vehicle structure where possible. Campaign color as primary background often works best.}}

---

### Retail / Point of Sale

#### Floor Display / Endcap
| Spec | Value |
|------|-------|
| Dimensions | {{W" × H"}} — confirm with retailer |
| Materials | {{Cardboard / Foam core / Metal — confirm}} |
| Viewing distance | 3–6 feet |

**Art direction:**
{{Product-forward. Campaign visual language applied. Clear price/offer if promotional. Brand mark prominent. Must work in context of retail environment.}}

---

### OOH Production Notes
- **Vendor:** {{vendor name if known}}
- **Material:** {{Vinyl / Backlit film / Mesh / Paper}}
- **Installation:** {{Permanent / Temporary / Rolling}}
- **Digital billboard specs:** {{If digital OOH — confirm loop duration, frame rate, pixel dimensions}}
- **Traffic/approval:** {{Lead time for installation and any approvals required}}
```

---

## Packaging / Brand Design Agent Brief

Append after common header:

```markdown
---

## Your Assignment — Packaging, Signage, and Brand Identity Design

Produce design briefs and specifications for non-advertising brand design touchpoints. These are often permanent or long-lived — they represent the brand at its most fundamental.

**Important:** Packaging and permanent signage follow brand standards more strictly than campaign creative. The campaign visual direction informs the mood and style, but brand identity is primary. Campaigns come and go — packaging and signage stay.

### Packaging

#### Primary Packaging
| Spec | Value |
|------|-------|
| Product type | {{product name and category}} |
| Packaging format | {{Box / Bag / Bottle / Can / Pouch / Sleeve}} |
| Dimensions (flat/dieline) | {{W × H × D}} |
| Printing method | {{Offset / Flexo / Digital / Gravure}} |
| Color | CMYK / Pantone (specify) |
| Substrate | {{Paper / Cardboard / Plastic / Glass / Metal}} |
| Finishes | {{Matte laminate / Gloss / Spot UV / Foil}} |
| Required elements | {{Logo, product name, ingredients/contents, regulatory info, barcodes, certifications}} |

**Design direction:**
{{How does the brand visual identity apply to this packaging format? What's the primary design element? How does it work at the size this product will be displayed? How does it look on shelf next to competitors?}}

**Front panel art direction:**
{{Logo position, product name treatment, hero visual if any, primary color application}}

**Back/side panel art direction:**
{{Required regulatory/informational content, secondary brand elements, call-outs}}

**Shelf presence:**
{{How does this package stand out at point of purchase? Color blocking? Distinctive shape? Brand mark visibility?}}

---

#### Label Design
| Spec | Value |
|------|-------|
| Label dimensions | {{W" × H"}} |
| Material | {{Paper / Vinyl / Foil}} |
| Application | {{Front / Back / Wrap-around}} |
| Print method | {{Flexo / Digital / Offset}} |
| Required info | {{List all regulatory and informational requirements}} |

---

### Signage

#### Interior Signage
| Type | Dimensions | Material | Notes |
|------|-----------|---------|-------|
| Reception/lobby sign | {{W × H}} | {{material}} | {{brand mark + tagline}} |
| Directional signs | {{W × H}} | {{material}} | {{wayfinding system}} |
| Feature wall | {{W × H}} | {{material}} | {{brand story / visual}} |

**Design direction:**
{{How the brand visual identity applies to interior environments. Scale, materials, and the experience of encountering the brand in physical space.}}

---

#### Exterior Signage
| Type | Dimensions | Material | Notes |
|------|-----------|---------|-------|
| Building sign | {{W × H}} | {{Dimensional letters / Lightbox / Painted}} | {{illumination?}} |
| Window graphics | {{coverage area}} | {{Vinyl}} | {{transparent / frosted}} |
| Sidewalk / A-frame | {{W × H}} | {{material}} | {{changeable copy?}} |

---

### Trade Show / Events

#### Trade Show Backdrop (10' × 8')
| Spec | Value |
|------|-------|
| Display area | 10'×8' (120"×96") |
| Print method | Dye sublimation fabric or vinyl |
| Resolution | 100 DPI at full size |
| Color | RGB (fabric dye sub) or CMYK (vinyl) |
| Viewing distance | 10–20 feet |

**Art direction:**
{{Brand-forward — this is the face of the company at a trade event. Logo large and high. Campaign line or brand tagline. Brand color dominant. Photography if relevant. Simple and impactful — complex design reads as chaos at this scale.}}

---

#### Banner Stand (2' × 6')
| Spec | Value |
|------|-------|
| Design area | 24"×72" (confirm with vendor) |
| Resolution | 100 DPI at full size |
| Color | CMYK or RGB depending on vendor |

**Art direction:**
{{Vertical format. Top third: logo + brand mark. Middle: campaign message or key value proposition. Bottom: CTA or contact info.}}

---

#### Table Display / Counter Card
| Spec | Value |
|------|-------|
| Dimensions | {{W" × H"}} |
| Material | {{Foam core / Acrylic / Cardboard}} |

---

### Corporate Identity

#### Business Cards
| Spec | Value |
|------|-------|
| Dimensions | 3.5"×2" (US standard) / 3.5"×2.125" (with bleed) |
| Front | Logo, name, title |
| Back | Contact info or brand element |
| Paper | {{Weight / Finish}} |
| Special | {{Spot UV / Foil / Rounded corners / None}} |

**Design direction:**
{{How the brand identity applies at business card scale. What goes on front vs. back. Typography hierarchy for name vs. title vs. contact info.}}

---

#### Presentation Deck Template
| Spec | Value |
|------|-------|
| Format | 16:9 (1920×1080px) |
| Slides to design | Cover, Section divider, Content slide, Full-bleed image slide, Data/chart slide, Thank you/CTA |
| Output | {{PowerPoint / Google Slides / Keynote}} |

**Design direction:**
{{Slide master using brand colors and fonts. How each slide type looks. Consistent header/footer treatment. Data visualization style.}}
```

---

## Review Criteria by Specialist

### Graphic Design Agent Review
- [ ] Visual direction system applied (color treatment, typography, photography style, campaign motif)
- [ ] Brand colors correct (check hex values — no approximations)
- [ ] Correct fonts at correct weights (no system font substitutions)
- [ ] Logo correctly placed with proper clear space
- [ ] Campaign motif present at correct position
- [ ] All format specs correct (dimensions, file format, color profile)
- [ ] Safe zones respected (no critical content in bleed areas)
- [ ] Text overlay within platform limits
- [ ] Copy on assets matches approved copy exactly

### Print Design Agent Review
- [ ] All files in CMYK (not RGB)
- [ ] Minimum 300 DPI at 100% scale
- [ ] Bleed included (0.125" minimum)
- [ ] Critical content within safe zone
- [ ] Rich black used for large solid areas (C60 M40 Y40 K100)
- [ ] All fonts embedded or outlined
- [ ] Visual direction applied within print constraints
- [ ] Proof colors against CMYK values (not screen)

### OOH Design Agent Review
- [ ] Copy at or under 7 words
- [ ] Readable at specified viewing distance
- [ ] High contrast — minimum 4.5:1 contrast ratio for text on background
- [ ] Logo visible and legible at viewing distance
- [ ] No small copy or fine detail that disappears at scale
- [ ] Correct dimensions and resolution for vendor
- [ ] Campaign motif visible at scale

### Packaging/Brand Design Agent Review
- [ ] Brand standards strictly followed (colors, fonts, logo — not campaign variations)
- [ ] All required regulatory elements present and legible
- [ ] Dieline/template correctly used
- [ ] Correct color mode for printing method
- [ ] Shelf presence considered (competitive context)
- [ ] File format matches vendor/printer requirements
