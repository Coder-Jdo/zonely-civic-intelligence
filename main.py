import sys
import asyncio

# Playwright needs an asyncio event loop that supports subprocesses on Windows.
if sys.platform.startswith("win"):
    _policy = getattr(asyncio, "WindowsProactorEventLoopPolicy", None)
    if _policy is not None:
        asyncio.set_event_loop_policy(_policy())

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from data import ZONELY_DEMO_DATA, normalize_postcode, is_valid_postcode
from pdf_generator import generate_report_pdf
import io

from fastapi.staticfiles import StaticFiles
app = FastAPI(title="Zonely Civic Intelligence")
app.mount("/static", StaticFiles(directory="static"), name="static")
import os
template_dir = "Templates" if os.path.exists("Templates") else "templates"
templates = Jinja2Templates(directory=template_dir)

# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    demo_postcodes = ["LS1 1BA", "LS3 1AA", "LS6 3BN"]
    bureau_bars = [
        {"label": "Crime",       "value": 42},
        {"label": "Planning",    "value": 76},
        {"label": "scoreInfra",  "value": 64},
        {"label": "Education",   "value": 58},
        {"label": "Liveability", "value": 70},
    ]
    demo_data = {pc: ZONELY_DEMO_DATA[pc] for pc in demo_postcodes}
    return templates.TemplateResponse(request=request, name="index.html", context={
        "request": request,
        "demo_postcodes": demo_postcodes,
        "bureau_bars": bureau_bars,
        "demo_data": demo_data,
    })


@app.get("/postcode", response_class=HTMLResponse)
async def postcode_report(request: Request, code: str = ""):
    normalized = normalize_postcode(code)
    if not is_valid_postcode(normalized):
        return templates.TemplateResponse(request=request, name="not_found.html", context={
            "request": request,
            "code": normalized,
        }, status_code=404)
    data = ZONELY_DEMO_DATA[normalized]
    return templates.TemplateResponse(request=request, name="postcode.html", context={
        "request": request,
        "code": normalized,
        "data": data,
    })


# ── API endpoints ─────────────────────────────────────────────────────────────

@app.get("/api/ping")
async def ping():
    return {"message": "pong"}

@app.get("/api/postcode/{code}")
async def api_postcode(code: str):
    normalized = normalize_postcode(code)
    if not is_valid_postcode(normalized):
        raise HTTPException(status_code=404, detail=f"Postcode '{normalized}' not found in demo data.")
    return ZONELY_DEMO_DATA[normalized]

@app.get("/api/postcodes")
async def api_postcodes():
    return {"postcodes": list(ZONELY_DEMO_DATA.keys())}


@app.get("/download/{code}")
async def download_report(request: Request, code: str):
    normalized = normalize_postcode(code)
    if not is_valid_postcode(normalized):
        raise HTTPException(status_code=404, detail=f"Postcode '{normalized}' not found.")

    # Construct the full URL to the report page for this postcode
    target_url = str(request.url_for('postcode_report')) + f"?code={normalized}"

    pdf_bytes = await generate_report_pdf(target_url)
    filename = f"Zonely-Report-{normalized.replace(' ', '_')}.pdf"

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'}
    )
@app.get("/compare", response_class=HTMLResponse)
async def compare(request: Request, codes: str = ""):
    results = []
    errors = []
    if codes:
        for raw in codes.split(","):
            normalized = normalize_postcode(raw.strip())
            if is_valid_postcode(normalized):
                results.append({"code": normalized, "data": ZONELY_DEMO_DATA[normalized]})
            else:
                errors.append(normalized)
    return templates.TemplateResponse(request=request, name="compare.html", context={
        "request": request,
        "results": results,
        "errors": errors,
        "codes_input": codes,
    })
@app.get("/vision", response_class=HTMLResponse)
async def vision(request: Request):
    return templates.TemplateResponse(request=request, name="vision.html", context={"request": request})
@app.get("/documentation", response_class=HTMLResponse)
async def documentation(request: Request):
    return templates.TemplateResponse(request=request, name="documentation.html", context={"request": request})

@app.get("/admin", response_class=HTMLResponse)
async def admin_login(request: Request, error: str = ""):
    return templates.TemplateResponse(request=request, name="admin.html", context={"request": request, "error": error})

@app.post("/admin", response_class=HTMLResponse)
async def admin_login_post(request: Request):
    from fastapi.responses import RedirectResponse
    form = await request.form()
    username = form.get("username", "")
    password = form.get("password", "")
    if username == "admin" and password == "zonely2024":
        return RedirectResponse(url="/admin/dashboard", status_code=302)
    return templates.TemplateResponse(request=request, name="admin.html", context={"request": request, "error": "Invalid username or password."})

@app.get("/admin/dashboard", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    stats = {
        "total_postcodes": len(ZONELY_DEMO_DATA),
        "total_reports": 3,
        "avg_score": round(sum(d["civicScore"] for d in ZONELY_DEMO_DATA.values()) / len(ZONELY_DEMO_DATA)),
        "high_impact": sum(1 for d in ZONELY_DEMO_DATA.values() if d["impactLevel"] == "high"),
    }
    return templates.TemplateResponse(request=request, name="admin_dashboard.html", context={
        "request": request,
        "stats": stats,
        "postcodes": ZONELY_DEMO_DATA,
    })