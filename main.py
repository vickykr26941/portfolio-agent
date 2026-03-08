import os
from dotenv import load_dotenv
load_dotenv()  # Must be first — loads .env before anything reads env vars

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
from agent import run_agent, warm_github_cache

app = FastAPI(title="Vicky Kumar Portfolio Agent", version="1.0.0")

# ── Models ─────────────────────────────────────────────────────────────────────

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Message]] = []

class ChatResponse(BaseModel):
    reply: str

# ── Startup ────────────────────────────────────────────────────────────────────

@app.on_event("startup")
async def startup():
    # Validate Cloudflare env vars
    cf_token    = os.getenv("CLOUDFLARE_API_TOKEN", "")
    cf_account  = os.getenv("CLOUDFLARE_ACCOUNT_ID", "")
    github_token = os.getenv("GITHUB_TOKEN", "")

    print("─── VickyBot Startup ───────────────────────")
    
    if not cf_token:
        print("❌ CLOUDFLARE_API_TOKEN is not set!")
    else:
        print(f"✅ CLOUDFLARE_API_TOKEN loaded: {cf_token[:8]}...")

    if not cf_account:
        print("❌ CLOUDFLARE_ACCOUNT_ID is not set!")
    else:
        print(f"✅ CLOUDFLARE_ACCOUNT_ID loaded: {cf_account[:8]}...")

    if not github_token:
        print("⚠️  GITHUB_TOKEN not set — GitHub features will use unauthenticated API (rate limited)")
    else:
        print(f"✅ GITHUB_TOKEN loaded: {github_token[:8]}...")

    print("────────────────────────────────────────────")

    # Pre-fetch GitHub data once at startup — cached for all requests
    await warm_github_cache()

# ── Routes ─────────────────────────────────────────────────────────────────────

@app.get("/api/health")
async def health():
    return {"status": "ok", "agent": "VickyBot", "version": "1.0.0"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    try:
        history = [{"role": m.role, "content": m.content} for m in (req.history or [])]
        reply = await run_agent(req.message, history)
        return ChatResponse(reply=reply)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {str(e)}")

# ── Static ─────────────────────────────────────────────────────────────────────

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_ui():
    return FileResponse("static/index.html")

@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    return FileResponse("static/index.html")

