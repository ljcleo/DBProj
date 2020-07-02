from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .AllDirectorDialogUI import Ui_AllDirectorDialog


class AllDirectorDialog(QDialog, Ui_AllDirectorDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
