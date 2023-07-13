import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
import keyboard
import mss


def blockScreen(screenSize):
    app = QApplication(sys.argv)

    blockWindow = QWidget()
    blockWindow.setWindowTitle("Translucent Window")
    blockWindow.setGeometry(
        screenSize["left"], screenSize["top"], screenSize["width"], screenSize["height"]
    )
    blockWindow.setWindowFlags(
        Qt.FramelessWindowHint
        | Qt.WindowStaysOnTopHint
        | Qt.Tool
        | Qt.X11BypassWindowManagerHint
    )
    blockWindow.setWindowOpacity(0.5)

    def exit():
        app.quit()

    keyboard.add_hotkey("esc", exit)

    blockWindow.show()
    sys.exit(app.exec_())


# blockScreen({"left": 0, "top": 0, "width": 1920, "height": 1080})
blockScreen(mss.mss().monitors[0])
