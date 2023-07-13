import multiprocessing
import keyboard
import tkinter as tk

window_open = multiprocessing.Value("b", False)


def menuWindow(window_open):
    print("!!!menuWindow!!!")
    with window_open.get_lock():
        window_open.value = True

    root = tk.Tk()
    root.title("Screenshot")
    root.geometry("200x200")
    root.wm_attributes("-topmost", 1)
    root.protocol("WM_DELETE_WINDOW", lambda: close_window(root, window_open))
    root.mainloop()


def close_window(root, window_open):
    with window_open.get_lock():
        window_open.value = False
    root.destroy()


def menu(window_open):
    with window_open.get_lock():
        if not window_open.value:
            print("menu")
            menu_process = multiprocessing.Process(
                target=menuWindow, args=(window_open,))
            menu_process.start()


def keyShot(window_open):
    keyboard.add_hotkey("space", lambda: menu(window_open))
    keyboard.wait("esc")


if __name__ == "__main__":
    keyShot_process = multiprocessing.Process(
        target=keyShot, args=(window_open,))
    keyShot_process.start()
    keyShot_process.join()
