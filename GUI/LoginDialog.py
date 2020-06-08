from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .ChangePasswordDialog import ChangePasswordDialog
from .LoginDialogUI import Ui_LoginDialog
from .RegisterDialog import RegisterDialog


class LoginDialog(QDialog, Ui_LoginDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def login(self):
        pass

    def register(self):
        dialog = RegisterDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()

    def changePassword(self):
        dialog = ChangePasswordDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()
