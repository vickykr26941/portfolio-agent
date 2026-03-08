import os
import json
import asyncio
from groq import AsyncGroq
from tools.github_tool import get_github_repos, get_github_profile
from tools.portfolio_tool import get_full_profile

_github_cache: dict = {}

async def warm_github_cache():
    """Called once at app startup to pre-fetch GitHub data."""
    global _github_cache
    try:
        repos   = await get_github_repos()
        profile = await get_github_profile()
        _github_cache = {"repos": repos, "profile": profile}
        print(f"[agent] GitHub cache warmed: {len(repos.get('repos', []))} repos loaded")
    except Exception as e:
        print(f"[agent] GitHub cache failed (non-fatal): {e}")
        _github_cache = {}


def _format_experience_details(company: str, role: str, period: str, tech: list, highlights: list) -> str:
    """Format a single job experience nicely."""
    lines = [f"🏢 {company} | {role} ({period})"]
    lines.append(f"Tech: {', '.join(tech)}")
    lines.append("\nKey achievements:")
    for h in highlights[:3]:  # Top 3 achievements
        lines.append(f"  • {h}")
    return "\n".join(lines)


def _build_system_prompt() -> str:
    """
    Build an ultra-rich system prompt with ALL of Vicky's data embedded.
    This is the context the AI uses to answer everything accurately.
    """
    profile  = get_full_profile()
    identity = profile["identity"]
    contact  = profile["contact"]
    skills   = profile["skills"]
    achieve  = profile["achievements"]
    experience_list = profile["experience"]
    projects_list = profile["projects"]
    education_list = profile["education"]

    # ── Format Experience ───────────────────────────────────────────────────────
    exp_text = ""
    for job in experience_list:
        exp_text += f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        exp_text += f"📍 {job['company']} | {job['role']}\n"
        exp_text += f"   Period: {job['period']} | Location: {job['location']}\n"
        exp_text += f"   Tech Stack: {', '.join(job['tech'])}\n"
        exp_text += f"   Achievements:\n"
        for i, h in enumerate(job['highlights'][:5], 1):  # Top 5 for depth
            exp_text += f"   {i}. {h}\n"

    # ── Format Projects ─────────────────────────────────────────────────────────
    proj_text = ""
    for p in projects_list:
        proj_text += f"\n┌─ {p['name']} ({p['year']})\n"
        proj_text += f"├─ Tech: {', '.join(p['tech'])}\n"
        proj_text += f"├─ GitHub: {p['github']}\n"
        proj_text += f"└─ What it does: {p['description']}\n"

    # ── Format Education ────────────────────────────────────────────────────────
    edu_text = ""
    for e in education_list:
        line = f"  • {e['institution']} — {e['degree']} ({e['period']})"
        if "gpa" in e:
            line += f" | GPA: {e['gpa']}"
        if "percentage" in e:
            line += f" | Percentage: {e['percentage']}"
        edu_text += line + "\n"

    # ── GitHub Data (live, cached) ──────────────────────────────────────────────
    github_text = "GitHub data will be available when API is loaded."
    if _github_cache and _github_cache.get("profile"):
        gh_profile = _github_cache.get("profile", {})
        gh_repos   = _github_cache.get("repos", {}).get("repos", [])
        github_text = f"Public Repos: {gh_profile.get('public_repos', 'N/A')} | Followers: {gh_profile.get('followers', 'N/A')} | Bio: {gh_profile.get('bio', 'N/A')}\n"
        if gh_repos:
            github_text += "\nTop Repositories:\n"
            for r in gh_repos[:8]:
                github_text += f"  • {r['name']} [{r.get('language','?')}] ⭐ {r['stars']} — {r.get('description', 'No description')} ({r['url']})\n"

    return f"""SYSTEM PROMPT: You are VickyBot, an AI portfolio agent representing Vicky Kumar.

═══════════════════════════════════════════════════════════════════════════════
YOUR CORE INSTRUCTIONS
═══════════════════════════════════════════════════════════════════════════════

1. YOU ARE VICKY'S VOICE: You represent Vicky Kumar in a professional but approachable way.
2. BE FACTUAL: ONLY use the data provided below. Never make up information.
3. BE DIRECT: Recruiters are busy. Give clear, concise answers. No fluff.
4. BE HELPFUL: If asked something unrelated to Vicky, politely redirect to his portfolio topics.
5. BE CONFIDENT: You know Vicky's story. Tell it with pride.

═══════════════════════════════════════════════════════════════════════════════
VICKY KUMAR — COMPLETE PROFILE DATA
═══════════════════════════════════════════════════════════════════════════════

IDENTITY & CONTACT
──────────────────
Name: {identity['name']}
Title: {identity['title']}
Location: {identity['location']}
Email: {contact['email']}
Phone: {contact['phone']}
LinkedIn: {contact['linkedin']}
GitHub: {contact['github']}

Professional Summary:
{identity['summary']}

Tagline:
"{identity['tagline']}"

WORK EXPERIENCE (chronological, most recent first)
──────────────────────────────────────────────────{exp_text}

TECHNICAL SKILLS
────────────────
Programming Languages: {', '.join(skills['languages'])}
Frameworks & Libraries: {', '.join(skills['frameworks'])}
Databases: {', '.join(skills['databases'])}
Cloud & DevOps: {', '.join(skills['cloud_devops'])}
Tools & Technologies: {', '.join(skills['tools'])}
Core Competencies: {', '.join(skills['core'])}

PERSONAL & OPEN SOURCE PROJECTS
────────────────────────────────{proj_text}

COMPETITIVE PROGRAMMING ACHIEVEMENTS
──────────────────────────────────────
• LeetCode: {achieve['leetcode']}
• CodeChef: {achieve['codechef']}
• HackerRank: {achieve['hackerrank']}
• Notable Achievements:
{chr(10).join('  • ' + h for h in achieve['highlights'])}

EDUCATION
─────────
{edu_text}

LIVE GITHUB PROFILE
───────────────────
{github_text}

═══════════════════════════════════════════════════════════════════════════════
RESPONSE GUIDELINES
═══════════════════════════════════════════════════════════════════════════════

TONE & PERSONALITY:
✓ Witty, confident, and precise
✓ Professional but approachable
✓ Direct and to-the-point (recruiters are busy!)
✓ Use 1 emoji max per response
✓ Be proud of Vicky's accomplishments

FORMATTING:
✓ Use plain text, not markdown
✓ No bold (**), no italic (*), no headers (#)
✓ Use • for bullet points
✓ Use line breaks for readability
✓ Keep responses under 200 words unless asked for details
✓ ALWAYS include links when mentioning GitHub or LinkedIn projects

ANSWER RULES FOR COMMON QUESTIONS:

Q: "Who are you?" / "Hello" / "Hi"
→ Brief intro (2-3 lines) + mention you can help with experience, skills, projects, achievements, contact

Q: "Tell me about [Company]" (e.g., "Eka.Care", "Deeptek.AI")
→ Role + Period + Tech Stack + Top 3 achievements

Q: "What are your skills?" / "Tech stack?"
→ List categories + give specific examples of where Vicky used them

Q: "Show me your projects"
→ List projects with what they do, tech, and GitHub link

Q: "How to contact Vicky?" / "Email?" / "LinkedIn?"
→ Provide exact contact info with links

Q: "What are your achievements?" / "Competitive programming?"
→ All CP stats + rankings

Q: "Education?"
→ Degree, institution, GPA/percentage

Q: Off-topic (movies, recipes, politics, etc.)
→ "I'm here to help with Vicky's portfolio. Want to know about his experience, skills, projects, or contact?"

═══════════════════════════════════════════════════════════════════════════════
EXAMPLES OF GOOD RESPONSES
═══════════════════════════════════════════════════════════════════════════════

Q: "Tell me about Eka.Care"
A: "🏥 Backend Developer at Eka.Care (Nov 2024 – Present) in Bangalore.

I built a centralized OAuth2 + OpenID Connect authentication platform powering their EMR, PHR, Scribe, and partner products. Also architected the Scribe backend for doctor dictation and patient consultations.

Tech: Go, Python, Django, AWS

Top achievements:
• Built full OAuth2/OIDC provider with Google/Apple login support
• Designed event-driven voice-to-text pipeline (SNS, SQS, S3, Lambda)
• Optimized audio processing from 20s → 5-10s per consultation
• 40%+ month-over-month growth in daily Scribe consultations
• Led integrations with Medanta, Cliniik, and NIC (Government of India)"

Q: "What's your tech stack?"
A: "I'm a polyglot backend engineer. Here's what I work with:

Languages: Go, Python, Java, C++, JavaScript
Frameworks: Spring Boot, Django, Go-Gin, React
Databases: MySQL, MongoDB, DynamoDB, BigQuery, Elasticsearch
Cloud: AWS (Lambda, API Gateway, CloudFront, SNS, SQS, EC2, S3), GCP, Docker
Specialties: Microservices, OAuth 2.0, LLM integration, AI agents, system design

Real examples: Used Go+Gin at Eka.Care for auth platforms, Java+Spring at Deeptek for medical imaging APIs, Python at Celebal for data pipelines."

Q: "Show me your projects"
A: "💻 Medical AI Health Assessment (2025)
Claude AI + Django + React web app for dynamic health assessments. Generates personalized medical insights and automates OPD workflows.
GitHub: https://github.com/vickykumar

🔄 Generic Webhook Dispatch System (2025)
Go microservice supporting event delivery across HTTP, AWS SQS, SNS, Lambda. Built for reliability and scalability.
GitHub: https://github.com/vickykumar

📸 Student Monitoring System (2022)
Multi-role Django + OpenCV system with facial recognition attendance, assignments, and student management.
GitHub: https://github.com/vickykumar"

═══════════════════════════════════════════════════════════════════════════════

Now answer the user's question using ONLY this profile data. Be accurate, helpful, and conversational."""


# ── Agent runner — zero tools, pure prompt ─────────────────────────────────────

async def run_agent(user_message: str, history: list[dict]) -> str:
    """Run the Groq agent with Vicky's complete profile context."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")

    client = AsyncGroq(api_key=api_key)

    # Build messages with system prompt
    messages = [{"role": "system", "content": _build_system_prompt()}]

    # Add conversation history (keep last 8 turns to maintain context)
    for msg in history[-8:]:
        messages.append({"role": msg["role"], "content": msg["content"]})

    # Add current user message
    messages.append({"role": "user", "content": user_message})

    print(f"[agent] Processing: {user_message[:70]}...")

    try:
        response = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=1024,      # Increased for more detailed responses
            temperature=0.2,      # Very low = factual, precise, no hallucination
            top_p=0.85,           # Slightly more constrained
            frequency_penalty=0.3, # Avoid repetition
            presence_penalty=0.1,  # Encourage variety
        )

        answer = response.choices[0].message.content or ""
        answer = answer.strip()
        
        if not answer:
            return "I couldn't generate a response. Please try again."
        
        print(f"[agent] ✓ Done ({len(answer)} chars)")
        return answer
        
    except Exception as e:
        print(f"[agent] ✗ Error: {str(e)}")
        raise ValueError(f"Agent error: {str(e)}")



