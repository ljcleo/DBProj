from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from .HomepagePart import HomepagePart
from .InformationPart import InformationPart
from .UserPart import UserPart
from .GuestPart import GuestPart
from .SearchPart import SearchResultPart

from .MainPartUI import Ui_MainWindow


class MainWindow(QDialog, Ui_MainWindow, HomepagePart, InformationPart, SearchResultPart, UserPart, GuestPart):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.login = 0
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
        if self.login == 0:
            self.hideUser()
            self.showGuest()
        else:
            self.hideGuest()
            self.showUser()