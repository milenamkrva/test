from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import QTimer
from test import MainWindow
import sys

class MainApplication(QtWidgets.QMainWindow):
    def showEvent(self, event):
        super(MainApplication, self).showEvent(event)

def show_main_window():
    app = QtWidgets.QApplication.instance()
    window = MainApplication()
    window.show()

def close_splash_screen(splash):
    splash.close()
    show_main_window()

def show_splash_and_main():
    app = QApplication(sys.argv)
    splash_image = QPixmap("img3.gif")
    splash = QSplashScreen(splash_image)
    splash.show()
    QTimer.singleShot(2000, lambda: close_splash_screen(splash))
    sys.exit(app.exec_())

if __name__ == "__main__":
    show_splash_and_main()
    app.exec_()