# Gibt auf der console die position in der ich die maus gedrückt habe
import mouse

print("Bereit zur Aufzeichnung")

start_x, start_y = None, None


def on_mouse_down():
    global start_x, start_y
    if start_x is None and start_y is None:
        start_x, start_y = mouse.get_position()
        print(f"Die Maus wurde bei x={start_x}, y={start_y} gedrückt.")


def on_mouse_up():
    global start_x, start_y
    if start_x is not None and start_y is not None:
        end_x, end_y = mouse.get_position()
        print(f"Die Maus wurde bei x={end_x}, y={end_y} losgelassen.")
        start_x, start_y = None, None


mouse.on_button(on_mouse_down, buttons=("left",), types=("down",))
# mouse.on_button(on_mouse_up, buttons=("left",), types=("up",))

while True:
    pass
