from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from .SearchResultButtonUI import Ui_SearchResultButtonWidget


class SearchResultButtonWidget(QWidget, Ui_SearchResultButtonWidget):
    def __init__(self, toMovie, modifyMovie, deleteMovie, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        self.MovieButton.clicked.connect(toMovie)
        self.ModifyButton.clicked.connect(modifyMovie)
        self.DeleteButton.clicked.connect(deleteMovie)
