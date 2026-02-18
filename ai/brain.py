"""AI response logic for ZARA."""

from __future__ import annotations

import json
from pathlib import Path

import requests

from config import SETTINGS

KB_PATH = Path(__file__).resolve().parent.parent / "data" / "knowledge_base.json"


def _load_knowledge_base() -> dict[str, str]:
    if not KB_PATH.exists():
        return {}
    try:
        with KB_PATH.open("r", encoding="utf-8") as file:
            raw = json.load(file)
    except json.JSONDecodeError:
        return {}

    return {str(k).lower(): str(v) for k, v in raw.items()}


def _knowledge_base_response(user_text: str) -> str | None:
    kb = _load_knowledge_base()
    lowered = user_text.lower().strip()

    if lowered in kb:
        return kb[lowered]

    for key, value in kb.items():
        if key in lowered:
            return value

    return None


def _api_response(user_text: str) -> str | None:
    if not SETTINGS.ai_api_url:
        return None

    headers = {"Content-Type": "application/json"}
    if SETTINGS.ai_api_key:
        headers["Authorization"] = f"Bearer {SETTINGS.ai_api_key}"

    payload = {"input": user_text}

    try:
        response = requests.post(
            SETTINGS.ai_api_url,
            json=payload,
            headers=headers,
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return None

    for key in ("answer", "response", "output", "text"):
        if key in data:
            return str(data[key])

    return None


def think(user_text: str) -> str:
    """Generate an answer using local KB first, then optional AI API."""
    if not user_text.strip():
        return "Please say that again so I can help you."

    kb_answer = _knowledge_base_response(user_text)
    if kb_answer:
        return kb_answer

    api_answer = _api_response(user_text)
    if api_answer:
        return api_answer

    return (
        "I am still learning. Please connect an AI API endpoint or add this topic "
        "to my knowledge base."
    )
