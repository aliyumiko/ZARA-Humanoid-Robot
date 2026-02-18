"""Main controller entry point for ZARA."""

from __future__ import annotations

from ai.brain import think
from config import SETTINGS
from voice.listen import listen
from voice.speak import speak


EXIT_WORDS = {"exit", "quit", "stop", "goodbye"}


def main() -> None:
    """Run the continuous speech -> AI -> speech interaction loop."""
    greeting = (
        f"Hello. I am {SETTINGS.robot_name}, your intelligent humanoid robot. "
        "I am ready to assist you."
    )
    print(greeting)
    speak(greeting)

    while True:
        try:
            user_text = listen()
        except Exception as exc:  # Hardware/runtime guard for onboarding experience.
            error_msg = f"Listening failed: {exc}"
            print(error_msg)
            speak("I could not access the microphone. Please check your audio device.")
            continue

        normalized = user_text.lower().strip()
        if normalized in EXIT_WORDS:
            farewell = "Goodbye. I am shutting down now."
            print(farewell)
            speak(farewell)
            break

        response = think(user_text)
        print(f"Zara: {response}")
        speak(response)


if __name__ == "__main__":
    main()
