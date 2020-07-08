import numpy as np

from .DBInterface import (COMMENT_TABLE, FILM_GENRE_TABLE, GENRE_TABLE,
                          CommentInterface, FilmInterface, GenreInterface,
                          getColumn)


class RecommendationSystem():
    def __init__(self, userID=None):
        self.candidateFilms = []
        self.genreIndex = {}
        self.genres = []

        genreLoader = GenreInterface(False)
        genreLoader.selectAllGenre()
        genreList = genreLoader.fetchResult()

        self.selector = FilmInterface(False)

        for index, row in enumerate(genreList):
            genreID = getColumn(row, GENRE_TABLE.id)
            self.genreIndex[genreID] = index
            self.genres.append(genreID)

            self.selector._custom(f'SELECT TOP 20 PERCENT WITH TIES {FILM_GENRE_TABLE.filmID} '
                                  f'FROM {FILM_GENRE_TABLE.table} '
                                  f'WHERE {FILM_GENRE_TABLE.genreID} = ? ORDER BY NEWID()',
                                  (genreID, ))

            result = self.selector.fetchResult()
            self.candidateFilms.append(tuple(getColumn(r, FILM_GENRE_TABLE.filmID) for r in result))

        self.genreRatio = np.array([float(len(films)) for films in self.candidateFilms])
        self.genreRatio /= np.sum(self.genreRatio)
        self.customizeRatio(userID)

    def customizeRatio(self, userID):
        self.customRatio = np.zeros(len(self.genres))
        if userID is None:
            return

        commentLoader = CommentInterface(False)
        commentLoader._custom(f'SELECT {COMMENT_TABLE.filmID}, {COMMENT_TABLE.userID}, '
                              f'{COMMENT_TABLE.rating} FROM {COMMENT_TABLE.table}', ())

        commentList = commentLoader.fetchResult()
        if len(commentList) == 0:
            return

        filmList = {getColumn(row, COMMENT_TABLE.filmID) for row in commentList}
        userList = {getColumn(row, COMMENT_TABLE.userID) for row in commentList}
        if userID not in userList:
            return

        filmIndex = {film: index for index, film in enumerate(filmList)}
        userIndex = {user: index for index, user in enumerate(userList)}
        ratings = np.zeros((len(filmList), len(userList)))

        for row in commentList:
            film = getColumn(row, COMMENT_TABLE.filmID)
            user = getColumn(row, COMMENT_TABLE.userID)
            rating = getColumn(row, COMMENT_TABLE.rating)
            ratings[userIndex[user], filmIndex[film]] = rating

        ratings /= np.sqrt(np.sum(ratings ** 2, axis=1, keepdims=True))
        similarity = ratings.dot(ratings.T)
        prediction = similarity.dot(ratings)
        userRecommendRating = prediction[userIndex[user], :]

        for filmID in filmList:
            curRatio = userRecommendRating[filmIndex[filmID]]
            self.selector.selectFilmGenre(filmID)
            result = self.selector.fetchResult()

            for row in result:
                genreID = getColumn(row, FILM_GENRE_TABLE.genreID)
                self.customRatio[self.genreIndex[genreID]] += curRatio

        self.customRatio /= np.sum(self.customRatio)

    def makeRecommendation(self, count):
        selectRatio = self.genreRatio + self.customRatio
        selectRatio /= np.sum(selectRatio)
        selection = np.random.choice(range(len(self.genres)), count, p=selectRatio)

        return tuple(int(np.random.choice(self.candidateFilms[category], 1))
                     for category in selection)
