from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from ..DBInterface import (DIRECTING_TABLE, DIRECTOR_TABLE, CAST_TABLE,
                           FILM_VIEW, GENRE_TABLE, PLAY_TABLE,
                           CompanyInterface, FilmInterface, getColumn)
from .Hint import Hint
from .ModifyMovieDialogUI import Ui_ModifyMovieDialog


class ModifyMovieDialog(QDialog, Ui_ModifyMovieDialog):
    def __init__(self, filmID=None, refreshAction=None, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
        self.SecondPageFrame.hide()

        if refreshAction is not None:
            self.accepted.connect(refreshAction)

        self.filmID = filmID
        self.companyID = None
        self.genres = []
        self.directors = []
        self.casts = []

        self.modifier = FilmInterface(True)
        self.companySelector = CompanyInterface(False)

        if filmID is not None:
            self.loadInfo()
            self.loadGenres()
            self.loadDirectors()
            self.loadCasts()

    def loadInfo(self):
        self.modifier.selectFilm(self.filmID)
        result = self.modifier.fetchResult()

        if len(result) == 0:
            raise Exception('attempted to modify a ghost film')

        chineseName = getColumn(result[0], FILM_VIEW.chineseName)
        originalName = getColumn(result[0], FILM_VIEW.originalName)
        picture = getColumn(result[0], FILM_VIEW.picture)
        length = getColumn(result[0], FILM_VIEW.length)
        releaseDate = getColumn(result[0], FILM_VIEW.releaseDate)

        if chineseName is not None:
            self.MovieName.setText(chineseName)
        if originalName is not None:
            self.OriginalName.setText(originalName)
        if picture is not None:
            self.Picture.setText(picture)
        if length is not None:
            self.MovieLength.setValue(length)
        if releaseDate is not None:
            self.ReleaseDate.setDate(QDate.fromString(f'{releaseDate}', 'yyyy-MM-dd'))

        self.companyID = getColumn(result[0], FILM_VIEW.companyID)
        companyName = getColumn(result[0], FILM_VIEW.companyName)

        if companyName is not None:
            self.ProductionCompany.setText(companyName)

        storyline = getColumn(result[0], FILM_VIEW.storyline)
        prizeHistory = getColumn(result[0], FILM_VIEW.prizeHistory)
        remark = getColumn(result[0], FILM_VIEW.remark)

        if storyline is not None:
            self.Storyline.setPlainText(storyline)
        if prizeHistory is not None:
            self.PrizeHistory.setPlainText(prizeHistory)
        if remark is not None:
            self.Remark.setPlainText(remark)

    def loadGenres(self):
        self.modifier.selectFilmGenre(self.filmID)
        result = self.modifier.fetchResult()
        self.GenreTable.setRowCount(len(result))

        for index, row in enumerate(result):
            genreID = getColumn(row, GENRE_TABLE.id)
            genreName = getColumn(row, GENRE_TABLE.name)

            self.genres.append(genreID)
            self.GenreTable.setItem(index, 0, QTableWidgetItem(genreName))

    def loadDirectors(self):
        self.modifier.selectFilmDirectingInfo(self.filmID)
        result = self.modifier.fetchResult()
        self.DirectorTable.setRowCount(len(result))

        for index, row in enumerate(result):
            directorID = getColumn(row, DIRECTOR_TABLE.id)
            directorName = getColumn(row, DIRECTOR_TABLE.name)
            directorRole = getColumn(row, DIRECTING_TABLE.role)

            self.directors.append(directorID)
            self.DirectorTable.setItem(index, 0, QTableWidgetItem(directorName))
            self.DirectorTable.setItem(index, 1, QTableWidgetItem(directorRole))

    def loadCasts(self):
        self.modifier.selectFilmPlayInfo(self.filmID)
        result = self.modifier.fetchResult()
        self.CastTable.setRowCount(len(result))

        for index, row in enumerate(result):
            castID = getColumn(row, CAST_TABLE.id)
            castName = getColumn(row, CAST_TABLE.name)
            castRole = getColumn(row, PLAY_TABLE.role)

            self.casts.append(castID)
            self.CastTable.setItem(index, 0, QTableWidgetItem(castName))
            self.CastTable.setItem(index, 1, QTableWidgetItem(castRole))

    def modifyMovie(self):
        chineseName = self.MovieName.text()
        if chineseName == '':
            chineseName = None

        originalName = self.OriginalName.text()
        if originalName == '':
            originalName = None

        picture = self.Picture.text()
        if picture == '':
            picture = None

        length = self.MovieLength.value()
        releaseDate = self.ReleaseDate.date().toString('yyyy-MM-dd')

        self.modifier.updateFilmBasic(self.filmID,
                                      filmChineseName=chineseName,
                                      filmOriginalName=originalName,
                                      releaseDate=releaseDate,
                                      length=length,
                                      companyID=self.companyID,
                                      picture=picture)

        storyline = self.Storyline.toPlainText()
        self.modifier.updateFilmStoryline(self.filmID, None if storyline == '' else storyline)

        prizeHistory = self.PrizeHistory.toPlainText()
        self.modifier.updateFilmPrizeHistory(self.filmID,
                                             None if prizeHistory == '' else prizeHistory)

        remark = self.Remark.toPlainText()
        self.modifier.updateFilmRemark(self.filmID, None if remark == '' else remark)

        self.modifyGenres()
        self.modifyDirectors()
        self.modifyCasts()

        dialog = Hint("修改成功", parent=self.parent(), flags=Qt.WindowTitleHint)
        dialog.open()
        self.accept()

    def modifyGenres(self):
        self.modifier.updateFilmGenre(self.filmID, self.genres)

    def modifyDirectors(self):
        roles = [self.DirectorTable.item(i, 1).text() for i in range(self.DirectorTable.rowCount())]
        self.modifier.updateFilmDirectingInfo(self.filmID, self.directors, roles)

    def modifyCasts(self):
        roles = [self.CastTable.item(i, 1).text() for i in range(self.CastTable.rowCount())]
        self.modifier.updateFilmPlayInfo(self.filmID, self.casts, roles)

    def toNextPage(self):
        self.FirstPageFrame.hide()
        self.SecondPageFrame.show()

    def toPreviousPage(self):
        self.FirstPageFrame.show()
        self.SecondPageFrame.hide()
