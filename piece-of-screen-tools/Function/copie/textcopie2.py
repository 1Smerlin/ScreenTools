import pyperclip


def textCopie(text):
    pyperclip.copy(text)
    print("Der Text wurde in die Zwischenablage kopiert: " + pyperclip.paste())


textCopie("Dies ist der Text, der in die Zwischenablage kopiert wird.")
