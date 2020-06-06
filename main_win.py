import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GuiWindows import *


class LoginDialog(QMainWindow, Ui_LoginDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)

    def ToChangePassword(self):
        ChangePassword = ChangePasswordDialog()
        ChangePassword.exec()

    def ToRegister(self):
        Register = RegisterDialog()
        Register.exec()


class ChangePasswordDialog(QMainWindow, Ui_ChangePasswordDialog):
    def __init__(self, parent=None):
        super(ChangePasswordDialog, self).__init__(parent)
        self.setupUi(self)


class RegisterDialog(QMainWindow, Ui_RegisterDialog):
    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = LoginDialog()
    Login.show()
    sys.exit(app.exec_())
