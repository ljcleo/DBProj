from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from .UserMainWindowUI import Ui_UserMainWindow

from .LoginDialog import LoginDialog
from .GuestMainWindow import GuestMainWindow
from .ChangePasswordDialog import ChangePasswordDialog

class UserMainWindow(QMainWindow, Ui_UserMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def movie1(self):
        print("这是给您推荐的第一部电影")
        pass

    def movie2(self):
        print("这是给您推荐的第二部电影")
        pass

    def movie3(self):
        print("这是给您推荐的第三部电影")
        pass

    def search(self):
        text = self.SearchInput.text()
        print("您想找", text, "吗？")
        print("亲亲这边建议您上豆瓣哦")

    def changePassword(self):
        dialog = ChangePasswordDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()

    def modifyInformation(self):
        print("暂不支持修改个人信息！")
        pass

    def logout(self):
        mainwindow = GuestMainWindow(flags=Qt.WindowTitleHint)
        mainwindow.show()
        self.close()


