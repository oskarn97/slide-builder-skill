#!/usr/bin/env node
/**
 * PPTX Exporter für Slide Builder
 * ================================
 * Exportiert HTML-Slides als editierbare PPTX via dom-to-pptx + Playwright.
 *
 * dom-to-pptx traversiert den DOM, liest computed styles (Flexbox/Grid-Positionen,
 * Gradients, Shadows, Border-Radius) und mappt sie auf native PowerPoint-Shapes.
 * Ergebnis: voll editierbarer, vektorbasierter PPTX — kein Screenshot-Ansatz.
 *
 * Gradient-Fix: dom-to-pptx rendert CSS linear-gradient als rasterisierte SVG-Bilder.
 * Dieses Script extrahiert Gradient-Infos vor dem Export, setzt Slide-Backgrounds
 * auf solid Fallback-Farben, und patcht danach die PPTX-XML mit nativen gradFill-
 * Elementen. Ergebnis: vektorbasierte Hintergründe, ~80% kleinere Dateien.
 *
 * Voraussetzungen:
 *   npm install dom-to-pptx playwright
 *   npx playwright install chromium
 *
 * Verwendung:
 *   node export_pptx.js slides/workshop_slides.html
 *   node export_pptx.js slides/workshop_slides.html -o output.pptx
 *   node export_pptx.js slides/workshop_slides.html --verbose
 *
 * Aufgerufen von export_pdf.py via --pptx Flag.
 */

const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");
const JSZip = require(path.join(__dirname, "node_modules", "jszip"));

const SLIDE_WIDTH = 1920;
const SLIDE_HEIGHT = 1080;

function parseArgs() {
  const args = process.argv.slice(2);
  const opts = { verbose: false, output: null, input: null, svgAsVector: true };

  for (let i = 0; i < args.length; i++) {
    if (args[i] === "-v" || args[i] === "--verbose") {
      opts.verbose = true;
    } else if ((args[i] === "-o" || args[i] === "--output") && args[i + 1]) {
      opts.output = args[++i];
    } else if (args[i] === "--no-svg-vector") {
      opts.svgAsVector = false;
    } else if (!args[i].startsWith("-")) {
      opts.input = args[i];
    }
  }

  if (!opts.input) {
    console.error("Usage: node export_pptx.js <slides.html> [-o output.pptx] [-v]");
    process.exit(1);
  }

  return opts;
}

/**
 * Parst einen CSS linear-gradient String und gibt Winkel + Farbstops zurück.
 * Handles both hex und computed rgb() Formate (mit Kommas in den Klammern).
 *
 * Input:  "linear-gradient(135deg, rgb(26, 26, 46) 0%, rgb(15, 52, 96) 100%)"
 * Output: { angle: 135, stops: [{ position: 0, color: "1A1A2E" }, ...] }
 */
function parseLinearGradient(cssGradient) {
  const outerMatch = cssGradient.match(/linear-gradient\((.+)\)$/);
  if (!outerMatch) return null;

  // Smart split: Split by commas that are NOT inside parentheses
  const inner = outerMatch[1];
  const parts = [];
  let depth = 0;
  let current = "";
  for (const ch of inner) {
    if (ch === "(") depth++;
    else if (ch === ")") depth--;
    if (ch === "," && depth === 0) {
      parts.push(current.trim());
      current = "";
    } else {
      current += ch;
    }
  }
  if (current.trim()) parts.push(current.trim());

  let angle = 180;
  let colorStartIndex = 0;

  if (parts[0].includes("deg")) {
    angle = parseFloat(parts[0]);
    colorStartIndex = 1;
  } else if (parts[0].startsWith("to ")) {
    const dir = parts[0].replace("to ", "");
    const dirMap = {
      top: 0, right: 90, bottom: 180, left: 270,
      "top right": 45, "right top": 45,
      "bottom right": 135, "right bottom": 135,
      "bottom left": 225, "left bottom": 225,
      "top left": 315, "left top": 315,
    };
    angle = dirMap[dir] ?? 180;
    colorStartIndex = 1;
  }

  const stops = [];
  for (let i = colorStartIndex; i < parts.length; i++) {
    const stopMatch = parts[i].match(/(#[0-9a-fA-F]{3,8}|rgba?\([^)]+\))\s*(\d+%)?/);
    if (!stopMatch) continue;

    let color = stopMatch[1];
    let position = stopMatch[2] ? parseInt(stopMatch[2]) : null;

    if (position === null) {
      const idx = i - colorStartIndex;
      const total = parts.length - colorStartIndex;
      position = total > 1 ? Math.round((idx / (total - 1)) * 100) : 0;
    }

    if (color.startsWith("#")) {
      color = color.slice(1);
      if (color.length === 3) {
        color = color[0] + color[0] + color[1] + color[1] + color[2] + color[2];
      }
    } else if (color.startsWith("rgb")) {
      const rgb = color.match(/\d+/g);
      if (rgb && rgb.length >= 3) {
        color = rgb
          .slice(0, 3)
          .map((c) => parseInt(c).toString(16).padStart(2, "0"))
          .join("");
      }
    }

    stops.push({ position: position * 1000, color: color.toUpperCase() });
  }

  return stops.length >= 2 ? { angle, stops } : null;
}

/**
 * Konvertiert CSS-Grad-Winkel in PowerPoints Winkel-System.
 * CSS: 0deg = nach oben, 90deg = nach rechts, 135deg = nach unten-rechts
 * OOXML: Winkel in 60.000stel Grad, 0 = rechts, 90° = unten
 */
function cssAngleToOoxml(cssDeg) {
  const ooxml = (cssDeg + 270) % 360;
  return ooxml * 60000;
}

/**
 * Generiert OOXML-XML für einen nativen Gradient-Hintergrund.
 */
function buildGradientBgXml(gradientInfo) {
  const { angle, stops } = gradientInfo;
  const oomAngle = cssAngleToOoxml(angle);

  const gsEntries = stops
    .map(
      (s) =>
        `<a:gs pos="${s.position}"><a:srgbClr val="${s.color}"/></a:gs>`
    )
    .join("");

  return `<p:bg><p:bgPr><a:gradFill rotWithShape="0"><a:gsLst>${gsEntries}</a:gsLst><a:lin ang="${oomAngle}" scaled="1"/></a:gradFill><a:effectLst/></p:bgPr></p:bg>`;
}

/**
 * Generiert OOXML-XML für einen soliden Hintergrund.
 */
function buildSolidBgXml(hexColor) {
  return `<p:bg><p:bgPr><a:solidFill><a:srgbClr val="${hexColor}"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>`;
}

/**
 * Post-Processing: Patcht die PPTX-Datei, um native Slide-Backgrounds zu setzen
 * und die rasterisierten Gradient-Bilder zu entfernen.
 */
async function patchPptxBackgrounds(pptxBuffer, slideBackgrounds, verbose) {
  const zip = await JSZip.loadAsync(pptxBuffer);

  for (let i = 0; i < slideBackgrounds.length; i++) {
    const bg = slideBackgrounds[i];
    if (!bg) continue;

    const slideFile = `ppt/slides/slide${i + 1}.xml`;
    const slideXml = await zip.file(slideFile)?.async("string");
    if (!slideXml) continue;

    let bgXml;
    if (bg.type === "gradient") {
      bgXml = buildGradientBgXml(bg.gradient);
      if (verbose) console.log(`  Slide ${i + 1}: Native Gradient-Background gesetzt`);
    } else if (bg.type === "solid") {
      bgXml = buildSolidBgXml(bg.color);
      if (verbose) console.log(`  Slide ${i + 1}: Native Solid-Background gesetzt`);
    }

    if (!bgXml) continue;

    // Remove existing <p:bg> if present
    let patched = slideXml.replace(/<p:bg>.*?<\/p:bg>/s, "");

    // Insert <p:bg> between <p:cSld ...> and <p:spTree>
    patched = patched.replace(
      /(<p:cSld[^>]*>)\s*(<p:spTree>)/,
      `$1${bgXml}$2`
    );

    // Remove the first large image shape (the rasterized gradient background).
    // It's typically the first <p:pic> with position x=0, y=0 that spans the full slide.
    const fullSlideImgPattern =
      /<p:pic>(?=.*?<a:off x="0" y="0"\/>)(?=.*?<a:ext cx="9144000").*?<\/p:pic>/s;
    const matchedImg = patched.match(fullSlideImgPattern);
    if (matchedImg) {
      patched = patched.replace(fullSlideImgPattern, "");

      // Extract the rId of the removed image to clean up media file + relationship
      const rIdMatch = matchedImg[0].match(/r:embed="(rId\d+)"/);
      if (rIdMatch) {
        const relsFile = `ppt/slides/_rels/slide${i + 1}.xml.rels`;
        let relsXml = await zip.file(relsFile)?.async("string");
        if (relsXml) {
          const targetMatch = relsXml.match(
            new RegExp(`Id="${rIdMatch[1]}"[^>]*Target="([^"]+)"`)
          );
          if (targetMatch) {
            const mediaPath = `ppt/${targetMatch[1].replace("../", "")}`;
            zip.remove(mediaPath);

            // Remove the relationship entry itself to prevent "needs repair"
            relsXml = relsXml.replace(
              new RegExp(`<Relationship[^>]*Id="${rIdMatch[1]}"[^>]*/>`),
              ""
            );
            zip.file(relsFile, relsXml);

            if (verbose) console.log(`  Slide ${i + 1}: Gradient-Bild + Relationship entfernt (${mediaPath})`);
          }
        }
      }
    }

    zip.file(slideFile, patched);
  }

  return await zip.generateAsync({ type: "nodebuffer" });
}

/**
 * Bereinigt dom-to-pptx Packaging-Bugs:
 * - Entfernt [Content_Types].xml Overrides für nicht-existierende Dateien
 *   (dom-to-pptx registriert einen slideMaster pro Slide, erstellt aber nur einen)
 */
async function cleanupPptxPackage(pptxBuffer, verbose) {
  const JSZip = require("jszip");
  const zip = await JSZip.loadAsync(pptxBuffer);

  const allFiles = new Set(Object.keys(zip.files));
  const ctFile = "[Content_Types].xml";
  let ct = await zip.file(ctFile).async("string");

  let removed = 0;
  ct = ct.replace(/<Override\s+PartName="([^"]+)"[^>]*\/>/g, (match, partName) => {
    const zipPath = partName.replace(/^\//, "");
    if (!allFiles.has(zipPath)) {
      removed++;
      return "";
    }
    return match;
  });

  if (removed > 0) {
    zip.file(ctFile, ct);
    if (verbose) console.log(`  Content_Types bereinigt: ${removed} Phantom-Einträge entfernt`);
  }

  return await zip.generateAsync({ type: "nodebuffer" });
}

/**
 * Ermittelt TTF-Font-URLs für alle Google Fonts im HTML.
 * Google Fonts liefert TTF-Format wenn der User-Agent "Mozilla/5.0" ist (statt woff2).
 * dom-to-pptx's fonteditor-core kann nur TTF/OTF/WOFF lesen, nicht woff2.
 */
async function resolveFontUrls(page, verbose) {
  const https = require("https");

  // Detect Google Fonts URLs from the loaded page
  const fontLinks = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('link[href*="fonts.googleapis.com"]')).map(
      (l) => l.href
    );
  });

  if (fontLinks.length === 0) return [];

  const fonts = [];
  for (const cssUrl of fontLinks) {
    if (verbose) console.log(`  Font-CSS: ${cssUrl.substring(0, 80)}...`);

    // Fetch CSS with user-agent that triggers TTF response
    const cssText = await new Promise((resolve, reject) => {
      https
        .get(cssUrl, { headers: { "User-Agent": "Mozilla/5.0" } }, (res) => {
          let data = "";
          res.on("data", (d) => (data += d));
          res.on("end", () => resolve(data));
        })
        .on("error", reject);
    });

    // Extract font families and their TTF URLs
    const blocks = cssText.split("@font-face");
    const seenFamilies = new Set();

    for (const block of blocks) {
      const familyMatch = block.match(/font-family:\s*'([^']+)'/);
      const urlMatch = block.match(/url\((https?:\/\/[^)]+\.ttf[^)]*)\)/);

      if (familyMatch && urlMatch && !seenFamilies.has(familyMatch[1])) {
        seenFamilies.add(familyMatch[1]);
        fonts.push({ name: familyMatch[1], url: urlMatch[1] });
        if (verbose) console.log(`  Font gefunden: ${familyMatch[1]} → TTF`);
      }
    }
  }

  return fonts;
}

async function exportSlides(opts) {
  const inputPath = path.resolve(opts.input);
  if (!fs.existsSync(inputPath)) {
    console.error(`ERROR: Datei nicht gefunden: ${inputPath}`);
    process.exit(1);
  }

  const outputPath = opts.output
    ? path.resolve(opts.output)
    : inputPath.replace(/\.html$/i, ".pptx");

  if (opts.verbose) {
    console.log(`  Input:  ${inputPath}`);
    console.log(`  Output: ${outputPath}`);
  }

  const bundlePath = path.join(
    __dirname,
    "node_modules",
    "dom-to-pptx",
    "dist",
    "dom-to-pptx.bundle.js"
  );
  if (!fs.existsSync(bundlePath)) {
    console.error("ERROR: dom-to-pptx bundle nicht gefunden.");
    console.error("       npm install dom-to-pptx");
    process.exit(1);
  }
  const bundleCode = fs.readFileSync(bundlePath, "utf-8");

  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: SLIDE_WIDTH, height: SLIDE_HEIGHT },
  });

  // Read HTML and fix crossorigin on Google Fonts BEFORE loading.
  // Without crossorigin="anonymous", the browser blocks JS access to @font-face
  // rules in the stylesheet, preventing dom-to-pptx from detecting font URLs.
  let htmlContent = fs.readFileSync(inputPath, "utf-8");
  const hasFontLink = htmlContent.includes("fonts.googleapis.com");
  if (hasFontLink) {
    htmlContent = htmlContent.replace(
      /(<link\s+(?=[^>]*fonts\.googleapis\.com)[^>]*?)(\/?>)/gi,
      (match, before, closing) => {
        if (before.includes("crossorigin")) return match;
        return `${before} crossorigin="anonymous"${closing}`;
      }
    );
  }

  // Load modified HTML via data URL to preserve file:// context for relative paths
  const tmpHtml = path.join(path.dirname(inputPath), "._pptx_export_tmp.html");
  fs.writeFileSync(tmpHtml, htmlContent, "utf-8");

  const fileUrl = `file://${tmpHtml}`;
  if (opts.verbose) console.log(`  Lade:   ${fileUrl}`);

  // Forward browser console to Node.js (font detection / error debugging)
  page.on("console", (msg) => {
    const text = msg.text();
    if (
      opts.verbose &&
      (text.includes("font") ||
        text.includes("Font") ||
        text.includes("Auto-detected") ||
        text.includes("Failed") ||
        text.includes("warn") ||
        text.includes("embed"))
    ) {
      console.log(`  [browser] ${text}`);
    }
  });

  try {
    await page.goto(fileUrl, { waitUntil: "networkidle" });
  } finally {
    fs.unlinkSync(tmpHtml);
  }
  await page.waitForTimeout(2000);

  // Phase 1: Extract gradient info and prepare slides for export
  const slideBackgrounds = await page.evaluate(() => {
    const slides = document.querySelectorAll(".slide");
    const backgrounds = [];

    slides.forEach((s) => {
      s.style.transform = "none";

      const computed = window.getComputedStyle(s);
      const bgImage = computed.backgroundImage;
      const bgColor = computed.backgroundColor;

      if (bgImage && bgImage.includes("linear-gradient")) {
        backgrounds.push({
          type: "gradient",
          cssGradient: bgImage,
          cssBackgroundColor: bgColor,
        });
        // Replace gradient with the first gradient color as solid fallback
        const firstColor = bgImage.match(/#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)/);
        if (firstColor) {
          s.style.background = firstColor[0];
        } else {
          s.style.background = "transparent";
        }
      } else if (bgColor && bgColor !== "rgba(0, 0, 0, 0)" && bgColor !== "transparent") {
        backgrounds.push({ type: "solid", cssColor: bgColor });
      } else {
        backgrounds.push(null);
      }
    });

    // Add crossorigin to Google Fonts link for font embedding
    document.querySelectorAll('link[href*="fonts.googleapis.com"]').forEach((link) => {
      link.setAttribute("crossorigin", "anonymous");
    });

    const indicator = document.getElementById("slide-indicator");
    if (indicator) indicator.style.display = "none";

    // Fix footers: dom-to-pptx can't map flex justify-content:space-between.
    // Split each .slide-footer into two absolutely positioned elements so
    // the left text and page number become separate shapes in the PPTX.
    document.querySelectorAll(".slide-footer").forEach((footer) => {
      const spans = footer.querySelectorAll("span");
      if (spans.length < 2) return;

      const computed = window.getComputedStyle(footer);
      const rect = footer.getBoundingClientRect();
      const slideRect = footer.closest(".slide")?.getBoundingClientRect();
      if (!slideRect) return;

      const bottom = slideRect.bottom - rect.bottom;
      const left = rect.left - slideRect.left;
      const height = rect.height;
      const width = rect.width;
      const bg = computed.backgroundColor;
      const borderTop = computed.borderTop;
      const color = computed.color;
      const fontSize = computed.fontSize;
      const paddingLeft = computed.paddingLeft;
      const paddingRight = computed.paddingRight;

      // Replace flex container with absolute-positioned background + two text elements
      footer.style.display = "block";
      footer.style.position = "absolute";
      footer.style.bottom = "0";
      footer.style.left = "0";
      footer.style.right = "0";
      footer.style.height = height + "px";
      footer.style.padding = "0";

      footer.innerHTML = "";

      // Left-aligned text
      const leftSpan = document.createElement("div");
      leftSpan.textContent = spans[0].textContent;
      leftSpan.style.cssText = `
        position: absolute; left: ${paddingLeft}; top: 50%;
        transform: translateY(-50%);
        font-size: ${fontSize}; color: ${color};
      `;

      // Right-aligned page number
      const rightSpan = document.createElement("div");
      rightSpan.textContent = spans[1].textContent;
      rightSpan.style.cssText = `
        position: absolute; right: ${paddingRight}; top: 50%;
        transform: translateY(-50%);
        font-size: ${fontSize}; color: ${color};
        text-align: right;
      `;

      footer.appendChild(leftSpan);
      footer.appendChild(rightSpan);
    });

    return backgrounds;
  });

  const slideCount = slideBackgrounds.length;
  if (slideCount === 0) {
    console.error("ERROR: Keine .slide-Elemente gefunden");
    await browser.close();
    process.exit(1);
  }

  if (opts.verbose) console.log(`  Gefunden: ${slideCount} Slides`);

  // Parse gradient infos for post-processing
  const parsedBackgrounds = slideBackgrounds.map((bg) => {
    if (!bg) return null;
    if (bg.type === "gradient") {
      const gradient = parseLinearGradient(bg.cssGradient);
      return gradient ? { type: "gradient", gradient } : null;
    }
    if (bg.type === "solid") {
      const match = bg.cssColor.match(/\d+/g);
      if (match && match.length >= 3) {
        const hex = match
          .slice(0, 3)
          .map((c) => parseInt(c).toString(16).padStart(2, "0"))
          .join("")
          .toUpperCase();
        return { type: "solid", color: hex };
      }
    }
    return null;
  });

  const gradientCount = parsedBackgrounds.filter(
    (b) => b && b.type === "gradient"
  ).length;
  if (opts.verbose && gradientCount > 0) {
    console.log(`  ${gradientCount} Gradient-Backgrounds → native PowerPoint-Fills`);
  }

  // Phase 2: Resolve font URLs (TTF format for embedding)
  // dom-to-pptx can't handle woff2 (bug: treats all non-woff/otf as ttf).
  // We fetch the Google Fonts CSS with a TTF-serving user-agent from Node.js
  // and pass the TTF URLs manually.
  const fontConfigs = await resolveFontUrls(page, opts.verbose);

  // Phase 3: Inject dom-to-pptx and export
  await page.addScriptTag({ content: bundleCode });
  await page.waitForTimeout(500);

  if (opts.verbose) console.log("  dom-to-pptx injiziert, starte Export...");

  const exportOpts = { svgAsVector: opts.svgAsVector, fonts: fontConfigs };
  const base64 = await page.evaluate(async (opts) => {
    const slides = Array.from(document.querySelectorAll(".slide"));

    slides.forEach((s) => {
      s.style.transform = "none";
      s.style.width = "1920px";
      s.style.height = "1080px";
    });

    const blob = await window.domToPptx.exportToPptx(slides, {
      fileName: "export.pptx",
      skipDownload: true,
      svgAsVector: opts.svgAsVector,
      autoEmbedFonts: false,
      fonts: opts.fonts,
    });

    const arrayBuffer = await blob.arrayBuffer();
    const bytes = new Uint8Array(arrayBuffer);
    let binary = "";
    for (let i = 0; i < bytes.length; i++) {
      binary += String.fromCharCode(bytes[i]);
    }
    return btoa(binary);
  }, exportOpts);

  await browser.close();

  // Phase 3: Post-process PPTX
  let buffer = Buffer.from(base64, "base64");

  if (gradientCount > 0) {
    if (opts.verbose) console.log("  Post-Processing: Native Backgrounds einsetzen...");
    buffer = await patchPptxBackgrounds(buffer, parsedBackgrounds, opts.verbose);
  }

  buffer = await cleanupPptxPackage(buffer, opts.verbose);

  fs.writeFileSync(outputPath, buffer);

  const fileSizeMB = (buffer.length / (1024 * 1024)).toFixed(1);
  console.log(`PPTX exportiert: ${outputPath}`);
  console.log(`  ${slideCount} Slides, ${fileSizeMB} MB`);

  return outputPath;
}

async function main() {
  const opts = parseArgs();
  console.log(`Exportiere PPTX: ${opts.input}`);

  try {
    await exportSlides(opts);
  } catch (err) {
    console.error(`ERROR: Export fehlgeschlagen: ${err.message}`);
    if (opts.verbose) console.error(err.stack);
    process.exit(1);
  }
}

main();
