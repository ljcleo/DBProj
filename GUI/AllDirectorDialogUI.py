# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DBProj\GUI\AllDirectorDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AllDirectorDialog(object):
    def setupUi(self, AllDirectorDialog):
        AllDirectorDialog.setObjectName("AllDirectorDialog")
        AllDirectorDialog.resize(640, 480)
        self.tableWidget = QtWidgets.QTableWidget(AllDirectorDialog)
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
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.ReturnButton = QtWidgets.QPushButton(AllDirectorDialog)
        self.ReturnButton.setGeometry(QtCore.QRect(270, 430, 93, 28))
        self.ReturnButton.setObjectName("ReturnButton")

        self.retranslateUi(AllDirectorDialog)
        self.ReturnButton.clicked.connect(AllDirectorDialog.reject)
        self.tableWidget.cellClicked['int','int'].connect(AllDirectorDialog.visitAltAtCell)
        QtCore.QMetaObject.connectSlotsByName(AllDirectorDialog)

    def retranslateUi(self, AllDirectorDialog):
        _translate = QtCore.QCoreApplication.translate
        AllDirectorDialog.setWindowTitle(_translate("AllDirectorDialog", "所有导演"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AllDirectorDialog", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AllDirectorDialog", "导演/编剧"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("AllDirectorDialog", "豆瓣链接"))
        self.ReturnButton.setText(_translate("AllDirectorDialog", "返回"))
