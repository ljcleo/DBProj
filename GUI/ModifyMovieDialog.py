from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .Hint import Hint
from .ModifyMovieDialogUI import Ui_ModifyMovieDialog


class ModifyMovieDialog(QDialog, Ui_ModifyMovieDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

    def modifyMovie(self):
        newMovieName = self.MovieName.text()
        newDate = self.ReleaseDate.text()
        newProduction = self.ProductionCompany.text()
        print(newMovieName, newDate, newProduction)
        dialog = Hint("修改成功", parent=self.parent(), flags=Qt.WindowTitleHint)
        dialog.open()
        self.accept()
