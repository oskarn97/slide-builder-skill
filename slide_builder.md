# Slide Builder - HTML Presentation Module

> **Erstellt professionelle HTML-Slides für Kundenpräsentationen**
> 
> Die Slides können standalone oder als Ergänzung zu Live-Demos verwendet werden.

---

## Quick Start

```
@.cursor/skills/slide-builder/slide_builder.md

Kunde: @[Kundenordner]
Sprache: [deutsch | englisch]
Integration: [standalone | mit_demo]
Layout: [custom | snowflake_corporate]
```

> **Layout-Option:**
> - `custom` (Standard) — Kunden-CI, weiße Slides, individuelle Farben, Kunden- + Company-Logo
> - Weitere Layouts koennen ueber Addons bereitgestellt werden (z.B. `snowflake_addon.md` fuer Snowflake Corporate Layout)

---

## ⚠️ WICHTIG: Kundenindividueller Ansatz

### Kein starres Template!

Die Slide-Struktur muss **individuell auf den Kunden abgestimmt** sein:

| Anpassungsfaktor | Beispiele |
|------------------|-----------|
| **Use Cases** | Sustainability-First vs. Inventory-First vs. AI-First |
| **Pain Points** | Legacy-Ablösung vs. Datensilos vs. Compliance-Druck |
| **Domäne** | Manufacturing, Pharma, Finance, Retail — andere Stories |
| **Stakeholder** | CTO-fokussiert vs. Business-fokussiert vs. CISO-fokussiert |
| **Reifegrad** | Greenfield vs. Migration vs. Erweiterung |
| **Wettbewerb** | Vergleich relevant? Welche Alternativen? |

### Flow-Beispiele nach Domäne

**Manufacturing (z.B. Syntegon):**
```
Context → Sustainability → Inventory → OEE → Data Sharing → Demo → Technical
```

**Healthcare (z.B. Siemens Healthineers):**
```
Context → Compliance/Regulation → Data Governance → AI/ML → Demo → Security → Technical
```

**Financial Services:**
```
Context → Risk & Compliance → Real-time Analytics → Cost Optimization → Demo → Security → Technical
```

**Retail:**
```
Context → Customer 360 → Supply Chain → Personalization → Demo → Scalability → Technical
```

### Vor dem Erstellen prüfen:

1. **Kundenordner lesen** — Requirements, Meeting Notes, Pain Points
2. **Prioritäten identifizieren** — Was ist das "Lighthouse Project"?
4. **Stakeholder-Map** — Wer ist im Raum? Was sind deren Interessen?
5. **Wettbewerbssituation** — Welche Alternativen werden evaluiert?
6. **Zeitrahmen** — Wie viel Zeit haben wir? Demo-Anteil?

---

## Pflicht-Deliverables (bei JEDER Slide-Erstellung)

> **Slides allein sind KEIN vollständiges Deliverable.** Zu jeder Slide-Erstellung gehören:

| Deliverable | Datei | Wann | Pflicht? |
|-------------|-------|------|----------|
| **HTML-Slides** | `[name]_slides.html` | Immer | ✅ Ja |
| **Talk Track** | `TALK_TRACK.html` | Immer wenn Slides | ✅ Ja |
| **Demo Flow** | `DEMO_FLOW.html` | Wenn Live-Demo Teil der Präsentation | ✅ Ja (bei Demo) |
| **Slide-Previews** | `_slide_previews/slide_*.jpg` | Automatisch bei Export | ✅ Ja |
| **PDF-Export** | `.pdf` für alle HTML-Dateien | Nach visueller Validierung | ✅ Ja |

**Workflow:**
```
1. Slides HTML erstellen
2. Talk Track HTML erstellen (Abschnitt 4)
3. Demo Flow HTML erstellen (Abschnitt 5, wenn Live-Demo)
4. Slide-Previews generieren (--preview-only)
5. Previews visuell validieren — Review-Loop bis alle Slides OK
6. ALLE HTML-Dateien als PDF exportieren (erst wenn Slides validiert)
```

> **⛔ KEIN PDF-Export ohne vorherige visuelle Validierung!**
> Der Agent MUSS die Preview-JPEGs mit dem `Read`-Tool öffnen und jede Slide visuell prüfen,
> bevor die PDF generiert wird. Details siehe Abschnitt "Visuelle Validierung".

**Ohne Talk Track, visuelle Validierung und PDF ist die Slide-Erstellung NICHT abgeschlossen.**

---

## Core Principles

### 1. Storyline-Struktur (Flexibel!)

**Problem → Impact → Solution** - Nicht umgekehrt!

> **Hinweis:** Die folgende Struktur ist ein **Referenzrahmen**, keine Pflicht. 
> Passe Reihenfolge und Slides an den spezifischen Kunden an.

```
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: KONTEXT & VALIDIERUNG (Slides 1-4)                    │
├─────────────────────────────────────────────────────────────────┤
│  1. Title Slide                                                 │
│  2. Agenda                                                      │
│  3. "Your Key Principles" (NUR Requirements, KEINE Features)    │
│     → Zeigt: "Wir haben zugehört"                               │
│     → Baut Vertrauen auf                                        │
│  4. The Challenge (Pain Point, Kundenzitat wenn vorhanden)      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 2: USE CASES (Slides 5-N)                                │
├─────────────────────────────────────────────────────────────────┤
│  Pro Use Case eine Slide:                                       │
│  • Title mit Badge (Priority, Pilot, etc.)                      │
│  • Business Value, nicht technische Details                     │
│  • "Data Sources" → "Insight" → "Value" Flow                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 3: LIVE DEMO (Transition Slide)                          │
│  (NUR wenn Integration = mit_demo)                              │
├─────────────────────────────────────────────────────────────────┤
│  • Dark themed Transition Slide                                 │
│  • Preview der Demo-Module                                      │
│  • Call-to-Action: "Let me show you..."                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 4: TECHNISCHE CREDIBILITY (Slides N+1 bis Ende-2)        │
├─────────────────────────────────────────────────────────────────┤
│  • "How We Deliver" (Feature Mapping zu Requirements)           │
│     → JETZT macht die Lösung Sinn (Pain ist etabliert)          │
│  • Platform Architecture                                        │
│  • Implementation Roadmap                                       │
│  • KEIN "Why Us?" Comparison (nur auf expl. Anfrage)          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 5: CLOSE (Letzte 2 Slides)                               │
├─────────────────────────────────────────────────────────────────┤
│  • Next Steps (konkrete Aktionen)                               │
│  • Thank You / Q&A                                              │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Key Principles: Aufteilen!

**FALSCH:** Requirements + Solution Features frueh in der Praesentation
**RICHTIG:** Aufteilen in zwei Slides

| Slide | Position | Inhalt | Ziel |
|-------|----------|--------|------|
| "Your Key Principles" | Früh (Slide 3) | NUR die Kunden-Requirements | Validierung, Vertrauen |
| "How We Deliver" | Spät (nach Use Cases) | Requirement → Feature Mapping | Lösungs-Credibility |

### 3. Optionale Slides (je nach Kunde)

| Slide | Wann einfügen? | Position |
|-------|----------------|----------|
| **Team Vorstellung** | Bei unbekannten Stakeholdern, wichtigen Erstterminen | Nach Title, vor Agenda |
| **Customer References** | Wenn Credibility wichtig, bei Enterprise-Kunden | Nach Feature Mapping |
| **InfoSec & Compliance** | CISO im Raum, regulierte Branche (Pharma, Finance) | Nach References |
| **Competitive Comparison** | ⛔ **NUR auf explizite Anfrage!** Standardmäßig NICHT einbauen. Nur wenn der Nutzer/AE dies ausdrücklich wünscht. | Nach Security |
| **Architecture Deep-Dive** | Technische Stakeholder, Architekten | Variable Position |
| **Pricing/Commercial** | Wenn explizit angefragt | Vor Next Steps |
| **Case Study Detail** | Spezifische Referenz besonders relevant | Nach References |

> **Customer References:** Falls ein Addon (z.B. `snowflake_addon.md`) geladen ist, dort die Recherche-Anleitung fuer References beachten.

### 4. Talk Track erstellen (`TALK_TRACK.html`)

Zu jeder Slide-Präsentation gehört ein **HTML Talk Track**, aus dem per `export_pdf.py` die PDF generiert wird.

> **Kein Markdown Talk Track.** HTML ist das einzige Format -- es ist gleichzeitig Quelle und Export-Vorlage.

**Template:** `@.cursor/skills/slide-builder/talk_track_template.html`

#### 4.1 Grundprinzip: Spickzettel, nicht Script

Der Talk Track liegt im Termin vor dem Presenter (Tablet/Ausdruck). Er muss **scanbar** sein:

| Prinzip | Richtig | Falsch |
|---------|---------|--------|
| **Talking Points** | Kurze Stichpunkte mit fettem Kern | Ausformulierte Absätze |
| **Kern-Phrase** | Nur den Kernsatz fett, Rest als Stichpunkt | Ganzer Absatz in Anführungszeichen |
| **Demo-Slides** | "Was zeigen & Punkt machen" | Klickpfade (Snowsight > Data > ...) |
| **Fragen** | Inline bei der Slide als Q&A-Block | Gesammelt am Ende des Dokuments |
| **Übergänge** | Implizit (Presenter sieht nächste Slide) | Eigener Transition-Block |

> **Warum keine Klickpfade?** Im Termin weiß der Presenter, wo er klicken muss -- er hat geprobt.
> Was er braucht: **Welchen Punkt will ich mit dieser Aktion machen?**
> Klickpfade gehören in eine Rehearsal-Checkliste, nicht in den Meeting-Spickzettel.

#### 4.2 Pflicht-Elemente

Jeder Talk Track MUSS diese Elemente enthalten:

**1. Kontext-Header** (`.context-box`) -- direkt unter dem Titel:

| Feld | Inhalt |
|------|--------|
| Teilnehmer (Kunde) | Namen + Rollen (z.B. "Mark (CIO), Jonas (Data Lead)") |
| Teilnehmer (eigenes Team) | Namen -- Account Executive zuerst, dann SE/weitere |
| Letzter Termin | Datum + was besprochen wurde |
| Ziel dieses Termins | Ein Satz |
| Gewünschtes Outcome / CTA | Konkreter nächster Schritt |

**2. Zeitliche Übersicht** (`<table>`) -- Phasen, Slides, Dauer, Inhalt

**3. Slide-Abschnitte** (`.slide-section`) -- pro Slide mit `<h2>` und Zeitstempel

**4. Appendix** (`.slide-section.appendix`) -- "Vor dem Termin lesen" mit goldenen Regeln

#### 4.3 Block-Typen

| Block | Label | CSS-Klasse | Verwendung | Pflicht? |
|-------|-------|-----------|------------|----------|
| **Talking Points** | `Talking Points` | `.block-talk` | Kurze Stichpunkte | Ja -- jede Slide |
| **Kern-Phrase** | `Kern-Phrase` | `.block-formulierung` | NUR Kernsatz fett + Stichpunkt | Optional |
| **Key Messages** | `Key Messages` | `.block-key` | Highlights, visuell prominent | Bei Demo-Slides |
| **Erwartbare Fragen** | `Erwartbare Fragen` | `.block-key` | Q&A inline bei der Slide | Bei wichtigen Slides |
| **Rückfrage** | `Rückfrage` | `.block-rueckfrage` | Frage an den Kunden | Optional, terminabhängig |
| **Warnung** | `Wichtig` | `.block-warn` | Don'ts, Sensibilitäten | Bei Bedarf |

**NICHT MEHR VERWENDEN:** `.block-transition` -- Übergänge sind implizit.

**Kern-Phrase vs. ganzer Absatz:**

| Falsch (zum Ablesen) | Richtig (scanbar) |
|----------------------|-------------------|
| "Stell dir vor, Jonas' Team stellt ein neues Datenprodukt bereit. Ein Kollege aus Peru soll es nutzen. Im Catalog sieht er sofort..." | **"Neuer Kollege sieht sofort: Wem gehören die Daten, wie sensitiv, welches Quellsystem"** -- ohne Doku zu suchen |

**Erwartbare Fragen -- inline, nicht am Ende:**

```html
<div class="block block-key">
    <span class="label label-key">Erwartbare Fragen</span>
    <p class="qa-item"><span class="q">"Frage?"</span> <span class="a">→ Antwort.</span></p>
</div>
```

**Rückfrage-Blöcke -- terminabhängig einsetzen:**

| Termintyp | Rückfragen? | Beispiel |
|-----------|------------|---------|
| Discovery / Ersttermin | Ja, viele | "Wie löst ihr das heute?" |
| Deep Dive / Folgetermin | Selektiv | "Passt das zu eurem Zielbild?" |
| Workshop | Ja, moderierend | "Was hat Priorität?" |
| Reine Präsentation / Keynote | Wenig bis keine | Nur am Ende |

#### 4.4 Kernregel: Demo-Slides inline

**Demo-Slides MÜSSEN konkrete Talking Points inline enthalten.** Nie nur "Siehe DEMO_STORYLINE.md" schreiben.

**FALSCH:**
```markdown
## Slide 5: Live Demo -- 13:00
→ Wechsel zu Snowsight (10 Minuten)
Siehe `DEMO_STORYLINE.md`
```

**RICHTIG:** "Was zeigen & Punkt machen" -- keine Klickpfade, stattdessen den Punkt:

```html
<h3>Phase 1: Tags & Discovery (3 min)</h3>
<div class="block block-talk">
    <span class="label label-talk">Was zeigen & Punkt machen</span>
    <ul>
        <li>Tabelle FAHRZEUGE öffnen → Tags + Comments zeigen</li>
        <li><strong>Kern-Phrase:</strong> "Neuer Kollege sieht sofort: Wem gehören die Daten..."</li>
    </ul>
</div>
```

#### 4.5 Spezial-Elemente

| Element | CSS-Klasse | Verwendung |
|---------|-----------|------------|
| Demo-Schritt | `.demo-step` | SQL-Befehl + Ergebnis |
| Rolle | `.demo-step .role` | SQL-Rolle (monospace, dunkel) |
| Ergebnis | `.result.full / .partial / .masked` | Grün / Amber / Rot |
| Q&A-Paar | `.qa-item` mit `.q` + `.a` | Frage + Antwort inline |
| Kontext-Header | `.context-box` mit `.ctx-item` | Teilnehmer, Ziel, CTA |
| Regeln-Grid | `.rules-grid` + `.rule-card` | Goldene Regeln im Appendix |
| Slide-Abschnitt | `.slide-section` / `.long` / `.appendix` | Seitenumbruch-Steuerung |

#### 4.6 Design-Prinzipien

| Prinzip | Umsetzung |
|---------|-----------|
| **Scanbar** | Kern-Phrasen fett, kein Fließtext, keine Absätze zum Ablesen |
| **Wenig Farbe** | Blocks unterscheiden sich primär durch Border-Left |
| **Key Messages prominent** | `.block-key` hat dickeren Border (4px) und dunkleres Label |
| **Q&A inline** | Erwartbare Fragen direkt bei der Slide, nicht gesammelt am Ende |
| **Kein Rauschen** | Keine Transition-Blöcke, keine Klickpfade, kein Boilerplate |

---

### 5. Demo Flow erstellen (`DEMO_FLOW.html`)

Zu jeder Präsentation mit Live-Demo gehört ein **Demo Flow** als HTML-Datei. PDF wird per `export_pdf.py` generiert (A4). Gleicher Design-Ansatz wie `TALK_TRACK.html` -- strukturierte Blöcke, scanbar, Print-optimiert.

> **Unterschied zum Talk Track:** Der Talk Track deckt die gesamte Präsentation ab (Slides + Demo + Übergänge). Der Demo Flow ist **nur die Demo** -- ein kompakter Spickzettel, den der SE neben Snowsight/Streamlit liegen hat.

#### 5.1 Grundprinzip: Kurz, actionable, SE-Perspektive

Der Demo Flow vereint drei Perspektiven auf einer Seite:

| Perspektive | Frage | Umsetzung im Flow |
|-------------|-------|-------------------|
| **SE (Technik)** | Was zeige ich? | Konkreter SQL/UI-Schritt |
| **Business Value** | Warum interessiert das den Kunden? | 1-2 Sätze unter jeder Phase |
| **Termintyp** | Was ist der Punkt? | "Punkt machen" -- der Kernsatz |

#### 5.2 Pflicht-Elemente

**1. Header** -- Termintyp, Dauer, Umgebung, Rollen, Kernbotschaft (je ein Satz)

**2. Vorbereitung** -- Checkliste: Welche Scripts deployed, welche Rollen getestet, Fallback vorbereitet

**3. Phasen** -- Pro Demo-Phase:

| Element | Beschreibung | Pflicht? |
|---------|-------------|----------|
| **Zeigen** | Was konkret öffnen/ausführen (1 Satz) | Ja |
| **Business Value für [Kunde]** | Warum das den Kunden interessiert | Ja |
| **Punkt machen** | Kernsatz(e) in Stichpunkten | Ja |
| **Rückfrage** | Frage an den Kunden (terminabhängig) | Optional |
| **SQL/Code** | Konkreter Befehl wenn nötig | Bei SQL-Demos |
| **Ergebnis-Tabelle** | Rolle → Ergebnis → Relevanz | Bei Rollen-Vergleichen |

**4. Kernbotschaften** -- 3 Takeaways für die Überleitung zurück zu Slides

#### 5.3 Block-Typen (HTML-Klassen)

| Block | Label | CSS-Klasse | Verwendung |
|-------|-------|-----------|------------|
| **Zeigen** | `Zeigen` | `.block-show` | Was konkret öffnen/ausführen |
| **Business Value** | `Business Value für [Kunde]` | `.block-value` | Warum das den Kunden interessiert |
| **Punkt machen** | `Punkt machen` | `.block-point` | Kernsätze (fett, prominent) |
| **Rückfrage** | `Rückfrage` | `.block-ask` | Frage an den Kunden |
| **SQL** | (kein Label) | `.sql-block` | SQL-Befehl als Monospace-Block |
| **Rollen-Tabelle** | `<table>` | mit `.result-full / .partial / .masked` | Rolle → Ergebnis → Relevanz |
| **Takeaways** | `Überleitung zurück zu Slides` | `.takeaways` | 3 Kernbotschaften am Ende |

Weitere Elemente aus dem Talk Track Design-System (`.context-box`, `.checklist`) werden wiederverwendet.

#### 5.5 Was NICHT rein gehört

- Keine ausformulierten Sätze zum Ablesen
- Keine Klickpfade (Snowsight > Data > Schema > ...)
- Keine Slide-Inhalte (dafür gibt es den Talk Track)
- Keine Feature-Listen oder Marketing-Sprache
- Kein Setup/Teardown (gehört in SQL-Scripts)

#### 5.6 Termintyp berücksichtigen

| Termintyp | Demo Flow Stil |
|-----------|---------------|
| **Discovery / Ersttermin** | Breit, viele Rückfragen, "Was meint ihr?" |
| **Deep Dive / Folgetermin** | Fokussiert auf besprochene Themen, weniger Rückfragen |
| **Workshop** | Interaktiv, Pausen für Diskussion, "Sollen wir hier tiefer rein?" |
| **Executive Briefing** | Kurz, nur 1-2 Phasen, Business Value dominant |

---

## Technical Specifications

### Base Dimensions
```css
--slide-width: 1920px;
--slide-height: 1080px;
/* 16:9 Aspect Ratio */
```

### Responsive Scaling
- Slides skalieren automatisch auf Viewport
- Aspect Ratio bleibt erhalten
- Scroll-Snap: Eine Slide pro Viewport

### Navigation
| Input | Aktion |
|-------|--------|
| `↓` / `→` / `Space` / `PageDown` | Nächste Slide |
| `↑` / `←` / `PageUp` | Vorherige Slide |
| `Home` | Erste Slide |
| `End` | Letzte Slide |
| Mausrad | Eine Slide pro Scroll (smooth, locked) |
| Touch Swipe | Nächste/Vorherige |

> **Hinweis:** Scroll-Snapping mit Animation-Lock verhindert versehentliches Überspringen von Slides.

### PDF-Export
- `@media print` mit `@page { size: 1920px 1080px; margin: 0 }` — Seite = Slide
- `transform: none` im Print-Modus — kein Skalieren, keine weißen Ränder
- `print-color-adjust: exact` — Hintergrundfarben, Gradients, Schatten bleiben erhalten
- Export via `export_pdf.py` (Playwright/Chromium headless) — **nicht** via Browser-Druck
- Talk Tracks (`.html`) werden automatisch als A4 PDF gerendert

---

## Slide Types & Templates

### Logos

#### Company Logo

Falls ein Addon geladen ist (z.B. `snowflake_addon.md`), enthaelt dieses die spezifische Logo-URL und Branding-Regeln fuer den Firmenkontext. Das Company Logo erscheint auf Title Slide, Thank You Slide und ueberall dort, wo das Firmen-Branding dargestellt wird.

#### Kunden-Logos

**ZUERST** im **Logo Registry** nachschlagen: `.cursor/rules/logo-registry.mdc`
→ Enthält validierte URLs für bereits recherchierte Kunden. Direkt verwenden, keine erneute Recherche nötig.

**Nur wenn KEIN Eintrag im Registry:** Logo recherchieren mit folgender Priorität:

1. **SVG bevorzugen** — skaliert verlustfrei, sieht auf jeder Auflösung scharf aus
2. **PNG mit Transparenz** als Fallback — wenn kein SVG verfügbar ist

**Quellen (in dieser Reihenfolge prüfen):**
1. Wikimedia Commons: `https://commons.wikimedia.org/wiki/File:[FIRMENNAME]_Logo.svg`
2. Wikipedia (en/de): `https://en.wikipedia.org/wiki/File:[FIRMENNAME]_logo.svg`
3. Firmenwebsite (WebSearch + WebFetch zur Validierung)

> **Regeln:**
> - **Immer das vollständige Logo mit Schriftzug** verwenden, nicht nur ein Icon/Symbol
> - Logos auf Wikimedia liegen oft unter abweichenden Dateinamen (z.B. `Vodafone_2017_logo.svg` statt `Vodafone_Logo.svg`) — im Zweifel per WebSearch suchen
> - Manche Logos liegen auf `en.wikipedia.org` statt `commons.wikimedia.org`
> - **Niemals** einen Text-Platzhalter verwenden, wenn ein echtes Logo verfügbar ist
> - **Nach erfolgreicher Recherche:** Logo-URL im Registry eintragen (`.cursor/rules/logo-registry.mdc`)

### 1. Title Slide (`.slide.title`)

```html
<div class="slide title">
    <h1>[Haupttitel]</h1>
    <h2>From <span class="green-accent">[Problem]</span> to <span class="green-accent">[Lösung]</span></h2>
    <div class="meta">
        [Event Name]<br>
        [Ort] | [Datum]
    </div>
    <div class="logos">
        <img src="[KUNDE_LOGO_URL]" alt="[Kunde]" style="height: 45px; filter: brightness(0) invert(1);">
        <span style="opacity: 0.4; font-size: 24px;">×</span>
        <img src="[COMPANY_LOGO_URL]" alt="[Company]" style="height: 40px;">
    </div>
</div>
```

**Design:**
- Dark gradient background (Kunden-CI)
- Zentrierter Inhalt
- Logos am unteren Rand (Kunde × Company)

### 2. Standard Content Slide

```html
<div class="slide">
    <div class="slide-header">
        <div>
            <div class="title-row">
                <h1>[Titel]</h1>
                <span class="badge">[Optional: Badge]</span>
            </div>
            <div class="subtitle">[Optional: Untertitel]</div>
        </div>
    </div>
    <div class="slide-content">
        <!-- Inhalt hier -->
    </div>
</div>
```

> **Hinweis:** Footer ist optional. Bei internen Slides weglassen, bei Kundenpräsentationen nach Bedarf hinzufügen.

**Layouts:**
- `.two-column` - 50/50 Split
- `.two-column.wide-left` - 60/40 Split
- `.card-grid` - 3 Spalten
- `.card-grid.two-col` - 2 Spalten
- `.card-grid.four-col` - 4 Spalten

### 3. Dark Slide (`.slide.dark`)

Für Übergänge, Zitate, Live Demo Transition.

```html
<div class="slide dark">
    <div class="slide-header" style="background: transparent;">
        <h1>[Titel]</h1>
    </div>
    <div class="slide-content">
        <!-- Inhalt -->
    </div>
    <div class="slide-footer" style="border-color: rgba(255,255,255,0.2); color: rgba(255,255,255,0.6);">
        <span>[Event]</span>
        <span>[Nr]</span>
    </div>
</div>
```

### 4. Use Case Slide

```html
<div class="slide">
    <div class="slide-header">
        <div>
            <div class="title-row">
                <h1>Use Case: [Name]</h1>
                <span class="badge">[Priority/Status]</span>
            </div>
        </div>
    </div>
    <div class="slide-content">
        <div class="two-column wide-left">
            <div>
                <div class="section-title">The Opportunity</div>
                <p style="font-size: 24px; line-height: 1.8; margin-bottom: 40px;">
                    [Value Proposition - 2-3 Sätze]
                </p>
                
                <div class="card-grid two-col" style="gap: 20px;">
                    <div class="card">
                        <h3>Data Sources</h3>
                        <p>[Quellen]</p>
                    </div>
                    <div class="card">
                        <h3>Insights</h3>
                        <p>[Was wird möglich]</p>
                    </div>
                </div>
            </div>
            
            <div class="highlight-box">
                <h3>Business Value</h3>
                <ul class="value-list">
                    <li>[Konkreter Benefit 1]</li>
                    <li>[Konkreter Benefit 2]</li>
                    <li>[Konkreter Benefit 3]</li>
                </ul>
            </div>
        </div>
    </div>
</div>
```

**Badge-Typen:**
- `Priority — Lighthouse Project` (grün)
- `Pilot Project` (grün)
- `Customer Value` (grün)
- `Strategic Differentiator` (grün)
- `Cross-ERP Consolidation` (grün)

### 5. Live Demo Transition Slide

```html
<div class="slide dark">
    <div class="slide-header" style="background: transparent;">
        <h1>Live Demo</h1>
        <div class="subtitle">See the platform in action</div>
    </div>
    <div class="slide-content" style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;">
        <!-- Play Icon -->
        <div style="margin-bottom: 60px;">
            <svg width="120" height="120" viewBox="0 0 24 24" fill="none" stroke="var(--primary-green)" stroke-width="1.5">
                <polygon points="5 3 19 12 5 21 5 3"/>
            </svg>
        </div>
        
        <!-- Quote/CTA -->
        <div style="font-size: 28px; color: white; max-width: 900px; line-height: 1.6; margin-bottom: 50px;">
            "[Call-to-Action mit Kundenbezug]"
        </div>
        
        <!-- Module Preview Cards -->
        <div style="display: flex; gap: 30px; flex-wrap: wrap; justify-content: center;">
            <!-- Card pro Demo-Modul -->
            <div style="background: rgba(255,255,255,0.1); padding: 25px 35px; border-radius: 12px;">
                <div style="font-size: 32px; margin-bottom: 10px;">[Icon]</div>
                <div style="color: white; font-size: 16px; font-weight: 600;">[Modul Name]</div>
                <div style="color: rgba(255,255,255,0.6); font-size: 14px;">[Kurzbeschreibung]</div>
            </div>
        </div>
        
        <!-- Platform Badge -->
        <div style="margin-top: 60px; padding: 20px 40px; background: rgba(0,214,125,0.15); border-radius: 12px; border: 1px solid var(--primary-green);">
            <span style="color: var(--primary-green); font-size: 18px; font-weight: 500;">[Live Demo Application]</span>
        </div>
    </div>
</div>
```

### 6. Requirements Validation Slide (Früh)

**NUR die Kunden-Requirements, KEINE Features!**

```html
<div class="slide">
    <div class="slide-header">
        <div>
            <h1>Your Key Principles</h1>
            <div class="subtitle">What's most important to [Kunde]</div>
        </div>
    </div>
    <div class="slide-content">
        <!-- 5 Requirements als Karten -->
        <div style="display: flex; flex-direction: column; gap: 20px;">
            <!-- Pro Requirement -->
            <div style="display: flex; gap: 25px; padding: 25px; background: white; border-radius: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                <div style="width: 56px; height: 56px; background: linear-gradient(135deg, var(--primary-green) 0%, var(--secondary-green) 100%); border-radius: 14px; display: flex; align-items: center; justify-content: center;">
                    <!-- SVG Icon -->
                </div>
                <div>
                    <div style="font-size: 24px; font-weight: 700; color: var(--text-dark);">[Requirement Name]</div>
                    <div style="font-size: 18px; color: var(--text-light); margin-top: 8px;">[Beschreibung]</div>
                </div>
            </div>
        </div>
        
        <!-- Summary -->
        <div style="margin-top: 40px; background: var(--bg-dark); border-radius: 16px; padding: 25px 35px;">
            <div style="color: white; font-size: 22px;">We've done our homework — these are your priorities.</div>
        </div>
    </div>
</div>
```

### 7. Feature Mapping Slide (Spät)

**Requirements → Features Mapping (NACH Use Cases!)**

```html
<div class="slide">
    <div class="slide-header">
        <div>
            <h1>How We Deliver</h1>
            <div class="subtitle">Your requirements — our capabilities</div>
        </div>
    </div>
    <div class="slide-content">
        <!-- Zwei-Spalten Header -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-bottom: 25px;">
            <div style="font-size: 20px; font-weight: 600;">Your Requirement</div>
            <div style="font-size: 20px; font-weight: 600; color: var(--accent-blue);">
                Our Solution
            </div>
        </div>
        
        <!-- Mapping Rows -->
        <div style="display: flex; flex-direction: column; gap: 12px;">
            <!-- Pro Requirement -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; background: white; border-radius: 16px; padding: 22px 30px;">
                <!-- Linke Spalte: Requirement -->
                <div style="display: flex; gap: 20px; align-items: center;">
                    <div style="width: 52px; height: 52px; background: var(--primary-green); border-radius: 12px;">
                        <!-- Icon -->
                    </div>
                    <div>
                        <div style="font-size: 22px; font-weight: 700;">[Requirement]</div>
                        <div style="font-size: 16px; color: var(--text-light);">[Kurzbeschreibung]</div>
                    </div>
                </div>
                
                <!-- Rechte Spalte: Solution Feature -->
                <div style="display: flex; align-items: center; gap: 15px; background: linear-gradient(135deg, #e3f6fc 0%, #d1f0fa 100%); padding: 15px 25px; border-radius: 0; border-left: 4px solid var(--accent-blue);">
                    <svg><!-- Checkmark --></svg>
                    <div>
                        <div style="font-size: 20px; font-weight: 600; color: #1a7ba8;">[Feature Name]</div>
                        <div style="font-size: 15px; color: #4a9bc7;">[Feature Details]</div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Summary Badge -->
        <div style="margin-top: 25px; background: var(--bg-dark); border-radius: 16px; padding: 22px 35px; display: flex; justify-content: space-between;">
            <div style="color: white;">All [N] principles natively supported</div>
            <div style="color: var(--primary-green); font-size: 48px; font-weight: 700;">[N]/[N]</div>
        </div>
    </div>
</div>
```

### 8. Comparison Slide ("Why X?")

> ⛔ **STANDARDMÄSSIG NICHT EINBAUEN!** Diese Slide wird NUR erstellt, wenn der Nutzer/AE explizit einen Wettbewerbsvergleich anfordert. Feature-Vergleichstabellen gegen Databricks, Fabric etc. sind in den meisten Kundenpräsentationen kontraproduktiv — sie lenken den Fokus vom Kunden-Problem auf Technologie-Debatten. Das Template bleibt als Referenz erhalten für die Fälle, in denen es explizit gewünscht wird.

```html
<div class="slide">
    <div class="slide-header">
        <div>
            <h1>Why [Platform]?</h1>
            <div class="subtitle">Addressing your key decision criteria</div>
        </div>
    </div>
    <div class="slide-content">
        <!-- Comparison Table -->
        <table class="comparison-table">
            <thead>
                <tr>
                    <th>Capability</th>
                    <th>[Platform 1]</th>
                    <th>[Platform 2]</th>
                    <th>[Recommended]</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>[Capability Name]</td>
                    <td class="partial">Partial</td>
                    <td class="no">No</td>
                    <td class="yes">Native</td>
                </tr>
                <!-- Weitere Zeilen -->
            </tbody>
        </table>
    </div>
</div>
```

### 9. Architecture Slide

**Drei-Spalten-Flow mit SVG Icons — OHNE Hintergrund-Container (KEINE Emojis!)**

> **⛔ Anti-Pattern: Riesige leere Hintergrund-Boxen**
>
> NIEMALS große Container-Divs mit `background` + `flex: 1` verwenden, die sich über die volle Spalte strecken.
> Das erzeugt riesige leere Flächen um kleine Inhalte herum.
>
> ```html
> <!-- ❌ VERBOTEN: Große Box mit wenig Inhalt -->
> <div style="flex: 1.5; background: var(--bg-dark); border-radius: 20px; padding: 30px;">
>     <div>Layer 1</div>
>     <div>Layer 2</div>
>     <!-- → 60% der Box ist leer -->
> </div>
>
> <!-- ✅ RICHTIG: Individuelle Karten, kein Container-Hintergrund -->
> <div style="flex: 1; display: flex; flex-direction: column; gap: 14px;">
>     <div style="padding: 20px 26px; background: white; border: 1px solid #e2e8f0; border-left: 4px solid var(--accent);">
>         <div style="font-size: 20px; font-weight: 700;">Layer 1</div>
>     </div>
>     <!-- Karten füllen den Raum, kein leerer Hintergrund -->
> </div>
> ```

> **⛔ Anti-Pattern: Zu kleine Fonts und zu schmale Spalten**
>
> Bei 1920×1080 sind `18px` Titel und `14px` Subtitel zu klein — auf Beamer oder großem Screen kaum lesbar.
> Seitenspalten von `280px` lassen bei 1760px verfügbarer Breite ~400px ungenutzt.
>
> | Fehler | Ergebnis |
> |--------|----------|
> | `font-size: 18px` für Kartentitel | Zu klein für Beamer, wirkt „luftig" |
> | `font-size: 14px` für Subtitel | Kaum lesbar aus Entfernung |
> | `flex: 0 0 280px` Seitenspalten | Verschenkt ~400px Breite |
> | `max-width: 680px` Center | Center zu eng, Gesamtlayout zu locker |
> | `padding: 18px 20px` auf Karten | Zu wenig Innenraum → Karten wirken gequetscht |

**Design-Prinzipien für Architecture Slides:**

| Regel | Warum |
|-------|-------|
| **Kein `flex: 1` auf Container mit `background`** | Streckt sich über volle Höhe → leerer Raum |
| **Individuelle Karten statt Container** | Jede Karte hat eigenen Rand/Hintergrund → kein Leerraum |
| **SVG-Icons in jeder Karte** | Füllt die Karte visuell, macht Inhalt scanbar |
| **`flex: 0 0 [px]` für Seitenpalten** | Fixe Breite statt stretch → kontrolliertes Layout |
| **`align-items: flex-start`** | Spalten wachsen nicht mit — Karten bleiben kompakt |
| **Fonts groß genug für Beamer** | Kartentitel ≥ 20px, Subtitel ≥ 15px — auf 1920px muss es aus 3m lesbar sein |

```html
<div class="slide">
    <div class="slide-header">
        <div>
            <h1>Platform Architecture</h1>
            <div class="subtitle">[Architektur-Prinzip]</div>
        </div>
    </div>
    <div class="slide-content" style="padding: 30px 80px 16px; display: flex; flex-direction: column;">
        <!-- KEIN flex: 1 auf diesem Container — sonst wird Bottom-Bar nach ganz unten gedrückt -->
        <div style="display: flex; align-items: flex-start; gap: 0;">
            
            <!-- Left: Data Sources (fixe Breite, 340px) -->
            <div style="flex: 0 0 340px; display: flex; flex-direction: column; gap: 14px;">
                <!-- Alle Spalten-Header gleiche Höhe (height: 30px) für Alignment -->
                <div style="font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: var(--primary-color); height: 30px; display: flex; align-items: center;">Data Sources</div>
                <div style="display: flex; gap: 16px; align-items: center; padding: 20px 26px; background: white; border: 1px solid #e2e8f0; border-left: 4px solid var(--primary-color);">
                    <div style="width: 48px; height: 48px; background: rgba(0,119,200,0.08); border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--primary-color)" stroke-width="2"><!-- icon --></svg>
                    </div>
                    <div>
                        <div style="font-size: 20px; font-weight: 700;">[Source Name]</div>
                        <div style="font-size: 15px; color: #64748b; margin-top: 3px;">[Details]</div>
                    </div>
                </div>
                <!-- ... weitere Source-Karten -->
            </div>
            
            <!-- Arrow -->
            <div style="display: flex; align-items: center; flex-shrink: 0; padding: 0 20px; align-self: center;">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#cbd5e1" stroke-width="2" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            </div>
            
            <!-- Center: Platform Layers (flex + max-width für kontrollierte Breite) -->
            <div style="flex: 1; max-width: 800px; display: flex; flex-direction: column; gap: 12px; margin: 0 auto;">
                <!-- Header: Company Logo + Kontext -->
                <div style="display: flex; align-items: center; justify-content: center; gap: 10px; height: 30px;">
                    <img src="[COMPANY_LOGO_URL]" alt="[Company]" style="height: 22px;">
                    <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: #94a3b8;">[Platform Context]</div>
                </div>
                <!-- Layer-Karten: font-size 20px Titel, 15px Subtitel (gleich wie Seitenspalten!) -->
                <div style="display: flex; gap: 16px; padding: 20px 26px; background: white; border: 1px solid #e2e8f0; border-left: 4px solid var(--accent-blue); align-items: center;">
                    <div style="width: 48px; height: 48px; background: rgba(41,181,232,0.08); border-radius: 10px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--accent-blue)" stroke-width="2"><!-- icon --></svg>
                    </div>
                    <div>
                        <div style="font-size: 20px; font-weight: 700;">[Layer Name]</div>
                        <div style="font-size: 15px; color: #64748b;">[Description]</div>
                    </div>
                </div>
                <!-- ... weitere Layer-Karten (4-5 Stück) -->
            </div>
            
            <!-- Arrow -->
            <div style="display: flex; align-items: center; flex-shrink: 0; padding: 0 20px; align-self: center;">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#cbd5e1" stroke-width="2" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            </div>
            
            <!-- Right: Consumers (fixe Breite, 340px) -->
            <div style="flex: 0 0 340px; display: flex; flex-direction: column; gap: 14px;">
                <div style="font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: #7C3AED; height: 30px; display: flex; align-items: center;">Consumers</div>
                <!-- Karten mit Icon + Text, gleiche Struktur wie Data Sources -->
            </div>
        </div>
        
        <!-- Key Principles Footer: margin-top: auto (füllt Lücke natürlich) + padding-top für Abstand -->
        <div style="display: flex; gap: 14px; margin-top: auto; padding-top: 24px; flex-shrink: 0;">
            <div style="flex: 1; padding: 18px 24px; background: #fafbfc; border: 1px solid #eceef1; border-left: 5px solid var(--primary-color);">
                <div style="font-size: 18px;"><strong>[Prinzip 1]</strong> &mdash; [Erklärung]</div>
            </div>
            <!-- ... 2-3 weitere Prinzipien -->
        </div>
    </div>
</div>
```

**Design-Regeln für den Architecture-Slide:**

| Eigenschaft | Wert | Warum |
|-------------|------|-------|
| **Seitenspalten-Breite** | **`flex: 0 0 340px`** | 280px verschenkt Platz — 340px füllt 1760px besser |
| **Center max-width** | **`max-width: 800px; margin: 0 auto;`** | 680px war zu eng → 800px nutzt den Raum |
| **Kartentitel** | **`font-size: 20px`** in ALLEN Spalten | Muss aus 3m auf Beamer lesbar sein |
| **Karten-Subtitel** | **`font-size: 15px`** | 14px ist auf Beamer kaum lesbar |
| **Icon-Größe** | **`48×48px`** konsistent | 44-46px war inkonsistent und zu klein |
| **Karten-Padding** | **`20px 26px`** | 18px 20px war zu eng — Karten wirkten gequetscht |
| **Karten-Gap** | **`14px` Seitenspalten, `12px` Center** | Konsistent, nicht zu weit auseinander |
| **Arrow-Padding** | **`padding: 0 20px`** | 14px war zu eng — Pfeile klebten an Spalten |
| **Alle Spalten-Header** | `height: 30px; display: flex; align-items: center;` | Gleiche Höhe → sauberes Alignment |
| **Center-Header** | Company Logo (`<img>`) + Platform-Kontext | Logo enthaelt bereits den Firmennamen — kein doppelter Text |
| **Bottom-Bar Font** | **`font-size: 18px`** | 17px war zu klein |
| **3-Column-Container** | **KEIN `flex: 1`** | Sonst wird Bottom-Bar nach ganz unten gedrückt |
| **Bottom-Bar margin** | `margin-top: auto; padding-top: 24px;` | Natürlicher Abstand, nicht eingeklemmt |
| **Bottom-Bar border-top** | NICHT setzen | Slide-Footer hat bereits border-top — doppelte Linie vermeiden |

**Referenz-Implementierung:** `KOSTAL/slides/kostal_simulation_slides.html` Slide 6

### 9b. Use Cases — Konsolidiert auf einem Slide (⛔ PFLICHT bei ≤ 3 Use Cases)

Wenn 2-3 Use Cases jeweils nur halb gefüllte Slides erzeugen → **auf einen Slide konsolidieren** als Karten nebeneinander.

**Karten-Aufbau (von oben nach unten):**
1. **Icon** (56px, oben links, eigene Zeile)
2. **Badge** (12px uppercase, z.B. "LIGHTHOUSE")
3. **Titel** (24px bold)
4. **Beschreibung** (17px, 2-3 Sätze)
5. **Hero-KPI** (großer Zahlenwert, 42px, in farbiger Box — visueller Anker)
6. **Checkmarks** (16px, 3 Stück mit SVG-Checkmark-Icons)

```html
<div class="slide-content" style="padding: 20px 80px 16px;">
    <!-- ⛔ KEIN height: 100% — Karten wachsen natürlich mit Inhalt -->
    <div style="display: flex; gap: 30px;">
        <div style="flex: 1; background: white; border: 1px solid #e2e8f0; border-top: 5px solid var(--primary-color); border-radius: 12px; padding: 36px 32px;">
            <!-- Icon als eigene Zeile (NICHT neben Titel) -->
            <div style="width: 56px; height: 56px; background: rgba(0,119,200,0.08); border-radius: 14px; display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
                <svg width="28" height="28"><!-- icon --></svg>
            </div>
            <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: var(--primary-color); margin-bottom: 8px;">[Badge]</div>
            <div style="font-size: 24px; font-weight: 700; line-height: 1.2; margin-bottom: 16px;">[UC Title]</div>
            <p style="font-size: 17px; color: #475569; line-height: 1.65; margin-bottom: 28px;">[Beschreibung]</p>
            <!-- Hero-KPI: großer Zahlenwert als visueller Anker — PFLICHT -->
            <div style="background: rgba(0,119,200,0.05); border-radius: 10px; padding: 20px; margin-bottom: 28px; text-align: center;">
                <div style="font-size: 42px; font-weight: 800; color: var(--primary-color); line-height: 1;">[KPI]</div>
                <div style="font-size: 14px; color: #64748b; margin-top: 6px;">[KPI-Erklärung]</div>
            </div>
            <!-- Checkmarks statt Dots -->
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--primary-color)" stroke-width="2.5" style="flex-shrink: 0;"><polyline points="20 6 9 17 4 12"/></svg>
                    <div style="font-size: 16px; color: #334155;">[Value Point]</div>
                </div>
            </div>
        </div>
        <!-- ... 2-3 Karten, jeweils mit eigener border-top Farbe -->
    </div>
</div>
```

**⛔ Anti-Patterns:**
- 3 separate Slides mit `two-column wide-left` bei denen 50% weiß bleibt → 1 dichter Slide
- `height: 100%` auf dem Flex-Container → erzeugt riesige weiße Lücke in jeder Karte
- `margin-top: auto` auf der Value-Section → drückt Business Value ganz nach unten, Lücke in der Mitte
- Icon + Badge + Titel in einer Zeile → zu gedrängt, Icon zu klein. Besser: Icon eigene Zeile, dann Badge, dann Titel
- Kleine Punkte (`8px dots`) als Bullet-Marker → zu unauffällig. Besser: SVG Checkmark-Icons (18px)
- Fehlender Hero-KPI → Karte hat keinen visuellen Anker, Text allein füllt den Platz nicht

**Referenz-Implementierung:** `KOSTAL/slides/kostal_simulation_slides.html` Slide 4

### 10. Roadmap/Timeline Slide

```html
<div class="slide">
    <div class="slide-header">
        <div>
            <h1>Implementation Roadmap</h1>
            <div class="subtitle">[Timeline-Kontext]</div>
        </div>
    </div>
    <div class="slide-content">
        <!-- Segmented Timeline Bar -->
        <div class="timeline-container">
            <div class="timeline-bar">
                <div class="timeline-segment phase1" style="width: 25%;">
                    <div class="milestone-dot"></div>
                </div>
                <div class="timeline-segment phase2" style="width: 35%;"></div>
                <div class="timeline-segment phase3" style="width: 40%;">
                    <div class="milestone-dot"></div>
                </div>
            </div>
            <div class="timeline-labels">
                <span>Q1 2026</span>
                <span>Q2 2026</span>
                <span>Q3 2026</span>
                <span>Q4 2026</span>
            </div>
        </div>
        
        <!-- Phase Cards -->
        <div class="phase-cards">
            <div class="phase-card">
                <div class="phase-badge">1</div>
                <h3>Foundation</h3>
                <ul>
                    <li>[Task 1]</li>
                    <li>[Task 2]</li>
                </ul>
            </div>
            <!-- Weitere Phasen -->
        </div>
        
        <!-- Milestones Footer -->
        <div class="milestones-footer">
            <!-- 3 Key Milestones -->
        </div>
    </div>
</div>
```

### 11. Next Steps Slide

```html
<div class="slide dark">
    <div class="slide-header" style="background: transparent;">
        <h1>Next Steps</h1>
    </div>
    <div class="slide-content">
        <div class="card-grid two-col">
            <!-- Step Cards mit Nummern -->
            <div class="step-card">
                <div class="step-number">1</div>
                <h3>[Aktion]</h3>
                <p>[Beschreibung]</p>
                <div class="step-meta">[Wer] | [Wann]</div>
            </div>
        </div>
    </div>
</div>
```

### 12. Thank You Slide

```html
<div class="slide title">
    <h1>Thank You</h1>
    <h2>Questions & Discussion</h2>
    <div class="meta">
        <strong>[Team/Company]</strong><br>
        [Kontakt-Email]
    </div>
    <div class="logos">
        <img src="[KUNDE_LOGO_URL]" alt="[Kunde]" style="height: 45px; filter: brightness(0) invert(1);">
        <span style="opacity: 0.4; font-size: 24px;">×</span>
        <img src="[COMPANY_LOGO_URL]" alt="[Company]" style="height: 40px;">
    </div>
</div>
```

### 13. Strategy Grid Slide (mit Row-Labels)

Für interne Strategy-Slides mit **mehreren Dimensionen** (z.B. Market Opportunity, GTM Matrix). Zeigt ein Grid mit Label-Spalte links und 3 gleichgroßen Karten-Spalten. Alle Boxen haben **gleiche Größe** (Grid `1fr`), kein Flex-Stretching.

**Wann verwenden:** Market Opportunity, GTM Strategy, Segmentierungs-Übersichten, Multi-Dimensionale Vergleiche

```html
<div class="slide">
    <div class="slide-header">
        <div>
            <h1>[Titel]</h1>
            <div class="subtitle">[Untertitel]</div>
        </div>
    </div>
    <div class="slide-content" style="padding: 16px 80px 80px; height: calc(1080px - 120px - 57px);">

        <!-- Grid: Label-Spalte + 3 Content-Spalten, gleich große Zeilen -->
        <div style="display: grid; grid-template-columns: 160px 1fr 1fr 1fr; grid-template-rows: 1fr 1fr 1fr; gap: 16px; height: calc(100% - 40px);">

            <!-- Row 1 Header -->
            <div style="display: flex; align-items: center; padding: 0 8px;">
                <div style="font-size: 15px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: #475569; line-height: 1.4;">[Row Label]</div>
            </div>

            <!-- Row 1: 3 Karten (je eine Farbe) -->
            <div style="background: #fafbfc; border: 1px solid #eceef1; border-left: 5px solid var(--accent-blue); padding: 28px 32px;">
                <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 16px;">
                    <!-- SVG Icon --> 
                    <div style="font-size: 24px; font-weight: 700; color: var(--text-dark);">[Titel]</div>
                </div>
                <div style="font-size: 19px; color: #334155; line-height: 1.5; margin-bottom: 18px;">[Beschreibung]</div>
                <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(41,181,232,0.1); padding: 10px 18px; border-radius: 6px;">
                    <!-- SVG Icon -->
                    <span style="font-size: 16px; font-weight: 700; color: #1a8ab5; text-transform: uppercase; letter-spacing: 0.5px;">[Badge Text]</span>
                </div>
            </div>

            <!-- Spalte 2: border-left mit --accent-green -->
            <!-- Spalte 3: border-left mit --accent-purple -->

            <!-- Row 2 + Row 3: gleiche Struktur, gleiche Farben pro Spalte -->
        </div>

    </div>
</div>
```

**Design-Regeln:**

| Element | Wert |
|---------|------|
| Grid | `grid-template-columns: 160px 1fr 1fr 1fr` — Label links, 3 gleiche Spalten |
| Zeilen | `grid-template-rows: 1fr 1fr 1fr` — **alle Boxen gleich groß** |
| Box-Padding | `28px 32px` — kein Flex, festes Padding |
| Row-Labels | 15px, uppercase, `#475569`, vertikal zentriert |
| Farbkodierung | Spalte 1: `--accent-blue`, Spalte 2: `--accent-green`, Spalte 3: `--accent-purple` |
| Content-Padding unten | `80px` — Slide nicht ganz füllen, Luft nach unten |
| Grid-Höhe | `calc(100% - 40px)` — zusätzlicher Puffer nach unten |

**Karten-Inhalt je nach Zeile variieren:**

| Zeile | Typischer Inhalt |
|-------|-----------------|
| Key Drivers | Icon + Titel + Beschreibung + farbiger Badge |
| ICP / Segment | Key-Value-Paare (`Focus:`, `Target:`) + Play-Badge (Pill) |
| Tailwinds/Challenges | Icon + Label (`Tailwind` grün, `Challenge` rot) + Text |

### 14. Scenario Comparison Slide (mit Focus Areas)

> ⛔ **Für Wettbewerbsvergleiche: NUR auf explizite Anfrage!** Dieses Template eignet sich auch für nicht-competitive Szenarien (z.B. Migrations-Szenarien, Partner-Strategien). Für Competitive Landscape gegen Databricks/Fabric etc. gilt die gleiche Regel wie bei Slide Typ 8: Nur wenn ausdrücklich gewünscht.

Für **Partner- oder Migrations-Szenarien** mit strukturierten Feldern und konkreten Handlungsempfehlungen. Oberer Bereich: 3 Szenario-Karten. Unterer Bereich: Connector-Bar + Focus Areas.

**Wann verwenden:** Partner Strategy, Market Entry Scenarios, Migration Roadmaps. Für Competitive Landscape: **nur auf explizite Anfrage**.

```html
<div class="slide">
    <div class="slide-header">
        <div>
            <h1>[Titel]</h1>
            <div class="subtitle">[Untertitel]</div>
        </div>
    </div>
    <div class="slide-content" style="padding: 16px 80px 80px; height: calc(1080px - 120px - 57px);">

        <!-- 3 Scenario Cards -->
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px; margin-bottom: 28px;">

            <!-- Scenario Card (wiederholen für jedes Szenario) -->
            <div style="background: #fafbfc; border: 1px solid #eceef1; border-left: 5px solid var(--accent-blue); padding: 32px 30px;">
                <div style="font-size: 24px; font-weight: 700; color: var(--text-dark); margin-bottom: 22px;">[Szenario-Name]</div>

                <!-- Strategie -->
                <div style="margin-bottom: 18px;">
                    <div style="font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #1a8ab5; margin-bottom: 6px;">[Feld-Label]</div>
                    <div style="font-size: 17px; color: #334155; line-height: 1.6;">[Inhalt]</div>
                </div>

                <!-- Risk / Mitigation nebeneinander -->
                <div style="display: flex; gap: 24px; margin-bottom: 18px;">
                    <div>
                        <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #DC2626; margin-bottom: 4px;">Risk</div>
                        <div style="font-size: 16px; color: #334155;">[Risk]</div>
                    </div>
                    <div>
                        <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #0a8a55; margin-bottom: 4px;">Mitigation</div>
                        <div style="font-size: 16px; color: #334155;">[Mitigation]</div>
                    </div>
                </div>

                <!-- Key Driver mit Trennlinie -->
                <div style="padding-top: 14px; border-top: 1px solid #eceef1;">
                    <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #475569; margin-bottom: 4px;">Key Driver</div>
                    <div style="font-size: 16px; color: #334155; font-weight: 500;">[Drivers]</div>
                </div>
            </div>

            <!-- Karte 2: border-left mit --accent-green -->
            <!-- Karte 3: border-left mit --accent-purple -->
        </div>

        <!-- Connector Bar (dunkler Akzent) -->
        <div style="text-align: center; margin-bottom: 28px;">
            <div style="display: inline-flex; align-items: center; gap: 14px; background: var(--bg-dark); padding: 14px 40px;">
                <!-- SVG Icon -->
                <span style="font-size: 19px; font-weight: 600; color: white;">[Verbindende Botschaft]</span>
            </div>
        </div>

        <!-- Focus Areas -->
        <div style="background: #fafbfc; border: 1px solid #eceef1; border-left: 5px solid var(--accent-blue); padding: 28px 34px;">
            <div style="font-size: 22px; font-weight: 700; color: var(--text-dark); margin-bottom: 16px;">Focus Areas</div>
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <!-- Pro Focus Area -->
                <div style="display: flex; align-items: baseline; gap: 14px; font-size: 18px; color: #334155; line-height: 1.5;">
                    <span style="font-size: 16px; font-weight: 700; color: white; background: var(--accent-blue); width: 28px; height: 28px; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0;">[Nr]</span>
                    <span>[Beschreibung mit <strong>Highlights</strong> und <strong style="color: #1a8ab5;">Targets in Blau</strong>]</span>
                </div>
            </div>
        </div>

    </div>
</div>
```

**Design-Regeln:**

| Element | Wert |
|---------|------|
| Scenario Cards | `grid-template-columns: 1fr 1fr 1fr`, `gap: 24px` |
| Card-Padding | `32px 30px` — großzügig, kein Flex |
| Card-Titel | 24px Bold |
| Feld-Labels | 13–14px, uppercase, farbkodiert (Blau/Grün/Rot je nach Typ) |
| Risk/Mitigation | Nebeneinander (`display: flex; gap: 24px`) |
| Key Driver | Abgetrennt mit `border-top: 1px solid #eceef1` |
| Connector Bar | `--bg-dark` Hintergrund, weißer Text, zentriert, inline |
| Focus Areas | Nummerierte Kreise (`--accent-blue`), Targets in `color: #1a8ab5` bold |
| Farbkodierung | Karte 1: `--accent-blue`, Karte 2: `--accent-green`, Karte 3: `--accent-purple` |

---

## Content Density: Maximale Inhalte pro Slide-Typ

Zu viel Content auf einer Slide erzeugt Overflow, Leerflächen-Probleme oder unlesbaren Text. Diese Limits gelten als Obergrenze — bei Überschreitung auf zwei Slides aufteilen statt Content zu quetschen.

| Slide-Typ | Maximale Inhalte | Typisches Problem bei Überschreitung |
|---|---|---|
| **Title Slide** | 1 Haupttitel + 1 Untertitel + optionale Tagline + Logos | — |
| **Content Slide** | 1 Titel + 4–6 Bullet Points ODER 1 Titel + 2 Absätze | Text zu klein oder Bullets abgeschnitten |
| **Card Grid** | 1 Titel + max 6 Karten (2×3 oder 3×2) | Karten zu klein, kein Platz für Hero-KPIs |
| **Architecture Diagram** | 3 Ebenen (Sources → Platform → Consumers) + max 1 Bottom-Bar | Pfeile/Labels unleserlich, Footer-Overlap |
| **Vergleichs-Tabelle** | 1 Titel + max 7 Zeilen + 1 Bottom-Bar | Zeilen zu eng, Footer-Overlap |
| **Timeline/Roadmap** | 1 Titel + max 4 Phasen + 1 Bottom-Bar | Phasen-Karten zu schmal |
| **Quote Slide** | 1 Zitat (max 3 Zeilen) + Attribution | — |

**Regeln:**
1. **Überschreitung → aufteilen**, nicht quetschen. Lieber "Teil 1/2" als unlesbaren Content.
2. Jeder Bullet Point sollte max 1–2 Zeilen lang sein.
3. Architecture-Slides mit mehr als 3 Ebenen + Bottom-Bar sind fast immer zu voll.
4. Card Grids: Jede Karte braucht genug Platz für Icon + Titel + Beschreibung + Hero-KPI. Bei 4+ Karten mit KPIs wird es eng.

---

## ⚠️ KRITISCH: Slide-Content Höhenberechnung

### Das Problem (gelöst)

Der Footer ist `position: absolute; bottom: 0` (~57px hoch). Die Content-Höhe **muss** den Footer abziehen, sonst überlappt Content den Footer — besonders bei Slides mit `margin-top: auto` oder Bottom-Bars.

### Die Lösung: Default-CSS berücksichtigt Footer

Die Base-CSS-Klasse `.slide-content` MUSS den Footer abziehen:

```css
.slide-content { padding: 60px 80px; height: calc(1080px - 140px - 57px); }  /* = 883px */
.slide.dark .slide-content { height: calc(1080px - 200px - 57px); }           /* = 823px */
```

Damit ist **kein inline-Override** mehr nötig, um Footer-Overlap zu vermeiden. Content-schwere Slides (Architektur, Multi-Column) funktionieren direkt.

### Höhen-Referenz

| Formel | Effektive Höhe | Verwendung |
|--------|----------------|------------|
| `calc(1080px - 140px - 57px)` = 883px | **Standard-CSS (Default)** | Header + Footer abgezogen |
| `calc(1080px - 200px - 57px)` = 823px | **Dark-Slides (Default)** | Größerer Header + Footer |
| Inline `calc(1080px - 260px)` = 820px | Konservativer Puffer | Nur wenn Bottom-Bar + extra Padding nötig |

### Anti-Pattern: `margin-top: auto` auf Bottom-Bars

Verwende **kein** `margin-top: auto` auf Bottom-Bars innerhalb von `.slide-content`. Es drückt Elemente an den unteren Rand des Content-Containers — bei falscher Höhe direkt hinter den Footer. Stattdessen festen `margin-top` verwenden (z.B. `margin-top: 28px`).

### Anti-Pattern: `justify-content: space-between` drückt Bottom-Bar in den Footer

Bei vertikalen Flex-Layouts mit `justify-content: space-between` wird das letzte Element (z.B. eine Vorteil/Beachten-Bar) an den unteren Rand des Content-Containers gedrückt. Wenn der Content die volle Höhe nutzt, landet die Bottom-Bar **direkt auf der Footer-Linie** — weniger als die geforderten 20px Abstand.

```html
<!-- ❌ SCHLECHT: space-between drückt Bottom-Bar bis zum Footer -->
<div class="slide-content" style="display: flex; flex-direction: column; justify-content: space-between;">
    <!-- Content-Elemente ... -->
    <div>Vorteil/Beachten Bar</div>  <!-- → klebt am Footer -->
</div>

<!-- ✅ GUT: gap steuert den Abstand, padding-bottom schützt den Footer -->
<div class="slide-content" style="display: flex; flex-direction: column; gap: 10px; padding-bottom: 16px;">
    <!-- Content-Elemente ... -->
    <div style="margin-top: auto;">Vorteil/Beachten Bar</div>
</div>
```

**Warum ist das besonders bei Architecture-Slides gefährlich?** Diese Slides haben viele vertikale Elemente (Consumer Row → Pfeile → Platform Row → Pfeile → Source Row → Bottom-Bar) und nutzen fast die volle Höhe aus. `space-between` verteilt den Restplatz gleichmäßig — aber wenn wenig Restplatz vorhanden ist, drückt es die Bottom-Bar bis zum Footer-Rand.

### Overflow-Schutz: `overflow: hidden` auf `.slide-content`

`.slide-content` (bzw. `.sf-content-area` im Corporate-Template) hat `overflow: hidden` gesetzt. Das verhindert, dass zu langer Content über die Slide-Grenzen hinaus rendert und in den Footer oder die nächste Slide überläuft.

```css
.slide-content {
    /* ... padding, height ... */
    overflow: hidden;
}
```

**Warum?** Bei fixen 1920×1080px-Slides gibt es keinen Scrollbar — überlaufender Content wäre unsichtbar im PDF und im Browser nur als Layoutbruch sichtbar. `overflow: hidden` schneidet Content sauber ab. Wenn Content abgeschnitten wird, ist das ein Signal, dass die Slide zu voll ist → Content Density Rules prüfen und ggf. auf zwei Slides aufteilen.

### Flex-Layout: Karten in Spalten

**Das häufigste Layout-Problem:** Karten in Flex-Spalten nutzen den Platz nicht gut.

#### RICHTIG: `flex: 1` auf Karten + `gap: 16px` + `justify-content: center`

Karten strecken sich gleichmäßig und füllen den verfügbaren Platz. Der Text wird mit `justify-content: center` vertikal zentriert.

```html
<!-- ✅ RICHTIG: Karten füllen Platz gleichmäßig, Text zentriert, sichtbarer Abstand -->
<div style="flex: 1; display: flex; flex-direction: column; gap: 16px;">
    <div style="flex: 1; padding: 16px 18px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: 18px; font-weight: 700;">Titel</div>
        <div style="font-size: 15px;">Subtitle</div>
    </div>
    <div style="flex: 1; padding: 16px 18px; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: 18px; font-weight: 700;">Titel</div>
        <div style="font-size: 15px;">Subtitle</div>
    </div>
</div>
```

#### Zusammenfassung der Regeln

| Element | `flex: 1`? | Warum |
|---------|-----------|-------|
| Flow-Container (äußerster) | ✅ Ja | Füllt den verfügbaren slide-content Platz |
| Spalten-Hintergrund (z.B. farbiger Bereich) | ✅ Ja | Streckt sich auf volle Spalten-Höhe |
| Einzelne Karten innerhalb der Spalte | ✅ Ja | Füllen den Platz gleichmäßig aus |
| Karten-Container | `gap: 16px` | Sichtbarer Abstand zwischen den Karten |
| Karten intern | `display: flex; flex-direction: column; justify-content: center` | Text vertikal zentriert |

### Empfohlene Größen für Karten-Content

| Element | Empfohlene Größe |
|---------|-----------------|
| Karten-Titel | **22px**, font-weight: 700 |
| Karten-Subtitle / Beschreibung | **16px**, color: **#334155** (dunkles Grau, NICHT var(--text-light)) |
| Karten-Padding | 16px 18px |
| Karten-Border-Radius | 12px (oder 16px bei größeren Karten) |
| Spalten-Header (Uppercase) | **15px**, font-weight: 700, uppercase |
| Spalten-Header Sub-Text | **14px**, color: **#475569** |
| SVG-Icons in Karten | 22px–26px |
| Pfeile zwischen Spalten | 28px–30px, Padding 8-12px, stroke: **#94a3b8** |
| Bottom-Bar (Key Messages) | font-size: **17px**, Padding: **20px 24px** |

> ⚠️ **PDF-Lesbarkeit: Kontrast und Schriftgröße**
> 
> CSS-Farben die am Bildschirm gut aussehen, sind im PDF oft zu blass.
> 
> | Eigenschaft | Zu vermeiden | Stattdessen verwenden |
> |-------------|-------------|----------------------|
> | Beschreibungstext | `color: var(--text-light)` (#666) | `color: #334155` (dunkles Slate) |
> | Labels / Subtitles | `color: rgba(255,255,255,0.4)` | `color: rgba(255,255,255,0.7)` oder heller |
> | Farbige Titel | `color: var(--accent-blue)` (#29B5E8) | Dunklere Variante: `#1a8ab5` |
> | Farbige Titel | `color: var(--gov-green)` (#00D67D) | Dunklere Variante: `#0a8a55` |
> | Farbige Titel | `color: var(--horizon-purple)` (#7C3AED) | Dunklere Variante: `#6528c7` |
> | Borders auf Farb-BG | `border: 1px solid rgba(..., 0.4)` | `border: 2px solid rgba(..., 0.6)` |
> | Schriftgröße Beschreibung | 15px | **16px** minimum |
> | Schriftgröße Titel | 18-20px | **22px** bei Flow/Diagram-Slides |
>
> **Regel:** Immer für PDF-Export optimieren. Lieber zu kräftig als zu blass.

### Bottom-Bar: Key Messages visuell abgrenzen

Bottom-Bars (z.B. 3 Key Messages unter einem Architektur-Diagramm) müssen sich klar vom Hauptbereich abheben:

```html
<!-- ✅ RICHTIG: Trennlinie, dezente Box mit Farbakzent links -->
<div style="display: flex; gap: 16px; margin-top: 20px; flex-shrink: 0; padding-top: 18px; border-top: 1px solid #eceef1;">
    <div style="flex: 1; padding: 20px 24px; background: #fafbfc; border: 1px solid #eceef1; border-left: 5px solid var(--horizon-purple);">
        <div style="font-size: 17px; line-height: 1.5;"><strong>Key Message</strong> &mdash; Details.</div>
    </div>
    <!-- weitere Boxen... -->
</div>
```

| Eigenschaft | Wert | Zweck |
|-------------|------|-------|
| `border-top` auf Container | `1px solid #eceef1` | Dezente Trennlinie zum Hauptbereich |
| `padding-top` auf Container | `18px` | Abstand nach der Trennlinie |
| `background` auf Karten | `#fafbfc` | Dezentes Grau, keine bunten Flächen |
| `border-left` auf Karten | `5px solid [akzentfarbe]` | Farbakzent -- einzige Stelle für Farbe |
| `margin-top` auf Container | `20px` | Extra Abstand zum Flow-Bereich darüber |

### CSS-Regeln für sauberen PDF-Export

Der PDF-Export (`export_pdf.py`) nutzt Chromiums nativen **Vektor-PDF-Export** via `page.pdf()`.
Chromiums Print-Pipeline hat bekannte Rendering-Bugs. Durch systematisches Testen wurden
die genauen Auslöser identifiziert:

#### Was funktioniert im PDF

| CSS-Property | Status | Hinweis |
|-------------|--------|---------|
| `border-radius` | ✅ Funktioniert | Abgerundete Ecken werden korrekt gerendert |
| `border` + `border-radius` | ✅ Funktioniert | Auch mit 1px/2px Borders sauber |
| `border-left` + `border-radius` | ✅ Funktioniert | z.B. `border-radius: 0 14px 14px 0` |
| `background: rgba(...)` | ✅ Funktioniert | Solide semi-transparente Hintergründe |
| `linear-gradient` (allein) | ✅ Funktioniert | Farbverläufe ohne Border |

#### Was Artefakte erzeugt

| CSS-Kombination | Problem | Lösung |
|----------------|---------|--------|
| `box-shadow` | Wird als **grobe, eckige Blöcke** gerendert | `export_pdf.py` setzt `box-shadow: none` automatisch im Print-CSS. Frei verwendbar im HTML. |
| `linear-gradient` + `1px border` + `border-radius` | Erzeugt **horizontale Linie** durch die Mitte des Elements | Gradient durch solide `rgba()`-Farbe ersetzen (Mittelwert des Gradients verwenden) |

> **Für Slide-Autoren:**
>
> - `border-radius` kann frei verwendet werden — funktioniert im PDF
> - `box-shadow` kann frei verwendet werden — wird im PDF automatisch entfernt
> - `linear-gradient` mit `border` + `border-radius` vermeiden → stattdessen solide `rgba()` verwenden
> - Im Zweifelsfall: **solide Hintergrundfarbe statt Gradient** bei Karten mit Border

### Vollständiges Beispiel: Multi-Column Flow Slide

```html
<div class="slide">
    <div class="slide-header">
        <h1>[Titel]</h1>
        <div class="subtitle">[Subtitle]</div>
    </div>
    <div class="slide-content" style="padding: 20px 80px 16px; display: flex; flex-direction: column;">
        
        <!-- Hauptbereich: flex: 1 damit er den Platz füllt -->
        <div style="display: flex; align-items: stretch; flex: 1;">
            
            <!-- Spalte -->
            <div style="flex: 1; display: flex; flex-direction: column;">
                <!-- Header -->
                <div style="text-align: center; padding: 14px 10px; background: [farbe]; border-radius: 14px 14px 0 0;">
                    <div style="font-size: 15px; font-weight: 700; text-transform: uppercase;">[SPALTEN-TITEL]</div>
                </div>
                <!-- Karten-Container: flex:1 + gap:16px -->
                <div style="flex: 1; background: [farbe]; border-radius: 0 0 14px 14px; padding: 14px 14px; display: flex; flex-direction: column; gap: 16px;">
                    <!-- Karten: flex:1 füllt Platz gleichmäßig, justify-content:center zentriert Text -->
                    <div style="flex: 1; padding: 16px 18px; background: white; border-radius: 12px; display: flex; flex-direction: column; justify-content: center;">
                        <div style="font-size: 18px; font-weight: 700;">[Titel]</div>
                        <div style="font-size: 15px; color: var(--text-light); margin-top: 4px;">[Subtitle]</div>
                    </div>
                    <!-- weitere Karten... -->
                </div>
            </div>
            
            <!-- Pfeil -->
            <div style="display: flex; align-items: center; flex-shrink: 0; padding: 0 8px;">
                <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#bbb" stroke-width="2.5" stroke-linecap="round"><path d="M9 6l6 6-6 6"/></svg>
            </div>
            
            <!-- weitere Spalten... -->
        </div>
        
        <!-- Bottom-Bar: flex-shrink: 0, visuell abgegrenzt -->
        <div style="display: flex; gap: 16px; margin-top: 20px; flex-shrink: 0; padding-top: 18px; border-top: 2px solid #e2e8f0;">
            <div style="flex: 1; padding: 20px 24px; background: [farbe]; border-radius: 0; border-left: 5px solid [akzentfarbe];">
                <div style="font-size: 17px; line-height: 1.5;">[Key Message]</div>
            </div>
            <!-- weitere Key Message Boxen... -->
        </div>
    </div>
    <div class="slide-footer">
        <span>[Event]</span>
        <span>[Nr]</span>
    </div>
</div>
```

---

## CSS Variables (Anpassen pro Kunde)

```css
:root {
    /* Kunden-CI */
    --primary-green: #00D67D;      /* Hauptfarbe */
    --secondary-green: #00A878;    /* Sekundärfarbe */
    --bg-dark: #11293E;            /* Dunkler Hintergrund (kühles Dunkelblau) */
    
    /* Akzentfarbe */
    --accent-blue: #29B5E8;
    
    /* Text */
    --text-dark: #1a1a1a;
    --text-light: #666666;
    
    /* Backgrounds */
    --bg-light: #f5f7f6;
}
```

### `--bg-dark` Farbwahl

> **WICHTIG:** `--bg-dark` sollte ein **kuehles, blau-getoentes Dunkelblau** sein. Der Standard ist `#11293E`.
>
> **Vermeiden:**
> - Reines Schwarz (`#000`, `#111`) — wirkt zu hart
> - Stark gesaettigte Farben — das Dunkelblau soll neutral wirken
>
> Dunkle Flaechen sind fuer Header und Akzente gedacht, der Grossteil der Slides bleibt hell.

---

## Design-Prinzipien: Box-Styling & Farbgebung

### Content-Boxen: Dezent + Farbakzent links

Das bevorzugte Muster für **alle** Content-Boxen auf hellen Slides:

```html
<!-- ✅ GUT: Dezenter Kasten mit farbigem Strich links -->
<div style="background: #fafbfc; border: 1px solid #eceef1; border-left: 5px solid var(--akzentfarbe); padding: 20px;">

<!-- ❌ SCHLECHT: Bunte Fläche, runde Ecken, Schatten -->
<div style="background: #EDE7F6; border: 2px solid #b39ddb; border-radius: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
```

| Eigenschaft | Wert | Warum |
|-------------|------|-------|
| `background` | `#fafbfc` | Dezentes Grau, hebt sich gerade so vom weißen Slide ab |
| `border` | `1px solid #eceef1` | Kaum sichtbar, gibt Struktur |
| `border-left` | `5px solid [Akzentfarbe]` | **Einzige Stelle für Farbe** auf der Box |
| `border-radius` | Keiner (eckig) | Wirkt professioneller, druckt sauberer im PDF |
| `box-shadow` | Keiner | Chromium rendert Schatten im PDF als eckige Blöcke |

### Farben sparsam einsetzen

- Farbe kommt nur über den **linken Strich** und **fetten Text/Icons** rein
- **Keine bunten Hintergrundflächen** auf Boxen -- wirkt unruhig
- Wenn mehrere Boxen nebeneinander stehen: Alle den **gleichen grauen Hintergrund**, Unterscheidung nur über `border-left`-Farbe

### Dunkle Akzentblöcke

Dunkle Hintergründe (`--bg-dark`) nur für **schmale Bars** verwenden:

- Footer-Leisten, Callout-Zeilen, Bottom-Bars
- **Nie** als ganzer Slide-Hintergrund
- Text darin weiß, Untertitel `rgba(255,255,255,0.6–0.7)`
- Kein `border-radius` auf dunklen Bars
- Innere Boxen auf dunklem Hintergrund: `background: rgba(255,255,255,0.06)` + farbiger `border-left`

### Header & Slide-Hintergrund

- **Slide-Hintergrund**: Immer weiß
- **Header**: Weißer Hintergrund, schwarzer Text (`--text-dark`), **farbiger Akzentbalken am linken Rand**
- **Footer**: Optional — kann dunkel sein (schmale Bar) oder ganz weggelassen werden

#### PFLICHT: Farbiger Balken links im Header

Jeder Content-Slide-Header hat einen **farbigen Balken** (`--accent-blue`, 12px breit) der **ganz links am Seitenrand** sitzt. Der Titel steht mit Abstand rechts davon.

```css
.slide-header {
    padding: 36px 80px 28px;
    padding-left: 0;              /* Kein linkes Padding — Balken sitzt am Rand */
    background: white;
    display: flex;
    align-items: stretch;
    gap: 40px;                    /* Abstand zwischen Balken und Titel */
}

.slide-header::before {
    content: '';
    display: block;
    width: 12px;                  /* Balken-Breite */
    flex-shrink: 0;
    background: var(--accent-blue);
}
```

#### Überschrift: Groß und dominant

| Element | Größe | Gewicht |
|---------|-------|---------|
| `h1` (Titel) | **56px** | 700 (Bold) |
| `.subtitle` | **26px** | 400 (Regular) |

> **Wichtig:** Titel und Subtitle müssen in einem **Wrapper-Div** stehen, damit sie bei `display: flex` auf dem Header untereinander bleiben:
>
> ```html
> <div class="slide-header">
>     <div>
>         <h1>[Titel]</h1>
>         <div class="subtitle">[Optional: Untertitel]</div>
>     </div>
> </div>
> ```

---

## Layout-Regeln: Harmonie statt Stretching

### KRITISCH: Kein `flex: 1` auf Content-Container

Die häufigste Ursache für schlechtes Layout ist `flex: 1` auf Boxen innerhalb eines `flex-direction: column`-Containers. Das führt dazu, dass Boxen sich auf die volle verfügbare Höhe ausdehnen und riesige leere Flächen entstehen.

```html
<!-- ❌ SCHLECHT: Boxen stretchen sich über die volle Höhe -->
<div style="display: flex; flex-direction: column; flex: 1;">
    <div style="flex: 1; padding: 20px;">Inhalt</div>  <!-- dehnt sich unnötig -->
</div>

<!-- ✅ GUT: Boxen nehmen nur den Platz ein, den sie brauchen -->
<div style="display: flex; flex-direction: column; gap: 14px;">
    <div style="padding: 18px;">Inhalt</div>  <!-- natürliche Höhe -->
</div>
```

### KRITISCH: Kein `margin-top: auto` für Schlussfolgerungs-Boxen

`margin-top: auto` schiebt eine Box an den unteren Rand des Containers — mit großem Leerraum dazwischen. Das sieht auf Slides schlecht aus.

```html
<!-- ❌ SCHLECHT: Box am Boden angepinnt mit Leerraum darüber -->
<div style="margin-top: auto; padding: 18px; background: var(--bg-dark);">
    Fazit-Box
</div>

<!-- ✅ GUT: Box folgt direkt nach dem Content mit definiertem Abstand -->
<div style="margin-top: 12px; padding: 16px; background: var(--bg-dark);">
    Fazit-Box
</div>
```

### Zwei-Spalten-Vergleich mit zentriertem Pfeil (Dark-Slides)

Häufiges Pattern: Links "alter Ansatz" (rot), rechts "neuer Ansatz" (grün), Pfeil dazwischen.

**Pfeil-Zentrierung:** `align-items: stretch` auf dem Grid sorgt dafür, dass beide Boxen gleich hoch sind. Die Pfeil-Spalte stretcht ebenfalls mit, und `display: flex; align-items: center` zentriert den Pfeil vertikal — unabhängig von der Content-Höhe.

```html
<!-- ✅ RICHTIG: Grid mit stretch → Pfeil immer mittig -->
<div style="display: grid; grid-template-columns: 1fr 60px 1fr; align-items: stretch;">
    <div style="background: var(--sf-white-06); border: 1px solid var(--sf-border); padding: 40px 44px;">
        <!-- Linke Box (Klassisch) -->
    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--sf-blue)" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
    </div>
    <div style="background: var(--sf-white-06); border: 1px solid rgba(41,181,232,0.25); padding: 40px 44px;">
        <!-- Rechte Box (Modern) -->
    </div>
</div>

<!-- ❌ FALSCH: align-items: start + align-self: center auf dem Pfeil -->
<!-- → Pfeil zentriert sich nur relativ zum Grid-Track, nicht zu den Boxen -->
```

**Key Statement nach Vergleichsboxen:** KEIN `flex: 1` auf dem Grid. Das Grid nimmt seine natürliche Höhe ein, und das Key Statement folgt direkt danach mit `margin-top: 28px`. Verbleibender Raum ist unter dem Key Statement (Breathing Room, ~25% der Slide-Höhe).

**Items innerhalb der Boxen:** Gap 28px zwischen Items für gute Platznutzung. Header-Margin 34px. Schriftgrößen: Titel 21px, Beschreibung 17px.

**Referenz:** `Sievert/slides/sievert_dwh_vs_cubes_slides.html`

### Grundregeln für harmonisches Layout

| Regel | Begründung |
|-------|-----------|
| Content nimmt **nur den Platz ein, den er braucht** | Leerfläche ≠ professionell — es wirkt unfertig |
| Kein `flex: 1` auf Content-Boxen innerhalb von Spalten-Layouts | Verhindert ungewolltes Stretching |
| Kein `margin-top: auto` für Fazit/Zusammenfassungs-Boxen | Erzeugt unharmonischen Leerraum zwischen Content und Fazit |
| Abstände über `gap` und `margin-top` steuern (12–18px) | Einheitlich, vorhersagbar, harmonisch |
| Dunkle Fazit-Bars: **kompakt** (padding 14–18px) | Soll Akzent sein, nicht dominieren |
| Hero-KPIs in Business-Value-Bars: **max 38px** Font-Größe | Größer wirkt übertrieben auf kompakten Bars |
| Tags/Badges: **zentriert** in ihrer Box (justify-content + align-items: center) | Verhindert dass kleine Tags oben-links in großen leeren Flächen hängen |

### Platznutzung: 75%-Ziel

Content (inkl. Key Statement) sollte **~75% der Slide-Höhe** füllen. Die unteren ~25% sind Breathing Room + Footer.

| Zustand | Bewertung | Aktion |
|---------|-----------|--------|
| Content bei ~60% | Zu luftig | Gaps vergrößern (20→28px), Paddings erhöhen, Schriftgrößen +1px |
| Content bei ~75% | Optimal | Professionelle Verteilung |
| Content bei ~90%+ | Zu vollgepackt | Content reduzieren, Split auf 2 Slides erwägen |

**Hebel für bessere Platznutzung (in Prioritätsreihenfolge):**
1. Item-Gaps erhöhen (z.B. 20px → 28px)
2. Box-Paddings erhöhen (z.B. 36px → 44px)
3. Header-Margins vergrößern (z.B. 28px → 34px)
4. Font-Sizes +1px (z.B. 20px → 21px für Titel)

### Checkliste vor Finalisierung

Vor dem Export jede Slide prüfen:

1. **Gibt es große leere Flächen?** → `flex: 1` oder `margin-top: auto` entfernen
2. **Sind Fazit-Boxen am Boden angepinnt?** → Auf `margin-top: 12–28px` umstellen
3. **Sind Content-Boxen gestretched?** → `flex: 1` durch natürliche Höhe ersetzen
4. **Füllt Content ~75% der Slide?** → Gaps/Paddings/Fonts anpassen (siehe Hebel oben)
5. **Sind kleine Elemente (Tags, Badges) zentriert?** → `justify-content: center` hinzufügen
6. **Ist das Gesamtbild harmonisch?** → Inhalt sollte wie ein zusammenhängendes Paket wirken, nicht wie Inseln in einem Meer aus Weißraum

---

## Icons: SVG statt Emojis

**IMMER SVG Icons verwenden, KEINE Emojis!**

### Häufig verwendete Icons

```html
<!-- Users/Team -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
    <circle cx="9" cy="7" r="4"/>
    <path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>
</svg>

<!-- Shield/Security -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
</svg>

<!-- Monitor/Self-Service -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/>
    <line x1="8" y1="21" x2="16" y2="21"/>
    <line x1="12" y1="17" x2="12" y2="21"/>
</svg>

<!-- Flag/Vendor-Agnostic -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/>
    <line x1="4" y1="22" x2="4" y2="15"/>
</svg>

<!-- Checkmark Circle -->
<svg viewBox="0 0 24 24" fill="currentColor">
    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
</svg>

<!-- Factory -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M2 20h20M4 20V10l4-4v4l4-4v4l4-4v14"/>
</svg>

<!-- Chart -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M18 20V10M12 20V4M6 20v-6"/>
</svg>

<!-- Play -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
    <polygon points="5 3 19 12 5 21 5 3"/>
</svg>
```

---

## JavaScript: Responsive Navigation

```javascript
// Dynamic slide scaling
function scaleSlides() {
    const slides = document.querySelectorAll('.slide');
    const slideWidth = 1920;
    const slideHeight = 1080;
    
    slides.forEach(slide => {
        const container = slide.parentElement;
        const containerWidth = container.clientWidth;
        const containerHeight = container.clientHeight;
        
        const scaleX = containerWidth / slideWidth;
        const scaleY = containerHeight / slideHeight;
        const scale = Math.min(scaleX, scaleY, 1);
        
        slide.style.transform = `scale(${scale})`;
    });
}

// Wheel navigation - one slide per scroll
let isScrolling = false;
document.addEventListener('wheel', (e) => {
    e.preventDefault();
    if (isScrolling) return;
    
    isScrolling = true;
    if (e.deltaY > 0) goToSlide(currentSlide + 1);
    else if (e.deltaY < 0) goToSlide(currentSlide - 1);
    
    setTimeout(() => { isScrolling = false; }, 600);
}, { passive: false });

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    switch(e.key) {
        case 'ArrowDown': case 'ArrowRight': case ' ': case 'PageDown':
            e.preventDefault();
            goToSlide(currentSlide + 1);
            break;
        case 'ArrowUp': case 'ArrowLeft': case 'PageUp':
            e.preventDefault();
            goToSlide(currentSlide - 1);
            break;
        case 'Home': goToSlide(0); break;
        case 'End': goToSlide(totalSlides - 1); break;
    }
});
```

---

## PDF-Export

Slides und Talk Tracks können als PDF exportiert werden. Das Script erkennt den Dateityp automatisch.

### Setup (einmalig)

```bash
# Aus dem Slides-Modul venv:
source .cursor/skills/slide-builder/.venv/bin/activate
pip install playwright markdown
playwright install chromium
```

### Verwendung

```bash
source .cursor/skills/slide-builder/.venv/bin/activate

# NUR Slide-Previews generieren (für visuelle Validierung, kein PDF)
python .cursor/skills/slide-builder/export_pdf.py [Kunde]/slides/[name]_slides.html --preview-only

# Slides als 16:9 PDF + Previews (auto-detected: enthält <div class="slide">)
python .cursor/skills/slide-builder/export_pdf.py [Kunde]/slides/[name]_slides.html

# Talk Track HTML als A4 PDF (auto-detected: kein <div class="slide">)
python .cursor/skills/slide-builder/export_pdf.py [Kunde]/slides/TALK_TRACK.html

# Alles auf einmal (Slides + Talk Track)
python .cursor/skills/slide-builder/export_pdf.py [Kunde]/slides/[name]_slides.html [Kunde]/slides/TALK_TRACK.html

# Optionen
python .cursor/skills/slide-builder/export_pdf.py slides.html -o output.pdf -v --wait 4000
```

### Was passiert

**Slides (.html mit `<div class="slide">` → Previews + 16:9 PDF):**
1. Chromium öffnet die HTML headless (Viewport 1920×1080)
2. **Slide-Previews:** JPEG-Screenshot (quality 85) jeder `.slide`-Div → `_slide_previews/slide_*.jpg`
3. Print-CSS wird injiziert: `@page { size: 1920px 1080px; margin: 0 }`
4. **Artefakt-Schutz:** `box-shadow` → `none` im `@media print` Kontext (Chromium rendert Schatten als eckige Blöcke)
5. `border-radius` bleibt **vollständig erhalten** — abgerundete Ecken im PDF
6. Nativer **Vektor-PDF-Export** via `page.pdf()` — Text selektierbar, scharf bei jedem Zoom
7. `print_background: true` → Hintergrundfarben und Gradients bleiben erhalten
8. Output: Previews in `_slide_previews/` + eine PDF-Seite pro Slide, exakt 16:9

**Preview-Only Modus (`--preview-only`):**
1. Chromium öffnet die HTML headless (Viewport 1920×1080)
2. JPEG-Screenshot jeder `.slide`-Div → `_slide_previews/slide_*.jpg`
3. Kein PDF-Export — nur für visuelle Validierung

**Talk Track HTML (.html OHNE `<div class="slide">` → A4 PDF):**
1. Script erkennt: Kein `<div class="slide">` → A4-Dokument, nicht Slide-Deck
2. Chromium öffnet die HTML headless (Viewport A4 bei 96dpi)
3. Das HTML enthält bereits eigene `@media print` und `@page` Styles
4. Export als A4 PDF mit Margins (20/22/25/22mm)
5. **Text ist sauber kopierbar** — kein harter Umbruch, farbcodierte Blöcke
6. Output: Mehrseitiges A4-Dokument

### Auto-Detection (HTML)

Das Script erkennt automatisch ob eine `.html`-Datei Slides oder ein Dokument enthält:

| Erkennung | Format | Ausgabe |
|-----------|--------|---------|
| `<div class="slide ...">` gefunden | 16:9 Slides | 1920×1080px pro Seite |
| Kein `class="slide"` gefunden | A4 Dokument | Standard A4 mit Margins |

### Technische Details

| Aspekt | Slides | Talk Track |
|--------|--------|-----------|
| Eingabe | `.html` (mit `<div class="slide">`) | `.html` (ohne `<div class="slide">`) |
| Seitengröße | 1920×1080px (16:9) | A4 (595×842pt) |
| Margins | 0 (randlos) | 20mm top, 22mm sides, 25mm bottom |
| Skalierung | keine (1:1) | automatisch |
| Hintergrund | erhalten | erhalten |
| **Text kopierbar** | ja | **ja (optimiert)** |

---

## Visuelle Validierung (PFLICHT)

> **Keine PDF ohne vorherige visuelle Prüfung.** Der Agent MUSS die Slide-Previews lesen
> und visuell bewerten, bevor die finale PDF exportiert wird.

### Ablauf

```
1. python export_pdf.py [Kunde]/slides/[name]_slides.html --preview-only
2. Read-Tool auf JEDE _slide_previews/slide_*.jpg anwenden
3. Pro Slide die Prüf-Checkliste durchgehen und JEDES Finding dokumentieren
4. Bei Problemen: HTML fixen → Schritt 1 wiederholen
5. Wenn alle Slides OK: PDF exportieren (ohne --preview-only)
```

> **⛔ KEIN Rubber-Stamping!** Der Agent darf NICHT einfach "sieht gut aus" sagen.
> Er MUSS pro Slide mindestens die kritischen Prüfpunkte (Footer-Spacing, Leerflächen,
> Proportionen) explizit kommentieren — auch wenn kein Problem vorliegt.
> Beispiel: "Slide 5: Footer-Abstand OK (~30px), Snowflake-Box füllt Platz, Pfeile lesbar."

### Prüf-Checkliste (pro Slide durchgehen)

| # | Was prüfen | Worauf achten | Pflicht-Kommentar? |
|---|------------|---------------|-------------------|
| 1 | **⛔ Footer-Spacing** | **KRITISCH:** Mindestens **20px sichtbarer Abstand** zwischen letztem Content-Element und Footer-Linie. Häufigster Fehler — bei JEDER Slide prüfen! Besonders bei Architecture-Slides mit Bottom-Bars. | **Ja — immer** |
| 2 | **Leerflächen & Proportionen** | Füllt der Content die Slide sinnvoll (~75%)? Gibt es große leere Flächen in Boxen? Sind Elemente proportional zueinander? Sind Pfeile/Icons groß genug um lesbar zu sein? | **Ja — immer** |
| 3 | **Logos** | Laden sie? Sichtbar auf dem Hintergrund? Invertierung korrekt auf dunklen Slides? | Nur bei Findings |
| 4 | **Text-Overflow** | Bricht Text aus Boxen aus? Unerwünschtes Wrapping in Karten? | Nur bei Findings |
| 5 | **Font-Größen** | Sind Titel/Subtitel auf Beamer aus 3m lesbar? Nicht unter 15px auf 1920px Slides? | Nur bei Findings |
| 6 | **Farben/Kontrast** | Sind Elemente auf dunklem/hellem Hintergrund sichtbar? De-Emphasis-Text mindestens `white-60`. | Nur bei Findings |
| 7 | **Icon-Größen** | Inline-Icons mindestens **20px**, Pfeile zwischen Elementen mindestens **28px** mit Stroke ≥ 2px. | Nur bei Findings |
| 8 | **Alignment** | Sind Spalten/Karten bündig? Gleiche Höhen bei nebeneinander liegenden Elementen? | Nur bei Findings |
| 9 | **Vollständigkeit** | Alle geplanten Inhalte vorhanden? Footer-Text korrekt? Slide-Nummern stimmen? | Nur bei Findings |

> **Hinweis:** Der `#slide-indicator` (die "X / 11" Navigations-Pill) wird in Previews automatisch
> ausgeblendet, damit die Previews die PDF-Darstellung korrekt abbilden. Falls die Pill trotzdem
> erscheint: `export_pdf.py` aktualisieren.

### ⛔ Footer-Overlap vermeiden (häufigster Fehler)

Der Footer (`sf-footer-bar` / `.slide-footer`) ist `position: absolute; bottom: 0` und **57px** hoch. Der Content-Bereich muss daher in `calc(1080px - 57px)` passen — inklusive aller Margins und Paddings.

**Typische Ursachen:**
- Zu viele Tabellenzeilen (max. 5 bei Standard-Padding, max. 4 mit Key Statement darunter)
- `margin-top: auto` auf Key Statements drückt sie an den untersten Rand — zusammen mit zu viel Content darüber überlappt das den Footer
- Große Card-Grids (3 Cards mit viel Text) plus Key Statement plus Footer

**Faustregel für Content-Höhe:**

| Slide-Typ | Max. Content vor Footer-Risiko |
|-----------|-------------------------------|
| Tabelle + Key Statement | max. 4–5 Zeilen (bei 16–18px Padding) |
| Card Grid (3 Spalten) + Key Statement | Cards max. ~400px Gesamthöhe |
| Zwei-Spalten-Split + Key Statement | Spalten max. ~550px |
| Architecture Slide + Bottom-Bar | Bottom-Bar mit `margin-top: auto; padding-top: 24px` |

**Fix:** Content reduzieren (weniger Zeilen/Karten), Paddings komprimieren, oder Key Statement kürzen. Key Statement immer mit `margin-bottom: 10px` versehen.

### Audience-gerechte Inhalte

| Audience | Content-Fokus | Vermeiden |
|----------|--------------|-----------|
| **CIO / C-Level** | Business Value, Time-to-Value, TCO, strategische Flexibilität | Feature-Listen, technische Architekturdetails, Produktnamen |
| **IT-Leitung / Architekten** | Architektur, Integration, Security, Governance | Reine Business-Phrasen ohne technische Substanz |
| **Fachbereich** | Konkrete Use Cases, Self-Service, Beispiel-Reports | Infrastruktur-Details, Deployment-Modelle |
| **Mixed Audience** | Business Value vorne, technische Details im Appendix | Zu tief in eine Richtung kippen |

### Vertraulichkeit: Keine Personenreferenzen aus Meeting Notes

Meeting Notes enthalten oft vertrauliche Aussagen einzelner Personen (z.B. "Jana findet, dass...", "Timke hat gesagt..."). Diese dürfen **NIEMALS** auf Slides erscheinen:

| Quelle | Auf Slides erlaubt? | Warum |
|---|---|---|
| "Jana möchte erst ein Fachkonzept" | **Nein** | Vertrauliche Meinung, vom AE im 1:1 geteilt |
| "Der CIO hat Bedenken zu..." | **Nein** | Interne Einschätzung, nicht für den Kunden bestimmt |
| "Laut Meeting: Priorität liegt auf X" | **Ja, aber neutral** | Inhalt verwenden, Quelle/Person weglassen |
| "Das Unternehmen plant eine Migration" | **Ja** | Allgemeine Fakten ohne Personenbezug |

**Goldene Regel:** Aus Meeting Notes nur die **sachlichen Anforderungen** übernehmen — nie, wer sie geäußert hat oder in welchem vertraulichen Kontext. Die Slide muss so aussehen, als käme das Wissen aus öffentlicher Recherche und allgemeiner Branchenkenntnis.

### Wichtig

- **Footer-Overlap bei JEDER Slide prüfen** — nicht nur stichprobenartig
- Bei **bekannt problemanfälligen Slide-Typen** (Architecture, Content mit Key Statement, Tabellen) besonders genau hinschauen
- Nur bei gefundenen Problemen den Fix-Loop starten, nicht prophylaktisch
- **Keine vertraulichen Personenreferenzen** aus Meeting Notes auf Slides — nur sachliche Anforderungen übernehmen

---

## Self-Update bei systematischen Problemen

Wenn der Agent im Review-Loop ein visuelles Problem findet, das **nicht kundenspezifisch** ist sondern aus dem Slide-Builder-Template stammt, soll er `slide_builder.md` direkt aktualisieren.

### Wann aktualisieren

| Aktualisieren (JA) | Nicht aktualisieren (NEIN) |
|---------------------|---------------------------|
| Template-Werte die konsistent zu schlechten Ergebnissen führen (Font-Sizes, Spaltenbreiten, Padding) | Einmaliger Kundenwunsch (spezifisches Layout) |
| Fehlende Anti-Patterns die wiederholt auftreten | Stilistische Präferenz die nicht generalisierbar ist |
| Neue Slide-Typen oder Varianten die häufig gebraucht werden | Problem das nur bei ungewöhnlichem Content auftritt |
| CSS-Bugs die bei jedem Export auftreten (Chromium Print-Rendering) | Geringfügige Anpassungen die Geschmackssache sind |

**Faustregel:** Nur aktualisieren wenn das gleiche Problem bei der nächsten Slide-Erstellung für einen anderen Kunden wieder auftreten würde. Im Zweifel: nicht aktualisieren.

### Wie aktualisieren

- Template-Werte direkt im HTML-Template-Snippet und in der Design-Regeln-Tabelle anpassen
- Anti-Pattern als Blockquote mit Erklärung dokumentieren
- Keine separate Dokumentation nötig — die Änderung ist self-documenting im Template

---

## Output-Dateien

```
[Kunde]/
├── slides/
│   ├── [name]_slides.html      ← Komplette Präsentation (16:9)
│   ├── [name]_slides.pdf       ← 16:9 PDF-Export
│   ├── _slide_previews/        ← JPEG-Previews für visuelle Validierung
│   │   ├── slide_1.jpg
│   │   ├── slide_2.jpg
│   │   └── ...
│   ├── TALK_TRACK.html         ← Speaker Notes (HTML, Quelle)
│   ├── TALK_TRACK.pdf          ← A4 PDF-Export (aus .html generiert)
│   ├── DEMO_FLOW.html          ← Demo-Spickzettel für den SE (HTML, Quelle)
│   └── DEMO_FLOW.pdf           ← A4 PDF-Export (aus .html generiert)
└── DEMO_STORYLINE.md           ← Aktualisiert mit Slide-Integration
```

**Wichtig:**
- `TALK_TRACK.html` wird aus dem Template `talk_track_template.html` erstellt. HTML ist die **einzige Quelle**.
- `DEMO_FLOW.html` ist HTML -- gleiches Design-System wie Talk Track, kompakt, SE-fokussiert, nur die Demo.
- Alle PDFs werden per `export_pdf.py` generiert.

---

## PDF-Export (PFLICHT — automatisch nach Erstellung)

> **Nach dem Erstellen jeder HTML-Datei MUSS sofort der PDF-Export ausgeführt werden.**
> PDFs sind kein optionaler Schritt — sie gehören zum Deliverable.

### Wann exportieren

| Datei erstellt | → PDF-Export sofort ausführen |
|----------------|------------------------------|
| `[name]_slides.html` | `→ [name]_slides.pdf` (16:9) |
| `TALK_TRACK.html` | `→ TALK_TRACK.pdf` (A4) |
| `DEMO_FLOW.html` | `→ DEMO_FLOW.pdf` (A4) |

### Wie exportieren

```bash
# Vom Workspace-Root aus:
".cursor/skills/slide-builder/.venv/bin/python" .cursor/skills/slide-builder/export_pdf.py [Kunde]/slides/[datei].html -v

# Mehrere Dateien auf einmal:
".cursor/skills/slide-builder/.venv/bin/python" .cursor/skills/slide-builder/export_pdf.py \
  [Kunde]/slides/[name]_slides.html \
  [Kunde]/slides/TALK_TRACK.html \
  [Kunde]/slides/DEMO_FLOW.html \
  -v
```

### Workflow-Regel

```
HTML erstellen → Qualitätscheck → PDF exportieren → ✅ Fertig
                                  ↑ NICHT optional!
```

**Ohne PDF ist die Slide-Erstellung NICHT abgeschlossen.**

---

## Integration mit Demo

Wenn `Integration: mit_demo`:

1. **Demo-Navigation prüfen** - Reihenfolge muss mit Slides übereinstimmen
2. **Transition Slide einfügen** - Nach Use Cases, vor technischen Slides
3. **DEMO_STORYLINE.md aktualisieren** - Integrierter Flow dokumentieren

```
┌───────────────────────────────────────────────────────────┐
│  Slides 1-N          │  LIVE DEMO           │  Slides N+1-Ende │
│  (Kontext)           │  (Streamlit App)     │  (Credibility)   │
└───────────────────────────────────────────────────────────┘
```

---

## Qualitätschecks

### Visual
- [ ] Kunden-CI korrekt (Farben, Logo)
- [ ] SVG Icons statt Emojis
- [ ] Responsive Scaling funktioniert
- [ ] Scroll-Snap lockt korrekt
- [ ] **PDF-Export testen** (`export_pdf.py` — nicht Browser-Druck)
- [ ] Kein `box-shadow` auf Inline-Karten (wird im PDF automatisch entfernt, aber sicherheitshalber prüfen)
- [ ] Kein `linear-gradient` + `border` + `border-radius` auf der gleichen Karte (erzeugt Linie im PDF — stattdessen solide `rgba()` verwenden)

### Layout Anti-Patterns (⛔ häufige Fehler)
- [ ] **Keine riesigen leeren Container-Boxen** — Kein `flex: 1` + `background` auf Container-Divs, die sich über die volle Spalte strecken. Stattdessen: individuelle Karten ohne umgebenden Container.
- [ ] **Architecture Slides:** Seitenspalten `flex: 0 0 280px` (fixe Breite), Mittelspalte `flex: 1; max-width: 680px; margin: 0 auto;`. `align-items: flex-start`, NICHT `stretch`.
- [ ] **Jede Karte hat eigenes SVG-Icon** — Karten ohne Icon wirken leer und erzwingen mehr Text. Ein 42-46px Icon-Container füllt die Karte visuell.
- [ ] **Einheitliche Schriftgröße:** Titel in ALLEN Spalten (links, mitte, rechts) identisch **18px**. Nicht 17px in der Mitte und 18px außen.
- [ ] **Spalten-Header Alignment:** Alle drei Spalten-Header mit `height: 30px; display: flex; align-items: center;` — gleiche Höhe für sauberes visuelles Alignment.
- [ ] **Center-Header mit Company Logo:** `<img src="[COMPANY_LOGO_URL]" style="height: 22px;">` + Platform-Kontext. **NICHT** den Firmennamen als Text dazuschreiben — das Logo enthaelt ihn bereits.
- [ ] **3-Column-Container KEIN `flex: 1`:** Sonst wird die Bottom-Bar ganz nach unten gedrückt. Stattdessen natürliche Höhe, Bottom-Bar folgt mit `margin-top: auto; padding-top: 30px;`.
- [ ] **Bottom-Bar KEIN `border-top`:** Der Slide-Footer hat bereits eine Linie — doppelte border-top vermeiden.
- [ ] **Use-Case-Slides konsolidieren:** ≤3 Use Cases → 1 Slide mit Karten nebeneinander. Jede Karte braucht: Icon (56px, eigene Zeile), Badge, Titel (24px), Beschreibung (17px), **Hero-KPI (42px, farbige Box)**, Checkmarks (16px). KEIN `height: 100%` auf Container, KEIN `margin-top: auto` auf Value-Section.

### Storyline
- [ ] Problem VOR Solution
- [ ] Requirements-Slide OHNE Features (früh)
- [ ] Feature-Mapping NACH Use Cases (spät)
- [ ] Live Demo Transition vorhanden (wenn mit Demo)
- [ ] Konkrete Next Steps

### Content
- [ ] Kunden-Terminologie verwendet
- [ ] Zitate aus Meeting Notes eingebaut
- [ ] Badges bei allen Use Cases
- [ ] Slide-Nummern konsistent

### Demo Flow (PFLICHT bei Live-Demo)
- [ ] `DEMO_FLOW.html` erstellt (gleicher Design-Ansatz wie Talk Track)
- [ ] `DEMO_FLOW.pdf` generiert per `export_pdf.py`
- [ ] **Jede Phase hat:** Zeigen + Business Value + Punkt machen
- [ ] **SQL-Blöcke** mit konkreten Befehlen
- [ ] **Rollen-Tabellen** mit Ergebnis-Indikatoren (full/partial/masked)
- [ ] **Keine Klickpfade**, keine Feature-Listen, kein Marketing
- [ ] **Takeaways** am Ende für die Überleitung zurück zu Slides
- [ ] PDF-Export getestet

### Talk Track (PFLICHT bei Slides)
- [ ] `TALK_TRACK.html` erstellt (aus Template `talk_track_template.html`)
- [ ] `TALK_TRACK.pdf` generiert per `export_pdf.py`
- [ ] **Kontext-Header** vorhanden: Teilnehmer, Ziel, CTA
- [ ] **Scanbar:** Kern-Phrasen statt ganzer Absätze, kein Fließtext zum Ablesen
- [ ] **Keine Transition-Blöcke** (implizit durch nächste Slide)
- [ ] **Keine Klickpfade** in "Was zeigen" (nur: was ist der Punkt?)
- [ ] **Erwartbare Fragen inline** bei der jeweiligen Slide (nicht am Ende gesammelt)
- [ ] Alle Block-Typen konsistent: talk, formulierung (Kern-Phrase), rueckfrage, key, warn
- [ ] Rückfrage-Blöcke nur wo sinnvoll (terminabhängig)
- [ ] Demo-Slides haben konkrete Talking Points inline (NICHT "siehe Datei XYZ")
- [ ] Demo-Steps mit Rollen und Ergebnis-Indikatoren (full/partial/masked)
- [ ] **Appendix:** "Vor dem Termin lesen" mit goldenen Regeln
- [ ] PDF-Export getestet: Text kopierbar, keine harten Umbrüche

---

## Beispiel: Syntegon Workshop

```
Slide 1:  Title
Slide 2:  Agenda
Slide 3:  Your Key Principles (NUR Requirements)
Slide 4:  The Challenge ("Splitterbombe")
Slide 5:  Use Case: Sustainability (Priority)
Slide 6:  Use Case: Inventory (Pilot)
Slide 7:  Use Case: OEE (Customer Value)
Slide 8:  Use Case: Data Sharing (Strategic)
Slide 9:  Use Case: Financial (Consolidation)
Slide 10: LIVE DEMO Transition
          ─── Demo hier zeigen ───
Slide 11: How We Deliver (Feature Mapping)
Slide 12: Platform Architecture
Slide 13: Implementation Roadmap
Slide 14: Next Steps
Slide 15: Thank You
          (KEIN "Why Us? Comparison" — nur auf explizite Anfrage)
```

---

## Weitere Layouts (via Addons)

Zusaetzliche Layouts (z.B. Corporate-Designs) werden ueber Addon-Dateien bereitgestellt. Siehe `snowflake_addon.md` als Beispiel.

