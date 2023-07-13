from gtts import gTTS


def create_audio_file(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    tts = gTTS(text=text, lang="de")
    tts.save("output_audio.mp3")


create_audio_file("./textOutput.txt")
