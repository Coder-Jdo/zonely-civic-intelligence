"""
Zonely PDF Report Generator
Uses Playwright to produce a high-fidelity PDF directly from the HTML report.
"""

import asyncio
from playwright.sync_api import sync_playwright

async def generate_report_pdf(url: str) -> bytes:
    def _render() -> bytes:
        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--no-sandbox", "--disable-setuid-sandbox"])
            context = browser.new_context(
                viewport={"width": 1200, "height": 800},
                device_scale_factor=2,
            )
            page = context.new_page()
            page.goto(url, wait_until="networkidle")
            page.wait_for_timeout(2000)
            pdf_bytes = page.pdf(
                format="A4",
                print_background=True,
                margin={
                    "top": "20px",
                    "right": "20px",
                    "bottom": "20px",
                    "left": "20px",
                },
            )
            browser.close()
            return pdf_bytes

    # Use a thread so this works on Windows loops that don't support subprocesses,
    # and to avoid blocking the server event loop during PDF rendering.
    return await asyncio.to_thread(_render)
