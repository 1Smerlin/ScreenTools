import tkinter as tk
import mss

# def menuWindow(numberOfScreen):


def button_clicked(button_name):
    numberOfScreens = len(mss.mss().monitors) - 1
    if button_name == 'cut Screen':
        print('cut Screen: '+button_name)
    elif button_name == 'Text':
        print('Text: '+button_name)
    elif button_name == 'Read':
        print('Read: ' + button_name)
    elif button_name == 'Folder':
        print('Folder: ' + button_name)
    else:
        for i in range(1, numberOfScreens + 1):
            if button_name == f'Screen {i}':
                print(f'Screen {i}: {button_name}')


# Menu
def menuWindow():
    def on_close():
        nonlocal root
        root.destroy()

    print("!!!menuWindow!!!")
    numberOfScreen = len(mss.mss().monitors) - 1
    root = tk.Tk()
    root.title("Screenshot")
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.wm_attributes("-topmost", 1)

    button_list = []

    for i, button_name in enumerate(["cut Screen", "Text", "Read"]):
        button = tk.Button(root, text=button_name, width=25, height=5,
                           command=lambda name=button_name: button_clicked(name))
        button_list.append(button)
        button.grid(row=i, column=0, padx=10, pady=10)
    for i in range(numberOfScreen):
        button = tk.Button(root, text="Screen "+str(i+1), width=25, height=5,
                           command=lambda name="Screen "+str(i+1): button_clicked(name))
        button.grid(row=i+3, column=0, padx=10, pady=10)
    button = tk.Button(root, text="Folder", width=25, height=5,
                       command=lambda name="Folder": button_clicked(name))
    button.grid(row=i+4, column=0, padx=10, pady=10)
    root.update_idletasks()
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+10+10")
    root.mainloop()


menuWindow()
# menuWindow(2)
