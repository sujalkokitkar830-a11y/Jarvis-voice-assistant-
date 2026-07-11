# Jarvis — Python Voice Assistant

A wake-word-activated voice assistant built in Python that listens for commands and responds using voice. Inspired by Iron Man's AI assistant, Jarvis can open websites, play music, read news headlines, and answer general queries using AI — all through voice.

## Features

- **Wake word detection** — listens continuously and activates only when it hears "Jarvis"
- **Voice commands** — captures spoken instructions using Google's speech recognition
- **Web navigation** — opens websites on command (Google, YouTube, Facebook, LinkedIn)
- **Music playback** — plays songs from a local music library via `musicLibrary.py`
- **News headlines** — fetches and reads out the latest headlines using NewsAPI
- **AI-powered responses** — any command that isn't a predefined action is passed to **Groq's LLaMA 3.3 70B** model for a smart, concise reply
- **Natural voice output** — uses Google Text-to-Speech (`gTTS`) with `pygame` for audio playback

## Tech Stack

- **Python 3**
- `speech_recognition` — converts voice input to text (Google Speech API)
- `gTTS` + `pygame` — generates and plays natural-sounding speech
- `groq` — LLM API for handling general/conversational commands
- `requests` — fetches live news headlines from NewsAPI
- `webbrowser` — opens websites
- `pyttsx3` — kept as an offline fallback TTS option (`speak_old`)

## How It Works

1. Jarvis continuously listens through the microphone for the wake word "Jarvis"
2. Once triggered, it says "Ya" and listens for the next command
3. `processCommand()` checks the command against known actions:
   - Opens a website, plays a song, or reads the news if matched
   - Otherwise, passes the command to `aiProcess()`, which queries the Groq API (LLaMA 3.3 70B) for a response
4. The response is converted to speech via `gTTS`, saved as a temporary MP3, and played using `pygame` — then the temp file is deleted

## Challenges & Learnings

- Switched from `pyttsx3` (robotic, offline) to `gTTS` + `pygame` for more natural-sounding speech output
- Debugged inconsistent NewsAPI responses due to endpoint/parameter issues
- Fixed choppy/interrupted speech by properly sequencing playback and cleanup (loading, waiting for playback to finish, then removing the temp file)
- Resolved indentation and logic bugs across command-handling functions
- Explored differences in behavior between Python 3.8 and 3.13 environments
- Integrated Groq's free LLaMA model to give Jarvis general conversational ability beyond fixed commands

## Setup

```bash
pip install speechrecognition pyttsx3 requests groq gtts pygame pocketsphinx
python jarvis.py
```

You'll also need a `musicLibrary.py` file in the same folder with a `music` dictionary mapping song names to URLs, e.g.:
```python
music = {
    "songname": "https://youtube.com/..."
}
```

> Note: API keys (Groq, NewsAPI) are hardcoded directly in the script for local testing convenience. Replace them with your own keys before running.

## Status

Actively in development — wake-word detection, web/music/news commands, and AI fallback responses are all functional. Planned improvements include better wake-word accuracy and expanding the command set.

## Why I Built This

to gain experience of api and other functions
