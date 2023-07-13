import pyttsx3

# initialisieren des TTS-Moduls
engine = pyttsx3.init()

# Konfiguration von Geschwindigkeit und Lautstärke
engine.setProperty('rate', 225)  # Geschwindigkeit auf 150 WPM setzen
engine.setProperty('volume', 1.0)  # Lautstärke auf 70% setzen

# Text, der vorgelesen werden soll
text = "Hallo, ich bin ein Text, der vorgelesen wird."

# Vorlesen des Textes
engine.say(text)
engine.runAndWait()
