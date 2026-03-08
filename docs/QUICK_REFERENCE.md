# 🎯 Quick Reference Card

Print this or bookmark it for quick access while using the portfolio agent!

---
## 🚀 Getting Started (2 minutes)

```bash
# 1. Activate environment
source /Users/vickykumar/Downloads/portfolio-agent/env/bin/activate

# 2. Create .env (copy from template)
cd /Users/vickykumar/Downloads/portfolio-agent
cp .env.example .env

# 3. Edit .env and add your API keys
# GROQ_API_KEY=gsk_your_key_here
# GITHUB_TOKEN=ghp_your_token_here (optional)

# 4. Install dependencies (first time only)
pip install -r requirements.txt

# 5. Run the server
uvicorn main:app --reload --port 8000

# 6. Open in browser
# http://localhost:8000
```

---

## 🎓 Where to Get API Keys

| Key | Website | Format | Required? |
|-----|---------|--------|-----------|
| **Groq API Key** | https://console.groq.com | `gsk_...` | ✅ YES |
| **GitHub Token** | https://github.com/settings/tokens | `ghp_...` | ⚠️ Optional |

---

## 📁 Key Files to Know

| File | Edit For | Don't Edit If |
|------|----------|---------------|
| `agent.py` | AI behavior, tone, examples | You don't know Python |
| `data/portfolio_data.json` | Your resume data | It's accurate |
| `.env` | API keys | It's working |
| `static/index.html` | UI design | It looks fine |
| `main.py` | Server behavior | It works |

---

## 💬 Test These Questions

```
1. "Who are you?" → Should introduce self
2. "Tell me about Eka.Care" → Should be detailed
3. "What's your tech stack?" → Should list skills
4. "Show me your projects" → Should list with links
5. "What are your achievements?" → Should show stats
6. "How can I contact you?" → Should give contact info
```

**If responses aren't detailed → Check `data/portfolio_data.json` is complete**

---

## ⚙️ Adjust AI Behavior

Edit `agent.py`, function `run_agent()`:

```python
response = await client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    max_tokens=1024,      # ⬆️ for longer responses
    temperature=0.2,      # ⬆️ for more creative, ⬇️ for factual
    top_p=0.85,          # ⬆️ for more variety, ⬇️ for consistency
    frequency_penalty=0.3, # ⬆️ to avoid repetition
)
```

---

## 🐛 Common Issues & Fixes

| Issue | Check | Fix |
|-------|-------|-----|
| "GROQ_API_KEY not set" | `.env` exists | `cp .env.example .env` |
| Chat stuck forever | API key valid | Get new key from Groq |
| Vague responses | Profile data complete | Update `data/portfolio_data.json` |
| GitHub repos not showing | Optional feature | Add `GITHUB_TOKEN` to `.env` |
| UI not loading | Port 8000 free | Check nothing else on 8000 |

---

## 🚀 Deploy to Render

```
1. Push code to GitHub
2. Go to https://render.com
3. New Web Service → Connect GitHub repo
4. Add environment variables:
   - GROQ_API_KEY=gsk_...
   - GITHUB_TOKEN=ghp_... (optional)
5. Deploy!
```

**Render free tier:** Sleeps after 15min inactivity (first request ~30sec slower)

---

## 📊 File Locations

```
/Users/vickykumar/Downloads/portfolio-agent/
├── agent.py              ← AI logic
├── main.py              ← Server
├── .env                 ← API keys (SECRET)
├── data/
│   └── portfolio_data.json  ← Your resume
├── static/
│   └── index.html       ← Chat UI
└── requirements.txt     ← Dependencies
```

---

## 🔐 Security Checklist

- ✅ `.env` in `.gitignore` (won't push to GitHub)
- ✅ API keys never logged or exposed
- ✅ Never commit `.env` file
- ✅ Never share API keys publicly
- ✅ Regenerate keys if leaked

---

## 📈 Performance Tips

| Tip | Why | How |
|-----|-----|-----|
| Pre-cache GitHub data | Faster startup | Already implemented |
| Keep context small | Faster responses | Last 8 turns kept |
| Use low temperature | More factual | Already set to 0.2 |
| Embed profile in prompt | Zero tool overhead | Already done |

---

## 🎨 Customize UI

Edit `static/index.html` for:
- Colors (CSS variables at top)
- Fonts and sizes
- Emoji and icons
- Button text
- Suggestion chips

---

## 📱 Mobile Testing

Your bot works on:
- ✅ Desktop browsers
- ✅ Mobile phones
- ✅ Tablets
- ✅ Touch devices

Test on your phone before sharing!

---

## 📚 Documentation Files

| File | Read For | Time |
|------|----------|------|
| `README.md` | Project overview | 5 min |
| `SETUP_GUIDE.md` | Detailed setup | 15 min |
| `EXAMPLE_CONVERSATIONS.md` | Sample Q&A | 10 min |
| `BUILD_SUMMARY.md` | Technical details | 10 min |
| `CHECKLIST.md` | Verification steps | 20 min |
| This file | Quick reference | 2 min |

---

## 🔗 Important Links

| What | URL |
|------|-----|
| Groq Console | https://console.groq.com |
| Groq Docs | https://console.groq.com/docs |
| GitHub Settings | https://github.com/settings/tokens |
| Render Dashboard | https://render.com |
| Local Server | http://localhost:8000 |

---

## ⌨️ Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Send message | `Enter` |
| New line | `Shift + Enter` |
| Clear input | Select all + Delete |
| Focus input | Click or Tab |

---

## 🎯 One-Line Commands

```bash
# Navigate to project
cd /Users/vickykumar/Downloads/portfolio-agent

# Activate environment
source env/bin/activate

# Run server
uvicorn main:app --reload --port 8000

# Deactivate environment
deactivate

# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Check Python version
python --version
```

---

## 💡 Troubleshooting Flowchart

```
Bot not responding?
├─ Check API key valid ✓
├─ Check internet connection ✓
├─ Check server logs ✓
├─ Try simpler question ✓
└─ Restart server

Responses not detailed?
├─ Check data/portfolio_data.json complete ✓
├─ Check system prompt in agent.py ✓
├─ Try asking more specifically ✓
└─ Adjust temperature setting

UI not loading?
├─ Check http://localhost:8000 ✓
├─ Check port 8000 not in use ✓
├─ Clear browser cache ✓
└─ Check static/index.html exists
```

---

## 🎓 Quick Learning

### How Prompt Injection Works
Your entire profile → System prompt → AI has full context → No tool calls needed → Fast responses ⚡

### Why Groq?
- Fast API (best latency)
- Free tier (no cost)
- Powerful model (70B parameters)
- LLaMA quality (accurate)

### Why This Architecture?
- **Fast:** No tool latency
- **Cheap:** No API overhead
- **Accurate:** Full context, no hallucinations
- **Simple:** Pure prompt-based

---

## 🚀 Launch Checklist (Quick)

- [ ] `.env` created with keys
- [ ] Dependencies installed
- [ ] Server running locally
- [ ] Test message sent
- [ ] Get detailed response
- [ ] Deployed to Render
- [ ] Share URL with recruiters!

---

## 💬 Sample Conversations

**Q:** Tell me about your current role
**A:** 🏥 [Detailed response about Eka.Care with tech and achievements]

**Q:** What can you build?
**A:** [Lists skills with examples from real projects]

**Q:** How do I contact you?
**A:** [Email, phone, LinkedIn, GitHub with links]

---

## 🎉 Success Indicators

✅ You know you're done when:
- Server starts without errors
- Chat UI loads in browser
- Bot responds to "Who are you?"
- Responses are detailed and accurate
- Deployed to Render with live URL
- Ready to share with recruiters!

---

## 📞 Emergency Help

**Key not working?**
- Get new key from Groq console
- Update `.env` file
- Restart server

**Chat stuck?**
- Check internet
- Verify API key
- Restart server
- Try simpler question

**Need to change something?**
- Profile data → `data/portfolio_data.json`
- AI behavior → `agent.py` system prompt
- UI design → `static/index.html`
- Server behavior → `main.py`

---

**Keep this handy! Print it or bookmark it. 🎯**

---

*Last updated: March 8, 2026*
*Your Portfolio Agent v1.0 - Ready to Go! 🚀*
