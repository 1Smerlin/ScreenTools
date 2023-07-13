import os
import ctypes


def changeMouseColor(pfad):
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    # Definieren der Konstanten
    IMAGE_CURSOR = 2
    LR_LOADFROMFILE = 0x00000010
    IDC_ARROW = 32512

    def set_cursor(cursor_file):
        h_cursor = user32.LoadImageW(
            0, cursor_file, IMAGE_CURSOR, 0, 0, LR_LOADFROMFILE)
        user32.SetSystemCursor(h_cursor, IDC_ARROW)

    cursor_file = os.path.abspath(pfad)
    set_cursor(cursor_file)


changeMouseColor("Normal_Select.ani")
