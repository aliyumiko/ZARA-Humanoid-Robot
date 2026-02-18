"""Speech recognition helpers for ZARA."""

from __future__ import annotations

import speech_recognition as sr

from config import SETTINGS


def listen() -> str:
    """Capture microphone audio and return recognized text."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(
            source,
            timeout=SETTINGS.listen_timeout,
            phrase_time_limit=SETTINGS.listen_phrase_limit,
        )

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        return "I could not understand."
    except sr.RequestError:
        return "Speech recognition service is unavailable."
