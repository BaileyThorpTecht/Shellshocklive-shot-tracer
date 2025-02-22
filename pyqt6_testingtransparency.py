import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import *

def DoTimeStep(timestep, x, y, xVel, yVel, xAcc, yAcc):

    #there may be a problem of a smaller timestep changing the arc due to how non-continuous acceleration works

    xVel = xVel + xAcc * timestep
    x = x + xVel * timestep
    x = x + xAcc * timestep / 2 #account for inaccurate timestepping (only works with constant acc, which is fine)

    yVel = yVel + yAcc * timestep
    y = y + yVel * timestep
    y = y + yAcc * timestep / 2 #account for inaccurate timestepping (only works with constant acc, which is fine)


    return x, y, xVel, yVel

class Box(QWidget):
    def paintEvent(self, event):
        #setup
        r = event.rect()
        p = QPainter(self)
        print(r)

        #change pen
        newPen = p.pen()
        newPen.setColor(QColor(0,0,255,255))
        newPen.setWidthF(3)
        p.setPen(newPen)

        #color background of box
        p.fillRect(r,QColor(255,127,127,20))

        #drawing arc
        #starting vars. Eventually, position will be from the tank and velocity from power/angle
        timestep = 1
        x = 800
        y = 400
        yVel = 50
        xVel = 40
        yAcc = -10 #gravity
        xAcc = 0 #wind       
        
        rectHeight = r.height()
        rectWidth = r.width()

        while y >= 0 and y <= rectHeight and x >= 0 and x <= rectWidth:
            xOld = x
            yOld = y

            x, y, xVel, yVel = DoTimeStep(timestep, x, y, xVel, yVel, xAcc, yAcc)

            line = QLineF(xOld, rectHeight - yOld, x, rectHeight - y)
            p.drawLine(line)

    def mousePressEvent(self, event):
        f = open("y_coords_90deg.txt", "a")
        x = event.pos().x()
        y = event.pos().y()
        print(f"Position: {x}, {y}")
        f.write(f"{y}\n")
        f.close()

        



class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
    
        main_layout = QHBoxLayout(self)

        #create objects for the layout here
        paintBox = Box()
        main_layout.addWidget(paintBox)

    def keyPressEvent(self, a0: QKeyEvent | None) -> None:
        print(a0.key())
        if a0.key() == Qt.Key.Key_P:
            sys.exit()
            
        return super().keyPressEvent(a0)
    



def SetWindowAttributes(win):
    if True: #transparent background fullscreen
        win.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        win.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground, True)
        #win.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        win.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        win.setGeometry(-11,-11,1942,1102)
    else:
        win.setGeometry(800,100, 800,600)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = App()
    SetWindowAttributes(window)
    window.show()
    sys.exit(app.exec())
   