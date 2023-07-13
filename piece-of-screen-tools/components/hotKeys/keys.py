import keyboard

while True:
    try:
        # Die folgende Funktion blockiert den Code, bis eine Taste gedrückt wird.
        # Sobald eine Taste gedrückt wird, gibt die Funktion die gedrückte Taste zurück.
        # Wenn eine Tastenkombination gedrückt wird, wird die Taste als "Strg + Alt + T" zurückgegeben.
        key = keyboard.read_event().name

        # Gib die gedrückte Taste auf der Konsole aus
        print("Gedrückte Taste: ", key)

    except KeyboardInterrupt:
        # Wenn der Benutzer "Strg + C" drückt, wird die Schleife beendet
        break
