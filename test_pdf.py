import asyncio
import httpx
import sys

async def test_download():
    # Give the server a moment to start up
    await asyncio.sleep(2)
    pdf_filename = 'test_download.pdf'
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        print("Requesting PDF for LS1 1BA...")
        response = await client.get('http://IP_PLACEHOLDER/download/LS1%201BA')
        if response.status_code == 200:
            with open(pdf_filename, 'wb') as f:
                f.write(response.content)
            print("Successfully downloaded PDF to", pdf_filename)
            sys.exit(0)
        else:
            print("Failed to download PDF. Status Code:", response.status_code)
            print("Response:", response.text)
            sys.exit(1)

if __name__ == "__main__":
    asyncio.run(test_download())
