# Slide Builder Skill

AI-gestützter Cursor Skill zur Erstellung professioneller HTML-Slides (16:9), Talk Tracks und Demo Flows mit automatischem PDF-Export.

## Features

- **HTML-Slides** — Responsive 16:9 Präsentationen mit Scroll-Snap Navigation
- **Zwei Layouts** — `custom` (Kunden-CI) oder `snowflake_corporate` (Snowflake-Branding)
- **Talk Track** — Farbcodierte Speaker Notes mit Demo-Steps
- **Demo Flow** — Kompakter Spickzettel für Live-Demos
- **PDF-Export** — Automatisch via Playwright/Chromium (Slides 16:9, Talk Track/Demo Flow A4)
- **Visuelle Validierung** — JPEG-Previews vor PDF-Export zur Qualitätskontrolle

## Prerequisites

- **Python >= 3.11**
- **Node.js >= 18**
- **Cursor IDE**

## Installation

### 1. Repo klonen

```bash
git clone git@github.com:oskarn97/slide-builder-skill.git
```

### 2. In den Cursor Workspace einbinden

Den Skill-Ordner nach `.cursor/skills/slide-builder/` im Workspace kopieren oder verlinken:

```bash
# Option A: Symlink (empfohlen — bleibt mit dem Repo synchron)
ln -s /pfad/zu/slide-builder-skill <workspace>/.cursor/skills/slide-builder

# Option B: Direkt klonen
git clone git@github.com:oskarn97/slide-builder-skill.git <workspace>/.cursor/skills/slide-builder
```

### 3. Dependencies installieren

```bash
cd <workspace>/.cursor/skills/slide-builder

# Python
python3 -m venv .venv
source .venv/bin/activate
pip install playwright markdown
playwright install chromium

# Node
npm install
```

## Verwendung in Cursor

Im Chat oder Composer den Skill referenzieren:

```
@.cursor/skills/slide-builder/slide_builder.md

Kunde: @[Kundenordner]
Sprache: deutsch
Layout: custom
```

### PDF-Export

```bash
# Previews generieren (visuelle Validierung)
python .cursor/skills/slide-builder/export_pdf.py slides.html --preview-only

# PDF exportieren
python .cursor/skills/slide-builder/export_pdf.py slides.html
```

## Dateistruktur

```
slide-builder/
├── SKILL.md                         ← Cursor Skill Entry Point
├── slide_builder.md                 ← Vollständige Anleitung (Slide-Typen, CSS, Layouts)
├── export_pdf.py                    ← PDF/Preview-Export (Playwright/Chromium)
├── export_pptx.js                   ← PPTX-Export (optional)
├── slide_template.html              ← HTML-Template: Custom Layout
├── slide_template_corporate.html    ← HTML-Template: Snowflake Corporate Layout
├── talk_track_template.html         ← HTML-Template: Talk Track
└── package.json                     ← Node Dependencies
```

## Output

Der Skill generiert pro Präsentation:

```
[Kunde]/slides/
├── [name]_slides.html        ← Präsentation (16:9, im Browser öffnen)
├── [name]_slides.pdf         ← PDF-Export
├── _slide_previews/          ← JPEG-Previews pro Slide
├── TALK_TRACK.html + .pdf    ← Speaker Notes
└── DEMO_FLOW.html + .pdf     ← Demo-Spickzettel
```
