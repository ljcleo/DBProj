from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox

from ..DBInterface import UserInterface
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
            QMessageBox.critical(self, '新用户注册', '存在未填的必填项！')
            return

        if passwordAgain != password:
            QMessageBox.critical(self, '新用户注册', '两次输入的密码不一致！')
            return

        age = self.Age.value()
        sex = self.Sex.currentText() if self.Sex.currentIndex() > 0 else None

        registerer = UserInterface(UserInterface.ROLE_USR_ADMIN)
        registerer.selectUserInfo(userID)

        if len(registerer.fetchResult()) != 0:
            QMessageBox.critical(self, '新用户注册', '用户名已被注册！')
            return

        registerer.createUser(userID, password, userName, userAge=age, userSex=sex)
        registerer.selectUserInfo(userID)

        if len(registerer.fetchResult()) == 0:
            raise RuntimeError('a ghost user has just registered')

        QMessageBox.information(self.parent(), '新用户注册', '注册成功，欢迎加入！')
        self.accept()
