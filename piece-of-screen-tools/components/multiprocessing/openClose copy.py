import multiprocessing
import keyboard
import tkinter as tk

window_open = multiprocessing.Value("b", False)
queue = multiprocessing.Queue()


def menuWindow(queue, window_open):
    def on_close():
        nonlocal root
        with window_open.get_lock():
            window_open.value = False
        root.destroy()

    print("!!!menuWindow!!!")
    with window_open.get_lock():
        window_open.value = True

    root = tk.Tk()
    root.title("Screenshot")
    root.geometry("200x200")
    root.wm_attributes("-topmost", 1)
    root.protocol("WM_DELETE_WINDOW", on_close)

    while window_open.value:
        try:
            message = queue.get_nowait()
            if message == "close":
                on_close()
                break
        except multiprocessing.queues.Empty:
            root.update_idletasks()
            root.update()


def menu(queue, window_open):
    with window_open.get_lock():
        if not window_open.value:
            print("menu")
            menu_process = multiprocessing.Process(
                target=menuWindow, args=(queue, window_open))
            menu_process.start()
        else:
            queue.put("close")


def keyShot(queue, window_open):
    keyboard.add_hotkey("space", lambda: menu(queue, window_open))
    keyboard.wait("esc")


if __name__ == "__main__":
    keyShot_process = multiprocessing.Process(
        target=keyShot, args=(queue, window_open))
    keyShot_process.start()
    keyShot_process.join()
