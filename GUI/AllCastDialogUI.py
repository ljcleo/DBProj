# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\AllCastDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
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
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.ReturnButton = QtWidgets.QPushButton(AllCastDialog)
        self.ReturnButton.setGeometry(QtCore.QRect(270, 430, 93, 28))
        self.ReturnButton.setObjectName("ReturnButton")

        self.retranslateUi(AllCastDialog)
        self.ReturnButton.clicked.connect(AllCastDialog.reject)
        self.tableWidget.cellClicked['int','int'].connect(AllCastDialog.visitAltAtCell)
        QtCore.QMetaObject.connectSlotsByName(AllCastDialog)

    def retranslateUi(self, AllCastDialog):
        _translate = QtCore.QCoreApplication.translate
        AllCastDialog.setWindowTitle(_translate("AllCastDialog", "所有演员"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AllCastDialog", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AllCastDialog", "饰演角色"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AllCastDialog", "豆瓣链接"))
        self.ReturnButton.setText(_translate("AllCastDialog", "返回"))
