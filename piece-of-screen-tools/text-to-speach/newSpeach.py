import pyttsx3
from pynput import keyboard
import threading
import time

pause_speech = threading.Event()


def on_press(key):
    if key == keyboard.Key.space:
        if pause_speech.is_set():
            pause_speech.clear()
        else:
            pause_speech.set()
        return False


def speak_word(engine, word):
    engine.say(word)
    engine.runAndWait()


def textToSpeech(textPfad, rate=200, volume=2):
    textFile = open(textPfad, 'r')
    text = textFile.read()
    textFile.close()

    engine = pyttsx3.init()

    engine.setProperty('rate', rate)

    engine.setProperty('volume', volume)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    last_output_time = time.perf_counter()
    for word in text.split():
        pause_speech.wait()
        start_time = time.perf_counter()
        elapsed_time_since_last_output = start_time - last_output_time
        print(f"Anfang: {elapsed_time_since_last_output:.2f}")
        speak_word(engine, word)
        end_time = time.perf_counter()
        elapsed_time_since_last_output = end_time - start_time
        print(f"Ende: {elapsed_time_since_last_output:.2f}")
        last_output_time = end_time

    listener.stop()


textToSpeech("./textOutput.txt")
