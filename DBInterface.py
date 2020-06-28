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
                                       'nationality': 'Director_Nationality'})

CAST_TABLE = TableDef('Film_Cast', {'id': 'Cast_ID',
                                    'name': 'Cast_Name',
                                    'sex': 'Cast_Sex',
                                    'birth': 'Cast_Birth',
                                    'nationality': 'Cast_Nationality'})

COMPANY_TABLE = TableDef('Company', {'id': 'Company_ID',
                                     'name': 'Company_Name',
                                     'nationality': 'Company_City'})

FILM_TABLE = TableDef('Film', {'id': 'Film_ID',
                               'chineseName': 'Film_Chinese_Name',
                               'originalName': 'Film_Original_Name',
                               'releaseDate': 'Release_Date',
                               'length': 'Length',
                               'companyID': 'Company_ID',
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

    def _insert(self, table, columns, values):
        """Insert single record to table at given columns"""
        if len(columns) != len(values):
            raise ValueError('columns and values do not match')

        placeholder = ", ".join(["%s"] * len(values))
        sql = f'INSERT %s({placeholder}) VALUES ({placeholder})'
        self._cursor.execute(sql, (table, ) + columns + values)

    def _insertMany(self, table, columns, values):
        """Insert multiple records to table at given columns"""
        columnLen = len(columns)
        if any(columnLen == len(valueSet) for valueSet in values):
            raise ValueError('columns and (some) values do not match')

        placeholder = ", ".join(["%s"] * len(values))
        sql = f'INSERT {table}({", ".join(columns)}) VALUES ({placeholder})'
        self._cursor.executemany(sql, values)

    def _select(self, table, columns, condition):
        """Select records with given columns from table where condition holds"""
        placeholder = ", ".join(["%s"] * len(columns))
        sql = f'SELECT {placeholder} FROM %s WHERE %s'
        self._cursor.execute(sql, (table, ) + columns + (condition, ))

    def _update(self, table, columns, values, condition):
        """Update record from table at given columns with values where """
        """condition holds"""
        if len(columns) != len(values):
            raise ValueError('columns and values do not match')

        placeholder = ", ".join(["%s = %s"] * len(values))
        sql = f'UPDATE %s SET {placeholder} WHERE %s'

        params = (table, )
        for pair in zip(columns, values):
            params = params + pair
        params = params + (condition, )

        self._cursor.execute(sql, params)

    def _delete(self, table, condition):
        """Delete record from table where condition holds"""
        sql = 'DELETE FROM %s WHERE %s'
        self._cursor.execute(sql, (table, condition))

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
                             storylines,
                             prizeHistories,
                             remarks))
        except Exception:
            print('failed to insert new film data')
            raise

    def selectFilm(self, **kwargs):
        """Select films (not implemented)"""
        raise NotImplementedError('film select function not implemented')

    def updateFilmBasic(self, filmID,
                        filmChineseName=None,
                        filmOriginalName=None,
                        releaseDate=None,
                        length=None,
                        companyID=None):
        """Update basic film data (without text data) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(FILM_TABLE.table, self.__columns[:-3],
                         (filmChineseName,
                          filmOriginalName,
                          releaseDate,
                          length,
                          companyID),
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

    def __init__(self):
        """Initialize as administrator"""
        super().__init__('admin')

    def insertGenre(self, genreName=None):
        """Insert new genre"""
        try:
            self._insert(GENRE_TABLE.table, self.__columns, (genreName, ))
        except Exception:
            print('failed to insert new genre info')
            raise

    def insertManyGenres(self, genreNames=None):
        """Insert multiple new genres"""
        try:
            self._insert(GENRE_TABLE.table, self.__columns, zip(genreNames))
        except Exception:
            print('failed to insert new genre info')
            raise

    def updateGenre(self, genreID, genreName=None):
        """Update genre with genre ID"""
        try:
            self._update(GENRE_TABLE.table, self.__columns, (genreName, ),
                         self.__idAsCondition(genreID))
        except Exception:
            print('failed to update genre info')
            raise

    def deleteGenre(self, genreID):
        """Delete genre with genre ID"""
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
                 DIRECTOR_TABLE.nationality)

    def __init__(self):
        """Initialize as administrator"""
        super().__init__('admin')

    def insertDirector(self,
                       directorName=None,
                       directorSex=None,
                       directorBirth=None,
                       directorNationality=None):
        """Insert new director"""
        try:
            self._insert(DIRECTOR_TABLE.table, self.__columns,
                         (directorName,
                          directorSex,
                          directorBirth,
                          directorNationality))
        except Exception:
            print('failed to insert new director info')
            raise

    def insertManyDirectors(self,
                            directorNames=None,
                            directorSexes=None,
                            directorBirths=None,
                            directorNationalities=None):
        """Insert multiple new directors"""
        try:
            self._insert(DIRECTOR_TABLE.table, self.__columns,
                         zip(directorNames,
                             directorSexes,
                             directorBirths,
                             directorNationalities))
        except Exception:
            print('failed to insert new director info')
            raise

    def updateDirector(self, directorID,
                       directorName=None,
                       directorSex=None,
                       directorBirth=None,
                       directorNationality=None):
        """Update genre with genre ID"""
        try:
            self._update(DIRECTOR_TABLE.table, self.__columns,
                         (directorName,
                          directorSex,
                          directorBirth,
                          directorNationality),
                         self.__idAsCondition(directorID))
        except Exception:
            print('failed to update director info')
            raise

    def deleteDirector(self, directorID):
        """Delete genre with genre ID"""
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
                 CAST_TABLE.nationality)

    def __init__(self):
        """Initialize as administrator"""
        super().__init__('admin')

    def insertCast(self,
                   castName=None,
                   castSex=None,
                   castBirth=None,
                   castNationality=None):
        """Insert new cast"""
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
                        castNationalities=None):
        """Insert multiple new casts"""
        try:
            self._insert(CAST_TABLE.table, self.__columns,
                         zip(castNames,
                             castSexes,
                             castBirths,
                             castNationalities))
        except Exception:
            print('failed to insert new cast info')
            raise

    def updateCast(self, castID,
                   castName=None,
                   castSex=None,
                   castBirth=None,
                   castNationality=None):
        """Update cast with cast ID"""
        try:
            self._update(CAST_TABLE.table, self.__columns,
                         (castName, castSex, castBirth, castNationality),
                         self.__idAsCondition(castID))
        except Exception:
            print('failed to update cast info')
            raise

    def deleteCast(self, castID):
        """Delete cast with cast ID"""
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

    def __init__(self):
        """Initialize as administrator"""
        super().__init__('admin')

    def insertCompany(self, companyName=None, companyNationality=None):
        """Insert new company"""
        try:
            self._insert(COMPANY_TABLE.table, self.__columns,
                         (companyName, companyNationality))
        except Exception:
            print('failed to insert new company info')
            raise

    def insertManyCompanies(self, companyNames=None, companyNationalities=None):
        """Insert multiple new companies"""
        try:
            self._insert(COMPANY_TABLE.table, self.__columns,
                         zip(companyNames, companyNationalities))
        except Exception:
            print('failed to insert new company info')
            raise

    def updateCompany(self, companyID,
                      companyName=None, companyNationality=None):
        """Update company with company ID"""
        try:
            self._update(COMPANY_TABLE.table, self.__columns,
                         (companyName, companyNationality),
                         self.__idAsCondition(companyID))
        except Exception:
            print('failed to update company info')
            raise

    def deleteCompany(self, companyID):
        """Delete company with company ID"""
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

        hashed = self._cursor.fetchone()
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
