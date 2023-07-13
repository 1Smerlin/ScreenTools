import os
import ctypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

IDC_ARROW = 32512


def save_original_cursor():
    h_cursor = user32.LoadCursorW(None, IDC_ARROW)
    user32.CopyImage.argtypes = [
        ctypes.wintypes.HANDLE, ctypes.wintypes.UINT, ctypes.c_int, ctypes.c_int, ctypes.wintypes.UINT]
    h_original_cursor = user32.CopyImage(h_cursor, 2, 0, 0, 0)
    return h_original_cursor


original_cursor = save_original_cursor()
