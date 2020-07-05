from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .ChangeInformationDialogUI import Ui_ChangeInformationDialog
from .Hint import Hint


class ChangeInformationDialog(QDialog, Ui_ChangeInformationDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def changeInformation(self):
        newUserName = self.UserName.text()
        newAge = self.Age.text()
        newSex = self.Sex.text()
        print(newUserName, newAge, newSex)
        dialog = Hint("修改成功", parent=self, flags=Qt.WindowTitleHint)
        dialog.open()
        self.accept()
