from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import QTimer
from test import MainWindow
import sys

class MainApplication(QtWidgets.QMainWindow):
    def showEvent(self, event):
        super(MainApplication, self).showEvent(event)
        print("Main window shown")

def show_main_window():
    app = QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    window.show()
    sys.exit(app.exec_())

def main():
    app = QApplication(sys.argv)
    splash_image = QPixmap("img3.gif")
    splash = QSplashScreen(splash_image)
    splash.show()
    QTimer.singleShot(2000, splash.close)
    QTimer.singleShot(2500, show_main_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash_image = QPixmap("img3.gif")
    splash = QSplashScreen(splash_image)
    splash.show()
    QTimer.singleShot(2000, splash.close)
    QTimer.singleShot(2500, show_main_window)
    sys.exit(app.exec_())