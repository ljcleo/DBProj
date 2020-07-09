from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox

from ..DBInterface import USER_TABLE, UserInterface, getColumn
from .ChangeInformationDialogUI import Ui_ChangeInformationDialog


class ChangeInformationDialog(QDialog, Ui_ChangeInformationDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        self.login = parent.login
        if self.login is None:
            raise RuntimeError('an unknown user has attempted to change user info')

        self.infoChanger = UserInterface(UserInterface.ROLE_MEMBER)
        self.infoChanger.selectUserInfo(self.login)
        result = self.infoChanger.fetchResult()

        if len(result) == 0:
            raise RuntimeError('a ghost user has logged-in')

        age = getColumn(result[0], USER_TABLE.age)
        sex = getColumn(result[0], USER_TABLE.sex)
        self.UserName.setText(getColumn(result[0], USER_TABLE.name))
        self.Age.setValue(0 if age is None else age)

        if sex is None:
            self.Sex.setCurrentIndex(0)
        else:
            self.Sex.setCurrentText(sex)

    def changeInformation(self):
        newUserName = self.UserName.text()
        newAge = self.Age.value()
        newSex = None if self.Sex.currentIndex() == 0 else self.Sex.currentText()

        if newUserName == '':
            QMessageBox.critical(self, '修改个人信息', '昵称不能为空！')
            return

        self.infoChanger.updateUserInfo(self.login, newUserName, newAge, newSex)
        self.parent().updateUserName()

        QMessageBox.information(self.parent(), '修改个人信息', '修改成功！')
        self.accept()
