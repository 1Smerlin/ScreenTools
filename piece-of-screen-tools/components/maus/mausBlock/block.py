from pynput import mouse
import keyboard

# Aktuelle Position der Maus abrufen und ausgeben
currentMouseX, currentMouseY = mouse.Controller().position
print(f'Mausposition: X={currentMouseX} Y={currentMouseY}')

# Position der Maus in einer Schleife überwachen und ausgeben, wenn sie sich ändert


def on_move(x, y):
    global currentMouseX, currentMouseY
    # Überprüfen, ob sich die Position geändert hat
    if x != currentMouseX or y != currentMouseY:
        # Position ausgeben
        print(f'Mausposition: X={x} Y={y}')

        # Aktuelle Position aktualisieren
        currentMouseX, currentMouseY = x, y

# Auf linke Maustaste prüfen


def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        # Programm beenden
        return False


# Maus-Events registrieren
with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
    # Auf Escape-Taste prüfen
    while not keyboard.is_pressed('esc'):
        pass
