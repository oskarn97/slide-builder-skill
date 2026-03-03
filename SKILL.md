---
name: slide-builder
description: "Erstellt professionelle HTML-Slides für Kundenpräsentationen (16:9, responsive, PDF-exportierbar). Use for ALL slide/presentation requests: Slides erstellen, Präsentation bauen, HTML Slides, Kundenpräsentation, Talk Track, Demo Flow. Triggers: Slides erstellen, Präsentation, neue Slides für [Kunde], Talk Track, Demo Flow, Slide Deck, Workshop Slides, PDF Export."
---

# Slide Builder - HTML Presentation Module

Erstellt professionelle HTML-Slides, Talk Tracks und Demo Flows für Kundenpräsentationen.

## Auto-Update (PFLICHT)

Vor jeder Verwendung den Skill aktualisieren. Verwende den Ordner dieser SKILL.md-Datei als Pfad:

```bash
git -C "<Pfad zum Ordner dieser SKILL.md>" pull --ff-only 2>/dev/null || true
```

## Anleitung

**Lies sofort die vollständige Anleitung:**

```
.cursor/skills/slide-builder/slide_builder.md
```

Dieses Dokument enthält alle Slide-Typen, Design-Prinzipien, CSS-Regeln, Layout-Muster und Qualitätschecks.

## Quick Start

```
@.cursor/skills/slide-builder/slide_builder.md

Kunde: @[Kundenordner]
Sprache: [deutsch | englisch]
Integration: [standalone | mit_demo]
Layout: [custom | ...]
```

## Layout-Optionen

| Layout | Verwendung |
|--------|-----------|
| `custom` (Standard) | Kunden-CI, weiße Slides, individuelle Farben, Kunden- + Company-Logo |

Weitere Layouts koennen ueber Addon-Dateien bereitgestellt werden (z.B. `snowflake_addon.md` fuer Snowflake Corporate Layout).

## Templates

| Template | Pfad | Verwendung |
|----------|------|-----------|
| Slide Template (Custom) | `.cursor/skills/slide-builder/slide_template.html` | Kunden-Slides |
| Talk Track Template | `.cursor/skills/slide-builder/talk_track_template.html` | Speaker Notes |

Addon-spezifische Templates (z.B. `slide_template_corporate.html`) werden in der jeweiligen Addon-Datei dokumentiert.

## Output-Dateien

```
[Kunde]/slides/
├── [name]_slides.html      ← Präsentation (16:9)
├── [name]_slides.pdf       ← PDF-Export
├── _slide_previews/        ← JPEG-Previews für visuelle Validierung
│   ├── slide_1.jpg
│   └── ...
├── TALK_TRACK.html         ← Speaker Notes (HTML)
├── TALK_TRACK.pdf          ← A4 PDF-Export
├── DEMO_FLOW.html          ← Demo-Spickzettel (HTML)
└── DEMO_FLOW.pdf           ← A4 PDF-Export
```

## Workflow: Visuelle Validierung → PDF-Export

> **KEIN PDF-Export ohne vorherige visuelle Validierung!**
> Der Agent MUSS Slide-Previews generieren, visuell prüfen und Probleme fixen, BEVOR die PDF exportiert wird.

Dependencies (Python venv, Playwright, Chromium, Node modules) werden beim ersten Aufruf automatisch installiert.

```bash
# 1. Previews generieren (kein PDF)
python .cursor/skills/slide-builder/export_pdf.py [Kunde]/slides/[name]_slides.html --preview-only

# 2. Previews mit Read-Tool visuell prüfen (Footer-Overlap, Spacing, Logos, Text-Overflow)
# 3. Bei Problemen: HTML fixen → Schritt 1 wiederholen
# 4. Wenn alle Slides OK: PDF exportieren

python .cursor/skills/slide-builder/export_pdf.py [Kunde]/slides/[name]_slides.html
python .cursor/skills/slide-builder/export_pdf.py [Kunde]/slides/TALK_TRACK.html
python .cursor/skills/slide-builder/export_pdf.py [Kunde]/slides/DEMO_FLOW.html
```

## Key Rules

- **TALK_TRACK.html (PFLICHT):** IMMER erstellen wenn Slides erstellt werden. Template: `talk_track_template.html`. Scanbar, Stichpunkte, keine Absätze. Demo-Slides inline mit konkreten Talking Points.
- **DEMO_FLOW.html (PFLICHT bei Live-Demo):** IMMER erstellen wenn eine Demo Teil der Präsentation ist. Referenz: `Jungheinrich/slides/DEMO_FLOW.html`. Kompakt, SE-Perspektive: Zeigen → Business Value → Punkt machen.
- **PDF-Export:** IMMER als letzter Schritt nach visueller Validierung — Slides, Talk Track UND Demo Flow
- **KEIN Competitive Comparison:** Vergleichstabellen gegen Wettbewerber standardmaessig NICHT einbauen. Nur auf **explizite Anfrage** des Nutzers. Das Template existiert in `slide_builder.md` (Slide Typ 8 + 14), wird aber NIE automatisch verwendet.
- **Storyline:** Problem → Impact → Solution (NICHT umgekehrt!)
- **Requirements aufteilen:** Frueeh "Your Key Principles" (NUR Requirements), spaet "How We Deliver" (Feature-Mapping)
- **Icons:** IMMER SVG, KEINE Emojis
- **Logos:** Company-Logo + Kunden-Logo von Wikimedia Commons (SVG bevorzugt). Addon-Dateien koennen spezifische Logo-URLs bereitstellen.
- **PDF-sicher:** Kein `linear-gradient` + `border` + `border-radius` kombinieren, `box-shadow` wird automatisch entfernt
- **Hoehe:** Default-CSS beruecksichtigt Footer automatisch (`calc(1080px - 140px - 57px)`). Kein `margin-top: auto` auf Bottom-Bars verwenden.

## Addons

Plattform-spezifische Erweiterungen werden ueber Addon-Dateien bereitgestellt:

| Addon | Datei | Inhalt |
|-------|-------|--------|
| Snowflake | `snowflake_addon.md` | Corporate Layout, Logo-URLs, Raven Report Integration, Kosten-Messaging |

Bei Snowflake-Praesentationen: **Zusaetzlich** `snowflake_addon.md` lesen fuer plattformspezifische Regeln, Templates und Slide-Typen.
