import tkinter as tk
import mss


def openText(textPfad="text.txt"):
    # Funktion, um den Textinhalt der Datei zu lesen
    def read_file(filename):
        with open(filename, 'r') as file:
            return file.read()
    screenSize = mss.mss().monitors[2]
    # Fenster erstellen
    textWindow = tk.Tk()
    textWindow.title("Dateiinhalt anzeigen")
    textWindow.wm_attributes("-topmost", 1)
    width, height = 600, 300
    textWindow.geometry(
        f"{width}x{height}+{(screenSize['left']+screenSize['width']-width-10)}+{(screenSize['top']+screenSize['height']-height-30)}")
    print(screenSize)
    print(
        f"{width}x{height}+{(screenSize['left']+screenSize['width']-width-10)}+{(screenSize['top']+screenSize['height']-height-30)}")

    # Text Widget erstellen
    text_widget = tk.Text(textWindow)
    text_widget.pack(fill="both", expand=True)

    # Dateiinhalt lesen und im Text Widget anzeigen
    text = read_file(textPfad)
    text_widget.insert("1.0", text)

    # Fenster öffnen
    textWindow.mainloop()


openText("textOutput.txt")
