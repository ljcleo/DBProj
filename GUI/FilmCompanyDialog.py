from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from ..DBInterface import COMPANY_TABLE, CompanyInterface, getColumn
from .FilmCompanyDialogUI import Ui_FilmCompanyDialog


class FilmCompanyDialog(QDialog, Ui_FilmCompanyDialog):
    def __init__(self, action, companyID=None, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)

        self.companies = []
        self.companySelector = CompanyInterface(False)
        self.action = action

        if companyID is not None:
            self.companySelector.selectCompany(companyID)
            result = self.companySelector.fetchResult(1)

            if len(result) == 0:
                raise RuntimeError('attempted to locate a ghost company')

            companyName = getColumn(result[0], COMPANY_TABLE.name)
            self.SearchText.setText(companyName)

        self.refresh()

    def refresh(self):
        self.companies = []
        self.companySelector.searchCompany(self.SearchText.text())
        result = self.companySelector.fetchResult(50)
        self.SearchResult.clearContents()
        self.SearchResult.setRowCount(len(result))

        for index, row in enumerate(result):
            companyID = getColumn(row, COMPANY_TABLE.id)
            name = getColumn(row, COMPANY_TABLE.name)
            nationality = getColumn(row, COMPANY_TABLE.nationality)

            self.companies.append(companyID)
            self.SearchResult.setItem(index, 0,
                                      QTableWidgetItem(name if name is not None else '--'))
            self.SearchResult.setItem(index, 1,
                                      QTableWidgetItem(nationality if nationality is not None
                                                       else '--'))

    def tryAccept(self):
        selected = self.SearchResult.selectedItems()

        if len(selected) == 0:
            QMessageBox.information(self, '选择制作公司', '请先选择一个公司！')
            return

        row = self.SearchResult.row(selected[0])
        self.action(self.companies[row], self.SearchResult.item(row, 0).text())
        self.accept()
