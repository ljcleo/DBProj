from random import randint

from PyQt5.QtGui import QImage, QPixmap
from requests import get as getURL
from requests.exceptions import RequestException

from ..DBInterface import FILM_TABLE, FilmInterface, getColumn
from .HomepagePartUI import Ui_HomepagePart


class HomepagePart(Ui_HomepagePart):
    def setupHomepage(self, HomepagePart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(HomepagePart)
        self.makeRecommendationInfo()

    def showHomepage(self):
        self.makeRecommendationInfo()  # Is this necessary? Maybe a refresh button is needed?
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
        # if self.login is None:
        return (randint(1, 10000), randint(1, 10000), randint(1, 10000))
        # else:
        #     file_path = 'recommendation.txt'
        #     with open(file_path, 'r') as f:
        #         for i in f.readlines():
        #             if self.login == i.split(',')[0]:
        #                 return i.strip().split(',')[1:]
