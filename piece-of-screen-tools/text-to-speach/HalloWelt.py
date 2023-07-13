import pyttsx3

# Initialisiere den pyttsx3-Engine
engine = pyttsx3.init()

# Abfrage der installierten Stimmen
voices = engine.getProperty('voices')

# Wählen Sie die erste verfügbare Stimme aus
engine.setProperty('voice', voices[0].id)

# Sprechen Sie den Text "Hallo Welt" aus
engine.say("Hallo Welt, ich heiße merlin")
engine.runAndWait()
