from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .CommentDialogUI import Ui_CommentDialog
from .Hint import Hint


class CommentDialog(QDialog, Ui_CommentDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def comment(self):
        text = self.CommentText.toPlainText()
        print(text)

        Hint("评论成功！", parent=self.parent(), flags=Qt.WindowTitleHint).open()

        self.close()
