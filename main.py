from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI()

TARGET_URL = "https://ljg.d72577a9dd0ec38.sbs"
REFERER = "https://inattv1278.xyz"

@app.get("/stream")
async def proxy_stream():
    headers = {
        "Referer": REFERER,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"
    }
    
    async with httpx.AsyncClient(follow_redirects=True) as client:
        # Hedef stream linkine referer ile istek atıyoruz
        resp = await client.get(TARGET_URL, headers=headers)
        
        # İçeriği (m3u8 veya ts fark etmez) tarayıcıya/oynatıcıya iletiyoruz
        return Response(
            content=resp.content, 
            status_code=resp.status_code, 
            media_type=resp.headers.get("content-type")
        )

# Pigi projesinin kendi route'larını buraya bağlayabilirsin
# from run import main_app
# app.mount("/pigi", main_app)
