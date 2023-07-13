import os
import pyttsx3


def textFilter(text):
    text = text.replace("\n", " ")
    while "  " in text:
        text = text.replace("  ", " ")
    return text


def textToSpeech(textPfad, rate=225, volume=2):
    engine = pyttsx3.init()
    if os.path.exists(textPfad):
        textFile = open(textPfad, 'r')
        text = textFile.read()
        textFile.close()
    text = filter(text)

    engine.setProperty('rate', rate)

    engine.setProperty('volume', volume)
    engine.say(text)

    engine.runAndWait()


textToSpeech("./outputFolder/text.txt")
