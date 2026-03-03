# Slide Builder Skill

AI-gestützter Cursor Skill zur Erstellung professioneller HTML-Slides (16:9), Talk Tracks und Demo Flows mit automatischem PDF-Export.

## Features

- **HTML-Slides** — Responsive 16:9 Präsentationen mit Scroll-Snap Navigation
- **Zwei Layouts** — `custom` (Kunden-CI) oder `snowflake_corporate` (Snowflake-Branding)
- **Talk Track** — Farbcodierte Speaker Notes mit Demo-Steps
- **Demo Flow** — Kompakter Spickzettel für Live-Demos
- **PDF-Export** — Automatisch via Playwright/Chromium (Slides 16:9, Talk Track/Demo Flow A4)
- **Visuelle Validierung** — JPEG-Previews vor PDF-Export zur Qualitätskontrolle
- **Auto-Setup** — Dependencies werden beim ersten Aufruf automatisch installiert

## Prerequisites

- **Python >= 3.11**
- **Node.js >= 18** (optional, für PPTX-Export)

## Installation

### 1. In den Cursor Workspace einbinden

```bash
# Option A: Direkt klonen (empfohlen)
git clone git@github.com:oskarn97/slide-builder-skill.git <workspace>/.cursor/skills/slide-builder

# Option B: Separat klonen und verlinken
git clone git@github.com:oskarn97/slide-builder-skill.git ~/slide-builder-skill
ln -s ~/slide-builder-skill <workspace>/.cursor/skills/slide-builder
```

Das war's. Beim ersten `export_pdf.py`-Aufruf werden automatisch installiert:
- Python venv mit `playwright` und `markdown`
- Chromium Browser (headless, für PDF-Rendering)
- Node modules (`dom-to-pptx`, für optionalen PPTX-Export)

### Update

```bash
cd <workspace>/.cursor/skills/slide-builder
git pull
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
├── export_pdf.py                    ← PDF/Preview-Export (auto-installiert Dependencies)
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
