from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from ..DBInterface import (CAST_TABLE, COMPANY_TABLE, DIRECTOR_TABLE,
                           FILM_TABLE, GENRE_TABLE, CastInterface,
                           CompanyInterface, DirectorInterface, FilmInterface,
                           GenreInterface, getColumn)
from .SubInfoDialogUI import Ui_SubInfoDialog


class SubInfoDialog(QDialog, Ui_SubInfoDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        self.companyManager = CompanyInterface(True)
        self.genreManager = GenreInterface(True)
        self.directorManager = DirectorInterface(True)
        self.castManager = CastInterface(True)
        self.filmChecker = FilmInterface(False)

        self.searchCompany()
        self.searchGenre()
        self.searchDirector()
        self.searchCast()

    def searchCompany(self):
        self.companies = []
        self.companyManager.searchCompany(self.CompanySearchText.text())
        result = self.companyManager.fetchResult(50)
        self.CompanySearchResult.clearContents()
        self.CompanySearchResult.setRowCount(len(result))

        for index, row in enumerate(result):
            companyID = getColumn(row, COMPANY_TABLE.id)
            name = getColumn(row, COMPANY_TABLE.name)
            nationality = getColumn(row, COMPANY_TABLE.nationality)

            self.companies.append(companyID)
            self.CompanySearchResult.setItem(index, 0,
                                             QTableWidgetItem(name if name is not None else '--'))
            self.CompanySearchResult.setItem(index, 1,
                                             QTableWidgetItem(nationality if nationality is not None
                                                              else '--'))

    def loadCompany(self, row, _):
        self.companyManager.selectCompany(self.companies[row])
        result = self.companyManager.fetchResult()

        if len(result) == 0:
            raise RuntimeError('attempted to load a ghost company')

        name = getColumn(result[0], COMPANY_TABLE.name)
        nationality = getColumn(result[0], COMPANY_TABLE.nationality)
        self.CompanyName.setText(name if name is not None else '')
        self.CompanyNationality.setText(nationality if nationality is not None else '')

    def addCompany(self):
        name = self.CompanyName.text()

        if name == '':
            QMessageBox.critical(self, '添加公司', '公司名称不能为空！')
            return

        nationality = self.CompanyNationality.text()
        if nationality == '':
            nationality = None

        self.companyManager.insertCompany(companyName=name, companyNationality=nationality)
        result = self.castManager.fetchResult(1)

        if len(result) == 0:
            raise RuntimeError('company inserted into void')

        QMessageBox.information(self, '添加公司', '公司添加成功！')
        self.CompanySearchText.setText(name)
        self.searchCompany()

    def modifyCompany(self):
        selected = self.CompanySearchResult.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '修改公司', '请先选择一个公司！')
            return

        row = self.CompanySearchResult.row(selected[0])

        name = self.CompanyName.text()
        if name == '':
            QMessageBox.critical(self, '修改公司', '公司名称不能为空！')
            return

        nationality = self.CompanyNationality.text()
        if nationality == '':
            nationality = None

        self.companyManager.updateCompany(self.companies[row], companyName=name,
                                          companyNationality=nationality)

        QMessageBox.information(self, '修改公司', '公司修改成功！')
        self.CompanySearchText.setText(name)
        self.searchCompany()

    def deleteCompany(self):
        selected = self.CompanySearchResult.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '删除公司', '请先选择一个公司！')
            return

        row = self.CompanySearchResult.row(selected[0])
        companyID = self.companies[row]

        self.filmChecker._custom(f'SELECT COUNT(*) FROM {FILM_TABLE.table} '
                                 f'WHERE {FILM_TABLE.companyID} = ?', (companyID, ))
        count = self.filmChecker.fetchResult()

        if len(count) > 0 and count[0][0] > 0:
            QMessageBox.critical(self, '删除公司', '公司仍有电影关联，删除失败！')
            return

        result = QMessageBox.warning(self, '删除公司', '删除操作不可恢复，是否继续？',
                                     QMessageBox.Yes | QMessageBox.No)

        if result == QMessageBox.Yes:
            self.companyManager.deleteCompany(self.companies[row])
            QMessageBox.information(self, '删除公司', '公司删除成功！')
            self.searchCompany()

    def searchGenre(self):
        self.genres = []
        self.genreManager.searchGenre(self.GenreSearchText.text())
        result = self.genreManager.fetchResult(50)
        self.GenreSearchResult.clearContents()
        self.GenreSearchResult.setRowCount(len(result))

        for index, row in enumerate(result):
            genreID = getColumn(row, GENRE_TABLE.id)
            name = getColumn(row, GENRE_TABLE.name)

            self.genres.append(genreID)
            self.GenreSearchResult.setItem(index, 0,
                                           QTableWidgetItem(name if name is not None else '--'))

    def loadGenre(self, row, _):
        self.genreManager.selectGenre(self.genres[row])
        result = self.genreManager.fetchResult()

        if len(result) == 0:
            raise RuntimeError('attempted to load a ghost genre')

        name = getColumn(result[0], GENRE_TABLE.name)
        self.GenreName.setText(name if name is not None else '')

    def addGenre(self):
        name = self.GenreName.text()

        if name == '':
            QMessageBox.critical(self, '添加分类', '分类名称不能为空！')
            return

        self.genreManager.insertGenre(genreName=name)
        result = self.castManager.fetchResult(1)

        if len(result) == 0:
            raise RuntimeError('genre inserted into void')

        QMessageBox.information(self, '添加分类', '分类添加成功！')
        self.GenreSearchText.setText(name)
        self.searchGenre()

    def modifyGenre(self):
        selected = self.GenreSearchResult.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '修改分类', '请先选择一个分类！')
            return

        row = self.GenreSearchResult.row(selected[0])

        name = self.GenreName.text()
        if name == '':
            QMessageBox.critical(self, '修改分类', '分类名称不能为空！')
            return

        self.genreManager.updateGenre(self.genres[row], genreName=name)

        QMessageBox.information(self, '修改分类', '分类修改成功！')
        self.GenreSearchText.setText(name)
        self.searchGenre()

    def deleteGenre(self):
        selected = self.GenreSearchResult.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '删除分类', '请先选择一个分类！')
            return

        row = self.GenreSearchResult.row(selected[0])
        result = QMessageBox.warning(self, '删除分类',
                                     '所有该分类下电影的该分类标签将同步删除，是否继续？',
                                     QMessageBox.Yes | QMessageBox.No)

        if result == QMessageBox.Yes:
            self.genreManager.deleteGenre(self.genres[row])
            QMessageBox.information(self, '删除分类', '分类删除成功！')
            self.searchGenre()

    def searchDirector(self):
        self.directors = []
        self.directorManager.searchDirector(self.DirectorSearchText.text())
        result = self.directorManager.fetchResult(50)
        self.DirectorSearchResult.clearContents()
        self.DirectorSearchResult.setRowCount(len(result))

        for index, row in enumerate(result):
            directorID = getColumn(row, DIRECTOR_TABLE.id)
            name = getColumn(row, DIRECTOR_TABLE.name)
            alt = getColumn(row, DIRECTOR_TABLE.alt)

            self.directors.append(directorID)
            self.DirectorSearchResult.setItem(index, 0,
                                              QTableWidgetItem(name if name is not None else '--'))
            self.DirectorSearchResult.setItem(index, 1,
                                              QTableWidgetItem(alt if alt is not None else '--'))

    def loadDirector(self, row, _):
        self.directorManager.selectDirector(self.directors[row])
        result = self.directorManager.fetchResult()

        if len(result) == 0:
            raise RuntimeError('attempted to load a ghost director')

        name = getColumn(result[0], DIRECTOR_TABLE.name)
        avatar = getColumn(result[0], DIRECTOR_TABLE.avatar)
        alt = getColumn(result[0], DIRECTOR_TABLE.alt)
        self.DirectorName.setText(name if name is not None else '')
        self.DirectorAvatar.setText(avatar if avatar is not None else '')
        self.DirectorAlt.setText(alt if alt is not None else '')

    def addDirector(self):
        name = self.DirectorName.text()

        if name == '':
            QMessageBox.critical(self, '添加导演', '导演名称不能为空！')
            return

        avatar = self.DirectorAvatar.text()
        if avatar == '':
            avatar = None

        alt = self.DirectorAlt.text()
        if alt == '':
            alt = None

        self.directorManager.insertDirector(directorName=name, directorAvatar=avatar,
                                            directorAlt=alt)
        result = self.castManager.fetchResult(1)

        if len(result) == 0:
            raise RuntimeError('director inserted into void')

        QMessageBox.information(self, '添加导演', '导演添加成功！')
        self.DirectorSearchText.setText(name)
        self.searchDirector()

    def modifyDirector(self):
        selected = self.DirectorSearchResult.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '修改导演', '请先选择一个导演！')
            return

        row = self.DirectorSearchResult.row(selected[0])

        name = self.DirectorName.text()
        if name == '':
            QMessageBox.critical(self, '修改导演', '导演名称不能为空！')
            return

        avatar = self.DirectorAvatar.text()
        if avatar == '':
            avatar = None

        alt = self.DirectorAlt.text()
        if alt == '':
            alt = None

        self.directorManager.updateDirector(self.directors[row], directorName=name,
                                            directorAvatar=avatar, directorAlt=alt)

        QMessageBox.information(self, '修改导演', '导演修改成功！')
        self.DirectorSearchText.setText(name)
        self.searchDirector()

    def deleteDirector(self):
        selected = self.DirectorSearchResult.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '删除导演', '请先选择一个导演！')
            return

        row = self.DirectorSearchResult.row(selected[0])
        result = QMessageBox.warning(self, '删除导演',
                                     '所有该导演执导电影的该导演标签将同步删除，是否继续？',
                                     QMessageBox.Yes | QMessageBox.No)

        if result == QMessageBox.Yes:
            self.directorManager.deleteDirector(self.directors[row])
            QMessageBox.information(self, '删除导演', '导演删除成功！')
            self.searchDirector()

    def searchCast(self):
        self.casts = []
        self.castManager.searchCast(self.CastSearchText.text())
        result = self.castManager.fetchResult(50)
        self.CastSearchResult.clearContents()
        self.CastSearchResult.setRowCount(len(result))

        for index, row in enumerate(result):
            castID = getColumn(row, CAST_TABLE.id)
            name = getColumn(row, CAST_TABLE.name)
            alt = getColumn(row, CAST_TABLE.alt)

            self.casts.append(castID)
            self.CastSearchResult.setItem(index, 0,
                                          QTableWidgetItem(name if name is not None else '--'))
            self.CastSearchResult.setItem(index, 1,
                                          QTableWidgetItem(alt if alt is not None else '--'))

    def loadCast(self, row, _):
        self.castManager.selectCast(self.casts[row])
        result = self.castManager.fetchResult()

        if len(result) == 0:
            raise RuntimeError('attempted to load a ghost cast')

        name = getColumn(result[0], CAST_TABLE.name)
        avatar = getColumn(result[0], CAST_TABLE.avatar)
        alt = getColumn(result[0], CAST_TABLE.alt)
        self.CastName.setText(name if name is not None else '')
        self.CastAvatar.setText(avatar if avatar is not None else '')
        self.CastAlt.setText(alt if alt is not None else '')

    def addCast(self):
        name = self.CastName.text()

        if name == '':
            QMessageBox.critical(self, '添加演员', '演员名称不能为空！')
            return

        avatar = self.CastAvatar.text()
        if avatar == '':
            avatar = None

        alt = self.CastAlt.text()
        if alt == '':
            alt = None

        self.castManager.insertCast(castName=name, castAvatar=avatar, castAlt=alt)
        result = self.castManager.fetchResult(1)

        if len(result) == 0:
            raise RuntimeError('cast inserted into void')

        QMessageBox.information(self, '添加演员', '演员添加成功！')
        self.CastSearchText.setText(name)
        self.searchCast()

    def modifyCast(self):
        selected = self.CastSearchResult.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '修改演员', '请先选择一个演员！')
            return

        row = self.CastSearchResult.row(selected[0])

        name = self.CastName.text()
        if name == '':
            QMessageBox.critical(self, '修改演员', '演员名称不能为空！')
            return

        avatar = self.CastAvatar.text()
        if avatar == '':
            avatar = None

        alt = self.CastAlt.text()
        if alt == '':
            alt = None

        self.castManager.updateCast(self.casts[row], castName=name, castAvatar=avatar, castAlt=alt)
        QMessageBox.information(self, '修改演员', '演员修改成功！')
        self.CastSearchText.setText(name)
        self.searchCast()

    def deleteCast(self):
        selected = self.CastSearchResult.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '删除演员', '请先选择一个演员！')
            return

        row = self.CastSearchResult.row(selected[0])
        result = QMessageBox.warning(self, '删除演员',
                                     '所有该演员出演电影的该演员标签将同步删除，是否继续？',
                                     QMessageBox.Yes | QMessageBox.No)

        if result == QMessageBox.Yes:
            self.castManager.deleteCast(self.casts[row])
            QMessageBox.information(self, '删除演员', '演员删除成功！')
            self.searchCast()
