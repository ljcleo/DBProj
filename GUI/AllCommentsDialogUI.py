# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AllCommentsDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AllComments(object):
    def setupUi(self, AllComments):
        AllComments.setObjectName("AllComments")
        AllComments.resize(640, 480)
        self.tableWidget = QtWidgets.QTableWidget(AllComments)
        self.tableWidget.setGeometry(QtCore.QRect(5, 40, 630, 390))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.Return = QtWidgets.QPushButton(AllComments)
        self.Return.setGeometry(QtCore.QRect(275, 440, 90, 28))
        self.Return.setAutoDefault(False)
        self.Return.setObjectName("Return")
        self.Label = QtWidgets.QLabel(AllComments)
        self.Label.setGeometry(QtCore.QRect(250, 5, 140, 30))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Label.setFont(font)
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setObjectName("Label")

        self.retranslateUi(AllComments)
        self.Return.clicked.connect(AllComments.accept)
        QtCore.QMetaObject.connectSlotsByName(AllComments)

    def retranslateUi(self, AllComments):
        _translate = QtCore.QCoreApplication.translate
        AllComments.setWindowTitle(_translate("AllComments", "评论信息"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AllComments", "新建列"))
        self.Return.setText(_translate("AllComments", "返回"))
        self.Label.setText(_translate("AllComments", "我的评论"))
