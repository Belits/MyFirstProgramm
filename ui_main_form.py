# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonPanel = QtWidgets.QWidget(self.centralwidget)
        self.buttonPanel.setMaximumSize(QtCore.QSize(16777215, 35))
        self.buttonPanel.setObjectName("buttonPanel")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.buttonPanel)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startButton = QtWidgets.QToolButton(self.buttonPanel)
        self.startButton.setMinimumSize(QtCore.QSize(30, 30))
        self.startButton.setBaseSize(QtCore.QSize(30, 30))
        self.startButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Belka/.designer/backup/startIco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon)
        self.startButton.setIconSize(QtCore.QSize(30, 30))
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_2.addWidget(self.startButton)
        self.stopButton = QtWidgets.QToolButton(self.buttonPanel)
        self.stopButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Belka/.designer/backup/stopIco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setIconSize(QtCore.QSize(30, 30))
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.closeButton = QtWidgets.QPushButton(self.buttonPanel)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.buttonPanel)
        self.centralView = QtWidgets.QWidget(self.centralwidget)
        self.centralView.setObjectName("centralView")
        self.labelHello = QtWidgets.QLabel(self.centralView)
        self.labelHello.setGeometry(QtCore.QRect(240, -20, 350, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.labelHello.setFont(font)
        self.labelHello.setObjectName("labelHello")
        self.pushButton = QtWidgets.QPushButton(self.centralView)
        self.pushButton.setGeometry(QtCore.QRect(190, 410, 461, 131))
        self.pushButton.setObjectName("pushButton")
        self.drawField = QtWidgets.QLabel(self.centralView)
        self.drawField.setGeometry(QtCore.QRect(130, 90, 581, 291))
        self.drawField.setAutoFillBackground(False)
        self.drawField.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.drawField.setText("")
        self.drawField.setObjectName("drawField")
        self.verticalLayout.addWidget(self.centralView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 885, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.mGameSpeed = QtWidgets.QMenu(self.menu_2)
        self.mGameSpeed.setObjectName("mGameSpeed")
        self.mDifficultyLevel = QtWidgets.QMenu(self.menu_2)
        self.mDifficultyLevel.setTearOffEnabled(False)
        self.mDifficultyLevel.setObjectName("mDifficultyLevel")
        self.aAbout = QtWidgets.QMenu(self.menubar)
        self.aAbout.setObjectName("aAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.aNewGame = QtWidgets.QAction(MainWindow)
        self.aNewGame.setObjectName("aNewGame")
        self.aSaveGame = QtWidgets.QAction(MainWindow)
        self.aSaveGame.setObjectName("aSaveGame")
        self.aLoadGame = QtWidgets.QAction(MainWindow)
        self.aLoadGame.setObjectName("aLoadGame")
        self.aQuit = QtWidgets.QAction(MainWindow)
        self.aQuit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.aQuit.setObjectName("aQuit")
        self.aGSx1 = QtWidgets.QAction(MainWindow)
        self.aGSx1.setCheckable(True)
        self.aGSx1.setChecked(True)
        self.aGSx1.setObjectName("aGSx1")
        self.aGSx2 = QtWidgets.QAction(MainWindow)
        self.aGSx2.setCheckable(True)
        self.aGSx2.setObjectName("aGSx2")
        self.aGSx5 = QtWidgets.QAction(MainWindow)
        self.aGSx5.setCheckable(True)
        self.aGSx5.setObjectName("aGSx5")
        self.aGSx10 = QtWidgets.QAction(MainWindow)
        self.aGSx10.setCheckable(True)
        self.aGSx10.setObjectName("aGSx10")
        self.mDLEasy = QtWidgets.QAction(MainWindow)
        self.mDLEasy.setCheckable(True)
        self.mDLEasy.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.mDLEasy.setObjectName("mDLEasy")
        self.mDLMedium = QtWidgets.QAction(MainWindow)
        self.mDLMedium.setCheckable(True)
        self.mDLMedium.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.mDLMedium.setObjectName("mDLMedium")
        self.mDLHard = QtWidgets.QAction(MainWindow)
        self.mDLHard.setCheckable(True)
        self.mDLHard.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.mDLHard.setObjectName("mDLHard")
        self.menu.addAction(self.aNewGame)
        self.menu.addAction(self.aSaveGame)
        self.menu.addAction(self.aLoadGame)
        self.menu.addAction(self.aQuit)
        self.mGameSpeed.addAction(self.aGSx1)
        self.mGameSpeed.addAction(self.aGSx2)
        self.mGameSpeed.addAction(self.aGSx5)
        self.mGameSpeed.addAction(self.aGSx10)
        self.mDifficultyLevel.addAction(self.mDLEasy)
        self.mDifficultyLevel.addAction(self.mDLMedium)
        self.mDifficultyLevel.addAction(self.mDLHard)
        self.menu_2.addAction(self.mGameSpeed.menuAction())
        self.menu_2.addAction(self.mDifficultyLevel.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.aAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.closeButton.clicked.connect(MainWindow.close)
        self.aQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????? ????????"))
        self.closeButton.setText(_translate("MainWindow", "??????????????"))
        self.labelHello.setText(_translate("MainWindow", "???????????? ??????!!!"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menu.setTitle(_translate("MainWindow", "????????"))
        self.menu_2.setTitle(_translate("MainWindow", "??????????????????"))
        self.mGameSpeed.setTitle(_translate("MainWindow", "???????????????? ????????"))
        self.mDifficultyLevel.setTitle(_translate("MainWindow", "?????????????? ??????????????????"))
        self.aAbout.setTitle(_translate("MainWindow", "?? ??????????????????"))
        self.aNewGame.setText(_translate("MainWindow", "?????????? ????????"))
        self.aSaveGame.setText(_translate("MainWindow", "??????????????????"))
        self.aLoadGame.setText(_translate("MainWindow", "??????????????????"))
        self.aQuit.setText(_translate("MainWindow", "??????????"))
        self.aGSx1.setText(_translate("MainWindow", "x1"))
        self.aGSx2.setText(_translate("MainWindow", "x2"))
        self.aGSx5.setText(_translate("MainWindow", "x5"))
        self.aGSx10.setText(_translate("MainWindow", "x10"))
        self.mDLEasy.setText(_translate("MainWindow", "Easy"))
        self.mDLMedium.setText(_translate("MainWindow", "Medium"))
        self.mDLHard.setText(_translate("MainWindow", "Hard"))
