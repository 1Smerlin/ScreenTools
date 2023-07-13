import threading
import keyboard
import tkinter as tk


def menuWindow():
    print("!!!menuWindow!!!")
    root = tk.Tk()
    root.title("Screenshot")
    root.geometry("200x200")
    root.wm_attributes("-topmost", 1)
    root.mainloop()


def menu():
    print("menu")
    menu_thread = threading.Thread(target=menuWindow)
    menu_thread.start()


def keyShot():
    keyboard.add_hotkey("space", menu)
    keyboard.wait("esc")


keyboard_thread = threading.Thread(target=keyShot)
keyboard_thread.start()
