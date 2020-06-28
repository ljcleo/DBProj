from .HomepagePartUI import Ui_HomepagePart


class HomepagePart(Ui_HomepagePart):
    def setupHomepage(self, HomepagePart):
        self.retranslateUi = super().retranslateUi
        super().setupUi(HomepagePart)

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
        text = self.SearchInput.text()
        print(text)
        self.hideRecommendation()
        self.showSearchResult()
