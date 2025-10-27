import os

import time
import threading
import queue
import sounddevice as sd
import soundfile as sf
import numpy as np
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ======================================
# Einstellungen
# ======================================

dir_path = os.path.dirname(os.path.realpath(__file__))

# if songs not here , error wil thrown
WATCH_FOLDER = dir_path + "\\songs"  # <-- Anpassen!
STOP_KEY = "q"  # Taste zum Stoppen

#-----------Not used today -----------------------------------
# Wait Playing vor File created
def wait_for_file(filepath, min_size=1024, timeout=5):
    """
    Wartet, bis die Datei existiert und mindestens `min_size` Bytes groß ist.
    Timeout in Sekunden.
    """
    waited = 0
    while not os.path.exists(filepath) or os.path.getsize(filepath) < min_size:
        time.sleep(0.1)
        waited += 0.1
        if waited >= timeout:
            raise FileNotFoundError(f"File not found or too small: {filepath}")
    return True

#----------End -------------------------------------------------




#-----use this routine instead------------------------------------------


def wait_for_file_complete(filepath, min_size=1024, check_interval=0.1, timeout=10):
    """
    Wartet, bis die Datei existiert, größer als min_size ist
    und die Größe sich über 2 Intervalle nicht mehr ändert.
    """
    start_time = time.time()
    last_size = -1

    while True:
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            if size >= min_size:
                if size == last_size:
                    return True  # Datei fertig
                last_size = size
        if time.time() - start_time > timeout:
            raise FileNotFoundError(f"File not found or too small: {filepath}")
        time.sleep(check_interval)




# ======================================
# Playlist-Verwaltung
# ======================================
class AudioQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.stop_flag = threading.Event()

    def add_file(self, filepath):
        if filepath.lower().endswith(".wav"):
            print(f"[+] Neue Audiodatei erkannt: {os.path.basename(filepath)}")
            self.queue.put(filepath)

    def get_next(self):
        return self.queue.get()


# ======================================
# Watchdog-Handler: erkennt neue WAVs
# ======================================
class WatchFolder(FileSystemEventHandler):
    def __init__(self, audio_queue):
        super().__init__()
        self.audio_queue = audio_queue

    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(".wav"):
            self.audio_queue.add_file(event.src_path)


# ======================================
# Audio-Wiedergabe-Thread
# ======================================
def audio_player(audio_queue: AudioQueue):
    print("[Player] Starte Wiedergabe-Thread...")

    while not audio_queue.stop_flag.is_set():
        try:
            next_file = audio_queue.get_next()
            print(f"[Player] Spiele: {os.path.basename(next_file)}")

            filepath=next_file

            # not used today
            #wait_for_file(filepath)

            # use this 
            wait_for_file_complete(filepath)


            #not used today
            # Prüfe auf wav mit daten
            #while os.path.getsize(os.path.basename(next_file)) < 1024:
            #    time.sleep(0.1)


            # Datei öffnen (SoundFile unterstützt Float & 32bit)
            data, samplerate = sf.read(next_file, dtype='float32', always_2d=True)

            # Wiedergabe starten
            sd.play(data, samplerate)

            # Warten bis fertig oder Stop
            while sd.get_stream().active:
                if audio_queue.stop_flag.is_set():
                    sd.stop()
                    break
                time.sleep(0.1)

            sd.stop()

        except Exception as e:
            print(f"[Fehler beim Abspielen von {next_file}]: {e}")
            time.sleep(1)

    print("[Player] Wiedergabe beendet.")


# ======================================
# Hauptprogramm
# ======================================
def main():
    print("=== Asynchroner WAV-Player (Float-WAV Support) ===")
    print(f"Überwache Ordner: {WATCH_FOLDER}")
    print(f"Drücke '{STOP_KEY}' zum Beenden.\n")

    # Queue + Watchdog initialisieren
    audio_queue = AudioQueue()
    event_handler = WatchFolder(audio_queue)
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    observer.start()

    # Vorhandene Dateien beim Start hinzufügen
    for f in sorted(os.listdir(WATCH_FOLDER)):
        if f.lower().endswith(".wav"):
            audio_queue.add_file(os.path.join(WATCH_FOLDER, f))

    # Player in separatem Thread starten
    player_thread = threading.Thread(target=audio_player, args=(audio_queue,), daemon=True)
    player_thread.start()

    # Auf Tastendruck warten
    try:
        while True:
            key = input().strip().lower()
            if key == STOP_KEY:
                print("[System] Stop-Befehl erkannt.")
                break
    except KeyboardInterrupt:
        pass

    # Stoppen
    audio_queue.stop_flag.set()
    sd.stop()
    observer.stop()
    observer.join()
    print("[System] Beendet.")


if __name__ == "__main__":

    # set size
    os.system("mode con: cols=80 lines=30")
    os.system("title Async WAV Player - FP32 Support")

    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Check and Create Songs Directory
    img_out_folder=""

    # Check for None String   
    if img_out_folder=="" or img_out_folder==None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = "songs"
        filepath= dir_path + "\\" + path
        img_out_folder=filepath
        print("Checking.. " + img_out_folder + " for saving Songs.")    

    # Check whether the specified path exists or not
    isExist = os.path.exists(img_out_folder)
    if not isExist:
   
        # Create a new directory because it does not exist
        os.makedirs(img_out_folder)
        print("The new directory " + img_out_folder + " is created!")   
        print("")
        print("I am using: "+img_out_folder+" for Songs saving")


    main()
