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

# Variablen
window_open = multiprocessing.Value("b", False)
command_queue = multiprocessing.Queue()
status_queue = multiprocessing.Queue()


def existFolder():
    if not os.path.exists("./outputFolder"):
        os.makedirs("./outputFolder")


# Funtionen
# Screenshot


def screenShot(bildschirm, kordinaten=None):
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
    pil_img.save('./outputFolder/screenshot.png')

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

# Text to Audio


def create_audio_file(file_path="./outputFolder/text.txt", savePfad="./outputFolder/audio.mp3"):
    with open(file_path, "r") as file:
        text = file.read()
    tts = gTTS(text=text, lang="de")
    tts.save(savePfad)

# Play the Audio


def play_audio(audio_file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()


def check_space_key():
    def startStopp():
        if pygame.mixer.music.get_busy():
            print("Pause")
            pygame.mixer.music.pause()
        else:
            print("Weiter")
            pygame.mixer.music.unpause()
            pygame.time.Clock().tick(10)

    def stop_audio():
        print("Abgebrochen")
        pygame.mixer.music.stop()

    keyboard.add_hotkey('esc', stop_audio)
    keyboard.add_hotkey('space', startStopp)
    keyboard.wait('esc')


def start_audio():
    audio_process = threading.Thread(
        target=play_audio, args=("./outputFolder/audio.mp3",))
    audio_process.start()
    play_process = threading.Thread(target=check_space_key)
    play_process.start()


# screencut
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
    print(screenKordinate)
    mouse.unhook_all()
    blockWindow.destroy()


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


# Ausführung

def button_clicked(button_name, window_open, command_queue, status_queue):
    numberOfScreens = len(mss.mss().monitors) - 1
    if button_name == 'cut Screen':
        print('cut Screen: '+button_name)
        if window_open.value:
            command_queue.put("close")
            blockScreen()
            status = status_queue.get()
            if status == "closed":
                screenShot(1, screenKordinate)
                menu_process = multiprocessing.Process(
                    target=menuWindow, args=(window_open, command_queue, status_queue))
                menu_process.start()
        else:
            screenShot(1, screenKordinate)
    elif button_name == 'Text':
        print('Text: '+button_name)
        if window_open.value:
            command_queue.put("close")
            blockScreen()
            status = status_queue.get()
            if status == "closed":
                screenShot(1, screenKordinate)
                menu_process = multiprocessing.Process(
                    target=menuWindow, args=(window_open, command_queue, status_queue))
                menu_process.start()
        else:
            screenShot(1, screenKordinate)
        pic_to_text()
        openText()
    elif button_name == 'Read':
        print('Read: ' + button_name)
        if window_open.value:
            command_queue.put("close")
            blockScreen()
            status = status_queue.get()
            if status == "closed":
                screenShot(1, screenKordinate)
                pic_to_text()
                create_audio_file()
                startaudio_process = multiprocessing.Process(
                    target=start_audio)
                startaudio_process.start()
                menu_process = multiprocessing.Process(
                    target=menuWindow, args=(window_open, command_queue, status_queue))
                menu_process.start()
        else:
            screenShot(1, screenKordinate)
            pic_to_text()
            create_audio_file()
            startaudio_process = multiprocessing.Process(
                target=start_audio)
            startaudio_process.start()
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
                            target=menuWindow, args=(window_open, command_queue, status_queue))
                        menu_process.start()
                else:
                    screenShot(i)


def fuctionStart(button_name, window_open, command_queue, status_queue):
    function_process = multiprocessing.Process(
        target=button_clicked, args=(button_name, window_open, command_queue, status_queue))
    function_process.start()


# Menu
def menuWindow(window_open, command_queue, status_queue):
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
                           command=lambda name=button_name: fuctionStart(name, window_open, command_queue, status_queue))
        button_list.append(button)
        button.grid(row=i, column=0, padx=10, pady=10)
    for i in range(numberOfScreen):
        button = tk.Button(root, text="Screen "+str(i+1), width=25, height=5,
                           command=lambda name="Screen "+str(i+1): fuctionStart(name, window_open, command_queue, status_queue))
        button.grid(row=i+3, column=0, padx=10, pady=10)
    button = tk.Button(root, text="Folder", width=25, height=5,
                       command=lambda name="Folder": fuctionStart(name, window_open, command_queue, status_queue))
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


def menu(window_open, command_queue, status_queue):
    with window_open.get_lock():
        if not window_open.value:  # Überprüfen, ob das Fenster bereits geöffnet ist
            print("menu")
            menu_process = multiprocessing.Process(
                target=menuWindow, args=(window_open, command_queue, status_queue))
            menu_process.start()
        else:
            # Sende eine Nachricht zum Schließen des Fensters
            command_queue.put("close")


def allClose(window_open, command_queue):
    with window_open.get_lock():
        if window_open.value:
            command_queue.put("close")


def keyShot(window_open, command_queue, status_queue):
    keyboard.add_hotkey("alt+q", lambda: menu(window_open,
                        command_queue, status_queue))
    # Füge eine neue Tastenkombination hinzu, um die Anzahl der aktiven Prozesse auszugeben
    keyboard.add_hotkey("p", print_active_processes)
    # keyboard.add_hotkey("esc", lambda: allClose(
    #     window_open, command_queue))
    # keyboard.wait("esc")
    keyboard.wait()


def print_active_processes():
    active_processes = multiprocessing.active_children()
    print(f"Anzahl der aktiven Prozesse: {len(active_processes)}")


if __name__ == "__main__":
    existFolder()
    keyShot_process = multiprocessing.Process(
        target=keyShot, args=(window_open, command_queue, status_queue))
    keyShot_process.start()
    keyShot_process.join()
