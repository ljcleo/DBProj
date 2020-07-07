from PyQt5.QtCore import Qt

from ..DBInterface import USER_TABLE, UserInterface, getColumn
from .ChangeInformationDialog import ChangeInformationDialog
from .ChangePasswordDialog import ChangePasswordDialog
from .UserPartUI import Ui_UserPart


class UserPart(Ui_UserPart):
    def setupUser(self, UserPart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(UserPart)

    def changePassword(self):
        dialog = ChangePasswordDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()

    def modifyInformation(self):
        dialog = ChangeInformationDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()

    def logout(self):
        self.login = None
        self.loginAdmin = False
        self.refresh()

    def hideUser(self):
        self.UserFrame.hide()

    def showUser(self):
        self.updateUserName()
        self.UserFrame.show()

    def updateUserName(self):
        if self.login is None:
            self.UserNameLabel.setText('无名氏')
            self.loginAdmin = False
        else:
            userNameLoader = UserInterface(UserInterface.ROLE_MEMBER)
            userNameLoader.selectUserInfo(self.login)
            result = userNameLoader.fetchResult(1)

            if len(result) == 0:
                raise RuntimeError('an unknown user has logged-in')

            userName = getColumn(result[0], USER_TABLE.name)
            self.loginAdmin = getColumn(result[0], USER_TABLE.isAdmin)

            if self.loginAdmin:
                userName = '管理员 ' + userName
            self.UserNameLabel.setText(userName)
