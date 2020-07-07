from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from ..DBInterface import GENRE_TABLE, GenreInterface, getColumn
from .FilmGenreDialogUI import Ui_FilmGenreDialog


class FilmGenreDialog(QDialog, Ui_FilmGenreDialog):
    def __init__(self, action, genreID=None, others=(), parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        self.genres = []
        self.genreSelector = GenreInterface(False)
        self.action = action
        self.others = others

        if genreID is not None:
            self.genreSelector.selectGenre(genreID)
            result = self.genreSelector.fetchResult(1)

            if len(result) == 0:
                raise RuntimeError('attempted to locate a ghost genre')

            genreName = getColumn(result[0], GENRE_TABLE.name)
            self.SearchText.setText(genreName)

        self.refresh()

    def refresh(self):
        self.genres = []
        self.genreSelector.searchGenre(self.SearchText.text())
        result = self.genreSelector.fetchResult(50)
        self.SearchResult.clearContents()
        self.SearchResult.setRowCount(len(result))

        index = 0

        for row in result:
            genreID = getColumn(row, GENRE_TABLE.id)
            name = getColumn(row, GENRE_TABLE.name)

            if genreID in self.others:
                self.SearchResult.setRowCount(self.SearchResult.rowCount() - 1)
                continue

            self.genres.append(genreID)
            self.SearchResult.setItem(index, 0,
                                      QTableWidgetItem(name if name is not None else '--'))
            index = index + 1

    def tryAccept(self):
        selected = self.SearchResult.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '选择电影分类', '请先选择一个分类！')
            return

        row = self.SearchResult.row(selected[0])
        self.action(self.genres[row], self.SearchResult.item(row, 0).text())
        self.accept()
