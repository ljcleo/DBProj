from PyQt5.QtCore import Qt

from .InformationPartUI import Ui_InformationPart

from .CommentDialog import CommentDialog
from .Hint import Hint


class InformationPart(Ui_InformationPart):
    def setupInformation(self, InformationPart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(InformationPart)

    def addComment(self):
        if self.login == 0:
            dialog = Hint("您还未登录，无法评论！", parent=self, flags=Qt.WindowTitleHint)
            dialog.open()
        else:
            dialog = CommentDialog(parent=self, flags=Qt.WindowTitleHint)
            dialog.open()

    def hideInformation(self):
        self.InformationFrame.hide()
        self.HLineMovie.hide()
        self.CommentFrame.hide()
        self.AddComment.setAutoDefault(False)
        self.AddComment.setDefault(False)

    def showInformation(self):
        self.InformationFrame.show()
        self.HLineMovie.show()
        self.CommentFrame.show()
        self.AddComment.setAutoDefault(True)
        self.AddComment.setDefault(True)

    def returnHomepage(self):
        self.hideInformation()
        self.showHomepage()