import pyttsx3


def textToSpeech(textPfad, outputFile, rate=200, volume=0.25):
    # Text to Speech Code
    # Text zum Sprechen geben
    textFile = open(textPfad, 'r')
    text = textFile.read()
    textFile.close()

    # Erstelle ein Text-to-Speech-Engine-Objekt
    engine = pyttsx3.init()

    # Passe die Einstellungen an
    # Setzen Sie eine neue, niedrigere Lesegeschwindigkeit
    engine.setProperty('rate', rate)

    # Holen Sie sich die aktuelle Lautstärke
    engine.setProperty('volume', volume)  # Erhöhen Sie die Lautstärke

    # Sprache ausgeben
    engine.save_to_file(text, outputFile)
    engine.runAndWait()


textToSpeech("textOutput.txt", "output.mp3", 200, 2)
