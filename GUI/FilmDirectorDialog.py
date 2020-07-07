from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from ..DBInterface import DIRECTOR_TABLE, DirectorInterface, getColumn
from .FilmDirectorDialogUI import Ui_FilmDirectorDialog


class FilmDirectorDialog(QDialog, Ui_FilmDirectorDialog):
    def __init__(self, action, directorID=None, role=None, others=(), parent=None,
                 flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        self.directors = []
        self.directorSelector = DirectorInterface(False)
        self.action = action
        self.others = others

        if directorID is not None:
            self.directorSelector.selectDirector(directorID)
            result = self.directorSelector.fetchResult(1)

            if len(result) == 0:
                raise RuntimeError('attempted to locate a ghost director')

            directorName = getColumn(result[0], DIRECTOR_TABLE.name)
            self.SearchText.setText(directorName)

        if role is not None:
            self.Role.setText(role)

        self.refresh()

    def refresh(self):
        self.directors = []
        self.directorSelector.searchDirector(self.SearchText.text())
        result = self.directorSelector.fetchResult(50)
        self.SearchResult.clearContents()
        self.SearchResult.setRowCount(len(result))

        index = 0

        for row in result:
            directorID = getColumn(row, DIRECTOR_TABLE.id)
            name = getColumn(row, DIRECTOR_TABLE.name)
            alt = getColumn(row, DIRECTOR_TABLE.alt)

            if directorID in self.others:
                self.SearchResult.setRowCount(self.SearchResult.rowCount() - 1)
                continue

            self.directors.append(directorID)
            self.SearchResult.setItem(index, 0,
                                      QTableWidgetItem(name if name is not None else '--'))
            self.SearchResult.setItem(index, 1,
                                      QTableWidgetItem(alt if alt is not None else '--'))

            index = index + 1

    def openLink(self, row, column):
        url = self.SearchResult.item(row, 1).text()
        if url != '--' and column == 1:
            QDesktopServices.openUrl(QUrl(url))

    def tryAccept(self):
        selected = self.SearchResult.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '选择电影导演', '请先选择一个导演！')
            return

        row = self.SearchResult.row(selected[0])
        self.action(self.directors[row], self.SearchResult.item(row, 0).text(), self.Role.text())
        self.accept()
