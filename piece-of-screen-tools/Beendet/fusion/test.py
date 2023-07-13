import tkinter as tk
import pyautogui
import mouse

# Globale Variablen
down = None
up = None
kordinaten = []
screen = None
mausWindow = None
mausOutput = True


def follow_mouse():
    # Aktuelle Position der Maus abrufen
    x, y = pyautogui.position()

    # Überprüfen, ob sich die Position geändert hat
    if x != mausWindow.winfo_x() or y != mausWindow.winfo_y():
        # Fensterposition aktualisieren
        mausWindow.geometry(f"100x100+{x-50}+{y-50}")

    # Schleife mit der after()-Methode von Tkinter alle 10 Millisekunden wiederholen
    mausWindow.after(10, follow_mouse)


def on_mouse_down():
    global kordinaten
    global screen
    kordinaten = [pyautogui.position()[0], pyautogui.position()[1]]
    if pyautogui.position().x >= 0:
        screen = 2
    else:
        screen = 1
    global mausOutput
    blockMaus()
    mouse.unhook(down)


def on_mouse_up():
    global kordinaten
    kordinaten.append(pyautogui.position()[0])
    kordinaten.append(pyautogui.position()[1])
    global mausOutput
    mausOutput = False
    mausWindow.quit()
    mouse.unhook(up)


def blockMaus():
    global mausWindow
    # Erstelle ein Fenster
    mausWindow = tk.Tk()

    # Entferne das Standard-Window-Manager-Menü
    mausWindow.overrideredirect(True)

    # Setze die Fenstergröße
    mausWindow.geometry("0x0")

    # Setze den Alphawert des Fensters auf 0.5
    mausWindow.attributes('-alpha', 0.5)

    # Funktion, die die Mausposition überwacht und das Fenster entsprechend positioniert
    follow_mouse()

    # Starte die Haupt-Schleife des Fensters
    mausWindow.mainloop()


def record_mouse():
    global down
    global up
    blockMaus()
    down = mouse.on_button(on_mouse_down, buttons=("left",), types=("down",))
    up = mouse.on_button(on_mouse_up, buttons=("left",), types=("up",))

    while mausOutput:
        pass

    return kordinaten, screen
