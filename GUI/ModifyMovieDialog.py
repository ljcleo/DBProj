from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .ModifyMovieDialogUI import Ui_ModifyMovieDialog

from .Hint import Hint
from .ModifyMoreDialog import ModifyMoreDialog


class ModifyMovieDialog(QDialog, Ui_ModifyMovieDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def modifyMovie(self):
        newmoviename = self.MovieName.text()
        newdate = self.ReleaseDate.text()
        newproduction = self.ProductionCompany.text()
        print(newmoviename, newdate, newproduction)
        dialog = Hint("修改成功", parent=self, flags=Qt.WindowTitleHint)
        dialog.open()
        self.accept()

    def modifyMore(self):
        dialog = ModifyMoreDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()
