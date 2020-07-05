from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ..DBInterface import UserInterface
from .Hint import Hint
from .RegisterDialogUI import Ui_RegisterDialog


class RegisterDialog(QDialog, Ui_RegisterDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def register(self):
        userID = self.UserID.text()
        password = self.Password.text()
        passwordAgain = self.PasswordAgain.text()
        userName = self.UserName.text()

        if userID == '' or password == '' or passwordAgain == '' or userName == '':
            Hint('存在未填的必填项！', parent=self, flags=Qt.WindowTitleHint).open()
            return

        if passwordAgain != password:
            dialog = Hint("两次输入的密码不一致！", parent=self, flags=Qt.WindowTitleHint)
            dialog.open()
            return

        age = self.Age.value()
        sex = self.Sex.currentText() if self.Sex.currentIndex() > 0 else None

        registerer = UserInterface(UserInterface.ROLE_USR_ADMIN)
        registerer.selectUserInfo(userID)

        if len(registerer.fetchResult()) != 0:
            Hint("用户名已被注册！", parent=self, flags=Qt.WindowTitleHint).open()
            return

        registerer.createUser(userID, password, userName, userAge=age, userSex=sex)
        registerer.selectUserInfo(userID)

        if len(registerer.fetchResult()) == 0:
            Hint("注册失败？！", parent=self, flags=Qt.WindowTitleHint).open()
            return

        dialog = Hint("注册成功！", parent=self.parent(), flags=Qt.WindowTitleHint)
        dialog.open()
        self.accept()
