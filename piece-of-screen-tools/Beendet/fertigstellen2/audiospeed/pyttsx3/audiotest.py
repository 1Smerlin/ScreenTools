import pyttsx3
import keyboard

textFile = open("./outputFolder/textOutputOrginal.txt", 'r')
text = textFile.read()
textFile.close()


def onWord(name, location, length):
    if keyboard.is_pressed("esc"):
        print("Stopp")
        engine.stop()


engine = pyttsx3.init()
engine.connect('started-word', onWord)
engine.say(text)
engine.runAndWait()
