from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import QTimer
from test import MainWindow
import sys

def main():
    """Main"""
    app = QApplication(sys.argv)
    splash(app)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

def splash(app):
    splash_image = QPixmap("img3.gif")
    splash = QSplashScreen(splash_image)
    splash.show()
    
    QTimer.singleShot(3000, lambda: show_main_window(splash))

def show_main_window(splash):
    splash.close()
    window = MainWindow()
    window.show()

if __name__ == "__main__":
    main()