# Screenshot Import
import mss
import numpy as np
import mouse
import keyboard
import pyautogui
from tkinter import *
# Picture to Text Import
import pyttsx3
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
# Text to Speech Import

# Anwendungs Funktionen
# Picture to Text


def pictureToText(picture, savePfad="text.txt"):
    # Picture to Text Code
    image = cv2.imread(picture)
    global string
    string = pytesseract.image_to_string(image)

    # Öffnen der Datei im Schreibmodus
    file = open(savePfad, "w")

    # Schreiben des Textes in die Datei
    file.write(string)

    # Schließen der Datei
    file.close()

# Text to Speech


def textToSpeech(textPfad, speed=200, sound=0.25, Komma=10, punkt=10, fragen=10):
    # Text to Speech Code
    # Text zum Sprechen geben
    textFile = open(textPfad, 'r')
    text = textFile.read()
    textFile.close()

    # Erstelle ein Text-to-Speech-Engine-Objekt
    engine = pyttsx3.init()

    # Passe die Einstellungen an
    # Holen Sie sich die aktuelle Lesegeschwindigkeit
    rate = engine.getProperty('rate')
    # Setzen Sie eine neue, niedrigere Lesegeschwindigkeit
    engine.setProperty('rate', rate - speed)

    # Holen Sie sich die aktuelle Lautstärke
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + sound)  # Erhöhen Sie die Lautstärke

    # Festlegen der Satzzeichen-Pausenzeit
    # Verkürzen Sie die Pause nach einem Komma um 50 Millisekunden
    engine.setProperty('comma', Komma)
    # Verkürzen Sie die Pause nach einem Punkt um 50 Millisekunden
    engine.setProperty('fullstop', punkt)
    # Verkürzen Sie die Pause nach einem Fragezeichen um 50 Millisekunden
    engine.setProperty('question', fragen)

    engine.say(text)

    # Sprache ausgeben
    engine.runAndWait()


def openText(textPfad):
    # Funktion, um den Textinhalt der Datei zu lesen
    def read_file(filename):
        with open(filename, 'r') as file:
            return file.read()

    # Fenster erstellen
    textWindow = Tk()
    textWindow.title("Dateiinhalt anzeigen")
    textWindow.wm_attributes("-topmost", 1)

    # Text Widget erstellen
    text_widget = Text(textWindow)
    text_widget.pack(fill="both", expand=True)

    # Dateiinhalt lesen und im Text Widget anzeigen
    filename = "text.txt"  # hier den Dateinamen angeben
    text = read_file(filename)
    text_widget.insert("1.0", text)

    # Fenster öffnen
    textWindow.mainloop()


# piece of screen
mausOutput = True


def on_mouse_down():
    print(pyautogui.position())
    pos = pyautogui.position()
    global kordinaten
    global screen
    kordinaten = [pos[0], pos[1]]
    global mausOutput
    if pos.x >= 0:
        screen = 2
    else:
        screen = 1
    mouse.unhook(down)


def on_mouse_up():
    print(pyautogui.position())
    pos = pyautogui.position()
    global kordinaten
    kordinaten.append(pos[0])
    kordinaten.append(pos[1])
    global mausOutput
    mausOutput = False
    mouse.unhook(up)

# ready-made options
# Screenshot of a specific area


def mausScreen():
    global down
    global up
    global mausOutput
    down = mouse.on_button(on_mouse_down, buttons=("left",), types=("down",))
    up = mouse.on_button(on_mouse_up, buttons=("left",), types=("up",))
    print(mausOutput)
    while mausOutput:
        pass
    mausOutput = True
    screenShot(screen, kordinaten)


# Screenshot
def screenShot(bildschirm, kordinaten=None):
    with mss.mss() as sct:
        # get information from monitor 1
        monitor_number = bildschirm
        mon = sct.monitors[monitor_number]
        if kordinaten is None:
            monitor = {
                "top": mon["top"],
                "left": mon["left"],
                "width": mon["width"],
                "height": mon["height"],
                "mon": monitor_number,
            }
        else:
            if kordinaten[0] > kordinaten[2]:
                kordinaten[0], kordinaten[2] = kordinaten[2], kordinaten[0]
            if kordinaten[1] > kordinaten[3]:
                kordinaten[1], kordinaten[3] = kordinaten[3], kordinaten[1]
            monitor = {
                "top": kordinaten[1],
                "left": kordinaten[0],
                "width": kordinaten[2]-kordinaten[0],
                "height": kordinaten[3]-kordinaten[1],
                "mon": monitor_number,
            }
    print("top:", monitor["top"])
    print("left:", monitor["left"])
    print("width:", monitor["width"])
    print("height:", monitor["height"])
    print("mon:", monitor["mon"])

    # grab the data
    sct_img = sct.grab(monitor)
    img = np.array(sct_img)

    # save the picture as PNG file
    cv2.imwrite("screenshot.png", img)


# Screenshot from screen 1


def screen1():
    screenShot(1)

# Screenshot from screen 2


def screen2():
    screenShot(2)


# Menu
def menu():
    print("menu")
    # Erstelle das Hauptfenster
    root = Tk()
    root.title("Screenshot")
    root.geometry("200x550+0+0")
    root.wm_attributes("-topmost", 1)

    # Erstelle eine Liste, in der die Buttons gespeichert werden sollen
    button_list = []

    # Schleife über die Button-Namen, um jeden Button zu erstellen
    global button_name

    def button_clicked(button_name):
        if button_name == 'Cut Screen':
            print("Cut Screen: "+button_name)
            mausScreen()
        elif button_name == 'Screen 1':
            print("Screen 1: "+button_name)
            screen1()
        elif button_name == 'Screen 2':
            print("Screen 2: "+button_name)
            screen2()
        elif button_name == 'Text':
            print("Text: "+button_name)
            mausScreen()
            pictureToText("./screenshot.png")
            openText("text.txt")
        elif button_name == 'Read aloud':
            print("Read aloud: "+button_name)
            mausScreen()
            pictureToText("./screenshot.png")
            textToSpeech("text.txt")

    for i, button_name in enumerate(["Cut Screen", "Screen 1", "Screen 2", "Text", "Read aloud"]):
        # Erstelle einen Button mit dem gegebenen Namen
        button = Button(root, text=button_name, width=25, height=5,
                        command=lambda name=button_name: button_clicked(name))
        # Füge den Button der Liste hinzu
        button_list.append(button)
        # Positioniere den Button in der i-ten Zeile und der 0-ten Spalte
        button.grid(row=i, column=0, padx=10, pady=10)
    # Starte die Hauptereignisschleife, um das Fenster anzuzeigen
    root.mainloop()


# hotkeys
keyboard.add_hotkey('alt+q', menu)
keyboard.wait()
# root.destroy() Scliest das fenster
