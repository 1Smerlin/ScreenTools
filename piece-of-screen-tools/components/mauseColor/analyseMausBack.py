import ctypes
import sys


def mousDefaultColor():
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    SPI_SETCURSORS = 0x0057
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    print()
    if not user32.SystemParametersInfoW(SPI_SETCURSORS, 0, None, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE):
        print("Fehler beim Zurücksetzen des Mauszeigers:",
              ctypes.get_last_error(), file=sys.stderr)


mousDefaultColor()
