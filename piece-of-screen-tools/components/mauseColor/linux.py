import os
import sys
import time
from Xlib import X, display
from Xlib.protocol import rq
from PIL import Image

os.system("clear")

def change_mouse_color(pfad):
    print("!!!---changeMouseColor---!!!")
    cursor_file = os.path.abspath(pfad)
    print("!!!---Test---!!!")
    print("!!!cursor_file!!!")
    print(cursor_file)
    disp = display.Display()
    print("!!!disp!!!")
    print(disp)
    cursor = create_cursor_from_file(disp, cursor_file)
    print("!!!cursor!!!")
    print(cursor)

    for screen in range(disp.screen_count()):
        root = disp.screen(screen).root
        root.change_attributes(cursor=cursor)

    disp.sync()


def create_cursor_from_file(disp, cursor_file):
    with Image.open(cursor_file) as im:
        width, height = im.size
        hotspot_x, hotspot_y = 0, 0
        screen = disp.screen()
        pixmap = screen.root.create_pixmap(width, height, screen.root_depth)
        gc = pixmap.create_gc()
        gc.foreground = screen.white_pixel
        gc.background = screen.black_pixel
        pixmap.put_image(gc, X.ZPixmap, 0, 0, 0, 0, width, height, im.tobytes())

        print("!!!screen.root!!!")
        print(screen.root)
        print("!!!pixmap!!!")
        print(pixmap)
        print("!!!pixmap!!!")
        print(pixmap)
        print("!!!screen.black_pixel!!!")
        print(screen.black_pixel)
        print("!!!screen.white_pixel!!!")
        print(screen.white_pixel)
        print("!!!hotspot_x!!!")
        print(hotspot_x)
        print("!!!hotspot_y!!!")
        print(hotspot_y)
        cursor = disp.create_cursor(pixmap, pixmap, screen.black_pixel, screen.white_pixel, hotspot_x, hotspot_y)
        print("!!!---Ende---!!!")
        pixmap.free()

    return cursor

# change_mouse_color("./png/Normal_Select.cursor")
change_mouse_color("./png/Normal_Select.png")
