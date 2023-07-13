import pygame
import threading
import keyboard

# Global flag to control playback state
pause_speech = False


def play_audio(audio_file_path):
    global pause_speech
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        if pause_speech:
            print("Pause")
            pygame.mixer.music.pause()
        else:
            print("Weiter")
            pygame.mixer.music.unpause()
        pygame.time.Clock().tick(10)


def check_space_key():
    global pause_speech
    while True:
        if keyboard.is_pressed('space'):
            pause_speech = not pause_speech
            # Wait for the space key to be released
            while keyboard.is_pressed('space'):
                pygame.time.delay(100)
        pygame.time.delay(100)


output_audio_path = "output_audio.mp3"

# Start the audio playback thread
audio_thread = threading.Thread(target=play_audio, args=(output_audio_path,))
audio_thread.start()

# Start the keyboard input checking thread
keyboard_thread = threading.Thread(target=check_space_key)
keyboard_thread.start()

# Wait for the audio thread to finish
audio_thread.join()
