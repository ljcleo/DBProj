from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from requests import get as getURL

from ..DBInterface import FILM_VIEW, FilmInterface, getColumn
from .AllCastDialog import AllCastDialog
from .AllDirectorDialog import AllDirectorDialog
from .CommentDialog import CommentDialog
from .Hint import Hint
from .InformationPartUI import Ui_InformationPart
from .ModifyMovieDialog import ModifyMovieDialog


class InformationPart(Ui_InformationPart):
    def setupInformation(self, InformationPart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(InformationPart)
        self.CommentFrame.hide()

    def addComment(self):
        if self.login is None:
            dialog = Hint("您还未登录，无法评论！", parent=self, flags=Qt.WindowTitleHint)
            dialog.open()
        else:
            dialog = CommentDialog(parent=self, flags=Qt.WindowTitleHint)
            dialog.open()

    def hideInformation(self):
        self.InformationFrame.hide()
        self.HLineMovie.hide()
        self.CommentFrame.hide()
        self.MoreInformationFrame.hide()
        self.AddComment.setAutoDefault(False)
        self.AddComment.setDefault(False)

    def showInformation(self, filmID):
        self.filmID = filmID
        self.__makeContents()

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
            Hint('暂无导演信息！', parent=self, flags=Qt.WindowTitleHint).open()
        else:
            dialog = AllDirectorDialog(self.filmID, parent=self, flags=Qt.WindowTitleHint)
            dialog.open()

    def showAllCast(self):
        if self.Cast.text() == '--':
            Hint('暂无演员信息！', parent=self, flags=Qt.WindowTitleHint).open()
        else:
            dialog = AllCastDialog(self.filmID, parent=self, flags=Qt.WindowTitleHint)
            dialog.open()

    def modifyMovie(self):
        dialog = ModifyMovieDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()

    def toComment(self):
        self.CommentFrame.show()
        self.MoreInformationFrame.hide()

    def toStoryline(self):
        self.CommentFrame.hide()
        self.MoreInformationFrame.show()

    def __makeContents(self):
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
        if url is not None:
            res = getURL(url)
            image = QImage.fromData(res.content)
            self.Picture.setPixmap(QPixmap.fromImage(image))
        else:
            self.Picture.setPixmap('')
