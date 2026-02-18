"""Configuration for the ZARA humanoid robot software stack."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from environment variables."""

    robot_name: str = os.getenv("ZARA_NAME", "Zara")
    tts_rate: int = int(os.getenv("ZARA_TTS_RATE", "160"))
    tts_volume: float = float(os.getenv("ZARA_TTS_VOLUME", "1.0"))
    listen_timeout: int = int(os.getenv("ZARA_LISTEN_TIMEOUT", "5"))
    listen_phrase_limit: int = int(os.getenv("ZARA_PHRASE_LIMIT", "12"))
    ai_api_url: str | None = os.getenv("ZARA_AI_API_URL")
    ai_api_key: str | None = os.getenv("ZARA_AI_API_KEY")


SETTINGS = Settings()
