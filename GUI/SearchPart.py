from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

from .SearchResultButton import SearchResultButtonWidget

from .SearchResultPartUI import Ui_SearchResultPart


class SearchResultPart(Ui_SearchResultPart):
    def setupSearchResult(self, SearchResultPart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(SearchResultPart)

        # set the width of columns
        self.tableWidget.setColumnWidth(0, 150) # title
        self.tableWidget.setColumnWidth(1, 50)  # country
        self.tableWidget.setColumnWidth(2, 120) # release date
        self.tableWidget.setColumnWidth(3, 140) # cast
        self.tableWidget.setColumnWidth(4, 50)  # rate
        self.tableWidget.setColumnWidth(5, 120) # operations

        self.buttons=[]
        for row in range(self.tableWidget.rowCount()):
            button = SearchResultButtonWidget()
            button.MovieButton.clicked.connect(self.toMovie)
            if self.login == 0:
                button.login = 0
            else:
                button.login = 1
            self.buttons.append(button)
            self.tableWidget.setCellWidget(row, 5, button)

    def hideSearchResult(self):
        self.SearchResultFrame.hide()

    def showSearchResult(self):
        self.SearchResultFrame.show()

    def returnRecommendation(self):
        self.hideSearchResult()
        self.showRecommendation()

    def refreshSearchButton(self):
        if self.login == 1:
            for button in self.buttons:
                button.login = 1
        else:
            for button in self.buttons:
                button.login = 0

    def toMovie(self):
        self.hideSearchResult()
        self.hideSearch()
        self.showInformation()

    def modifyFilm(self):
        pass