from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .Hint import Hint
from .ModifyMoreDialogUI import Ui_ModifyMoreDialog


class ModifyMoreDialog(QDialog, Ui_ModifyMoreDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def modify(self):
        dialog = Hint("修改成功", parent=self, flags=Qt.WindowTitleHint)
        dialog.open()
        self.accept()
