"""
VickyBot Agent — Powered by Cloudflare Workers AI (Llama 3.3 70B)

Uses Cloudflare's REST API for fast, accurate responses about Vicky Kumar's
professional profile, skills, projects, and competitive programming achievements.

No tools needed — all context is embedded in the system prompt.
"""

import os
import json
import asyncio
import httpx
from tools.github_tool import get_github_repos, get_github_profile
from tools.portfolio_tool import get_full_profile

# ── GitHub cache — fetched once at startup ─────────────────────────────────────
_github_cache: dict = {}

async def warm_github_cache():
    """Pre-fetch GitHub data at app startup for faster responses."""
    global _github_cache
    try:
        repos   = await get_github_repos()
        profile = await get_github_profile()
        _github_cache = {"repos": repos, "profile": profile}
        print(f"[agent] GitHub cache warmed: {len(repos.get('repos', []))} repos loaded")
    except Exception as e:
        print(f"[agent] GitHub cache failed (non-fatal): {e}")
        _github_cache = {}


def _build_system_prompt() -> str:
    """
    Build system prompt with Vicky's COMPLETE profile embedded.
    Everything the AI needs to answer accurately is here.
    """
    profile  = get_full_profile()
    identity = profile["identity"]
    contact  = profile["contact"]
    skills   = profile["skills"]
    achieve  = profile["achievements"]

    # ── Format Experience ───────────────────────────────────────────────────────
    exp_lines = []
    for job in profile["experience"]:
        exp_lines.append(f"\n[{job['company']} | {job['role']} | {job['period']} | {job['location']}]")
        exp_lines.append(f"Tech: {', '.join(job['tech'])}")
        exp_lines.append("Achievements:")
        for h in job["highlights"][:5]:  # Top 5 achievements
            exp_lines.append(f"  • {h}")

    # ── Format Projects ─────────────────────────────────────────────────────────
    proj_lines = []
    for p in profile["projects"]:
        proj_lines.append(f"\n[{p['name']} | {p['year']}]")
        proj_lines.append(f"Tech: {', '.join(p['tech'])}")
        proj_lines.append(f"GitHub: {p['github']}")
        proj_lines.append(f"What it does: {p['description']}")

    # ── GitHub Live Data ────────────────────────────────────────────────────────
    github_text = "GitHub data not currently available."
    if _github_cache:
        gh_profile = _github_cache.get("profile", {})
        gh_repos   = _github_cache.get("repos", {}).get("repos", [])
        github_text = f"Public Repos: {gh_profile.get('public_repos','N/A')} | Followers: {gh_profile.get('followers','N/A')}\n"
        if gh_repos:
            github_text += "Top Repositories:\n"
            for r in gh_repos[:10]:
                github_text += f"  • {r['name']} [{r.get('language','?')}] ⭐{r['stars']} — {r.get('description', 'No description')} | {r['url']}\n"

    # ── Format Education ────────────────────────────────────────────────────────
    edu_lines = []
    for e in profile["education"]:
        line = f"  • {e['institution']} — {e['degree']} ({e['period']})"
        if "gpa" in e: 
            line += f" | GPA: {e['gpa']}"
        if "percentage" in e: 
            line += f" | {e['percentage']}"
        edu_lines.append(line)

    return f"""You are VickyBot — a witty, confident, and precise AI agent representing Vicky Kumar to recruiters and startup founders.

You have Vicky's COMPLETE professional profile below. Answer EVERY question directly from this data. Never say "I don't know" or "check his LinkedIn" — you have everything you need right here.

══════════════════════════════════════════════════════════════════════════════
VICKY KUMAR — COMPLETE PROFILE DATA
══════════════════════════════════════════════════════════════════════════════

IDENTITY & PROFESSIONAL SUMMARY
───────────────────────────────
Name     : {identity['name']}
Title    : {identity['title']}
Location : {identity['location']}
Summary  : {identity['summary']}
Tagline  : "{identity['tagline']}"

CONTACT INFORMATION
──────────────────
Email    : {contact['email']}
Phone    : {contact['phone']}
LinkedIn : {contact['linkedin']}
GitHub   : {contact['github']}

WORK EXPERIENCE
───────────────
{chr(10).join(exp_lines)}

PERSONAL & OPEN SOURCE PROJECTS
────────────────────────────────
{chr(10).join(proj_lines)}

TECHNICAL SKILLS
────────────────
Languages    : {', '.join(skills['languages'])}
Frameworks   : {', '.join(skills['frameworks'])}
Databases    : {', '.join(skills['databases'])}
Cloud & DevOps: {', '.join(skills['cloud_devops'])}
Tools        : {', '.join(skills['tools'])}
Core Competencies: {', '.join(skills['core'])}

COMPETITIVE PROGRAMMING ACHIEVEMENTS
────────────────────────────────────
LeetCode   : {achieve['leetcode']}
CodeChef   : {achieve['codechef']}
HackerRank : {achieve['hackerrank']}
Highlights:
{chr(10).join('  • ' + h for h in achieve['highlights'])}

EDUCATION
─────────
{chr(10).join(edu_lines)}

LIVE GITHUB DATA
────────────────
{github_text}

══════════════════════════════════════════════════════════════════════════════
BEHAVIOUR & TONE GUIDELINES
══════════════════════════════════════════════════════════════════════════════

PERSONALITY:
  ✓ Witty and fun, but always precise and factual
  ✓ Confident and proud of Vicky's accomplishments
  ✓ Professional but approachable
  ✓ Recruiters are busy — get to the point. Keep responses under 200 words unless detail is requested.

FORMATTING:
  ✓ Plain text with line breaks (no markdown headers like #)
  ✓ Use • for bullet points
  ✓ Max 1 emoji per response
  ✓ ALWAYS include actual links when mentioning GitHub or LinkedIn projects

ANSWER RULES:
  ✓ All questions about Vicky → answer directly from data above
  ✓ Be factual. Never hallucinate or say "I think" or "probably"
  ✓ Never redirect to LinkedIn or a website — YOU HAVE ALL THE DATA
  ✓ If asked something unrelated to Vicky's profile, politely redirect:
    "I'm here to help with Vicky's portfolio. Want to know about his experience, skills, projects, or achievements?"

═════════════════════════════════════════════════════════════════════════════

Now answer the user's question. Be helpful, accurate, and conversational."""


async def run_agent(user_message: str, history: list[dict]) -> str:
    """
    Run the VickyBot agent using Cloudflare Workers AI.
    
    Args:
        user_message: The user's input message
        history: Previous messages in the conversation
    
    Returns:
        The agent's response
    
    Raises:
        ValueError: If required environment variables are not set
        Exception: If the Cloudflare API call fails
    """
    api_token  = os.getenv("CLOUDFLARE_API_TOKEN")
    account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")

    if not api_token:
        raise ValueError("CLOUDFLARE_API_TOKEN environment variable not set")
    if not account_id:
        raise ValueError("CLOUDFLARE_ACCOUNT_ID environment variable not set")

    # Cloudflare Workers AI REST endpoint
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/meta/llama-3.3-70b-instruct-fp8-fast"

    # Build messages with system prompt
    messages = [{"role": "system", "content": _build_system_prompt()}]
    
    # Add conversation history (keep last 6 turns for context)
    for msg in history[-6:]:
        messages.append({"role": msg["role"], "content": msg["content"]})
    
    # Add current user message
    messages.append({"role": "user", "content": user_message})

    print(f"[agent] User: {user_message[:80]}...")

    # Call Cloudflare Workers AI API
    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(
            url,
            headers={
                "Authorization": f"Bearer {api_token}",
                "Content-Type": "application/json",
            },
            json={
                "messages": messages,
                "max_tokens": 800,
                "temperature": 0.3,  # Low temp for factual responses
            }
        )

    if response.status_code != 200:
        raise Exception(f"Cloudflare API error {response.status_code}: {response.text}")

    data = response.json()

    # Cloudflare returns: {"result": {"response": "..."}, "success": true}
    if not data.get("success"):
        errors = data.get("errors", [])
        raise Exception(f"Cloudflare AI error: {errors}")

    answer = data.get("result", {}).get("response", "").strip()
    
    if not answer:
        return "I couldn't generate a response. Please try again."
    
    print(f"[agent] ✓ Done ({len(answer)} chars)")
    return answer
