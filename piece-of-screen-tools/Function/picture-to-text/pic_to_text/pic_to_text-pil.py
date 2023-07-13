import pytesseract
import numpy as np
from PIL import Image

# Picture to Text


def pic_to_text(pic, savePfad="text.txt"):
    # Picture to Text Code
    image = np.array(Image.open(pic))
    global string
    string = pytesseract.image_to_string(image)

    # Öffnen der Datei im Schreibmodus
    file = open(savePfad, "w")

    # Schreiben des Textes in die Datei
    file.write(string)

    # Schließen der Datei
    file.close()


pic_to_text("./test.png", "pil.txt")
