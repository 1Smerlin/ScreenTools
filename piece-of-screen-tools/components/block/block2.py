import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
import keyboard


def blockScreen(screenSize):
    app = QApplication(sys.argv)

    blockWindow = QWidget()
    blockWindow.setWindowTitle("Translucent Window")
    blockWindow.setGeometry(
        screenSize["left"],
        screenSize["top"],
        screenSize["width"],
        screenSize["height"]
    )
    blockWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    blockWindow.setWindowOpacity(1)

    def exit():
        app.quit()

    keyboard.add_hotkey("esc", exit)

    blockWindow.show()
    sys.exit(app.exec_())


blockScreen({"left": 0, "top": 0, "width": 1920, "height": 1080})
