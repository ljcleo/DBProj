from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .CommentDialogUI import Ui_CommentDialog
from .Hint import Hint


class CommentDialog(QDialog, Ui_CommentDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def comment(self):
        if self.Rate5.isChecked():
            print(5)
        elif self.Rate4.isChecked():
            print(4)
        elif self.Rate3.isChecked():
            print(3)
        elif self.Rate2.isChecked():
            print(2)
        else:
            print(1)

        text = self.CommentText.toPlainText()
        print(text)

        dialog = Hint("评论成功！", parent=self, flags=Qt.WindowTitleHint)
        dialog.open()

        self.close()
