import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

    #just make a class with a paintEvent it can be anything (maybe. maybe 'Button' is a specific thing)

class Box(QWidget):
    def paintEvent(self, event):
        r = event.rect()
        p = QPainter(self)
        print(r)

        newPen = p.pen()
        newPen.setColor(QColor(0,0,255,255))
        p.setPen(newPen)

        p.fillRect(r,QColor(255,127,127,255))

        p1 = QPointF(20,50)
        p2 = QPointF(200,170)
        p.drawLine(p1,p2)


class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QHBoxLayout(self)

        pushButton = Box()
        main_layout.addWidget(pushButton)

        paintBox = Box()
        main_layout.addWidget(paintBox)

def SetWindowAttributes(win):
    if True:
        win.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        win.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
        win.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
    win.setGeometry(800,100, 400,300)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = App()
    SetWindowAttributes(window)
    window.show()
    sys.exit(app.exec())
   