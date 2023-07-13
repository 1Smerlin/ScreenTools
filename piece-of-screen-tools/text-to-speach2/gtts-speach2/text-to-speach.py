from gtts import gTTS
import pygame

language = "de"
tts = gTTS(text="Hallo Welt, abonnier mich!",
           lang=language,
           slow=False)
tts.speed = 10

tts.save("./audio/tts.mp3")

pygame.mixer.init()
pygame.mixer.music.load("./audio/tts.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
