import pyttsx3


def textToSpeech(textPfad, rate=200, volume=2):
    textFile = open(textPfad, 'r')
    text = textFile.read()
    textFile.close()

    engine = pyttsx3.init()

    engine.setProperty('rate', rate)

    engine.setProperty('volume', volume)
    engine.say(text)

    engine.runAndWait()


textToSpeech("./textOutput.txt")
# textToSpeech("laute.txt")
