# Gibt auf der console die position in der ich die maus gedrückt habe
import mouse

print("Bereit zur Aufzeichnung")

screenKordinate = {}


def on_mouse_down():
    print("!!!on_mouse_down!!!")
    global start_x, start_y
    start_x, start_y = mouse.get_position()


def on_mouse_up():
    print("!!!on_mouse_up!!!")
    global end_x, end_y
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


mouse.on_button(on_mouse_down, buttons=("left",), types=("down",))
mouse.on_button(on_mouse_up, buttons=("left",), types=("up",))

while True:
    pass
