from gtts import gTTS


def create_audio_file(file_path="./outputFolder/text.txt", savePfad="./outputFolder/audio.mp3"):
    with open(file_path, "r") as file:
        text = file.read()
    tts = gTTS(text=text, lang="de")
    tts.save(savePfad)


create_audio_file()
