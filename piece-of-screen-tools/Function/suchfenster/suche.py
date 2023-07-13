from tkinter import Tk
from tkinter.filedialog import askopenfilename


def select_file():
    Tk().withdraw()  # Dies versteckt das Hauptfenster von Tkinter
    filename = (
        askopenfilename()
    )  # Öffnet den Datei-Explorer und gibt den Pfad der ausgewählten Datei zurück
    return filename


# Verwendung der Funktion
selected_file = select_file()
print(f"Sie haben die Datei {selected_file} ausgewählt.")
