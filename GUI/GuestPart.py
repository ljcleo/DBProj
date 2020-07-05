from PyQt5.QtCore import Qt

from .GuestPartUI import Ui_GuestPart

from .LoginDialog import LoginDialog


class GuestPart(Ui_GuestPart):
    def setupGuest(self, GuestPart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(GuestPart)

    def loginOrRegister(self):
        dialog = LoginDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()

    def hideGuest(self):
        self.GuestFrame.hide()

    def showGuest(self):
        self.GuestFrame.show()


