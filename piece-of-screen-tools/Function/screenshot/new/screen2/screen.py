from mss import mss
from PIL import Image

# Erstellen Sie eine Instanz von mss
sct = mss()

# Liste aller Monitore bekommen
monitors = sct.monitors

# Prüfen ob mehr als ein Monitor vorhanden ist
if len(monitors) > 1:
    # Zweiten Monitor auswählen
    monitor = monitors[0]

    # Einen Screenshot eines spezifischen Bereichs (des gesamten zweiten Monitors) erstellen
    screenshot = sct.grab(monitor)

    # Den Screenshot in einer Datei speichern
    Image.frombytes('RGB', screenshot.size, screenshot.bgra, 'raw', 'BGRX').save('screenshot.png')
else:
    print("Es ist nur ein Monitor angeschlossen.")
