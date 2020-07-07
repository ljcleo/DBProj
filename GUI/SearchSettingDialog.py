from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ..DBInterface import GENRE_TABLE, GenreInterface
from .SearchSettingDialogUI import Ui_SearchSettingDialog
from .Hint import Hint


class SearchSettingDialog(QDialog, Ui_SearchSettingDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def setSearch(self):
        Hint("设置成功！", parent=self.parent(), flags=Qt.WindowTitleHint).open()
        self.accept()

        dateLow = self.DateLow.text()
        dateHigh = self.DateHigh.text()
        rateLow = self.RateLow.text()
        rateHigh = self.RateHigh.text()
        genre = self.Genre2.currentText()

        if genre != '不限':
            searchEngine = GenreInterface(False)
            searchEngine.searchGenreIDByName(genre)
            result = searchEngine.fetchResult()
            self.parent().genreID = result[0][0]
            print(genre, self.parent().genreID)

        self.parent().releaseDate = (dateLow, dateHigh)

        if rateLow == '0.0' and rateHigh == '10.0':
            self.parent().rating = None
        else:
            self.parent().rating = (rateLow, rateHigh)

        self.parent().showSearchResult(self.parent().search)
