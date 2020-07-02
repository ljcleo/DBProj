from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QDialog

from .HintUI import Ui_Hint


class Hint(QDialog, Ui_Hint):
    def __init__(self, text, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
        self.label.setText(text)
        self.Timer = QTimer()
        self.Timer.start(1000)
        self.Timer.timeout.connect(self.close)
