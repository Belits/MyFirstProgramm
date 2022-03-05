from PyQt5 import QtWidgets, QtGui
from ui_main_form import Ui_MainWindow
from PyQt5.QtCore import QTimer
from drawedObject import DrawMoveDiag,DrawMoveVert,DrawMoveHor

class MainForm(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.moveTimer = QTimer()
        self.setConnections()
        self.show()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill()
        self.ui.drawField.setPixmap(canvas)

        self.__objList = [DrawMoveDiag(0, 0, QtGui.QColor('red')), DrawMoveVert(100, 100, QtGui.QColor('blue')),
                          DrawMoveHor(200, 0, QtGui.QColor('margenta'))]

    def setConnections(self):
        self.ui.aGSx1.triggered.connect(self.onActionGameSpeed)
        self.ui.aGSx2.triggered.connect(self.onActionGameSpeed)
        self.ui.aGSx5.triggered.connect(self.onActionGameSpeed)
        self.ui.aGSx10.triggered.connect(self.onActionGameSpeed)
        self.ui.startButton.clicked.connect(self.onStartButtonClicked)
        self.ui.stopButton.clicked.connect(self.onStopButtonClicked)
        self.moveTimer.timeout.connect(self.onMoveTimerTimeout)
        self.ui.pushButton.clicked.connect(self.drawSomething)

    def onActionGameSpeed(self):
        self.ui.aGSx1.setChecked(False)
        self.ui.aGSx2.setChecked(False)
        self.ui.aGSx5.setChecked(False)
        self.ui.aGSx10.setChecked(False)
        self.sender().setChecked(True)

    def onStartButtonClicked(self):
        self.moveTimer.start(100)

    def onStopButtonClicked(self):
        self.moveTimer.stop()


    def onMoveTimerTimeout(self):
#        geom = self.ui.labelHello.geometry()
#        self.ui.labelHello.setGeometry(geom.x(), (geom.y()+10) % self.ui.centralwidget.height(), geom.width(),
#                                       geom.height())
        for obj in self.__objList:
            obj.moveObj()
        self.drawSomething()

    def drawSomething(self):
        self.ui.drawField.pixmap().fill()
        painter = QtGui.QPainter(self.ui.drawField.pixmap())
        for obj in self.__objList:
            obj.paint(painter)

        painter.end()
        self.ui.drawField.repaint()

