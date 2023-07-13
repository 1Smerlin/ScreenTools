from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QTimer
import mss
import multiprocessing
import sys


def blockScreen(block_queue):
    print("!!!---blockScreen---!!!")

    # Diese Funktion wird aufgerufen, wenn das Fenster geschlossen werden soll.
    def check_queue():
        try:
            message = block_queue.get_nowait()
            if message == "close":
                app.quit()
        except multiprocessing.queues.Empty:
            pass

    screenSize = mss.mss().monitors[0]

    app = QApplication(sys.argv)

    blockWindow = QWidget()
    blockWindow.setWindowTitle("Translucent Window")
    blockWindow.setGeometry(screenSize["left"], screenSize["top"], screenSize["width"], screenSize["height"])
    blockWindow.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
    blockWindow.setWindowOpacity(0.5)

    # Qtimer wird genutzt um die check_queue Methode in einer Schleife aufzurufen.
    timer = QTimer()
    timer.timeout.connect(check_queue)
    timer.start(100)  # Prüfe alle 100 ms.

    blockWindow.show()
    sys.exit(app.exec_())
