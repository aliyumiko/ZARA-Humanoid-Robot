"""Text-to-speech utilities for ZARA."""

from __future__ import annotations

import pyttsx3

from config import SETTINGS


_engine = pyttsx3.init()
_engine.setProperty("rate", SETTINGS.tts_rate)
_engine.setProperty("volume", SETTINGS.tts_volume)


def speak(text: str) -> None:
    """Speak text through the default system output device."""
    _engine.say(text)
    _engine.runAndWait()
