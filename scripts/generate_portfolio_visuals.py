"""Generate the approved portfolio thumbnails and architecture infographics.

Outputs are deterministic 1200x675 PNG covers plus accessible SVG diagrams. The
visuals intentionally use abstract technical shapes rather than logos or UI mockups.
"""
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1] / "static" / "postImg"


def first_existing_font(*candidates):
    for candidate in candidates:
        if Path(candidate).is_file():
            return candidate
    raise FileNotFoundError(f"No supported portfolio font found: {candidates}")


FONT = first_existing_font(
    "C:/Windows/Fonts/arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
)
FONT_BOLD = first_existing_font(
    "C:/Windows/Fonts/arialbd.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
)

PROJECTS = [
    ("job_advantech", "ENGINEERING\nPORTFOLIO", "THERMAL  •  AUTOMATION  •  QUALITY", "#14b8a6", "engineering-portfolio-map.svg",
     ["SERVER SYSTEMS", "AUTOMATION", "QUALITY ENGINEERING"], ["Thermal control", "Stress & telemetry", "Evidence-gated QA"]),
    ("job_sentos", "SIGNAL TO\nFIRMWARE", "DSP  •  CALIBRATION  •  PRODUCT SUPPORT", "#8b5cf6", "signal-to-firmware-flow.svg",
     ["SIGNAL", "ANALYZE", "FIRMWARE"], ["Ultrasound waveform", "MATLAB / WPF", "C++ implementation"]),
    ("lightnews", "LOCAL-LLM\nEDITORIAL FLOW", "INGEST  •  TRANSFORM  •  REVIEW", "#f59e0b", "editorial-pipeline-v2.svg",
     ["EXTERNAL", "PRIVATE HOST", "CMS"], ["RSS / Web / Unsplash", "n8n + Ollama", "Draft → review"]),
    ("ice_algo", "THERMAL\nCONTROL LOOP", "PROFILE  •  DERIVE  •  CONTROL", "#06b6d4", "thermal-control-loop.svg",
     ["PROFILE", "DERIVE", "RUNTIME"], ["Load / fan / dT/dt≈0", "Kp → Ki, Kd", "BMC PID + reset"]),
    ("rack_monitor", "RACK\nOBSERVABILITY", "COLLECT  •  NORMALIZE  •  OBSERVE", "#22c55e", "observability-pipeline-v2.svg",
     ["DEVICES", "METRICS", "OBSERVE"], ["IPMI / SNMP", "Golang → Prometheus", "Grafana / alerts"]),
    ("Redmine-Tracker", "PLAN • TRACK\n• LOG", "DESKTOP PRODUCTIVITY WORKFLOW", "#f97316", "plan-track-log-flow.svg",
     ["PLAN", "TRACK", "LOG"], ["Profiles / planner", "Calendar / review", "Redmine REST API"]),
    ("smartfan", "PREDICT • CONTROL\n• ANALYZE", "TARGET-POWER STRESS TESTING", "#3b82f6", "predict-control-analyze-loop.svg",
     ["MODEL", "CONTROL", "ANALYZE"], ["Component response", "Target → workload mix", "Telemetry → Grafana"]),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def generate_thumbnail(folder, title, subtitle, accent):
    w, h = 1200, 675
    im = Image.new("RGB", (w, h), "#071827")
    d = ImageDraw.Draw(im)
    # deterministic technical grid
    for x in range(0, w, 75):
        d.line((x, 0, x, h), fill="#0d2b3b", width=1)
    for y in range(0, h, 75):
        d.line((0, y, w, y), fill="#0d2b3b", width=1)
    d.rounded_rectangle((54, 50, 1146, 625), radius=28, fill="#0b2233", outline="#1d4960", width=2)
    d.rectangle((54, 50, 70, 625), fill=accent)
    # abstract connected system symbol
    pts = [(855, 205), (1055, 160), (1115, 340), (955, 470), (795, 370)]
    for a, b in zip(pts, pts[1:] + pts[:1]):
        d.line((*a, *b), fill="#23617a", width=5)
    for i, (x, y) in enumerate(pts):
        r = 30 if i == 0 else 22
        d.ellipse((x-r, y-r, x+r, y+r), fill=accent if i == 0 else "#0f3448", outline="#8ddce6", width=3)
    d.line((825, 337, 1075, 337), fill=accent, width=8)
    d.ellipse((930, 321, 962, 353), fill="#dffcff")
    title_lines = title.split("\n")
    title_size = 70
    while title_size > 54:
        title_font = font(FONT_BOLD, title_size)
        if max(d.textlength(line, font=title_font) for line in title_lines) <= 650:
            break
        title_size -= 2
    y = 155
    for line in title_lines:
        d.text((125, y), line, font=title_font, fill="#f1fbff")
        y += title_size + 12
    d.text((128, 420), subtitle, font=font(FONT_BOLD, 21), fill=accent)
    d.text((128, 535), "TECHNICAL CASE STUDY", font=font(FONT, 18), fill="#8eb4c5")
    out = ROOT / folder / "thumbnail-v2.png"
    im.save(out, format="PNG", optimize=False, compress_level=9)


def generate_svg(folder, filename, title, accent, stages, details):
    cards = []
    arrows = []
    xs = [70, 425, 780]
    for i, (x, stage, detail) in enumerate(zip(xs, stages, details)):
        cards.append(f'''<g transform="translate({x} 185)">
  <rect width="300" height="190" rx="22" fill="#ffffff" stroke="{accent}" stroke-width="3"/>
  <circle cx="45" cy="45" r="22" fill="{accent}"/><text x="45" y="52" class="num" text-anchor="middle">{i+1}</text>
  <text x="150" y="92" class="label" text-anchor="middle">{escape(stage)}</text>
  <text x="150" y="128" class="detail" text-anchor="middle">{escape(detail)}</text>
</g>''')
        if i < 2:
            arrows.append(f'<path d="M {x+305} 280 H {xs[i+1]-10}" class="arrow"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="560" viewBox="0 0 1200 560" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)} workflow</title>
<desc id="desc">Three-stage technical architecture showing {escape(details[0])}, then {escape(details[1])}, then {escape(details[2])}.</desc>
<defs><marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="{accent}"/></marker>
<style>.heading{{font:700 32px Arial,sans-serif;fill:#e9f7fb}}.sub{{font:400 15px Arial,sans-serif;fill:#9fc1ce}}.label{{font:700 20px Arial,sans-serif;fill:#102b3a}}.detail{{font:400 15px Arial,sans-serif;fill:#496574}}.num{{font:700 17px Arial,sans-serif;fill:#fff}}.arrow{{stroke:{accent};stroke-width:4;fill:none;marker-end:url(#arrowhead)}}</style></defs>
<rect width="1200" height="560" fill="#071827"/><rect x="35" y="35" width="1130" height="490" rx="28" fill="#0b2233" stroke="#1d4960"/>
<text x="600" y="93" class="heading" text-anchor="middle">{escape(title)}</text><text x="600" y="125" class="sub" text-anchor="middle">EVIDENCE-CALIBRATED PORTFOLIO ARCHITECTURE</text>
{''.join(arrows)}{''.join(cards)}
<text x="600" y="465" class="sub" text-anchor="middle">Boundaries and labels reflect the publicly described project scope.</text>
</svg>'''
    (ROOT / folder / filename).write_text(svg, encoding="utf-8", newline="\n")


for folder, cover_title, subtitle, accent, svg_name, stages, details in PROJECTS:
    generate_thumbnail(folder, cover_title, subtitle, accent)
    generate_svg(folder, svg_name, cover_title.replace("\n", " ").replace(" • ", " / "), accent, stages, details)
