import threading
import keyboard
import pygame


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

    def stop_audio():
        print("Abgebrochen")
        pygame.mixer.music.stop()

    keyboard.add_hotkey('esc', stop_audio)
    keyboard.add_hotkey('space', startStopp)
    keyboard.wait('esc')


def start_audio():
    audio_process = threading.Thread(
        target=play_audio, args=("./outputFolder/audio.mp3",))
    audio_process.start()
    play_process = threading.Thread(target=check_space_key)
    play_process.start()


start_audio()
