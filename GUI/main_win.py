import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from GUI.MainPart import MainWindow
from GUI.Hint import Hint

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow(flags=Qt.WindowTitleHint)
    main_window.show()
    sys.exit(app.exec())