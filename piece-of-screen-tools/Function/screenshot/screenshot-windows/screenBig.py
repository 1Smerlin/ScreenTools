# Öffnet Fenster mit option zum screenshot und öffnet das bild direkt

from tkinter import *
import pyautogui
import time


root = Tk()
root.geometry("800x500")


def take_screenshot(screen_number):
    screen_size = pyautogui.size()
    width = int(screen_size.width / num_screens)
    x = screen_number * width
    im = pyautogui.screenshot(region=(x, 0, width, screen_size.height))
    im.show()


def take_screenshot_with_mouse():
    time.sleep(5)
    start_pos = pyautogui.position()
    end_pos = pyautogui.position()
    left = min(start_pos[0], end_pos[0])
    top = min(start_pos[1], end_pos[1])
    width = abs(start_pos[0] - end_pos[0])
    height = abs(start_pos[1] - end_pos[1])
    im = pyautogui.screenshot(region=(left, top, width, height))
    im.show()


# Is there an whether multiple screens are connected
num_screens = len(pyautogui.screenshot().size)
screen_buttons = []
for i in range(num_screens):
    screen_button = Button(
        root, text=f"Screen {i+1}", width=20, height=5, command=lambda i=i: take_screenshot(i))
    screen_buttons.append(screen_button)

mouse_button = Button(root, text="Maus", width=20, height=5,
                      command=take_screenshot_with_mouse)

for i, button in enumerate(screen_buttons):
    button.grid(row=0, column=i, padx=50, pady=50)

mouse_button.grid(row=1, column=0, padx=50, pady=50)

root.mainloop()
