from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ..DBInterface import USER_TABLE, UserInterface, getColumn
from .ChangeInformationDialogUI import Ui_ChangeInformationDialog
from .Hint import Hint


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
            Hint('昵称不能为空！', parent=self, flags=Qt.WindowTitleHint).open()
            return

        self.infoChanger.updateUserInfo(self.login, newUserName, newAge, newSex)
        self.parent().updateUserName()

        dialog = Hint("修改成功！", parent=self.parent(), flags=Qt.WindowTitleHint)
        dialog.open()
        self.accept()
