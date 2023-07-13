import pyttsx3

# Initialisiere den pyttsx3-Engine
engine = pyttsx3.init()

# Abfrage der installierten Stimmen
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.name)
