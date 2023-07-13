import ctypes
import sys
import time
import os
import subprocess
import multiprocessing
import threading
import keyboard
import mouse
import tkinter as tk
import mss
import numpy as np
import pytesseract
from PIL import Image
from gtts import gTTS
import pygame
import pyttsx3

# Variablen
window_open = multiprocessing.Value("b", False)
command_queue = multiprocessing.Queue()
status_queue = multiprocessing.Queue()
block_queue = multiprocessing.Queue()
screenKordinate_queue = multiprocessing.Queue()


def existFolder():
    if not os.path.exists("./outputFolder"):
        os.makedirs("./outputFolder")
    if not os.path.exists("./img"):
        os.makedirs("./img")


def textFilter(text):
    text = text.replace("\n", " ")
    while "  " in text:
        text = text.replace("  ", " ")
    return text

# Funtionen
# Screenshot


def screenShot(bildschirm, kordinaten=None, save='./outputFolder/screenshot.png'):
    existFolder()
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
    sct_img = sct.grab(monitor)
    img = np.array(sct_img)

    # Konvertieren des Numpy-Arrays in ein Bildobjekt
    pil_img = Image.fromarray(img)

    # Speichern des Bildobjekts als PNG-Datei
    pil_img.save(save)

    # save the picture as PNG file
    # cv2.imwrite("./outputFolder/screenshot.png", img)


# Picture to Text
def pic_to_text(pic='./outputFolder/screenshot.png', savePfad="./outputFolder/text.txt"):
    # Picture to Text Code
    image = np.array(Image.open(pic))
    global string
    string = pytesseract.image_to_string(image)

    # Öffnen der Datei im Schreibmodus
    file = open(savePfad, "w")

    # Schreiben des Textes in die Datei
    file.write(string)

    # Schließen der Datei
    file.close()


# Open text
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

# Text to Speech


def textToSpeech(textPfad, rate=225, volume=2):
    engine = pyttsx3.init()
    if os.path.exists(textPfad):
        textFile = open(textPfad, 'r')
        text = textFile.read()
        textFile.close()
    text = textFilter(text)

    engine.setProperty('rate', rate)

    engine.setProperty('volume', volume)
    engine.say(text)

    engine.runAndWait()


# screencut


def changeMouseColor():
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    # Definieren der Konstanten
    IMAGE_CURSOR = 2
    LR_LOADFROMFILE = 0x00000010
    IDC_ARROW = 32512

    def set_cursor(cursor_file):
        h_cursor = user32.LoadImageW(
            0, cursor_file, IMAGE_CURSOR, 0, 0, LR_LOADFROMFILE)
        user32.SetSystemCursor(h_cursor, IDC_ARROW)

    cursor_file = os.path.abspath("./img/Normal_Select.ani")
    set_cursor(cursor_file)


def mousDefaultColor():
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    SPI_SETCURSORS = 0x0057
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    try:
        if not user32.SystemParametersInfoW(SPI_SETCURSORS, 0, None, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE):
            print("Fehler beim Zurücksetzen des Mauszeigers:",
                  ctypes.get_last_error(), file=sys.stderr)
    except FileNotFoundError:
        print("Mous back to old color will ABFUCKEN")


screenKordinate = {}
end_x, end_y = 0, 0
start_x, start_y = 0, 0


def on_mouse_down():
    print("!!!on_mouse_down!!!")
    global start_x, start_y
    start_x, start_y = mouse.get_position()
    print(start_x, start_y)


def on_mouse_up():
    global block_queue, screenKordinate_queue
    print("!!!on_mouse_up!!!")
    global end_x, end_y
    global start_x, start_y
    global screenKordinate
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
    mousDefault_process = multiprocessing.Process(target=mousDefaultColor)
    mousDefault_process.start()
    print(start_x, start_y)
    print(end_x, end_y)
    print("screenKordinate")
    print(screenKordinate)
    screenKordinate_queue.put(screenKordinate)
    mouse.unhook_all()
    print("hallo1")
    block_queue.put("close")
    print("hallo2")


def blockScreen():
    global block_queue

    def block_close():
        blockWindow.destroy()

    screenSize = mss.mss().monitors[0]
    blockWindow = tk.Tk()
    blockWindow.overrideredirect(True)
    blockWindow.geometry(
        f"{screenSize['width']}x{screenSize['height']}+{screenSize['left']}+{screenSize['top']}")

    blockWindow.protocol("WM_DELETE_WINDOW", block_close)
    blockWindow.wm_attributes("-topmost", 1)

    blockWindow.attributes('-alpha', 0.5)
    while True:
        try:
            message = block_queue.get_nowait()
            if message == "close":
                break
        except multiprocessing.queues.Empty:
            pass
        blockWindow.update_idletasks()
        blockWindow.update()


def mousKordinate():
    print("!!!mousKordinate!!!")
    blockScreen_process = multiprocessing.Process(
        target=blockScreen, args=(block_queue,))
    blockScreen_process.start()
    changeMouse_process = multiprocessing.Process(target=changeMouseColor)
    changeMouse_process.start()
    time.sleep(10)
    mouse.on_button(lambda: on_mouse_down(),
                    buttons=("left",), types=("down",))
    mouse.on_button(lambda: on_mouse_up(),
                    buttons=("left",), types=("up",))


# Ausführung

def button_clicked(button_name):
    global window_open, command_queue, status_queue, screenKordinate_queue
    numberOfScreens = len(mss.mss().monitors) - 1
    if button_name == 'cut Screen':
        print('cut Screen: '+button_name)
        if window_open.value:
            command_queue.put("close")
            mousKordinate()
            screenKordinate = screenKordinate_queue.get()
            print("screenKordinate")
            print(screenKordinate)
            if not screenKordinate["width"] == 0 and not screenKordinate["height"] == 0:
                status = status_queue.get()
                if status == "closed":
                    screenShot(1, screenKordinate)
                    menu_process = multiprocessing.Process(
                        target=menuWindow)
                    menu_process.start()
        else:
            mousKordinate()
            screenKordinate = screenKordinate_queue.get()
            print("screenKordinate")
            print(screenKordinate)
            if not screenKordinate["width"] == 0 and not screenKordinate["height"] == 0:
                screenShot(1, screenKordinate)
    elif button_name == 'Text':
        print('Text: '+button_name)
        if window_open.value:
            command_queue.put("close")
            mousKordinate()
            screenKordinate = screenKordinate_queue.get()
            print("screenKordinate")
            print(screenKordinate)
            if not screenKordinate["width"] == 0 and not screenKordinate["height"] == 0:
                status = status_queue.get()
                if status == "closed":
                    screenShot(1, screenKordinate)
                    menu_process = multiprocessing.Process(
                        target=menuWindow)
                    menu_process.start()
        else:
            mousKordinate()
            screenKordinate = screenKordinate_queue.get()
            print("screenKordinate")
            print(screenKordinate)
            if not screenKordinate["width"] == 0 and not screenKordinate["height"] == 0:
                screenShot(1, screenKordinate)
        if not screenKordinate["width"] == 0 and not screenKordinate["height"] == 0:
            pic_to_text()
            openText()
    elif button_name == 'Read':
        print('Read: ' + button_name)
        if window_open.value:
            command_queue.put("close")
            mousKordinate()
            screenKordinate = screenKordinate_queue.get()
            print("screenKordinate")
            print(screenKordinate)
            if not screenKordinate["width"] == 0 and not screenKordinate["height"] == 0:
                status = status_queue.get()
                if status == "closed":
                    screenShot(1, screenKordinate)
                    pic_to_text()
                    speach_process = multiprocessing.Process(
                        target=textToSpeech, args=("./outputFolder/text.txt",))
                    speach_process.start()
                    menu_process = multiprocessing.Process(
                        target=menuWindow)
                    menu_process.start()
        else:
            mousKordinate()
            screenKordinate = screenKordinate_queue.get()
            print("screenKordinate")
            print(screenKordinate)
            if not screenKordinate["width"] == 0 and not screenKordinate["height"] == 0:
                screenShot(1, screenKordinate)
                pic_to_text()
                speach_process = multiprocessing.Process(
                    target=textToSpeech, args=("./outputFolder/text.txt",))
                speach_process.start()
    elif button_name == 'Folder':
        print('Folder: ' + button_name)
        existFolder()
        subprocess.run(['explorer', os.path.abspath("./outputFolder")])
    else:
        for i in range(1, numberOfScreens + 1):
            if button_name == f'Screen {i}':
                print(f'Screen {i}: {button_name}')
                if window_open.value:
                    command_queue.put("close")
                    status = status_queue.get()
                    if status == "closed":
                        screenShot(i)
                        menu_process = multiprocessing.Process(
                            target=menuWindow)
                        menu_process.start()
                else:
                    screenShot(i)


def fuctionStart(button_name):
    function_process = multiprocessing.Process(
        target=button_clicked, args=(button_name,))
    function_process.start()


# Menu
def menuWindow():
    global window_open, status_queue, command_queue

    def on_close():
        nonlocal root
        with window_open.get_lock():
            window_open.value = False
        root.destroy()
        time.sleep(0.2)
        status_queue.put("closed")

    print("!!!menuWindow!!!")
    with window_open.get_lock():
        window_open.value = True
    numberOfScreen = len(mss.mss().monitors) - 1
    root = tk.Tk()
    root.title("Screenshot")
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.wm_attributes("-topmost", 1)

    button_list = []

    for i, button_name in enumerate(["cut Screen", "Text", "Read"]):
        button = tk.Button(root, text=button_name, width=25, height=5,
                           command=lambda name=button_name: fuctionStart(name))
        button_list.append(button)
        button.grid(row=i, column=0, padx=10, pady=10)
    for i in range(numberOfScreen):
        button = tk.Button(root, text="Screen "+str(i+1), width=25, height=5,
                           command=lambda name="Screen "+str(i+1): fuctionStart(name))
        button.grid(row=i+3, column=0, padx=10, pady=10)
    button = tk.Button(root, text="Folder", width=25, height=5,
                       command=lambda name="Folder": fuctionStart(name))
    button.grid(row=i+4, column=0, padx=10, pady=10)
    root.update_idletasks()
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+10+10")
    while window_open.value:
        try:
            message = command_queue.get_nowait()
            if message == "close":
                on_close()
                break
        except multiprocessing.queues.Empty:
            root.update_idletasks()
            root.update()


def menu():
    global window_open
    with window_open.get_lock():
        if not window_open.value:  # Überprüfen, ob das Fenster bereits geöffnet ist
            print("menu")
            menu_process = multiprocessing.Process(
                target=menuWindow)
            menu_process.start()
        else:
            # Sende eine Nachricht zum Schließen des Fensters
            command_queue.put("close")


def allClose(window_open, command_queue):
    with window_open.get_lock():
        if window_open.value:
            command_queue.put("close")


def button_process(name):
    button_clicked_process = multiprocessing.Process(
        target=button_clicked, args=(name,))
    button_clicked_process.start()


def test():
    global window_open
    print("TEST")
    print(window_open.get_lock())


def keyShot():
    numberOfScreen = len(mss.mss().monitors) - 1
    keyboard.add_hotkey("alt+q", lambda: menu())
    keyboard.add_hotkey("alt+x", lambda: button_process("cut Screen",))
    keyboard.add_hotkey("alt+c", lambda: button_process("Text",))
    keyboard.add_hotkey("alt+v", lambda: button_process("Read",))
    keyboard.add_hotkey("alt+y", lambda: button_process("Folder",))
    keyboard.add_hotkey("p", lambda: test())
    screenKeys = ""
    for i in range(numberOfScreen):
        code = f"keyboard.add_hotkey('alt+{i+1}', lambda: button_process('Screen {i+1}',))"
        screenKeys += code + "\n"
    exec(screenKeys)
    keyboard.wait()


def print_active_processes():
    active_processes = multiprocessing.active_children()
    print(f"Anzahl der aktiven Prozesse: {len(active_processes)}")


if __name__ == "__main__":
    existFolder()
    keyShot_process = multiprocessing.Process(
        target=keyShot)
    keyShot_process.start()
    keyShot_process.join()
