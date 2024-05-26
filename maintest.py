from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import QTimer
from test import MainWindow
import sys

class MainApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Application")

def splash(app):
    splash_image = QPixmap("img3.gif")
    splash = QSplashScreen(splash_image)
    splash.show()
    QTimer.singleShot(2000, lambda: show_main_window(app, splash))

def show_main_window(app, splash):
    splash.close()
    window = MainApplication()
    window.show()

def main():
    app = QApplication(sys.argv)
    splash(app)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()







