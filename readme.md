
# ACE-R – Continuous Music Generator

### Add-on for ACE-Step (AI Music Rendering) – with Automatic ChatGPT Lyrics

ACE-R is an addon for the **ACE-Step** AI music software.
It generates **endless music in a continuous loop**, saving each finished WAV file into the `songs/` folder, while a separate asynchronous WAV player automatically plays every new track.

Additionally, ACE-R creates **song lyrics via AI** (g4f → ChatGPT-4 / gpt-4), based on randomly selected hook words from built-in wordlists.

---

## 🚀 Features

### 🎵 **1. Continuous Music Renderer (ACE-R)**

* automatic song generation using:

  * random genre
  * random instruments
  * random musical features
  * random male/female voice selection
  * optional drum track
* automatically creates prompt text files in `songs/`
* auto-generates lyrics via ChatGPT using g4f
* uses ACE-Step's inference model for music rendering
* saves WAV files sequentially, without user interaction
* stores metadata, prompt and lyrics for each song
* optimized for GPU rendering (recommended: RTX 3060 or better)

---

### ▶️ **2. Asynchronous WAV Player**

* monitors the `songs/` folder in real time (via Watchdog)
* plays new WAV files as soon as they have fully finished rendering
* supports:

  * float32 WAV
  * stereo
  * very large audio files
* playback will never block rendering:
  Renderer and Player run independently.

---

## 📦 Installation

### 1️⃣ Install Python

Recommended: **Python 3.10.10 (64-bit)**
Use a **virtual environment**.

### 2️⃣ Install ACE-Step

ACE-R requires a complete ACE-Step installation:

👉 ACE-Step Repository
[https://github.com/ace-step/ACE-Step](https://github.com/ace-step/ACE-Step)

ACE-Step must be installed fully, including inference models.
GPU support (CUDA) is recommended for real-time generation.

### 3️⃣ Install ACE-R

Copy the **ACE-R repository** into the *root directory* of ACE-Step —
next to `pipeline_ace_step.py`.

### 4️⃣ Install Python dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running ACE-R

### Start the main renderer:

```
python "ACE-R Continuous Music Generator.py"
```

What happens:

* starts the **WAV Player** automatically in a new window
* loads the ACE-Step model
* generates random prompts
* generates lyrics
* renders WAV files endlessly
* stores everything inside `songs/`

### WAV Player

Starts automatically.
Runs independently in its own terminal window.

To stop playback:
In the player window press: **q**

---

## 🧠 AI Features

### 🎤 **AI Lyric Generator**

ACE-R generates new lyrics for every track using ChatGPT (via g4f):

* English lyrics
* approx. 3:30 minutes length
* structure uses:
  `[intro]`, `[verse1]`, `[verse2]`, `[bridge]`, `[chorus]`, `[outro]`
* hook word is randomly selected from wordlists

If ChatGPT/g4f is unavailable → a fallback lyric is used automatically.

---

### 🎛 **Automatic Prompt Creation**

ACE-R randomly mixes:

* Genre
* Instrument
* Musical feature
* Male/Female voice
* Drums yes/no

The final prompt controls the ACE-Step AI music generation pipeline.

---

## 🗂 Directory Structure

```
ACE-R/
│
├── ACE-R Continuous Music Generator.py   # Main renderer
├── wav_player.py                         # Asynchronous WAV player
├── wordlist/                             # Wordlists for prompt generation
│   ├── hooks.txt
│   ├── genre.txt
│   ├── instruments.txt
│   └── features.txt
└── songs/                                # Auto-generated songs + metadata
```

---

## Update ACE-R to Version 2 with new g4f Provider "WeWordle"


ACE-R with old g4f Provider is not working anymore.
g4f Library has changed and provider "PolliantionAi" is now Payware.

Please update g4f to Version 6.8.2

with: pip install g4f==6.8.2 -U

the new Version 2.0 from ACE-R has another g4f provider "WeWordle"
with the Model "gpt-4" and is working again.
this Version has a little fix for nasty ChatGPT-Comments in the Lyrics.
the code in "test-provider.py" can check if internet and g4f provider
is valid.

please try out and comment other bugs and issues.
thanks.




---

## ⚙️ System Requirements

* Windows 10/11
* NVIDIA GPU recommended (RTX 3060 12GB works well)
* Full ACE-Step installation
* Internet connection required for AI lyrics (optional)

---

## 👤 Author

**Hermann Knopp**
Contact: [hermann.knopp@gmx.at](mailto:hermann.knopp@gmx.at)
Status: Early Alpha 0.1a

---

## 🐞 Issues / Support

Please open a GitHub Issue for bugs, errors, or feature requests.

Enjoy creating infinite AI-generated music! 🎶
