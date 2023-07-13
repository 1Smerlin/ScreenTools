import os
import ctypes
import keyboard
import sys

# folderContent = ['.env', 'Alternate Select.ani', 'bigblueset.crs', 'Blue Cursor (Original).ani', 'Blue Cursor Busy.ani', 'Blue Cursor Help.ani', 'Blue Cursor Timer.ani', 'Blue Link Select.ani', 'Blue Rock On.cur', 'Busy.ani', 'chroma-shadow.crs', 'Diagonal Resize 1.ani', 'Diagonal Resize 2.ani', 'dirRead.py', 'Electric Link Select lila.ani',
#  'finishMausBack.py', 'finishMausColor copy.py', 'Handwriting.cur', 'Help Select.ani', 'Horizontal Resize.ani', 'Link Select.ani', 'Move.ani', 'Normal Select.ani', 'Precision Select.ani', 'purple electric.ani', 'Purple text electric', 'testMausColor.py', 'Text Select.ani', 'Unavailable.ani', 'Verticle Resize.ani', 'Working in Background.ani']
filterFileTyp = ["py", "env", "crs"]
file_list = []


def imgListe():
    folderOutput = []
    for name in os.listdir("."):
        # vollständiger Pfad zur Datei
        file_path = os.path.join(os.getcwd(), name)

        if os.path.isfile(file_path):
            # Überprüfen des Dateityps
            if not any(file_path.endswith(f'.{fileTyp}') for fileTyp in filterFileTyp):
                folderOutput.append(name)
    return folderOutput


file_list = imgListe()

print(file_list)
print(len(file_list))


notiz = []
file = 0


def mousDefaultColor():
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    SPI_SETCURSORS = 0x0057
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    try:
        if not user32.SystemParametersInfoW(SPI_SETCURSORS, 0, None, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE):
            print("Fehler beim Zurücksetzen des Mauszeigers:",
                  ctypes.get_last_error(), file=sys.stderr)
    except FileNotFoundError:
        print("Mous back to old color will ABFUCKEN")


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


def notieren(file_list, file):
    print(f"{file_list[file]} wird eingespeichert")
    notiz.append(file_list[file])


def allNotiz():
    print("Interesant")
    print(notiz)


def changemous(file_list, file):
    try:
        print(f"{file}. {file_list[file]}")
        changeMouseColor(file_list[file])
    except FileExistsError:
        print(f"{file_list[file]} ist kein bild")


def up():
    global file
    global file_list
    file_list = imgListe()
    if not file == len(file_list)-1:
        print("up")
        file += 1
        changemous(file_list, file)


def down():
    global file
    global file_list
    file_list = imgListe()
    if not file == 0:
        print("down")
        file -= 1
        changemous(file_list, file)


changemous(file_list, file)
keyboard.add_hotkey("up", lambda: up())
keyboard.add_hotkey("down", lambda: down())
keyboard.add_hotkey("space", lambda: notieren(file_list, file))
keyboard.add_hotkey("c", lambda: allNotiz())


keyboard.wait("esc")
mousDefaultColor()
