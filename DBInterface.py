from dotenv import load_dotenv as loadEnv
from os import getenv
from os.path import abspath, exists, split

from pyodbc import connect
from yaml import full_load as loadYAML

from Password import Password


class TableDef:
    def __init__(self, table, columns):
        self.table = table
        self.columns = columns

    def __getattr__(self, name):
        if name in self.columns:
            return self.columns[name]
        else:
            raise AttributeError(name)


GENRE_TABLE = TableDef('Genre', {'id': 'Genre_ID', 'name': 'Genre_Name'})

DIRECTOR_TABLE = TableDef('Director', {'id': 'Director_ID',
                                       'name': 'Director_Name',
                                       'sex': 'Director_Sex',
                                       'birth': 'Director_Birth',
                                       'nationality': 'Director_Nationality',
                                       'picture': 'Director_Picture'})

CAST_TABLE = TableDef('Film_Cast', {'id': 'Cast_ID',
                                    'name': 'Cast_Name',
                                    'sex': 'Cast_Sex',
                                    'birth': 'Cast_Birth',
                                    'nationality': 'Cast_Nationality',
                                    'picture': 'Cast_Picture'})

COMPANY_TABLE = TableDef('Company', {'id': 'Company_ID',
                                     'name': 'Company_Name',
                                     'nationality': 'Company_City'})

FILM_TABLE = TableDef('Film', {'id': 'Film_ID',
                               'chineseName': 'Film_Chinese_Name',
                               'originalName': 'Film_Original_Name',
                               'releaseDate': 'Release_Date',
                               'length': 'Length',
                               'companyID': 'Company_ID',
                               'picture': 'Picture',
                               'storyline': 'Storyline',
                               'prizeHistory': 'Prize_History',
                               'remark': 'Remark'})

FILM_GENRE_TABLE = TableDef('Film_Genre', {'filmID': 'Film_ID',
                                           'genreID': 'Genre_ID'})

DIRECTING_TABLE = TableDef('Directing', {'filmID': 'Film_ID',
                                         'directorID': 'Director_ID',
                                         'role': 'Director_Role'})

PLAY_TABLE = TableDef('Play', {'filmID': 'Film_ID',
                               'castID': 'Cast_ID',
                               'role': 'Cast_Role'})

USER_TABLE = TableDef('User', {'id': 'User_ID',
                               'name': 'User_Name',
                               'age': 'User_Age',
                               'sex': 'User_Sex',
                               'password': 'User_Password',
                               'isAdmin': 'User_Is_Admin'})

COMMENT_TABLE = TableDef('Comment', {'filmID': 'Film_ID',
                                     'userID': 'User_ID',
                                     'rating': 'Rating',
                                     'comment': 'User_Comment'})


class DB:
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
            driver = 'DRIVER={ODBC Driver 17 for SQL Server}'

            self._conn = connect(autocommit=True,
                                 driver=driver,
                                 host=config['server'],
                                 database=config['database'],
                                 user=role,
                                 password=password,
                                 encoding='utf8')

            self._cursor = self._conn.cursor
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

    def _insert(self, table, columns, values):
        """Insert single record to table"""
        if len(columns) != len(values):
            raise ValueError('columns and values do not match')

        placeholder = ', '.join(['%s'] * len(values))
        sql = f'INSERT %s ({placeholder}) VALUES ({placeholder})'
        self._cursor.execute(sql, (table, ) + columns + values)

    def _insertMany(self, table, columns, values):
        """Insert multiple records to table"""
        columnLen = len(columns)
        if any(columnLen == len(valueSet) for valueSet in values):
            raise ValueError('columns and (some) values do not match')

        placeholder = ', '.join(['%s'] * len(values))
        sql = f'INSERT {table} ({", ".join(columns)}) VALUES ({placeholder})'
        self._cursor.executemany(sql, values)

    def _select(self, table, columns, condition=None, orderCondition=None):
        """Select records from table"""
        placeholder = ', '.join(['%s'] * len(columns))
        sql = f'SELECT {placeholder} FROM %s'
        params = (table, ) + columns

        if condition is not None:
            sql = sql + ' WHERE %s'
            params = params + (condition, )

        if orderCondition is not None:
            orderColumns = [column for column, _ in orderCondition]
            orderDirections = [f'%s {"DESC" if reverse else "ASC"}'
                               for _, reverse in orderCondition]

            sql = sql + ' ORDER BY ' + ', '.join(orderDirections)
            params = params + (orderColumns, )

        self._cursor.execute(sql, params)

    def _update(self, table, columns, values, condition=None):
        """Update record from table"""
        if len(columns) != len(values):
            raise ValueError('columns and values do not match')

        placeholder = ', '.join(["%s = %s"] * len(values))
        sql = f'UPDATE %s SET {placeholder}'

        params = (table, )
        for pair in zip(columns, values):
            params = params + pair

        if condition is not None:
            sql = sql + ' WHERE %s'
            params = params + (condition, )

        self._cursor.execute(sql, params)

    def _delete(self, table, condition=None):
        """Delete record from table"""
        sql = 'DELETE FROM %s'
        params = (table, )

        if condition is not None:
            sql = sql + ' WHERE %s'
            params = params + (condition, )

        self._cursor.execute(sql, params)

    def _custom(self, sql, params):
        """Execute custom SQL statement with given parameters"""
        self._cursor.execute(sql, params)


class FilmDB(DB):
    """Film info management interface"""

    __columns = (FILM_TABLE.chineseName,
                 FILM_TABLE.originalName,
                 FILM_TABLE.releaseDate,
                 FILM_TABLE.length,
                 FILM_TABLE.companyID,
                 FILM_TABLE.picture,
                 FILM_TABLE.storyline,
                 FILM_TABLE.prizeHistory,
                 FILM_TABLE.remark)

    def __init__(self, isAdmin):
        """Initialize as guest or administrator"""
        self.role = 'admin' if isAdmin else 'guest'
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
            self._insert(FILM_TABLE.table, self.__columns,
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
            self._select(FILM_TABLE.table, self.__columns,
                         self.__idAsCondition(filmID))
            return self._cursor.rowcount
        except Exception:
            print('failed to select film with film ID')
            raise

    def searchFilm(self, name, genre=None, releaseDate=None, rating=None,
                   releaseDateOrder=None, ratingOrder=None):
        """Search film with name, genre, release date and rating"""
        rating_table = f'SELECT {COMMENT_TABLE.filmID}, ' + \
            f'AVG({COMMENT_TABLE.rating}) AS {COMMENT_TABLE.rating} ' + \
            f'FROM {COMMENT_TABLE.table} GROUP BY {COMMENT_TABLE.filmID}'

        table = f'{FILM_TABLE.table} AS a ' + \
            f'INNER JOIN ({FILM_GENRE_TABLE.table}) AS b ' + \
            f'ON a.{FILM_TABLE.id} = b.{FILM_GENRE_TABLE.filmID} ' + \
            f'LEFT OUTER JOIN {rating_table} AS c ' + \
            f'ON a.{FILM_TABLE.id} = c.{COMMENT_TABLE.filmID}'

        columns = self.__columns[:-3] + (COMMENT_TABLE.rating, )

        condition = f'({FILM_TABLE.chineseName} LIKE %{name}% OR ' + \
            f'{FILM_TABLE.originalName} LIKE %{name}%)'

        if genre is not None:
            condition = condition + f' AND {FILM_GENRE_TABLE.genreID} = {genre}'

        if releaseDate is not None:
            condition = condition + f' AND {FILM_TABLE.releaseDate} ' + \
                f'BETWEEN {releaseDate[0]:%Y-%m-%d} ' + \
                f'AND {releaseDate[1]:%Y-%m-%d}'

        if rating is not None:
            condition = condition + f' AND {COMMENT_TABLE.rating} BETWEEN' + \
                f'{rating[0]:.1f} AND {rating[1]:.1f}'

        orderCondition = []

        if releaseDateOrder is not None:
            orderCondition.append(FILM_TABLE.releaseDate, releaseDateOrder)

        if ratingOrder is not None:
            orderCondition.append(COMMENT_TABLE.rating, ratingOrder)

        if len(orderCondition) == 0:
            orderCondition = None

        try:
            self._select(table, columns, condition, orderCondition)
            return self._cursor.rowcount
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
                         self.__idAsCondition(filmID))
        except Exception:
            print('failed to update film basic data')
            raise

    def updateFilmStoryline(self, filmID, storyline=None):
        """Update film storyline with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(FILM_TABLE.table, (self.__columns[-3], ),
                         (storyline, ), self.__idAsCondition(filmID))
        except Exception:
            print('failed to update film storyline')
            raise

    def updateFilmPrizeHistory(self, filmID, prizeHistory=None):
        """Update film prize history with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(FILM_TABLE.table, (self.__columns[-2], ),
                         (prizeHistory, ), self.__idAsCondition(filmID))
        except Exception:
            print('failed to update film prize history')
            raise

    def updateFilmRemark(self, filmID, remark=None):
        """Update film remark with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(FILM_TABLE.table, (self.__columns[-1], ),
                         (remark, ), self.__idAsCondition(filmID))
        except Exception:
            print('failed to update film remark')
            raise

    def deleteFilm(self, filmID):
        """Delete film with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(FILM_TABLE.table, self.__idAsCondition(filmID))
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
                         self.__idAsCondition(filmID))

            return self._cursor.rowcount
        except Exception:
            print('failed to select film genre')
            raise

    def updateFilmGenre(self, filmID, genreIDs):
        """Update film genre (all pairs) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(FILM_GENRE_TABLE.table, self.__idAsCondition(filmID))
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
                          DIRECTING_TABLE.role),
                         self.__idAsCondition(filmID))

            return self._cursor.rowcount
        except Exception:
            print('failed to select film directing info')
            raise

    def updateFilmDirectingInfo(self, filmID, directorIDs, directorRoles):
        """Update film directing info (all pairs) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(DIRECTING_TABLE.table, self.__idAsCondition(filmID))

            values = [(filmID, directorID, directorRole)
                      for directorID, directorRole
                      in zip(directorIDs, directorRoles)]

            self._insertMany(DIRECTING_TABLE.table,
                             (DIRECTING_TABLE.filmID,
                              DIRECTING_TABLE.castID,
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
                          PLAY_TABLE.role),
                         self.__idAsCondition(filmID))

            return self._cursor.rowcount
        except Exception:
            print('failed to select film play info')
            raise

    def updateFilmPlayInfo(self, filmID, castIDs, castRoles):
        """Update film play info (all pairs) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(PLAY_TABLE.table, self.__idAsCondition(filmID))

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

    def __idAsCondition(self, filmID):
        """Generate SQL condition with film ID"""
        return f'{FILM_TABLE.id} = {filmID}'


class GenreDB(DB):
    """Genre info management interface"""
    __columns = (GENRE_TABLE.name, )

    def __init__(self, isAdmin):
        """Initialize as guest or administrator"""
        self.role = 'admin' if isAdmin else 'guest'
        super().__init__(self.role)

    def insertGenre(self, genreName=None):
        """Insert new genre"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify genre info')

        try:
            self._insert(GENRE_TABLE.table, self.__columns, (genreName, ))
        except Exception:
            print('failed to insert new genre info')
            raise

    def insertManyGenres(self, genreNames=None):
        """Insert multiple new genres"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify genre info')

        try:
            self._insert(GENRE_TABLE.table, self.__columns, zip(genreNames))
        except Exception:
            print('failed to insert new genre info')
            raise

    def selectAllGenre(self):
        """Select all genre"""
        try:
            self._select(GENRE_TABLE.table, self.__columns)
            return self._cursor.rowcount
        except Exception:
            print('failed to select genre info')
            raise

    def selectGenre(self, genreID):
        """Select genre with genre ID"""
        try:
            self._select(GENRE_TABLE.table, self.__columns,
                         self.__idAsCondition(genreID))
            return self._cursor.rowcount
        except Exception:
            print('failed to select genre info')
            raise

    def searchGenreIDByName(self, genreName=None):
        """Search genre ID by genre name"""
        try:
            self._select(GENRE_TABLE.table, (GENRE_TABLE.id, ),
                         f'{GENRE_TABLE.name} = {genreName}'
                         if genreName is not None else None)
            return self._cursor.rowcount
        except Exception:
            print('failed to search genre ID')
            raise

    def updateGenre(self, genreID, genreName=None):
        """Update genre with genre ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify genre info')

        try:
            self._update(GENRE_TABLE.table, self.__columns, (genreName, ),
                         self.__idAsCondition(genreID))
        except Exception:
            print('failed to update genre info')
            raise

    def deleteGenre(self, genreID):
        """Delete genre with genre ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify genre info')

        try:
            self._delete(GENRE_TABLE.table, self.__idAsCondition(genreID))
        except Exception:
            print('failed to delete genre info')
            raise

    def __idAsCondition(self, genreID):
        """Generate SQL condition with genre ID"""
        return f'{GENRE_TABLE.id} = {genreID}'


class DirectorDB(DB):
    """Director info management interface"""

    __columns = (DIRECTOR_TABLE.name,
                 DIRECTOR_TABLE.sex,
                 DIRECTOR_TABLE.birth,
                 DIRECTOR_TABLE.nationality,
                 DIRECTOR_TABLE.picture)

    def __init__(self, isAdmin):
        """Initialize as guest or administrator"""
        self.role = 'admin' if isAdmin else 'guest'
        super().__init__(self.role)

    def insertDirector(self,
                       directorName=None,
                       directorSex=None,
                       directorBirth=None,
                       directorNationality=None,
                       directorPicture=None):
        """Insert new director"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify director info')

        try:
            self._insert(DIRECTOR_TABLE.table, self.__columns,
                         (directorName,
                          directorSex,
                          directorBirth,
                          directorNationality,
                          directorPicture))
        except Exception:
            print('failed to insert new director info')
            raise

    def insertManyDirectors(self,
                            directorNames=None,
                            directorSexes=None,
                            directorBirths=None,
                            directorNationalities=None,
                            directorPictures=None):
        """Insert multiple new directors"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify director info')

        try:
            self._insert(DIRECTOR_TABLE.table, self.__columns,
                         zip(directorNames,
                             directorSexes,
                             directorBirths,
                             directorNationalities,
                             directorPictures))
        except Exception:
            print('failed to insert new director info')
            raise

    def selectDirector(self, directorID):
        """Select director with director ID"""
        try:
            self._select(DIRECTOR_TABLE.table, self.__columns,
                         self.__idAsCondition(directorID))
            return self._cursor.rowcount
        except Exception:
            print('failed to select director info')
            raise

    def searchDirectorIDByName(self, directorName=None):
        """Search director ID by director name"""
        try:
            self._select(DIRECTOR_TABLE.table, (DIRECTOR_TABLE.id, ),
                         f'{DIRECTOR_TABLE.name} = {directorName}'
                         if directorName is not None else None)
            return self._cursor.rowcount
        except Exception:
            print('failed to search director ID')
            raise

    def updateDirector(self, directorID,
                       directorName=None,
                       directorSex=None,
                       directorBirth=None,
                       directorNationality=None,
                       directorPicture=None):
        """Update genre with genre ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify director info')

        try:
            self._update(DIRECTOR_TABLE.table, self.__columns,
                         (directorName,
                          directorSex,
                          directorBirth,
                          directorNationality,
                          directorPicture),
                         self.__idAsCondition(directorID))
        except Exception:
            print('failed to update director info')
            raise

    def deleteDirector(self, directorID):
        """Delete genre with genre ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify director info')

        try:
            self._delete(DIRECTOR_TABLE.table, self.__idAsCondition(directorID))
        except Exception:
            print('failed to delete director info')
            raise

    def __idAsCondition(self, directorID):
        """Generate SQL condition with director ID"""
        return f'{DIRECTOR_TABLE.id} = {directorID}'


class CastDB(DB):
    """Cast info management interface"""

    __columns = (CAST_TABLE.name,
                 CAST_TABLE.sex,
                 CAST_TABLE.birth,
                 CAST_TABLE.nationality,
                 CAST_TABLE.picture)

    def __init__(self, isAdmin):
        """Initialize as guest or administrator"""
        self.role = 'admin' if isAdmin else 'guest'
        super().__init__(self.role)

    def insertCast(self,
                   castName=None,
                   castSex=None,
                   castBirth=None,
                   castNationality=None,
                   castPicture=None):
        """Insert new cast"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify cast info')

        try:
            self._insert(CAST_TABLE.table, self.__columns,
                         (castName, castSex, castBirth, castNationality))
        except Exception:
            print('failed to insert new cast info')
            raise

    def insertManyCasts(self,
                        castNames=None,
                        castSexes=None,
                        castBirths=None,
                        castNationalities=None,
                        castPictures=None):
        """Insert multiple new casts"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify cast info')

        try:
            self._insert(CAST_TABLE.table, self.__columns,
                         zip(castNames,
                             castSexes,
                             castBirths,
                             castNationalities,
                             castPictures))
        except Exception:
            print('failed to insert new cast info')
            raise

    def selectCast(self, castID):
        """Select cast with cast ID"""
        try:
            self._select(CAST_TABLE.table, self.__columns,
                         self.__idAsCondition(castID))
            return self._cursor.rowcount
        except Exception:
            print('failed to select cast info')
            raise

    def searchCastIDByName(self, castName=None):
        """Search cast ID by cast name"""
        try:
            self._select(CAST_TABLE.table, (CAST_TABLE.id, ),
                         f'{CAST_TABLE.name} = {castName}'
                         if castName is not None else None)
            return self._cursor.rowcount
        except Exception:
            print('failed to search cast ID')
            raise

    def updateCast(self, castID,
                   castName=None,
                   castSex=None,
                   castBirth=None,
                   castNationality=None,
                   castPicture=None):
        """Update cast with cast ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify cast info')

        try:
            self._update(CAST_TABLE.table, self.__columns,
                         (castName,
                          castSex,
                          castBirth,
                          castNationality,
                          castPicture),
                         self.__idAsCondition(castID))
        except Exception:
            print('failed to update cast info')
            raise

    def deleteCast(self, castID):
        """Delete cast with cast ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify cast info')

        try:
            self._delete(CAST_TABLE.table, self.__idAsCondition(castID))
        except Exception:
            print('failed to delete cast info')
            raise

    def __idAsCondition(self, castID):
        """Generate SQL condition with cast ID"""
        return f'{CAST_TABLE.id} = {castID}'


class CompanyDB(DB):
    """Company info management interface"""
    __columns = (COMPANY_TABLE.name, COMPANY_TABLE.nationality)

    def __init__(self, isAdmin):
        """Initialize as guest or administrator"""
        self.role = 'admin' if isAdmin else 'guest'
        super().__init__(self.role)

    def insertCompany(self, companyName=None, companyNationality=None):
        """Insert new company"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify company info')

        try:
            self._insert(COMPANY_TABLE.table, self.__columns,
                         (companyName, companyNationality))
        except Exception:
            print('failed to insert new company info')
            raise

    def insertManyCompanies(self, companyNames=None, companyNationalities=None):
        """Insert multiple new companies"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify company info')

        try:
            self._insert(COMPANY_TABLE.table, self.__columns,
                         zip(companyNames, companyNationalities))
        except Exception:
            print('failed to insert new company info')
            raise

    def selectCompany(self, companyID):
        """Select company with company ID"""
        try:
            self._select(COMPANY_TABLE.table, self.__columns,
                         self.__idAsCondition(companyID))
            return self._cursor.rowcount
        except Exception:
            print('failed to select company info')
            raise

    def searchCompanyIDByName(self, companyName=None):
        """Search company ID by company name"""
        try:
            self._select(COMPANY_TABLE.table, (COMPANY_TABLE.id, ),
                         f'{COMPANY_TABLE.name} = {companyName}'
                         if companyName is not None else None)
            return self._cursor.rowcount
        except Exception:
            print('failed to search company ID')
            raise

    def updateCompany(self, companyID,
                      companyName=None, companyNationality=None):
        """Update company with company ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify company info')

        try:
            self._update(COMPANY_TABLE.table, self.__columns,
                         (companyName, companyNationality),
                         self.__idAsCondition(companyID))
        except Exception:
            print('failed to update company info')
            raise

    def deleteCompany(self, companyID):
        """Delete company with company ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify company info')

        try:
            self._delete(COMPANY_TABLE.table, self.__idAsCondition(companyID))
        except Exception:
            print('failed to delete company info')
            raise

    def __idAsCondition(self, companyID):
        """Generate SQL condition with company ID"""
        return f'{COMPANY_TABLE.id} = {companyID}'


class CommentDB(DB):
    """Comment management interface"""
    __idColumns = (COMMENT_TABLE.filmID, COMMENT_TABLE.userID)
    __columns = (COMMENT_TABLE.rating, COMMENT_TABLE.comment)

    def __init__(self, isUser):
        """Initialize as guest or member"""
        self.role = 'member' if isUser else 'guest'
        super.__init__(self.role)

    def selectCommentByFilmID(self, filmID):
        """Select comment by film ID"""
        try:
            self._select(f'{COMMENT_TABLE.table} AS a INNER JOIN '
                         f'{USER_TABLE.table} AS b ON'
                         f'a.{COMMENT_TABLE.userID} = b.{USER_TABLE.id}',
                         (f'b.{USER_TABLE.id}', USER_TABLE.name)
                         + self.__columns,
                         f'{COMMENT_TABLE.filmID} = {filmID}')
            return self._cursor.rowcount
        except Exception:
            print('failed to select comment by film ID')
            raise

    def selectCommentByUserID(self, userID):
        """Select comment by user ID"""
        try:
            self._select(f'{COMMENT_TABLE.table} AS a INNER JOIN '
                         f'{FILM_TABLE.table} AS b ON'
                         f'a.{COMMENT_TABLE.filmID} = b.{FILM_TABLE.id}',
                         (f'b.{FILM_TABLE.id}', FILM_TABLE.chineseName)
                         + self.__columns,
                         f'{COMMENT_TABLE.userID} = {userID}')
            return self._cursor.rowcount
        except Exception:
            print('failed to select comment by user ID')
            raise

    def selectFilmAverageRating(self, filmID):
        """Select average rating by film ID"""
        try:
            self._select(COMMENT_TABLE.table,
                         (f'AVG({COMMENT_TABLE.rating})', ),
                         f'{COMMENT_TABLE.filmID} = {filmID}')
            return self._cursor.rowcount
        except Exception:
            print('failed to select average rating by film ID')
            raise

    def upsertComment(self, filmID, userID, rating=None, userComment=None):
        """Insert new or update existed comment with film ID and user ID"""
        if self.role != 'member':
            raise RuntimeError('only members can modify comments')

        condition = self.__idAsCondition(filmID, userID)

        try:
            self._select(COMMENT_TABLE.table, self.__idColumns, condition)

            if self._cursor.rowcount == 0:
                self._insert(COMMENT_TABLE.table,
                             self.__idColumns + self.__columns,
                             (filmID, userID, rating, userComment))
            else:
                self._update(COMMENT_TABLE.table, self.__columns,
                             (rating, userComment), condition)
        except Exception:
            print('failed to insert or update comment')
            raise

    def deleteComment(self, filmID, userID):
        """Delete comment with film ID and user ID"""
        if self.role != 'member':
            raise RuntimeError('only members can modify comments')

        try:
            self._delete(COMMENT_TABLE.table,
                         self.__idAsCondition(filmID, userID))
        except Exception:
            print('failed to delete comment')
            raise

    def __idAsCondition(self, filmID, userID):
        """Generate SQL condition with film ID and user ID"""
        return f'{self.__idColumns[0]} = {filmID} AND '\
            + f'{self.__idColumns[1]} = {userID}'


class UserDB(DB):
    """User info management interface"""
    __columns = (USER_TABLE.name,
                 USER_TABLE.age,
                 USER_TABLE.sex)

    def __init__(self, isLogin, isAdmin):
        """Initialize as login verifier, member or user administrator"""
        self.role = 'login' if isLogin else 'usr_admin' if isAdmin else 'member'
        super.__init__(self.role)

    def verifyLogin(self, userID, password):
        """Verify login """
        if self.role != 'login':
            raise RuntimeError('only login interface can verify login')

        self._select(USER_TABLE.table, USER_TABLE.password,
                     self.__idAsCondition(userID))

        if self._cursor.rowcount == 0:
            return False

        hashed = self.fetchResult(1)[0]
        return Password.verify(password, hashed)

    def createUser(self, userID, password, userIsAdmin,
                   userName=None,
                   userAge=None,
                   userSex=None):
        """Create new user"""
        if self.role != 'usr_admin':
            raise RuntimeError('only user administrators can create new user')

        hashed = Password.encrypt(password)
        columns = (USER_TABLE.id, USER_TABLE.password, USER_TABLE.isAdmin)\
            + self.__columns

        try:
            self._insert(self.__table, columns,
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
            self._select(USER_TABLE.table, self.__columns,
                         self.__idAsCondition(userID))
            return self._cursor.rowcount
        except Exception:
            print('failed to select user info')
            raise

    def updateUserInfo(self, userID,
                       userName=None,
                       userAge=None,
                       userSex=None):
        """Update user info with user ID"""
        if self.role != 'member':
            raise RuntimeError('only users can modify user info')

        try:
            self._update(USER_TABLE.table, self.__columns,
                         (userName, userAge, userSex),
                         self.__idAsCondition(userID))
        except Exception:
            print('failed to update user info')
            raise

    def updateUserPassword(self, userID, password):
        """Update user password with user ID"""
        if self.role != 'member':
            raise RuntimeError('only users can modify user password')

        try:
            self._update(USER_TABLE.table, (USER_TABLE.password, ),
                         (password, ), self.__idAsCondition(userID))
        except Exception:
            print('failed to update user info')
            raise

    def updateUserAdmin(self, userID, userIsAdmin):
        """Update user administration status with user ID"""
        if self.role != 'usr_admin':
            raise RuntimeError('only user administrators can modify '
                               'user administration status')

        try:
            self._update(USER_TABLE.table, (USER_TABLE.isAdmin, ),
                         (userIsAdmin, ), self.__idAsCondition(userID))
        except Exception:
            print('failed to update user administration status')
            raise

    def deleteUser(self, userID):
        """Delete user with user ID"""
        if self.role != 'usr_admin':
            raise RuntimeError('only user administrators can create new user')

        try:
            self._delete(USER_TABLE.table, self.__idAsCondition(userID))
        except Exception:
            print('failed to delete user info')
            raise

    def __idAsCondition(self, userID):
        """Generate SQL condition with user ID"""
        return f'{USER_TABLE.id} = {userID}'
