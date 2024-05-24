from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSplashScreen, QApplication
from PyQt5.QtCore import QTimer
import sys

app = QApplication(sys.argv)
splash_image = QPixmap("img3.gif")
splash = QSplashScreen(splash_image)
splash.show()

QTimer.singleShot(2000, splash.close)


# Запуск выполнения главного цикла приложения
sys.exit(app.exec_())






