from PyQt5.QtCore import QSize, Qt, QUrl
from PyQt5.QtGui import QDesktopServices, QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem
from requests import get as getURL
from requests.exceptions import RequestException

from ..DBInterface import (DIRECTING_TABLE, DIRECTOR_TABLE, FilmInterface,
                           getColumn)
from .AllDirectorDialogUI import Ui_AllDirectorDialog


class AllDirectorDialog(QDialog, Ui_AllDirectorDialog):
    def __init__(self, filmID, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        directorFetcher = FilmInterface(False)
        directorFetcher.selectFilmDirectingInfo(filmID)
        result = directorFetcher.fetchResult()
        self.tableWidget.setRowCount(len(result))

        self.alts = {}

        for index, row in enumerate(result):
            avatar = getColumn(row, DIRECTOR_TABLE.avatar)
            name = getColumn(row, DIRECTOR_TABLE.name)
            role = getColumn(row, DIRECTING_TABLE.role)
            alt = getColumn(row, DIRECTOR_TABLE.alt)

            if avatar is not None:
                try:
                    avatarResponse = getURL(avatar, timeout=20)
                    if avatarResponse.status_code != 200:
                        raise RequestException()

                    avatarImage = QImage.fromData(avatarResponse.content)
                    avatarItem = QTableWidgetItem(QIcon(QPixmap.fromImage(avatarImage)), '')
                except RequestException:
                    avatarItem = QTableWidgetItem('海报加载失败')
            else:
                avatarItem = QTableWidgetItem('暂无海报')

            self.tableWidget.setItem(index, 0, avatarItem)
            self.tableWidget.setItem(index, 1, QTableWidgetItem('--' if name is None else name))
            self.tableWidget.setItem(index, 2, QTableWidgetItem('--' if role is None else role))

            if alt is None:
                self.tableWidget.setItem(index, 3, QTableWidgetItem('--'))
            else:
                self.tableWidget.setItem(index, 3, QTableWidgetItem(alt))
                self.alts[index] = alt

        self.tableWidget.setIconSize(QSize(90, 127))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def visitAltAtCell(self, row, column):
        if column == 3 and row in self.alts:
            QDesktopServices.openUrl(QUrl(self.alts[row]))
