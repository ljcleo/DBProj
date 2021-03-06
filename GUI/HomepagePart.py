from PyQt5.QtGui import QImage, QPixmap
from requests import get as getURL
from requests.exceptions import RequestException

from ..DBInterface import FILM_TABLE, FilmInterface, getColumn
from ..RecommendationSystem import RecommendationSystem
from .HomepagePartUI import Ui_HomepagePart


class HomepagePart(Ui_HomepagePart):
    def setupHomepage(self, HomepagePart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(HomepagePart)

        self.Recommendation1.enterEvent = self.RecommendationTitle1.enterEvent
        self.Recommendation1.leaveEvent = self.RecommendationTitle1.leaveEvent
        self.Recommendation2.enterEvent = self.RecommendationTitle2.enterEvent
        self.Recommendation2.leaveEvent = self.RecommendationTitle2.leaveEvent
        self.Recommendation3.enterEvent = self.RecommendationTitle3.enterEvent
        self.Recommendation3.leaveEvent = self.RecommendationTitle3.leaveEvent

        self.recommendationSystem = RecommendationSystem(self.login)
        self.makeRecommendationInfo()

    def showHomepage(self):
        self.makeRecommendationInfo()
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
        self.showInformation(self.recommendations[0])
        self.hideHomepage()

    def movie2(self):
        self.showInformation(self.recommendations[1])
        self.hideHomepage()

    def movie3(self):
        self.showInformation(self.recommendations[2])
        self.hideHomepage()

    def search(self):
        self.hideRecommendation()
        self.showSearchResult(self.SearchInput.text())

    def makeRecommendationInfo(self):
        self.recommendations = self.__generateRecommendation()

        pictures = (self.RecommendationPicture1, self.RecommendationPicture2,
                    self.RecommendationPicture3)
        titles = (self.RecommendationTitle1, self.RecommendationTitle2, self.RecommendationTitle3)

        posterFetcher = FilmInterface(False)

        for i in range(3):
            posterFetcher.selectFilm(self.recommendations[i])
            result = posterFetcher.fetchResult()

            if len(result) == 0:
                raise RuntimeError('the recommendation algorithm has suggested a ghost film')

            name = getColumn(result[0], FILM_TABLE.chineseName)
            url = getColumn(result[0], FILM_TABLE.picture)
            titles[i].setText(name)
            pictures[i].clear()

            if url is not None:
                try:
                    res = getURL(url, timeout=20)
                    if res.status_code != 200:
                        raise RequestException()

                    image = QImage.fromData(res.content)
                    pictures[i].setPixmap(QPixmap.fromImage(image))
                except RequestException:
                    pictures[i].setText('海报加载失败')
            else:
                pictures[i].setText('暂无海报')

    def __generateRecommendation(self):
        return self.recommendationSystem.makeRecommendation(3)
