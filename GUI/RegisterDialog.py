from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .RegisterDialogUI import Ui_RegisterDialog


class RegisterDialog(QDialog, Ui_RegisterDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def register(self):
        username = self.UserName.text()
        password = self.Password.text()
        passwordagain = self.PasswordAgain.text()

        if passwordagain != password:
            print("两次输入的密码不一致！")
        else:
            print("用户名：", username)
            print("密码：", password)
            self.accept()
