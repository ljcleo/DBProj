from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .ChangePasswordDialogUI import Ui_ChangePasswordDialog


class ChangePasswordDialog(QDialog, Ui_ChangePasswordDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def changePassword(self):
        # oldpassword = self.OldPassword.text()
        newpassword = self.NewPassword.text()
        newpasswordagain = self.NewPasswordAgain.text()
        # CHECK OLD PASSWORD HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if newpasswordagain != newpassword:
            print("两次输入的密码不一致！")
        else:
            print("新密码：", newpassword)
            self.accept()
