# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\FilmDirectorDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FilmDirectorDialog(object):
    def setupUi(self, FilmDirectorDialog):
        FilmDirectorDialog.setObjectName("FilmDirectorDialog")
        FilmDirectorDialog.resize(480, 180)
        self.SearchLabel = QtWidgets.QLabel(FilmDirectorDialog)
        self.SearchLabel.setGeometry(QtCore.QRect(20, 20, 120, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.SearchLabel.setFont(font)
        self.SearchLabel.setObjectName("SearchLabel")
        self.OKButton = QtWidgets.QPushButton(FilmDirectorDialog)
        self.OKButton.setGeometry(QtCore.QRect(20, 130, 90, 30))
        self.OKButton.setDefault(True)
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(FilmDirectorDialog)
        self.CancelButton.setGeometry(QtCore.QRect(130, 130, 90, 30))
        self.CancelButton.setObjectName("CancelButton")
        self.SearchText = QtWidgets.QLineEdit(FilmDirectorDialog)
        self.SearchText.setGeometry(QtCore.QRect(20, 50, 200, 30))
        self.SearchText.setObjectName("SearchText")
        self.SearchResult = QtWidgets.QTableWidget(FilmDirectorDialog)
        self.SearchResult.setGeometry(QtCore.QRect(240, 20, 220, 140))
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
        self.RoleLabel = QtWidgets.QLabel(FilmDirectorDialog)
        self.RoleLabel.setGeometry(QtCore.QRect(20, 90, 80, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.RoleLabel.setFont(font)
        self.RoleLabel.setObjectName("RoleLabel")
        self.Role = QtWidgets.QLineEdit(FilmDirectorDialog)
        self.Role.setGeometry(QtCore.QRect(100, 90, 120, 30))
        self.Role.setObjectName("Role")

        self.retranslateUi(FilmDirectorDialog)
        self.CancelButton.clicked.connect(FilmDirectorDialog.reject)
        self.OKButton.clicked.connect(FilmDirectorDialog.tryAccept)
        self.SearchText.textChanged['QString'].connect(FilmDirectorDialog.refresh)
        self.SearchResult.cellClicked['int','int'].connect(FilmDirectorDialog.openLink)
        QtCore.QMetaObject.connectSlotsByName(FilmDirectorDialog)
        FilmDirectorDialog.setTabOrder(self.SearchText, self.SearchResult)
        FilmDirectorDialog.setTabOrder(self.SearchResult, self.Role)
        FilmDirectorDialog.setTabOrder(self.Role, self.OKButton)
        FilmDirectorDialog.setTabOrder(self.OKButton, self.CancelButton)

    def retranslateUi(self, FilmDirectorDialog):
        _translate = QtCore.QCoreApplication.translate
        FilmDirectorDialog.setWindowTitle(_translate("FilmDirectorDialog", "选择电影导演"))
        self.SearchLabel.setText(_translate("FilmDirectorDialog", "搜索导演姓名："))
        self.OKButton.setText(_translate("FilmDirectorDialog", "确定"))
        self.CancelButton.setText(_translate("FilmDirectorDialog", "取消"))
        self.SearchText.setPlaceholderText(_translate("FilmDirectorDialog", "请输入导演姓名"))
        item = self.SearchResult.horizontalHeaderItem(0)
        item.setText(_translate("FilmDirectorDialog", "导演姓名"))
        item = self.SearchResult.horizontalHeaderItem(1)
        item.setText(_translate("FilmDirectorDialog", "豆瓣链接"))
        self.RoleLabel.setText(_translate("FilmDirectorDialog", "执导/编剧"))
        self.Role.setPlaceholderText(_translate("FilmDirectorDialog", "请输入导演职务"))
