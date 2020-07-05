from PyQt5.QtCore import Qt

from .UserPartUI import Ui_UserPart

from .ChangePasswordDialog import ChangePasswordDialog
from .ChangeInformationDialog import ChangeInformationDialog


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
        self.login = 0
        self.refresh()

    def hideUser(self):
        self.UserFrame.hide()

    def showUser(self):
        self.UserFrame.show()

