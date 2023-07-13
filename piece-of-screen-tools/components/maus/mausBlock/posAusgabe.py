import pyautogui
import keyboard

# Aktuelle Position der Maus abrufen und ausgeben
currentMouseX, currentMouseY = pyautogui.position()
print(f'Mausposition: X={currentMouseX} Y={currentMouseY}')

# Position der Maus in einer Schleife überwachen und ausgeben, wenn sie sich ändert
while True:
    # Aktuelle Position der Maus abrufen
    x, y = pyautogui.position()

    # Überprüfen, ob sich die Position geändert hat
    if x != currentMouseX or y != currentMouseY:
        # Position ausgeben
        print(f'Mausposition: X={x} Y={y}')

        # Aktuelle Position aktualisieren
        currentMouseX, currentMouseY = x, y

    # Auf Escape-Taste prüfen
    if keyboard.is_pressed('esc'):
        # Schleife beenden
        break
