# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchResultButtonUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchResultButtonWidget(object):
    def setupUi(self, SearchResultButtonWidget):
        SearchResultButtonWidget.setObjectName("SearchResultButtonWidget")
        SearchResultButtonWidget.resize(120, 36)
        SearchResultButtonWidget.setStyleSheet("text-align: left;")
        self.MovieButton = QtWidgets.QPushButton(SearchResultButtonWidget)
        self.MovieButton.setGeometry(QtCore.QRect(0, 0, 40, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.MovieButton.setFont(font)
        self.MovieButton.setStyleSheet("text-align: left")
        self.MovieButton.setFlat(False)
        self.MovieButton.setObjectName("MovieButton")
        self.ModifyButton = QtWidgets.QPushButton(SearchResultButtonWidget)
        self.ModifyButton.setGeometry(QtCore.QRect(40, 0, 40, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.ModifyButton.setFont(font)
        self.ModifyButton.setStyleSheet("text-align: left")
        self.ModifyButton.setFlat(False)
        self.ModifyButton.setObjectName("ModifyButton")
        self.DeleteButton = QtWidgets.QPushButton(SearchResultButtonWidget)
        self.DeleteButton.setGeometry(QtCore.QRect(80, 0, 40, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.DeleteButton.setFont(font)
        self.DeleteButton.setStyleSheet("text-align: left")
        self.DeleteButton.setFlat(False)
        self.DeleteButton.setObjectName("DeleteButton")

        self.retranslateUi(SearchResultButtonWidget)
        self.MovieButton.clicked.connect(SearchResultButtonWidget.toMovie)
        self.ModifyButton.clicked.connect(SearchResultButtonWidget.modifyMovie)
        self.DeleteButton.clicked.connect(SearchResultButtonWidget.deleteMovie)
        QtCore.QMetaObject.connectSlotsByName(SearchResultButtonWidget)

    def retranslateUi(self, SearchResultButtonWidget):
        _translate = QtCore.QCoreApplication.translate
        SearchResultButtonWidget.setWindowTitle(_translate("SearchResultButtonWidget", "Form"))
        self.MovieButton.setText(_translate("SearchResultButtonWidget", "查看"))
        self.ModifyButton.setText(_translate("SearchResultButtonWidget", "修改"))
        self.DeleteButton.setText(_translate("SearchResultButtonWidget", "删除"))
