import json
from pathlib import Path

_DATA_PATH = Path(__file__).parent.parent / "data" / "portfolio_data.json"
_data = None


def _load():
    global _data
    if _data is None:
        _data = json.loads(_DATA_PATH.read_text())
    return _data


def get_identity() -> dict:
    """Get Vicky's basic identity, title, summary and tagline."""
    d = _load()
    return d["identity"]


def get_experience() -> dict:
    """Get Vicky's full work experience history."""
    d = _load()
    return {"experience": d["experience"]}


def get_skills() -> dict:
    """Get Vicky's technical skills grouped by category."""
    d = _load()
    return d["skills"]


def get_projects() -> dict:
    """Get Vicky's personal and technical projects with descriptions and links."""
    d = _load()
    return {"projects": d["projects"]}


def get_contact_info() -> dict:
    """Get Vicky's contact information including email, LinkedIn, GitHub."""
    d = _load()
    return d["contact"]


def get_achievements() -> dict:
    """Get Vicky's competitive programming achievements and ratings."""
    d = _load()
    return d["achievements"]


def get_education() -> dict:
    """Get Vicky's educational background."""
    d = _load()
    return {"education": d["education"]}


def get_full_profile() -> dict:
    """Get the complete portfolio profile — all info at once."""
    return _load()
