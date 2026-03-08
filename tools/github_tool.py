import os
import httpx
from typing import Optional

GITHUB_USERNAME = "vickykr26941"
GITHUB_API = "https://api.github.com"


def _headers():
    token = os.getenv("GITHUB_TOKEN")
    h = {"Accept": "application/vnd.github+json"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


async def get_github_repos() -> dict:
    """Fetch all public repositories for Vicky Kumar from GitHub."""
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(
                f"{GITHUB_API}/users/{GITHUB_USERNAME}/repos",
                headers=_headers(),
                params={"sort": "updated", "per_page": 20, "type": "public"},
            )
            if resp.status_code != 200:
                return {"error": f"GitHub API returned {resp.status_code}"}
            repos = resp.json()
            result = []
            for r in repos:
                result.append({
                    "name": r["name"],
                    "description": r.get("description") or "No description",
                    "url": r["html_url"],
                    "stars": r["stargazers_count"],
                    "forks": r["forks_count"],
                    "language": r.get("language") or "Unknown",
                    "updated": r["updated_at"][:10],
                    "topics": r.get("topics", []),
                })
            return {"repos": result, "total": len(result), "username": GITHUB_USERNAME}
    except Exception as e:
        return {"error": str(e)}


async def get_repo_details(repo_name: str) -> dict:
    """Fetch detailed info and README for a specific repository."""
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            repo_resp = await client.get(
                f"{GITHUB_API}/repos/{GITHUB_USERNAME}/{repo_name}",
                headers=_headers(),
            )
            if repo_resp.status_code != 200:
                return {"error": f"Repo not found: {repo_name}"}

            repo = repo_resp.json()

            readme_resp = await client.get(
                f"{GITHUB_API}/repos/{GITHUB_USERNAME}/{repo_name}/readme",
                headers={**_headers(), "Accept": "application/vnd.github.raw"},
            )
            readme = readme_resp.text[:2000] if readme_resp.status_code == 200 else "No README available"

            langs_resp = await client.get(
                f"{GITHUB_API}/repos/{GITHUB_USERNAME}/{repo_name}/languages",
                headers=_headers(),
            )
            languages = list(langs_resp.json().keys()) if langs_resp.status_code == 200 else []

            return {
                "name": repo["name"],
                "description": repo.get("description") or "No description",
                "url": repo["html_url"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "languages": languages,
                "topics": repo.get("topics", []),
                "created": repo["created_at"][:10],
                "updated": repo["updated_at"][:10],
                "readme_preview": readme,
            }
    except Exception as e:
        return {"error": str(e)}


async def get_github_profile() -> dict:
    """Fetch Vicky's GitHub profile stats."""
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(
                f"{GITHUB_API}/users/{GITHUB_USERNAME}",
                headers=_headers(),
            )
            if resp.status_code != 200:
                return {"error": "Could not fetch GitHub profile"}
            u = resp.json()
            return {
                "username": u["login"],
                "name": u.get("name"),
                "bio": u.get("bio"),
                "public_repos": u["public_repos"],
                "followers": u["followers"],
                "following": u["following"],
                "profile_url": u["html_url"],
                "avatar_url": u.get("avatar_url"),
            }
    except Exception as e:
        return {"error": str(e)}
