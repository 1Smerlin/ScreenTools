import pyperclip

# Lese den Inhalt der Zwischenablage
text = pyperclip.paste()

# Gib den Inhalt der Zwischenablage aus
print("Inhalt der Zwischenablage: " + text)

# Füge den Inhalt der Zwischenablage zu einer Liste hinzu
my_list = []
my_list.append(text)
