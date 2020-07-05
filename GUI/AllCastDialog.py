from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .AllCastDialogUI import Ui_AllCastDialog


class AllCastDialog(QDialog, Ui_AllCastDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
