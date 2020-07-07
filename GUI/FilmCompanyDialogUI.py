# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\FilmCompanyDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FilmCompanyDialog(object):
    def setupUi(self, FilmCompanyDialog):
        FilmCompanyDialog.setObjectName("FilmCompanyDialog")
        FilmCompanyDialog.resize(480, 160)
        self.SearchLabel = QtWidgets.QLabel(FilmCompanyDialog)
        self.SearchLabel.setGeometry(QtCore.QRect(20, 20, 120, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.SearchLabel.setFont(font)
        self.SearchLabel.setObjectName("SearchLabel")
        self.OKButton = QtWidgets.QPushButton(FilmCompanyDialog)
        self.OKButton.setGeometry(QtCore.QRect(20, 110, 90, 30))
        self.OKButton.setDefault(True)
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(FilmCompanyDialog)
        self.CancelButton.setGeometry(QtCore.QRect(130, 110, 90, 30))
        self.CancelButton.setObjectName("CancelButton")
        self.SearchText = QtWidgets.QLineEdit(FilmCompanyDialog)
        self.SearchText.setGeometry(QtCore.QRect(20, 50, 200, 30))
        self.SearchText.setObjectName("SearchText")
        self.SearchResult = QtWidgets.QTableWidget(FilmCompanyDialog)
        self.SearchResult.setGeometry(QtCore.QRect(240, 20, 220, 120))
        self.SearchResult.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SearchResult.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.SearchResult.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.SearchResult.setObjectName("SearchResult")
        self.SearchResult.setColumnCount(2)
        self.SearchResult.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.SearchResult.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SearchResult.setHorizontalHeaderItem(1, item)
        self.SearchResult.horizontalHeader().setStretchLastSection(True)
        self.SearchResult.verticalHeader().setVisible(False)

        self.retranslateUi(FilmCompanyDialog)
        self.CancelButton.clicked.connect(FilmCompanyDialog.reject)
        self.OKButton.clicked.connect(FilmCompanyDialog.tryAccept)
        self.SearchText.textChanged['QString'].connect(FilmCompanyDialog.refresh)
        QtCore.QMetaObject.connectSlotsByName(FilmCompanyDialog)
        FilmCompanyDialog.setTabOrder(self.SearchText, self.SearchResult)
        FilmCompanyDialog.setTabOrder(self.SearchResult, self.OKButton)
        FilmCompanyDialog.setTabOrder(self.OKButton, self.CancelButton)

    def retranslateUi(self, FilmCompanyDialog):
        _translate = QtCore.QCoreApplication.translate
        FilmCompanyDialog.setWindowTitle(_translate("FilmCompanyDialog", "选择制作公司"))
        self.SearchLabel.setText(_translate("FilmCompanyDialog", "搜索公司名称："))
        self.OKButton.setText(_translate("FilmCompanyDialog", "确定"))
        self.CancelButton.setText(_translate("FilmCompanyDialog", "取消"))
        self.SearchText.setPlaceholderText(_translate("FilmCompanyDialog", "请输入公司名称"))
        item = self.SearchResult.horizontalHeaderItem(0)
        item.setText(_translate("FilmCompanyDialog", "公司名称"))
        item = self.SearchResult.horizontalHeaderItem(1)
        item.setText(_translate("FilmCompanyDialog", "国家/地区"))
