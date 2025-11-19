

# ✅ **Neue README.md**

```md
# ACE-R – Continuous Music Generator  
### Add-on für ACE-Step (KI-Musikrenderer) – inkl. automatischen Lyrics per ChatGPT

ACE-R ist ein Erweiterungs-Addon für die KI-Musiksoftware **ACE-Step**.  
Es generiert **endlos Musik in einer Schleife**, speichert jede fertige WAV-Datei im `songs/`-Ordner und spielt diese anschließend automatisch über einen separaten, asynchronen WAV-Player ab.

Zusätzlich erzeugt ACE-R automatisch **Songtexte per KI (g4f → ChatGPT-4-mini / o4-mini)**, basierend auf zufällig gewählten Hook-Wörtern aus Wordlists.

---

## 🚀 Funktionsübersicht

### 🎵 **1. Continuous Renderer (ACE-R)**
- rendert automatisch Songs durch:
  - zufälliges Genre  
  - zufällige Instrument-Kombination  
  - zufällige Features  
  - zufällige Stimmwahl (male/female)  
  - optional Drums  
- erzeugt vollständige Prompt-Dateien im Ordner `songs/`
- erzeugt automatisch Liedtexte (Lyrics) über ChatGPT (g4f)  
- nutzt ACE-Step-KI-Modell zum Musikrendern  
- speichert WAV-Dateien fortlaufend als Loop  
- Seed, Prompt, Lyrics und Metadaten pro Song werden gespeichert
- benötigt GPU (empfohlen RTX 3060 oder besser)

### ▶️ **2. Asynchroner WAV-Player**
- überwacht den `songs/`-Ordner in Echtzeit (Watchdog)
- sobald eine neue WAV vollständig gespeichert wurde:
  → wird sie automatisch abgespielt  
- unterstützt:
  - float32 WAV  
  - Stereo  
  - große Dateien  
- spielt Songs vollständig ab und nimmt automatisch die nächste Datei
- blockiert das Rendern nicht – beide Prozesse sind getrennt

---

## 📦 Installation

### 1️⃣ Python installieren  
Empfohlen: **Python 3.10.10 (64-bit)**  
Bitte in einer **virtuellen Umgebung**.

### 2️⃣ ACE-Step installieren  
ACE-R funktioniert **nur** wenn ACE-Step bereits korrekt installiert ist:

👉 ACE-Step Repository  
https://github.com/ace-step/ACE-Step

ACHTUNG:  
- Inferenzmodelle müssen vollständig installiert sein  
- GPU-Support (CUDA) wird benötigt

### 3️⃣ ACE-R in ACE-Step kopieren  
Das gesamte ACE-R Repository wird direkt in das Hauptverzeichnis von ACE-Step kopiert – neben `pipeline_ace_step.py`.

### 4️⃣ Python-Abhängigkeiten installieren  
```

pip install -r requirements.txt

```

---

## ▶️ Starten

### 1. Haupt-Renderer starten:
```

python "ACE-R Continuous Music Generator.py"

```

Der Renderer:
- startet den **WAV-Player automatisch** in einem zweiten Fenster  
- lädt das Modell  
- generiert zufällige Prompts  
- erzeugt Lyrics  
- rendert WAVs fortlaufend  
- legt alles in `songs/` ab  

### 2. WAV-Player  
Startet automatisch.  
Läuft völlig unabhängig weiter.

Beenden:  
Im Player-Fenster `q` drücken.

---

## 🧠 KI-Funktionen

### 🎤 AI-Lyrics Generator
ACE-R erzeugt jedes Mal neue Lyrics über ChatGPT (g4f):

- 3:30 min Länge  
- englischer Text  
- Hook basiert auf zufälligem Wordlist-Eintrag  
- Struktur: `[verse1]`, `[verse2]`, `[bridge]`, `[chorus]`, `[intro]`, `[outro]`

Falls g4f nicht erreichbar ist → Fallback-Lyrics werden automatisch verwendet.

### 🎛 Automatische Prompt-Generierung  
ACE-R mischt zufällig:
- Genre  
- Instrument  
- Feature  
- Male/Female-Voice  
- Drums On/Off  

Diese Prompts steuern das Musikmodell von ACE-Step.

---

## 🗂 Verzeichnisstruktur

```

ACE-R/
│
├── ACE-R Continuous Music Generator.py   # Haupt-Renderer
├── wav_player.py                         # Asynchroner WAV-Player
├── wordlist/                             # Zufallswortlisten
│   ├── hooks.txt
│   ├── genre.txt
│   ├── instruments.txt
│   └── features.txt
└── songs/                                # Automatisch generierte WAVs & Metadaten

```

---

## ⚙️ Systemanforderungen

- Windows 10/11  
- NVIDIA GPU (RTX 3060 mit 12 GB funktioniert gut)  
- CUDA-fähige ACE-Step-Installation  
- Internetverbindung für AI-Lyrics (optional)

---

## 🧑‍💻 Entwickler

**Author:** Hermann Knopp  
**Kontakt:** hermann.knopp@gmx.at  
**Status:** Early Alpha 0.1a

---

## 🐞 Fehler / Support
Bitte Issues direkt im GitHub-Repository melden.

Danke fürs Testen und viel Spaß beim Generieren deiner eigenen endlosen KI-Musik!  
```

---

# ✅ **requirements.txt**

Basierend auf deinem Code, ohne überflüssige Pakete:

```txt
click
pygetwindow
g4f==0.6.2.8
sounddevice
soundfile
numpy
watchdog
```

Zusätzlich werden ACE-Step-Module benötigt (lokal installiert):

```txt
acestep @ file:.
```

Optional (je nach ACE-Step Setup):

```txt
torch
```

