import requests
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QLabel

from .HomepagePartUI import Ui_HomepagePart


class HomepagePart(Ui_HomepagePart):
    def setupHomepage(self, HomepagePart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(HomepagePart)
        url1 = 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p513344864.jpg'
        url2 = 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p513344864.jpg'
        url3 = 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p513344864.jpg'
        self.showRecommendationImage(url1, url2, url3)

    def showHomepage(self):
        self.SearchFrame.show()
        self.RecommendationFrame.show()
        self.HLineSearch.show()
        self.Search.setAutoDefault(True)
        self.Search.setDefault(True)

    def hideHomepage(self):
        self.SearchFrame.hide()
        self.RecommendationFrame.hide()
        self.HLineSearch.hide()
        self.Search.setAutoDefault(False)
        self.Search.setDefault(False)

    def hideSearch(self):
        self.SearchFrame.hide()
        self.HLineSearch.hide()
        self.Search.setAutoDefault(False)
        self.Search.setDefault(False)

    def showSearch(self):
        self.SearchFrame.show()
        self.HLineSearch.show()
        self.Search.setAutoDefault(True)
        self.Search.setAutoDefault(True)

    def hideRecommendation(self):
        self.RecommendationFrame.hide()

    def showRecommendation(self):
        self.RecommendationFrame.show()

    def movie1(self):
        self.showInformation()
        self.hideHomepage()

    def movie2(self):
        self.showInformation()
        self.hideHomepage()

    def movie3(self):
        self.showInformation()
        self.hideHomepage()

    def search(self):
        self.hideRecommendation()
        self.showSearchResult(self.SearchInput.text())

    def showRecommendationImage(self, url1, url2, url3):
        # Get the pictures from the Internet then show them in GUI
        res = requests.get(url1)
        image = QImage.fromData(res.content)
        picture = QLabel(self.RecommendationFrame)
        picture.setPixmap(QPixmap.fromImage(image))
        picture.setGeometry(20, 80, 180, 254)
        picture.setScaledContents(True)

        res = requests.get(url2)
        image = QImage.fromData(res.content)
        picture = QLabel(self.RecommendationFrame)
        picture.setPixmap(QPixmap.fromImage(image))
        picture.setGeometry(250, 80, 180, 254)
        picture.setScaledContents(True)

        res = requests.get(url3)
        image = QImage.fromData(res.content)
        picture = QLabel(self.RecommendationFrame)
        picture.setPixmap(QPixmap.fromImage(image))
        picture.setGeometry(480, 80, 180, 254)
        picture.setScaledContents(True)
