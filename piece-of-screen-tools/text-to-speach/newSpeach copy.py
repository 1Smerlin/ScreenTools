import pyttsx3
from pynput import keyboard
import threading

pause_speech = threading.Event()


def on_press(key):
    if key == keyboard.Key.space:
        if pause_speech.is_set():
            pause_speech.clear()
        else:
            pause_speech.set()
        return False


def textToSpeech(textPfad, rate=200, volume=2):
    textFile = open(textPfad, 'r')
    text = textFile.read()
    textFile.close()

    engine = pyttsx3.init()

    engine.setProperty('rate', rate)

    engine.setProperty('volume', volume)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    for word in text.split():
        pause_speech.wait()
        engine.say(word)
        engine.runAndWait()

    listener.stop()


textToSpeech("./textOutput.txt")
