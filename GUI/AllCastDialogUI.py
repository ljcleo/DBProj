# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AllCastDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AllCastDialog(object):
    def setupUi(self, AllCastDialog):
        AllCastDialog.setObjectName("AllCastDialog")
        AllCastDialog.resize(640, 480)
        self.tableWidget = QtWidgets.QTableWidget(AllCastDialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 640, 400))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.ReturnButton = QtWidgets.QPushButton(AllCastDialog)
        self.ReturnButton.setGeometry(QtCore.QRect(270, 430, 93, 28))
        self.ReturnButton.setObjectName("ReturnButton")

        self.retranslateUi(AllCastDialog)
        self.ReturnButton.clicked.connect(AllCastDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AllCastDialog)

    def retranslateUi(self, AllCastDialog):
        _translate = QtCore.QCoreApplication.translate
        AllCastDialog.setWindowTitle(_translate("AllCastDialog", "所有演员"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("AllCastDialog", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("AllCastDialog", "新建行"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AllCastDialog", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AllCastDialog", "照片"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AllCastDialog", "饰演角色"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AllCastDialog", "豆瓣链接"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("AllCastDialog", "A"))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("AllCastDialog", "B"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.ReturnButton.setText(_translate("AllCastDialog", "返回"))