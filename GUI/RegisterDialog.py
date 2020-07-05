from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .Hint import Hint
from .RegisterDialogUI import Ui_RegisterDialog


class RegisterDialog(QDialog, Ui_RegisterDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def register(self):
        username = self.UserName.text()
        password = self.Password.text()
        passwordAgain = self.PasswordAgain.text()

        if passwordAgain != password:
            dialog = Hint("两次输入的密码不一致！", parent=self, flags=Qt.WindowTitleHint)
            dialog.open()
        else:
            dialog = Hint(f"用户名：{username} 密码：{password}", parent=self,
                          flags=Qt.WindowTitleHint)
            dialog.open()
            self.accept()
