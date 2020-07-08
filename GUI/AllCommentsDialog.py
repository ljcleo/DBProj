from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ..DBInterface import (COMMENT_VIEW, USER_TABLE, CommentInterface,
                           UserInterface, getColumn)
from .AllCommentsDialogUI import Ui_AllCommentsDialog
from .CommentWidget import CommentWidget


class AllCommentsDialog(QDialog, Ui_AllCommentsDialog):
    def __init__(self, userID, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
        self.CommentTable.setColumnWidth(0, 630)

        userFetcher = UserInterface(UserInterface.ROLE_GUEST)
        userFetcher.selectUserInfo(userID)
        result = userFetcher.fetchResult()

        if len(result) == 0:
            raise RuntimeError('attempted to load comments by a ghost user')

        name = getColumn(result[0], USER_TABLE.name)
        sex = getColumn(result[0], USER_TABLE.sex)
        age = getColumn(result[0], USER_TABLE.age)
        userIsAdmin = getColumn(result[0], USER_TABLE.isAdmin)

        if userIsAdmin:
            name = '管理员 ' + name

        self.UserName.setText(name)
        self.Sex.setText(f'性别：{"保密" if sex is None else sex}')
        self.Age.setText(f'年龄：{0 if age is None else age:d}')
        self.CommentLabel.setText(f'{name} 的评论')

        self.CommentTable.clearContents()
        self.films = []

        searchEngine = CommentInterface(False)
        searchEngine.selectCommentByUserID(userID=userID)
        result = searchEngine.fetchResult()
        self.CommentTable.setRowCount(len(result))

        for index, row in enumerate(result):
            filmID = getColumn(row, COMMENT_VIEW.filmID)
            filmName = getColumn(row, COMMENT_VIEW.filmName)
            rating = getColumn(row, COMMENT_VIEW.rating)
            comment = getColumn(row, COMMENT_VIEW.comment)

            self.films.append(filmID)

            widget = CommentWidget()
            widget.NameLabel.setText(filmName)
            widget.RateLabel.setText(f'评分：{rating:.1f}')
            widget.CommentText.setText(comment if comment is not None else '（该用户未评论）')

            self.CommentTable.setCellWidget(index, 0, widget)
            self.CommentTable.setRowHeight(index, 130)

    def showMovieInfo(self, row, _):
        if len(self.films) != 0:
            self.parent().hideHomepage()
            self.parent().hideSearchResult()
            self.parent().hideSearch()
            self.parent().hideInformation()

            self.parent().showInformation(self.films[row])
            self.accept()
