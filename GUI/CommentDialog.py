from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox

from ..DBInterface import COMMENT_TABLE, CommentInterface, getColumn
from .CommentDialogUI import Ui_CommentDialog


class CommentDialog(QDialog, Ui_CommentDialog):
    def __init__(self, filmID, userID, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
        self.accepted.connect(parent.makeContents)
        self.accepted.connect(parent.makeComments)

        self.filmID = filmID
        self.userID = userID

        self.commenter = CommentInterface(True)
        self.commenter.selectComment(filmID, userID)
        result = self.commenter.fetchResult()

        if len(result) != 0:
            rating = getColumn(result[0], COMMENT_TABLE.rating)
            comment = getColumn(result[0], COMMENT_TABLE.comment)

            self.Rating.setValue(rating)
            self.CommentText.setPlainText(comment)

    def comment(self):
        rating = self.Rating.value()
        comment = self.CommentText.toPlainText()

        if comment == '':
            comment = None

        self.commenter.upsertComment(self.filmID, self.userID, rating=rating, userComment=comment)
        QMessageBox.information(self.parent(), '评论', '评论成功！')
        self.accept()
