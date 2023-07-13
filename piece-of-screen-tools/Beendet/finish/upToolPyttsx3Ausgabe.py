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
manager = multiprocessing.Manager()
window_open = manager.Value(bool, False)
command_queue = multiprocessing.Queue()
status_queue = multiprocessing.Queue()
block_queue = multiprocessing.Queue()
screenKordinate_queue = multiprocessing.Queue()


# Menu
def menuWindow():
    global window_open, status_queue, command_queue
    print(window_open)

    def on_close():
        nonlocal root
        with window_open.get_lock():
            window_open.value = False
        root.destroy()
        time.sleep(0.2)
        status_queue.put("closed")

    print(window_open.get_lock())
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


if __name__ == "__main__":
    # existFolder()
    keyShot_process = multiprocessing.Process(
        target=keyShot)
    keyShot_process.start()
    keyShot_process.join()
