from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import QTimer
from test_two import WindowTwo
import sys

class MainApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Application")
        
    # Отображение заставки
    def showSplashScreen(self):
        self.splash = QSplashScreen(QPixmap("img3.gif"))
        self.splash.show()
        
        QTimer.singleShot(1500, self.showMainWindow)

    # Отображение основного окна
    def showMainWindow(self):
        self.splash.close()
        self.windowTwo = WindowTwo()
        self.windowTwo.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splashApp = MainApplication()
    splashApp.showSplashScreen()
    sys.exit(app.exec_())

