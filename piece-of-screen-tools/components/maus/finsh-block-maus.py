import mss
import tkinter as tk
import keyboard
import mouse


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
    blockWindow.destroy()


def blockScreen():
    global blockWindow
    global screenKordinate
    screenSize = mss.mss().monitors[0]
    blockWindow = tk.Tk()
    blockWindow.overrideredirect(True)
    blockWindow.geometry(
        f"{screenSize['width']}x{screenSize['height']}+{screenSize['left']}+{screenSize['top']}")

    blockWindow.attributes('-alpha', 0.5)

    mouse.on_button(on_mouse_down, buttons=("left",), types=("down",))
    mouse.on_button(on_mouse_up, buttons=("left",), types=("up",))

    blockWindow.mainloop()
    print(screenKordinate)


blockScreen()

keyboard.wait("esc")
