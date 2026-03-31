"""
Zonely PDF Report Generator
Uses Playwright to produce a high-fidelity PDF directly from the HTML report.
"""

import asyncio

async def generate_report_pdf(url: str) -> bytes:
    def _render() -> bytes:
        # Import inside the worker thread so Playwright's sync API is initialized
        # in the same thread that drives the browser.
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(args=["--no-sandbox", "--disable-setuid-sandbox"])
            context = browser.new_context(
                viewport={"width": 1200, "height": 800},
                device_scale_factor=2,
            )
            try:
                page = context.new_page()
                page.set_default_timeout(120_000)
                page.set_default_navigation_timeout(120_000)

                # "networkidle" can hang on pages with long-polling/analytics.
                # Prefer "domcontentloaded" for reliability.
                page.goto(url, wait_until="domcontentloaded")
                page.wait_for_selector("body")
                page.wait_for_timeout(1500)

                return page.pdf(
                    format="A4",
                    print_background=True,
                    margin={
                        "top": "20px",
                        "right": "20px",
                        "bottom": "20px",
                        "left": "20px",
                    },
                )
            finally:
                context.close()
                browser.close()

    # Run sync Playwright in a worker thread to avoid relying on asyncio subprocess
    # support (which can vary by event loop policy on Windows).
    return await asyncio.to_thread(_render)
