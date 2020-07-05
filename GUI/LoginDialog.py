from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ..DBInterface import UserInterface
from .Hint import Hint
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
            Hint('用户名与密码不能为空！', parent=self, flags=Qt.WindowTitleHint).open()
            return

        loginVerifier = UserInterface(UserInterface.ROLE_LOGIN)

        if not loginVerifier.verifyLogin(userID, password):
            Hint('用户名或密码错误！', parent=self, flags=Qt.WindowTitleHint).open()
            return

        self.last.login = userID
        self.last.refresh()
        dialog = Hint("登录成功", parent=self.parent(), flags=Qt.WindowTitleHint)
        dialog.open()
        self.accept()

    def register(self):
        dialog = RegisterDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()
