from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from .CommentWidgetUI import Ui_CommentWidget


class CommentWidget(QWidget, Ui_CommentWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
