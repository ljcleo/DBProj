from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from ..DBInterface import CAST_TABLE, CastInterface, getColumn
from .FilmCastDialogUI import Ui_FilmCastDialog


class FilmCastDialog(QDialog, Ui_FilmCastDialog):
    def __init__(self, action, castID=None, role=None, others=(), parent=None,
                 flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        self.casts = []
        self.castSelector = CastInterface(False)
        self.action = action
        self.others = others

        if castID is not None:
            self.castSelector.selectCast(castID)
            result = self.castSelector.fetchResult(1)

            if len(result) == 0:
                raise RuntimeError('attempted to locate a ghost cast')

            castName = getColumn(result[0], CAST_TABLE.name)
            self.SearchText.setText(castName)

        if role is not None:
            self.Role.setText(role)

        self.refresh()

    def refresh(self):
        self.casts = []
        self.castSelector.searchCast(self.SearchText.text())
        result = self.castSelector.fetchResult(50)
        self.SearchResult.clearContents()
        self.SearchResult.setRowCount(len(result))

        index = 0

        for row in result:
            castID = getColumn(row, CAST_TABLE.id)
            name = getColumn(row, CAST_TABLE.name)
            alt = getColumn(row, CAST_TABLE.alt)

            if castID in self.others:
                self.SearchResult.setRowCount(self.SearchResult.rowCount() - 1)
                continue

            self.casts.append(castID)
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
            QMessageBox.information(self, '选择电影演员', '请先选择一个演员！')
            return

        row = self.SearchResult.row(selected[0])
        self.action(self.casts[row], self.SearchResult.item(row, 0).text(), self.Role.text())
        self.accept()
