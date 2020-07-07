# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchResultPartUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchResultPart(object):
    def setupUi(self, SearchResultPart):
        SearchResultPart.setObjectName("SearchResultPart")
        SearchResultPart.resize(960, 640)
        self.SearchResultFrame = QtWidgets.QFrame(SearchResultPart)
        self.SearchResultFrame.setGeometry(QtCore.QRect(250, 200, 701, 411))
        self.SearchResultFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SearchResultFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SearchResultFrame.setObjectName("SearchResultFrame")
        self.tableWidget = QtWidgets.QTableWidget(self.SearchResultFrame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 681, 361))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.AddMovie = QtWidgets.QPushButton(self.SearchResultFrame)
        self.AddMovie.setGeometry(QtCore.QRect(582, 5, 107, 28))
        self.AddMovie.setObjectName("AddMovie")
        self.SetSearch = QtWidgets.QPushButton(self.SearchResultFrame)
        self.SetSearch.setGeometry(QtCore.QRect(10, 5, 107, 28))
        self.SetSearch.setObjectName("SetSearch")
        self.DefaultSort = QtWidgets.QPushButton(self.SearchResultFrame)
        self.DefaultSort.setGeometry(QtCore.QRect(124, 5, 108, 28))
        self.DefaultSort.setObjectName("DefaultSort")
        self.DateSortDesc = QtWidgets.QPushButton(self.SearchResultFrame)
        self.DateSortDesc.setGeometry(QtCore.QRect(239, 5, 107, 28))
        self.DateSortDesc.setObjectName("DateSortDesc")
        self.ReturnRecommendation = QtWidgets.QPushButton(self.SearchResultFrame)
        self.ReturnRecommendation.setGeometry(QtCore.QRect(467, 5, 108, 28))
        self.ReturnRecommendation.setObjectName("ReturnRecommendation")
        self.RateSortDesc = QtWidgets.QPushButton(self.SearchResultFrame)
        self.RateSortDesc.setGeometry(QtCore.QRect(353, 5, 107, 28))
        self.RateSortDesc.setObjectName("RateSortDesc")
        self.RateSortAsc = QtWidgets.QPushButton(self.SearchResultFrame)
        self.RateSortAsc.setGeometry(QtCore.QRect(353, 5, 107, 28))
        self.RateSortAsc.setObjectName("RateSortAsc")
        self.DateSortAsc = QtWidgets.QPushButton(self.SearchResultFrame)
        self.DateSortAsc.setGeometry(QtCore.QRect(239, 5, 107, 28))
        self.DateSortAsc.setObjectName("DateSortAsc")

        self.retranslateUi(SearchResultPart)
        self.SetSearch.clicked.connect(SearchResultPart.setSearch)
        self.DefaultSort.clicked.connect(SearchResultPart.sortDefault)
        self.DateSortDesc.clicked.connect(SearchResultPart.sortByDateDesc)
        self.RateSortDesc.clicked.connect(SearchResultPart.sortByRateDesc)
        self.ReturnRecommendation.clicked.connect(SearchResultPart.returnRecommendation)
        self.AddMovie.clicked.connect(SearchResultPart.addMovie)
        self.DateSortAsc.clicked.connect(SearchResultPart.sortByDateAsc)
        self.RateSortAsc.clicked.connect(SearchResultPart.sortByRateAsc)
        QtCore.QMetaObject.connectSlotsByName(SearchResultPart)

    def retranslateUi(self, SearchResultPart):
        _translate = QtCore.QCoreApplication.translate
        SearchResultPart.setWindowTitle(_translate("SearchResultPart", "搜索结果"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SearchResultPart", "片名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SearchResultPart", "国家"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SearchResultPart", "上映时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SearchResultPart", "分类"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SearchResultPart", "评分"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SearchResultPart", "操作"))
        self.AddMovie.setText(_translate("SearchResultPart", "添加电影"))
        self.SetSearch.setText(_translate("SearchResultPart", "高级搜索"))
        self.DefaultSort.setText(_translate("SearchResultPart", "默认排序"))
        self.DateSortDesc.setText(_translate("SearchResultPart", "上映时间降序"))
        self.ReturnRecommendation.setText(_translate("SearchResultPart", "返回首页"))
        self.RateSortDesc.setText(_translate("SearchResultPart", "评分降序"))
        self.RateSortAsc.setText(_translate("SearchResultPart", "评分升序"))
        self.DateSortAsc.setText(_translate("SearchResultPart", "上映时间升序"))
