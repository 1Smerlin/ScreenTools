from gtts import gTTS
from playsound import playsound

language = "de"
tts = gTTS(text="Hallo Welt, abonnier mich!",
           lang=language,
           slow=False)
tts.speed = 0.5  # Geschwindigkeit auf 150% erhöhen

# save to file
tts.save("./audio/tts.mp3")

# play from file
playsound("./audio/tts.mp3")
