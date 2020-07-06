# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DBProj\GUI\SearchResultButtonUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
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
        self.MovieButton.setObjectName("MovieButton")
        self.ModifyButton = QtWidgets.QPushButton(SearchResultButtonWidget)
        self.ModifyButton.setGeometry(QtCore.QRect(40, 0, 40, 36))
        self.ModifyButton.setObjectName("ModifyButton")
        self.DeleteButton = QtWidgets.QPushButton(SearchResultButtonWidget)
        self.DeleteButton.setGeometry(QtCore.QRect(80, 0, 40, 36))
        self.DeleteButton.setObjectName("DeleteButton")

        self.retranslateUi(SearchResultButtonWidget)
        QtCore.QMetaObject.connectSlotsByName(SearchResultButtonWidget)

    def retranslateUi(self, SearchResultButtonWidget):
        _translate = QtCore.QCoreApplication.translate
        SearchResultButtonWidget.setWindowTitle(_translate("SearchResultButtonWidget", "Form"))
        self.MovieButton.setText(_translate("SearchResultButtonWidget", "查看"))
        self.ModifyButton.setText(_translate("SearchResultButtonWidget", "修改"))
        self.DeleteButton.setText(_translate("SearchResultButtonWidget", "删除"))
