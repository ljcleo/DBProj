from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QDialog

from ..DBInterface import GENRE_TABLE, GenreInterface, getColumn
from .Hint import Hint
from .SearchSettingDialogUI import Ui_SearchSettingDialog


class SearchSettingDialog(QDialog, Ui_SearchSettingDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
        self.Genre.addItem('不限', userData=-1)

        genreFetcher = GenreInterface(False)
        genreFetcher.selectAllGenre()
        result = genreFetcher.fetchResult()

        for row in result:
            genreID = getColumn(row, GENRE_TABLE.id)
            name = getColumn(row, GENRE_TABLE.name)

            if name is not None:
                self.Genre.addItem(name, genreID)

        curRating = self.parent().rating
        curDate = self.parent().releaseDate
        curGenre = self.parent().genreID

        if curRating is not None:
            curRatingLow, curRatingHigh = curRating
            self.RatingLow.setValue(curRatingLow)
            self.RatingHigh.setValue(curRatingHigh)

        if curDate is not None:
            curDateLow, curDateHigh = curDate
            self.DateLow.setDate(QDate.fromString(curDateLow, 'yyyy-MM-dd'))
            self.DateHigh.setDate(QDate.fromString(curDateHigh, 'yyyy-MM-dd'))

        if curGenre is None:
            self.Genre.setCurrentIndex(0)
        else:
            index = self.Genre.findData(curGenre)
            self.Genre.setCurrentIndex(index)

    def setSearch(self):
        ratingLow = self.RatingLow.value()
        ratingHigh = self.RatingHigh.value()

        if ratingLow == 0 and ratingHigh == 10:
            self.parent().rating = None
        else:
            self.parent().rating = (ratingLow, ratingHigh)

        dateLow = self.DateLow.date().toString('yyyy-MM-dd')
        dateHigh = self.DateHigh.date().toString('yyyy-MM-dd')
        self.parent().releaseDate = (dateLow, dateHigh)

        genre = self.Genre.currentData()
        self.parent().genreID = None if genre == -1 else genre

        Hint("设置成功！", parent=self.parent(), flags=Qt.WindowTitleHint).open()
        self.parent().showSearchResult(self.parent().search)
        self.accept()
