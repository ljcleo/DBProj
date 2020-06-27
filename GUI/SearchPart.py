from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

from .SearchResultButton import SearchResultButtonWidget

from .SearchResultPartUI import Ui_SearchResultPart


class SearchResultPart(Ui_SearchResultPart):
    def setupSearchResult(self, SearchResultPart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(SearchResultPart)

        self.buttons=[]
        for row in range(self.tableWidget.rowCount()):
            button = SearchResultButtonWidget("你好")
            self.buttons.append(button)
            self.tableWidget.setCellWidget(row, 0, button)

    def hideSearchResult(self):
        self.SearchResultFrame.hide()

    def showSearchResult(self):
        self.SearchResultFrame.show()

    def returnRecommendation(self):
        self.hideSearchResult()
        self.showRecommendation()