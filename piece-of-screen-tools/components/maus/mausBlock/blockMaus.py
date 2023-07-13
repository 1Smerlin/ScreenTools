import pyautogui
import tkinter as tk

# Erstelle ein Fenster
mausWindow = tk.Tk()

# Entferne das Standard-Window-Manager-Menü
mausWindow.overrideredirect(True)

# Setze die Fenstergröße
mausWindow.geometry("0x0")

# Setze den Alphawert des Fensters auf 0.5
mausWindow.attributes('-alpha', 0.5)

# Funktion, die die Mausposition überwacht und das Fenster entsprechend positioniert


def follow_mouse():
    # Aktuelle Position der Maus abrufen
    x, y = pyautogui.position()

    # Überprüfen, ob sich die Position geändert hat
    if x != mausWindow.winfo_x() or y != mausWindow.winfo_y():
        # Fensterposition aktualisieren
        mausWindow.geometry(f"1000x1000+{x-500}+{y-500}")

    # Schleife mit der after()-Methode von Tkinter alle 10 Millisekunden wiederholen
    mausWindow.after(10, follow_mouse)

# Funktion zum Beenden des Programms


def on_key_press(event):
    if event.keysym == 'Escape':
        mausWindow.quit()


# Escape-Taste an on_key_press-Funktion binden
mausWindow.bind('<Escape>', on_key_press)

# Funktion starten
follow_mouse()

# Starte die Haupt-Schleife des Fensters
mausWindow.mainloop()
