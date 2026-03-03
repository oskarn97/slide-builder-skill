#!/usr/bin/env python3
"""
PDF & PPTX Exporter für Slide Builder
========================================
Exportiert HTML-Slides als 16:9 PDF oder editierbare PPTX.
Talk Track HTML als A4 PDF. Markdown-Fallback vorhanden.

Dateityp-Erkennung:
  - .html mit <div class="slide ..."> → 16:9 Slide-PDF (oder PPTX mit --pptx)
  - .html OHNE Slides (z.B. Talk Track HTML) → A4 Dokument-PDF
  - .md / .markdown → A4 Dokument-PDF (Markdown → HTML → PDF)

PDF: Chromiums nativer Vektor-PDF-Export (page.pdf()).
PPTX: dom-to-pptx via Node.js — traversiert DOM, mappt computed styles auf
native PowerPoint-Shapes. Ergebnis: voll editierbar, keine Screenshots.

Bekannte Einschränkung (PDF): linear-gradient + border + border-radius auf dem
gleichen Element erzeugt eine horizontale Linie. Workaround: Gradient durch
solide rgba()-Hintergrundfarbe ersetzen.

Voraussetzungen:
    pip install playwright markdown
    playwright install chromium

    # Für PPTX-Export zusätzlich (im 05_slides-Verzeichnis):
    npm install dom-to-pptx playwright
    npx playwright install chromium

Verwendung:
    # Slides als 16:9 PDF (auto-detected via <div class="slide">)
    python export_pdf.py slides/horizon_catalog_slides.html

    # Slides als editierbare PPTX
    python export_pdf.py slides/horizon_catalog_slides.html --pptx

    # Nur Slide-Previews (kein PDF)
    python export_pdf.py slides/horizon_catalog_slides.html --preview-only

    # Talk Track HTML (A4) — auto-detected
    python export_pdf.py slides/TALK_TRACK.html

    # Slides + Talk Track auf einmal
    python export_pdf.py slides/horizon_catalog_slides.html slides/TALK_TRACK.html

    # Mit Optionen
    python export_pdf.py slides.html -o output.pdf -v
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent
VENV_DIR = SKILL_DIR / ".venv"
VENV_PYTHON = VENV_DIR / "bin" / "python"


def _ensure_venv():
    """Bootstrap: venv + Python-Dependencies automatisch installieren."""
    if VENV_DIR.exists() and VENV_PYTHON.exists():
        return

    print(f"[slide-builder] Erstelle Python venv in {VENV_DIR} ...")
    subprocess.run([sys.executable, "-m", "venv", str(VENV_DIR)], check=True)
    subprocess.run(
        [str(VENV_PYTHON), "-m", "pip", "install", "--quiet", "playwright", "markdown"],
        check=True,
    )
    subprocess.run(
        [str(VENV_PYTHON), "-m", "playwright", "install", "chromium"],
        check=True,
    )
    print("[slide-builder] Python-Dependencies + Chromium installiert.")


def _ensure_node_modules():
    """Bootstrap: Node-Dependencies automatisch installieren."""
    node_modules = SKILL_DIR / "node_modules"
    if node_modules.exists():
        return

    if not shutil.which("npm"):
        return

    print("[slide-builder] Installiere Node-Dependencies ...")
    subprocess.run(["npm", "install", "--silent"], cwd=str(SKILL_DIR), check=True)
    print("[slide-builder] Node-Dependencies installiert.")


def _reexec_in_venv():
    """Falls wir nicht im Skill-venv laufen, Dependencies sicherstellen und im venv neu starten."""
    if sys.prefix == str(VENV_DIR):
        return

    _ensure_venv()
    _ensure_node_modules()
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), __file__] + sys.argv[1:])


_reexec_in_venv()

from playwright.sync_api import sync_playwright


# ─── Slide Export (16:9) ────────────────────────────────────────────────────────
#
# Strategie: Nativer Vektor-PDF-Export via page.pdf().
#
# Chromiums Print-Pipeline: Was funktioniert, was nicht:
#   ✅ border-radius              → Abgerundete Ecken werden korrekt gerendert
#   ✅ border + border-radius     → Auch mit 1px/2px Borders sauber
#   ✅ background: rgba(...)      → Solide semi-transparente Hintergründe
#   ✅ linear-gradient (allein)   → Farbverläufe ohne Border
#   ❌ box-shadow                 → Grobe eckige Blöcke (→ wird auf none gesetzt)
#   ❌ linear-gradient + border + border-radius → Horizontale Linie
#      (Workaround: Gradient durch solide rgba() ersetzen)

SLIDE_WIDTH_PX = 1920
SLIDE_HEIGHT_PX = 1080


def inject_slide_print_css() -> str:
    """Print-CSS für sauberen Vektor-PDF-Export.

    Setzt Seitengröße auf 1920×1080px.  Entfernt nur box-shadow im
    Print-Kontext (Chromium rendert diese als eckige Blöcke).
    border-radius bleibt vollständig erhalten.
    """
    return """
    <style id="pdf-export-overrides">
        @page {
            size: 1920px 1080px;
            margin: 0;
        }
        @media print {
            body {
                background: white !important;
                overflow: visible !important;
                scroll-snap-type: none !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            .slide-container {
                width: 1920px !important;
                height: 1080px !important;
                page-break-after: always !important;
                page-break-inside: avoid !important;
                break-after: page !important;
                break-inside: avoid !important;
                overflow: hidden !important;
                display: block !important;
                padding: 0 !important;
                margin: 0 !important;
            }
            .slide-container:last-child {
                page-break-after: avoid !important;
                break-after: avoid !important;
            }
            .slide {
                width: 1920px !important;
                height: 1080px !important;
                transform: none !important;
                box-shadow: none !important;
                margin: 0 !important;
                position: relative !important;
            }

            /* box-shadow → none (Chromium rendert Schatten als eckige Blöcke) */
            .slide div,
            .slide section,
            .slide article,
            .slide span,
            .slide a {
                box-shadow: none !important;
            }

            * {
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
                color-adjust: exact !important;
            }
            #slide-indicator {
                display: none !important;
            }
        }
    </style>
    """


def capture_slide_previews(page, html_file: Path, verbose: bool = False) -> tuple[Path, int]:
    """Erstellt JPEG-Screenshots jeder Slide für visuelle Validierung.

    Muss VOR der Print-CSS-Injection aufgerufen werden, damit die
    Previews das Screen-Rendering zeigen (nicht das Print-Rendering).
    """
    preview_dir = html_file.parent / "_slide_previews"
    if preview_dir.exists():
        shutil.rmtree(preview_dir)
    preview_dir.mkdir()

    slides = page.locator(".slide")
    count = slides.count()

    if count == 0:
        print("  WARN: Keine .slide-Elemente gefunden, keine Previews erstellt")
        return preview_dir, 0

    for i in range(count):
        slide = slides.nth(i)
        preview_path = preview_dir / f"slide_{i + 1}.jpg"
        slide.screenshot(path=str(preview_path), type="jpeg", quality=85)
        if verbose:
            print(f"  Preview: slide_{i + 1}.jpg")

    total_size_kb = sum(f.stat().st_size for f in preview_dir.glob("*.jpg")) / 1024
    print(f"Previews: {preview_dir}")
    print(f"  {count} Slides, {total_size_kb:.0f} KB gesamt")
    return preview_dir, count


def export_slides_preview_only(
    html_path: str,
    wait_ms: int = 2000,
    verbose: bool = False,
) -> Path:
    """Generiert nur Slide-Previews (JPEG), kein PDF."""
    html_file = Path(html_path).resolve()
    if not html_file.exists():
        print(f"ERROR: Datei nicht gefunden: {html_file}")
        sys.exit(1)

    if verbose:
        print(f"  Input:  {html_file}")
        print(f"  Modus:  Preview-Only (kein PDF)")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": SLIDE_WIDTH_PX, "height": SLIDE_HEIGHT_PX})

        file_url = html_file.as_uri()
        if verbose:
            print(f"  Lade:   {file_url}")

        page.goto(file_url, wait_until="networkidle")

        if verbose:
            print(f"  Warte {wait_ms}ms auf Rendering...")
        page.wait_for_timeout(wait_ms)

        preview_dir, _ = capture_slide_previews(page, html_file, verbose)
        browser.close()

    return preview_dir


def export_slides_pdf(
    html_path: str,
    output_path: str | None = None,
    wait_ms: int = 2000,
    verbose: bool = False,
) -> Path:
    """Exportiert HTML-Slides als nativen Vektor-PDF (16:9) mit Slide-Previews."""
    html_file = Path(html_path).resolve()
    if not html_file.exists():
        print(f"ERROR: Datei nicht gefunden: {html_file}")
        sys.exit(1)

    pdf_file = Path(output_path).resolve() if output_path else html_file.with_suffix(".pdf")

    if verbose:
        print(f"  Input:  {html_file}")
        print(f"  Output: {pdf_file}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": SLIDE_WIDTH_PX, "height": SLIDE_HEIGHT_PX})

        file_url = html_file.as_uri()
        if verbose:
            print(f"  Lade:   {file_url}")

        page.goto(file_url, wait_until="networkidle")

        if verbose:
            print(f"  Warte {wait_ms}ms auf Rendering...")
        page.wait_for_timeout(wait_ms)

        capture_slide_previews(page, html_file, verbose)

        page.add_style_tag(content=inject_slide_print_css())
        page.wait_for_timeout(500)

        slide_count = page.locator(".slide").count()
        if slide_count == 0:
            slide_count = page.locator(".slide-container").count()
        if verbose:
            print(f"  Gefunden: {slide_count} Slides")

        page.pdf(
            path=str(pdf_file),
            width=f"{SLIDE_WIDTH_PX}px",
            height=f"{SLIDE_HEIGHT_PX}px",
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            print_background=True,
            prefer_css_page_size=False,
        )
        browser.close()

    file_size_mb = pdf_file.stat().st_size / (1024 * 1024)
    print(f"PDF exportiert: {pdf_file}")
    print(f"  {slide_count} Slides, {file_size_mb:.1f} MB")
    return pdf_file


# ─── Markdown / Talk Track Export (A4) ──────────────────────────────────────────

def markdown_to_html(md_path: Path) -> str:
    """Konvertiert Markdown zu einem vollständigen HTML-Dokument mit A4-optimiertem Styling."""
    try:
        import markdown
    except ImportError:
        print("ERROR: markdown ist nicht installiert.")
        print("       pip install markdown")
        sys.exit(1)

    md_text = md_path.read_text(encoding="utf-8")

    # Markdown zu HTML konvertieren
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "codehilite", "toc", "smarty"],
    )

    # Titel aus dem Dateinamen oder erstem H1
    title = md_path.stem.replace("_", " ")

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        @page {{
            size: A4;
            margin: 20mm 22mm 25mm 22mm;
        }}

        * {{
            box-sizing: border-box;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            font-size: 11pt;
            line-height: 1.65;
            color: #1a1a1a;
            max-width: 100%;
            margin: 0;
            padding: 0;
        }}

        /* Headings */
        h1 {{
            font-size: 22pt;
            font-weight: 700;
            color: #0f172a;
            margin: 0 0 16pt 0;
            padding-bottom: 8pt;
            border-bottom: 3px solid #29B5E8;
            page-break-after: avoid;
        }}

        h2 {{
            font-size: 15pt;
            font-weight: 700;
            color: #0f172a;
            margin: 24pt 0 10pt 0;
            padding-bottom: 5pt;
            border-bottom: 1.5px solid #e2e8f0;
            page-break-after: avoid;
        }}

        h3 {{
            font-size: 12pt;
            font-weight: 600;
            color: #334155;
            margin: 18pt 0 6pt 0;
            page-break-after: avoid;
        }}

        /* Paragraphs */
        p {{
            margin: 0 0 8pt 0;
            orphans: 3;
            widows: 3;
        }}

        /* Blockquotes — Talk Track "Say" Blöcke */
        blockquote {{
            margin: 8pt 0 12pt 0;
            padding: 10pt 16pt;
            background: #f8fafc;
            border-left: 4px solid #29B5E8;
            border-radius: 0 8px 8px 0;
            color: #334155;
            font-style: normal;
        }}

        blockquote em {{
            color: #64748b;
        }}

        blockquote strong {{
            color: #0f172a;
        }}

        /* Nested blockquotes */
        blockquote blockquote {{
            background: #f1f5f9;
            border-left-color: #7C3AED;
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 10pt 0 16pt 0;
            font-size: 10pt;
            page-break-inside: avoid;
        }}

        thead {{
            background: #0f172a;
            color: white;
        }}

        th {{
            padding: 8pt 12pt;
            font-weight: 600;
            text-align: left;
        }}

        td {{
            padding: 7pt 12pt;
            border-bottom: 1px solid #e2e8f0;
            vertical-align: top;
        }}

        tbody tr:nth-child(even) {{
            background: #f8fafc;
        }}

        /* Bold rows (Gesamt, total etc.) */
        td strong {{
            color: #0f172a;
        }}

        /* Lists */
        ul, ol {{
            margin: 6pt 0 12pt 0;
            padding-left: 20pt;
        }}

        li {{
            margin-bottom: 8pt;
            line-height: 1.6;
        }}

        /* Nested lists (sub-bullets) — etwas enger */
        li > ul, li > ol {{
            margin: 4pt 0 4pt 0;
        }}

        li > ul > li, li > ol > li {{
            margin-bottom: 3pt;
        }}

        /* Bold labels in list items (Talking Points) — als Mini-Header */
        li > strong:first-child {{
            display: inline;
            color: #0f172a;
        }}

        /* Code */
        code {{
            font-family: 'SF Mono', 'Fira Code', 'Consolas', monospace;
            font-size: 9.5pt;
            background: #f1f5f9;
            padding: 1pt 4pt;
            border-radius: 3px;
            color: #7C3AED;
        }}

        pre {{
            background: #0f172a;
            color: #e2e8f0;
            padding: 12pt 16pt;
            border-radius: 8px;
            overflow-x: auto;
            font-size: 9pt;
            line-height: 1.5;
            margin: 8pt 0 14pt 0;
            page-break-inside: avoid;
        }}

        pre code {{
            background: none;
            color: inherit;
            padding: 0;
        }}

        /* Horizontal Rules — Section Breaks */
        hr {{
            border: none;
            border-top: 1.5px solid #e2e8f0;
            margin: 20pt 0;
        }}

        /* Strong emphasis for speaker notes */
        strong {{
            font-weight: 600;
        }}

        /* Emphasis for transitions/stage directions */
        em {{
            font-style: italic;
            color: #64748b;
        }}

        /* Page break hints */
        h2 {{
            page-break-before: auto;
        }}
    </style>
</head>
<body>
{html_body}
</body>
</html>"""


def export_markdown_pdf(
    md_path: str,
    output_path: str | None = None,
    wait_ms: int = 1500,
    verbose: bool = False,
) -> Path:
    """Exportiert eine Markdown-Datei als A4 PDF."""
    md_file = Path(md_path).resolve()
    if not md_file.exists():
        print(f"ERROR: Datei nicht gefunden: {md_file}")
        sys.exit(1)

    pdf_file = Path(output_path).resolve() if output_path else md_file.with_suffix(".pdf")

    if verbose:
        print(f"  Input:  {md_file}")
        print(f"  Output: {pdf_file}")

    # Markdown → HTML
    html_content = markdown_to_html(md_file)

    # Temporäre HTML-Datei erstellen (im gleichen Verzeichnis für relative Links)
    tmp_html = md_file.parent / f".{md_file.stem}_tmp_export.html"
    tmp_html.write_text(html_content, encoding="utf-8")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 794, "height": 1123})  # A4 bei 96dpi

            file_url = tmp_html.as_uri()
            if verbose:
                print(f"  Lade:   {file_url}")

            page.goto(file_url, wait_until="networkidle")

            if verbose:
                print(f"  Warte {wait_ms}ms auf Rendering...")
            page.wait_for_timeout(wait_ms)

            page.pdf(
                path=str(pdf_file),
                format="A4",
                margin={
                    "top": "20mm",
                    "right": "22mm",
                    "bottom": "25mm",
                    "left": "22mm",
                },
                print_background=True,
            )
            browser.close()
    finally:
        # Temporäre Datei aufräumen
        tmp_html.unlink(missing_ok=True)

    file_size_mb = pdf_file.stat().st_size / (1024 * 1024)
    print(f"PDF exportiert: {pdf_file}")
    print(f"  A4 Format, {file_size_mb:.1f} MB")
    return pdf_file


# ─── HTML-Dokument-Export (A4) ────────────────────────────────────────────────
#
# Für Talk Track HTML-Dateien, die KEINE Slides sind.
# Diese haben bereits @media print Styles im HTML und werden als A4 gerendert.

def export_html_document_pdf(
    html_path: str,
    output_path: str | None = None,
    wait_ms: int = 2000,
    verbose: bool = False,
) -> Path:
    """Exportiert ein HTML-Dokument (z.B. Talk Track) als A4 PDF."""
    html_file = Path(html_path).resolve()
    if not html_file.exists():
        print(f"ERROR: Datei nicht gefunden: {html_file}")
        sys.exit(1)

    pdf_file = Path(output_path).resolve() if output_path else html_file.with_suffix(".pdf")

    if verbose:
        print(f"  Input:  {html_file}")
        print(f"  Output: {pdf_file}")
        print(f"  Format: A4 Dokument (kein Slide-Deck)")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 794, "height": 1123})  # A4 bei 96dpi

        file_url = html_file.as_uri()
        if verbose:
            print(f"  Lade:   {file_url}")

        page.goto(file_url, wait_until="networkidle")

        if verbose:
            print(f"  Warte {wait_ms}ms auf Rendering...")
        page.wait_for_timeout(wait_ms)

        page.evaluate("""() => {
            document.querySelectorAll('.block').forEach(el => {
                el.style.pageBreakInside = 'avoid';
                el.style.breakInside = 'avoid';
            });
            document.querySelectorAll('tr').forEach(tr => {
                tr.style.pageBreakInside = 'avoid';
                tr.style.breakInside = 'avoid';
            });
        }""")
        page.wait_for_timeout(500)

        page.pdf(
            path=str(pdf_file),
            format="A4",
            margin={
                "top": "20mm",
                "right": "22mm",
                "bottom": "25mm",
                "left": "22mm",
            },
            print_background=True,
        )
        browser.close()

    file_size_mb = pdf_file.stat().st_size / (1024 * 1024)
    print(f"PDF exportiert: {pdf_file}")
    print(f"  A4 Format, {file_size_mb:.1f} MB")
    return pdf_file


# ─── PPTX Export (editierbar, via dom-to-pptx) ──────────────────────────────

def export_slides_pptx(
    html_path: str,
    output_path: str | None = None,
    verbose: bool = False,
) -> Path:
    """Exportiert HTML-Slides als editierbare PPTX via dom-to-pptx + Node.js.

    Ruft export_pptx.js auf, das Playwright + dom-to-pptx nutzt, um den DOM
    zu traversieren und computed styles auf native PowerPoint-Shapes zu mappen.
    """
    html_file = Path(html_path).resolve()
    if not html_file.exists():
        print(f"ERROR: Datei nicht gefunden: {html_file}")
        sys.exit(1)

    pptx_file = Path(output_path).resolve() if output_path else html_file.with_suffix(".pptx")
    script_dir = Path(__file__).parent
    export_script = script_dir / "export_pptx.js"

    if not export_script.exists():
        print("ERROR: export_pptx.js nicht gefunden.")
        print(f"       Erwartet in: {export_script}")
        sys.exit(1)

    node_modules = script_dir / "node_modules" / "dom-to-pptx"
    if not node_modules.exists():
        print("ERROR: dom-to-pptx nicht installiert.")
        print(f"       cd {script_dir} && npm install dom-to-pptx playwright")
        sys.exit(1)

    cmd = ["node", str(export_script), str(html_file), "-o", str(pptx_file)]
    if verbose:
        cmd.append("-v")
        print(f"  Input:  {html_file}")
        print(f"  Output: {pptx_file}")
        print(f"  Cmd:    {' '.join(cmd)}")

    result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(script_dir))

    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)

    if result.returncode != 0:
        print(f"ERROR: PPTX-Export fehlgeschlagen (exit code {result.returncode})")
        sys.exit(1)

    return pptx_file


def is_slide_html(html_path: str) -> bool:
    """Prüft ob eine HTML-Datei Slides enthält oder ein Dokument ist.

    Erkennt Slide-Decks anhand von <div class="slide"> oder <div class="slide dark"> etc.
    NICHT matchen: class="slide-section", class="slide-container" (Talk Track HTML).
    """
    content = Path(html_path).read_text(encoding="utf-8", errors="replace")
    import re
    # Matcht class="slide", class="slide dark", class="slide title" etc.
    # Matcht NICHT class="slide-section", class="slide-container" etc.
    return bool(re.search(r'class\s*=\s*["\']slide(?:\s+[\w-]+)*["\']', content))


# ─── Main ───────────────────────────────────────────────────────────────────────

def export_file(
    file_path: str,
    output_path: str | None,
    wait_ms: int,
    verbose: bool,
    preview_only: bool = False,
    pptx: bool = False,
):
    """Erkennt den Dateityp und ruft den passenden Exporter auf."""
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".html":
        if is_slide_html(file_path):
            if pptx:
                if verbose:
                    print(f"  Erkannt: HTML-Slides (16:9) — PPTX-Export")
                export_slides_pptx(file_path, output_path, verbose)
            elif preview_only:
                if verbose:
                    print(f"  Erkannt: HTML-Slides (16:9) — Preview-Only")
                export_slides_preview_only(file_path, wait_ms, verbose)
            else:
                if verbose:
                    print(f"  Erkannt: HTML-Slides (16:9)")
                export_slides_pdf(file_path, output_path, wait_ms, verbose)
        else:
            if pptx:
                print(f"  SKIP: {path.name} ist kein Slide-Deck, --pptx ignoriert")
                return
            if preview_only:
                print(f"  SKIP: {path.name} ist kein Slide-Deck, --preview-only ignoriert")
                return
            if verbose:
                print(f"  Erkannt: HTML-Dokument (A4)")
            export_html_document_pdf(file_path, output_path, wait_ms, verbose)
    elif suffix in (".md", ".markdown"):
        if pptx or preview_only:
            print(f"  SKIP: {path.name} ist Markdown, --pptx/--preview-only ignoriert")
            return
        export_markdown_pdf(file_path, output_path, wait_ms, verbose)
    else:
        print(f"ERROR: Unbekannter Dateityp: {suffix}")
        print("       Unterstützt: .html (Slides/Dokumente), .md (Markdown → A4 PDF, Fallback)")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Exportiert Slides (HTML→16:9) als PDF oder editierbare PPTX, Talk Tracks (HTML→A4) als PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  # Slides als 16:9 PDF + Previews (auto-detected via <div class="slide">)
  python export_pdf.py slides/workshop_slides.html

  # Slides als editierbare PPTX (voll editierbar in PowerPoint)
  python export_pdf.py slides/workshop_slides.html --pptx

  # Nur Slide-Previews, kein PDF (für visuelle Validierung)
  python export_pdf.py slides/workshop_slides.html --preview-only

  # Talk Track HTML als A4 PDF (auto-detected: kein <div class="slide">)
  python export_pdf.py slides/TALK_TRACK.html

  # Slides + Talk Track auf einmal
  python export_pdf.py slides/workshop_slides.html slides/TALK_TRACK.html

  # Mit Optionen
  python export_pdf.py slides.html -o output.pdf -v --wait 3000
        """,
    )
    parser.add_argument("files", nargs="+", help="HTML-Dateien (Slides oder Talk Track)")
    parser.add_argument("-o", "--output", help="Output-Pfad (nur bei einer Datei)")
    parser.add_argument(
        "--pptx",
        action="store_true",
        help="Editierbare PPTX statt PDF exportieren (nur für Slide-Decks)",
    )
    parser.add_argument(
        "--preview-only",
        action="store_true",
        help="Nur JPEG-Previews generieren, kein PDF (nur für Slide-Decks)",
    )
    parser.add_argument(
        "--wait",
        type=int,
        default=2000,
        help="Wartezeit in ms nach Laden (default: 2000)",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose Output")

    args = parser.parse_args()

    if args.output and len(args.files) > 1:
        print("ERROR: --output kann nur bei einer einzelnen Datei verwendet werden.")
        sys.exit(1)

    if args.output and args.preview_only:
        print("ERROR: --output und --preview-only können nicht kombiniert werden.")
        sys.exit(1)

    if args.pptx and args.preview_only:
        print("ERROR: --pptx und --preview-only können nicht kombiniert werden.")
        sys.exit(1)

    for file_path in args.files:
        print(f"Exportiere: {file_path}")
        export_file(file_path, args.output, args.wait, args.verbose, args.preview_only, args.pptx)
        print()


if __name__ == "__main__":
    main()
