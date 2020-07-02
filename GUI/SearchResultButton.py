from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from .SearchResultButtonUI import Ui_SearchResultButtonWidget

from .Hint import Hint


class SearchResultButtonWidget(QWidget, Ui_SearchResultButtonWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
        # self.MovieButton.setText(text)

    def toMovie(self):
        #dialog = Hint("暂不支持该功能！", parent=self, flags=Qt.WindowTitleHint)
        #dialog.open()
        pass

    def deleteMovie(self):
        if self.login == 0:
            dialog = Hint("您还未登录，无法操作！", parent=self, flags=Qt.WindowTitleHint)
            dialog.open()
        else:
            dialog = Hint("您不是管理员，无法操作！", parent=self, flags=Qt.WindowTitleHint)
            dialog.open()

    def modifyMovie(self):
        if self.login == 0:
            dialog = Hint("您还未登录，无法操作！", parent=self, flags=Qt.WindowTitleHint)
            dialog.open()
        else:
            dialog = Hint("您不是管理员，无法操作！", parent=self, flags=Qt.WindowTitleHint)
            dialog.open()