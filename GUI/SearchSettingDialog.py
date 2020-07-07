from PyQt5.QtCore import Qt
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

    def setSearch(self):
        ratingLow = self.RatingLow.text()
        ratingHigh = self.RatingHigh.text()

        if ratingLow == '0.0' and ratingHigh == '10.0':
            self.parent().rating = None
        else:
            self.parent().rating = (ratingLow, ratingHigh)

        dateLow = self.DateLow.text()
        dateHigh = self.DateHigh.text()
        self.parent().releaseDate = (dateLow, dateHigh)

        genre = self.Genre.currentData()
        if genre != -1:
            self.parent().genreID = genre

        Hint("设置成功！", parent=self.parent(), flags=Qt.WindowTitleHint).open()
        self.parent().showSearchResult(self.parent().search)
        self.accept()
