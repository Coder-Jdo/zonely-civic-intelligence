"""
Zonely PDF Report Generator
Uses reportlab to produce a bureau-style PDF for a given postcode.
"""

import io
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.graphics.shapes import Drawing, Rect, String, Circle
from reportlab.graphics import renderPDF

# ── Colour palette ─────────────────────────────────────────────────────────────
BRAND      = colors.HexColor("#0F3D57")
BRAND_LIGHT= colors.HexColor("#EAF6FF")
BRAND_MID  = colors.HexColor("#1e5f82")
SLATE_400  = colors.HexColor("#94a3b8")
SLATE_500  = colors.HexColor("#64748b")
SLATE_700  = colors.HexColor("#334155")
WHITE      = colors.white
BG         = colors.HexColor("#F7FBFF")
TAG_COLORS = {
    "planning":       (colors.HexColor("#dbeafe"), colors.HexColor("#1d4ed8")),
    "infrastructure": (colors.HexColor("#d1fae5"), colors.HexColor("#065f46")),
    "crisis":         (colors.HexColor("#fee2e2"), colors.HexColor("#991b1b")),
    "market":         (colors.HexColor("#fef3c7"), colors.HexColor("#92400e")),
}

# ── Styles ─────────────────────────────────────────────────────────────────────
def make_styles():
    return {
        "title":       ParagraphStyle("title",       fontName="Helvetica-Bold",   fontSize=22, textColor=BRAND,     leading=28, spaceAfter=4),
        "subtitle":    ParagraphStyle("subtitle",    fontName="Helvetica",         fontSize=11, textColor=SLATE_500, leading=16, spaceAfter=2),
        "label":       ParagraphStyle("label",       fontName="Helvetica-Bold",   fontSize=7,  textColor=SLATE_400, leading=10, spaceAfter=2, wordWrap='LTR'),
        "section":     ParagraphStyle("section",     fontName="Helvetica-Bold",   fontSize=13, textColor=BRAND,     leading=18, spaceBefore=14, spaceAfter=6),
        "body":        ParagraphStyle("body",        fontName="Helvetica",         fontSize=9,  textColor=SLATE_700, leading=14, spaceAfter=4),
        "small":       ParagraphStyle("small",       fontName="Helvetica",         fontSize=8,  textColor=SLATE_400, leading=12),
        "score_big":   ParagraphStyle("score_big",   fontName="Helvetica-Bold",   fontSize=36, textColor=BRAND,     leading=40),
        "mono":        ParagraphStyle("mono",        fontName="Courier-Bold",      fontSize=7,  textColor=SLATE_400, leading=10),
        "bold":        ParagraphStyle("bold",        fontName="Helvetica-Bold",   fontSize=9,  textColor=BRAND,     leading=13),
        "center":      ParagraphStyle("center",      fontName="Helvetica",         fontSize=9,  textColor=SLATE_500, leading=14, alignment=TA_CENTER),
        "footer":      ParagraphStyle("footer",      fontName="Helvetica",         fontSize=7,  textColor=SLATE_400, leading=10, alignment=TA_CENTER),
    }

W, H = A4
MARGIN = 18 * mm
INNER_W = W - 2 * MARGIN


# ── Helper: horizontal bar ─────────────────────────────────────────────────────
def bar_drawing(value: int, width: float = INNER_W - 60, height: float = 8) -> Drawing:
    d = Drawing(width, height)
    d.add(Rect(0, 0, width, height, rx=4, ry=4, fillColor=BRAND_LIGHT, strokeColor=None))
    fill_w = max(4, width * value / 200)
    d.add(Rect(0, 0, fill_w, height, rx=4, ry=4, fillColor=BRAND, strokeColor=None))
    return d


# ── Helper: info stat box row ──────────────────────────────────────────────────
def stat_row(items: list[tuple[str, str]], styles) -> Table:
    """items = list of (label, value)"""
    cell_data = [[
        [Paragraph(lbl.upper(), styles["mono"]), Paragraph(val, styles["bold"])]
        for lbl, val in items
    ]]
    col_w = INNER_W / len(items)
    t = Table(cell_data, colWidths=[col_w] * len(items), rowHeights=[32])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BRAND_LIGHT),
        ("ROUNDEDCORNERS", [6]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING",  (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        ("LINEAFTER", (0, 0), (-2, -1), 0.5, colors.HexColor("#d1dde8")),
    ]))
    return t


# ── Main generator ─────────────────────────────────────────────────────────────
def generate_report_pdf(code: str, data: dict) -> bytes:
    buf = io.BytesIO()
    styles = make_styles()

    doc = SimpleDocTemplate(
        buf,
        pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN,  bottomMargin=MARGIN,
        title=f"Zonely Report — {code}",
        author="Zonely Civic Intelligence",
    )

    story = []

    # ── Cover / Header block ───────────────────────────────────────────────────
    header_data = [[
        # Left: branding + postcode
        [
            Paragraph("▲  ZONELY CIVIC INTELLIGENCE REPORT", styles["mono"]),
            Spacer(1, 4),
            Paragraph(data["area"], styles["title"]),
            Paragraph(code, styles["mono"]),
            Spacer(1, 6),
            Paragraph(data["headlineSummary"], styles["body"]),
        ],
        # Right: big score
        [
            Paragraph("CIVIC SCORE", styles["mono"]),
            Paragraph(str(data["civicScore"]), styles["score_big"]),
            Paragraph("/ 1000", styles["subtitle"]),
            Spacer(1, 4),
            Paragraph(f"Confidence band: ± {data['confidenceBand']}", styles["small"]),
            Paragraph(f"Direction: {data['directionSymbol']} {data['direction']}", styles["small"]),
            Paragraph(data["impactLabel"], styles["label"]),
        ],
    ]]
    header_table = Table(header_data, colWidths=[INNER_W * 0.62, INNER_W * 0.38])
    header_table.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, -1), BRAND_LIGHT),
        ("ROUNDEDCORNERS", [8]),
        ("VALIGN",       (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING",  (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING",   (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 14),
        ("LINEAFTER",    (0, 0), (0, -1),  0.5, colors.HexColor("#d1dde8")),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 14))

    # ── Civic Signals ──────────────────────────────────────────────────────────
    story.append(Paragraph("Civic Signals", styles["section"]))
    sig = data["signals"]
    story.append(stat_row([
        ("Active Applications", str(sig["activeApplications"])),
        ("Units Pipeline",      f"{sig['unitsPipeline']:,}"),
        ("In Consultation",     str(sig["inConsultation"])),
        ("Approval Rate",       f"{sig['approvalRate']}%"),
        ("Submitted Pending",   str(sig["submittedPending"])),
    ], styles))
    story.append(Spacer(1, 14))

    # ── Score Breakdown ────────────────────────────────────────────────────────
    story.append(Paragraph("Score Breakdown", styles["section"]))
    for cat, item in data["breakdown"].items():
        row = [[
            Paragraph(cat, styles["bold"]),
            Paragraph(item["trend"], styles["small"]),
            Paragraph(f"{item['score']}/200", styles["bold"]),
        ]]
        t = Table(row, colWidths=[INNER_W * 0.52, INNER_W * 0.28, INNER_W * 0.2])
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN",  (2, 0), (2, 0),   "RIGHT"),
            ("LEFTPADDING",  (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING",   (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING",(0, 0), (-1, -1), 4),
        ]))
        story.append(KeepTogether([
            t,
            bar_drawing(item["score"]),
            Spacer(1, 2),
            Paragraph(item["note"], styles["small"]),
            Spacer(1, 8),
        ]))
    story.append(Spacer(1, 6))

# ── Planning Momentum ──────────────────────────────────────────────────────
    pm = data["planningMomentum"]
    ttv = data["timeToValue"]

    story.append(Paragraph("Planning Momentum", styles["section"]))
    story.append(stat_row([
        ("Score",         str(pm["score"])),
        ("Direction",     pm["direction"]),
        ("Approval Range", f"{pm['approvalRangeLow']}–{pm['approvalRangeHigh']}%"),
    ], styles))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Development Factors", styles["label"]))
    story.append(Spacer(1, 4))
    story.append(Paragraph(f"Scale: {ttv['factors']['developmentScale']}", styles["body"]))
    story.append(Paragraph(f"Heights: {ttv['factors']['buildingHeights']}", styles["body"]))
    story.append(Paragraph(f"Approval: {ttv['factors']['approvalLikelihood']}", styles["body"]))
    story.append(Spacer(1, 14))

    # ── Time to Value ──────────────────────────────────────────────────────────
    story.append(Paragraph("Time to Value", styles["section"]))
    story.append(Paragraph(f"{ttv['phase']}  ({ttv['phaseRange']})", styles["bold"]))
    story.append(Spacer(1, 4))
    story.append(Paragraph(ttv["timeline"], styles["mono"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph("What to Expect", styles["label"]))
    story.append(Spacer(1, 3))
    for x in ttv["whatToExpect"]:
        story.append(Paragraph(f"▲  {x}", styles["body"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Risk Flags", styles["label"]))
    story.append(Spacer(1, 3))
    for x in ttv["riskFlags"]:
        story.append(Paragraph(f"!  {x}", styles["body"]))
    story.append(Spacer(1, 14))

    # ── Civic Credit History ───────────────────────────────────────────────────
    ch = data["creditHistory"]
    story.append(Paragraph("Planning and Development History", styles["section"]))
    story.append(stat_row([
        ("Volatility Index", str(ch["volatilityIndex"])),
        ("Recovery Speed",   str(ch["recoverySpeed"])),
        ("10-Year Trend",    str(ch["tenYearTrend"])),
    ], styles))
    story.append(Spacer(1, 10))

    for event in ch["events"]:
        tag = event["tag"].lower()
        tag_bg, tag_fg = TAG_COLORS.get(tag, (BRAND_LIGHT, BRAND))
        tag_cell = Paragraph(event["tag"], ParagraphStyle(
            "tag", fontName="Helvetica-Bold", fontSize=7,
            textColor=tag_fg, leading=10
        ))
        row = [[
            Paragraph(str(event["year"]), styles["bold"]),
            tag_cell,
            [Paragraph(event["title"], styles["bold"]),
             Paragraph(event["note"],  styles["small"])],
        ]]
        t = Table(row, colWidths=[30, 65, INNER_W - 95])
        t.setStyle(TableStyle([
            ("BACKGROUND", (1, 0), (1, 0), tag_bg),
            ("ROUNDEDCORNERS", [4]),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING",  (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING",   (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING",(0, 0), (-1, -1), 3),
        ]))
        story.append(t)
        story.append(Spacer(1, 6))

# ── Score Category Descriptions ───────────────────────────────────────────
    story.append(Paragraph("Score Category Descriptions", styles["section"]))
    story.append(Spacer(1, 6))

    categories = [
        ("1. Growth & Investment Potential",
         "Forecasts future property price growth and rental yield trends by analysing historical price data, housing demand, and economic activity to identify areas likely to appreciate in value."),
        ("2. Planning & Development Momentum",
         "Tracks approved developments, regeneration projects, and planning applications to identify neighbourhoods where upcoming construction and investment could drive future demand."),
        ("3. Infrastructure & Connectivity",
         "Evaluates transport links, accessibility, and upcoming infrastructure projects that improve connectivity and increase the attractiveness of an area."),
        ("4. Safety & Community Stability",
         "Analyses crime rates and safety trends to assess the stability and long-term desirability of a neighbourhood."),
        ("5. Liveability & Social Infrastructure",
         "Measures quality of life factors such as schools, healthcare, green spaces, amenities, and walkability that influence where people choose to live."),
    ]

    for title, desc in categories:
        story.append(KeepTogether([
            Paragraph(title, styles["bold"]),
            Spacer(1, 3),
            Paragraph(desc, styles["body"]),
            Spacer(1, 10),
        ]))

    story.append(Spacer(1, 6))

    # ── Footer ─────────────────────────────────────────────────────────────────
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width=INNER_W, thickness=0.5, color=SLATE_400))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Zonely Civic Intelligence  ·  Leeds Pilot  ·  Not financial advice. Use alongside professional review.",
        styles["footer"]
    ))

    doc.build(story)
    return buf.getvalue()
