import os
import time
from gtts import gTTS
import pygame
from pynput import keyboard

pygame.mixer.init()


def speak_text(text, audio_file_path):
    tts = gTTS(text=text, lang="de")
    tts.save(audio_file_path)

    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)


def read_file(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    return text


def on_press(key):
    if key == keyboard.Key.space:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()


text_path = "./textOutput.txt"
text = read_file(text_path)

current_directory = os.path.dirname(os.path.abspath(__file__))
audio_file_path = os.path.join(current_directory, "temp_audio.mp3")

listener = keyboard.Listener(on_press=on_press)
listener.start()

speak_text(text, audio_file_path)

listener.stop()

os.remove(audio_file_path)
