from gtts import gTTS
import os


def text_to_wav(text, filename):
    # Text in Sprache umwandeln
    tts = gTTS(text=text, lang='de')

    # Temporäre MP3-Datei speichern
    temp_mp3 = "temp.mp3"
    tts.save(temp_mp3)

    # MP3-Datei in WAV-Datei konvertieren
    mp3_to_wav(temp_mp3, filename)

    # Temporäre MP3-Datei löschen
    os.remove(temp_mp3)


def mp3_to_wav(mp3_file, wav_file):
    from pydub import AudioSegment

    # MP3-Datei laden
    audio = AudioSegment.from_mp3(mp3_file)

    # Audio in WAV-Format konvertieren und speichern
    audio.export(wav_file, format="wav")


if __name__ == "__main__":
    text = "Hallo, ich bin ein Text-zu-Sprache-Beispiel."
    output_wav = "output.wav"

    text_to_wav(text, output_wav)
    print(f"Text wurde in die WAV-Datei '{output_wav}' umgewandelt.")
