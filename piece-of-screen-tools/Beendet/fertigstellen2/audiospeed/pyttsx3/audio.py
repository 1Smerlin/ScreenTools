import pyttsx3
import os
import keyboard
import threading

engine = pyttsx3.init()
stop_flag = False


def textToSpeech(engine, textPfad, rate=200, volume=2, chunk_size=50):
    global stop_flag
    if os.path.exists(textPfad):
        textFile = open(textPfad, 'r')
        text = textFile.read()
        textFile.close()

        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)

        words = text.split()
        for i in range(0, len(words), chunk_size):
            if stop_flag:
                break
            chunk = ' '.join(words[i:i+chunk_size])
            engine.say(chunk)
            engine.runAndWait()


def stopp():
    global stop_flag
    stop_flag = True
    print("Stopp")


def keyslisten():
    keyboard.add_hotkey("space", stopp)


keythread = threading.Thread(target=keyslisten)
keythread.start()

audiothread = threading.Thread(target=textToSpeech, args=(
    engine, "./outputFolder/textOutputOrginal.txt", 200, 2))
audiothread.start()
audiothread.join()
