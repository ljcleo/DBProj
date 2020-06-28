from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from .Hint import Hint
from .SearchResultButtonUI import Ui_SearchResultButtonWidget


class SearchResultButtonWidget(QWidget, Ui_SearchResultButtonWidget):
    def __init__(self, text, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
        self.MovieButton.setText(text)

    def toMovie(self):
        dialog = Hint("暂不支持该功能！", parent=self, flags=Qt.WindowTitleHint)
        dialog.open()
