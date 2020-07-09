from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox

from ..DBInterface import UserInterface
from .ChangePasswordDialogUI import Ui_ChangePasswordDialog


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
            QMessageBox.critical(self, '修改密码', '密码不能为空！')
            return

        if newPasswordAgain != newPassword:
            QMessageBox.critical(self, '修改密码', '两次输入的密码不一致！')
            return

        passwordVerifier = UserInterface(UserInterface.ROLE_LOGIN)
        if not passwordVerifier.verifyLogin(login, oldPassword):
            QMessageBox.critical(self, '修改密码', '旧密码错误！')
            return

        passwordChanger = UserInterface(UserInterface.ROLE_MEMBER)
        passwordChanger.updateUserPassword(login, newPassword)

        if not passwordVerifier.verifyLogin(login, newPassword):
            raise RuntimeError('something abnormal happened on the new password')

        QMessageBox.information(self.parent(), '修改密码', '密码修改成功！')
        self.accept()
