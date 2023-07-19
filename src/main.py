from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPainter, QPen, QMouseEvent
from PyQt5.QtCore import Qt, QPoint

class Canvas(QLabel):
    def __init__(self):
        super().__init__()
        self.last_point = None
        self.pen = QPen(Qt.white)
        # self.setScaledContents(True)

        pixmap = QPixmap(280, 280)
        pixmap.fill(Qt.black)
        self.setPixmap(pixmap)
        

    def mouseMoveEvent(self, e: QMouseEvent):
        mouse_pos = QPoint(round(e.x() / 10), round(e.y() / 10))
        
        if (self.last_point == None):
            self.last_point = mouse_pos
        
        smallerMap = self.pixmap().scaled(28, 28, aspectRatioMode=Qt.IgnoreAspectRatio, transformMode=Qt.FastTransformation)
        painter = QPainter(smallerMap)
        painter.setPen(self.pen)
        painter.drawLine(self.last_point, mouse_pos)
        painter.end()
        self.last_point = mouse_pos
        self.setPixmap(smallerMap.scaled(280, 280,  aspectRatioMode=Qt.IgnoreAspectRatio, transformMode=Qt.FastTransformation))
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
      
        self.canvas = Canvas()

        button = QPushButton()
        button2 = QPushButton()

        buttons = QWidget()
        vlay = QVBoxLayout(buttons)
        vlay.addWidget(button, 1)
        vlay.addWidget(button2, 1)

        hlay = QHBoxLayout(centralWidget)
        hlay.setContentsMargins(0, 0, 0, 0)
        hlay.addStretch(1)
        hlay.addWidget(self.canvas, 1, Qt.AlignBottom)
        hlay.addWidget(buttons, 1, Qt.AlignRight)
        
        self.last_point = None


def main():
    app = QApplication([])
    window = MainWindow()

    # button = QPushButton()
    # dockWidget = QDockWidget("Dock Widget")
    # dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea |
    #                                       Qt.RightDockWidgetArea)
    # dockWidget.setWidget(button)
    # window.add(Qt.LeftDockWidgetArea, dockWidget)
    
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()