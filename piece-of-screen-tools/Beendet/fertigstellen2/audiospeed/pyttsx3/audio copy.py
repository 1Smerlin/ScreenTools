import pyttsx3
import os
import keyboard
import threading

engine = None


def textToSpeech(engine, textPfad, rate=200, volume=2):
    if os.path.exists(textPfad):
        textFile = open(textPfad, 'r')
        text = textFile.read()
        textFile.close()

        engine = pyttsx3.init()

        engine.setProperty('rate', rate)

        engine.setProperty('volume', volume)

        def onWord(name, location, length):
            print('word', name, location, length)
            if keyboard.is_pressed("esc"):
                engine.stop()

            engine.connect('started-word', onWord)

        onWord()
        engine.say(text)

        engine.runAndWait()


textToSpeech(engine, "./outputFolder/textOutputOrginal.txt")

# def stopp(engine):
#     print("Stopp")
#     engine.endLoop()


# def keyslisten(engine):
#     keyboard.add_hotkey("space", lambda: stopp(engine))


# engine = pyttsx3.init()
# keythread = threading.Thread(target=keyslisten, args=(engine,))
# keythread.start()
# audiothread = threading.Thread(target=textToSpeech, args=(
#     engine, "./outputFolder/textOutputOrginal.txt", 200, 2))
# audiothread.start()
