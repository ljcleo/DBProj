# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\FilmGenreDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FilmGenreDialog(object):
    def setupUi(self, FilmGenreDialog):
        FilmGenreDialog.setObjectName("FilmGenreDialog")
        FilmGenreDialog.resize(300, 180)
        self.SearchLabel = QtWidgets.QLabel(FilmGenreDialog)
        self.SearchLabel.setGeometry(QtCore.QRect(20, 20, 120, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.SearchLabel.setFont(font)
        self.SearchLabel.setObjectName("SearchLabel")
        self.OKButton = QtWidgets.QPushButton(FilmGenreDialog)
        self.OKButton.setGeometry(QtCore.QRect(20, 90, 120, 30))
        self.OKButton.setDefault(True)
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(FilmGenreDialog)
        self.CancelButton.setGeometry(QtCore.QRect(20, 130, 120, 30))
        self.CancelButton.setObjectName("CancelButton")
        self.SearchText = QtWidgets.QLineEdit(FilmGenreDialog)
        self.SearchText.setGeometry(QtCore.QRect(20, 50, 120, 30))
        self.SearchText.setObjectName("SearchText")
        self.SearchResult = QtWidgets.QTableWidget(FilmGenreDialog)
        self.SearchResult.setGeometry(QtCore.QRect(160, 20, 120, 140))
        self.SearchResult.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SearchResult.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.SearchResult.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.SearchResult.setObjectName("SearchResult")
        self.SearchResult.setColumnCount(1)
        self.SearchResult.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.SearchResult.setHorizontalHeaderItem(0, item)
        self.SearchResult.horizontalHeader().setStretchLastSection(True)
        self.SearchResult.verticalHeader().setVisible(False)

        self.retranslateUi(FilmGenreDialog)
        self.CancelButton.clicked.connect(FilmGenreDialog.reject)
        self.OKButton.clicked.connect(FilmGenreDialog.tryAccept)
        self.SearchText.textChanged['QString'].connect(FilmGenreDialog.refresh)
        QtCore.QMetaObject.connectSlotsByName(FilmGenreDialog)
        FilmGenreDialog.setTabOrder(self.SearchText, self.SearchResult)
        FilmGenreDialog.setTabOrder(self.SearchResult, self.OKButton)
        FilmGenreDialog.setTabOrder(self.OKButton, self.CancelButton)

    def retranslateUi(self, FilmGenreDialog):
        _translate = QtCore.QCoreApplication.translate
        FilmGenreDialog.setWindowTitle(_translate("FilmGenreDialog", "选择电影分类"))
        self.SearchLabel.setText(_translate("FilmGenreDialog", "搜索分类："))
        self.OKButton.setText(_translate("FilmGenreDialog", "确定"))
        self.CancelButton.setText(_translate("FilmGenreDialog", "取消"))
        self.SearchText.setPlaceholderText(_translate("FilmGenreDialog", "请输入分类名称"))
        item = self.SearchResult.horizontalHeaderItem(0)
        item.setText(_translate("FilmGenreDialog", "分类"))
