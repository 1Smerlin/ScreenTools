import keyboard


def sag():
    print("hallo mei BUUUU")


keyboard.add_hotkey('space', sag)
# wait for hotkeys
keyboard.wait("esc")
