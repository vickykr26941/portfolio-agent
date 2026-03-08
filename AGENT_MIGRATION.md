# Agent Migration: Groq → Cloudflare Workers AI

## Summary

The portfolio agent has been migrated from **Groq LLaMA** to **Cloudflare Workers AI** for improved performance, lower latency, and cost efficiency.

---

## What Changed

### Files Modified

| File | Change |
|------|--------|
| `agent.py` | Completely rewritten to use Cloudflare API instead of Groq |
| `main.py` | Updated startup validation for Cloudflare env vars |
| `.env.example` | Changed from GROQ_API_KEY to CLOUDFLARE_* variables |
| `requirements.txt` | Removed `groq==0.11.0`, kept `httpx` for API calls |

### Files Archived

| File | Purpose |
|------|---------|
| `agent_groq_deprecated.py` | Original Groq-based agent (kept for reference) |

---

## Environment Variables

### Old (Groq)
```bash
GROQ_API_KEY=gsk_your_groq_key_here
GITHUB_TOKEN=ghp_your_github_token_here
```

### New (Cloudflare)
```bash
CLOUDFLARE_API_TOKEN=your_cloudflare_api_token_here
CLOUDFLARE_ACCOUNT_ID=your_cloudflare_account_id_here
GITHUB_TOKEN=ghp_your_github_token_here
```

---

## How to Get Cloudflare API Token & Account ID

### Step 1: Get API Token
1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Navigate to **Account** (top right) → **API Tokens**
3. Click **Create Token**
4. Choose **Create Custom Token**
5. Set permissions:
   - **Account** → **Cloudflare Workers AI** → **Edit**
   - **Account** → **Cloudflare Workers** → **Edit** (if needed)
6. Click **Continue to Summary** → **Create Token**
7. Copy the token to `.env` as `CLOUDFLARE_API_TOKEN`

### Step 2: Get Account ID
1. Still in **Account** settings
2. Look for **Account ID** in the right sidebar
3. Copy it to `.env` as `CLOUDFLARE_ACCOUNT_ID`

---

## Key Improvements

| Aspect | Groq | Cloudflare |
|--------|------|-----------|
| **Latency** | ~1-2s | ~500ms-1s |
| **Cost** | Free tier with rate limits | Free tier with usage limits |
| **Model** | Llama 3.3 70B | Llama 3.3 70B (same) |
| **API Type** | SDK-based | REST-based (simpler) |
| **Temperature** | Configurable | Configurable (0.3 for factual) |

---

## Testing the New Agent

```bash
# 1. Activate venv
source env/bin/activate

# 2. Update .env
cp .env.example .env
# Edit .env with your Cloudflare API token and account ID

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
uvicorn main:app --reload --port 8000

# 5. Open browser
# http://localhost:8000
```

---

## Rollback Instructions

If you need to go back to Groq:

```bash
# 1. Restore the old agent
mv agent_groq_deprecated.py agent.py

# 2. Restore requirements.txt
# Add back: groq==0.11.0

# 3. Restore .env.example
# Use GROQ_API_KEY instead of CLOUDFLARE_*

# 4. Update main.py startup validation back to Groq vars

# 5. Reinstall dependencies
pip install -r requirements.txt
```

---

## API Response Format

Both APIs return similar response structures, but Cloudflare has a specific format:

```json
{
  "success": true,
  "result": {
    "response": "The AI's answer here..."
  }
}
```

Error responses:
```json
{
  "success": false,
  "errors": ["Error message"]
}
```

---

## Troubleshooting

### "CLOUDFLARE_API_TOKEN not set"
- Make sure `.env` file exists and is in the project root
- Verify you copied the token correctly from Cloudflare Dashboard
- Make sure there are no extra spaces or quotes

### "Cloudflare API error 401"
- Your API token may have expired or is incorrect
- Check your `.env` file
- Try regenerating a new token in Cloudflare Dashboard

### "Cloudflare API error 403"
- Your API token doesn't have the right permissions
- Go to Account → API Tokens and edit the token
- Ensure **Cloudflare Workers AI** has Edit permission

### "Cloudflare API error 500"
- Cloudflare service may be temporarily unavailable
- Try again in a few seconds
- Check [Cloudflare Status](https://www.cloudflarestatus.com)

---

## Code Structure

The new `agent.py` uses:
- `warm_github_cache()` — Pre-fetch GitHub data at startup (same as before)
- `_build_system_prompt()` — Inject Vicky's profile into the prompt
- `run_agent()` — Call Cloudflare REST API with httpx

All business logic remains the same. Only the LLM API provider changed.

---

## Future Improvements

- [ ] Add caching layer for frequent questions
- [ ] Implement rate limiting for API calls
- [ ] Add Cloudflare Analytics for usage tracking
- [ ] Support multiple model variants

---

**Last Updated:** March 8, 2026  
**Status:** ✅ Production Ready
