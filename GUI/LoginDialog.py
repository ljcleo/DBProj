from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox

from ..DBInterface import UserInterface
from .LoginDialogUI import Ui_LoginDialog
from .RegisterDialog import RegisterDialog


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.last = parent
        self.setupUi(self)

    def login(self):
        userID = self.UserName.text()
        password = self.Password.text()

        if userID == '' or password == '':
            QMessageBox.critical(self, '用户登录', '用户名与密码不能为空！')
            return

        loginVerifier = UserInterface(UserInterface.ROLE_LOGIN)

        if not loginVerifier.verifyLogin(userID, password):
            QMessageBox.critical(self, '用户登录', '用户名或密码错误！')
            return

        self.last.login = userID
        self.last.refresh()
        self.accept()

    def register(self):
        RegisterDialog(parent=self, flags=Qt.Drawer).open()
