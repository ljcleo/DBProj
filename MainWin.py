import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from GUI.MainPart import MainWindow


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow(flags=Qt.WindowTitleHint)
    mainWindow.show()
    sys.exit(app.exec())
