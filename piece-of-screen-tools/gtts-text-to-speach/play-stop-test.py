import pygame
import threading
import keyboard

# Global flag to control playback states


def play_audio(audio_file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()


def check_space_key():
    def startStopp():
        if pygame.mixer.music.get_busy():
            print("Pause")
            pygame.mixer.music.pause()
        else:
            print("Weiter")
            pygame.mixer.music.unpause()
            pygame.time.Clock().tick(10)
    keyboard.add_hotkey('space', startStopp)
    keyboard.wait("esc")


output_audio_path = "output_audio.mp3"

# Start the audio playback thread
audio_thread = threading.Thread(target=play_audio, args=(output_audio_path,))
audio_thread.start()

# Start the keyboard input checking thread
keyboard_thread = threading.Thread(target=check_space_key)
keyboard_thread.start()

# Wait for the audio thread to finish
audio_thread.join()
