import time
import os
import subprocess
import mss
import keyboard
import tkinter as tk
import mouse
import numpy as np
import cv2
import pyttsx3
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Screenshot

if not os.path.exists("./outputFolder"):
    os.makedirs("./outputFolder")


def screenShot(bildschirm, kordinaten=None):
    print("!!!screenShot!!!")
    if os.path.exists("./outputFolder/screenshot.png"):
        os.remove("./outputFolder/screenshot.png")
    try:
        global root
        if root:
            if root.winfo_exists():
                root.destroy()
                time.sleep(0.5)
    except:
        pass
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
            monitor = kordinaten
            monitor["mon"] = monitor_number
    print("top:", monitor["top"])
    print("left:", monitor["left"])
    print("width:", monitor["width"])
    print("height:", monitor["height"])
    print("mon:", monitor["mon"])
    # grab the data
    if 'kordinaten' in locals():
        if monitor["height"] > 0 and monitor["width"] > 0:
            sct_img = sct.grab(monitor)
            img = np.array(sct_img)
            # save the picture as PNG file
            cv2.imwrite("./outputFolder/screenshot.png", img)
    else:
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)
        # save the picture as PNG file
        cv2.imwrite("./outputFolder/screenshot.png", img)

# Picture to text


def pic_to_text(picPfad):
    # read the picture
    print("pic_to_text")
    if os.path.exists("./outputFolder/text.txt"):
        os.remove("./outputFolder/text.txt")
    if os.path.exists(picPfad):
        image = cv2.imread(picPfad)
        string = pytesseract.image_to_string(image)

        #  write the text
        with open("./outputFolder/text.txt", "w") as file:
            file.write(string)

# Outepute Text

# Text to Speech


def textToSpeech(textPfad, rate=200, volume=2):
    if os.path.exists(textPfad):
        textFile = open(textPfad, 'r')
        text = textFile.read()
        textFile.close()

        engine = pyttsx3.init()

        engine.setProperty('rate', rate)

        engine.setProperty('volume', volume)
        engine.say(text)

        engine.runAndWait()


def openText(textPfad="./outputFolder/text.txt"):
    # Funktion, um den Textinhalt der Datei zu lesen
    if os.path.exists(textPfad):
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


# Maus cotrolle
screenKordinate = {}


def on_mouse_down():
    print("!!!on_mouse_down!!!")
    global start_x, start_y
    start_x, start_y = mouse.get_position()


def on_mouse_up():
    print("!!!on_mouse_up!!!")
    global blockWindow
    global end_x, end_y
    global start_x, start_y
    global screenKordinate
    global root
    end_x, end_y = mouse.get_position()
    if start_x < end_x:
        screenKordinate["left"] = start_x
    else:
        screenKordinate["left"] = end_x
    if start_y < end_y:
        screenKordinate["top"] = start_y
    else:
        screenKordinate["top"] = end_y
    screenKordinate["width"] = abs(start_x - end_x)
    screenKordinate["height"] = abs(start_y - end_y)
    mouse.unhook_all()
    blockWindow.destroy()
    root.destroy()


def blockScreen():
    print("!!!blockScreen!!!")
    global blockWindow
    global screenKordinate
    screenSize = mss.mss().monitors[0]
    blockWindow = tk.Tk()
    blockWindow.overrideredirect(True)
    blockWindow.geometry(
        f"{screenSize['width']}x{screenSize['height']}+{screenSize['left']}+{screenSize['top']}")

    blockWindow.attributes('-alpha', 0.01)

    mouse.on_button(on_mouse_down, buttons=("left",), types=("down",))
    mouse.on_button(on_mouse_up, buttons=("left",), types=("up",))

    blockWindow.mainloop()

# Menu


def controlleWindow():
    print("!!!controlleWindow!!!")
    numberOfScreen = len(mss.mss().monitors) - 1
    global root
    root = tk.Tk()
    root.title("Screenshot")
    # root.geometry(f"200x{108*(numberOfScreen+4)}+0+0")
    root.wm_attributes("-topmost", 1)

    button_list = []

    def button_clicked(button_name):
        global screenKordinate
        numberOfScreens = len(mss.mss().monitors) - 1
        if button_name == 'cut Screen':
            print('cut Screen: '+button_name)
            blockScreen()
            screenShot(1, screenKordinate)
            controlleWindow()
        elif button_name == 'Text':
            print('Text: '+button_name)
            blockScreen()
            screenShot(1, screenKordinate)
            pic_to_text("./outputFolder/screenshot.png")
            openText()
            controlleWindow()
        elif button_name == 'Read':
            print('Read: ' + button_name)
            blockScreen()
            screenShot(1, screenKordinate)
            pic_to_text("./outputFolder/screenshot.png")
            textToSpeech("./outputFolder/text.txt")
            controlleWindow()
        elif button_name == 'Folder':
            print('Folder: ' + button_name)
            subprocess.run(['explorer', os.path.abspath("./outputFolder")])
        else:
            for i in range(1, numberOfScreens + 1):
                if button_name == f'Screen {i}':
                    print(f'Screen {i}: {button_name}')
                    screenShot(i)
                    controlleWindow()
                    break

    for i, button_name in enumerate(["cut Screen", "Text", "Read"]):
        button = tk.Button(root, text=button_name, width=25, height=5,
                           command=lambda name=button_name: button_clicked(name))
        button_list.append(button)
        button.grid(row=i, column=0, padx=10, pady=10)
    for i in range(numberOfScreen):
        button = tk.Button(root, text="Screen "+str(i+1), width=25, height=5,
                           command=lambda name="Screen "+str(i+1): button_clicked(name))
        button.grid(row=i+3, column=0, padx=10, pady=10)
    button = tk.Button(root, text="Folder", width=25, height=5,
                       command=lambda name="Folder": button_clicked(name))
    button.grid(row=i+4, column=0, padx=10, pady=10)
    root.update_idletasks()
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+10+10")
    # keyboard.add_hotkey('alt+x', button_clicked('Text'))
    try:
        root.mainloop()
    except:
        pass


keyboard.add_hotkey('alt+q', controlleWindow)
# wait for hotkeys
keyboard.wait("esc")
