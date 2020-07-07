from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ..DBInterface import CommentInterface, COMMENT_VIEW, getColumn
from .AllCommentsDialogUI import Ui_AllComments
from .CommentWidget import CommentWidget


class AllComments(QDialog, Ui_AllComments):
    def __init__(self, userID, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0, 630)

        self.tableWidget.clearContents()
        searchEngine = CommentInterface(False)
        searchEngine.selectCommentByUserID(userID=userID)
        result = searchEngine.fetchResult()
        self.tableWidget.setRowCount(len(result))

        for index, row in enumerate(result):
            # filmID = getColumn(row, COMMENT_VIEW.filmID)
            filmName = getColumn(row, COMMENT_VIEW.filmName)
            rating = getColumn(row, COMMENT_VIEW.rating)
            comment = getColumn(row, COMMENT_VIEW.comment)

            widget = CommentWidget()
            widget.NameLabel.setText(filmName)
            widget.RateLabel.setText(f'评分：{rating:.1f}')
            widget.CommentText.setText(comment if comment is not None else '（该用户未评论）')

            self.tableWidget.setCellWidget(index, 0, widget)
            self.tableWidget.setRowHeight(index, 130)
