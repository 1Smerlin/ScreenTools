import tkinter as tk

# Erstellen Sie das Tkinter-Fenster
root = tk.Tk()

# root.overrideredirect(True)
root.geometry("100x100+100+100")
# Setzen Sie die Transparenz auf 50%
root.attributes('-alpha', 0.5)

# Fügen Sie einige Widgets hinzu, um zu demonstrieren, dass sie ebenfalls transparent sind
label = tk.Label(root, text="Hallo, Welt!")
label.pack()

# Starten Sie die Tkinter-Schleife
root.mainloop()
