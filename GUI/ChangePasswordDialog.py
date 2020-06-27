from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .ChangePasswordDialogUI import Ui_ChangePasswordDialog
from .Hint import Hint


class ChangePasswordDialog(QDialog, Ui_ChangePasswordDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def changePassword(self):
        newpassword = self.NewPassword.text()
        newpasswordagain = self.NewPasswordAgain.text()
        if newpasswordagain != newpassword:
            dialog = Hint("两次输入的密码不一致！", parent=self, flags=Qt.WindowTitleHint)
            dialog.open()
        else:
            dialog = Hint("新密码："+newpassword, parent=self, flags=Qt.WindowTitleHint)
            dialog.open()
            self.accept()
