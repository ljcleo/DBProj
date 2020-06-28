from PyQt5.QtCore import Qt

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
        print("暂不支持修改信息")

    def logout(self):
        self.login = 0
        self.refresh()

    def hideUser(self):
        self.UserFrame.hide()

    def showUser(self):
        self.UserFrame.show()
