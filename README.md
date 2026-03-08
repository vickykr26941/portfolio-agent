# 🤖 Vicky Kumar — Portfolio Agent

An AI-powered portfolio chatbot built with **FastAPI + Groq LLaMA**, featuring live GitHub integration and a slick dark terminal UI. Recruiters and founders can chat with the agent to learn about Vicky's experience, skills, projects, and competitive programming achievements.

---

## ✨ Features

- 💬 **AI Chat** powered by Groq LLaMA 3.3 70B (fast, accurate, free tier)
- 🧠 **Smart Context** — complete profile embedded for instant, accurate responses
- 🎨 **Dark Terminal UI** — striking design built for tech recruiters
- 📱 **Mobile Responsive** — works perfectly on all screen sizes
- ⚡ **Quick Question Chips** — one-click suggestions for common questions
- 📬 **Contact Buttons** — email, LinkedIn, GitHub always visible
- � **Live GitHub Integration** — shows real repos with stars and languages
- 🚀 **Instant Deploy** — one-click deployment to Render (free)

---

## 🏗️ Project Structure

```
portfolio-agent/
├── main.py                  # FastAPI server
├── agent.py                 # LLM agent with Vicky's profile context
├── tools/
│   ├── github_tool.py       # GitHub API integration
│   └── portfolio_tool.py    # Profile data loader
├── data/
│   └── portfolio_data.json  # Complete resume/profile data
├── static/
│   └── index.html           # Beautiful chat UI
├── .env.example             # Environment template
├── requirements.txt         # Python dependencies
└── render.yaml              # Render deployment config
```

---

## 🚀 Local Setup

### 1. Clone and navigate
```bash
git clone https://github.com/vickykumar/portfolio-agent.git
cd portfolio-agent
```

### 2. Activate virtual environment
```bash
source env/bin/activate    # macOS/Linux
# or
env\Scripts\activate       # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```
GROQ_API_KEY=gsk_your_groq_key_here
GITHUB_TOKEN=ghp_your_github_token_here
```

### 5. Run locally
```bash
uvicorn main:app --reload --port 8000
```

Open **http://localhost:8000** in your browser — you're live! 🎉

---

## 🔑 Getting API Keys

### Groq API Key (Free)
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up or log in
3. Click **API Keys** → **Create API Key**
4. Free tier: Fast inference with rate limits

### GitHub Personal Access Token
1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **Generate new token (classic)**
3. Select scope: `public_repo` only
4. Copy the `ghp_...` token

---

## 🌐 Deploy to Render (Free)

### Quick Deploy
1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Render auto-detects `render.yaml` and configures everything
5. Add environment variables:
   - `GROQ_API_KEY` → your Groq key
   - `GITHUB_TOKEN` → your GitHub token
6. Click **Deploy** — done! 🚀

> **Free tier note:** Render free tier suspends services after 15 minutes of inactivity. First request after suspension takes ~30 seconds. Perfect for a portfolio!

---

## ✏️ Customizing Your Profile

All your profile data lives in `data/portfolio_data.json`. Edit it to update:
- **Identity**: Name, title, location, bio, tagline
- **Experience**: Companies, roles, tech stacks, achievements
- **Projects**: Name, tech, description, GitHub links
- **Skills**: Languages, frameworks, databases, cloud tools
- **Achievements**: Competitive programming stats
- **Education**: Degree, GPA, institution
- **Contact**: Email, phone, LinkedIn, GitHub

The AI uses all this data to answer questions accurately.

---

## 🎯 How It Works

1. **System Prompt Injection** — Your complete profile is embedded in the AI's system prompt
2. **Zero Tools** — No tool calls needed; all data is pre-loaded for instant responses
3. **Context-Aware** — The LLM uses your actual resume to answer everything
4. **Fast** — Groq's API is blazingly fast (no latency)
5. **Accurate** — No hallucinations; only answers from your profile data

---

## 🧪 Example Conversations

**User:** "Tell me about Eka.Care"
**Bot:** 🏥 Backend Developer at Eka.Care (Nov 2024 – Present) in Bangalore.

Architected and implemented a centralized OAuth2 + OpenID Connect authentication platform powering Eka Care EMR, PHR, Scribe, and partner-facing products.

Tech: Go, Python, Django, AWS

Key achievements:
• Built full OAuth2/OIDC provider with Google/Apple login support
• Designed event-driven voice-to-text pipeline (SNS, SQS, S3, Lambda)
• Optimized audio processing from 20s → 5-10s per consultation

---

**User:** "What's your tech stack?"
**Bot:** I'm a polyglot backend engineer. Here's what I work with:

Languages: Go, Python, Java, C++, JavaScript
Frameworks: Spring Boot, Django, Go-Gin, React
Databases: MySQL, MongoDB, DynamoDB, BigQuery, Elasticsearch
Cloud: AWS (EC2, S3, Lambda, API Gateway, CloudFront, SNS, SQS), GCP, Docker, CI/CD

---

## 📚 Project Details

This is a **recruitment/networking tool** for developers. The chatbot:
- Knows your complete professional history
- Can discuss specific projects with technical depth
- Has your competitive programming stats
- Provides accurate contact information
- Links to your GitHub repositories

Perfect for **recruiters, startup founders, or anyone** wanting to learn about your skills!

---

## 📄 License

MIT — feel free to fork and create your own portfolio agent!

---

## 🤝 Support

Questions or issues? Check the code or feel free to reach out:
- Email: vickykr26941@gmail.com
- LinkedIn: https://www.linkedin.com/in/vicky-kumar-a948431a9/
- GitHub: https://github.com/vickykr26941


