import keyboard
import pygame


def play_audio(audio_file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()


play_audio("./outputFolder/audio.mp3",)
keyboard.wait('esc')
