from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from ..DBInterface import (DIRECTING_TABLE, DIRECTOR_TABLE, CAST_TABLE,
                           FILM_VIEW, GENRE_TABLE, PLAY_TABLE,
                           CompanyInterface, FilmInterface, getColumn)
from .FilmCastDialog import FilmCastDialog
from .FilmCompanyDialog import FilmCompanyDialog
from .FilmDirectorDialog import FilmDirectorDialog
from .FilmGenreDialog import FilmGenreDialog
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
        if self.companyID is None:
            QMessageBox.critical(self, '添加/修改电影', '制作公司不能为空！')
            return

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

        storyline = self.Storyline.toPlainText()
        if storyline == '':
            storyline = None

        prizeHistory = self.PrizeHistory.toPlainText()
        if prizeHistory == '':
            prizeHistory = None

        remark = self.Remark.toPlainText()
        if remark == '':
            remark = None

        if self.filmID is not None:
            self.modifier.updateFilmBasic(self.filmID,
                                          filmChineseName=chineseName,
                                          filmOriginalName=originalName,
                                          releaseDate=releaseDate,
                                          length=length,
                                          companyID=self.companyID,
                                          picture=picture)

            self.modifier.updateFilmStoryline(self.filmID, storyline)
            self.modifier.updateFilmPrizeHistory(self.filmID, prizeHistory)
            self.modifier.updateFilmRemark(self.filmID, remark)
        else:
            self.modifier.insertFilm(filmChineseName=chineseName,
                                     filmOriginalName=originalName,
                                     releaseDate=releaseDate,
                                     length=length,
                                     companyID=self.companyID,
                                     picture=picture,
                                     storyline=storyline,
                                     prizeHistory=prizeHistory,
                                     remark=remark)

            result = self.modifier.fetchResult(1)
            if len(result) == 0:
                raise RuntimeError('film inserted into void')

            self.filmID = result[0][0]

        self.modifyGenres()
        self.modifyDirectors()
        self.modifyCasts()

        QMessageBox.information(self.parent(), '添加/修改电影', '添加/修改成功')
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

    def modifyCompany(self):
        def action(companyID, name):
            if companyID is None:
                raise RuntimeError('cannot ignore company column')

            self.companyID = companyID
            self.ProductionCompany.setText(name)

        FilmCompanyDialog(action, self.companyID, parent=self, flags=Qt.Drawer).open()

    def addGenre(self):
        def action(genreID, name):
            if genreID is None:
                raise RuntimeError('cannot insert null genre')

            self.genres.append(genreID)
            self.GenreTable.setRowCount(len(self.genres))
            self.GenreTable.setItem(len(self.genres) - 1, 0, QTableWidgetItem(name))

        FilmGenreDialog(action, others=tuple(self.genres), parent=self, flags=Qt.Drawer).open()

    def modifyGenre(self):
        selected = self.GenreTable.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '修改分类', '请先选择一个分类再修改！')
            return

        row = self.GenreTable.row(selected[0])

        def action(genreID, name):
            if genreID is None:
                raise RuntimeError('cannot modify into null genre')

            self.genres[row] = genreID
            self.GenreTable.setItem(row, 0, QTableWidgetItem(name))

        others = self.genres.copy()
        del others[row]

        FilmGenreDialog(action, genreID=self.genres[row], others=tuple(others), parent=self,
                        flags=Qt.Drawer).open()

    def deleteGenre(self):
        selected = self.GenreTable.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '删除分类', '请先选择一个分类再删除！')
            return

        row = self.GenreTable.row(selected[0])
        result = QMessageBox.warning(self, '删除分类', '删除操作不可恢复，是否继续？',
                                     QMessageBox.Yes | QMessageBox.No)

        if result == QMessageBox.Yes:
            del self.genres[row]
            self.GenreTable.removeRow(row)

    def addDirector(self):
        def action(directorID, name, role):
            if directorID is None:
                raise RuntimeError('cannot insert null director')

            self.directors.append(directorID)
            self.DirectorTable.setRowCount(len(self.directors))
            self.DirectorTable.setItem(len(self.directors) - 1, 0, QTableWidgetItem(name))
            self.DirectorTable.setItem(len(self.directors) - 1, 1, QTableWidgetItem(role))

        FilmDirectorDialog(action, others=tuple(self.directors), parent=self,
                           flags=Qt.Drawer).open()

    def modifyDirector(self):
        selected = self.DirectorTable.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '修改导演', '请先选择一个导演再修改！')
            return

        row = self.DirectorTable.row(selected[0])

        def action(directorID, name, role):
            if directorID is None:
                raise RuntimeError('cannot modify into null director')

            self.directors[row] = directorID
            self.DirectorTable.setItem(row, 0, QTableWidgetItem(name))
            self.DirectorTable.setItem(row, 1, QTableWidgetItem(role))

        role = self.DirectorTable.item(row, 1).text()
        if role == '--':
            role = None

        others = self.directors.copy()
        del others[row]

        FilmDirectorDialog(action, directorID=self.directors[row], role=role, others=tuple(others),
                           parent=self, flags=Qt.Drawer).open()

    def deleteDirector(self):
        selected = self.DirectorTable.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '删除导演', '请先选择一个导演再删除！')
            return

        row = self.DirectorTable.row(selected[0])
        result = QMessageBox.warning(self, '删除导演', '删除操作不可恢复，是否继续？',
                                     QMessageBox.Yes | QMessageBox.No)

        if result == QMessageBox.Yes:
            del self.directors[row]
            self.DirectorTable.removeRow(row)

    def addCast(self):
        def action(castID, name, role):
            if castID is None:
                raise RuntimeError('cannot insert null cast')

            self.casts.append(castID)
            self.CastTable.setRowCount(len(self.casts))
            self.CastTable.setItem(len(self.casts) - 1, 0, QTableWidgetItem(name))
            self.CastTable.setItem(len(self.casts) - 1, 1, QTableWidgetItem(role))

        FilmCastDialog(action, others=tuple(self.casts), parent=self, flags=Qt.Drawer).open()

    def modifyCast(self):
        selected = self.CastTable.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '修改演员', '请先选择一个演员再修改！')
            return

        row = self.CastTable.row(selected[0])

        def action(castID, name, role):
            if castID is None:
                raise RuntimeError('cannot modify into null cast')

            self.casts[row] = castID
            self.CastTable.setItem(row, 0, QTableWidgetItem(name))
            self.CastTable.setItem(row, 1, QTableWidgetItem(role))

        role = self.CastTable.item(row, 1).text()
        if role == '--':
            role = None

        others = self.casts.copy()
        del others[row]

        FilmCastDialog(action, castID=self.casts[row], role=role, others=tuple(others), parent=self,
                       flags=Qt.Drawer).open()

    def deleteCast(self):
        selected = self.CastTable.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '删除演员', '请先选择一个演员再删除！')
            return

        row = self.CastTable.row(selected[0])
        result = QMessageBox.warning(self, '删除演员', '删除操作不可恢复，是否继续？',
                                     QMessageBox.Yes | QMessageBox.No)

        if result == QMessageBox.Yes:
            del self.casts[row]
            self.CastTable.removeRow(row)
