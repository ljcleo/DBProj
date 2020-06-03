from dotenv import load_dotenv
from os import getenv
from os.path import abspath, exist, split

from pyodbc import connect
from yaml import full_load

from .password import Password


class DB:
    """Database manipulation base class"""

    def __init__(self, role):
        """Create connection and cursor with given role"""
        try:
            load_dotenv()
        except Exception:
            raise RuntimeError('.env not found')

        password = getenv(role)
        if password is None:
            raise ValueError(f'"{role}" is not an available role')

        config_path = split(abspath(__file__))[0] + '/config.yaml'
        if not exist(config_path):
            raise RuntimeError(f'config file not found at {config_path}')

        with open(config_path, 'r', encoding='utf8') as f:
            config = full_load(f)

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

    def _insert_many(self, table, columns, values):
        """Insert multiple records to table at given columns"""
        column_len = len(columns)
        if any(column_len == len(value_set) for value_set in values):
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

    __table = 'Film'
    __id_column = 'Film_ID'

    __columns = ('Film_Chinese_Name',
                 'Film_Original_Name',
                 'Release_Date',
                 'Length',
                 'Storyline',
                 'Prize_History',
                 'Remark')

    __genre_table = 'Genre'
    __genre_columns = ('Film_ID', 'Genre_ID')

    __directing_table = 'Directing'
    __directing_columns = ('Film_ID', 'Director_ID', 'Director_Role')

    __play_table = 'Play'
    __play_columns = ('Film_ID', 'Cast_ID', 'Cast_Role')

    __production_table = 'Production'
    __production_columns = ('Film_ID', 'Company_ID')

    def __init__(self, is_admin):
        """Initialize as guest or administrator"""
        self.role = 'admin' if is_admin else 'guest'
        super().__init__(self.role)

    def insert_film(self,
                    film_chinese_name=None,
                    film_original_name=None,
                    release_date=None,
                    length=None,
                    storyline=None,
                    prize_history=None,
                    remark=None):
        """Insert new film"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._insert(self.__table, self.__columns,
                         (film_chinese_name,
                          film_original_name,
                          release_date,
                          length,
                          storyline,
                          prize_history,
                          remark))
        except Exception:
            print('failed to insert new film data')
            raise

    def insert_many_films(self,
                          film_chinese_names=None,
                          film_original_names=None,
                          release_dates=None,
                          lengths=None,
                          storylines=None,
                          prize_histories=None,
                          remarks=None):
        """Insert multiple new films"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._insert(self.__table, self.__columns,
                         zip(film_chinese_names,
                             film_original_names,
                             release_dates,
                             lengths,
                             storylines,
                             prize_histories,
                             remarks))
        except Exception:
            print('failed to insert new film data')
            raise

    def select_film(self, **kwargs):
        """Select films (not implemented)"""
        raise NotImplementedError('film select function not implemented')

    def update_film_basic(self, film_id,
                          film_chinese_name=None,
                          film_original_name=None,
                          release_date=None,
                          length=None):
        """Update basic film data (without text data) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(self.__table, self.__columns[:-3],
                         (film_chinese_name,
                          film_original_name,
                          release_date,
                          length),
                         self.__id_as_condition(film_id))
        except Exception:
            print('failed to update film basic data')
            raise

    def update_film_storyline(self, film_id, storyline=None):
        """Update film storyline with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(self.__table, (self.__columns[-3], ),
                         (storyline, ),
                         self.__id_as_condition(film_id))
        except Exception:
            print('failed to update film storyline')
            raise

    def update_film_prize_history(self, film_id, prize_history=None):
        """Update film prize history with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(self.__table, (self.__columns[-2], ),
                         (prize_history, ),
                         self.__id_as_condition(film_id))
        except Exception:
            print('failed to update film prize history')
            raise

    def update_film_remark(self, film_id, remark=None):
        """Update film remark with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._update(self.__table, (self.__columns[-1], ),
                         (remark, ),
                         self.__id_as_condition(film_id))
        except Exception:
            print('failed to update film remark')
            raise

    def delete_film(self, film_id):
        """Delete film with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(self.__table, self.__id_as_condition(film_id))
        except Exception:
            print('failed to delete film data')
            raise

    def update_film_genre(self, film_id, genre_ids):
        """Update film genre (all pairs) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(self.__genre_table, self.__id_as_condition(film_id))
            values = [(film_id, genre_id) for genre_id in genre_ids]
            self._insert_many(self.__genre_table, self.__genre_columns, values)
        except Exception:
            print('failed to update film genre')
            raise

    def update_film_directing_info(self, film_id, director_ids, director_roles):
        """Update film directing info (all pairs) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(self.__director_table, self.__id_as_condition(film_id))

            values = [(film_id, director_id, director_role)
                      for director_id, director_role
                      in zip(director_ids, director_roles)]

            self._insert_many(self.__directing_table, self.__directing_columns,
                              values)
        except Exception:
            print('failed to update film directing info')
            raise

    def update_film_play_info(self, film_id, cast_ids, cast_roles):
        """Update film play info (all pairs) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(self.__play_table, self.__id_as_condition(film_id))

            values = [(film_id, cast_id, cast_role)
                      for cast_id, cast_role in zip(cast_ids, cast_roles)]

            self._insert_many(self.__play_table, self.__play_columns, values)
        except Exception:
            print('failed to update film play info')
            raise

    def update_film_production(self, film_id, company_ids):
        """Update film production (all pairs) with film ID"""
        if self.role != 'admin':
            raise RuntimeError('only administrators can modify film data')

        try:
            self._delete(self.__production_table,
                         self.__id_as_condition(film_id))

            values = [(film_id, company_id) for company_id in company_ids]

            self._insert_many(self.__production_table,
                              self.__production_columns, values)
        except Exception:
            print('failed to update film production')
            raise

    def __id_as_condition(self, film_id):
        """Generate SQL condition with film ID"""
        return f'{self.__id_column} = {film_id}'


class GenreDB(DB):
    """Genre info management interface"""

    __table = 'Genre_Info'
    __id_column = 'Genre_ID'
    __columns = ('Genre_Name', )

    def __init__(self):
        """Initialize as administrator"""
        super().__init__('admin')

    def insert_genre(self, genre_name=None):
        """Insert new genre"""
        try:
            self._insert(self.__table, self.__columns, (genre_name, ))
        except Exception:
            print('failed to insert new genre info')
            raise

    def insert_many_genres(self, genre_names=None):
        """Insert multiple new genres"""
        try:
            self._insert(self.__table, self.__columns, zip(genre_names))
        except Exception:
            print('failed to insert new genre info')
            raise

    def update_genre(self, genre_id, genre_name=None):
        """Update genre with genre ID"""
        try:
            self._update(self.__table, self.__columns, (genre_name),
                         self.__id_as_condition(genre_id))
        except Exception:
            print('failed to update genre info')
            raise

    def delete_genre(self, genre_id):
        """Delete genre with genre ID"""
        try:
            self._delete(self.__table, self.__id_as_condition(genre_id))
        except Exception:
            print('failed to delete genre info')
            raise

    def __id_as_condition(self, genre_id):
        """Generate SQL condition with genre ID"""
        return f'{self.__id_column} = {genre_id}'


class DirectorDB(DB):
    """Director info management interface"""

    __table = 'Director'
    __id_column = 'Director_ID'

    __columns = ('Director_Name',
                 'Director_Sex',
                 'Director_Birth',
                 'Director_Nationality')

    def __init__(self):
        """Initialize as administrator"""
        super().__init__('admin')

    def insert_director(self,
                        director_name=None,
                        director_sex=None,
                        director_birth=None,
                        director_nationality=None):
        """Insert new director"""
        try:
            self._insert(self.__table, self.__columns,
                         (director_name,
                          director_sex,
                          director_birth,
                          director_nationality))
        except Exception:
            print('failed to insert new director info')
            raise

    def insert_many_directors(self,
                              director_names=None,
                              director_sexes=None,
                              director_births=None,
                              director_nationalities=None):
        """Insert multiple new directors"""
        try:
            self._insert(self.__table, self.__columns,
                         zip(director_names,
                             director_sexes,
                             director_births,
                             director_nationalities))
        except Exception:
            print('failed to insert new director info')
            raise

    def update_director(self, director_id,
                        director_name=None,
                        director_sex=None,
                        director_birth=None,
                        director_nationality=None):
        """Update genre with genre ID"""
        try:
            self._update(self.__table, self.__columns,
                         (director_name,
                          director_sex,
                          director_birth,
                          director_nationality),
                         self.__id_as_condition(director_id))
        except Exception:
            print('failed to update director info')
            raise

    def delete_director(self, director_id):
        """Delete genre with genre ID"""
        try:
            self._delete(self.__table, self.__id_as_condition(director_id))
        except Exception:
            print('failed to delete director info')
            raise

    def __id_as_condition(self, director_id):
        """Generate SQL condition with director ID"""
        return f'{self.__id_column} = {director_id}'


class CastDB(DB):
    __table = 'Film_Cast'
    __id_column = 'Cast_ID'
    __columns = ('Cast_Name', 'Cast_Sex', 'Cast_Birth', 'Cast_Nationality')

    def __init__(self):
        """Initialize as administrator"""
        super().__init__('admin')

    def insert_cast(self,
                    cast_name=None,
                    cast_sex=None,
                    cast_birth=None,
                    cast_nationality=None):
        """Insert new cast"""
        try:
            self._insert(self.__table, self.__columns,
                         (cast_name,
                          cast_sex,
                          cast_birth,
                          cast_nationality))
        except Exception:
            print('failed to insert new cast info')
            raise

    def insert_many_casts(self,
                          cast_names=None,
                          cast_sexes=None,
                          cast_births=None,
                          cast_nationalities=None):
        """Insert multiple new casts"""
        try:
            self._insert(self.__table, self.__columns,
                         zip(cast_names,
                             cast_sexes,
                             cast_births,
                             cast_nationalities))
        except Exception:
            print('failed to insert new cast info')
            raise

    def update_cast(self, cast_id,
                    cast_name=None,
                    cast_sex=None,
                    cast_birth=None,
                    cast_nationality=None):
        """Update cast with cast ID"""
        try:
            self._update(self.__table, self.__columns,
                         (cast_name,
                          cast_sex,
                          cast_birth,
                          cast_nationality),
                         self.__id_as_condition(cast_id))
        except Exception:
            print('failed to update cast info')
            raise

    def delete_cast(self, cast_id):
        """Delete cast with cast ID"""
        try:
            self._delete(self.__table, self.__id_as_condition(cast_id))
        except Exception:
            print('failed to delete cast info')
            raise

    def __id_as_condition(self, cast_id):
        """Generate SQL condition with cast ID"""
        return f'{self.__id_column} = {cast_id}'


class CompanyDB(DB):
    __table = 'Company_Info'
    __id_column = 'Company_ID'
    __columns = ('Company_Name', 'Company_Nationality')

    def __init__(self):
        """Initialize as administrator"""
        super().__init__('admin')

    def insert_company(self, company_name=None, company_nationality=None):
        """Insert new company"""
        try:
            self._insert(self.__table, self.__columns,
                         (company_name, company_nationality))
        except Exception:
            print('failed to insert new company info')
            raise

    def insert_many_companies(self,
                              company_names=None,
                              company_nationalities=None):
        """Insert multiple new companies"""
        try:
            self._insert(self.__table, self.__columns,
                         zip(company_names, company_nationalities))
        except Exception:
            print('failed to insert new company info')
            raise

    def update_company(self, company_id,
                       company_name=None,
                       company_nationality=None):
        """Update company with company ID"""
        try:
            self._update(self.__table, self.__columns,
                         (company_name, company_nationality),
                         self.__id_as_condition(company_id))
        except Exception:
            print('failed to update company info')
            raise

    def delete_company(self, company_id):
        """Delete company with company ID"""
        try:
            self._delete(self.__table, self.__id_as_condition(company_id))
        except Exception:
            print('failed to delete company info')
            raise

    def __id_as_condition(self, company_id):
        """Generate SQL condition with company ID"""
        return f'{self.__id_column} = {company_id}'


class CommentDB(DB):
    __table = 'Comment'
    __id_columns = ('Film_ID', 'Users_ID')
    __columns = ('Rating', 'Users_Comment')

    def __init__(self, is_user):
        """Initialize as guest or member"""
        self.role = 'member' if is_user else 'guest'
        super.__init__(self.role)

    def upsert_comment(self, film_id, user_id,
                       rating=None, user_comment=None):
        """Insert new or update existed comment with film ID and user ID"""
        if self.role != 'member':
            raise RuntimeError('only members can modify comments')

        condition = self.__id_as_condition(film_id, user_id)

        try:
            self._select(self.__table, self.__id_columns, condition)

            if self._cursor.rowcount == 0:
                self._insert(self.__table, self.__id_columns + self.__columns,
                             (film_id, user_id, rating, user_comment))
            else:
                self._update(self.__table, self.__columns,
                             (rating, user_comment), condition)
        except Exception:
            print('failed to insert or update comment')
            raise

    def delete_comment(self, film_id, user_id):
        """Delete comment with film ID and user ID"""
        if self.role != 'member':
            raise RuntimeError('only members can modify comments')

        try:
            self._delete(self.__table,
                         self.__id_as_condition(film_id, user_id))
        except Exception:
            print('failed to delete comment')
            raise

    def __id_as_condition(self, film_id, user_id):
        """Generate SQL condition with film ID and user ID"""
        return f'{self.__id_columns[0]} = {film_id} AND '\
            + f'{self.__id_columns[1]} = {user_id}'


class UserDB(DB):
    __table = 'Users'
    __id_column = 'Users_ID'
    __password_column = 'Users_Password'
    __admin_column = 'Users_Is_Admin'

    __columns = ('Users_Name',
                 'Users_Age',
                 'Users_Sex',
                 'Users_Is_Admin')

    def __init__(self, is_login, is_admin):
        """Initialize as login verifier, member or user administrator"""
        self.role = 'login' if is_login else \
            'usr_admin' if is_admin else 'member'

        super.__init__(self.role)

    def verify_login(self, user_id, password):
        """Verify login """
        if self.role != 'login':
            raise RuntimeError('only login interface can verify login')

        self._select(self.__table, self.__password_column,
                     self.__id_as_condition(user_id))

        if self._cursor.rowcount == 0:
            return False

        hashed = self._cursor.fetchone()
        return Password.verify(password, hashed)

    def create_user(self, user_id, password, is_admin,
                    user_name=None,
                    user_age=None,
                    user_sex=None):
        """Create new user"""
        if self.role != 'usr_admin':
            raise RuntimeError('only user administrators can create new user')

        hashed = Password.encrypt(password)
        columns = (self.__id_column + self.__password_column
                   + self.__admin_column) + self.__columns

        try:
            self._insert(self.__table, columns,
                         (user_id,
                          hashed,
                          is_admin,
                          user_name,
                          user_age,
                          user_sex))
        except Exception:
            print('failed to insert new user')
            raise

    def update_user_info(self, user_id,
                         user_name=None,
                         user_age=None,
                         user_sex=None):
        """Update user info with user ID"""
        if self.role != 'member':
            raise RuntimeError('only users can modify user info')

        try:
            self._update(self.__table, self.__columns,
                         (user_name, user_age, user_sex),
                         self.__id_as_condition(user_id))
        except Exception:
            print('failed to update user info')
            raise

    def update_admin(self, user_id, is_admin):
        """Update user administrator status with user ID"""
        if self.role != 'usr_admin':
            raise RuntimeError('only user administrators can modify '
                               'user administration status')

        try:
            self._update(self.__table, (self.__admin_column, ), (is_admin, ),
                         self.__id_as_condition(user_id))
        except Exception:
            print('failed to update user administration status')
            raise

    def delete_user(self, user_id):
        """Delete user with user ID"""
        if self.role != 'member':
            raise RuntimeError('only users can delete user')

        try:
            self._delete(self.__table, self.__id_as_condition(user_id))
        except Exception:
            print('failed to delete user info')
            raise

    def __id_as_condition(self, user_id):
        """Generate SQL condition with user ID"""
        return f'{self.__id_column} = {user_id}'
