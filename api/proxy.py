from fastapi import FastAPI, Request, HTTPException
import httpx
import os

app = FastAPI()

# Password stored in environment variable
PASSWORD = os.getenv("PROXY_PASSWORD", "defaultpassword")

@app.middleware("http")
async def password_protect(request: Request, call_next):
    """
    Middleware to enforce password protection.
    The client must provide the correct password in the Authorization header.
    """
    auth = request.headers.get("Authorization")
    if not auth or auth != f"Bearer {PASSWORD}":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await call_next(request)

@app.post("/proxy")
async def proxy(request: Request):
    """
    Proxy endpoint to forward requests to a target URL.
    The target URL is specified in the `X-Target-URL` header.
    """
    target_url = request.headers.get("X-Target-URL")
    if not target_url:
        raise HTTPException(status_code=400, detail="Target URL missing in headers.")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=request.method,
                url=target_url,
                headers=request.headers,
                content=await request.body(),
                timeout=10.0
            )
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
