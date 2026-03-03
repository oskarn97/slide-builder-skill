# Snowflake Addon — Slide Builder Erweiterung

> **Dieses Addon wird zusätzlich zu `slide_builder.md` geladen wenn Snowflake-Kontext vorliegt.**
> Es enthält Snowflake-spezifische Regeln, das Corporate Layout und Integrationen mit internen Tools.

---

## Snowflake Logo

Das offizielle Snowflake-Logo als SVG wird **immer** von dieser URL eingebunden:

```
https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg
```

> **Regel:** Dieses Logo in jeder Präsentation verwenden — auf Title Slide, Thank You Slide und überall dort, wo das Snowflake-Branding erscheint. Keine Text-Platzhalter oder alternative URLs nutzen.

### Title Slide Logos (Snowflake-Kontext)

```html
<div class="logos">
    <img src="[KUNDE_LOGO_URL]" alt="[Kunde]" style="height: 45px; filter: brightness(0) invert(1);">
    <span style="opacity: 0.4; font-size: 24px;">×</span>
    <img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg" alt="Snowflake" style="height: 40px;">
</div>
```

### CSS Variable

```css
--snowflake-blue: #29B5E8;
```

Wird in folgenden Templates verwendet:
- `--accent-blue` im generischen Slide Builder entspricht `--snowflake-blue`
- Bei Snowflake-Kontext immer `#29B5E8` als Wert fuer `--accent-blue` verwenden

---

## Raven Report als Input (PFLICHT wenn vorhanden)

Falls `RAVEN_REPORT.md` im Kundenordner existiert, **MUSS** dieser als primaere Quelle fuer folgende Slide-Inhalte verwendet werden:

| Slide | Raven Report Sektion | Was uebernehmen |
|-------|---------------------|----------------|
| **Title Slide** | `SECTION:executive_summary` | Hook / Subtitle |
| **Agenda** | `SECTION:industry_landscape` | Branchenzahl ("X Kunden in Ihrer Branche") |
| **"Your Key Principles"** | `SECTION:pain_points` | Pain Points als Requirements |
| **Use-Case-Slides** | `SECTION:use_case_mapping` | Opportunity, Snowflake-Produkte, Data Sources |
| **Customer References** | `SECTION:references` | 2-3 Referenz-Boxen mit ROI-Zahlen |
| **Case Study** | `SECTION:reference_detail` | Deep-Dive der besten Referenz |
| **"Why Snowflake?"** | `SECTION:competitive_intel` | Comparison-Table-Zeilen — **NUR auf explizite Anfrage einbauen!** |
| **"How We Deliver"** | `SECTION:use_case_mapping` + `SECTION:business_value` | Feature → Requirement Mapping |

> **Referenzierung:** `@[Kunde]/RAVEN_REPORT.md` — Sektionen durch `<!-- SECTION:id -->` Marker identifizierbar.

### Customer References recherchieren

1. **Bevorzugt:** Aus `RAVEN_REPORT.md` lesen (Sektionen `references` + `reference_detail`)
   → `@[Kunde]/RAVEN_REPORT.md`
2. **Falls kein Report:** Raven Research Agent manuell befragen
   → `@demo_builder/modules/06_raven_research/raven_research.md`
   → Typische Frage: `"Give me 3 customer references for [PRODUKT] in [BRANCHE] in [REGION]"`

---

## Snowflake-spezifische Slide-Anpassungen

### "How We Deliver" Slide

Im Snowflake-Kontext wird die rechte Spalte mit Snowflake-Branding versehen:

```html
<div style="font-size: 20px; font-weight: 600; color: var(--accent-blue);">
    Snowflake Solution
</div>
```

### Architecture Slide — Snowflake Platform

Der Center-Header zeigt das Snowflake-Logo:

```html
<div style="display: flex; align-items: center; justify-content: center; gap: 10px; height: 30px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg" alt="Snowflake" style="height: 22px;">
    <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: #94a3b8;">(in [Azure/AWS/GCP])</div>
</div>
```

> **NICHT** "Snowflake (in Azure)" schreiben — das Logo enthaelt bereits den Namen.

### Demo Transition — Platform Badge

```html
<div style="margin-top: 60px; padding: 20px 40px; background: rgba(0,214,125,0.15); border-radius: 12px; border: 1px solid var(--primary-green);">
    <span style="color: var(--primary-green); font-size: 18px; font-weight: 500;">Streamlit App running on Snowflake</span>
</div>
```

### `--bg-dark` Farbwahl (Snowflake-CI)

> `--bg-dark` muss immer ein **kuehles, blau-getoentes Dunkelblau** sein, das zur Snowflake Corporate Identity passt. Der Standard ist `#11293E`.
>
> **NIEMALS** verwenden:
> - `#1a1a2e` — dunkles Violett-Navy
> - `#0D2818` — dunkles Gruen
> - Reines Schwarz (`#000`, `#111`) — wirkt zu hart
>
> Snowflake-CI fuehlt sich hell, modern und blau an. Dunkle Flaechen sind die Ausnahme und sollten sich wie ein natuerlicher Teil des Snowflake-Universums anfuehlen.

### Header-Balken (Custom Layout mit Snowflake)

Jeder Content-Slide-Header hat einen **blauen Balken** (`--accent-blue` / `#29B5E8`, 12px breit) der **ganz links am Seitenrand** sitzt.

---

## Kosten-Messaging: Vorsicht bei Preismodell-Aussagen

Snowflake platziert in der Regel **Kapazitaetsvertraege mit festem Commitment** (nicht reines Pay-per-Use). Slides muessen das korrekt widerspiegeln:

| Formulierung | Bewertung | Warum |
|---|---|---|
| "Pay-per-Use, nur zahlen was genutzt wird" | **Falsch** | Suggeriert On-Demand ohne Commitment |
| "Planbare Kosten, volle Transparenz" | **Richtig** | Betont Planbarkeit + Steuerbarkeit |
| "Festes Commitment, flexible Nutzung" | **Richtig** | Ehrlich ueber Vertrag, positiv ueber Flexibilitaet |
| "Verbrauch jederzeit steuerbar" | **Richtig** | Betont Governance-Aspekt (CIO-relevant) |
| "Keine Hardware-Fixkosten" | **Richtig** | Stimmt — Cloud vs. On-Prem |
| "Kosten skalieren mit dem Business" | **OK** | Stimmt im Rahmen des Commitments |

**Goldene Regel:** Auf CIO-Level nie "kostenlos" oder "nur zahlen was genutzt wird" formulieren — ein CIO kennt den Unterschied und verliert Vertrauen. Stattdessen: **Transparenz, Planbarkeit, Steuerbarkeit** betonen.

---

## Snowflake Corporate Layout (`Layout: snowflake_corporate`)

> **Dieses Layout repliziert das offizielle Snowflake-Praesentationsdesign.**
> Es ist fuer Standard-Intros, Plattform-Overviews und generische Snowflake-Praesentationen gedacht —
> also immer dann, wenn **kein** kundenspezifisches Branding benoetigt wird.

### Wann verwenden?

| Situation | Layout |
|-----------|--------|
| Kunden-Workshop, POC-Praesentation, Folgetermin | `custom` |
| Snowflake Intro, Plattform-Overview, Event-Talk | `snowflake_corporate` |
| Gemischt (Intro + Kunden-Deep-Dive) | `snowflake_corporate` fuer Intro-Slides, dann `custom` fuer Kunden-Teil |

### Template

Bei `Layout: snowflake_corporate` das Template `slide_template_corporate.html` verwenden.

```
@.cursor/skills/slide-builder/slide_template_corporate.html
```

---

### Design-Prinzipien (Corporate)

| Eigenschaft | Corporate Layout | Custom Layout |
|-------------|-----------------|---------------|
| **Hintergrund** | Fast alle Slides dunkel (#0E1C2F) | Weiße Slides, dunkler Header |
| **Primaerfarbe** | Snowflake Light Blue (#29B5E8) | Kunden-CI-Farbe |
| **Sekundaerfarbe** | Bright Blue (#1B98D4), Violet (#7C3AED) | Kunden-Sekundaerfarbe |
| **Text** | Weiß auf dunkel | Dunkel auf weiß |
| **Footer** | "© 2025 Snowflake Inc. All Rights Reserved" + Logo | Event-Name + Slide-Nr |
| **Logos** | Nur Snowflake | Kunde × Snowflake |
| **Header-Bar** | Kein separater Header — Titel direkt auf dunklem Hintergrund | Dunkler Header-Balken |
| **Slide-Nummern** | Dezent im Footer oder als Overlay | Im Footer |
| **Typografie** | Sehr groß, viel Negativraum, wenig Text | Kompakter, mehr Content |
| **Icons** | Lineare SVG-Icons in Light Blue | SVG-Icons in Primaerfarbe |

---

### CSS Variables (Corporate)

```css
:root {
    /* Snowflake Corporate CI */
    --sf-navy: #0E1C2F;          /* Primaerer Hintergrund — tiefes Navy */
    --sf-navy-light: #162A45;    /* Leicht helleres Navy fuer Karten/Akzente */
    --sf-navy-mid: #1A3352;      /* Mittlerer Navy-Ton fuer Hover/Hervorhebungen */
    --sf-blue: #29B5E8;          /* Snowflake Light Blue — primaere Akzentfarbe */
    --sf-blue-dark: #1B98D4;     /* Dunklerer Blue fuer Kontrast */
    --sf-violet: #7C3AED;        /* Akzent-Violett (fuer Diagramme, Badges) */
    --sf-green: #00D67D;         /* Akzent-Gruen (fuer Checkmarks, Erfolg) */
    --sf-white: #FFFFFF;         /* Primaere Textfarbe */
    --sf-white-80: rgba(255,255,255,0.8);  /* Sekundaerer Text */
    --sf-white-60: rgba(255,255,255,0.6);  /* Tertiaerer Text */
    --sf-white-40: rgba(255,255,255,0.4);  /* Dezente Labels */
    --sf-white-10: rgba(255,255,255,0.10); /* Karten-Hintergrund auf dunkel */
    --sf-white-06: rgba(255,255,255,0.06); /* Sehr dezenter Karten-BG */
    --sf-border: rgba(255,255,255,0.12);   /* Karten-Borders */

    /* Gradient-Akzente */
    --sf-gradient-blue: linear-gradient(135deg, #29B5E8 0%, #1B7ED4 100%);
    --sf-gradient-title: linear-gradient(180deg, #0E1C2F 0%, #162A45 100%);
}
```

---

### Corporate Slide-Typen (aus dem offiziellen Deck)

#### 1. Title Slide (`.slide.sf-title`)

**Referenz:** Slide 1 — "SNOWFLAKE INTRO"

Dunkler Hintergrund, zentriertes Layout, großer "SNOWFLAKE"-Schriftzug, Untertitel, Presenter-Namen, Snowflake-Logo.

```html
<div class="slide sf-title">
    <div class="sf-logo-icon">
        <img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg" 
             alt="Snowflake" style="height: 80px; opacity: 0.3;">
    </div>
    
    <h1>SNOWFLAKE</h1>
    <h2>[UNTERTITEL]</h2>
    
    <div class="sf-presenters">
        <span>[Name 1]</span>
        <span>[Name 2]</span>
    </div>
    
    <div class="sf-footer-bar">
        <span>© 2025 Snowflake Inc. All Rights Reserved</span>
    </div>
</div>
```

**CSS:**
```css
.slide.sf-title {
    background: var(--sf-gradient-title);
    color: var(--sf-white);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.slide.sf-title h1 {
    font-size: 96px;
    font-weight: 800;
    letter-spacing: 12px;
    text-transform: uppercase;
    margin-bottom: 20px;
}

.slide.sf-title h2 {
    font-size: 48px;
    font-weight: 300;
    color: var(--sf-white-80);
    letter-spacing: 2px;
    margin-bottom: 60px;
}

.slide.sf-title .sf-presenters {
    display: flex;
    gap: 40px;
    font-size: 22px;
    color: var(--sf-white-60);
    font-weight: 400;
}

.slide.sf-title .sf-logo-icon {
    margin-bottom: 40px;
}
```

---

#### 2. Statement Slide (`.slide.sf-statement`)

**Referenz:** Slide 2 — "Every Organization Struggles with Silos"

Dunkler Hintergrund, großer Titel oben, Key Statement prominent in der Mitte, optional: Beschreibungstext und Highlight-Block.

```html
<div class="slide sf-dark">
    <div class="sf-slide-number">2</div>
    
    <div class="sf-content-area">
        <h1>[Titel / Provokante These]</h1>
        <p class="sf-subtitle">[Erklaerung / Kontext — 1 Zeile]</p>
        
        <div class="sf-key-statement">
            <div class="sf-statement-text">
                [KERNAUSSAGE IN GROSSBUCHSTABEN]<br>
                [ZWEITE ZEILE DER AUSSAGE]
            </div>
        </div>
    </div>
    
    <div class="sf-footer-bar">
        <span>© 2025 Snowflake Inc. All Rights Reserved</span>
    </div>
</div>
```

**CSS:**
```css
.slide.sf-dark {
    background: var(--sf-navy);
    color: var(--sf-white);
    position: relative;
}

.sf-slide-number {
    position: absolute;
    top: 50px;
    right: 80px;
    font-size: 18px;
    color: var(--sf-white-40);
    font-weight: 500;
}

.sf-content-area {
    padding: 100px 120px 120px;
    height: calc(1080px - 60px);
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.sf-content-area h1 {
    font-size: 52px;
    font-weight: 700;
    margin-bottom: 20px;
    line-height: 1.2;
}

.sf-subtitle {
    font-size: 24px;
    color: var(--sf-white-60);
    margin-bottom: 60px;
    line-height: 1.6;
}

.sf-key-statement {
    background: var(--sf-white-06);
    border-left: 5px solid var(--sf-blue);
    padding: 40px 50px;
    margin-top: 20px;
}

.sf-statement-text {
    font-size: 36px;
    font-weight: 700;
    line-height: 1.4;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--sf-white);
}
```

---

#### 3. Platform Overview Slide (`.slide.sf-platform`)

**Referenz:** Slide 3 — "Snowflake: The AI Data Cloud"

Dunkler Hintergrund, zentriertes Key-Visual, Snowflake als Plattform mit umgebenden Capability-Bloecken.

```html
<div class="slide sf-dark">
    <div class="sf-slide-number">3</div>
    
    <div class="sf-content-area" style="align-items: center; text-align: center;">
        <h1>[Snowflake: The AI Data Cloud]</h1>
        
        <div class="sf-platform-visual">
            <div class="sf-platform-core">
                <div class="sf-platform-label">[BUSINESS]</div>
                <div class="sf-platform-label">[TRANSFORMATION]</div>
                <div class="sf-platform-label">[PLATFORM]</div>
            </div>
            
            <div class="sf-capability-ring">
                <div class="sf-capability">[Capability 1]</div>
                <div class="sf-capability">[Capability 2]</div>
                <div class="sf-capability">[Capability 3]</div>
                <div class="sf-capability">[Capability 4]</div>
            </div>
        </div>
    </div>
    
    <div class="sf-footer-bar">
        <span>© 2025 Snowflake Inc. All Rights Reserved</span>
    </div>
</div>
```

**CSS:**
```css
.sf-platform-visual {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 40px;
    margin-top: 60px;
}

.sf-platform-core {
    background: var(--sf-gradient-blue);
    border-radius: 20px;
    padding: 50px 80px;
    text-align: center;
}

.sf-platform-label {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--sf-white);
    line-height: 1.3;
}

.sf-capability-ring {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    justify-content: center;
}

.sf-capability {
    background: var(--sf-white-10);
    border: 1px solid var(--sf-border);
    padding: 18px 32px;
    font-size: 18px;
    font-weight: 500;
    color: var(--sf-white-80);
    text-transform: uppercase;
    letter-spacing: 1px;
}
```

---

#### 4. Product Architecture Slide (`.slide.sf-architecture`)

**Referenz:** Slide 4 — "Snowflake Cortex AI"

Dunkler Hintergrund, Titel oben, gestapelte Produkt-Layer mit horizontaler Unterteilung.

```html
<div class="slide sf-dark">
    <div class="sf-slide-number">4</div>
    
    <div class="sf-content-area">
        <h1>[Snowflake AI is Easy, Efficient, and Trusted]</h1>
        <div class="sf-product-badge">[SNOWFLAKE CORTEX AI]</div>
        
        <div class="sf-architecture-stack">
            <div class="sf-arch-row">
                <div class="sf-arch-block sf-arch-primary">[UNSTRUCTURED]</div>
                <div class="sf-arch-block sf-arch-primary">[STRUCTURED]</div>
            </div>
            <div class="sf-arch-row">
                <div class="sf-arch-block">[Intelligence]</div>
                <div class="sf-arch-block">[Doc AI]</div>
                <div class="sf-arch-block">[Studio]</div>
            </div>
            <div class="sf-arch-row">
                <div class="sf-arch-block sf-arch-wide">[CORTEX AGENTS]</div>
            </div>
            <div class="sf-arch-row">
                <div class="sf-arch-block sf-arch-foundation">[Governance]</div>
                <div class="sf-arch-block sf-arch-foundation">[Guardrails]</div>
                <div class="sf-arch-block sf-arch-foundation">[Observability]</div>
            </div>
            <div class="sf-arch-row">
                <div class="sf-arch-block sf-arch-wide sf-arch-base">[ORCHESTRATION]</div>
            </div>
        </div>
    </div>
    
    <div class="sf-footer-bar">
        <span>© 2025 Snowflake Inc. All Rights Reserved</span>
    </div>
</div>
```

**CSS:**
```css
.sf-product-badge {
    display: inline-block;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--sf-blue);
    margin-bottom: 40px;
    padding: 10px 0;
    border-bottom: 2px solid var(--sf-blue);
}

.sf-architecture-stack {
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-top: 40px;
    max-width: 1200px;
}

.sf-arch-row { display: flex; gap: 8px; }

.sf-arch-block {
    flex: 1;
    padding: 24px 30px;
    background: var(--sf-white-10);
    border: 1px solid var(--sf-border);
    font-size: 18px;
    font-weight: 600;
    color: var(--sf-white-80);
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.sf-arch-block.sf-arch-primary {
    background: var(--sf-gradient-blue);
    color: var(--sf-white);
    border: none;
}
.sf-arch-block.sf-arch-wide { flex: 1 1 100%; }
.sf-arch-block.sf-arch-foundation {
    background: var(--sf-navy-light);
    border: 1px solid var(--sf-border);
    color: var(--sf-white-60);
}
.sf-arch-block.sf-arch-base {
    background: var(--sf-navy-mid);
    border: 1px solid rgba(41,181,232,0.3);
    color: var(--sf-blue);
}
```

---

#### 5. Three-Pillar Slide (`.slide.sf-pillars`)

**Referenz:** Slide 5 — "Snowflake Powers the Connected Enterprise"

Dunkler Hintergrund, drei gleichbreite Spalten mit Icon, Titel und Beschreibung.

```html
<div class="slide sf-dark">
    <div class="sf-slide-number">5</div>
    
    <div class="sf-content-area" style="align-items: center;">
        <h1>[Snowflake Powers the Connected Enterprise]</h1>
        
        <div class="sf-pillars">
            <div class="sf-pillar">
                <div class="sf-pillar-icon">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--sf-blue)" stroke-width="1.5">
                        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                    </svg>
                </div>
                <h3>[Trusted]</h3>
                <p>[Description]</p>
            </div>
            <div class="sf-pillar">
                <div class="sf-pillar-icon">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--sf-blue)" stroke-width="1.5">
                        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>
                    </svg>
                </div>
                <h3>[Connected]</h3>
                <p>[Description]</p>
            </div>
            <div class="sf-pillar">
                <div class="sf-pillar-icon">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--sf-blue)" stroke-width="1.5">
                        <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/>
                    </svg>
                </div>
                <h3>[Easy]</h3>
                <p>[Description]</p>
            </div>
        </div>
    </div>
    
    <div class="sf-footer-bar">
        <span>© 2025 Snowflake Inc. All Rights Reserved</span>
    </div>
</div>
```

**CSS:**
```css
.sf-pillars { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; margin-top: 80px; max-width: 1400px; }
.sf-pillar { text-align: center; padding: 40px 30px; }
.sf-pillar-icon { width: 80px; height: 80px; margin: 0 auto 30px; display: flex; align-items: center; justify-content: center; background: var(--sf-white-06); border-radius: 50%; border: 1px solid var(--sf-border); }
.sf-pillar h3 { font-size: 32px; font-weight: 700; color: var(--sf-white); margin-bottom: 20px; }
.sf-pillar p { font-size: 20px; line-height: 1.6; color: var(--sf-white-60); }
```

---

#### 6. Demo Transition Slide

Dunkler Hintergrund, zentriertes "Demo" mit Play-Icon, minimalistisch.

```html
<div class="slide sf-dark" style="display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
    <div style="margin-bottom: 40px;">
        <svg width="100" height="100" viewBox="0 0 24 24" fill="none" stroke="var(--sf-blue)" stroke-width="1" opacity="0.6">
            <circle cx="12" cy="12" r="10"/>
            <polygon points="10 8 16 12 10 16 10 8" fill="var(--sf-blue)" stroke="none"/>
        </svg>
    </div>
    <h1 style="font-size: 72px; font-weight: 300; letter-spacing: 8px; text-transform: uppercase; color: var(--sf-white);">Demo</h1>
    <div class="sf-footer-bar">
        <span>© 2025 Snowflake Inc. All Rights Reserved</span>
    </div>
</div>
```

---

#### 7. Closing / CTA Slide

Dunkler Hintergrund, großer Statement oben, drei Aktionssaeulen darunter.

```html
<div class="slide sf-dark">
    <div class="sf-content-area" style="align-items: center; text-align: center;">
        <div class="sf-closing-statement">
            THERE IS NO AI STRATEGY WITHOUT<br>
            <span style="color: var(--sf-blue);">A DATA STRATEGY</span>
        </div>
        
        <div class="sf-closing-pillars">
            <div class="sf-closing-pillar">
                <h3>[Strengthen Your Data Foundation]</h3>
                <p>[For all data and workloads]</p>
            </div>
            <div class="sf-closing-pillar">
                <h3>[Accelerate Enterprise AI]</h3>
                <p>[For all users against enterprise data]</p>
            </div>
            <div class="sf-closing-pillar">
                <h3>[Build & Distribute Applications]</h3>
                <p>[With streamlined development, deployment, and distribution]</p>
            </div>
        </div>
    </div>
    
    <div class="sf-footer-bar">
        <span>© 2025 Snowflake Inc. All Rights Reserved</span>
    </div>
</div>
```

**CSS:**
```css
.sf-closing-statement { font-size: 48px; font-weight: 800; line-height: 1.3; letter-spacing: 2px; text-transform: uppercase; color: var(--sf-white); margin-bottom: 80px; }
.sf-closing-pillars { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; max-width: 1400px; }
.sf-closing-pillar { background: var(--sf-white-06); border: 1px solid var(--sf-border); border-top: 3px solid var(--sf-blue); padding: 40px 30px; text-align: center; }
.sf-closing-pillar h3 { font-size: 24px; font-weight: 700; color: var(--sf-white); margin-bottom: 15px; line-height: 1.3; }
.sf-closing-pillar p { font-size: 18px; color: var(--sf-white-60); line-height: 1.5; }
```

---

### Corporate Footer-Bar (auf jeder Slide)

```css
.sf-footer-bar {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 18px 80px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 14px;
    color: var(--sf-white-40);
    border-top: 1px solid var(--sf-border);
}
```

Optional mit Snowflake-Logo rechts:
```html
<div class="sf-footer-bar">
    <span>© 2025 Snowflake Inc. All Rights Reserved</span>
    <img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg" 
         alt="Snowflake" style="height: 20px; opacity: 0.4;">
</div>
```

---

### Corporate-spezifische Regeln

| Regel | Beschreibung |
|-------|-------------|
| **Alles dunkel** | Fast jede Slide hat `background: var(--sf-navy)`. Weiße Slides sind die Ausnahme. |
| **Copyright auf JEDER Slide** | `© [Jahr] Snowflake Inc. All Rights Reserved` im Footer. |
| **Keine Kunden-Logos** | Nur Snowflake-Branding. Kunden-Logos gehoeren in `custom`-Layout. |
| **Slide-Nummern dezent** | Kleine Nummer oben-rechts (`sf-slide-number`), nicht im Footer. |
| **Uppercase fuer Key Messages** | Kernaussagen in `text-transform: uppercase` + `letter-spacing`. |
| **Light Blue als einzige Akzentfarbe** | `--sf-blue` (#29B5E8) ist die primaere Highlight-Farbe. Sparsam einsetzen. |
| **Viel Negativraum** | Weniger Content pro Slide als im Custom-Layout. Wirken lassen. |
| **Große Typografie** | Titel 48–96px, keine kleinen Fonts unter 18px. |
| **Keine Box-Shadows** | Karten werden durch `border` und `background`-Kontrast abgegrenzt. |
| **Keine border-radius > 0 auf Karten** | Eckige Karten wirken Corporate. Nur runde Icons (`border-radius: 50%`). |
| **Keine bunten Hintergruende** | Farbe kommt NUR ueber `border-top`, `border-left` oder Text-Farbe rein. |

### Zusaetzliche Corporate Slide-Typen

| Slide-Typ | Basis-Klasse | Besonderheiten |
|-----------|-------------|----------------|
| **Content mit Bullets** | `.sf-dark` | Titel + 4-6 Bullet Points, große Font-Size (22px) |
| **Split Content** | `.sf-dark` + `.sf-split` | 50/50 Split, links Text, rechts Visual/Diagramm |
| **Statistics / KPI** | `.sf-dark` | Große Zahlen in `--sf-blue`, Beschreibung in `--sf-white-60` |
| **Quote** | `.sf-dark` | Zitat zentriert, große italic Font, Quelle darunter |
| **Timeline** | `.sf-dark` | Horizontale Timeline mit Light-Blue-Akzenten |
| **Comparison** | `.sf-dark` | Tabelle mit `--sf-navy-light` Zeilen, `--sf-blue` Highlights |

### Beispiel-Flow: Snowflake Intro

```
Slide 1: Title (SNOWFLAKE [THEMA])           → sf-title
Slide 2: Statement (Provokante These)         → sf-dark + sf-key-statement
Slide 3: Platform Overview (AI Data Cloud)    → sf-dark + sf-platform-visual
Slide 4: Product Architecture (Cortex AI)     → sf-dark + sf-architecture-stack
Slide 5: Three Pillars (Value Props)          → sf-dark + sf-pillars
Slide 6: Demo Transition                      → sf-dark (minimalistisch)
Slide 7: Closing CTA (Data Strategy)          → sf-dark + sf-closing
```
