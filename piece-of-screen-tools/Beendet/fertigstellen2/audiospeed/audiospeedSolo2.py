import keyboard
from pydub import AudioSegment
from pydub.playback import play


def play_audio(audio_file_path, speed=1):
    audio = AudioSegment.from_file(audio_file_path, format="mp3")
    audio_with_speed = audio.speedup(playback_speed=speed)
    play(audio_with_speed)


play_audio("./outputFolder/audio.mp3", speed=1.5)
keyboard.wait('esc')
