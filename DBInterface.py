from dotenv import load_dotenv as loadEnv
from os import getenv
from os.path import abspath, exists, split

from pyodbc import connect
from yaml import full_load as loadYAML

from DBProj.Password import Password


def getColumn(row, columnName):
    return row.__getattribute__(columnName)


class DBStructure:
    def __init__(self, table, columns):
        self.table = table
        self.columns = columns

    def __getattr__(self, name):
        if name in self.columns:
            return self.columns[name]
        else:
            raise AttributeError(name)


GENRE_TABLE = DBStructure('Genre', {'id': 'Genre_ID', 'name': 'Genre_Name'})

DIRECTOR_TABLE = DBStructure('Director', {'id': 'Director_ID',
                                          'name': 'Director_Name',
                                          'avatar': 'Director_Avatars',
                                          'alt': 'Director_Alt'})

CAST_TABLE = DBStructure('Film_Cast', {'id': 'Cast_ID',
                                       'name': 'Cast_Name',
                                       'avatar': 'Cast_Avatar',
                                       'alt': 'Cast_Alt'})

COMPANY_TABLE = DBStructure('Company', {'id': 'Company_ID',
                                        'name': 'Company_Name',
                                        'nationality': 'Company_City'})

FILM_TABLE = DBStructure('Film', {'id': 'Film_ID',
                                  'chineseName': 'Film_Chinese_Name',
                                  'originalName': 'Film_Original_Name',
                                  'releaseDate': 'Release_Date',
                                  'length': 'Length',
                                  'companyID': 'Company_ID',
                                  'picture': 'Picture',
                                  'storyline': 'Storyline',
                                  'prizeHistory': 'Prize_History',
                                  'remark': 'Remark'})

FILM_GENRE_TABLE = DBStructure('Film_Genre', {'filmID': 'Film_ID',
                                              'genreID': 'Genre_ID'})

DIRECTING_TABLE = DBStructure('Directing', {'filmID': 'Film_ID',
                                            'directorID': 'Director_ID',
                                            'role': 'Director_Role'})

PLAY_TABLE = DBStructure('Play', {'filmID': 'Film_ID',
                                  'castID': 'Cast_ID',
                                  'role': 'Cast_Role'})

USER_TABLE = DBStructure('Users', {'id': 'Users_ID',
                                   'name': 'Users_Name',
                                   'age': 'Users_Age',
                                   'sex': 'Users_Sex',
                                   'password': 'Users_Password',
                                   'isAdmin': 'Users_Is_Admin'})

COMMENT_TABLE = DBStructure('Comment', {'filmID': 'Film_ID',
                                        'userID': 'Users_ID',
                                        'rating': 'Rating',
                                        'comment': 'Users_Comment'})

FILM_VIEW = DBStructure('Film_View',
                        {'id': 'Film_ID',
                         'chineseName': 'Film_Chinese_Name',
                         'originalName': 'Film_Original_Name',
                         'genres': 'Film_Genres',
                         'releaseDate': 'Release_Date',
                         'picture': 'Picture',
                         'length': 'Length',
                         'companyName': 'Company_Name',
                         'companyNationality': 'Company_City',
                         'directors': 'Film_Directors',
                         'casts': 'Film_Casts',
                         'rating': 'Rating',
                         'ratingCount': 'Rating_Count',
                         'storyline': 'Storyline',
                         'prizeHistory': 'Prize_History',
                         'remark': 'Remark'})

COMMENT_VIEW = DBStructure('Comment_View', {'filmID': 'Film_ID',
                                            'filmName': 'Film_Chinese_Name',
                                            'userID': 'Users_ID',
                                            'userName': 'Users_Name',
                                            'userIsAdmin': 'Users_Is_Admin',
                                            'rating': 'Rating',
                                            'comment': 'Users_Comment'})


class DBInterface:
    """Database manipulation base class"""

    def __init__(self, role):
        """Create connection and cursor with given role"""
        try:
            loadEnv()
        except Exception:
            raise RuntimeError('.env not found')

        password = getenv(role)
        if password is None:
            raise ValueError(f'"{role}" is not an available role')

        configPath = split(abspath(__file__))[0] + '/config.yaml'
        if not exists(configPath):
            raise RuntimeError(f'config file not found at {configPath}')

        with open(configPath, 'r', encoding='utf8') as f:
            config = loadYAML(f)

        try:
            connStr = 'Driver={ODBC Driver 17 for SQL Server};' + \
                f'Database={config["database"]["database"]};' + \
                f'Server={config["database"]["server"]};' + \
                f'UID={role};PWD={password}'

            self._conn = connect(connStr, autocommit=True)
            self._cursor = self._conn.cursor()
        except Exception:
            print('cannot connect to database')
            raise

    def __del__(self):
        """Close cursor and connection before GC"""
        self._cursor.close()
        self._conn.close()

    def fetchResult(self, count=None):
        """Fetch given count of results from cursor"""
        try:
            return self._cursor.fetchmany(count) if count is not None\
                else self._cursor.fetchall()
        except Exception:
            print('failed to fetch result from cursor')
            raise

    def _insert(self, table, columns, value):
        """Insert single record to table"""
        if len(columns) != len(value):
            raise ValueError('columns and value do not match')

        columnStr = ', '.join(columns)
        placeholder = ', '.join(['?'] * len(value))
        sql = f'INSERT INTO {table} ({columnStr}) VALUES ({placeholder})'
        self._cursor.execute(sql, value)

    def _insertMany(self, table, columns, values):
        """Insert multiple records to table"""
        columnLen = len(columns)
        if any(columnLen != len(valueSet) for valueSet in values):
            raise ValueError('columns and (some) values do not match')

        columnStr = ', '.join(columns)
        placeholder = ', '.join(['?'] * len(values))
        sql = f'INSERT INTO {table} ({columnStr}) VALUES ({placeholder})'
        self._cursor.executemany(sql, values)

    def _select(self, table, columns, conditionExpression=None,
                conditionArgument=None, orderCondition=None):
        """Select records from table"""
        columnStr = ', '.join(columns)
        sql = f'SELECT {columnStr} FROM {table}'
        params = ()

        if conditionExpression is not None and conditionArgument is not None:
            sql = sql + ' WHERE ' + conditionExpression
            params = conditionArgument

        if orderCondition is not None:
            orderDirections = [f'{column} {"DESC" if reverse else "ASC"}'
                               for column, reverse in orderCondition]
            sql = sql + ' ORDER BY ' + ', '.join(orderDirections)

        self._cursor.execute(sql, params)

    def _update(self, table, columns, values, conditionExpression=None,
                conditionArgument=None):
        """Update record from table"""
        if len(columns) != len(values):
            raise ValueError('columns and values do not match')

        columnStr = ', '.join(f'{column} = ?' for column in columns)
        sql = f'UPDATE {table} SET {columnStr}'
        params = values

        if conditionExpression is not None and conditionArgument:
            sql = sql + ' WHERE ' + conditionExpression
            params = params + conditionArgument

        self._cursor.execute(sql, params)

    def _delete(self, table, conditionExpression=None, conditionArgument=None):
        """Delete record from table"""
        sql = f'DELETE FROM {table}'
        params = ()

        if conditionExpression is not None and conditionArgument:
            sql = sql + ' WHERE ' + conditionExpression
            params = conditionArgument

        self._cursor.execute(sql, params)

    def _custom(self, sql, args):
        """Execute custom SQL statement with given arguments"""
        self._cursor.execute(sql, args)


class FilmInterface(DBInterface):
    """Film info management interface"""

    __idCondition = f'{FILM_TABLE.id} = ?'

    __columns = (FILM_TABLE.chineseName,
                 FILM_TABLE.originalName,
                 FILM_TABLE.releaseDate,
                 FILM_TABLE.length,
                 FILM_TABLE.companyID,
                 FILM_TABLE.picture,
                 FILM_TABLE.storyline,
                 FILM_TABLE.prizeHistory,
                 FILM_TABLE.remark)

    __viewColumns = (FILM_VIEW.chineseName,
                     FILM_VIEW.originalName,
                     FILM_VIEW.genres,
                     FILM_VIEW.releaseDate,
                     FILM_VIEW.picture,
                     FILM_VIEW.length,
                     FILM_VIEW.companyName,
                     FILM_VIEW.companyNationality,
                     FILM_VIEW.directors,
                     FILM_VIEW.casts,
                     FILM_VIEW.rating,
                     FILM_VIEW.ratingCount,
                     FILM_VIEW.storyline,
                     FILM_VIEW.prizeHistory,
                     FILM_VIEW.remark)

    __listColumns = (FILM_VIEW.id,
                     FILM_VIEW.chineseName,
                     FILM_VIEW.originalName,
                     FILM_VIEW.picture,
                     FILM_VIEW.companyNationality,
                     FILM_VIEW.releaseDate,
                     FILM_VIEW.genres,
                     FILM_VIEW.rating)

    def __init__(self, isAdmin):
        """Initialize as guest or administrator"""
        self.role = 'admin' if isAdmin else 'guest_usr'
        super().__init__(self.role)

    def insertFilm(self,
                   filmChineseName=None,
                   filmOriginalName=None,
                   releaseDate=None,
                   length=None,
                   companyID=None,
                   picture=None,
                   storyline=None,
                   prizeHistory=None,
                   remark=None):
        """Insert new film"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._insert(FILM_TABLE.table, self.__columns,
                         (filmChineseName,
                          filmOriginalName,
                          releaseDate,
                          length,
                          companyID,
                          picture,
                          storyline,
                          prizeHistory,
                          remark))
        except Exception:
            print('failed to insert new film data')
            raise

    def insertManyFilms(self,
                        filmChineseNames=None,
                        filmOriginalNames=None,
                        releaseDates=None,
                        lengths=None,
                        companyIDs=None,
                        pictures=None,
                        storylines=None,
                        prizeHistories=None,
                        remarks=None):
        """Insert multiple new films"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._insertMany(FILM_TABLE.table, self.__columns,
                             zip(filmChineseNames,
                                 filmOriginalNames,
                                 releaseDates,
                                 lengths,
                                 companyIDs,
                                 pictures,
                                 storylines,
                                 prizeHistories,
                                 remarks))
        except Exception:
            print('failed to insert new film data')
            raise

    def selectFilm(self, filmID):
        """Select film with film ID"""
        try:
            self._select(FILM_VIEW.table, self.__viewColumns,
                         f'{FILM_VIEW.id} = ?', (filmID, ))
        except Exception:
            print('failed to select film with film ID')
            raise

    def searchFilm(self, name, genreID=None, releaseDate=None, rating=None,
                   releaseDateOrder=None, ratingOrder=None):
        """Search film with name, genre, release date and rating"""
        conditionExpression = f'({FILM_VIEW.chineseName} LIKE ? OR ' + \
            f'{FILM_VIEW.originalName} LIKE ?)'
        conditionArgument = (f'%{name}%', f'%{name}%')

        if genreID is not None:
            filmList = f'SELECT {FILM_GENRE_TABLE.filmID} ' + \
                f'FROM {FILM_GENRE_TABLE.table} ' + \
                f'WHERE ({FILM_GENRE_TABLE.genreID} = ?)'

            conditionExpression = conditionExpression + \
                f' AND ({FILM_VIEW.id} IN ({filmList}))'
            conditionArgument = conditionArgument + (genreID, )

        if releaseDate is not None:
            conditionExpression = conditionExpression + \
                f' AND ({FILM_VIEW.releaseDate} BETWEEN ? AND ?)'
            conditionArgument = conditionArgument + releaseDate

        if rating is not None:
            conditionExpression = conditionExpression + \
                f' AND {FILM_VIEW.rating} BETWEEN ? AND ?'
            conditionArgument = conditionArgument + rating

        orderCondition = []

        if releaseDateOrder is not None:
            orderCondition.append((FILM_VIEW.releaseDate, releaseDateOrder))

        if ratingOrder is not None:
            orderCondition.append((FILM_VIEW.rating, ratingOrder))

        if len(orderCondition) == 0:
            orderCondition = None

        try:
            self._select(FILM_VIEW.table, self.__listColumns,
                         conditionExpression, conditionArgument, orderCondition)
        except Exception:
            print('failed to search film')
            raise

    def updateFilmBasic(self, filmID,
                        filmChineseName=None,
                        filmOriginalName=None,
                        releaseDate=None,
                        length=None,
                        companyID=None,
                        picture=None):
        """Update basic film data (without text data) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(FILM_TABLE.table, self.__columns[:-3],
                         (filmChineseName,
                          filmOriginalName,
                          releaseDate,
                          length,
                          companyID,
                          picture),
                         self.__idCondition, (filmID, ))
        except Exception:
            print('failed to update film basic data')
            raise

    def updateFilmStoryline(self, filmID, storyline=None):
        """Update film storyline with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(FILM_TABLE.table, (self.__columns[-3], ),
                         (storyline, ), self.__idCondition, (filmID, ))
        except Exception:
            print('failed to update film storyline')
            raise

    def updateFilmPrizeHistory(self, filmID, prizeHistory=None):
        """Update film prize history with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(FILM_TABLE.table, (self.__columns[-2], ),
                         (prizeHistory, ), self.__idCondition, (filmID, ))
        except Exception:
            print('failed to update film prize history')
            raise

    def updateFilmRemark(self, filmID, remark=None):
        """Update film remark with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(FILM_TABLE.table, (self.__columns[-1], ),
                         (remark, ), self.__idCondition, (filmID, ))
        except Exception:
            print('failed to update film remark')
            raise

    def deleteFilm(self, filmID):
        """Delete film with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(FILM_TABLE.table, self.__idCondition, (filmID, ))
        except Exception:
            print('failed to delete film data')
            raise

    def selectFilmGenre(self, filmID):
        """Select film genre (ID and name) with film ID"""
        try:
            self._select(f'{FILM_GENRE_TABLE.table} AS a INNER JOIN '
                         f'{GENRE_TABLE.table} AS b ON '
                         f'a.{FILM_GENRE_TABLE.genreID} = b.{GENRE_TABLE.id}',
                         (f'b.{GENRE_TABLE.id}', GENRE_TABLE.name),
                         self.__idCondition, (filmID, ))

        except Exception:
            print('failed to select film genre')
            raise

    def updateFilmGenre(self, filmID, genreIDs):
        """Update film genre (all pairs) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(FILM_GENRE_TABLE.table, self.__idCondition, (filmID, ))
            values = [(filmID, genreID) for genreID in genreIDs]

            self._insertMany(FILM_GENRE_TABLE.table,
                             (FILM_GENRE_TABLE.filmID,
                              FILM_GENRE_TABLE.genreID),
                             values)
        except Exception:
            print('failed to update film genre')
            raise

    def selectFilmDirectingInfo(self, filmID):
        """Select film directing info (ID, name and role) with film ID"""
        try:
            self._select(f'{DIRECTING_TABLE.table} AS a INNER JOIN '
                         f'{DIRECTOR_TABLE.table} AS b ON '
                         f'a.{DIRECTING_TABLE.directorID} = '
                         f'b.{DIRECTOR_TABLE.id}',
                         (f'b.{DIRECTOR_TABLE.id}',
                          DIRECTOR_TABLE.name,
                          DIRECTOR_TABLE.avatar,
                          DIRECTING_TABLE.role,
                          DIRECTOR_TABLE.alt),
                         self.__idCondition, (filmID, ))

        except Exception:
            print('failed to select film directing info')
            raise

    def updateFilmDirectingInfo(self, filmID, directorIDs, directorRoles):
        """Update film directing info (all pairs) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(DIRECTING_TABLE.table, self.__idCondition, (filmID, ))

            values = [(filmID, directorID, directorRole)
                      for directorID, directorRole
                      in zip(directorIDs, directorRoles)]

            self._insertMany(DIRECTING_TABLE.table,
                             (DIRECTING_TABLE.filmID,
                              DIRECTING_TABLE.directorID,
                              DIRECTING_TABLE.role),
                             values)
        except Exception:
            print('failed to update film directing info')
            raise

    def selectFilmPlayInfo(self, filmID):
        """Select film play info (ID, name, role) with film ID"""
        try:
            self._select(f'{PLAY_TABLE.table} AS a INNER JOIN '
                         f'{CAST_TABLE.table} AS b ON '
                         f'a.{PLAY_TABLE.castID} = b.{CAST_TABLE.id}',
                         (f'b.{CAST_TABLE.id}',
                          CAST_TABLE.name,
                          CAST_TABLE.avatar,
                          PLAY_TABLE.role,
                          CAST_TABLE.alt),
                         self.__idCondition, (filmID, ))

        except Exception:
            print('failed to select film play info')
            raise

    def updateFilmPlayInfo(self, filmID, castIDs, castRoles):
        """Update film play info (all pairs) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(PLAY_TABLE.table, self.__idCondition, (filmID, ))

            values = [(filmID, castID, castRole)
                      for castID, castRole in zip(castIDs, castRoles)]

            self._insertMany(PLAY_TABLE.table,
                             (PLAY_TABLE.filmID,
                              PLAY_TABLE.castID,
                              PLAY_TABLE.role),
                             values)
        except Exception:
            print('failed to update film play info')
            raise


class SubInfoInterface(DBInterface):
    """Sub info management base interface"""

    def __init__(self, table, columns, isAdmin):
        """Initialize as guest or administrator"""
        self.__table = table
        self.__idCondition = f'{table.id} = ?'
        self.__columns = columns
        self.role = 'admin' if isAdmin else 'guest_usr'
        super().__init__(self.role)

    def _insertSubInfo(self, value):
        """Insert new sub info"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify sub info')

        try:
            self._insert(self.__table.table, self.__columns, value)
        except Exception:
            print('failed to insert new sub info')
            raise

    def _insertManySubInfo(self, values):
        """Insert new sub info"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify sub info')

        try:
            self._insertMany(self.__table.table, self.__columns, values)
        except Exception:
            print('failed to insert new sub info')
            raise

    def _selectSubInfo(self, infoID):
        """Select sub info with info ID"""
        try:
            self._select(self.__table.table, self.__columns, self.__idCondition,
                         (infoID, ))
        except Exception:
            print('failed to select sub info')
            raise

    def _searchSubInfoIDByName(self, name):
        """Search info ID by name"""
        try:
            self._select(self.__table.table, (self.__table.id, ),
                         f'{self.__table.name} LIKE ?', (f'%{name}%', ))
        except Exception:
            print('failed to search info ID')
            raise

    def _updateSubInfo(self, infoID, value):
        """Update sub info with info ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify sub info')

        try:
            self._update(self.__table.table, self.__columns, value,
                         self.__idCondition, (infoID, ))
        except Exception:
            print('failed to update sub info')
            raise

    def _deleteSubInfo(self, infoID):
        """Delete sub info with info ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify sub info')

        try:
            self._delete(self.__table.table, self.__idCondition, (infoID, ))
        except Exception:
            print('failed to delete sub info')
            raise


class GenreInterface(SubInfoInterface):
    """Genre info management interface"""

    def __init__(self, isAdmin):
        """Initialize as guest or administrator"""
        super().__init__(GENRE_TABLE, (GENRE_TABLE.name, ), isAdmin)

    def insertGenre(self, genreName=None):
        """Insert new genre"""
        self._insertSubInfo((genreName, ))

    def insertManyGenres(self, genreNames=None):
        """Insert multiple new genres"""
        self._insertManySubInfo(zip(genreNames))

    def selectAllGenre(self):
        """Select all genre"""
        try:
            self._select(GENRE_TABLE.table, self.__columns)
        except Exception:
            print('failed to select genre info')
            raise

    def selectGenre(self, genreID):
        """Select genre with genre ID"""
        return self._selectSubInfo(genreID)

    def searchGenreIDByName(self, genreName):
        """Search genre ID by genre name"""
        return self._searchSubInfoIDByName(genreName)

    def updateGenre(self, genreID, genreName=None):
        """Update genre with genre ID"""
        self._updateSubInfo(genreID, (genreName, ))

    def deleteGenre(self, genreID):
        """Delete genre with genre ID"""
        self._deleteSubInfo(genreID)


class DirectorInterface(SubInfoInterface):
    """Director info management interface"""

    def __init__(self, isAdmin):
        """Initialize as guest or administrator"""
        super().__init__(DIRECTOR_TABLE, (DIRECTOR_TABLE.name,
                                          DIRECTOR_TABLE.avatar,
                                          DIRECTOR_TABLE.alt), isAdmin)

    def insertDirector(self,
                       directorName=None,
                       directorAvatar=None,
                       directorAlt=None):
        """Insert new director"""
        self._insertSubInfo((directorName, directorAvatar, directorAlt))

    def insertManyDirectors(self,
                            directorNames=None,
                            directorAvatars=None,
                            directorAlts=None):
        """Insert multiple new directors"""
        self._insertManySubInfo(zip(directorNames, directorAvatars, directorAlts))

    def selectDirector(self, directorID):
        """Select director with director ID"""
        return self._selectSubInfo(directorID)

    def searchDirectorIDByName(self, directorName):
        """Search director ID by director name"""
        return self._searchSubInfoIDByName(directorName)

    def updateDirector(self, directorID,
                       directorName=None,
                       directorAvatar=None,
                       directorAlt=None):
        """Update genre with genre ID"""
        self._updateSubInfo(directorID, (directorName,
                                         directorAvatar,
                                         directorAlt))

    def deleteDirector(self, directorID):
        """Delete genre with genre ID"""
        self._deleteSubInfo(directorID)


class CastInterface(SubInfoInterface):
    """Cast info management interface"""

    def __init__(self, isAdmin):
        """Initialize as guest or administrator"""
        super().__init__(CAST_TABLE, (CAST_TABLE.name,
                                      CAST_TABLE.avatar,
                                      CAST_TABLE.alt), isAdmin)

    def insertCast(self, castName=None, castAvatar=None, castAlt=None):
        """Insert new cast"""
        self._insertSubInfo((castName, castAvatar, castAlt))

    def insertManyCasts(self, castNames=None, castAvatars=None, castAlts=None):
        """Insert multiple new casts"""
        self._insertManySubInfo(zip(castNames, castAvatars, castAlts))

    def selectCast(self, castID):
        """Select cast with cast ID"""
        return self._selectSubInfo(castID)

    def searchCastIDByName(self, castName):
        """Search cast ID by cast name"""
        return self._searchSubInfoIDByName(castName)

    def updateCast(self, castID, castName=None, castAvatar=None, castAlt=None):
        """Update cast with cast ID"""
        self._updateSubInfo(castID, (castName, castAvatar, castAlt))

    def deleteCast(self, castID):
        """Delete cast with cast ID"""
        self._deleteSubInfo(castID)


class CompanyInterface(SubInfoInterface):
    """Company info management interface"""

    def __init__(self, isAdmin):
        """Initialize as guest or administrator"""
        super().__init__(COMPANY_TABLE, (COMPANY_TABLE.name,
                                         COMPANY_TABLE.nationality), isAdmin)

    def insertCompany(self, companyName=None, companyNationality=None):
        """Insert new company"""
        self._insertSubInfo((companyName, companyNationality))

    def insertManyCompanies(self, companyNames=None, companyNationalities=None):
        """Insert multiple new companies"""
        self._insertManySubInfo(zip(companyNames, companyNationalities))

    def selectCompany(self, companyID):
        """Select company with company ID"""
        return self._selectSubInfo(companyID)

    def searchCompanyIDByName(self, companyName):
        """Search company ID by company name"""
        return self._searchSubInfoIDByName(companyName)

    def updateCompany(self, companyID,
                      companyName=None, companyNationality=None):
        """Update company with company ID"""
        self._updateSubInfo(companyID, (companyName, companyNationality))

    def deleteCompany(self, companyID):
        """Delete company with company ID"""
        self._deleteSubInfo(companyID)


class CommentInterface(DBInterface):
    """Comment management interface"""
    __idCondition = f'{COMMENT_TABLE.filmID} = ? AND {COMMENT_TABLE.userID} = ?'

    __idColumns = (COMMENT_TABLE.filmID, COMMENT_TABLE.userID)
    __columns = (COMMENT_TABLE.rating, COMMENT_TABLE.comment)

    __filmColumns = (COMMENT_VIEW.filmID, COMMENT_VIEW.filmName)
    __userColumns = (COMMENT_VIEW.userID, COMMENT_VIEW.userName,
                     COMMENT_VIEW.userIsAdmin)
    __infoColumns = (COMMENT_VIEW.rating, COMMENT_VIEW.comment)

    def __init__(self, isUser):
        """Initialize as guest or member"""
        self.role = 'member' if isUser else 'guest_usr'
        super().__init__(self.role)

    def selectCommentByFilmID(self, filmID):
        """Select comment by film ID"""
        try:
            self._select(COMMENT_VIEW.table,
                         self.__userColumns + self.__infoColumns,
                         f'{COMMENT_VIEW.filmID} = ?', (filmID, ))
        except Exception:
            print('failed to select comment by film ID')
            raise

    def selectCommentByUserID(self, userID):
        """Select comment by user ID"""
        try:
            self._select(COMMENT_VIEW.table,
                         self.__filmColumns + self.__infoColumns,
                         f'{COMMENT_VIEW.userID} = ?', (userID, ))
        except Exception:
            print('failed to select comment by user ID')
            raise

    def upsertComment(self, filmID, userID, rating=None, userComment=None):
        """Insert new or update existed comment with film ID and user ID"""
        if self.role != 'member':
            raise RuntimeError('only members can modify comments')

        try:
            self._select(COMMENT_TABLE.table, self.__idColumns,
                         self.__idCondition, (filmID, userID))

            if self._cursor.rowcount == 0:
                self._insert(COMMENT_TABLE.table,
                             self.__idColumns + self.__columns,
                             (filmID, userID, rating, userComment))
            else:
                self._update(COMMENT_TABLE.table, self.__columns,
                             (rating, userComment), self.__idCondition,
                             (filmID, userID))
        except Exception:
            print('failed to insert or update comment')
            raise

    def deleteComment(self, filmID, userID):
        """Delete comment with film ID and user ID"""
        if self.role != 'member':
            raise RuntimeError('only members can modify comments')

        try:
            self._delete(COMMENT_TABLE.table, self.__idCondition,
                         (filmID, userID))
        except Exception:
            print('failed to delete comment')
            raise


class UserInterface(DBInterface):
    """User info management interface"""
    ROLE_LOGIN = 'login'
    ROLE_GUEST = 'guest_usr'
    ROLE_MEMBER = 'member'
    ROLE_USR_ADMIN = 'usr_admin'

    __available_roles = (ROLE_LOGIN, ROLE_GUEST, ROLE_MEMBER, ROLE_USR_ADMIN)
    __idCondition = f'{USER_TABLE.id} = ?'

    __columns = (USER_TABLE.name,
                 USER_TABLE.age,
                 USER_TABLE.sex)

    def __init__(self, role):
        """Initialize as login verifier, guest, member or user administrator"""
        if role not in self.__available_roles:
            raise ValueError(role)

        self.role = role
        super().__init__(self.role)

    def verifyLogin(self, userID, password):
        """Verify login """
        if self.role != self.ROLE_LOGIN:
            raise RuntimeError('only login interface can verify login')

        self._select(USER_TABLE.table, (USER_TABLE.password, ),
                     self.__idCondition, (userID, ))
        result = self.fetchResult(1)

        if len(result) == 0:
            return False
        return Password.verify(password,
                               getColumn(result[0], USER_TABLE.password))

    def createUser(self, userID, password, userName,
                   userIsAdmin=False,
                   userAge=None,
                   userSex=None):
        """Create new user"""
        if self.role != self.ROLE_USR_ADMIN:
            raise RuntimeError('only user administrators can create new user')

        hashed = Password.encrypt(password)
        columns = (USER_TABLE.id, USER_TABLE.password, USER_TABLE.isAdmin)\
            + self.__columns

        try:
            self._insert(USER_TABLE.table, columns,
                         (userID,
                          hashed,
                          userIsAdmin,
                          userName,
                          userAge,
                          userSex))
        except Exception:
            print('failed to insert new user')
            raise

    def selectUserInfo(self, userID):
        """Select user info with user ID"""
        try:
            self._select(USER_TABLE.table,
                         self.__columns + (USER_TABLE.isAdmin, ),
                         self.__idCondition, (userID, ))
        except Exception:
            print('failed to select user info')
            raise

    def updateUserInfo(self, userID, userName,
                       userAge=None,
                       userSex=None):
        """Update user info with user ID"""
        if self.role != self.ROLE_MEMBER:
            raise RuntimeError('only users can modify user info')

        try:
            self._update(USER_TABLE.table, self.__columns,
                         (userName, userAge, userSex), self.__idCondition,
                         (userID, ))
        except Exception:
            print('failed to update user info')
            raise

    def updateUserPassword(self, userID, password):
        """Update user password with user ID"""
        if self.role != self.ROLE_MEMBER:
            raise RuntimeError('only users can modify user password')

        try:
            self._update(USER_TABLE.table, (USER_TABLE.password, ),
                         (Password.encrypt(password), ), self.__idCondition,
                         (userID, ))
        except Exception:
            print('failed to update user password')
            raise

    def updateUserAdmin(self, userID, userIsAdmin):
        """Update user administration status with user ID"""
        if self.role != self.ROLE_USR_ADMIN:
            raise RuntimeError('only user administrators can modify '
                               'user administration status')

        try:
            self._update(USER_TABLE.table, (USER_TABLE.isAdmin, ),
                         (userIsAdmin, ), self.__idCondition, userID)
        except Exception:
            print('failed to update user administration status')
            raise

    def deleteUser(self, userID):
        """Delete user with user ID"""
        if self.role != self.ROLE_USR_ADMIN:
            raise RuntimeError('only user administrators can create new user')

        try:
            self._delete(USER_TABLE.table, self.__idCondition, (userID, ))
        except Exception:
            print('failed to delete user info')
            raise
