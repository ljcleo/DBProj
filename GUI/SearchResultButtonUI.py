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
        SearchResultButtonWidget.resize(120, 28)
        self.MovieButton = QtWidgets.QPushButton(SearchResultButtonWidget)
        self.MovieButton.setGeometry(QtCore.QRect(0, 0, 120, 28))
        self.MovieButton.setFlat(True)
        self.MovieButton.setObjectName("MovieButton")

        self.retranslateUi(SearchResultButtonWidget)
        self.MovieButton.clicked.connect(SearchResultButtonWidget.toMovie)
        QtCore.QMetaObject.connectSlotsByName(SearchResultButtonWidget)

    def retranslateUi(self, SearchResultButtonWidget):
        _translate = QtCore.QCoreApplication.translate
        SearchResultButtonWidget.setWindowTitle(_translate("SearchResultButtonWidget", "Form"))
        self.MovieButton.setText(_translate("SearchResultButtonWidget", "电影名"))
