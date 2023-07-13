import mss
import tkinter as tk
import keyboard


def blockScreen(screenSize):
    # Erstelle ein Fenster
    blockWindow = tk.Tk()
    # Entferne das Standard-Window-Manager-Menü
    blockWindow.overrideredirect(True)
    print(screenSize["left"])
    print(screenSize["top"])
    print(screenSize["width"])
    print(screenSize["height"])

    # Setze die Fenstergröße
    blockWindow.geometry(
        f"{screenSize['width']}x{screenSize['height']}+{screenSize['left']}+{screenSize['top']}")
    # blockWindow.geometry("1680x1050+-1680+34")
    # blockWindow.geometry("1920x1080+0+0")

    # Setze den Alphawert des Fensters auf 0.5
    blockWindow.wm_attributes('-alpha', 0.5)

    def exit():
        blockWindow.destroy()

    keyboard.add_hotkey("esc", exit)

    # Starte die Haupt-Schleife des Fensters
    blockWindow.mainloop()


blockScreen(mss.mss().monitors[0])
# blockScreen("-1680", "0", "3600", "1084")
