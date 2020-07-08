from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from ..DBInterface import FILM_VIEW, FilmInterface, getColumn
from .ModifyMovieDialog import ModifyMovieDialog
from .SearchResultButton import SearchResultButtonWidget
from .SearchResultPartUI import Ui_SearchResultPart
from .SearchSettingDialog import SearchSettingDialog


class SearchResultPart(Ui_SearchResultPart):
    def setupSearchResult(self, SearchResultPart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(SearchResultPart)
        self.RateSortAsc.hide()
        self.DateSortAsc.hide()

        # set the width of columns
        self.tableWidget.setColumnWidth(0, 150)  # title
        self.tableWidget.setColumnWidth(1, 80)  # country
        self.tableWidget.setColumnWidth(2, 100)  # release date
        self.tableWidget.setColumnWidth(3, 140)  # genre
        self.tableWidget.setColumnWidth(4, 50)  # rate
        self.tableWidget.setColumnWidth(5, 120)  # operations

        # initialize search settings
        self.genreID = None
        self.releaseDate = None
        self.rating = None
        self.releaseDateOrder = None
        self.ratingOrder = None

    def hideSearchResult(self):
        self.SearchResultFrame.hide()

    def showSearchResult(self, searchText, genreID=None, releaseDate=None, rating=None,
                         releaseDateOrder=None, ratingOrder=None):
        genreID = self.genreID if genreID is None else genreID
        releaseDate = self.releaseDate if releaseDate is None else releaseDate
        rating = self.rating if rating is None else rating
        releaseDateOrder = self.releaseDateOrder if releaseDateOrder is None else releaseDate
        ratingOrder = self.ratingOrder if ratingOrder is None else ratingOrder

        self.tableWidget.clearContents()
        self.search = searchText
        searchEngine = FilmInterface(False)
        searchEngine.searchFilm(self.search, genreID=genreID, releaseDate=releaseDate,
                                rating=rating, releaseDateOrder=releaseDateOrder,
                                ratingOrder=ratingOrder)
        result = searchEngine.fetchResult(100)
        self.tableWidget.setRowCount(len(result))

        for index, row in enumerate(result):
            filmID = getColumn(row, FILM_VIEW.id)
            name = getColumn(row, FILM_VIEW.chineseName)
            nationality = getColumn(row, FILM_VIEW.companyNationality)
            releaseDate = getColumn(row, FILM_VIEW.releaseDate)
            genres = getColumn(row, FILM_VIEW.genres)
            rating = getColumn(row, FILM_VIEW.rating)

            self.tableWidget.setItem(
                index, 0, QTableWidgetItem('--' if name is None else name))
            self.tableWidget.setItem(
                index, 1, QTableWidgetItem('--' if nationality is None else nationality))
            self.tableWidget.setItem(
                index, 2, QTableWidgetItem('--' if releaseDate is None else f'{releaseDate}'))
            self.tableWidget.setItem(
                index, 3, QTableWidgetItem('--' if genres is None else genres))
            self.tableWidget.setItem(
                index, 4, QTableWidgetItem('--' if rating is None else f'{rating:.1f}'))

            self.tableWidget.setCellWidget(
                index, 5, SearchResultButtonWidget(self.generateToMovie(filmID),
                                                   self.generateModifyMovie(filmID),
                                                   self.generateDeleteMovie(filmID)))

        self.SearchResultFrame.show()

    def returnRecommendation(self):
        self.hideSearchResult()
        self.showRecommendation()

    def generateToMovie(self, filmID):
        def toMovie():
            self.hideSearchResult()
            self.hideSearch()
            self.showInformation(filmID)

        return toMovie

    def generateModifyMovie(self, filmID):
        def modifyMovie():
            if not self.loginAdmin:
                QMessageBox.critical(self, '修改电影信息', '您没有修改电影信息的权限！')
                return

            dialog = ModifyMovieDialog(filmID, lambda: self.showSearchResult(self.search),
                                       parent=self, flags=Qt.WindowTitleHint)
            dialog.open()

        return modifyMovie

    def generateDeleteMovie(self, filmID):
        def deleteMovie():
            if not self.loginAdmin:
                QMessageBox.critical(self, '删除电影', '您没有删除电影的权限！')
                return

            result = QMessageBox.warning(self, '删除电影', '删除操作不可恢复，是否继续？',
                                         QMessageBox.Yes | QMessageBox.No)

            if result == QMessageBox.Yes:
                filmDeleter = FilmInterface(True)
                filmDeleter.deleteFilm(filmID)

                filmDeleter.selectFilm(filmID)
                result = filmDeleter.fetchResult()

                if len(result) == 0:
                    QMessageBox.information(self, '删除电影', '电影删除成功！')
                else:
                    QMessageBox.information(self, '删除电影', '电影删除失败？！')

                self.showSearchResult(self.search)

        return deleteMovie

    def setSearch(self):
        dialog = SearchSettingDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()

    def sortDefault(self):
        self.showSearchResult(self.SearchInput.text())

    def sortByDateAsc(self):
        self.releaseDateOrder = False
        self.ratingOrder = None
        self.showSearchResult(self.SearchInput.text())
        self.DateSortAsc.hide()
        self.DateSortDesc.show()

    def sortByDateDesc(self):
        self.releaseDateOrder = True
        self.ratingOrder = None
        self.showSearchResult(self.SearchInput.text())
        self.DateSortAsc.show()
        self.DateSortDesc.hide()

    def sortByRateAsc(self):
        self.releaseDateOrder = None
        self.ratingOrder = False
        self.showSearchResult(self.SearchInput.text())
        self.RateSortAsc.hide()
        self.RateSortDesc.show()

    def sortByRateDesc(self):
        self.releaseDateOrder = None
        self.ratingOrder = True
        self.showSearchResult(self.SearchInput.text())
        self.RateSortAsc.show()
        self.RateSortDesc.hide()

    def addMovie(self):
        dialog = ModifyMovieDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()
