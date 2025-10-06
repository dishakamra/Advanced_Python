from __future__ import annotations

def slugify(text: str) -> str:
    return "-".join(text.lower().split())