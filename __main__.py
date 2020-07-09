import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from DBProj.GUI.MainPart import MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow(flags=Qt.Window)
    mainWindow.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
    mainWindow.setFixedSize(mainWindow.size())
    mainWindow.show()
    sys.exit(app.exec())
