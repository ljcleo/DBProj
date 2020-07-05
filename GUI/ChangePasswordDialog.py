from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ..DBInterface import UserInterface
from .ChangePasswordDialogUI import Ui_ChangePasswordDialog
from .Hint import Hint


class ChangePasswordDialog(QDialog, Ui_ChangePasswordDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def changePassword(self):
        login = self.parent().login
        if login is None:
            raise RuntimeError('an unknown user has attempted to change password')

        oldPassword = self.OldPassword.text()
        newPassword = self.NewPassword.text()
        newPasswordAgain = self.NewPasswordAgain.text()

        if oldPassword == '' or newPassword == '':
            Hint('密码不能为空！', parent=self, flags=Qt.WindowTitleHint).open()
            return

        if newPasswordAgain != newPassword:
            dialog = Hint("两次输入的密码不一致！", parent=self, flags=Qt.WindowTitleHint)
            dialog.open()
            return

        passwordVerifier = UserInterface(UserInterface.ROLE_LOGIN)
        if not passwordVerifier.verifyLogin(login, oldPassword):
            Hint('旧密码错误！', parent=self, flags=Qt.WindowTitleHint).open()
            return

        passwordChanger = UserInterface(UserInterface.ROLE_MEMBER)
        passwordChanger.updateUserPassword(login, newPassword)

        if not passwordVerifier.verifyLogin(login, newPassword):
            Hint('密码修改失败？！', parent=self, flags=Qt.WindowTitleHint).open()
            return

        dialog = Hint("密码修改成功！", parent=self.parent(), flags=Qt.WindowTitleHint)
        dialog.open()
        self.accept()
