"""
Zonely PDF Report Generator — WeasyPrint (no browser needed)
"""
import httpx
from weasyprint import HTML

async def generate_report_pdf(url: str) -> bytes:
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=60)
        html_content = response.text

    pdf_bytes = HTML(string=html_content, base_url=url).write_pdf()
    return pdf_bytes