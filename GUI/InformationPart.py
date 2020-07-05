import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel

from .AllCastDialog import AllCastDialog
from .AllDirectorDialog import AllDirectorDialog
from .CommentDialog import CommentDialog
from .Hint import Hint
from .InformationPartUI import Ui_InformationPart


class InformationPart(Ui_InformationPart):
    def setupInformation(self, InformationPart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(InformationPart)
        self.showInformationImage(
            'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p513344864.jpg')

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

    def showInformationImage(self, url):
        res = requests.get(url)
        image = QImage.fromData(res.content)

        picture = QLabel(self.InformationFrame)
        picture.setPixmap(QPixmap.fromImage(image))
        picture.setGeometry(40, 40, 180, 254)
        picture.setScaledContents(True)

    def showAllDirector(self):
        dialog = AllDirectorDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()

    def showAllCast(self):
        dialog = AllCastDialog(parent=self, flags=Qt.WindowTitleHint)
        dialog.open()
