import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie

class LoadingScreen(QWidget):
        def __init__(self):
            super().__init__()
            self.setFixedSize(200,200)
            self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

            self.label_animation = QLabel(self) 

            self.movie=QMovie('Loading_2.gif')
            self.label_animation.setMovie(self.movie)

            timer = QTimer(self)
            self.startAnimation()
            timer.singleShot(3000, self.stopAnimation)

            self.show()

        def startAnimation(self):
            self.movie.start()

        def stopAnimation(self):
            self.movie.stop()
            self.close()

class Appdemo(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel('<font size=12> This is main app window </font>', self)
        label.setGeometry(150,150,300,50)

        self.loading_screen=LoadingScreen()

        self.show()

app = QApplication(sys.argv)

demo = Appdemo()

app.exit(app.exec_())
