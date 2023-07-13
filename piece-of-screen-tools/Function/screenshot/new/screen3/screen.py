from mss import mss
from PIL import Image

# Erstellen Sie eine Instanz von mss
sct = mss()

# Definiere den Bereich für den Screenshot (left, top, width, height)
# region = {"top": 0, "left": 0, "width": 5000, "height": 1000}
region = {'left': 2044, 'top': 332, 'width': 371, 'height': 85}


# Einen Screenshot eines spezifischen Bereichs erstellen

print("!!!!!Test!!!!!")
print("monitor")
print(region)
screenshot = sct.grab(region)

# Den Screenshot in einer Datei speichern
Image.frombytes('RGB', screenshot.size, screenshot.bgra, 'raw', 'BGRX').save('screenshot.png')
