import os
import sys
import time
from Xlib import X, display
from Xlib.protocol import rq
from PIL import Image

os.system("clear")

def create_cursor_from_file(cursor_file):
    im = Image.open(cursor_file)
    width, height = im.size
    hotspot_x, hotspot_y = width // 2, height // 2

    pixmap = disp.create_pixmap(width, height, screen.root_depth)
    gc = pixmap.create_gc()
    pixmap.put_image(gc, 0, 0, 0, 0, width, height, im.tobytes())

    color_fg = screen.black_pixel
    color_bg = screen.white_pixel

    cursor = disp.create_cursor(pixmap, pixmap, color_fg, color_bg, hotspot_x, hotspot_y)
    return cursor
