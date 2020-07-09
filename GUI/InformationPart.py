from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QAbstractItemView, QMessageBox, QTableWidgetItem
from requests import get as getURL
from requests.exceptions import RequestException

from ..DBInterface import (COMMENT_VIEW, FILM_VIEW, CommentInterface,
                           FilmInterface, getColumn)
from .AllCastDialog import AllCastDialog
from .AllCommentsDialog import AllCommentsDialog
from .AllDirectorDialog import AllDirectorDialog
from .CommentDialog import CommentDialog
from .CommentWidget import CommentWidget
from .InformationPartUI import Ui_InformationPart
from .ModifyMovieDialog import ModifyMovieDialog


class InformationPart(Ui_InformationPart):
    def setupInformation(self, InformationPart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(InformationPart)

        self.CommentFrame.hide()
        self.CommentTable.setColumnWidth(0, 630)
        self.commentUsers = []

    def addComment(self):
        if self.login is None:
            QMessageBox.critical(self, '评论', '请登录后再添加/修改评论！')
        else:
            CommentDialog(self.filmID, self.login, parent=self, flags=Qt.Drawer).open()

    def hideInformation(self):
        self.InformationFrame.hide()
        self.HLineMovie.hide()
        self.CommentFrame.hide()
        self.MoreInformationFrame.hide()
        self.AddComment.setAutoDefault(False)
        self.AddComment.setDefault(False)

    def showInformation(self, filmID):
        self.filmID = filmID
        self.makeContents()

        self.InformationFrame.show()
        self.HLineMovie.show()
        self.MoreInformationFrame.show()
        self.AddComment.setAutoDefault(True)
        self.AddComment.setDefault(True)

    def returnHomepage(self):
        self.hideInformation()
        self.showHomepage()

    def showAllDirector(self):
        if self.Director.text() == '--':
            QMessageBox.information(self, '导演信息', '暂无导演信息！')
        else:
            AllDirectorDialog(self.filmID, parent=self, flags=Qt.Drawer).open()

    def showAllCast(self):
        if self.Cast.text() == '--':
            QMessageBox.information(self, '演员信息', '暂无演员信息！')
        else:
            AllCastDialog(self.filmID, parent=self, flags=Qt.Drawer).open()

    def modifyMovie(self):
        if not self.loginAdmin:
            QMessageBox.critical(self, '修改电影', '您没有修改电影的权限！')
            return

        ModifyMovieDialog(self.filmID, self.makeContents, parent=self, flags=Qt.Drawer).open()

    def toComment(self):
        self.makeComments()
        self.CommentFrame.show()
        self.MoreInformationFrame.hide()

    def toStoryline(self):
        self.CommentFrame.hide()
        self.MoreInformationFrame.show()

    def showUserComment(self, row, _):
        if len(self.commentUsers) != 0:
            AllCommentsDialog(self.commentUsers[row], parent=self, flags=Qt.Drawer).open()

    def makeComments(self):
        self.CommentTable.clearContents()
        self.commentUsers = []

        if self.filmID is None:
            raise RuntimeError('cannot display comment for nothing')

        self.CommentTable.clear()
        commentFetcher = CommentInterface(False)
        commentFetcher.selectCommentByFilmID(self.filmID)
        result = commentFetcher.fetchResult()

        if len(result) == 0:
            self.CommentTable.setSelectionMode(QAbstractItemView.NoSelection)
            self.CommentTable.setRowCount(1)

            item = QTableWidgetItem('还没有评论，快来抢沙发吧！')
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.CommentTable.setItem(0, 0, item)
        else:
            self.CommentTable.setSelectionMode(QAbstractItemView.SingleSelection)
            self.CommentTable.setRowCount(len(result))

            for index, row in enumerate(result):
                userID = getColumn(row, COMMENT_VIEW.userID)
                userName = getColumn(row, COMMENT_VIEW.userName)
                userIsAdmin = getColumn(row, COMMENT_VIEW.userIsAdmin)
                rating = getColumn(row, COMMENT_VIEW.rating)
                comment = getColumn(row, COMMENT_VIEW.comment)

                self.commentUsers.append(userID)
                if userIsAdmin:
                    userName = '管理员 ' + userName

                widget = CommentWidget()
                widget.NameLabel.setText(userName)
                widget.RateLabel.setText(f'评分：{rating:.1f}')
                widget.CommentText.setText(comment if comment is not None else '（该用户未评论）')

                self.CommentTable.setCellWidget(index, 0, widget)
                self.CommentTable.setRowHeight(index, 130)

    def makeContents(self):
        if self.filmID is None:
            raise RuntimeError('cannot display null information')

        filmFetcher = FilmInterface(False)
        filmFetcher.selectFilm(self.filmID)
        result = filmFetcher.fetchResult()

        if len(result) == 0:
            raise RuntimeError('cannot display ghost information')
        row = result[0]

        chineseName = getColumn(row, FILM_VIEW.chineseName)
        originalName = getColumn(row, FILM_VIEW.originalName)
        genres = getColumn(row, FILM_VIEW.genres)
        releaseDate = getColumn(row, FILM_VIEW.releaseDate)
        length = getColumn(row, FILM_VIEW.length)
        companyName = getColumn(row, FILM_VIEW.companyName)
        companyNationality = getColumn(row, FILM_VIEW.companyNationality)
        directors = getColumn(row, FILM_VIEW.directors)
        casts = getColumn(row, FILM_VIEW.casts)
        rating = getColumn(row, FILM_VIEW.rating)
        storyline = getColumn(row, FILM_VIEW.storyline)
        prizeHistory = getColumn(row, FILM_VIEW.prizeHistory)
        picture = getColumn(row, FILM_VIEW.picture)

        self.ChineseName.setText('--' if chineseName is None else chineseName)
        self.OriginalName.setText('--' if originalName is None else originalName)
        self.Genre.setText('--' if genres is None else genres)
        self.ReleaseDate.setText('--' if releaseDate is None else f'{releaseDate}')
        self.Length.setText('--' if length is None else f'{length:d} 分钟')
        self.Company.setText(('--' if companyName is None else companyName) +
                             ('--' if companyNationality is None else f'（{companyNationality}）'))
        self.Director.setText('--' if directors is None else
                              directors if len(directors) < 18 else directors[:15] + '……')
        self.Cast.setText('--' if casts is None else
                          casts if len(casts) < 18 else casts[:15] + '……')
        self.Rating.setText('--/10' if rating is None else f'{rating:.1f}/10')

        self.Storyline.setText('无' if storyline is None else storyline)
        self.PrizeHistory.setText('无' if prizeHistory is None else prizeHistory)

        self.__showInformationImage(picture)

    def __showInformationImage(self, url=None):
        self.Picture.clear()

        if url is not None:
            try:
                res = getURL(url, timeout=20)
                if res.status_code != 200:
                    raise RequestException()

                image = QImage.fromData(res.content)
                self.Picture.setPixmap(QPixmap.fromImage(image))
            except RequestException:
                self.Picture.setText('海报加载失败')
        else:
            self.Picture.setText('暂无海报')
