from mss import mss
from PIL import Image

def screenShot(bildschirm, kordinaten=None, save='./screenshot.png'):
    # Erstellen Sie eine Instanz von mss
    sct = mss()
    # Definiere den Bereich für den Screenshot (left, top, width, height)
    # monitor = {"top": 0, "left": 0, "width": 5000, "height": 1000}
    # monitor = {'left': 2044, 'top': 332, 'width': 371, 'height': 85}

    mon = sct.monitors[bildschirm]
    if kordinaten is None:
        monitor = {
            "top": mon["top"],
            "left": mon["left"],
            "width": mon["width"],
            "height": mon["height"],
        }
    else:
        monitor = kordinaten
    
    
    # Einen Screenshot eines spezifischen Bereichs erstellen
    print("!!!!!Test!!!!!")
    print("monitor")
    print(monitor)
    screenshot = sct.grab(monitor)

    # Den Screenshot in einer Datei speichern
    Image.frombytes('RGB', screenshot.size, screenshot.bgra, 'raw', 'BGRX').save('screenshot.png')
# screenShot(1,{'left': 2044, 'top': 332, 'width': 371, 'height': 85})
screenShot(1)