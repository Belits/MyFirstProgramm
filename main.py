import sys
from PyQt5 import QtWidgets
from MainFormM import MainForm

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainForm()
    sys.exit(app.exec_())
