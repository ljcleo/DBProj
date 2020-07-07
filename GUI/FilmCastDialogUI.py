# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\FilmCastDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FilmCastDialog(object):
    def setupUi(self, FilmCastDialog):
        FilmCastDialog.setObjectName("FilmCastDialog")
        FilmCastDialog.resize(480, 180)
        self.SearchLabel = QtWidgets.QLabel(FilmCastDialog)
        self.SearchLabel.setGeometry(QtCore.QRect(20, 20, 120, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.SearchLabel.setFont(font)
        self.SearchLabel.setObjectName("SearchLabel")
        self.OKButton = QtWidgets.QPushButton(FilmCastDialog)
        self.OKButton.setGeometry(QtCore.QRect(20, 130, 90, 30))
        self.OKButton.setDefault(True)
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(FilmCastDialog)
        self.CancelButton.setGeometry(QtCore.QRect(130, 130, 90, 30))
        self.CancelButton.setObjectName("CancelButton")
        self.SearchText = QtWidgets.QLineEdit(FilmCastDialog)
        self.SearchText.setGeometry(QtCore.QRect(20, 50, 200, 30))
        self.SearchText.setObjectName("SearchText")
        self.SearchResult = QtWidgets.QTableWidget(FilmCastDialog)
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
        self.RoleLabel = QtWidgets.QLabel(FilmCastDialog)
        self.RoleLabel.setGeometry(QtCore.QRect(20, 90, 40, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        self.RoleLabel.setFont(font)
        self.RoleLabel.setObjectName("RoleLabel")
        self.Role = QtWidgets.QLineEdit(FilmCastDialog)
        self.Role.setGeometry(QtCore.QRect(70, 90, 150, 30))
        self.Role.setObjectName("Role")

        self.retranslateUi(FilmCastDialog)
        self.CancelButton.clicked.connect(FilmCastDialog.reject)
        self.OKButton.clicked.connect(FilmCastDialog.tryAccept)
        self.SearchText.textChanged['QString'].connect(FilmCastDialog.refresh)
        self.SearchResult.cellClicked['int','int'].connect(FilmCastDialog.openLink)
        QtCore.QMetaObject.connectSlotsByName(FilmCastDialog)
        FilmCastDialog.setTabOrder(self.SearchText, self.SearchResult)
        FilmCastDialog.setTabOrder(self.SearchResult, self.Role)
        FilmCastDialog.setTabOrder(self.Role, self.OKButton)
        FilmCastDialog.setTabOrder(self.OKButton, self.CancelButton)

    def retranslateUi(self, FilmCastDialog):
        _translate = QtCore.QCoreApplication.translate
        FilmCastDialog.setWindowTitle(_translate("FilmCastDialog", "选择电影演员"))
        self.SearchLabel.setText(_translate("FilmCastDialog", "搜索演员姓名："))
        self.OKButton.setText(_translate("FilmCastDialog", "确定"))
        self.CancelButton.setText(_translate("FilmCastDialog", "取消"))
        self.SearchText.setPlaceholderText(_translate("FilmCastDialog", "请输入演员姓名"))
        item = self.SearchResult.horizontalHeaderItem(0)
        item.setText(_translate("FilmCastDialog", "演员姓名"))
        item = self.SearchResult.horizontalHeaderItem(1)
        item.setText(_translate("FilmCastDialog", "豆瓣链接"))
        self.RoleLabel.setText(_translate("FilmCastDialog", "角色"))
        self.Role.setPlaceholderText(_translate("FilmCastDialog", "请输入演员角色"))
