import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from GUI.LoginDialog import LoginDialog


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = LoginDialog(flags=Qt.WindowTitleHint)
    login.show()
    sys.exit(app.exec())
