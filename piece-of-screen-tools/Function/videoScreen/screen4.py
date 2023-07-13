import cv2
import numpy as np
import pyautogui
import time

# Aufnahmezeit in Sekunden
aufnahmezeit = 5

# FPS der Aufnahme
aufnahme_fps = 1

# Bildschirmauflösung
screen = (1920, 1080)

# Anzahl der aufzunehmenden Frames berechnen
aufnahme_frames = aufnahmezeit * aufnahme_fps

# VideoWriter initialisieren
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter("output.mp4", fourcc, aufnahme_fps, screen)

# Startzeit für die Aufnahme speichern
start_time = time.time()

# Aufnahme starten
for i in range(aufnahme_frames):
    # Screenshot aufnehmen
    img = pyautogui.screenshot()

    # Bild in NumPy-Array umwandeln
    frame = np.array(img)

    # Farbkanäle umwandeln, damit sie von OpenCV erkannt werden
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Frame in VideoWriter schreiben
    output.write(frame)

# VideoWriter freigeben
output.release()
# Zeit für die Aufnahme berechnen und ausgeben
aufnahme_zeit = time.time() - start_time
print("Das {} Sekunden Video wurde {} Sekunden aufgenommen.".format(
    aufnahmezeit, aufnahme_zeit))
if aufnahmezeit == aufnahme_zeit:
    print("Die Aufnahmezeit und die Ausgabezeit sind gleich.")
else:
    print("Die Aufnahmezeit und die Ausgabezeit sind nicht gleich.")
