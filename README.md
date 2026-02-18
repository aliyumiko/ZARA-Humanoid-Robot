# ZARA – Intelligent Humanoid Educational & Agricultural Assistant Robot

## Objective

ZARA is an AI-powered humanoid robot software stack designed to support:

- Voice interaction (speech input and output)
- Educational assistance
- Agricultural advisory guidance
- Visual recognition with a camera
- Decision-making via local knowledge and optional AI APIs

This version is intended to run on a Windows PC first, then later be ported to Raspberry Pi.

## Repository Structure

```text
ZARA-Humanoid-Robot/
├── main.py
├── config.py
├── requirements.txt
├── test_voice.py
├── ai/
│   └── brain.py
├── voice/
│   ├── listen.py
│   └── speak.py
├── vision/
│   └── vision.py
└── data/
    └── knowledge_base.json
```

## Setup (Windows)

1. Clone the repository:

   ```powershell
   git clone https://github.com/aliyumiko/Zara-Humanoid-Robot.git
   cd Zara-Humanoid-Robot
   ```

2. Create and activate virtual environment:

   ```powershell
   py -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

## Run Modules

- Initial voice test:

  ```powershell
  py test_voice.py
  ```

- Main robot loop:

  ```powershell
  py main.py
  ```

- Vision module (ESC to exit):

  ```powershell
  py -c "from vision.vision import see; see()"
  ```

## Configuration

Create a `.env` file (optional) to customize behavior:

```env
ZARA_NAME=Zara
ZARA_TTS_RATE=160
ZARA_TTS_VOLUME=1.0
ZARA_LISTEN_TIMEOUT=5
ZARA_PHRASE_LIMIT=12
# Optional external AI endpoint:
# ZARA_AI_API_URL=https://your-api/ask
# ZARA_AI_API_KEY=your_token
```

If no AI endpoint is configured, ZARA answers from `data/knowledge_base.json` and a fallback response.
