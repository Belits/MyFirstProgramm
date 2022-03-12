from PyQt5.QtGui import QColor, QImage
from PyQt5.QtCore import QPoint

class DrawedObject:

    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    def X(self):
        return self._x

    def Y(self):
        return self._y

    def setCoords(self, newX, newY):
        self._x = newX
        self._y = newY

    def paint(self, painter):
        painter.setPen(self._color)
        painter.drawImage(QPoint(self._x, self._y), QImage("redCircle.png"))

class DrawMoveDiag(DrawedObject) :
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def moveObj(self):
        self._x = self._x + 5
        self._y = self._y + 5


class DrawMoveHor(DrawedObject) :
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def moveObj(self):
        #self.setCoord(self.X() + 5, self.Y())
        self._x += 5

class DrawMoveVert(DrawedObject) :
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def moveObj(self):
        self._y += 5
