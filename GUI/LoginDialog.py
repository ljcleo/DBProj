from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QDialog

from .ChangePasswordDialog import ChangePasswordDialog
from .LoginDialogUI import Ui_LoginDialog
from .RegisterDialog import RegisterDialog
from .Hint import Hint


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.last = parent
        self.setupUi(self)

    def login(self):
        self.last.login=1
        self.last.refresh()
        dialog = Hint("登录成功", parent=self, flags=Qt.WindowTitleHint)
        dialog.open()
        self.close()

    def register(self):
        dialog = RegisterDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()

    def changePassword(self):
        dialog = ChangePasswordDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()
