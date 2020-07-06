from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .GuestPart import GuestPart
from .HomepagePart import HomepagePart
from .InformationPart import InformationPart
from .MainPartUI import Ui_MainWindow
from .SearchResultPart import SearchResultPart
from .UserPart import UserPart


class MainWindow(QDialog, Ui_MainWindow, HomepagePart, InformationPart, SearchResultPart, UserPart,
                 GuestPart):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.login = None
        self.setupGuest(self)
        self.setupUser(self)
        self.setupSearchResult(self)
        self.setupHomepage(self)
        self.setupInformation(self)
        self.hideUser()
        self.hideSearchResult()
        self.hideInformation()
        self.setupUi(self)

    def refresh(self):
        if self.login is None:
            self.hideUser()
            self.showGuest()
        else:
            self.hideGuest()
            self.showUser()
